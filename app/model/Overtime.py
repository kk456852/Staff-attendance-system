from .. import db

from datetime import date, time, datetime


class Overtime(db.Model):  # 加班
    """
    表示员工的一次加班申请。

    员工加班需要指定起始日期时间和一个结束时间。
    如果结束时间小于起始时间，说明加班跨越零点，在第二天结束。

    :param staffID 申请人ID
    :param status 表示该申请的状态。0:未审核 1:通过 2:不通过 3:已取消 4:已过期
    :param reason 加班申请原因

    :param submitStamp 提交申请时间戳
    :param reviewStamp 审批时间戳
    """
    ID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey(
        'user.ID'), nullable=False)  # 员工
    reviewerID = db.Column(db.Integer, db.ForeignKey(
        'user.ID'))

    beginDateTime = db.Column(db.DateTime, nullable=False)
    endTime = db.Column(db.Time, nullable=False)

    status = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.String(200))

    submitStamp = db.Column(db.DateTime)
    reviewStamp = db.Column(db.DateTime)

    staff = db.relationship("User", foreign_keys="Overtime.staffID")
    reviewer = db.relationship("User", foreign_keys="Overtime.reviewerID")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<Overtime {}:{}>'.format(self.staff.name, self.beginDateTime)

    def inform_overtime(self):
        pass

    def overtime_application_to_director(self):
        pass

    def overtime_result_to_employee(self):
        pass


class TemporaryOvertime(db.Model):
    """
    临时加班表

    表示由经理创建的一项临时加班类。

    :param submitStamp 提交时间戳
    """
    ID = db.Column(db.Integer, primary_key=True)
    beginDateTime = db.Column(db.DateTime, nullable=False)
    endTime = db.Column(db.Time, nullable=False)

    reason = db.Column(db.String(200))
    submitStamp = db.Column(db.DateTime)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.submitStamp = datetime.now()

    def inform_all(self):
        pass
