from flask import Blueprint, Flask, json, request
from .auth import loged_Veri
from ..model import Manager

bp = Blueprint('manager', __name__, url_prefix='/manager')

@bp.route('/checkstaff',methods = ('GET','POST'))
def check_staff():
    request_data = json.loads(str(request.get_data(), 'utf-8'))
    if loged_Veri(request_data['UserId']) == 2:
        manager =  Manager(request_data['UserId'])
        response_data = manager.retrieve_employee()