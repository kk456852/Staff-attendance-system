from flask import Blueprint, json, jsonify, request, current_app

from ..model import User
from .util import failed, login_required, success, Role

bp = Blueprint('staff', __name__, url_prefix='/staff')


@bp.route('/s', methods=['GET'])
# @login_required(Role.Manager)
def all_staffs():
    try:
        return success({
            "staffs": [x.dict() for x in User.All() if x.role is not Role.MANAGER]
        })
    except Exception as e:
        current_app.logger.exception(e)
        return failed()


@bp.route('/<int:ID>', methods=['GET'])
# @login_required(Role.Manager)
def staff_info(ID):
    try:
        return success(User.ByID(ID).dict())
    except Exception as e:
        current_app.logger.exception(e)
        return failed()


@bp.route('/<int:ID>', methods=['POST'])
# @login_required(Role.Manager)
def staff_updateinfo(ID):
    try:
        U = User.ByID(ID).update(request.get_json())
        return success()
    except Exception as e:
        current_app.logger.exception(e)
        return failed()


@bp.route('/<int:ID>', methods=['PATCH'])
def staff_index(ID):
    try:
        u = User.ByID(ID).update(request.get_json())
        return success()
    except Exception as e:
        current_app.logger.exception(e)
        return failed()


@bp.route('/<int:ID>', methods=['DELETE'])
def staff_index(ID):
    try:
        User.delete_db(User.ByID(ID))
        return success()
    except Exception as e:
        current_app.logger.exception(e)
        return failed()

@bp.route('/leave', methods=('GET', 'POST'))
def staff_leave():
    pass


@bp.route('/leaveabense', methods=('GET', 'POST'))
def staff_leave_abense():
    pass


@bp.route('/checkrecord', methods=('GET', 'POST'))
def staff_check_record():
    pass


@bp.route('/overtimeapply', methods=('GET', 'POST'))
def staff_overtime_apply():
    pass
