from datetime import date, datetime, time, timedelta

from sqlalchemy import or_

from .. import db
from ..util.dateutil import date_to_datetime
from ..util.mail import send_mail
from .Department import Department


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
        return '<Leave {}:{} {}-{}>'.format(self.staff.name, self.reason, self.beginDateTime, self.endDateTime)

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

    @staticmethod
    def new(staff, info: dict):
        # TODO: 此处应该查询请假时间段是否在正常范围内，否则抛出异常
        l = Leave(**info)
        l.staff = staff
        l.status = 0
        l.update_db()
        # l.inform_charge()

    def review(self, charge, permit: bool):
        """主管审核"""
        self.status = 1 if permit else 2
        self.reviewer = charge
        self.reviewStamp = datetime.now()
        self.update_db()
        self.inform_staff()

    def report(self):
        """销假"""
        # TODO: 进行状态、时间、权限检查
        self.status = 4
        self.reportStamp = datetime.now()

    def inform_charge(self):
        """请假申请通知主管"""
        # TODO: 应转化成异步任务
        charge = self.staff.department.charge()
        if charge.email:
            send_mail(to=charge.email, subject='新请假', template='leave_new.html',
                      charge=charge, leave=self)

    def inform_staff(self):
        """请假结果通知员工"""
        # TODO: 应转化成异步任务
        if self.staff.email:
            send_mail(to=self.staff.email, subject='请假审批结果', template='leave_review.html',
                      leave=self)

    @classmethod
    def ByStaffIDandDate(cls, staffID, date):
        return cls.ByStaffIDandRange(staffID, date, date)

    @classmethod
    def ByStaffIDandRange(cls, staffID, from_: date, to_: date):
        """
        通过员工ID和时间范围获取该期间所有的工作安排。

        返回期间内所有工作安排的列表。
        """
        f = date_to_datetime(from_)
        t = date_to_datetime(to_ + timedelta(days=1))

        return cls.query.filter_by(staffID=staffID).filter(or_(Leave.endDateTime > f,  Leave.beginDateTime < t)).all()
