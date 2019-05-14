from functools import wraps

from flask import (Blueprint, current_app, json, jsonify, redirect, request,
                   session, url_for)

from app.database import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


def success(**args):
    return jsonify({
        "status": 20000,
        "data": args
    })


def failed(reason=50000):
    return jsonify({
        "status": reason,
        "data": {}
    })


def login_required(method):
    @wraps(method)
    def check_and_do(*args, **kwargs):
        try:
            if session['id'] is 1: # TODO: 修改这里，符合实际权限层次模型
                return method(*args, **kwargs)
            else:
                raise Exception
        except Exception as e:
            current_app.logger.debug(e)
            return failed()

    return check_and_do


@bp.route('/test', methods=['GET'])
@login_required
def log_Index():
    return success()


@bp.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    try:
        u = User.ByID(request_data['id'])
        u.login(request_data['password'])
        session['id'] = u.identity
        return success()
    except Exception as e:
        current_app.logger.debug(e)
        return failed(50001)


@bp.route('/logout', methods=['POST'])
def logout():
    session['id'] = None
    return success()


def loged_Veri():
    pass
