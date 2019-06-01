from flask import Blueprint, json, jsonify, request, current_app

from ..model import Leave
from .util import failed, login_required, success, Role, url

bp = Blueprint('leaves', __name__, url_prefix='/leaves')


@bp.route('/', methods=['GET'])
@url
def all_leaves():
    try:
        return success("经理查看所有请假信息")
    except Exception as e:
        current_app.logger.exception(e)
        return failed()


@bp.route('/<int:ID>',methods = ['PUT','GET'])
def leave_apply(ID):
    try:
        if request.method == 'PUT':
            return success("员工申请请假")
        elif request.method == 'GET':
            return success("员工查看请假申请状态")
    except Exception as e:
        current_app.logger.exception(e)
        return failed()




