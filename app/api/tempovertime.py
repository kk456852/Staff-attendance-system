from flask import Blueprint, json, jsonify, request, current_app
from .util import failed, login_required, success, Role
from ..model import Overtime


bp = Blueprint('tempovertimes', __name__, url_prefix='/tempovertimes')


@bp.route('/', methods= ['GET','POST'])
def tempovertimes_():
    try:
        if request.method == 'POST':
            return success("经理增加一次临时加班")
        elif request.method == 'GET':
            return success("查看所有临时加班")
        return success(request.method) 
    except  Exception as e: 
        current_app.logger.exception(e)
        return failed()



@bp.route('/<int:ID>',methods = ['PUT','DELETE'])
def tempovertimes__(ID):
    try:
        if request.method == 'PUT':
            return success("经理修改一次加班活动")
        elif request.method == 'DELETE':
            return success("经理删除一次加班活动")
        return success(request.method)
    except  Exception as e: 
        current_app.logger.exception(e)
        return failed()