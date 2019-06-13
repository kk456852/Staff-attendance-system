from datetime import datetime, date, time, timedelta

from sqlalchemy import or_

from .. import db
from ..util.dateutil import date_to_datetime


class SignSheet(db.Model):
    """
    签到记录

    包含一个时间戳。将在构造对象时自动生成。
    """

    ID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey(
        'user.ID'), nullable=False)  # 员工标号
    commitStamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.commitStamp = datetime.now()

    def __repr__(self):
        return '<SignSheet {}:{}>'.format(self.user.name, self.commitStamp)

    # @staticmethod
    # def ByStaffIDandDate(staffID, date):
    #    return SignSheet.query.filter_by(staffID=staffID, date=date).all()

    @staticmethod
    def sign(ID):
        """
        签到操作。

        将检查对应的员工是否能够进行签到，以及签到对应工作的类型。
        如果检查失败，抛出异常。
        """
        u = SignSheet(staffID=ID)
        u.count = u.count + 1
        u.update_db()

    @staticmethod
    def ByDate(date):
        pass

    @classmethod
    def ByStaffIDandDate(cls, staffID, date):
        return cls.ByStaffIDandRange(staffID, date, date)

    @classmethod
    def ByStaffIDandRange(cls, staffID, from_: date, to_: date):
        """
        通过员工ID和时间范围获取该期间所有的签到记录。

        注意。由于工作安排可能跨越一整天，所以需要
        """
        assert from_ < to_
        f = date_to_datetime(from_)
        t = date_to_datetime(to_ + timedelta(days=1))

        return cls.query.filter_by(staffID=staffID) \
            .filter(SignSheet.commitStamp > f) \
            .filter(SignSheet.commitStamp < t) \
            .all()

    @classmethod
    def onWork(cls, staffID):
        pass
