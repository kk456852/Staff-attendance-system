from flask import Blueprint, json, jsonify, request, current_app

from ..model import Leave
from .util import failed, login_required, success, Role

bp = Blueprint('leaves', __name__, url_prefix='/leaves')


@bp.route('/', methods=['GET'])
# @login_required(Role.Manager)
def all_leaves():
    try:
        return success("请假查看")
    except Exception as e:
        current_app.logger.exception(e)
        return failed()


@bp.route('/<int:ID>',methods = ['PUT'])
def leave_apply(ID):
    try:
        return success("请假申请")
    except Exception as e:
        current_app.logger.exception(e)
        return failed()

