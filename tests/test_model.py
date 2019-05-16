import unittest
from app.model import User
from flask import current_app
from app import create_app, db


class Test_DB(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        u = User(ID=10, name="小明", password="123456", identity=1,
                 gender=1)
        u.update_db()

    def test_user(self):
        u1 = User.ByID(10)
        self.assertEqual(u1.identity, 1)
        self.assertEqual(u1.name, "小明")

    def test_login_failed(self):
        with self.assertRaises(Exception):
            User.ByID(10).login('not-password')

    def test_login_success(self):
        u3 = User.ByID(10).login('123456')

    def tearDown(self):
        User.ByID(10).delete_db()
        self.app_context.pop()
