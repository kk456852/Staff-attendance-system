from flask import Blueprint, json, jsonify, request, current_app

from ..model import Overtime
from .util import failed, login_required, success, Role

bp = Blueprint('overtimes', __name__, url_prefix='/overtimes')


@bp.route('/', methods=['GET','POST'])
# @login_required(Role.Manager)
def ovetimeByStaffId():
    try:
        if request.method == 'GET':
            staff_id = request.args.get('staffID')
            return success('按照员工ID获取加班信息成功')
        elif request.method == 'POST':
            return success("员工申请加班")
    except Exception as e:
        current_app.logger.exception(e)
        return failed()

@bp.route('/<int:ID>', methods=['PUT'])
# @login_required(Role.Manager)
def ovetimeByStaffId_(ID):
    try:
        if Role ==  3:
            return success("主管批准加班")
        elif Role == 1:
            return success("员工取消申请")
    except Exception as e:
        current_app.logger.exception(e)
        return failed()




