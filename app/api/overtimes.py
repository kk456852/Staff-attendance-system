from flask import Blueprint, json, jsonify, request, current_app

from ..model import Overtime
from .util import failed, login_required, success, Role, url, current_role

bp = Blueprint('overtimes', __name__, url_prefix='/overtimes')


@bp.route('/', methods=['GET', 'POST'])
@url
def ovetimeByStaffId():
    # login_required(Role.Manager)
    if request.method == 'GET':
        staff_id = request.args.get('staffID')
        return success('按照员工ID获取加班信息成功')
    elif request.method == 'POST':
        return success("员工申请加班")


@bp.route('/<int:ID>', methods=['PUT'])
@url
def ovetimeByStaffId_(ID):

    role = current_role()
    if role == Role.MANAGER:
        return success("主管批准加班")
    else:
        return success("员工取消申请")
    return success()
