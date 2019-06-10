import os
from datetime import date, datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

from .. import db
from ..exceptions import PasswordNotCorrectError
from .Department import Department
from .Leave import Leave
from .Overtime import Overtime
from .Role import Role


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

    # 伪属性，被下面的 @property department 代理
    departmentID = db.Column(db.Integer, db.ForeignKey('department.ID'))

    # 反向引用，包含所有引用User.ID的项
    leaves = db.relationship('Leave', foreign_keys='[Leave.staffID]')
    overtimes = db.relationship('Overtime', foreign_keys='[Overtime.staffID]')
    signsheets = db.relationship('SignSheet', backref='user')

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
    def role(self) -> Role:
        """返回用户的角色

        可以使用u.role.name方法获取角色的名字 (MANAGER/CHARGE/STAFF)
        """
        if self.identity:
            return Role(self.identity)

    @role.setter
    def role(self, r: Role):
        self.identity = r

    # 公共方法
    def login(self, password):
        """登录操作，失败后会抛出异常

        :param str
        :raise PasswordNotCorrectError
        """
        if not self.verify_password(password):
            raise PasswordNotCorrectError

    # 普通员工方法
    def new_overtime(self, info: dict):
        """申请新的加班

        :param info {}
            beginDateTime 
            endDateTime
            reason
        """
        # TODO: 此处应该查询加班时间段是否在正常范围内，否则抛出异常
        o = Overtime(**info)
        o.staff = self
        o.status = 0
        o.update_db()
        # TODO:此处应通知主管

    def new_leave(self, info: dict):
        """新请假

        :param info {}
            beginDateTime 
            endDateTime
            reason
        """
        Leave.new(self, info)

    def in_leave(self, time):
        for l in self.leaves:
            if l.leaveBeginTime < time and l.leaveEndTime > time and l.isLeavePermitted:
                return True

        return False

    #
    # 主管方法

    def arrange_work(self):
        """安排工作班次"""
        pass

    def update_work_arrangement(self):
        """修改本部门员工工作安排"""
        pass

    #
    # 经理方法
    #

    def release_temporary_overtime(self):
        """发布全单位加班"""
        pass
