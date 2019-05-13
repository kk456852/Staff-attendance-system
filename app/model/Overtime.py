class Overtime:
    # overtimeThreshold加班阈值 int
    # overtimeName加班人姓名 string
    # overtimeID加班人工号 int
    # isOvertimePermitted是否准许加班 bool

    def __init__(self, overtimeThreshold, overtimeName, overtimeID):
        self.overtimeThreshold = overtimeThreshold
        self.overtimeName = overtimeName
        self.overtimeID = overtimeID
        isOvertimePermitted = False

    def inform_overtime(self):
        """inform_overtime提醒员工加班"""
        pass

    def overtime_application_to_director(self):
        """overtime_application_to_director加班申请通知主管"""
        pass

    def overtime_result_to_employee(self):
        """overtime_result_to_employee加班申请结果通知员工"""
        pass
