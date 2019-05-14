class TemporaryOvertime:
    # overtimeStartTime加班开始时间 string
    # overtimeEndTime加班结束时间 string

    def __init__(self, overtimeStartTime, overtimeEndTime):
        self.overtimeStartTime = overtimeStartTime
        self.overtimeEndTime = overtimeEndTime

    def inform_temporary_overtime(self):
        """inform_temporary_overtime全员加班通知员工"""
        pass


class OvertimeSituation:
    # temporaryOvertimeName加班人姓名 string
    # emporaryOvertimeID加班人工号 int
    # isEmporaryOvertime是否参与加班 bool

    def __init__(self, temporaryOvertimeName, emporaryOvertimeID):
        self.temporaryOvertimeName = temporaryOvertimeName
        self.emporaryOvertimeID = emporaryOvertimeID
        isEmporaryOvertime = False
