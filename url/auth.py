from flask import Blueprint,request,session,json,redirect,url_for
from model import User
bp = Blueprint('auth',__name__,url_prefix='/auth')


@bp.route('/',methods = ('GET','POST'))
def log_Index():
    return "This is auth index page!"

@bp.route('/login',method = ('POST'))
def login():
    user = User(request.Userid,request.Password)
    if user.login() is "success":
        try:
            session[request.Userid] = user.isManager
        except:
            return {
                'result': True,
                'status': 201  #账户已登陆，返回到相应页面
            }
        return {
            'result' :  True,
            'status' :  200
        }
    else :
        return {
            'result': False,
            'status': 500    #错误代码给与区分，例如账号不存在或者密码不对
        }

@bp.route('/logout',methods = ('GET','POST'))
def logout():

    session.pop(request.form['user_id'], None)
    return redirect(url_for(log_Index))


def loged_Veri(id = None):
    #检查会话是否存在，不存在跳转到log_index界面
    #返回身份ID  0：普通员工， 1：主管   2：经理
    return id