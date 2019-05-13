from flask import Blueprint,request,session,json,redirect,url_for

bp = Blueprint('auth',__name__,url_prefix='/auth')


@bp.route('/',methods = ('GET','POST'))
def log_Index():
    return "This is auth index page!"

@bp.route('/login',methods = ('GET','POST'))
def login():
    #数据库验证
    # if db.id_auth == True :
    #     session[request.form['user_id']] = True
    #     result_response = {'result':True,'status':200}
    # else:
    #     result_response = {'result':False, 'stat
    # 验证成功与否返回JSON信息us': 500}
    # 验证失败回转到登陆页面
    # return result_response
    return "login index"

@bp.route('/logout',methods = ('GET','POST'))
def logout():
    #对应会话删除
    session.pop(request.form['user_id'], None)
    return redirect(url_for(log_Index))


def loged_Veri(id = None):
    #检查会话是否存在，不存在跳转到log_index界面
    #返回身份ID  0：普通员工， 1：主管   2：经理
    return id