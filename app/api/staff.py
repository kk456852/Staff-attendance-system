from flask import Blueprint, json, jsonify, request, current_app

from ..model import User
from .util import failed, login_required, success, Role

bp = Blueprint('staff', __name__, url_prefix='/staff')


@bp.route('/all', methods=['GET'])
# @login_required(Role.Manager)
def all_staffs():
    try:
        return success({
            "staffs": [x.dict() for x in User.All() if x.role is not Role.MANAGER]
        })
    except Exception as e:
        current_app.logger.exception(e)
        return failed()


@bp.route('/<int:ID>', methods= ['POST','DELETE','PATCH'])
# @login_required(Role.Manager)
def staff_info(ID):
    try:
        if request.method == 'POST':
            U = User.ByID(ID).update(request.get_json())
            return success()
        elif request.method == 'PATCH':
            u = User.ByID(ID).update(request.get_json())
            return success()
        elif request.method == 'DELETE':
            User.delete_db(User.ByID(ID))
            return success()
    except Exception as e:
        current_app.logger.exception(e)
        return failed()

@bp.route('/<int:ID>', methods= ['GET'])
def staff_info_all(ID):
    try:
        return User.ByID(ID).
    except Exception as e:
        