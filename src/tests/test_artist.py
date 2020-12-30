from main import db, create_app
import unittest
import json

class TestArtist(unittest.TestCase):
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

    def test_artist_index(self):
        response = self.client.get("/artist/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_artist_create(self):
        response = self.client.post(
            "/artist/",
            data=json.dumps({"name": "testname"}),
            content_type="application/json"
        )
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)

    def test_artist_update(self):
        response = self.client.patch(
            "/artist/4",
            data=json.dumps({"name": "updatedtestname"}),
            content_type="application/json"
        )

        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(data['name'], "updatedtestname")