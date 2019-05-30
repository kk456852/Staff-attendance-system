from flask import Blueprint, json, jsonify, request, current_app
from .util import failed, login_required, success, Role
from ..model import Overtime


bp = Blueprint('tempovertimes', __name__, url_prefix='tempovertimes')


bp.route('/',methods = ['POST','GET'])
def tempovertimes_():
    try:
        if request.method == 'POST':
            pass
        elif request.method == 'GET':
            pass
        return success(request.method) 
    except  Exception as e: 
        current_app.logger.exception(e)
        return failed()



bp.route('/<int:id>',methods = ['PUT','DELLETE'])
def tempovertimes__():
    try:
        if request.method == 'PUT':
            pass
        elif request.method == 'DELETE':
            pass
        return success(request.method)
    except  Exception as e: 
        current_app.logger.exception(e)
        return failed()