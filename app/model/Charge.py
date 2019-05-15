from .. import db

from .Employee import Employee


class Charge(Employee):
    def __init__(self, user):
        super().__init__(self, user)

    def arrange_work(self):
        """安排工作班次"""
        pass

    def update_work_arrangement(self):
        """修改本部门员工工作安排"""
        pass

    def approve_leave(self):
        """请假审批"""
        pass

    def approve_report(self):
        """销假处理"""
        pass

    def approve_overtime(self):
        """加班审批"""
        pass
