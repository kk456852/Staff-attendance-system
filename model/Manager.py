from . import User
from . import Employee
from database.operation import UserInfo


class Manager(User):
    def __init__(self, ID, name, password):
        super().__init__(self, ID, name, password)

    
    def update_employee(self,employeeID):
        """update_employee修改员工信息"""
        
        

    def retrieve_employee(self,employeeID):
        """retrieve_employee查看员工信息"""
        #数据库获取员工工号对应的姓名、职位、部门、工作状态
        employeeName = getEmployNameByEmployeeID(employeeID)
        employeeDepartment = getEmployDepartmentByEmployeeID(employeeID)
        employeeIdentity = getEmployIdentityByEmployeeID(employeeID)
        employeeWorkStatus = getEmployWorkStatusByEmployeeID(employeeID)
        dictEmployInfo = {'ID':employeeID，'name':employeeName，'department':employeeDepartment，'identity':employeeIdentity，'workStatus':employeeWorkStatus}
        return dictEmployInfo


        

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
