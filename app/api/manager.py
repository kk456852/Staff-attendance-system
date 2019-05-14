from flask import Blueprint, json, request
from url.auth import loged_Veri
from model import Manager
bp = Blueprint('manager', __name__, url_prefix='/manager')


@bp.route('/checkstaff', methods=('GET'))
def check_staff():
    request_data = json.loads(str(request.get_data(), 'utf-8'))
    try:
        if loged_Veri(request_data['ManageId']) == 2:
            manager = Manager(request_data['UserId'])
            response_data = manager.retrieve_employee()
            response_data = {
                'result': True,
                'status': 210,
                'data': response_data
            }
        else:
            response_data = {
                'result': False,
                'status': 510
            }
    except:
        response_data = {
            'result': False,
            'status': 511
        }
    response_data = json.dumps(response_data)
    return response_data


@bp.route('/updatestaff', methods=('PUT'))
def update_staff():
    request_data = json.loads(str(request.get_data(), 'utf-8'))
    try:
        if loged_Veri(request_data['ManagerId']) == 2:
            manager = Manager(request_data['StaffId'])
            manager.update_employee(request_data['data'])
            response_data = {
                'result': True,
                'status': 211
            }
        else:
            response_data = {
                'result': False,
                'status': 510
            }

    except:
        response_data = {
            'result': False,
            'status': 512
        }
    response_data = json.dumps(response_data)
    return response_data
