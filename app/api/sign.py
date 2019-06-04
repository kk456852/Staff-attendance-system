from flask import Blueprint, json, jsonify, request, current_app
from .util import failed, success, Role, url, login_required
from ..model import SignSheet


bp = Blueprint('sign', __name__, url_prefix='/sign')


def face_recognition(photo):
    """
    人脸识别功能接口。接受一个图片文件，返回对应图片的用户ID。
    如果没有识别成功，抛出异常。
    """
    pass

@bp.route('/', methods=['POST'])
@url
def sign():
    """签到操作，此处接受一张图片。将返回人脸识别后的结果"""
    # login_required()
    photo = request.files['photo']
    ID = face_recognition(photo)
    SignSheet.sign(ID)
    return success()


@bp.route('/<int:ID>', methods=['POST'])
@url
def sign_test(ID):
    """测试用的签到操作，可以为某个用户ID的人签到"""
    SignSheet.sign(ID)
    return success()
