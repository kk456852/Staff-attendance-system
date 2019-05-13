class Leave:
    # leaveName请假人姓名 string
    # leaveID请假人工号 int
    # leaveReason请假原因 string
    # leaveStartTime请假开始时间 string
    # leaveEndTime请假预期结束时间 string
    # isLeavePermitted是否准假 bool

    def __init__(self, leaveName, leaveID, leaveReason, leaveStartTime,
                 leaveEndTime):
        self.leaveName = leaveName
        self.leaveID = leaveID
        self.leaveReason = leaveReason
        self.leaveStartTime = leaveStartTime
        self.leaveEndTime = leaveEndTime
        isLeavePermitted = False  # True为准假，初始化为False

    def leave_application_to_director(self):
        """leave_application_to_director请假申请通知主管"""
        pass

    def leave_result_to_employee(self):
        """leave_result_to_employee请假结果通知员工"""
        pass


class Report:
    # reportName销假人姓名 string
    # reportID销假人工号 int
    # reportTime销假时间 string

    def __init__(self, reportName, reportID, reportTime):
        self.reportName = reportName
        self.reportID = reportID
        self.reportTime = reportTime

    def report_to_director(self):
        """report_to_director销假通知主管"""
        pass
