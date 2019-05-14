class User:

    def __init__(self, ID, password):
        self.ID = ID
        self.password = password

    def login(self):
        dPassword = User.getPasswordByID(self.ID)  # getPasswordByID() 通过员工工号查询密码
        if(dPassword == self.password):
            raise Exception

    def isManager(self):
        # getIdentityByUserName()通过员工工号查询其身份
        dIdentity = User.getIdentityByID(self.ID)
        # dIdentity为用户身份是否为经理，1表示经理
        if(dIdentity == 1):
            return True
        else:
            return False

    def logout(self):
        pass

    def addEmail(self, email):
        pass

    def updateUser(self, newEmail):
        pass
