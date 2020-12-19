from main import db, create_app
from schemas.MoodSchema import MoodSchema
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
        pass

    def test_mood_increment(self):
        pass

    def test_moods_clear(self):
        pass