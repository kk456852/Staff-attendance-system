from datetime import datetime

from .. import db


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

    @staticmethod
    def ByStaffIDandDate(staffID, date):
        return SignSheet.query.filter_by(staffID=staffID, date=date).all()

    @staticmethod
    def sign(ID):
        """
        签到操作。

        将检查对应的员工是否能够进行签到，以及签到对应工作的类型。
        如果检查失败，抛出异常。
        """
        SignSheet(staffID=ID).update_db()
