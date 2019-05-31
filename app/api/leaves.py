from flask import Blueprint, json, jsonify, request, current_app

from ..model import Leave
from .util import failed, login_required, success, Role, url

bp = Blueprint('leaves', __name__, url_prefix='/leaves')


@bp.route('/', methods=['GET'])
@url
def all_leaves():
    return success("请假查看")


@bp.route('/<int:ID>', methods=['PUT'])
@url
def leave_apply(ID):
    return success("请假申请")
