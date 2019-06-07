from functools import wraps

from flask import jsonify, session, current_app

from ..model import Role, User
from ..exceptions import NoPermissionError, RequestError, NoLoginError


def success(args={}):
    return jsonify({
        "status": 20000,
        "data": args
    })


def failed(reason=50000, message=""):
    return jsonify({
        "status": reason,
        "message": message
    })


def url(method):
    """对于每一个URL的请求访问装饰器，在出错时返回对应的信息"""

    @wraps(method)
    def error_handler(*args, **kwargs):
        try:
            return success(method(*args, **kwargs))
        except RequestError as r:
            current_app.logger.exception(r)

            # 返回对应异常类的字符串文档
            return failed(reason=r.err_num(), message=r.err_msg())
        except Exception as e:
            current_app.logger.exception(e)
            return failed()

    return error_handler


def current_role():
    """返回当前登录用户的角色

    如果没有登录，抛出一个异常

    :raise NoLoginError
    :return role : Role
    """
    role = session['role']
    if not role:
        raise NoLoginError
    return role


def current_user() -> User:
    if session['id']:
        return User.ByID(session['id'])
    else:
        raise NoLoginError


def login_required(ID=None, role=Role.STAFF):
    """要求当前登录用户有对应的权限，否则抛出异常

    需要用关键字参数调用。如果多个关键词参数都被调用时
    只有同时不满足两者时才会抛出异常。

    :param role : Role
    :param ID : int
    :raise NoPermissionError
    """

    if current_role() >= role:
        return

    if ID and session['id'] == ID:
        return

    raise NoPermissionError
