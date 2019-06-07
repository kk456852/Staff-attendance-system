from flask import Blueprint, json, jsonify, request, current_app

from ..model import WorkArrangement
from .util import failed, url, success, Role

bp = Blueprint('arranges', __name__, url_prefix='/arranges')


@bp.route('/', methods=['GET', 'POST', 'PUT'])
@url
def arranges():
    if request.method == 'GET':
        departmentid = request.args.get('departmentID')
        return "根据部门ID查询部门工作安排"
    elif request.method == 'POST':
        return "主管更改部门工作安排"
    elif request.method == 'PUT':
        staff_id = request.args.get('staffID')
        date = request.args.get('date')
        return "根据员工ID和日期查询工作安排"
