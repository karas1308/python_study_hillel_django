import datetime

import pytest

from animal.time_scheduler import WorkingDayTimeException, calculate_booking_time

test_data = [([],
              [(datetime.datetime(2023, 8, 1, 8, 0),
                datetime.datetime(2023, 8, 1, 18, 0))],
              1,
              15),
             (['08:00', '08:15', '08:30', '08:45', '09:00', '09:15', '09:30', '09:45', '10:00', '10:15',
               '10:30', '10:45', '11:00', '11:15', '11:30', '11:45', '12:00', '12:15', '12:30', '12:45',
               '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:30', '14:45', '15:00', '15:15',
               '15:30', '15:45', '16:00', '16:15', '16:30', '16:45', '17:00'],
              [],
              1,
              15),
             (['10:00', '10:30', '11:00', '11:30', '12:00', '14:30', '15:00', '15:30'],
              [(datetime.datetime(2024, 12, 31, 8, 0),
                datetime.datetime(2024, 12, 31, 10, 0)),
               (datetime.datetime(2024, 12, 31, 13, 0),
                datetime.datetime(2024, 12, 31, 14, 30)),
               (datetime.datetime(2024, 12, 31, 16, 30),
                datetime.datetime(2024, 12, 31, 18, 00))],
              1,
              30
              ),
             (['08:00', '08:15', '08:30', '08:45', '09:00', '09:15', '09:30', '09:45', '10:00', '10:15',
               '10:30', '10:45', '11:00', '11:15', '11:30', '11:45', '12:00', '12:15', '12:30', '12:45',
               '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:30', '14:45', '15:00', '15:15',
               '15:30', '15:45', '16:00'],
              [(datetime.datetime(2024, 12, 31, 17, 0),
                datetime.datetime(2024, 12, 31, 18, 0))],
              1,
              15
              ),
             (['09:00', '09:15', '09:30', '09:45', '10:00', '10:15', '10:30', '10:45', '11:00', '11:15',
               '11:30', '11:45', '12:00', '12:15', '12:30', '12:45', '13:00', '13:15', '13:30', '13:45',
               '14:00', '14:15', '14:30', '14:45', '15:00', '15:15', '15:30', '15:45', '16:00'],
              [(datetime.datetime(2024, 12, 31, 8, 0),
                datetime.datetime(2024, 12, 31, 9, 0)),
               (datetime.datetime(2024, 12, 31, 17, 0),
                datetime.datetime(2024, 12, 31, 18, 0))],
              1,
              15),
             (['09:00', '09:30', '10:00', '10:30', '11:00'],
              [(datetime.datetime(2024, 12, 31, 8, 0),
                datetime.datetime(2024, 12, 31, 9, 0)),
               (datetime.datetime(2024, 12, 31, 14, 0),
                datetime.datetime(2024, 12, 31, 18, 0))],
              3,
              30)
             ]


@pytest.mark.parametrize("expected_result, booked_time_frames, min_time_duration, min_time_slot",
                         test_data)
def test_schedule(expected_result, booked_time_frames, min_time_duration, min_time_slot):
    actual_result = calculate_booking_time(booked_time_frames, min_time_duration, min_time_slot)
    assert expected_result == actual_result


def test_schedule_booked_too_long_duration():
    booked_time_frames = [(datetime.datetime(2024, 12, 31, 8, 0),
                           datetime.datetime(2024, 12, 31, 9, 0))]
    min_time_duration = 11
    min_time_slot = 15
    with pytest.raises(WorkingDayTimeException) as ex:
        calculate_booking_time(booked_time_frames, min_time_duration, min_time_slot)
    assert str(ex.value) == f"min_time_duration longer than working day"
