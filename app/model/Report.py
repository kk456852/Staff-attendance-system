from .. import db


class Report(db.Model):  # 销假

    reportID = db.Column(db.Integer, primary_key=True)
    leaveID = db.Column(db.Integer, db.ForeignKey(
        'leave.leaveID'), nullable=False)  # 对应的请假id
    reportTime = db.Column(db.Time, nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<Report %i %i>' % (self.reportID, self.leaveID)

    @classmethod
    def findAll():
        return Report.query.all()

    @classmethod
    def getInfoById(reportId):
        return Report.query.get(reportId)

    @classmethod
    def getInfoByleaveId(leaveId):
        return Report.query.filter_by(leaveId=leaveId).all()

    def report_to_director(self):
        """销假通知主管"""
        pass
