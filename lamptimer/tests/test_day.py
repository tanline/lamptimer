import unittest
import datetime
from lamptimer import day
from .test_lamptimer import TestLampTimerBase

class TestDay(TestLampTimerBase):
    def test_day_create(self):
        time = datetime.datetime(2016, 1, 1)
        new_day = self.create_day(time)

        self.assertEqual(new_day.date, time)
        self.assertEqual(new_day.location, self.location)

    def test_calculate_lamp_shutoff_time(self):
        new_day = self.create_day(datetime.datetime(2016, 1, 1))
        dusk = new_day.dusk_time()
        shutoff_time = new_day.calculate_lamp_shutoff_time()

        self.assertEqual(dusk.hour + 4, shutoff_time.hour)
        self.assertEqual(dusk.minute, shutoff_time.minute)

        rounded_dusk = new_day.rounded_dusk_time()
        shutoff_time = new_day.calculate_lamp_shutoff_time(True)
        self.assertEqual(rounded_dusk.hour + 4, shutoff_time.hour)
        self.assertEqual(rounded_dusk.minute, shutoff_time.minute)

        on_length = 8
        shutoff_time = new_day.calculate_lamp_shutoff_time(True, on_length)
        expected_hour = (rounded_dusk.hour + on_length) % 24
        self.assertEqual(expected_hour, shutoff_time.hour)
        self.assertEqual(rounded_dusk.minute, shutoff_time.minute)
