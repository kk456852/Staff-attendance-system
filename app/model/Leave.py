from .. import db

from .User import User
from .Department import Department
from ..exceptions import DepartmentError



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

    @staticmethod
    def findAll():
        return Leave.query.all()

    @staticmethod
    def getInfoById(leaveId):
        return Leave.query.get(leaveId)

    @staticmethod
    def getInfoBystaffId(staffId):
        return Leave.query.filter_by(staffId=staffId).all()

    @staticmethod
    def getInfoByleaveDate(leaveDate):
        return Leave.query.filter_by(leaveDate=leaveDate).all()

    @staticmethod
    def getInfoByPermitted(permitted):
        return Leave.query.filter_by(isLeavePermitted=permitted).all()

    def leave_application_to_director(self):
        """leave_application_to_director请假申请通知主管"""
        """返回该员工的主管的邮箱"""

        u = User.ByID(self.staffID)
        d = Department.ByID(u.departmentID)

        users = [] 
        users = d.users #???

        for i in range(len(users)):
            if(users[i].identity == 2  ):
                director = users[i]
                break
            else:
                raise DepartmentError
        
        return (director.email)

            

        

    def leave_result_to_employee(self):
        """leave_result_to_employee请假结果通知员工"""
        pass


