from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from .dbBase import JsonModel
import config

db = SQLAlchemy(model_class=JsonModel)
# db = SQLAlchemy()

def create_app():
    """
    创建一个Flask应用实例。

    :returns: flask-app
    """
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    # 此处必须函数内部导入路由，在之前导入可能因为没有构建好所有的组件而出现错误。
    from .api import auth, charger, manager, staff,leaves,sign,tempovertime,workstatus,department,arranges,overtimes
    app.register_blueprint(auth.bp)
    app.register_blueprint(staff.bp)
    app.register_blueprint(workstatus.bp)
    app.register_blueprint(tempovertime.bp)
    app.register_blueprint(sign.bp)
    app.register_blueprint(leaves.bp)
    app.register_blueprint(department.bp)
    app.register_blueprint(arranges.bp)
    app.register_blueprint(overtimes.bp)
    return app
