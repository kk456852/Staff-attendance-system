from flask import Blueprint, json, jsonify, request, current_app
from .util import failed, success, Role, url
from ..model import SignSheet


bp = Blueprint('sign', __name__, url_prefix='/sign')


@bp.route('/', methods=['POST'])
@url
def tempovertimes_():
    """签到操作"""
    return success(request.method)
