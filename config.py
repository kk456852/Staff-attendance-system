import os

base_dir = os.path.abspath(os.path.dirname(__name__))

# 以下是 Flask 配置项，内容将从环境变量中导入
SQLALCHEMY_DATABASE_URI = os.environ.get(
    'SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + os.path.join(base_dir, 'db.sqlite3')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ.get('SECRET_KEY') or b'_5#y2L"F4Q8z\n\xec]/'
MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.126.com'
MAIL_PORT = os.environ.get('MAIL_PORT') or 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
