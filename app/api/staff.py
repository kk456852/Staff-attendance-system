from flask import Blueprint, json, jsonify, request, current_app

from ..model import User, Department
from .util import failed, login_required, success, Role, url

bp = Blueprint('staffs', __name__, url_prefix='/staffs')


@bp.route('/', methods=['GET'])
@url
def get_staffs():
    # login_required(role=Role.MANAGER)
    dep = request.args.get('departmentID')
    if dep:
        return [x.dict() for x in Department.ByID(dep).users]
    return [x.dict() for x in User.All() if x.role is not Role.MANAGER]


@bp.route('/', methods=['POST'])
@url
def new_staff():
    # login_required(role=Role.MANAGER)
    User.new(request.get_json())


@bp.route('/<int:ID>', methods=['DELETE', 'PUT'])
@url
def change_staff(ID):
    if request.method == 'PUT':
        # login_required(ID=ID, role=Role.MANAGER)
        current_app.logger.debug(request.get_json())
        User.ByID(ID).update(request.get_json())

    elif request.method == 'DELETE':
        # login_required(role=Role.MANAGER)
        User.ByID(ID).delete()


@bp.route('/<int:ID>', methods=['GET'])
@url
def get_staff(ID):
    return User.ByID(ID).dict()
