import unittest

from flask.testing import FlaskClient

from app import create_app
from app.model import User


class Test_api(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        u = User(ID=10, name="小明", password="123456", identity=1,
                 gender=1)
        u.update_db()

    def test_api(self):
        client = self.app.test_client()
        data = {
            'id': '123456',
            'password': '123'
        }
        r = client.post('/auth/login', json=data)
        self.assertEquals(r.json['status'], 50001)

    def test_login(self):
        data = {"id": 10, "password": "123456"}

        client = self.app.test_client()
        client.preserve_context = True
        self.assertEqual(client.get('/auth/test').json['status'], 50000)
        self.assertEqual(client.post(
            '/auth/login', json=data).json['status'], 20000)
        self.assertEqual(client.get('/auth/test').json['status'], 20000)
        self.assertEqual(client.post('/auth/logout').json['status'], 20000)

    def tearDown(self):
        User.ByID(10).delete_self()
        self.app_context.pop()
