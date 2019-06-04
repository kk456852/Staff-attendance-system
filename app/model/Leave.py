from .. import db


class Leave(db.Model):
    """
    请假

    开始时间和结束时间是可选的。默认为从开始时间到结束时间内的整天。

    :param status 表示请假的状态。0-未审核 1-主管已审核 2-主管拒绝 3-已取消 4-已销假
    """
    ID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey(
        'user.ID'), nullable=False)  # 员工标号
    reason = db.Column(db.String(50))

    beginDate = db.Column(db.Date, nullable=False)
    endDate = db.Column(db.Date)
    beginTime = db.Column(db.Time)
    endTime = db.Column(db.Time)

    status = db.Column(db.Integer)

    submitTime = db.Column(db.DateTime)
    chargeTime = db.Column(db.DateTime)
    reportTime = db.Column(db.DateTime)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<Leave %i %r>' % (self.staffID, self.leaveReason)

    def leave_application_to_director(self):
        """leave_application_to_director请假申请通知主管"""
        pass

    def leave_result_to_employee(self):
        """leave_result_to_employee请假结果通知员工"""
        pass
