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

    # 这个方法作为对象的打印方法，类似于java类中 自己重写的 toString()方法，实现这个方法后，print(类) 将会执行这个方法进行打印
    def __repr__(self):
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


class Department(db.Model):  # 部门
    __tablename__ = 'department'
    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    users = db.relationship('User', backref='department')  # ?

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<Department %i %r>' % (self.id, self.name)

    @classmethod
    def findAll():
        return Department.query.all()

    @classmethod
    def getInfoByID(ID):
        return Department.query.get(ID)

    @classmethod
    def getInfoByName(name):
        return Department.query.filter_by(name=name).all()


class WorkArrangement(db.Model):  # 工作安排
    __tablename__ = 'arrangement'
    arragementID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey('user.ID'))  # 员工标号
    departmentID = db.Column(
        db.Integer, db.ForeignKey('department.ID'))  # 部门标号
    workDate = db.Column(db.Date, nullable=False)  # 工作日期
    beginTime = db.Column(db.Time, nullable=False)  # 开始时间
    endTime = db.Column(db.Time, nullable=False)  # 结束时间
    assignment = db.Column(db.String(50))  # 工作安排

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<WorkArrangement %i %i>' % (self.staffID, self.departmentID)

    @classmethod
    def findAll():
        return WorkArrangement.query.all()

    @classmethod
    def getInfoByID(self, arragementID):
        return WorkArrangement.query.get(arragementID)

    @classmethod
    def getInfoBystaffID(self, staffID):
        return WorkArrangement.query.filter_by(staffID=staffID).all()

    @classmethod
    def getInfoBydepID(self, departmentID):
        return WorkArrangement.query.filter_by(departmentID=departmentID).all()


class SignSheet(db.Model):  # 签到表
    __tablename__ = 'signsheet'
    sheetID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey(
        'user.ID'), nullable=False)  # 员工标号
    type = db.Column(db.Integer, nullable=False)  # 类型 0-日常签到 1-临时加班
    date = db.Column(db.Integer, nullable=False)
    punchBeginTime = db.Column(db.Time)  # 签到上班时间
    punchEndTime = db.Column(db.Time)  # 签到下班时间
    isLate = db.Column(db.Boolean)  # 是否迟到
    isEarly = db.Column(db.Boolean)  # 是否早退

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<SignSheet %i %i>' % (self.sheetIdID, self.type)

    @classmethod
    def findAll():
        return SignSheet.query.all()

    @classmethod
    def getInfoById(sheetId):
        return SignSheet.query.get(sheetId)

    @classmethod
    def getInfoBystaffId(staffId):
        return SignSheet.query.filter_by(staffId=staffId).all()

    @classmethod
    def getInfoBytype(type):
        return SignSheet.query.filter_by(type=type).all()

    @classmethod
    def getInfoBydate(date):
        return SignSheet.query.filter_by(date=date).all()


class Leave(db.Model):  # 请假
    __tablename__ = 'leave'
    leaveID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey(
        'user.ID'), nullable=False)  # 员工标号
    leaveReason = db.Column(db.String(50))
    leaveDate = db.Column(db.Date, nullable=False)
    submitTime = db.Column(db.Time, nullable=False)
    leaveBeginTime = db.Column(db.Time, nullable=False)
    leaveEndTime = db.Column(db.Time, nullable=False)
    isLeavePermitted = db.Column(db.Integer)  # 0-未审核 1-通过审核 2-未通过审核

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<Leave %i %r>' % (self.staffID, self.leaveReason)

    @classmethod
    def findAll():
        return Leave.query.all()

    @classmethod
    def getInfoById(leaveId):
        return Leave.query.get(leaveId)

    @classmethod
    def getInfoBystaffId(staffId):
        return Leave.query.filter_by(staffId=staffId).all()

    @classmethod
    def getInfoByleaveDate(leaveDate):
        return Leave.query.filter_by(leaveDate=leaveDate).all()

    @classmethod
    def getInfoByPermitted(permitted):
        return Leave.query.filter_by(isLeavePermitted=permitted).all()


class Report(db.Model):  # 销假
    __tablename__ = 'report'
    reportID = db.Column(db.Integer, primary_key=True)
    leaveID = db.Column(db.Integer, db.ForeignKey(
        'leave.leaveID'), nullable=False)  # 对应的请假id
    reportTime = db.Column(db.Time, nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<Report %i %i>' % (self.reportID, self.leaveID)

    @classmethod
    def findAll():
        return Report.query.all()

    @classmethod
    def getInfoById(reportId):
        return Report.query.get(reportId)

    @classmethod
    def getInfoByleaveId(leaveId):
        return Report.query.filter_by(leaveId=leaveId).all()


class Overtime(db.Model):  # 加班
    __tablename__ = 'overtime'
    overtimeID = db.Column(db.Integer, primary_key=True)
    overtimeThreshold = db.Column(db.Integer)  # 加班阈值 单位-分钟
    staffID = db.Column(db.Integer, db.ForeignKey(
        'user.ID'), nullable=False)  # 员工标号
    overtimeBeginTime = db.Column(db.Time, nullable=False)
    overtimeEndTime = db.Column(db.Time, nullable=False)
    overtimeType = db.Column(db.Integer, nullable=False)  # 0-法定假日 1-工作时间
    submitTime = db.Column(db.Time, nullable=False)
    isOvertimePermitted = db.Column(db.Boolean)  # 是否准许加班 0-未审核 1-通过 2-不通过

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<Overtime %i>' % self.overtimeId

    @classmethod
    def findall():
        return Overtime.query.all()

    @classmethod
    def getInfoById(overtimeId):
        return Overtime.query.get(overtimeId)

    @classmethod
    def getInfoBystaffId(staffId):
        return Overtime.query.filter_by(staffId=staffId).all()

    @classmethod
    def getInfoByThreshold(overtimeThreshold):
        return Overtime.query.filter_by(overtimeThreshold=overtimeThreshold).all()

    @classmethod
    def getInfoBypermitted(permitted):
        return Overtime.query.filter_by(isOvertimePermitted=permitted).all()
