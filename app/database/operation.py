from . import Department, Leave, Report, SignSheet, User, WorkArrangement

Base = declarative_base()
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

session = Session()

class UserInfo():
    """查询方法"""
    # 全表查询

    def findAll(self):
        return User.query.all()

    # 根据ID主键查询
    def getInfoById(self, id):
        return User.query.get(id)

    # 自定义查询条件
    def getInfoByUserName(self, userName):
        #return User.query.filter_by(username=userName).all()
        return session.query(User).filter(User.username==userName).all()

    def getIdentityByID(self, id):
        raise NotImplementedError

    # 根据员工工号查询姓名
    def getNameByID(self, id):
        return User.query.filter_by(id=id)[0].username

    # 根据员工工号查询密码
    def getPasswordByID(self, id):
        return User.query.filter_by(id=id)[0].password

    # 通过员工工号查询其身份
    def getIdentityByID(self, id):
        return User.query.filter_by(id=id)[0].position

    # 通过员工工号查询其Email
    def getEmailByID(self, id):
        return User.query.filter_by(id=id)[0].email

    # 通过员工ID更新其Email为newEmail
    def updateEmailByID(self, id, newEmail):
        user = User.query.filter_by(id=id).first()
        user.email = newEmail
        return 1


class DepartmentInfo():
    def findAll(self):
        return Department.query.all()

    def getInfoById(self, id):
        return Department.query.get(id)

    def getInfoByName(self, name):
        return Department.query.filter_by(name=name).all()


class WorkArrangementInfo():
    def findAll(self):
        return WorkArrangement.query.all()

    def getInfoById(self, arragementId):
        return WorkArrangement.query.get(arragementId)

    def getInfoBystaffId(self, staffId):
        return WorkArrangement.query.filter_by(staffId=staffId).all()

    def getInfoBydepId(self, departmentId):
        return WorkArrangement.query.filter_by(departmentId=departmentId).all()


class SignSheetInfo():
    def findAll(self):
        return SignSheet.query.all()

    def getInfoById(self, sheetId):
        return SignSheet.query.get(sheetId)

    def getInfoBystaffId(self, staffId):
        return SignSheet.query.filter_by(staffId=staffId).all()

    def getInfoBytype(self, type):
        return SignSheet.query.filter_by(type=type).all()

    def getInfoBydate(self, date):
        return SignSheet.query.filter_by(date=date).all()


class LeaveInfo():
    def findAll(self):
        return Leave.query.all()

    def getInfoById(self, leaveId):
        return Leave.query.get(leaveId)

    def getInfoBystaffId(self, staffId):
        return Leave.query.filter_by(staffId=staffId).all()

    def getInfoByleaveDate(self, leaveDate):
        return Leave.query.filter_by(leaveDate=leaveDate).all()

    def getInfoByPermitted(self, permitted):
        return Leave.query.filter_by(isLeavePermitted=permitted).all()


class ReportInfo():
    def findAll(self):
        return Report.query.all()

    def getInfoById(self, reportId):
        return Report.query.get(reportId)

    def getInfoByleaveId(self, leaveId):
        return Report.query.filter_by(leaveId=leaveId).all()


class Overtime():
    def findalll(self):
        return Overtime.query.all()

    def getInfoById(self, overtimeId):
        return Overtime.query.get(overtimeId)

    def getInfoBystaffId(self, staffId):
        return Overtime.query.filter_by(staffId=staffId).all()

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
