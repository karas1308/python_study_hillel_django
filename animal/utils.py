from animal.time_scheduler import calculate_booking_time


def calculate_free_time(booked_time_frames, min_time_duration, min_time_slot=15):
    return __calculate_free_time(booked_time_frames=booked_time_frames, min_time_duration=min_time_duration,
                                 min_time_slot=min_time_slot)


def __calculate_free_time(booked_time_frames, min_time_duration, min_time_slot=15):
    return calculate_booking_time(booked_time_frames=booked_time_frames, min_time_duration=min_time_duration,
                                  min_time_slot=min_time_slot)


class CalculateFreeTime:
    def __call__(self, *args, **kwargs):
        return self

    def calculate_free_time_1(self, booked_time_frames, min_time_duration, min_time_slot=15):
        return calculate_booking_time(booked_time_frames=booked_time_frames, min_time_duration=min_time_duration,
                                      min_time_slot=min_time_slot)

    @classmethod
    def calculate_free_time_2(cls, booked_time_frames, min_time_duration, min_time_slot=15):
        return calculate_booking_time(booked_time_frames=booked_time_frames, min_time_duration=min_time_duration,
                                      min_time_slot=min_time_slot)

    @staticmethod
    def calculate_free_time_3(booked_time_frames, min_time_duration, min_time_slot=15):
        return calculate_booking_time(booked_time_frames=booked_time_frames, min_time_duration=min_time_duration,
                                      min_time_slot=min_time_slot)


def calc_proxy(*args, **kwargs):
    c_f_t = CalculateFreeTime()
    return c_f_t.calculate_free_time_1(*args, **kwargs)


calc_free_time = CalculateFreeTime()
