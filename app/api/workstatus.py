from datetime import date

from flask import Blueprint, current_app, json, jsonify, request

from ..model import SignSheet, User
from .util import Role, failed, login_required, success, url

bp = Blueprint('workstatus', __name__, url_prefix='/workstatus')


@bp.route('/', methods=['GET'])
@url
def workstatus():
    """
    工作状态：

    请求：员工ID、日期

    {
        "works" : [
            {
                "type" : "normal",

            },
            {
                "type" : "overwork"
            },
            {
                "type" : "leave"
            }
        ]
    }
    """
    staff_id = request.args.get('staffID')
    work_date = date(*[int(i) for i in request.args.get('date').split('-')])
    # login_required()

    return User.ByID(staff_id).arrangement_by_date(work_date)

"""
关于工作状态：


"""
