from .. import db


class Department(db.Model):  # 部门
    __tablename__ = 'department'
    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    users = db.relationship('User', backref='department')  # ?

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<Department %i %r>' % (self.id, self.name)

    @classmethod
    def findAll():
        return Department.query.all()

    @classmethod
    def getInfoByID(ID):
        return Department.query.get(ID)

    @classmethod
    def getInfoByName(name):
        return Department.query.filter_by(name=name).all()
