from flask import Blueprint, json, jsonify, request, current_app

from ..model import Leave
from .util import failed, login_required, success, Role

bp = Blueprint('leaves', __name__, url_prefix='/leaves')


@bp.route('/all', methods=['GET'])
# @login_required(Role.Manager)
def all_leaves():
    try:
        return success()
    except Exception as e:
        current_app.logger.exception(e)
        return failed()

