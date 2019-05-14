from .Employee import Employee


class Director(Employee):
    def __init__(self, ID, name, password):
        super().__init__(self, ID, name, password)

    def arrange_work(self):
        """arrange_work安排工作班次"""
        pass

    def update_work_arrangement(self):
        """update_work_arrangement修改本部门员工工作安排"""
        pass

    def approve_leave(self):
        """approve_leave请假审批"""
        pass

    def approve_report(self):
        """approve_report销假处理"""
        pass

    def approve_overtime(self):
        """approve_overtime加班审批"""
        pass

    @classmethod
    def getDirectorById(id):
        u = UserInfo().getInfoById(id)
        return Director(u.id, u.name, u.password)