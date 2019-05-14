from .User import User
from .Employee import Employee


class Manager(User):
    def __init__(self, ID, name, password):
        super(self, ID, name, password)

    # 字典的格式为员工 工号、姓名、部门、职位、工作状态，指定工号不可更改！！
    def update_employee(self, **dictEmployeeInfo):
        """update_employee修改员工信息"""
        employeeID = dictEmployeeInfo['employeeID']
        # 先获取数据库中原本的该员工
        employeeName = User.getEmployNameByEmployeeID(employeeID)
        employeeDepartment = User.getEmployDepartmentByEmployeeID(
            employeeID)
        employeeIdentity = User.getEmployIdentityByEmployeeID(employeeID)
        employeeWorkStatus = User.getEmployWorkStatusByEmployeeID(
            employeeID)

        # 把字典中的信息与原信息比对，若发生更改，则更新数据库相应的属性
        if(dictEmployeeInfo['employeeName'] != employeeName):
            employeeName = dictEmployeeInfo['employeeName']
            User.update_employee(employeeID, employeeName)

        if(dictEmployeeInfo['employeeDepartment'] != employeeDepartment):
            employeeDepartment = dictEmployeeInfo['employeeDepartment']
            User.update_employee(employeeID, employeeDepartment)

        if(dictEmployeeInfo['employeeIdentity'] != employeeIdentity):
            employeeIdentity = dictEmployeeInfo['employeeIdentity']
            User.update_employee(employeeID, employeeIdentity)

        if(dictEmployeeInfo['employeeWorkStatus'] != employeeWorkStatus):
            employeeWorkStatus = dictEmployeeInfo['employeeWorkStatus']
            User.update_employee(employeeID, employeeWorkStatus)

    def retrieve_employee(self, employeeID):
        """retrieve_employee查看员工信息"""
        # 数据库获取员工工号对应的姓名、部门、职位、工作状态
        u = UserInfo().getInfoByID(employeeID)
        d = DepartmentInfo().getInfoByID(u.departmenID)
    
        dictEmployeeInfo = {'ID': u.ID, 'name': u.name, 'department': d.name,
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
    def getManagerById(ID):
        u = UserInfo().getInfoByID(ID)
        return Manager(u.ID, u.name, u.password)
