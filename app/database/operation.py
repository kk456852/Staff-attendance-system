from . import Department, Leave, Report, SignSheet, User, WorkArrangement

# ---------------------------查询方法---------------------------------
class UserInfo():
    # 全表查询
    def findAll(self):
        return User.query.all()

    # 根据ID主键查询
    def getInfoByID(self, ID):
        return User.query.get(ID)

    # 自定义查询条件
    def getNameByID(self, ID):
        return User.query.filter_by(ID=ID)[0].username

    # 根据员工工号查询密码
    def getPasswordByID(self, ID):
        return User.query.filter_by(ID=ID)[0].password

    # 通过员工工号查询其身份
    def getIdentityByID(self, ID):
        return User.query.filter_by(ID=ID)[0].identity

    # 通过员工工号查询其Email
    def getEmailByID(self, ID):
        return User.query.filter_by(ID=ID)[0].email

    # 通过员工ID更新其Email为newEmail
    def updateEmailByID(self, ID, newEmail):
        user = User.query.filter_by(ID=ID).first()
        user.email = newEmail
        return 1


class DepartmentInfo():
    def findAll(self):
        return Department.query.all()

    def getInfoByID(self, ID):
        return Department.query.get(ID)

    def getInfoByName(self, name):
        return Department.query.filter_by(name=name).all()


class WorkArrangementInfo():
    def findAll(self):
        return WorkArrangement.query.all()

    def getInfoByID(self, arragementID):
        return WorkArrangement.query.get(arragementID)

    def getInfoBystaffID(self, staffID):
        return WorkArrangement.query.filter_by(staffID=staffID).all()

    def getInfoBydepID(self, departmentID):
        return WorkArrangement.query.filter_by(departmentID=departmentID).all()


class SignSheetInfo():
    def findAll(self):
        return SignSheet.query.all()

    def getInfoByID(self, sheetID):
        return SignSheet.query.get(sheetID)

    def getInfoBystaffID(self, staffID):
        return SignSheet.query.filter_by(staffID=staffID).all()

    def getInfoBytype(self, type):
        return SignSheet.query.filter_by(type=type).all()

    def getInfoBydate(self, date):
        return SignSheet.query.filter_by(date=date).all()


class LeaveInfo():
    def findAll(self):
        return Leave.query.all()

    def getInfoByID(self, leaveID):
        return Leave.query.get(leaveID)

    def getInfoBystaffID(self, staffID):
        return Leave.query.filter_by(staffID=staffID).all()

    def getInfoByleaveDate(self, leaveDate):
        return Leave.query.filter_by(leaveDate=leaveDate).all()

    def getInfoByPermitted(self, permitted):
        return Leave.query.filter_by(isLeavePermitted=permitted).all()


class ReportInfo():
    def findAll(self):
        return Report.query.all()

    def getInfoByID(self, reportID):
        return Report.query.get(reportID)

    def getInfoByleaveID(self, leaveID):
        return Report.query.filter_by(leaveID=leaveID).all()


class Overtime():
    def findalll(self):
        return Overtime.query.all()

    def getInfoByID(self, overtimeID):
        return Overtime.query.get(overtimeID)

    def getInfoBystaffID(self, staffID):
        return Overtime.query.filter_by(staffID=staffID).all()

    def getInfoByThreshold(self, overtimeThreshold):
        return Overtime.query.filter_by(overtimeThreshold=overtimeThreshold).all()

    def getInfoBypermitted(self, permitted):
        return Overtime.query.filter_by(isOvertimePermitted=permitted).all()

