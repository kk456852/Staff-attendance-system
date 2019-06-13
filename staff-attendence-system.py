import os

from app import create_app, db

app = create_app()


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
                           SignSheet, User, WorkArrangement)
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
    from itertools import chain
    from datetime import date, time, datetime
    from app.model import (Department, Leave, Role,
                           Overtime, TemporaryOvertime,
                           SignSheet, User, WorkArrangement)
    signsheet = [SignSheet(ID=1, staffID=1,
                           commitStamp=datetime(2000, 1, 1, 1, 1))]
    departments = [Department(ID=1, name="销售"),
                   Department(ID=2, name="财务"),
                   Department(ID=3, name="技术")]
    users = [User(ID=1, password="123456", name="老王",
                  role=Role.MANAGER, gender=False),
             User(ID=2, password="123456", name="马大叔",
                  role=Role.CHARGE, gender=True, birthday=datetime(1978, 2, 15), department=departments[0], email="mahaoqu@gmail.com"),
             User(ID=3, password="123456", name="木木",
                  role=Role.CHARGE, birthday=datetime(1981, 11, 30), gender=False, department=departments[1], email="390400239@qq.com"),
             User(ID=4, password="123456", name="小马",
                  role=Role.STAFF, gender=False, department=departments[0], email="mahaoqu@qq.com"),
             User(ID=5, password="123456", name="小刚",
                  role=Role.STAFF, gender=False, department=departments[0]),
             User(ID=6, password="123456", name="小静",
                  role=Role.STAFF, gender=True, department=departments[1]),
             User(ID=7, password="123456", name="小芳",
                  role=Role.STAFF, gender=True, department=departments[1])]

    for d in chain(departments, users):
        d.update_db()

    def overtime(b, e, r):
        return {
            "beginDateTime": b,
            "endDateTime": e,
            "reason": r
        }

    users[3].new_overtime(
        overtime(datetime(2019, 6, 14, 22, 0, 0), datetime(2019, 6, 15, 1, 0, 0), "没弄完"))

    Leave(staff=users[3], status=0, type=0, reason="回家种地", beginDateTime=datetime(
        2019, 6, 13), endDateTime=datetime(2019, 6, 22)).update_db()

    w = WorkArrangement(staff=users[3], date=date(2019, 6, 12), beginTime=time(
        8, 0), endTime=time(18, 0))

    s1 = SignSheet(user=users[4])
    s1.commitStamp = datetime(2019, 6, 12, 8, 5)
    s1.update_db()

    s2 = SignSheet(user=users[4])
    s2.commitStamp = datetime(2019, 6, 12, 17, 55)
    s2.update_db()

    w.beginSign = s1
    w.endSign = s2
    w.update_db()
