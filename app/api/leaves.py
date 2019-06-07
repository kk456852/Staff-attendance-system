from flask import Blueprint, json, jsonify, request, current_app

from ..model import Leave, User, Department
from .util import failed, login_required, success, Role, url, current_user

bp = Blueprint('leaves', __name__, url_prefix='/leaves')


@bp.route('/', methods=['GET'])
@url
def get_leaves():
    staff_id = request.args.get('staffID')
    department_id = request.args.get('departmentID')
    charge_id = request.args.get('chargeID')
    if staff_id:
        return [l.dict() for l in User.ByID(staff_id).leaves]
    elif department_id:
        return [l.dict() for u in Department.ByID(department_id).users for l in u.leaves]
    elif charge_id:
        charge = User.ByID(charge_id)
        assert charge.role == Role.CHARGE
        return [l.to_charge() for u in charge.department.users for l in u.leaves]
    else:
        return [l.dict() for l in Leave.All()]


@bp.route('/', methods=['POST'])
@url
def new_leave():
    info = Leave.format_str(request.get_json())
    current_user().new_leave(info=info)


@bp.route('/<int:ID>', methods=['DELETE'])
@url
def delete_overtime(ID):
    """
    删除一个请假请求。

    只有当该请求没有被审批时才能由员工本人取消。
    """
    o = Leave.ByID(ID)
    if o.status == 0 and o.staff.ID == current_user().ID:
        o.delete()
    else:
        raise Exception


@bp.route('/<int:ID>', methods=['PUT'])
@url
def change_leave(ID):
    permit = request.args.get('permit')
    reject = request.args.get('reject')
    report = request.args.get('leave')
    l = Leave.ByID(ID)
    if permit:
        # login_required(role=)
        l.review(current_user(), True)
    elif reject:
        # login_required()
        l.review(current_user(), False)
    elif report:
        # login_required(ID=l.staff.ID)
        l.report()
