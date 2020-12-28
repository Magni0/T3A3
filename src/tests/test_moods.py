from main import db, create_app
import unittest
import json

class TestMoods(unittest.TestCase):
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

    def test_moods_retrive(self):
        response = self.client.get("/tracks/1/moods/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)

    def test_mood_increment(self):
        response = self.client.post(
            "/tracks/5/moods/add",
            data=json.dumps({"joy": 1}),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

    def test_moods_clear(self):
        response = self.client.delete("/tracks/1/moods/clear")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)