from .. import db
from .User import User
import datetime
import time

class WorkArrangement(db.Model):  # 工作安排

    arragementID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey('user.ID'))  # 员工标号
    departmentID = db.Column(
        db.Integer, db.ForeignKey('department.ID'))  # 部门标号
    workDate = db.Column(db.Date, nullable=False)  # 工作日期
    beginTime = db.Column(db.Time, nullable=False)  # 开始时间
    endTime = db.Column(db.Time, nullable=False)  # 结束时间
    assignment = db.Column(db.String(50))  # 工作安排

    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    now_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))

    
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

    @staticmethod
    def ByID(ID):
        """根据ID构造对象
        数据库中没有此ID时抛出异常

        :returns User
        :raise UserNotFoundException
        """
        w = WorkArrangement.query.get(ID)
        return w

    def update_db(self):
        """将修改后的对象，或者新增的对象添加/修改到数据库中。
        失败时抛出异常。

        :raise InvalidRequestError
        """
        db.session.add(self)
        db.session.commit()

    def delete_db(self):
        """删除数据库中该对象对应的用户。
        失败时抛出异常。

        :raise InvalidRequestError
        """
        db.session.delete(self)
        db.session.commit()


