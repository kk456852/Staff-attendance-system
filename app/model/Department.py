from .. import db


class Department(db.Model):  # 部门

    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    users = db.relationship('User', backref='department')  # 包含该部门所有的员工

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<Department %i %r>' % (self.ID, self.name)

    @staticmethod
    def All():
        return Department.query.all()

    @staticmethod
    def ByID(ID):
        return Department.query.get(ID)

    @staticmethod
    def ByName(name):
        return Department.query.get(name=name)

    def update_db(self):
        """将修改后的对象，或者新增的对象添加/修改到数据库中。

        :raise InvalidRequestError
        """
        db.session.add(self)
        db.session.commit()

    def delete_db(self):
        """删除数据库中的该对象。

        :raise InvalidRequestError
        """
        db.session.delete(self)
        db.session.commit()
