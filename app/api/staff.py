from flask import Blueprint, json, jsonify, request, current_app

from ..model import User
from .util import failed, login_required, success, Role, url

bp = Blueprint('staffs', __name__, url_prefix='/staffs')


@bp.route('/', methods=['GET'])
@url
def all_staffs():
    # login_required(role=Role.MANAGER)
    return success({
        "staffs": [x.dict() for x in User.All() if x.role is not Role.MANAGER]
    })


@bp.route('/<int:ID>', methods=['POST', 'DELETE', 'PUT'])
@url
def staff_info(ID):
    if request.method == 'POST':
        U = User.ByID(ID).update(request.get_json())
        return success()
    elif request.method == 'PUT':
        u = User.ByID(ID).update(request.get_json())
        return success()
    elif request.method == 'DELETE':
        User.delete_db(User.ByID(ID))
        return success()


@bp.route('/<int:ID>', methods=['GET'])
@url
def staff_info_(ID):
    return success(User.ByID(ID).dict())
