from datetime import date, time, datetime, timedelta

from .. import db


class WorkArrangement(db.Model):
    """
    工作安排

    :param staff
    """
    ID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey('user.ID'))  # 员工标号
    date = db.Column(db.Date, nullable=False)  # 工作日期
    beginTime = db.Column(db.Time, nullable=False)  # 开始时间
    endTime = db.Column(db.Time, nullable=False)  # 结束时间
    content = db.Column(db.String(200))  # 工作安排

    beginSignID = db.Column(db.Integer, db.ForeignKey(
        'sign_sheet.ID'))
    endSignID = db.Column(db.Integer, db.ForeignKey(
        'sign_sheet.ID'))

    staff = db.relationship("User", foreign_keys="WorkArrangement.staffID")

    beginSign = db.relationship(
        "SignSheet", foreign_keys="WorkArrangement.beginSignID")
    endSign = db.relationship(
        "SignSheet", foreign_keys="WorkArrangement.endSignID")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return "<WorkArrangeMent {}:{} {}-{}>".format(self.staff.name, self.date, self.beginTime, self.endTime)

    @staticmethod
    def ByStaffIDandDate(staffID, date):
        return WorkArrangement.query.filter_by(staffID=staffID, date=date).all()

    @classmethod
    def ByStaffIDandRange(cls, staffID, from_: date, to_: date):
        """
        通过员工ID和时间范围获取该期间所有的工作安排。

        返回期间内所有工作安排的列表。
        """
        return WorkArrangement.query.filter_by(staffID=staffID).filter(
            WorkArrangement.date.between(from_, to_)).all()
