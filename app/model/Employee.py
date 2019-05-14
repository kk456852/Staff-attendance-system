from .User import User
from ..database import UserInfo


class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees


class Employee(User):
    def __init__(self, ID, name, password, email, workStatus=None):
        super().__init__(ID, password, email)
        self.isDirector = False  # True为主管，False为普通员工，初始化为False
        self.workStatus = workStatus  # workStatus：0为下班，1为上班，2为加班，-1为休假
        
        u = UserInfo().getInfoById(self.ID)
        dIdentity = u.identity
        # dIdentity为用户身份是否为经理，1表示经理,2表示主管，3表示普通员工
        if(dIdentity == 2):
            self.isDirector = True
        else:
            self.isDirector = False

    def retrieve_work_arrangement(self):
        """retrieveWorkArrangement查看工作安排"""
        pass

    def leave_application(self):
        """leave_application申请请假"""
        pass

    def report_application(self):
        """report_application申请销假"""
        pass

    def overtime_application(self):
        """overtimeApplication申请加班"""
        pass

    def punchin(self):
        """punchin打卡上班"""
        pass

    def punchout(self):
        """punchout打卡下班"""
        pass

    def punchin_overtime(self):
        """punchin_overtime打卡加班开始"""
        pass

    def punchout_overtimne(self):
        """punchout_overtimne打卡加班结束"""
        pass

    @classmethod
    def getEmployeeById(id):
        u = UserInfo().getInfoById(id)
        return Employee(u.id, u.name, u.password, u.email, u.workStatus)
