import datetime
import unittest

from animal.time_scheduler import WorkingDayTimeException, calculate_booking_time


class TestSchedulePositive(unittest.TestCase):

    def test_schedule_whole_day_busy(self):
        expected_result = []
        booked_time_frames = [(datetime.datetime(2023, 8, 1, 8, 0),
                               datetime.datetime(2023, 8, 1, 18, 0))]
        min_time_duration = 1
        min_time_slot = 15
        actual_result = calculate_booking_time(booked_time_frames, min_time_duration, min_time_slot)
        self.assertEqual(expected_result, actual_result)

    def test_schedule_whole_day_free(self):
        expected_result = ['08:00', '08:15', '08:30', '08:45', '09:00', '09:15', '09:30', '09:45', '10:00', '10:15',
                           '10:30', '10:45', '11:00', '11:15', '11:30', '11:45', '12:00', '12:15', '12:30', '12:45',
                           '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:30', '14:45', '15:00', '15:15',
                           '15:30', '15:45', '16:00', '16:15', '16:30', '16:45', '17:00']
        booked_time_frames = []
        min_time_duration = 1
        min_time_slot = 15
        actual_result = calculate_booking_time(booked_time_frames, min_time_duration, min_time_slot)
        self.assertEqual(expected_result, actual_result)

    def test_schedule_booked_beginning(self):
        expected_result = ['10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30',
                           '15:00', '15:30', '16:00']
        booked_time_frames = [(datetime.datetime(2024, 12, 31, 8, 0),
                               datetime.datetime(2024, 12, 31, 10, 0))]
        min_time_duration = 2
        min_time_slot = 30
        actual_result = calculate_booking_time(booked_time_frames, min_time_duration, min_time_slot)
        print(actual_result)
        self.assertEqual(expected_result, actual_result)

    def test_schedule_booked_mix(self):
        expected_result = ['11:30', '12:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00']
        booked_time_frames = [(datetime.datetime(2024, 12, 31, 8, 0),
                               datetime.datetime(2024, 12, 31, 10, 0)),
                              (datetime.datetime(2024, 12, 31, 13, 0),
                               datetime.datetime(2024, 12, 31, 14, 30)),
                              (datetime.datetime(2024, 12, 31, 10, 30),
                               datetime.datetime(2024, 12, 31, 11, 30))

                              ]
        min_time_duration = 1
        min_time_slot = 30
        actual_result = calculate_booking_time(booked_time_frames, min_time_duration, min_time_slot)
        print(actual_result)
        self.assertEqual(expected_result, actual_result)

    def test_schedule_booked_mix_2(self):
        expected_result = ['10:00', '10:30', '11:00', '11:30', '12:00', '14:30', '15:00', '15:30']
        booked_time_frames = [(datetime.datetime(2024, 12, 31, 8, 0),
                               datetime.datetime(2024, 12, 31, 10, 0)),
                              (datetime.datetime(2024, 12, 31, 13, 0),
                               datetime.datetime(2024, 12, 31, 14, 30)),
                              (datetime.datetime(2024, 12, 31, 16, 30),
                               datetime.datetime(2024, 12, 31, 18, 00))

                              ]
        min_time_duration = 1
        min_time_slot = 30
        actual_result = calculate_booking_time(booked_time_frames, min_time_duration, min_time_slot)
        print(actual_result)
        self.assertEqual(expected_result, actual_result)

    def test_schedule_booked_end(self):
        expected_result = ['08:00', '08:15', '08:30', '08:45', '09:00', '09:15', '09:30', '09:45', '10:00', '10:15',
                           '10:30', '10:45', '11:00', '11:15', '11:30', '11:45', '12:00', '12:15', '12:30', '12:45',
                           '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:30', '14:45', '15:00', '15:15',
                           '15:30', '15:45', '16:00']
        booked_time_frames = [(datetime.datetime(2024, 12, 31, 17, 0),
                               datetime.datetime(2024, 12, 31, 18, 0))]
        min_time_duration = 1
        min_time_slot = 15
        actual_result = calculate_booking_time(booked_time_frames, min_time_duration, min_time_slot)
        print(actual_result)
        self.assertEqual(expected_result, actual_result)

    def test_schedule_booked_beginning_end(self):
        expected_result = ['09:00', '09:15', '09:30', '09:45', '10:00', '10:15', '10:30', '10:45', '11:00', '11:15',
                           '11:30', '11:45', '12:00', '12:15', '12:30', '12:45', '13:00', '13:15', '13:30', '13:45',
                           '14:00', '14:15', '14:30', '14:45', '15:00', '15:15', '15:30', '15:45', '16:00']
        booked_time_frames = [(datetime.datetime(2024, 12, 31, 8, 0),
                               datetime.datetime(2024, 12, 31, 9, 0)),
                              (datetime.datetime(2024, 12, 31, 17, 0),
                               datetime.datetime(2024, 12, 31, 18, 0))]
        min_time_duration = 1
        min_time_slot = 15
        actual_result = calculate_booking_time(booked_time_frames, min_time_duration, min_time_slot)
        print(actual_result)
        self.assertEqual(expected_result, actual_result)


class TestScheduleNegative(unittest.TestCase):
    def test_schedule_booked_too_long_duration(self):
        booked_time_frames = [(datetime.datetime(2024, 12, 31, 8, 0),
                               datetime.datetime(2024, 12, 31, 9, 0))]
        min_time_duration = 11
        min_time_slot = 15
        with self.assertRaises(WorkingDayTimeException):
            calculate_booking_time(booked_time_frames, min_time_duration, min_time_slot)
