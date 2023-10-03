import datetime
import unittest
from unittest.mock import Mock, patch

from animal.time_scheduler import calculate_booking_time
from animal.utils import CalculateFreeTime, calc_free_time, calc_proxy, calculate_free_time


def custom_mock(*args, **kwargs):
    return [1]


class ScheduleMock:
    def __call__(self, *args, **kwargs):
        return [1]

    def calculate_free_time_1(self, *args, **kwargs):
        return [1]

    @classmethod
    def calculate_free_time_2(cls, *args, **kwargs):
        return [1]

    @staticmethod
    def calculate_free_time_3(*args, **kwargs):
        return [1]


class TestScheduleMock(unittest.TestCase):
    @patch('tests_mock.calculate_booking_time', Mock(return_value=[1]))
    def test_schedule_mock(self):
        expected_result = []
        booked_time_frames = [(datetime.datetime(2023, 8, 1, 8, 0),
                               datetime.datetime(2023, 8, 1, 18, 0))]
        min_time_duration = 1
        min_time_slot = 300
        actual_result = calculate_booking_time(booked_time_frames, min_time_duration, min_time_slot)
        print(f"expected_result:{expected_result} vs actual_result:{actual_result}")
        self.assertEqual(expected_result, actual_result)

    @patch('animal.utils.calculate_booking_time', Mock(return_value=[1]))
    def test_schedule_mock_1(self):
        expected_result = []
        booked_time_frames = [(datetime.datetime(2023, 8, 1, 8, 0),
                               datetime.datetime(2023, 8, 1, 18, 0))]
        min_time_duration = 1
        min_time_slot = 300
        actual_result = calculate_free_time(booked_time_frames, min_time_duration, min_time_slot)
        print(f"expected_result:{expected_result} vs actual_result:{actual_result}")
        self.assertEqual(expected_result, actual_result)

    @patch('animal.utils.calculate_booking_time', custom_mock)
    def test_schedule_mock_2(self):
        expected_result = []
        booked_time_frames = [(datetime.datetime(2023, 8, 1, 8, 0),
                               datetime.datetime(2023, 8, 1, 18, 0))]
        min_time_duration = 1
        min_time_slot = 300
        actual_result = calculate_free_time(booked_time_frames, min_time_duration, min_time_slot)
        print(f"expected_result:{expected_result} vs actual_result:{actual_result}")
        self.assertEqual(expected_result, actual_result)

    @patch('tests_mock.CalculateFreeTime', ScheduleMock)
    def test_schedule_mock_3(self):
        expected_result = []
        booked_time_frames = [(datetime.datetime(2023, 8, 1, 8, 0),
                               datetime.datetime(2023, 8, 1, 18, 0))]
        min_time_duration = 1
        min_time_slot = 300
        calculate_time = CalculateFreeTime()
        actual_result = calculate_time.calculate_free_time_1(booked_time_frames, min_time_duration, min_time_slot)
        print(f"expected_result:{expected_result} vs actual_result:{actual_result}")
        self.assertEqual(expected_result, actual_result)

    @patch('tests_mock.CalculateFreeTime', ScheduleMock)
    def test_schedule_mock_4(self):
        expected_result = []
        booked_time_frames = [(datetime.datetime(2023, 8, 1, 8, 0),
                               datetime.datetime(2023, 8, 1, 18, 0))]
        min_time_duration = 1
        min_time_slot = 300
        actual_result = CalculateFreeTime.calculate_free_time_2(booked_time_frames, min_time_duration, min_time_slot)
        print(f"expected_result:{expected_result} vs actual_result:{actual_result}")
        self.assertEqual(expected_result, actual_result)

    @patch('tests_mock.CalculateFreeTime', ScheduleMock)
    def test_schedule_mock_5(self):
        expected_result = []
        booked_time_frames = [(datetime.datetime(2023, 8, 1, 8, 0),
                               datetime.datetime(2023, 8, 1, 18, 0))]
        min_time_duration = 1
        min_time_slot = 300
        actual_result = CalculateFreeTime.calculate_free_time_3(booked_time_frames, min_time_duration, min_time_slot)
        print(f"expected_result:{expected_result} vs actual_result:{actual_result}")
        self.assertEqual(expected_result, actual_result)

    @patch('animal.utils.CalculateFreeTime', ScheduleMock)
    def test_schedule_mock_6(self):
        expected_result = [1]
        booked_time_frames = []
        min_time_duration =  ""
        min_time_slot = ""
        actual_result = calc_proxy(booked_time_frames, min_time_duration, min_time_slot)
        print(f"expected_result:{expected_result} vs actual_result:{actual_result}")
        self.assertEqual(expected_result, actual_result)

    @patch('animal.utils.calc_free_time', ScheduleMock())  # так робити не треба, бо це мок на мок
    def test_schedule_mock_7(self):
        expected_result = []
        booked_time_frames = [(datetime.datetime(2023, 8, 1, 8, 0),
                               datetime.datetime(2023, 8, 1, 18, 0))]
        min_time_duration = 1
        min_time_slot = 300
        actual_result = calc_free_time(booked_time_frames, min_time_duration, min_time_slot)
        print(f"expected_result:{expected_result} vs actual_result:{actual_result}")
        self.assertEqual(expected_result, actual_result)
