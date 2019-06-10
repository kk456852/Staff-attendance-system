from flask import Blueprint, json, jsonify, request, current_app
from .. import BaseModel
from ..model import WorkArrangement
from .util import failed, url, success, Role

bp = Blueprint('arranges', __name__, url_prefix='/arranges')


@bp.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
@url
def arranges():
    if request.method == 'GET':#根据ID查看
        staffID = request.args.get('staffID')
        date = request.args.get('date')
        staffArrengement = WorkArrangement.ByStaffIDandDate(staffID, date)[0]
        return success(staffArrengement.dict())
    elif request.method == 'POST':#更改某员工的工作安排
        info = request.get_json()
        w = WorkArrangement.ByStaffIDandDate(info['staffID'], info['date'])[0]
        w.update(info)
        w.update_db()
        return success(" ")
    elif request.method == 'DELETE':#增加某员工的工作安排
        w = WorkArrangement.ByStaffIDandDate(info['staffID'],info['date'])[0]
        w.delete()
        return success(" ")




