from .. import db


class Leave(db.Model):  # 请假

    ID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey(
        'user.ID'), nullable=False)  # 员工标号
    reason = db.Column(db.String(50))
    date = db.Column(db.Date, nullable=False)
    submitTime = db.Column(db.Time, nullable=False)
    beginTime = db.Column(db.Time, nullable=False)
    endTime = db.Column(db.Time, nullable=False)
    isLeavePermitted = db.Column(db.Integer)  # 0-未审核 1-通过审核 2-未通过审核

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<Leave %i %r>' % (self.staffID, self.leaveReason)

    @staticmethod
    def All():
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
        pass

    def leave_result_to_employee(self):
        """leave_result_to_employee请假结果通知员工"""
        pass
