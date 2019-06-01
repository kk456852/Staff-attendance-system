from flask import (Blueprint, current_app, jsonify, redirect, request,
                   session, url_for)

from .util import url, success, failed, login_required

from ..model import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/test', methods=['GET'])
@url
def log_Index():
    login_required()
    return success()


@bp.route('/login', methods=['POST'])
@url
def login():
    request_data = request.get_json()
    try:
        """
           实例化User对象调用登陆验证方法进行验证
           返回成功或者失败
        """
        return success()
    except Exception as e:
        current_app.logger.exception(e)
        return failed(50001)


@bp.route('/logout', methods=['POST'])
@url
def logout():
    try:
        session['id'] = None
        session['role'] = None
        return success()
    except Exception as e:
        return failed()
