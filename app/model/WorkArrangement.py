from .. import db
from .User import User
import datetime
import time


class WorkArrangement(db.Model):
    """
    工作安排

    :param staff
    """
    ID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey('user.ID'))  # 员工标号
    departmentID = db.Column(
        db.Integer, db.ForeignKey('department.ID'))  # 部门标号
    date = db.Column(db.Date, nullable=False)  # 工作日期
    beginTime = db.Column(db.Time, nullable=False)  # 开始时间
    endTime = db.Column(db.Time, nullable=False)  # 结束时间
    content = db.Column(db.String(50))  # 工作安排

    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    now_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))

    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return self.dict()


    @staticmethod
    def show_work_arrangement(staffID):
        """展示工作安排"""
        staffArrengement = WorkArrangement.ByID(staffID);
        return staffArrengement.dict()
        
   
    
  