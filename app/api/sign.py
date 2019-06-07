import base64
from io import BytesIO

from flask import Blueprint, current_app, json, jsonify, request

from ..model import SignSheet
from .util import Role, failed, login_required, success, url

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
    data = request.get_json()
    x: bytes = data['img'][22:]  # remove 'data:image/png;base64,'
    b = base64.b64decode(x)
    image = None  # Image.open(BytesIO(b))  # 需要PIL库

    ID = face_recognition(image)
    SignSheet.sign(ID)


@bp.route('/<int:ID>', methods=['POST'])
@url
def sign_test(ID):
    """测试用的签到操作，可以为某个用户ID的人签到"""
    SignSheet.sign(ID)
