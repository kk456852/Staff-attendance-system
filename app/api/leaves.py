from flask import Blueprint, json, jsonify, request, current_app

from ..model import Leave, User, Department
from .util import failed, login_required, success, Role, url, current_user

bp = Blueprint('leaves', __name__, url_prefix='/leaves')



@bp.route('/', methods=['GET'])
@url
def get_leaves():
    staff_id = request.args.get('staffID')
    department_id = request.args.get('departmentID')
    if staff_id:
        return [o.dict() for o in User.ByID(staff_id).leaves]
    elif department_id:
        return [o.dict() for u in Department.ByID(department_id).users for o in u.leaves]
    else:
        return [o.dict() for o in Leave.All()]


@bp.route('/', methods=['POST'])
@url
def new_leave():
    info = Leave.format_str(request.get_json())
    current_user().new_leave(info=info)


@bp.route('/<int:ID>', methods=['PUT'])
@url
def leave_apply(ID):
    pass
