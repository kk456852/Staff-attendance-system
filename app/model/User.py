from ..database import UserInfo


class User:

    def __init__(self, ID, password):
        self.ID = ID
        self.password = password

    def login(self):
        u = UserInfo().getInfoById(self.ID)
        dPassword = u.password  # getPasswordByID() 通过员工工号查询密码
        if(dPassword == self.password):
            return "succeed"
        else:
            return "fail"

    def isManager(self):
        # getIdentityByUserName()通过员工工号查询其身份
        u = UserInfo().getInfoById(self.ID)
        dIdentity = u.identity
        # dIdentity为用户身份是否为经理，1表示经理
        if(dIdentity == 1):
            return True
        else:
            return False

    def logout(self):
        pass

    def addEmail(self, email):
        u = UserInfo().getInfoById(self.ID)
        dEmail = u.email
        if(dEmail != None):
            return "fail"
        else:
            UserInfo().update_Email(self.ID, email)
            return "succeed"

    def updateUser(self, newEmail):
        UserInfo().update_Email(self.ID, newEmail)
        return "succeed"



