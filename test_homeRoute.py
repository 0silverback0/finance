import unittest
from app import app

class TestHomeRoute(unittest.TestCase):
    def test_homeRoute(self):
        self.client = app.test_client()
        with self.client as c:
            res = c.get('/')
            self.assertEqual(res.status_code, 200)