import unittest
from app.model import User
from flask import current_app
from app import db
from app import create_app, db


class TestDb(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    # def test_User(self):
    #     u = User(username="小明", password="123456", position=1,
    #              gender=1, age=22, workStatus=1, departmentId=1)
    #     db.session.add(u)
    #     db.session.commit()
    #
    #     u1 = User.query.filter_by(username="小明").first()
    #     self.assertEqual(u1.position, 1)

    def tearDown(self):
        u1 = User.query.filter_by(username="小明").first()
        db.session.delete(u1)
        db.session.commit()
        db.session.remove()
        self.app_context.pop()
