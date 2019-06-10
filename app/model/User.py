import os
from enum import IntEnum
from typing import List
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .. import db
from .Department import Department
from ..exceptions import UserNotFoundException

from .Leave import *

class Role(IntEnum):
    """职务

    使用数值枚举类，该类是int的子类
    """
    STAFF = 1
    CHARGE = 2
    MANAGER = 3


class User(db.Model):
    """用户类，必须使用具名参数新建对象。带有*的是必须项。

    :param ID* 主键
    :param password* 只可写，不可读
    :param role* 角色，枚举Role类型
    :param name*
    :param gender 性别 False-男 True-女
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

    # 伪属性，被下面的 @property department 代理
    _departmentID = db.Column(db.Integer, db.ForeignKey('department.ID'))

    # 反向引用，包含所有引用User.ID的项
    leaves = db.relationship('Leave', backref='user')
    signsheets = db.relationship('SignSheet', backref='user')
    overtimes = db.relationship('Overtime', backref='user')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # （可选地）初始化数据库内容

    def __repr__(self):
        """打印对象的信息"""
        return '<User {}, ID={}, Role={},Email={}>'.format(self.name, self.ID, Role(self.identity).name, self.email)

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
        """返回用户的角色
        可以使用.name方法获取角色的名字 (MANAGER/CHARGE/STAFF)

        :return Role
        """
        return Role(self.identity)

    @role.setter
    def role(self, r):
        self.identity = r

    @property
    def departmentID(self):
        return self.department.ID

    @departmentID.setter
    def departmentID(self, ID):
        self.department = Department.ByID(ID)

    #
    # 数据库方法
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
        数据库中没有此ID时抛出异常

        :returns User
        :raise UserNotFoundException
        """
        u = User.query.get(ID)
        if not u:
            raise UserNotFoundException()
        return u

    def update_db(self):
        """将修改后的对象，或者新增的对象添加/修改到数据库中。
        失败时抛出异常。

        :raise InvalidRequestError
        """
        db.session.add(self)
        db.session.commit()

    def delete_db(self):
        """删除数据库中该对象对应的用户。
        失败时抛出异常。

        :raise InvalidRequestError
        """
        db.session.delete(self)
        db.session.commit()

    #
    # 公共方法
    #

    def login(self, password):
        """登录操作，失败后会抛出异常

        :param str
        :raise Exception
        """
        if not self.verify_password(password):
            raise Exception

    def update(self, data):
        """修改自身属性。

        :data 属性字典
        :param 具名参数
        """
        for x in self.dict().keys():
            if x in data.keys():
                self.__setattr__(x, data[x])

        self.update_db()

    def in_leave(self, time):
        for l in self.leaves:
            if l.leaveBeginTime < time and l.leaveEndTime > time and l.isLeavePermitted:
                return True

        return False

    #
    # 主管方法
    #

    def arrange_work(self):
        """安排工作班次"""
        pass

    def update_work_arrangement(self):
        """修改本部门员工工作安排"""
        pass

    def approve_leave(self, LeaveID, isLeavePermitted):
        """请假审批"""
        l = Leave.ByID(LeaveID)
        l.isLeavePermitted = isLeavePermitted
        l.update_db()
        l.leave_result_to_employee()

    def approve_report(self, LeaveID):
        """销假处理"""
        l = Leave.ByID(LeaveID)
        u = User.ByID(l.staffID)
        u.workStatus = 1
        u.update_db()


    def approve_overtime(self):
        """加班审批"""
        pass

    #
    # 经理方法
    #

    def retrieve_employee(self, employeeID):
        """查看员工信息"""
        u = User.ByID(employeeID)
        return u.__repr__


    def delete_employee(self, employeeID):
        """人员删除"""
        u = User.ByID(employeeID)
        u.delete_db()

    def update_position(self,ID,identity):
        """身份修改"""
        u = User.ByID(ID)
        u.identity = identity
        u.update()

    def release_temporary_overtime(self):
        """发布全单位加班"""
        pass

    def retrieve_work_situation(self):
        """查看上班情况"""
        pass
