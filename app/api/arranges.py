from flask import Blueprint, json, jsonify, request, current_app
from .. import BaseModel
from ..model import WorkArrangement
from .util import failed, url, success, Role

bp = Blueprint('arranges', __name__, url_prefix='/arranges')


@bp.route('/director', methods=['GET', 'POST', 'PUT'])
@url
def arranges():
    if request.method == 'GET':#根据ID查看
        staffID = request.args.get('staffID')
        date = request.args.get('date')
        staffArrengement = WorkArrangement.ByStaffIDandDate(staffID, date)
        return success(staffArrengement.dict())
    elif request.method == 'POST':#主管更改某员工的工作安排
        info = request.get_json()
        w = WorkArrangement.ByID(info['staffId'])
        w.update(info)
        return success("主管更改某员工的工作安排")

@bp.route('/staff', methods=['GET', 'POST', 'PUT'])
@url
def arrangesStaff():
    if request.method == 'GET':#根据ID查看
        staffID = request.args.get('staffID')
        date = request.args.get('date')
        staffArrengement = WorkArrangement.ByStaffIDandDate(staffID, date)
        return success(staffArrengement.dict())


@bp.route('/manager', methods=['GET', 'POST', 'PUT'])
def arrangesManger():
    if request.method == 'GET':#根据ID查看
        staffID = request.args.get('staffID')
        date = request.args.get('date')
        staffArrengement = WorkArrangement.ByStaffIDandDate(staffID, date)
        return success(staffArrengement.dict())

    elif request.method == 'POST':#经理更改某员工的工作安排
        info = request.get_json()
        w = WorkArrangement.ByID(info['staffId'])
        w.update(info)
        return success("主管更改某员工的工作安排")
