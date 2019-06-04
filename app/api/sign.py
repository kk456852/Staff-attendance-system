from flask import Blueprint, json, jsonify, request, current_app
from .util import failed, success, Role, url
from ..model import SignSheet


bp = Blueprint('sign', __name__, url_prefix='/sign')


@bp.route('/', methods=['POST'])
@url
def sign():
    """签到操作，此处接受一张图片。将返回人脸识别后的结果"""
    return success(request.method)


@bp.route('/<int:ID>', methods=['POST'])
@url
def sign_test():
    """测试用的签到操作，可以为某个用户ID的人签到"""
    return success(request.method)
