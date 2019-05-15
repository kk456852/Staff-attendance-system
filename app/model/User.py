import os
from enum import IntEnum

from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .. import db
from .Department import Department


class Role(IntEnum):
    """职务

    使用数值枚举类，该类是int的子类
    """
    STAFF = 1
    CHARGE = 2
    MANAGER = 3


class User(db.Model):
    """用户类，必须使用具名参数新建对象

    :param ID* 主键
    :param password* 只可写，不可读
    :param identity* 职务 1-员工 2-主管 3-经理
    :param name*
    :param gender 性别 0-男 1-女
    :param birthday
    :param email
    :param phoneNumber
    :param workStatus 工作状态 1-上班 2-正常休假 3-经理状态 4-下班 5-请假休假
    :param departmentID 部门标号 为department表的外键
    """

    ID = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)
    identity = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.Boolean)
    birthday = db.Column(db.Date)
    email = db.Column(db.String(30))
    phoneNumber = db.Column(db.String(20))
    workStatus = db.Column(db.Integer)
    departmentID = db.Column(db.Integer, db.ForeignKey('department.ID'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # （可选地）初始化数据库内容

    def __repr__(self):
        """打印对象的信息"""
        return '<User {}, ID={}, Role={}>'.format(self.name, self.ID, Role(self.identity).name)

    @property
    def password(self):
        raise AttributeError('密码不能被明文读取！')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def role(self):
        return Role(self.identity)

    @role.setter
    def role(self, r):
        self.identity = r

    #
    # 数据库查询方法
    #

    @staticmethod
    def All():
        """返回数据库中所有的User对象

        :returns List[User]
        """
        return User.query.all()

    @staticmethod
    def ByID(ID):
        """根据ID构造对象

        :returns User
        """
        return User.query.get(ID)

    #
    # 公共方法
    #

    def login(self, password):
        """登录操作，失败后会抛出异常

        :raise Exception
        """
        if not self.verify_password(password):
            raise Exception

    def update_self(self):
        """将修改后的对象，或者新增的对象添加/修改到数据库中。

        :raise InvalidRequestError
        """
        db.session.add(self)
        db.session.commit()

    def delete_self(self):
        """删除数据库中该对象对应的用户。

        :raise InvalidRequestError
        """
        db.session.delete(self)
        db.session.commit()

    #
    # 主管方法
    #

    def arrange_work(self):
        """安排工作班次"""
        pass

    def update_work_arrangement(self):
        """修改本部门员工工作安排"""
        pass

    def approve_leave(self):
        """请假审批"""
        pass

    def approve_report(self):
        """销假处理"""
        pass

    def approve_overtime(self):
        """加班审批"""
        pass

    #
    # 经理方法
    #

    def update_employee(self, u):
        """修改员工信息

        :param u : User
        """
        employee.user.update_self()

    def retrieve_employee(self, employeeID):
        """查看员工信息"""
        return

    def get_employees(self):
        """查看全部员工的信息

        :return List[Employee]
        """
        return

    def delete_employee(self, employee):
        """人员删除"""
        employee.delete_self()

    def update_position(self):
        """身份修改"""
        pass

    def create_employee(self):
        """人员添加"""
        pass

    def release_temporary_overtime(self):
        """发布全单位加班"""
        pass

    def retrieve_work_situation(self):
        """查看上班情况"""
        pass
