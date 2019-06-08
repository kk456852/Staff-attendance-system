from .. import db
from .Role import Role


class Department(db.Model):  # 部门

    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    users = db.relationship('User', backref='department')  # 包含该部门所有的员工

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<Department %i %r>' % (self.ID, self.name)

    def charge(self):
        return [u for u in self.users if u.role == Role.CHARGE][0]

    @staticmethod
    def ByName(name):
        return Department.query.get(name=name)
