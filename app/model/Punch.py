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
