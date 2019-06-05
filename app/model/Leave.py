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

    type = db.Column(db.Integer)
    status = db.Column(db.Integer)
    reason = db.Column(db.String(200))

    submitStamp = db.Column(db.DateTime)
    reviewStamp = db.Column(db.DateTime)
    reportStamp = db.Column(db.DateTime)

    staff = db.relationship("User", foreign_keys="Leave.staffID")
    reviewer = db.relationship("User", foreign_keys="Leave.reviewerID")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.submitTime = datetime.now()

    def __repr__(self):
        return '<Leave {}:{}>'.format(self.staffID, self.reason)

    def review(self, info, reviewer):
        """审核"""
        self.reviewer = reviewer
        self.reviewStamp = datetime.now()
        self.update(info)

    def report(self):
        """销假"""
        pass

    def inform_director(self):
        """请假申请通知主管"""
        pass

    def inform_employee(self):
        """请假结果通知员工"""
        pass
