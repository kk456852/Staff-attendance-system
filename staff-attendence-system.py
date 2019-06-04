import os

from flask_migrate import Migrate

from app import create_app, db

app = create_app()

migrate = Migrate(app, db)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.cli.command()
def ipy():
    """Open IPython Debug Shell"""
    ctx = app.app_context()
    ctx.push()
    from app.model import (Department, Leave, Role,
                           Overtime, TemporaryOvertime,
                           SignSheet, User)
    __import__('IPython').embed()
    ctx.pop()


@app.cli.command()
def init_db():
    """Init database and create basic test data."""
    file = 'db.sqlite3'
    if os.path.exists(file):
        os.remove(file)

    db.drop_all()
    db.create_all()
    create_test_data()


def create_test_data():
    """新建测试数据"""
    from app.model import (Department, Leave, Role,
                           Overtime, TemporaryOvertime,
                           SignSheet, User, WorkArrangement)
    departments = [Department(ID=1, name="销售"),
                   Department(ID=2, name="财务"),
                   Department(ID=3, name="技术")]
    users = [User(ID=1, password="123456", name="老王",
                  role=Role.MANAGER, gender=False),
             User(ID=2, password="123456", name="李主任",
                  role=Role.CHARGE, gender=True, department=departments[0]),
             User(ID=3, password="123456", name="刘主任",
                  role=Role.CHARGE, gender=False, department=departments[1]),
             User(ID=4, password="123456", name="小明",
                  role=Role.STAFF, gender=False, department=departments[0]),
             User(ID=5, password="123456", name="小刚",
                  role=Role.STAFF, gender=False, department=departments[0]),
             User(ID=6, password="123456", name="小静",
                  role=Role.STAFF, gender=True, department=departments[1]),
             User(ID=7, password="123456", name="小芳",
                  role=Role.STAFF, gender=True, department=departments[1])]

    for d in departments:
        d.update_db()

    for u in users:
        u.update_db()
