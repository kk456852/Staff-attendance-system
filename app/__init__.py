from flask import Flask
from flask_sqlalchemy import SQLAlchemy


import config

db = SQLAlchemy()


def create_app():
    """
    创建一个Flask应用实例。

    :returns: flask-app
    """
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    # 此处必须函数内部导入路由，在之前导入可能因为没有构建好所有的组件而出现错误。
    from .api import auth, charger, manager, staff
    app.register_blueprint(auth.bp)
    app.register_blueprint(charger.bp)
    app.register_blueprint(manager.bp)
    app.register_blueprint(staff.bp)

    return app
