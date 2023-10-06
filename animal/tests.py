import datetime
import json

from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from animal.models import Animal, Schedule
from animal.time_scheduler import WorkingDayTimeException


# Create your tests here.
def update_test_data():
    with open("all_data.json", "r", encoding='utf-8') as all_data:
        data = json.load(all_data)
    for n in data:
        if n["model"] == "animal.schedule":
            start_time = n["fields"]["start_time"]
            end_time = n["fields"]["end_time"]
            n["fields"]["start_time"] = start_time.replace(start_time[:10],
                                                           datetime.datetime.utcnow().date().strftime(
                                                               '%Y-%m-%d'))
            n["fields"]["end_time"] = end_time.replace(end_time[:10],
                                                       datetime.datetime.utcnow().date().strftime(
                                                           '%Y-%m-%d'))

    with open("all_data.json", 'w', encoding='utf-8') as all_data:
        json.dump(data, all_data, indent=4)


class AnimalTestsFixtures(TestCase):
    update_test_data()
    fixtures = ["all_data.json"]
    client = Client()

    def test_1(self):
        test_animal = Animal.objects.get(id=1)
        response = self.client.get(reverse("animal_detail", args=[test_animal.id]))
        status_code = response.status_code
        self.assertEqual(200, status_code)
        self.assertTrue(test_animal.name in str(response.content))

    def test_book_1(self):
        self.client.login(username="user1", password="user1")
        test_animal = Animal.objects.get(id=1)
        test_start_time = "16:00"
        test_schedules_before = len(Schedule.objects.filter(animal=test_animal).all())
        response = self.client.post(reverse("animal_detail", args=[test_animal.id]),
                                    data={"time_duration": 1, "start_time": test_start_time, 'hidden_field': "book"})
        status_code = response.status_code
        self.assertEqual(200, status_code)
        test_schedules_after = len(Schedule.objects.filter(animal=test_animal).all())
        self.assertEqual(test_schedules_before + 1, test_schedules_after)

    def test_book_2(self):
        self.client.login(username="user1", password="user1")
        test_animal = Animal.objects.get(id=2)
        test_start_time = "11:00"
        test_schedules_before = len(Schedule.objects.filter(animal=test_animal).all())
        response = self.client.post(reverse("animal_detail", args=[test_animal.id]),
                                    data={"time_duration": 2, "start_time": test_start_time, 'hidden_field': "book"})
        status_code = response.status_code
        self.assertEqual(200, status_code)
        test_schedules_after = len(Schedule.objects.filter(animal=test_animal).all())
        self.assertEqual(test_schedules_before + 1, test_schedules_after)

    def test_book_2_do_not_write(self):
        self.client.login(username="user1", password="user1")
        test_animal = Animal.objects.get(id=1)
        test_start_time = "12:00"
        test_schedules_before = Schedule.objects.filter(animal=test_animal).all()
        response = self.client.post(reverse("animal_detail", args=[test_animal.id]),
                                    data={"time_duration": 2, "start_time": test_start_time})
        status_code = response.status_code
        self.assertEqual(200, status_code)
        test_schedules_after = Schedule.objects.filter(animal=test_animal).all()
        self.assertEqual(len(test_schedules_before), len(test_schedules_after))

    def test_check_time_1(self):
        self.client.login(username="user1", password="user1")
        test_animal = Animal.objects.get(id=1)
        test_schedules_before = len(Schedule.objects.filter(animal=test_animal).all())
        response = self.client.post(reverse("animal_detail", args=[test_animal.id]),
                                    data={"time_duration": 2})
        status_code = response.status_code
        self.assertEqual(200, status_code)
        self.assertTrue('value="16:00">16:00<' in str(response.content))
        test_schedules_after = len(Schedule.objects.filter(animal=test_animal).all())
        self.assertEqual(test_schedules_before, test_schedules_after)

    def test_check_time_2(self):
        self.client.login(username="user1", password="user1")
        test_animal = Animal.objects.get(id=2)
        test_schedules_before = len(Schedule.objects.filter(animal=test_animal).all())
        response = self.client.post(reverse("animal_detail", args=[test_animal.id]),
                                    data={"time_duration": 2})
        status_code = response.status_code
        expected_response = \
            ['value="08:00">08:00<', 'value="08:15">08:15<', 'value="08:30">08:30<', 'value="08:45">08:45<',
             'value="09:00">09:00<', 'value="09:15">09:15<', 'value="09:30">09:30<', 'value="09:45">09:45<',
             'value="10:00">10:00<', 'value="10:15">10:15<', 'value="10:30">10:30<', 'value="10:45">10:45<',
             'value="11:00">11:00<', 'value="15:00">15:00<', 'value="15:15">15:15<', 'value="15:30">15:30<',
             'value="15:45">15:45<', 'value="16:00">16:00<']
        self.assertEqual(200, status_code)
        self.assertTrue('value="16:00">16:00<' in str(response.content))
        test_schedules_after = len(Schedule.objects.filter(animal=test_animal).all())
        self.assertEqual(test_schedules_before, test_schedules_after)
        for res in expected_response:
            self.assertIn(res, str(response.content))

    def test_check_time_negative(self):
        self.client.login(username="user1", password="user1")
        test_animal = Animal.objects.get(id=1)
        with self.assertRaises(WorkingDayTimeException):
            self.client.post(reverse("animal_detail", args=[test_animal.id]),
                             data={"time_duration": 11})

    def test_check_no_free_time(self):
        self.client.login(username="user1", password="user1")
        test_animal = Animal.objects.get(id=1)
        test_schedules_before = len(Schedule.objects.filter(animal=test_animal).all())
        response = self.client.post(reverse("animal_detail", args=[test_animal.id]),
                                    data={"time_duration": 3})
        status_code = response.status_code
        self.assertEqual(200, status_code)
        self.assertTrue('value="NO FREE TIME">NO FREE TIME<' in str(response.content))
        test_schedules_after = len(Schedule.objects.filter(animal=test_animal).all())
        self.assertEqual(test_schedules_before, test_schedules_after)


class TestAnimalFilter(TestCase):
    fixtures = ["all_data.json"]
    client = Client()

    def test_filter_by_type(self):
        response = self.client.get(reverse("index"), data={"animal_type": "cat"})
        status_code = response.status_code
        self.assertEqual(200, status_code)
        self.assertIn("Vasya", str(response.content))
        self.assertNotIn("dog", str(response.content))

    def test_filter_by_breed(self):
        response = self.client.get(reverse("index"), data={"animal_breed": "brit"})
        status_code = response.status_code
        self.assertEqual(200, status_code)
        self.assertIn("Vasya", str(response.content))
        self.assertNotIn("dog", str(response.content))

    def test_no_filter(self):
        response = self.client.get(reverse("index"))
        status_code = response.status_code
        self.assertEqual(200, status_code)
        expected_response = ["bim", "bosya", "Vasya"]
        for res in expected_response:
            self.assertIn(res, str(response.content))
