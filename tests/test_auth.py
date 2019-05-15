import unittest

from flask.testing import FlaskClient

from app import create_app


class Test_api(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def test_api(self):
        client: FlaskClient = self.app.test_client()
        data = {
            'UserId' : '123456',
            'password': '123'
        }
        r = client.post('/auth/login',json = data)
        self.assertEquals(r.json['status'], 50000)


    def tearDown(self):
        self.app_context.pop()