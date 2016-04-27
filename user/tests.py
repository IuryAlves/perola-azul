# coding: utf-8
import json
import unittest
from app import app, db
from user.model import User


class UserTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        for user in User.get_all():
            User.delete_user(user.email)

    def setUp(self):
        self.client = app.test_client()
        self.user = User(name="iury", email="iury@gmail.com", password="blabla", gender='M')
        User.save(self.user)

    def test_get_one_user(self):
        response = self.client.get("/user/{email}".format(email=self.user.email))
        decoded_response = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(decoded_response, self.user.to_dict())
