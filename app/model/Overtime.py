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
    endDateTime = db.Column(db.DateTime, nullable=False)

    status = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.String(200))

    submitStamp = db.Column(db.DateTime)
    reviewStamp = db.Column(db.DateTime)

    staff = db.relationship("User", foreign_keys="Overtime.staffID")
    reviewer = db.relationship("User", foreign_keys="Overtime.reviewerID")

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

    def review(self, charge, permit: bool):
        self.status = 1 if permit else 2
        self.reviewer = charge
        self.reviewStamp = datetime.now()
        self.update_db()
        # TODO:此处应通知被审批人

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
