from .. import db

from .User import User
from .Department import Department
from ..exceptions import DepartmentError
from .sendEmail1 import SendEmail





class Leave(db.Model):  # 请假

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



    #
    # 数据库方法
    #
    @staticmethod
    def findAll():
        return Leave.query.all()

    @staticmethod
    def getInfoByID(leaveID):
        return Leave.query.get(leaveID)

    @staticmethod
    def getInfoBystaffID(staffID):
        return Leave.query.filter_by(staffID=staffID).all()

    @staticmethod
    def getInfoByleaveDate(leaveDate):
        return Leave.query.filter_by(leaveDate=leaveDate).all()

    @staticmethod
    def getInfoByPermitted(permitted):
        return Leave.query.filter_by(isLeavePermitted=permitted).all()
    
 


    def leave_application_to_director(self):
        """leave_application_to_director请假申请通知主管"""

        u = User.ByID(self.staffID)
        d = Department.ByID(u.departmentID)
        self.isLeavePermitted = 0    # 请假未审核

        for i in range(len(d.users)):
            if(d.users[i].identity == 2):
                director = d.users[i]
                break
                
        if(d.users[i].identity != 2 ):
            return DepartmentError
        
        else:
            dictLeave = {'email':director.email, 'leaveInfo':self.json(), 'result':"请假审批中"}
            #SendEmail()
            subject = '有人请假啦'
            str = dictLeave['leaveInfo']+dictLeave['result']
            SendEmail(dictLeave['email'], subject, str)
            return dictLeave

        
    def leave_result_to_employee(self):
        """leave_result_to_employee请假结果通知员工"""
        staff = User.ByID(self.staffID)
        if(self.isLeavePermitted == 1):   #主管批准
            dictLeave = {'email':staff.email, 'leaveInfo':Leave, 'result':'你的请假获得批准'}
            subject = '请假成功！'
            str = dictLeave['leaveInfo']+dictLeave['result']
            SendEmail(dictLeave['email'], subject, str)
            return dictLeave

        if(self.isLeavePermitted == 2):   #主管未批准
            dictLeave = {'email':staff.email, 'leaveInfo':Leave, 'result':'你的请假未获批准'}
            subject = '请假失败。。。！'
            str = dictLeave['leaveInfo']+dictLeave['result']
            SendEmail(dictLeave['email'], subject, str)
            return dictLeave






