import base64
from io import BytesIO
from datetime import datetime

from flask import Blueprint, current_app, json, jsonify, request as flask_request

from ..model import SignSheet, User
from .util import Role, failed, login_required, success, url

import json
import urllib, sys,urllib.request
import ssl
from urllib import request ,parse
import requests as rq

bp = Blueprint('sign', __name__, url_prefix='/sign')


def get_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=h1f1ICQ7YjgrfzLAzLHQFEuR&client_secret=jXPBn5dZr9it2Eler7VfnsuNwvq9fiF0'
    req = urllib.request.Request(host)
    req.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(req)
    content = response.read()
    content = bytes.decode(content)
    content = eval(content[:-1])
    return content['access_token']

def imgdata(image,filepath):
    import base64
    # f = open(r'%s' %file1path,'rb')
    # pic1 =  base64.b64encode(f.read())
    # f.close()
    pic1 = image
    f = open(r'%s' %filepath,'rb')
    pic2 =  base64.b64encode(f.read())
    f.close()
    params = pic1, str(pic2,'utf-8')
    return params

def img(image,filepath,token):
    # token = get_token()
    print(token)
    
    url = 'https://aip.baidubce.com/rest/2.0/face/v3/match?access_token='+token
    f1, f2 = imgdata(image,filepath)
    
    data = [{ "image_type" : "BASE64","image" : f1},{"image_type" : "BASE64","image" : f2}]
    
    content = rq.post(url, json=data).text
    content = json.loads(content)
    # print(content)
    #获得分数
    score = content['result']['score']
    return score

def face_recognition(image):
    """

    人脸识别功能接口。接受一个图片文件，返回对应图片的用户ID。
    如果没有识别成功，抛出异常。
    """
    # score_max = 0
    url_map = { u.ID:u.image_url for u in User.All() if u.image_url  }
    token = get_token()
    for k,v in url_map.items():
        score = img(image,v,token)
        if score > 85:
            ID = k
            print(score)
            break

    return ID


@bp.route('/', methods=['POST'])
@url
def sign():
    """签到操作，此处接受一张图片。将返回人脸识别后的结果"""
    # login_required()
    data = flask_request.get_json()
    image : bytes = data['img'][22:]  # remove 'data:image/png;base64,'
    
    ID = face_recognition(image)
    SignSheet.sign(ID)
    return {"ID" : ID}


@bp.route('/<int:ID>', methods=['POST'])
@url
def sign_test(ID):
    """测试用的签到操作，可以为某个用户ID的人在某特定时间点签到"""
    data = flask_request.get_json()
    s = SignSheet(staffID=ID)
    s.commitStamp = datetime.fromtimestamp(data['DateTime'])
    s.update_db()
