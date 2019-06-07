from flask import (Blueprint, current_app, jsonify, redirect, request,
                   session, url_for)

from .util import url, success, failed, login_required

from ..model import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/test', methods=['GET'])
@url
def log_Index():
    login_required()


@bp.route('/login', methods=['POST'])
@url
def login():
    request_data = request.get_json()
    u = User.ByID(request_data['id'])
    u.login(request_data['password'])
    session['id'] = u.ID
    session['role'] = u.role
    return {"role": u.role.name.lower()}


@bp.route('/logout', methods=['POST'])
@url
def logout():
    session['id'] = None
    session['role'] = None
