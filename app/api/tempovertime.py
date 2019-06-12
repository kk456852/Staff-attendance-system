from datetime import datetime, date, time

from flask import Blueprint, current_app, json, jsonify, request

from ..model import TemporaryOvertime
from .util import Role, failed, login_required, success, url, current_role

bp = Blueprint('tempovertimes', __name__, url_prefix='/tempovertimes')


@bp.route('/', methods=['GET'])
@url
def get_tempovertimes():
    return [x.dict() for x in TemporaryOvertime.All() if x.endTime > datetime.now()]


@bp.route('/', methods=['POST'])
@url
def new_tempovertimes():
    info = TemporaryOvertime.format_str(request.get_json())
    TemporaryOvertime.new(info)


@bp.route('/<int:ID>', methods=['PUT'])
@url
def change_tempovertimes(ID):
    info = TemporaryOvertime.format_str(request.get_json())
    TemporaryOvertime.ByID(ID).update(info)


@bp.route('/<int:ID>', methods=['DELETE'])
@url
def delete_tempovertimes(ID):
    TemporaryOvertime.ByID(ID).delete()
