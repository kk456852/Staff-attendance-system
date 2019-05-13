from . import User
from . import Employee
from database.operation import UserInfo


class Manager(User):
    def __init__(self, ID, name, password):
        super().__init__(self, ID, name, password)

    
    def update_employee(self,**dictEmployeeInfo):#字典的格式为员工 工号、姓名、部门、职位、工作状态，指定工号不可更改！！
        """update_employee修改员工信息"""
        employeeID = dictEmployeeInfo['employeeID']
        #先获取数据库中原本的该员工
        employeeName = UserInfo.getEmployNameByEmployeeID(employeeID)
        employeeDepartment = UserInfo.getEmployDepartmentByEmployeeID(employeeID)
        employeeIdentity = UserInfo.getEmployIdentityByEmployeeID(employeeID)
        employeeWorkStatus = UserInfo.getEmployWorkStatusByEmployeeID(employeeID)
        
        #把字典中的信息与原信息比对，若发生更改，则更新数据库相应的属性
        if(dictEmployeeInfo['employeeName'] != employeeName)
           employeeName = dictEmployeeInfo['employeeName']
           UserInfo.update_employee(employeeID,employeeName)

        if(dictEmployeeInfo['employeeDepartment'] != employeeDepartment)
           employeeDepartment = dictEmployeeInfo['employeeDepartment']
           UserInfo.update_employee(employeeID,employeeDepartment)

        if(dictEmployeeInfo['employeeIdentity'] != employeeIdentity)
           employeeIdentity = dictEmployeeInfo['employeeIdentity']
           UserInfo.update_employee(employeeID,employeeIdentity)

        if(dictEmployeeInfo['employeeWorkStatus'] != employeeWorkStatus)
           employeeWorkStatus = dictEmployeeInfo['employeeWorkStatus']
           UserInfo.update_employee(employeeID,employeeWorkStatus)
        

    def retrieve_employee(self,employeeID):
        """retrieve_employee查看员工信息"""
        #数据库获取员工工号对应的姓名、部门、职位、工作状态
        employeeName = UserInfo.getEmployNameByEmployeeID(employeeID)
        employeeDepartment = UserInfo.getEmployDepartmentByEmployeeID(employeeID)
        employeeIdentity = UserInfo.getEmployIdentityByEmployeeID(employeeID)
        employeeWorkStatus = UserInfo.getEmployWorkStatusByEmployeeID(employeeID)
        dictEmployeeInfo = {'ID':employeeID，'name':employeeName，'department':employeeDepartment，'identity':employeeIdentity，'workStatus':employeeWorkStatus}
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
