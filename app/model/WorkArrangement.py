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
    content = db.Column(db.String(50))  # 工作安排

    staff = db.relationship("User", foreign_keys="WorkArrangement.staffID")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return "<WorkArrangeMent {}:{} {}-{}>".format(self.staff.name, self.date, self.beginTime, self.endTime)

    @staticmethod
    def ByStaffIDandDate(staffID, date):
        return WorkArrangement.query.filter_by(staffID=staffID, date=date).one()
