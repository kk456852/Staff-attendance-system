from .. import db
from .User import User

class WorkArrangement(db.Model):  # 工作安排

    arragementID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey('user.ID'))  # 员工标号
    departmentID = db.Column(
        db.Integer, db.ForeignKey('department.ID'))  # 部门标号
    workDate = db.Column(db.Date, nullable=False)  # 工作日期
    beginTime = db.Column(db.Time, nullable=False)  # 开始时间
    endTime = db.Column(db.Time, nullable=False)  # 结束时间
    assignment = db.Column(db.String(50))  # 工作安排

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return self.dict()


    #
    # 数据库方法
    #
    
    @staticmethod
    def findAll():
        return WorkArrangement.query.all()

    @staticmethod
    def getInfoByID(arragementID):
        return WorkArrangement.query.get(arragementID)

    @staticmethod
    def getInfoBystaffID(staffID):
        return WorkArrangement.query.filter_by(staffID=staffID).all()

    @staticmethod
    def getInfoBydepID(departmentID):
        return WorkArrangement.query.filter_by(departmentID=departmentID).all()


