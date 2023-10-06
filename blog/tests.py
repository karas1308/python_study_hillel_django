from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from animal.models import Animal


# Create your tests here.

class TestFeedbacks(TestCase):
    fixtures = ["all_data.json"]
    client = Client()

    def test_get_blog(self):
        response = self.client.get("/blog/")
        status_code = response.status_code
        self.assertEqual(200, status_code)
        expected_result = ["title_1", "title_2"]
        for res in expected_result:
            self.assertIn(res, str(response.content))

    def test_get_feedbacks(self):
        response = self.client.get("/blog/feedbacks")
        status_code = response.status_code
        self.assertEqual(200, status_code)
        expected_result = ["qqqqqqqqq", "wwwwww"]
        for res in expected_result:
            self.assertIn(res, str(response.content))

    def test_add_feedback(self):
        animal = Animal.objects.get(id=1)
        self.client.login(username='user1', password='user1')
        feedback = {"title": "title_fixture_test", "text": "text_fixture_test", "media": "media_fixture_test",
                    "animal": animal.id}
        response = self.client.post(reverse("feedbacks"), {"title": feedback["title"],
                                                           "text": feedback["text"],
                                                           "media": feedback["media"],
                                                           "animal": feedback["animal"]})
        status_code = response.status_code
        self.assertEqual(200, status_code)

    def test_add_feedback_no_auth(self):
        animal = Animal.objects.get(id=1)
        feedback = {"title": "title_fixture_test", "text": "text_fixture_test", "media": "media_fixture_test",
                    "animal": animal.id}
        response = self.client.post(reverse("feedbacks"), {"title": feedback["title"],
                                                           "text": feedback["text"],
                                                           "media": feedback["media"],
                                                           "animal": feedback["animal"]})
        status_code = response.status_code
        self.assertEqual(302, status_code)
        self.assertEqual("/login", response.url)
