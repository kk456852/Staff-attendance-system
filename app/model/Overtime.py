from datetime import date, datetime, time, timedelta

from sqlalchemy import or_

from .. import db
from ..util.dateutil import date_to_datetime
from ..util.mail import send_mail


class Overtime(db.Model):  # 加班
    """
    表示员工的一次加班申请。

    员工加班需要指定起始日期时间和一个结束时间。
    如果结束时间小于起始时间，说明加班跨越零点，在第二天结束。

    :param staffID 申请人ID
    :param status 表示该申请的状态。0:未审核 1:通过 2:不通过 3:已取消 4:已过期 5:全员性加班
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
    endDateTime = db.Column(db.DateTime, nullable=False)

    status = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.String(200))

    submitStamp = db.Column(db.DateTime)
    reviewStamp = db.Column(db.DateTime)

    beginSignID = db.Column(db.Integer, db.ForeignKey(
        'sign_sheet.ID'))
    endSignID = db.Column(db.Integer, db.ForeignKey(
        'sign_sheet.ID'))

    staff = db.relationship("User", foreign_keys="Overtime.staffID")
    reviewer = db.relationship("User", foreign_keys="Overtime.reviewerID")
    beginSign = db.relationship(
        "SignSheet", foreign_keys="Overtime.beginSignID")
    endSign = db.relationship("SignSheet", foreign_keys="Overtime.endSignID")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.submitStamp = datetime.now()

    def __repr__(self):
        return '<Overtime {}:{}>'.format(self.staff.name, self.beginDateTime)

    def to_staff(self):
        """
        返回给员工的信息。

        ==> 想不到更好的实现方式了。
        """
        res = self.dict()
        res["reviewerName"] = self.reviewer.name if self.reviewer else None
        res.pop("reviewerID")
        return res

    def to_charge(self):
        """
        返回给主管的信息。包含申请人的姓名。
        """
        res = self.dict()

        res["reviewerName"] = self.reviewer.name if self.reviewer else None
        res["staffName"] = self.staff.name
        return res

    @staticmethod
    def new(staff, info: dict):
        # TODO: 此处应该查询请假时间段是否在正常范围内，否则抛出异常
        o = Overtime(**info)
        o.staff = staff
        o.status = 0
        o.update_db()
        # o.inform_charge()
        # 通知template: overtime_new.html
        staff.inform_charge()

    def inform_charge(self):
        """
        发送邮件通知主管。
        """
        send_mail(to=self.reviewer.email, subject="员工加班请求", template="overtime_new.html",
                  overtime=self, staff=self.staff, charge=self.reviewer)

    def review(self, charge, permit: bool):
        self.status = 1 if permit else 2
        self.reviewer = charge
        self.reviewStamp = datetime.now()
        self.update_db()
        self.inform_staff()

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

        return cls.query.filter_by(staffID=staffID).filter(or_(Overtime.endDateTime > f,  Overtime.beginDateTime < t)).all()

    def inform_staff(self):
        """
        发送邮件通知员工审批结果。
        """
        send_mail(to=self.staff, subject="加班审批结果通知",
                  template="overtime_review.html", overtime=self, staff=self.staff)
