from flask import Blueprint,request,session,json,redirect,url_for
from model.User import User
bp = Blueprint('auth',__name__,url_prefix='/auth')


@bp.route('/',methods = ('GET','POST'))
def log_Index():
    return "This is auth index page!"

@bp.route('/login',methods = ('GET','POST'))
def login():
    request_data = json.loads(str(request.get_data(),'utf-8'))
    user = User(request_data['UserId'],request_data['password'])
    if user.login() is "success":
        try:
            session[request.Userid] = user.isManager
        except:
            response_data = {
                'result': True,
                'status': 201  #账户之前已登陆，返回到相应页面
            }
            response_data = json.dumps(response_data)
            return response_data
        response_data = {
            'result': True, #正常登陆
            'status': 200
        }
        response_data = json.dumps(response_data)
        return response_data
    else :
        response_data = {
            'result': False,# 登陆失败
            'status': 500
        }
        response_data = json.dumps(response_data)
        return response_data

@bp.route('/logout',methods = ('GET','POST'))
def logout():
    request_data = json.loads(str(request.get_data(), 'utf-8'))
    try:
        session.pop(request_data['UserId'], None)
        response_data = {
            'result': True,
            'status': 202
        }
        #退出登陆成功
    except:
        response_data = {
            'result' : False,
            'status' : 501 #退出登陆失败
        }
    response_data = json.dumps(response_data)
    return response_data


def loged_Veri(id = None):
    #检查会话是否存在，不存在跳转到log_index界面
    #返回身份ID  0：普通员工， 1：主管   2：经理 3:未查询到
    try :
        result = session[id]
    except:
        result = 3
    return result