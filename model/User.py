from database.operation import UserInfo


class User:
    def __init__(self, ID, password):
        self.ID = ID
        self.password = password

    def login(self):
        dPassword = UserInfo().getPasswordByID(self.ID)  # getPasswordByID() 通过员工工号查询密码 
        if(dPassword == self.password):
            return "succeed"
        else:
            return "fail"

    def isManager(self):
<<<<<<< HEAD
          dIdentity = UserInfo().getIdentityByID(self.ID) #getIdentityByUserName()通过员工工号查询其身份
            # dIdentity为用户身份是否为经理，1表示经理
             if(dIdentity == 1)：
                return True
            else:
                return False
=======
        dIdentity = UserInfo().getIdentityByUserName(self.ID)
        # dIdentity为用户身份是否为经理，1表示经理，2表示非经理（普通员工和主管）
        if(dIdentity == 1):
            return True
        else:
            return False
>>>>>>> 648e52faf5ec0135b898038db9ac444c788f4a17
    def logout(self):
        pass

    def updateUser(self):
        pass
