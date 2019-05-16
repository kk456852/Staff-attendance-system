from flask import (Blueprint, current_app, jsonify, redirect, request,
                   session, url_for)

from .util import login_required, success, failed

from ..model import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/test', methods=['GET'])
@login_required()
def log_Index():
    return success()


@bp.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    try:
        u = User.ByID(request_data['id'])
        u.login(request_data['password'])
        session['id'] = u.ID
        session['role'] = u.role
        return success()
    except Exception as e:
        current_app.logger.exception(e)
        return failed(50001)


@bp.route('/logout', methods=['POST'])
@login_required()
def logout():
    session['id'] = None
    session['role'] = None
    return success()
