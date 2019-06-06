from flask import Blueprint, json, jsonify, request, current_app
from .. import BaseModel
from ..model import WorkArrangement
from .util import failed, url, success, Role

bp = Blueprint('arranges', __name__, url_prefix='/arranges')


@bp.route('/', methods=['GET', 'POST', 'PUT'])
@url
def arranges():
    if request.method == 'GET':#根据ID查看
        staffID = request.args.get('staffID')
        staffArrengement = WorkArrangement.ByID(staffID)
        return success(staffArrengement.dict())
    elif request.method == 'POST':#主管更改某员工的工作安排
        info = request.get_json()
        w = WorkArrangement.ByID(info['staffId'])
        w.update(info)
        return success("主管更改某员工的工作安排")

