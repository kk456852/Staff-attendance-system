from datetime import date

from flask import Blueprint, current_app, json, jsonify, request

from .. import BaseModel
from ..model import User, WorkArrangement
from .util import Role, failed, success, url

bp = Blueprint('arranges', __name__, url_prefix='/arrangements')


def format_date(date_str):
    return date(*[int(i) for i in date_str.split('-')])


@bp.route('/', methods=['GET'])
@url
def get_arranges_by_staff_date():
    staff_id = request.args.get('staffID')
    str_date = request.args.get('date')
    str_from = request.args.get('fromDateTime')


    if str_date:
        work_date = format_date(str_date)
        # login_required()
        return [a.dict() for a in User.ByID(staff_id).arrangement_by_date(work_date)]
    else :
        pass


@bp.route('/', methods=['POST'])
@url
def new_arranges():
    info = request.get_json()
    w = WorkArrangement.new(info)


@bp.route('/<int:ID>', methods=['PUT'])
@url
def change_arranges(ID):
    info = request.get_json()
    w = WorkArrangement.ByID(ID).update(info)


@bp.route('/<int:ID>', methods=['DELETE'])
@url
def cancel_arranges(ID):
    WorkArrangement.ByID(ID).delete()
