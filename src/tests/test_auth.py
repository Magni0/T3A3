from main import db, create_app
import unittest
import json

class TestAuth(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()

        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db-c", "seed"])

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()
    
    def test_register(self):
        response = self.client.post(
            "/userprofile/register",
            data=json.dumps({
                "displayname": "ThisIsADisplayName",
                "username": "ThiIsAUsername",
                "email": "randomemail@email.com",
                "password": "testregpassword"
                }),
            content_type="application/json"
        )

        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)

    def test_login(self):
        response = self.client.get(
            "/userprofile/login",
            data=json.dumps({
                "email": "TestEmail1@test.com",
                "password": "testpassword"
            }),
            content_type="application/json"
        )

        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)