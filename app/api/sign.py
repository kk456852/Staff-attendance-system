from flask import Blueprint, json, jsonify, request, current_app
from .util import failed, success, Role
from ..model import SignSheet


bp = Blueprint('sign', __name__, url_prefix='sign')


bp.route('/',methods = ['POST'])
def tempovertimes_():
    try:
        '''签到操作'''
        return success(request.method)
    except  Exception as e: 
        current_app.logger.exception(e)
        return failed()
 