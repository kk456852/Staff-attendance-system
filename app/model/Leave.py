from datetime import datetime

from .. import db


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

    def inform_director(self):
        """请假申请通知主管"""
        pass

    def inform_employee(self):
        """请假结果通知员工"""
        pass
