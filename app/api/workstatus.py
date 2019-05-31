from flask import Blueprint, json, jsonify, request, current_app

from ..model import User
from .util import failed, login_required, success, Role, url

bp = Blueprint('workstatus', __name__, url_prefix='/workstatus')


@bp.route('/', methods=['GET'])
@url
def all_staffs_worktatus():
    # login_required(Role.Manager)
    from_ = request.args.get('from')
    to_ = request.args.get('to')
    return success(request.method)

@bp.route('/<int:ID>', methods=['GET'])
@url
def staff_info_(ID):
    return success(request.method)
    
