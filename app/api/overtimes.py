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
        return [o.dict() for o in User.ByID(staff_id).overtimes]
    elif department_id:
        return [o.dict() for u in Department.ByID(department_id).users for o in u.overtimes]
    else:
        return [o.dict() for o in Overtime.All()]


@bp.route('/', methods=['POST'])
@url
def new_overtime():
    info = Overtime.format_str(request.get_json())
    current_user().new_overtime(info=info)


@bp.route('/<int:ID>', methods=['PUT'])
@url
def ovetimeByStaffId(ID):
    login_required(role=Role.CHARGE)


def delete_overtime(ID):
    """
    删除一个加班请求。

    只有当该加班请求没有被审批时才能由员工本人取消。
    """
    o = Overtime.ByID(ID)
    if o.status == 0 and o.staff.ID == current_user().ID:
        o.delete()
    else:
        raise Exception
