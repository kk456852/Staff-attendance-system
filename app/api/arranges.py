from datetime import date

from flask import Blueprint, current_app, json, jsonify, request

from .. import BaseModel
from ..model import User, WorkArrangement
from .util import Role, failed, success, url

bp = Blueprint('arranges', __name__, url_prefix='/arranges')


@bp.route('/', methods=['GET'])
@url
def get_arranges():
    staff_id = request.args.get('staffID')
    work_date = date(*[int(i) for i in request.args.get('date').split('-')])
    # login_required()
    return User.ByID(staff_id).arrangement_by_date(work_date).dict()

@bp.route('/staff', methods=['GET', 'POST', 'PUT'])
@url
def arrangesStaff():
    if request.method == 'GET':#根据ID查看
        staffID = request.args.get('staffID')
        staffArrengement = WorkArrangement.ByID(staffID)
        return success(staffArrengement.dict())

@bp.route('/', methods=['POST'])
@url
def new_arranges():
    info = request.get_json()
    w = WorkArrangement.new(info)

@bp.route('/manager', methods=['GET', 'POST', 'PUT'])
def arrangesManger():
    if request.method == 'GET':#根据ID查看
        staffID = request.args.get('staffID')
        staffArrengement = WorkArrangement.ByID(staffID)
        return success(staffArrengement.dict())

@bp.route('/<int:ID>', methods=['PUT'])
@url
def change_arranges(ID):
    info = request.get_json()
    w = WorkArrangement.ByID(ID).update(info)


@bp.route('/<int:ID>', methods=['DELETE'])
@url
def cancel_arranges(ID):
    WorkArrangement.ByID(ID).delete()
