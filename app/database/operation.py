from . import Department, Leave, Report, SignSheet, User, WorkArrangement



# ---------------------------查询方法---------------------------------
class UserInfo():
    # 全表查询
    def findAll(self):
        return User.query.all()

    # 根据ID主键查询
    def getInfoByID(self, ID):
        return User.query.get(ID)

    # 根据工号查询姓名
    def getNameByID(self, ID):
        return User.query.filter_by(ID=ID)[0].name

    # 根据员工工号查询密码
    def getPasswordByID(self, ID):
        return User.query.filter_by(ID=ID)[0].password

    # 通过员工工号查询其身份
    def getIdentityByID(self, ID):
        return User.query.filter_by(ID=ID)[0].identity

    # 通过员工工号查询其Email
    def getEmailByID(self, ID):
        return User.query.filter_by(ID=ID)[0].email


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


class OvertimeInfo():
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


# # 复杂查询以及多表关联查询DEMO展示
# class UtilsQuery():
#     def find(self):
#         # 这里通过关联User和Token两张表进行关联查询
#         return User.query.filter(User.id == Token.user_id).filter(Token.user_cname == 'XXXX').all()
#         # return db.session.query(User).filter(User.id == Token.user_id).filter(Token.user_cname=='XXXX').all()
#
#     def findByPage(self, pageNum, size):
#         # 这里展示分页查询
#         if pageNum < 1:
#             pageNum = 1
#         if size < 1:
#             size = 2
#         start = (pageNum - 1) * size
#         end = pageNum * size
#         return User.query.slice(start, end).all()


# ---------------------------更新方法---------------------------------
class UserUpdate():
    # 通过员工ID更新其Email为newEmail
    def updateEmailByID(self, ID, newEmail):
        user = User.query.filter_by(ID=ID).first()
        user.email = newEmail
        db.session.commit()
        return 1

    # 通过字典更新员工信息
    # 字典的格式为员工 工号、姓名、部门、职位、工作状态，指定工号不可更改！！
    # dictEmployeeInfo = {'ID': u.ID, 'name': u.name, 'department': u.department,
    #                         'identity': u.identity, 'workStatus': u.workStatus}
    def updateEmployee(self, ID, dictEmployeeInfo):
        user = User.query.filter_by(ID=ID).first()
        user.name = dictEmployeeInfo['name']
        user.identity = dictEmployeeInfo['identity']
        user.departmentID = dictEmployeeInfo['department']
        user.workStatus = dictEmployeeInfo['workStatus']
        db.session.commit()
        return 1


# ---------------------------插入方法---------------------------------
# ---------------------------删除方法---------------------------------