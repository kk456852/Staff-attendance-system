import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .. import db


class User(db.Model):  # 用户
    __tablename__ = 'user'
    ID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    identity = db.Column(db.Integer, nullable=False)  # 职务 1-员工 2-主管 3-经理
    name = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.Boolean)  # 性别 0-男 1-女
    birthday = db.Column(db.Date)
    email = db.Column(db.String(30))
    phoneNumber = db.Column(db.String(20))
    workStatus = db.Column(db.Integer)  # 工作状态 1-上班 2-正常休假 3-经理状态 4-下班 5-请假休假
    departmentID = db.Column(db.Integer, db.ForeignKey('department.ID'))  # 部门标号

    def __init__(self, username, password, position, gender, age, workStatus, departmentID):
        self.username = username
        self.password = password
        self.age = age
        self.gender = gender
        self.position = position

        if(position == 2):
            self.workStatus = 3
            self.departmentID = 0
        else:
            self.workStatus = workStatus
            self.departmentID = departmentID

    # 这个方法作为对象的打印方法，类似于java类中 自己重写的 toString()方法，实现这个方法后，print(类) 将会执行这个方法进行打印
    def __repr__(self):
        return '<User %r>' % self.username


class Department(db.Model):  # 部门
    __tablename__ = 'department'
    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    users = db.relationship('User', backref='department')  # ?

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<Department %i %r>' % (self.id, self.name)


class WorkArrangement(db.Model):  # 工作安排
    __tablename__ = 'arrangement'
    arragementID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey('user.ID'))  # 员工标号
    departmentID = db.Column(db.Integer, db.ForeignKey('department.ID'))  # 部门标号
    workDate = db.Column(db.Date, nullable=False)  # 工作日期
    beginTime = db.Column(db.Time, nullable=False)  # 开始时间
    endTime = db.Column(db.Time, nullable=False)  # 结束时间
    assignment = db.Column(db.String(50))  # 工作安排

    def __init__(self, staffID, departmentID, workDate, beginTime, endTime, assignment):
        self.staffID = staffID
        self.departmentID = departmentID
        self.workDate = workDate
        self.beginTime = beginTime
        self.endTime = endTime
        self.assignment = assignment

    def __repr__(self):
        return '<WorkArrangement %i %i>' % (self.staffID, self.departmentID)


class SignSheet(db.Model):  # 签到表
    __tablename__ = 'signsheet'
    sheetID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey('user.ID'), nullable=False)  # 员工标号
    type = db.Column(db.Integer, nullable=False)  # 类型 0-日常签到 1-临时加班
    date = db.Column(db.Integer, nullable=False)
    punchBeginTime = db.Column(db.Time)  # 签到上班时间
    punchEndTime = db.Column(db.Time)  # 签到下班时间
    isLate = db.Column(db.Boolean)  # 是否迟到
    isEarly = db.Column(db.Boolean)  # 是否早退

    def __init__(self, staffID, type, date, punchBeginTime, punchEndTime, isLate):
        self.sheetID = staffID
        self.type = type
        self.date = date
        self.punchBeginTime = punchBeginTime
        self.punchEndTime = punchEndTime
        self.isLate = isLate

    def __repr__(self):
        return '<SignSheet %i %i>' % (self.sheetIdID, self.type)


class Leave(db.Model):  # 请假
    __tablename__ = 'leave'
    leaveID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey('user.ID'), nullable=False)  # 员工标号
    leaveReason = db.Column(db.String(50))
    leaveDate = db.Column(db.Date, nullable=False)
    submitTime = db.Column(db.Time, nullable=False)
    leaveBeginTime = db.Column(db.Time, nullable=False)
    leaveEndTime = db.Column(db.Time, nullable=False)
    isLeavePermitted = db.Column(db.Integer)  # 0-未审核 1-通过审核 2-未通过审核

    def __init__(self, staffID, leaveReason, leaveDate, leaveBeginTime, leaveEndTime, isLeavePermitted):
        self.staffID = staffID
        self.leaveReason = leaveReason
        self.leaveDate = leaveDate
        self.leaveBeginTime = leaveBeginTime
        self.leaveEndTime = leaveEndTime
        self.isLeavePermitted = isLeavePermitted

    def __repr__(self):
        return '<Leave %i %r>' % (self.staffID, self.leaveReason)


class Report(db.Model):  # 销假
    __tablename__='report'
    reportID = db.Column(db.Integer, primary_key=True)
    leaveID = db.Column(db.Integer, db.ForeignKey('leave.leaveID'), nullable=False)  # 对应的请假id
    reportTime = db.Column(db.Time, nullable=False)

    def __init__(self, leaveID, reportTime):
        self.leaveID = leaveID
        self.reportTime = reportTime

    def __repr__(self):
        return '<Report %i %i>' % (self.reportID, self.leaveID)


class Overtime(db.Model):  # 加班
    __tablename__ = 'overtime'
    overtimeID = db.Column(db.Integer, primary_key=True)
    overtimeThreshold = db.Column(db.Integer)  # 加班阈值 单位-分钟
    staffID = db.Column(db.Integer, db.ForeignKey('user.ID'), nullable=False)  # 员工标号
    overtimeBeginTime = db.Column(db.Time, nullable=False)
    overtimeEndTime = db.Column(db.Time, nullable=False)
    overtimeType = db.Column(db.Integer, nullable=False)  # 0-法定假日 1-工作时间
    submitTime = db.Column(db.Time, nullable=False)
    isOvertimePermitted = db.Column(db.Boolean)  # 是否准许加班 0-未审核 1-通过 2-不通过

    def __init__(self, overtimeThreshold, staffID, isOvertimePermitted):
        self.overtimeThreshold = overtimeThreshold
        self.staffID = staffID
        self.isOvertimePermitted = isOvertimePermitted

    def __repr__(self):
        return '<Overtime %i>' % self.overtimeID
