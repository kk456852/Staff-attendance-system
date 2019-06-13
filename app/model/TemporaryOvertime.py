from datetime import datetime

from .. import db
from .User import User
from .Role import Role
from ..util.mail import send_mail


class TemporaryOvertime(db.Model):
    """
    经理发起的临时加班类。

    员工可以看到当前所有没有开始的临时加班。并且可以在加班结束前将其加入到自己的加班申请中。
    """
    ID = db.Column(db.Integer, primary_key=True)
    beginDateTime = db.Column(db.DateTime, nullable=False)
    endDateTime = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.String(200))

    submitStamp = db.Column(db.DateTime)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.submitStamp = datetime.now()

    def inform_staffs(self):
        """
        通知所有不在请假的员工开启了新的全员加班请求。

        为每个员工发送邮件。
        """
        for u in User.All():
            if not u.in_leave(self.beginDateTime) and not u.in_leave(self.endDateTime) and u.role != Role.MANAGER:
                self.inform_staff(u)

    def inform_staff(self, user):
        #TODO: 发送临时加班邮件(非请假状态)
        send_mail(to = user.email, subject = "新临时加班", template = "temporary_overtime_new.html", temporaryOvertime = self, user = user)
        pass

    @staticmethod
    def new(info):
        pass
        t = TemporaryOvertime(**info)
        t.update_db()
        t.inform_staffs()

    # def inform_temporary_overtime(self, startTime, endTime):
    #     """全员加班通知员工"""
    #     self.startTime = startTime
    #     self.endTime = endTime
    #     for user in listUser:
    #         if not user.in_leave(startTime) and not user.in_leave(endTime):
