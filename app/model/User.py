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
from .WorkArrangement import WorkArrangement
from .SignSheet import SignSheet


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
        Overtime.new(self, info)

    def new_leave(self, info: dict):
        """新请假

        :param info {}
            beginDateTime 
            endDateTime
            reason
        """
        Leave.new(self, info)

    def arrangement_by_date(self, date):
        """
        根据日期返回对应日期该员工的工作安排。

        返回的是一个列表，其中每个对象都是一次工作安排。

        :param date 工作日期
        :return List[WorkArrangement]
        """
        return WorkArrangement.ByStaffIDandDate(self.ID, date)

    def leaves_by_date(self, date):
        return Leave.ByStaffIDandDate(self.ID, date)

    def overtimes_by_date(self, date):
        return Overtime.ByStaffIDandDate(self.ID, date)

    def signs_by_date(self, date):
        return SignSheet.ByStaffIDandDate(self.ID, date)

    def arrangement_by_range(self, from_, to_):
        """
        根据日期范围返回范围内的工作安排。

        返回一个字典。键是Date对象，值是List[WorkArrangement]
        """
        return WorkArrangement.ByStaffIDandRange(self.ID, from_, to_)

    def leaves_by_range(self, from_, to_):
        return Leave.ByStaffIDandRange(self.ID, from_, to_)

    def overtimes_by_range(self, from_, to_):
        return Overtime.ByStaffIDandRange(self.ID, from_, to_)

    def signs_by_range(self, from_, to_):
        return SignSheet.ByStaffIDandRange(self.ID, from_, to_)

    def in_leave(self, datetime) -> bool:
        """
        查询该员工在对应的时间中是否为假期。
        """
        for l in self.leaves:
            if l.beginDateTime < datetime and l.endDateTime > datetime and l.status == 1:
                return True

        return False
