from database.operation import *


class User:
    def __init__(self, ID, password):
        self.ID = ID
        self.password = password

    def login(self):
        dPassword = UserInfo().getPasswordByUserName(self.ID)
        if(dPassword == self.password):
            return "success"
        else:
            return "fail"

    def isManager(self):
          dIdentity = UserInfo().getIdentityByUserName(self.ID)
            # dIdentity为用户身份是否为经理，1表示经理，2表示非经理（普通员工和主管）
             if(dIdentity == 1)：
                return True
            else:
                return False
    def logout(self):
        pass

    def updateUser(self):
        pass
