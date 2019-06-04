from .. import db


class SignSheet(db.Model):  # 签到表

    ID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey(
        'user.ID'), nullable=False)  # 员工标号
    type = db.Column(db.Integer, nullable=False)  # 类型 0-日常签到 1-临时加班
    date = db.Column(db.Integer, nullable=False)
    beginTime = db.Column(db.Time)  # 签到上班时间
    endTime = db.Column(db.Time)  # 签到下班时间

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<SignSheet %i %i>' % (self.sheetIdID, self.type)

    @classmethod
    def All():
        return SignSheet.query.all()

    @classmethod
    def ById(sheetId):
        return SignSheet.query.get(sheetId)

    @classmethod
    def BystaffId(staffId):
        return SignSheet.query.filter_by(staffId=staffId).all()

    @classmethod
    def Bytype(type):
        return SignSheet.query.filter_by(type=type).all()

    @classmethod
    def Bydate(date):
        return SignSheet.query.filter_by(date=date).all()


class Punch:
    # punchName打卡人姓名 string
    # punchID打卡人工号 int
    # punchTime打卡时间 string

    def __init__(self, punchName, punchID, punchTime):
        self.punchName = punchName
        self.punchID = punchID
        self.punchTime = punchTime

    def punch(self):
        pass


class WorkSituation:
    # actualStartWork实际上班时间 string
    # actualEndWork实际下班时间 string
    # isLate是否迟到 bool

    def __init__(self, actualStartWork, actualEndWork):
        self.actualStartWork = actualStartWork
        self.actualEndWork = actualEndWork
        isLate = False
