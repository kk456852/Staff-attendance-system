from datetime import datetime

from .. import db

from .User import User
from .Department import Department
from ..exceptions import DepartmentError
from .sendEmail1 import SendEmail





class Leave(db.Model):
    """
    请假

    :param staffID 请假人ID
    :param reviewerID 审核人ID
    :param type 请假类型。0:病假 1:事假
    :param status 请假的状态。0:未审核 1:主管已审核 2:主管未批准 3:已取消 4:已销假
    :param reason 请假原因
    :param submitStamp 提交申请时间戳
    :param reviewStamp 审核时间戳
    :param reportStamp 销假时间戳
    """
    ID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey(
        'user.ID'), nullable=False)
    reviewerID = db.Column(db.Integer, db.ForeignKey(
        'user.ID'))

    beginDateTime = db.Column(db.DateTime, nullable=False)
    endDateTime = db.Column(db.DateTime, nullable=False)

    type = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.String(200))

    submitStamp = db.Column(db.DateTime)
    reviewStamp = db.Column(db.DateTime)
    reportStamp = db.Column(db.DateTime)

    staff = db.relationship("User", foreign_keys="Leave.staffID")
    reviewer = db.relationship("User", foreign_keys="Leave.reviewerID")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.submitStamp = datetime.now()

    def __repr__(self):
        return '<Leave {}:{}>'.format(self.staffID, self.reason)

    def to_staff(self):
        """
        返回给员工的信息。
        """
        res = self.dict()
        res["reviewerName"] = self.reviewer.name if self.reviewer else None
        res.pop("reviewerID")
        return res

    def to_charge(self):
        res = self.dict()
        res["reviewerName"] = self.reviewer.name if self.reviewer else None
        res["staffName"] = self.staff.name
        return res

    def review(self, charge, permit: bool):
        self.status = 1 if permit else 2
        self.reviewer = charge
        self.reviewStamp = datetime.now()
        self.update_db()
        # TODO:此处应通知被审批人

    def report(self):
        """销假"""
        # TODO: 进行状态、时间、权限检查
        self.status = 4
        self.reportStamp = datetime.now()



    def leave_application_to_director(self):
        """leave_application_to_director请假申请通知主管"""
        """返回该员工的主管的邮箱"""

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






