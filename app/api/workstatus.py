from datetime import date, time, datetime, timedelta
from collections import defaultdict

from flask import Blueprint, current_app, json, jsonify, request

from ..model import SignSheet, User
from .util import Role, failed, login_required, success, url

bp = Blueprint('workstatus', __name__, url_prefix='/workstatus')


@bp.route('/', methods=['GET'])
@url
def workstatus():
    """
    工作情况：

    请求：员工ID、日期
    { "2019-9-9": [
        {
            "type" : "arrangement",
            "beginTime" : "10:00",
            "endTime" : "19:00",
            "pbegin" : "9:59",
            "pend" : "18:58"
        },
        {
            "type" : "overwork",
            "beginTime" : "19:00",
            "endTime" : "22:00",
            "pbegin" : "19:03",
            "pend" : "20:00"
        },
        {
            "type" : "leave",
            "beginTime" : "08:00",
            "endTime" : "10:00"
        }
    ], "2019-9-8" : [{
        "type": "leave"
        "allDay" true
    }]
    }
    """

    staff_id = request.args.get('staffID')

    from_ = request.args.get('from')
    to_ = request.args.get('to')

    dt = request.args.get('date')
    if dt:
        dt = date(*[int(i) for i in dt.split('-')])
        u = User.ByID(staff_id)

        arranges = u.arrangement_by_date(dt)
        leaves = u.leaves_by_date(dt)
        overtimes = u.overtimes_by_date(dt)

        return format_status(arranges, leaves, overtimes).get(dt.isoformat())

    elif from_ and to_:
        fm = date(*[int(i) for i in from_.split('-')])
        to = date(*[int(i) for i in to_.split('-')])
        u = User.ByID(staff_id)

        arranges = u.arrangement_by_range(fm, to)
        leaves = u.leaves_by_range(fm, to)
        overtimes = u.overtimes_by_range(fm, to)

        return format_status(arranges, leaves, overtimes)


def format_status(arranges, leaves, overtimes):
    res = defaultdict(list)

    for a in arranges:
        res[a.date.isoformat()].append(arrange_format(a))

    for o in overtimes:
        beginDate = o.beginDateTime.date()
        endDate = o.endDateTime.date()
        res[beginDate.isoformat()].append(overtime_format(o))

        if beginDate != endDate:
            res[endDate.isoformat()].append(
                overtime_format(o, nextday=True))

    for l in leaves:
        pass

    return dict(res)


def overtime_format(o, nextday=False):
    no_cross_day = o.beginDateTime.time() < o.endDateTime.time()  # 跨越一整天
    res = {
        "type": "overtime",
        "beginTime": o.beginDateTime.time(),
        "endTime": o.endDateTime.time() if no_cross_day else time.max,
        "pbeginDateTime": o.beginSign.commitStamp if o.beginSign else None,
        "pendDateTime": o.endSign.commitStamp if no_cross_day and o.endSign else None
    }
    if nextday:
        res['beginTime'] = time.min
        res['endTime'] = o.endDateTime.time()
        res['pendDateTime'] = o.endSign.commitStamp if o.endSign else None

    return res


def arrange_format(a):
    return {
        "type": "arrangement",
        "beginTime": a.beginTime,
        "endTime": a.endTime,
        "pbeginDateTime": a.beginSign.commitStamp if a.beginSign else None,
        "pendDateTime": a.endSign.commitStamp if a.endSign else None
    }
