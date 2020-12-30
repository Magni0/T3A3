from main import db, create_app
import unittest
import json

class TestTracks(unittest.TestCase):
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

    def test_track_index(self):
        response = self.client.get("/tracks/")

        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        
        # removed because of frontend
        # self.assertIsInstance(data, list)

    def test_track_retrive(self):
        response = self.client.get("/tracks/1")

        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)

    def test_track_create(self):
        response = self.client.post(
            "/tracks/create",
            data=json.dumps({"trackname": "testname", "trackurl": "testurl"}),
            content_type="application/json"
        )

        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)

    def test_track_update(self):
        response = self.client.patch(
            "/tracks/3",
            data=json.dumps({"trackname": "newtrackname"}),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

    def test_track_delete(self):
        response = self.client.delete("/tracks/2")

        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)