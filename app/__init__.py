from datetime import date, time, datetime

from flask import Flask
from flask.json import JSONEncoder, JSONDecoder
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

import config

from .dbBase import BaseModel
from .util import executor

db = SQLAlchemy(model_class=BaseModel)
mail = Mail()


def create_app():
    """
    创建一个Flask应用实例。

    :returns: flask-app
    """
    app = Flask(__name__)
    app.config.from_object(config)
    app.json_encoder = CustomJSONEncoder
    app.json_decoder = CustomJSONDecoder

    db.init_app(app)
    mail.init_app(app)

    # 此处必须函数内部导入路由，在之前导入可能因为没有构建好所有的组件而出现错误。
    from .api import auth, staff, leaves, sign, tempovertime, workstatus, department, arrangements, overtimes
    app.register_blueprint(auth.bp)
    app.register_blueprint(staff.bp)
    app.register_blueprint(workstatus.bp)
    app.register_blueprint(tempovertime.bp)
    app.register_blueprint(sign.bp)
    app.register_blueprint(leaves.bp)
    app.register_blueprint(department.bp)
    app.register_blueprint(arrangements.bp)
    app.register_blueprint(overtimes.bp)

    # 在此处加入所有后台程序。
    # from .util.background import print_number
    # add_background(app, print_number)

    return app


def add_background(app, func):
    """
    加入后台任务。

    将一个后台任务加入后台执行。这个任务将在第一次请求被调用之前加入线程池。
    """
    def new_dg():
        def add_dg():
            with app.app_context():
                try:
                    func()
                except Exception as e:
                    app.logger.exception(e)

        executor.submit(add_dg)

    app.before_first_request(new_dg)


class CustomJSONEncoder(JSONEncoder):
    """设置JSON编码器

    datetime.date 使用isoformat格式化"""

    def default(self, obj):
        try:
            if isinstance(obj, datetime):
                return int(obj.timestamp())
            elif isinstance(obj, date):
                return obj.isoformat()
            elif isinstance(obj, time):
                return obj.isoformat()[:-3]  # 去掉秒
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


class CustomJSONDecoder(JSONDecoder):
    def __init__(self, *args, **kwargs):
        self.orig_obj_hook = kwargs.pop("object_hook", None)
        super(CustomJSONDecoder, self).__init__(*args,
                                                object_hook=self.custom_obj_hook, **kwargs)

    def custom_obj_hook(self, dct):
        for k, v in dct.items():
            if k.lower().endswith('date'):
                dct[k] = date(*[int(i) for i in v.split('-')])
            elif k.lower().endswith('datetime') or k.lower().endswith('stamp') or k == 'birthday':
                dct[k] = datetime.fromtimestamp(v)
            elif k.lower().endswith('time'):
                dct[k] = time(*[int(i) for i in v.split(':')])

        if (self.orig_obj_hook):
            return self.orig_obj_hook(dct)
        return dct
