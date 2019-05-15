from .User import User
from .Department import Department
from .Employee import Employee


class Manager:
    def __init__(self, user):
        self.user = user

    def update_employee(self, employee):
        """修改员工信息

        :param employee : Employee
        """
        employee.user.update_self()

    def retrieve_employee(self, employeeID):
        """查看员工信息"""
        return Employee.ByID(employeeID)

    def delete_employee(self, employee):
        """人员删除"""
        User.ByID(employee.id).delete_self()

    def update_position(self):
        """身份修改"""
        pass

    def create_employee(self):
        """人员添加"""
        pass

    def release_temporary_overtime(self):
        """发布全单位加班"""
        pass

    def retrieve_work_situation(self):
        """查看上班情况"""
        pass

    @staticmethod
    def getManagerById(ID):
        u = User.getInfoByID(ID)
        if u.identity != 3:
            raise Exception("Not a Manager")
        return Manager(u)
