from ..database import UserInfo


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
        # getIdentityByUserName()通过员工工号查询其身份
        dIdentity = UserInfo().getIdentityByID(self.ID)
        # dIdentity为用户身份是否为经理，1表示经理
        if(dIdentity == 1):
            return True
        else:
            return False

    def logout(self):
        pass

    def addEmail(self, email):
        dEmail = UserInfo.getEmailByID(self.ID)
        if(dEmail != None):
            return "fail"
        else:
            UserInfo.insert_Email(self.ID, email)
            return "succeed"

    def updateUser(self, newEmail):
        UserInfo.update_Email(self.ID, newEmail)
        return "succeed"
