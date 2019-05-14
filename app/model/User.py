from ..database import UserInfo


class User:

    def __init__(self, ID, password):
        self.ID = ID
        self.password = password

    def login(self):
        u = UserInfo().getInfoByID(self.ID)
        dPassword = u.password  # getPasswordByID() 通过员工工号查询密码
        if(dPassword == self.password):
            return "succeed"
        else:
            return "fail"

    def judgeIdentity(self):
        # 1表示经理,2表示主管，3表示普通员工
        u = UserInfo().getInfoByID(self.ID)
        return u.identity

    def logout(self):
        pass

    def addEmail(self, email):
        u = UserInfo().getInfoByID(self.ID)
        dEmail = u.email
        if(dEmail != None):
            return "fail"
        else:
            UserInfo().updateEmailByID(self.ID, email)
            return "succeed"

    def updateUser(self, newEmail):
        UserInfo().updateEmailByID(self.ID, newEmail)
        return "succeed"



