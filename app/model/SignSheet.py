from .. import db


class SignSheet(db.Model):
    """
    签到记录

    包含一个时间戳
    """

    ID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey(
        'user.ID'), nullable=False)  # 员工标号
    timeStamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<SignSheet {}>'.format(self.timeStamp)

    
    @staticmethod
    def BystaffID(staffID):
        return SignSheet.query.filter_by(staffID=staffID).all()
