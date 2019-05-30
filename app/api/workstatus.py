from flask import Blueprint, json, jsonify, request, current_app

from ..model import User
from .util import failed, login_required, success, Role

bp = Blueprint('workstatus', __name__, url_prefix='/workstatus')


@bp.route('/', methods=['GET'])
# @login_required(Role.Manager)
def all_staffs_worktatus():
    try:
        from_ = request.args.get('from')
        to_ = request.args.get('to')
        return success(request.method)
    except Exception as e:
        current_app.logger.exception(e)
        return failed()



@bp.route('/<int:ID>', methods= ['GET'])
def staff_info_(ID):
    try:
        return success(request.method)
    except Exception as e:
        return failed()