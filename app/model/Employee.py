from .User import User


class Employee:

    def __init__(self, user):
        self.user = user

    def update(self):
        pass

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

    @staticmethod
    def getEmployeeById(ID):
        u = User.getInfoByID(ID)
        if u.identity == 3:
            raise Exception("Not a Manager")
        return Employee(u)

    @staticmethod
    def All():
        return [Employee(x) for x in User.query.filter(User.identity != 3).all()]
