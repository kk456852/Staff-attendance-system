from flask import Blueprint, json, jsonify, request, current_app
from .util import failed, login_required, success, Role
from ..model import Overtime


bp = Blueprint('tempovertimes', __name__, url_prefix='/tempovertimes')


@bp.route('/', methods= ['GET','POST'])
def tempovertimes_():
    try:
        if request.method == 'POST':
            """
               实例化加班类对象，调用增加方法增加一条记录
               返回值为成功或者失败
               输入参数为{开始时间，结束时间，开始日期，结束日期}
            """
            return success("经理增加一次临时加班")
        elif request.method == 'GET':
            """
                实例化加班类对象，调用查询所有数据方法，查询所有加班信息
                返回值为字典列表[{开始时间，结束时间，开始日期，结束日期}]
            """
            return success("查看所有临时加班")
        return success(request.method) 
    except  Exception as e: 
        current_app.logger.exception(e)
        return failed()


@bp.route('/<int:ID>',methods = ['PUT','DELETE'])
def tempovertimes__(ID):
    try:
        if request.method == 'PUT':
            """
                实例化加班类对象，调用修改方法，修改加班信息
                输入参数为{overtimeID，开始时间，结束时间，开始日期，结束日期}
            """
            return success("经理修改一次加班活动")
        elif request.method == 'DELETE':
            """
                实例化加班类对象，调用删除方法，删除加班信息
                输入参数为{overtimeID}
            """
            return success("经理删除一次加班活动")
        return success(request.method)
    except Exception as e:
        current_app.logger.exception(e)
        return failed()