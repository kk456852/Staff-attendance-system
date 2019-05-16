from functools import wraps

from flask import jsonify, session, current_app

from ..model import Role


def success(args={}):
    return jsonify({
        "status": 20000,
        "data": args
    })


def failed(reason=50000):
    return jsonify({
        "status": reason,
        "data": {}
    })


def login_required(role=Role.STAFF):

    def check_role(method):
        @wraps(method)
        def check_and_do(*args, **kwargs):
            try:
                if session['role'] >= role:  # 高权限的可以访问低权限的
                    return method(*args, **kwargs)
                else:
                    raise Exception
            except Exception as e:
                current_app.logger.debug(e)
                return failed()

        return check_and_do
    return check_role
