from flask import Blueprint, request, session, json, redirect, url_for,jsonify
from app.model import User
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/', methods=('GET', 'POST'))
def log_Index():
    return "This is auth index page!"


@bp.route('/login', methods=['POST'])
def login():
    request_data = json.loads(str(request.get_data(), 'utf-8'))
    user = User(request_data['UserId'], request_data['password'])
    if user.login() is "success":
        session[request_data['UserId']] = user.isManager()
        response_data = {
            'status': 20000,
            'data': {}
        }
    else:
        response_data = {
            'status': 50000,
            'data': {}
        }
    response_data = jsonify(response_data)
    return response_data


@bp.route('/logout', methods=['GET'])
def logout():
    request_data = json.loads(str(request.get_data(), 'utf-8'))
    session.pop(request_data['UserId'], None)
    response_data = {
        'status': 20000,
        'data': {}
    }
    response_data = jsonify(response_data)
    return response_data


def loged_Veri(id=None):
    # 检查会话是否存在，不存在跳转到log_index界面
    # 返回身份ID  0：普通员工， 1：主管   2：经理 3:未查询到
    try:
        result = session[str(id)]
    except BaseException:
        result = 3
    return result
