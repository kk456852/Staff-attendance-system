from flask import Blueprint, json, jsonify, request, current_app

from ..model import Overtime, User, Department
from .util import failed, login_required, success, Role, url, current_role, current_user

bp = Blueprint('overtimes', __name__, url_prefix='/overtimes')


@bp.route('/', methods=['GET'])
@url
def get_overtime():
    # login_required(Role.Manager)
    staff_id = request.args.get('staffID')
    department_id = request.args.get('departmentID')
    if staff_id:
        return success([o.dict() for o in User.ByID(staff_id).overtimes])
    elif department_id:
        return success([o.dict() for u in Department.ByID(department_id).users for o in u.overtimes])
    else:
        return success([o.dict() for o in Overtime.All()])


@bp.route('/', methods=['POST'])
@url
def new_overtime():
    info = Overtime.format_str(request.get_json())
    current_user().new_overtime(info=info)
    return success()

@bp.route('/<int:ID>', methods=['PUT'])
@url
def ovetimeByStaffId(ID):
    role = current_role()
    if role == Role.MANAGER:
        return success("主管批准加班")
    else:
        return success("员工取消申请")
    return success()
