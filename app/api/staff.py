from flask import Blueprint, json, jsonify, request, current_app

from ..model import User
from .util import failed, login_required, success, Role, url

bp = Blueprint('staffs', __name__, url_prefix='/staffs')


@bp.route('/', methods=['GET'])
@url
def all_staffs():
    # login_required(role=Role.MANAGER)
    return success([x.dict() for x in User.All() if x.role is not Role.MANAGER])


@bp.route('/', methods=['POST'])
@url
def new_staff():
    # login_required(role=Role.MANAGER)
    User.new(User.format_str(request.get_json()))
    return success()


@bp.route('/<int:ID>', methods=['DELETE', 'PUT'])
@url
def change_staff(ID):
    if request.method == 'PUT':
        # login_required(ID=ID, role=Role.MANAGER)
        current_app.logger.debug(request.get_json())
        User.ByID(ID).update(User.format_str(request.get_json()))
        return success()

    elif request.method == 'DELETE':
        # login_required(role=Role.MANAGER)
        User.delete(User.ByID(ID))
        return success()


@bp.route('/<int:ID>', methods=['GET'])
@url
def get_staff(ID):
    return success(User.ByID(ID).dict())
