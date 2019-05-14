from .User import User
from .Employee import Employee
from ..database import UserInfo


class Manager(User):
    def __init__(self, ID, name, password):
        super(self, ID, name, password)

    # 字典的格式为员工 工号、姓名、部门、职位、工作状态，指定工号不可更改！！
    def update_employee(self, **dictEmployeeInfo):
        """update_employee修改员工信息"""
        employeeID = dictEmployeeInfo['employeeID']
        UserInfo.update_employee(employeeID, **dictEmployeeInfo)

    


    def retrieve_employee(self, employeeID):
        """retrieve_employee查看员工信息"""
        # 数据库获取员工工号对应的姓名、部门、职位、工作状态
        u = UserInfo().getInfoById(employeeID)
        dictEmployeeInfo = {'ID': u.ID, 'name': u.name, 'department': u.department,
                            'identity': u.identity, 'workStatus': u.workStatus}
        return dictEmployeeInfo

    def delete_employee(self):
        """delete_employee人员删除"""
        pass

    def update_position(self):
        """update_position身份修改"""
        pass

    def create_employee(self):
        """create_employee人员添加"""
        pass

    def release_temporary_overtime(self):
        """release_temporary_overtime发布全单位加班"""
        pass

    def retrieve_work_situation(self):
        """retrieve_work_situation查看上班情况"""
        pass

    @classmethod
    def getManagerById(id):
        u = UserInfo().getInfoById(id)
        return Manager(u.id, u.name, u.password)
