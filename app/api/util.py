from functools import wraps

from flask import jsonify, session


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
            if session['id'] is 1:  # TODO: 修改这里，符合实际权限层次模型
                return method(*args, **kwargs)
            else:
                raise Exception
        except Exception as e:
            current_app.logger.debug(e)
            return failed()

    return check_and_do
