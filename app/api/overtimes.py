from flask import Blueprint, json, jsonify, request, current_app

from ..model import Overtime, User, Department
from .util import failed, login_required, success, Role, url, current_role

bp = Blueprint('overtimes', __name__)


@bp.route('/overtimes', methods=['GET'])
@url
def get_overtime():
    # login_required(Role.Manager)
    staff_id = request.args.get('staffID')
    department_id = request.args.get('departmentID')
    if staff_id:
        return success([o.dict for o in User.ByID(staff_id).overtimes])
    elif department_id:
        return success([o.dict for o in u.overtimes for u in Department.ByID(department_id).users])
    else:
        return success([o.dict for o in Overtime.All()])


@bp.route('/overtimes', methods=['POST'])
@url
def new_overtime():
    pass


@bp.route('/overtimes/<int:ID>', methods=['PUT'])
@url
def ovetimeByStaffId(ID):

    role = current_role()
    if role == Role.MANAGER:
        return success("主管批准加班")
    else:
        return success("员工取消申请")
    return success()
