from .. import db
from .User import User


class Overtime(db.Model):  # 加班
    """
    ## 加班类
    表示员工的一次加班申请

    员工加班需要指定一个起始时间和一个结束时间。

    :param staffID/user 员工的
    :param status 表示该申请的状态
    :param isTemporary 表示是否是
    """
    ID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer, db.ForeignKey(
        'user.ID'), nullable=False)  # 员工

    beginTime = db.Column(db.DateTime, nullable=False)
    endTime = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Boolean)  # 是否准许加班 0-未审核 1-通过 2-不通过

    isTemporary = db.Column(db.Boolean)

    submitTime = db.Column(db.DateTime)
    permitTime = db.Column(db.DateTime)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<Overtime {}:{}>'.format(self.staffID, self.beginTime)

    @staticmethod
    def ByDepartmentID(department_id):
        return Overtime.query.join(User).filter(User.departmentID == 1).all()

    def inform_overtime(self):
        pass

    def overtime_application_to_director(self):
        pass

    def overtime_result_to_employee(self):
        pass


class TemporaryOvertime(db.Model):
    """
    临时加班表

    表示由经理创建的一项临时加班类。


    """
    ID = db.Column(db.Integer, primary_key=True)
    beginTime = db.Column(db.DateTime, nullable=False)
    endTime = db.Column(db.DateTime, nullable=False)
    submitTime = db.Column(db.DateTime)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def inform_all(self):
        pass
