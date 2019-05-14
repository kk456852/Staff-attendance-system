import os

from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .. import db


class User(db.Model):  # 用户
    __tablename__ = 'user'
    ID = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)
    identity = db.Column(db.Integer, nullable=False)  # 职务 1-员工 2-主管 3-经理
    name = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.Boolean)  # 性别 0-男 1-女
    birthday = db.Column(db.Date)
    email = db.Column(db.String(30))
    phoneNumber = db.Column(db.String(20))
    workStatus = db.Column(db.Integer)  # 工作状态 1-上班 2-正常休假 3-经理状态 4-下班 5-请假休假
    departmentID = db.Column(
        db.Integer, db.ForeignKey('department.ID'))  # 部门标号

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # （可选地）初始化数据库内容

    def __repr__(self):
        """打印对象的信息"""
        return '<User {}, ID={}>'.format(self.name, self.ID)

    @property
    def password(self):
        raise AttributeError('密码不能被明文读取！')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    #
    # 数据库查询方法
    #

    @staticmethod
    def All():
        """返回数据库中所有的User对象

        returns: List[User]
        """
        return User.query.all()

    @classmethod
    def ByID(self, ID):
        """根据ID构造对象

        returns: User
        """
        return User.query.get(ID)

    #
    # 自修改方法
    #

    def login(self, password):
        """登录操作，失败后会抛出异常

        raise: Exception
        """
        if not self.verify_password(password):
            raise Exception

    def update_self(self):
        """将修改后的对象，或者新增的对象添加/修改到数据库中。

        raise: 
        """
        db.session.add(self)
        db.session.commit()
