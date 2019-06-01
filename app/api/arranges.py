from flask import Blueprint, json, jsonify, request, current_app

from ..model import WorkArrangement
from .util import failed, login_required, success, Role

bp = Blueprint('arranges', __name__, url_prefix='/arranges')


@bp.route('/', methods=['GET','POST','PUT'])
# @login_required(Role.Manager)
def arranges():
    try:
        if request.method == 'GET':
            departmentid = request.args.get('departmentID')
            return success("根据部门ID查询部门工作安排")
        elif request.method == 'POST':
            return success("主管更改部门工作安排")
        elif request.method == 'PUTq':
            staff_id = request.args.get('staffID')
            date = request.args.get('date')
            return success("根据员工ID和日期查询工作安排")
    except Exception as e:
        current_app.logger.exception(e)
        return failed()
