from . import User


class Manager(User):
    def __init__(self, ID, name, password):
        super(self, ID, name, password)

    def update_employee(self):
        """update_employee修改员工信息"""
        pass

    def retrieve_employee(self):
        """retrieve_employee查看员工信息"""
        pass

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
