from flask import Blueprint, json, request,jsonify
from app.api.auth import loged_Veri
from app.model import Manager
bp = Blueprint('manager', __name__, url_prefix='/manager')


@bp.route('/checkstaff', methods=['GET'])
def check_staff():
    request_data = json.loads(str(request.get_data(), 'utf-8'))
    if loged_Veri(request_data['UserId']) == 2:
        manager = Manager(request_data['UserId'])
        response_data = manager.retrieve_employee()
        response_data = {
            'status': 20000,
            'data': response_data
        }
    else:
        response_data = {
            'status': 50000,
            'data': {}
        }
    response_data = jsonify(response_data)
    return response_data


@bp.route('/updatestaff', methods=['PUT'])
def update_staff():
    request_data = json.loads(str(request.get_data(), 'utf-8'))
    if loged_Veri(request_data['UserId']) == 2:
        manager = Manager(request_data['UserId'])
        manager.update_employee(request_data['data'])
        response_data = {
            'status': 20000,
            'data': {}
        }
    else:
        response_data = {
            'status': 50000,
            'data': {}
        }
    response_data = jsonify(response_data)
    return response_data
