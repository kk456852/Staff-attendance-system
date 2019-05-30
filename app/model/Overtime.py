from .. import db

import time
from datetime import datetime
from .User import User
from .Leave import Leave
from .sendEmail1 import SendEmail


class Overtime(db.Model):  # 加班
    # DateTime类对象，使用overtimeBeginTime.year;overtimeBeginTime.month;
    # overtimeBeginTime.day;overtimeBeginTime.hour;
    # overtimeBeginTime.minute;overtimeBeginTime.second
    # 也可  overtimeBeginTime = datetime(2019,6,6,10,0)

    overtimeID = db.Column(db.Integer, primary_key=True)
    overtimeThreshold = db.Column(db.Integer)  # 加班阈值 单位-分钟
    staffID = db.Column(db.Integer, db.ForeignKey(
        'user.ID'), nullable=False)  # 员工标号
    overtimeBeginTime = db.Column(db.DateTime, nullable=False)
    overtimeEndTime = db.Column(db.DateTime, nullable=False)
    overtimeType = db.Column(db.Integer, nullable=False)  # 0-法定假日 1-工作时间
    submitTime = db.Column(db.DateTime, nullable=False)
    isOvertimePermitted = db.Column(db.Boolean)  # 是否准许加班 0-未审核 1-通过 2-不通过

    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    now_time_year = time.strftime('%Y', time.localtime(time.time()))
    now_time_month = time.strftime('%M', time.localtime(time.time()))
    now_time_day = time.strftime('%d', time.localtime(time.time()))
    now_time_hour = time.strftime('%H', time.localtime(time.time()))
    now_time_minute = time.strftime('%M', time.localtime(time.time()))
    now_time_second = time.strftime('%S', time.localtime(time.time()))
    dictNowTime = {'year': now_time_year,
                   'month': now_time_month,
                   'day': now_time_day,
                   'hour': now_time_hour,
                   'minute': now_time_minute,
                   'second': now_time_second}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<Overtime %i>' % self.overtimeID

    #
    # 数据库方法
    #
    @staticmethod
    def findall():
        return Overtime.query.all()

    @staticmethod
    def getInfoById(overtimeId):
        return Overtime.query.get(overtimeId)

    @staticmethod
    def getInfoBystaffId(staffId):
        return Overtime.query.filter_by(staffId=staffId).all()

    @staticmethod
    def getInfoByThreshold(overtimeThreshold):
        return Overtime.query.filter_by(overtimeThreshold=overtimeThreshold).all()

    @staticmethod
    def getInfoBypermitted(permitted):
        return Overtime.query.filter_by(isOvertimePermitted=permitted).all()

    def inform_overtime(self):
        """inform_overtime提醒员工加班"""
        pass

    def overtime_application_to_director(self):
        """overtime_application_to_director加班申请通知主管"""
        pass

    def overtime_result_to_employee(self):
        """overtime_result_to_employee加班申请结果通知员工"""
        pass


#
# 全单位临时性加班活动类
#
class TemporaryOvertime:

    startTime = db.Column(db.DateTime)
    endTime = db.Column(db.DateTime)
    name = db.Column(db.String(20))
    userID = db.Column(db.Integer, db.ForeignKey('User.ID'))
    isPermitted = db.Column(db.Integer)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def inform_temporary_overtime(self, startTime, endTime):
        """inform_temporary_overtime全员加班通知员工(非请假状态)"""
        self.startTime = startTime
        self.endTime = endTime
        listUser = User.All()
        for user in listUser:
            if not user.in_leave(startTime) and not user.in_leave(endTime):
                str1 = startTime.strftime('%Y-%m-%d-%h-%m')
                str2 = startTime.strftime('%Y-%m-%d-%h-%m')
                SendEmail(user.email, "临时加班", str1+str2)

    def start(self):
        pass
