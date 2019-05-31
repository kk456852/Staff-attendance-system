from flask import Blueprint, current_app, json, jsonify, request

from ..model import Overtime
from .util import Role, failed, login_required, success, url, current_role

bp = Blueprint('tempovertimes', __name__, url_prefix='/tempovertimes')


@bp.route('/', methods=['GET', 'POST'])
@url
def tempovertimes_():
    if request.method == 'POST':
        return success("经理增加一次临时加班")
    elif request.method == 'GET':
        return success("查看所有临时加班")
    return success(request.method)


@bp.route('/<int:ID>', methods=['PUT', 'DELETE'])
@url
def tempovertimes__(ID):
    if request.method == 'PUT':
        return success("经理修改一次加班活动")
    elif request.method == 'DELETE':
        return success("经理删除一次加班活动")
    return success(request.method)
