from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client

from animal.models import Animal, Sex


# Додати тести для:
#
# реєстрації, логіну користувача
# запису на візит до тварини
# додавання відгуків
class TestUser(TestCase):

    def test_register_user(self):
        username = "register_jhon"
        client = Client()
        response = client.post("/register/", {"username": username, "password": "password"})
        status_code = response.status_code
        self.assertEqual(200, status_code)
        response_json = response.json()
        self.assertEqual(username, response_json["username"])
        self.assertFalse(response_json["is_superuser"])

    def test_login_user(self):
        client = Client()
        response = client.post("/login/", {"username": "jhon", "password": "password"})
        status_code = response.status_code
        self.assertEqual(404, status_code)
        user = User.objects.create(username="test")
        user.set_password("test")
        user.save()
        result = User.objects.get(username="test")
        self.assertEqual("test", result.username)
        logged_in = client.login(username='test', password='test')
        self.assertTrue(logged_in)

    def test_add_feedback(self):
        client = Client()
        male = Sex.objects.create(name="male")
        animal = Animal.objects.create(name="name_1",
                                       type="dog",
                                       sex=male,
                                       age=1,
                                       breed="home",
                                       availability=True,
                                       description="good boy",
                                       healthy=True)
        user = User.objects.create(username="add_feedback")
        user.set_password("test")
        user.save()
        client.login(username='add_feedback', password='test')
        feedback = {"title": "title", "text": "text", "media": "media", "animal": animal.id}
        response = client.post("/blog/feedbacks", {"title": feedback["title"],
                                                   "text": feedback["text"],
                                                   "media": feedback["media"],
                                                   "animal": feedback["animal"]})
        status_code = response.status_code
        self.assertEqual(200, status_code)
        response = client.post("/feedbacks/", {"title": feedback["title"],
                                               "text": feedback["text"],
                                               "media": feedback["media"],
                                               "animal": 1111111})
        status_code = response.status_code
        self.assertEqual(404, status_code)
