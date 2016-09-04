import unittest
import datetime
from lamptimer import day
from .test_lamptimer import TestLampTimerBase

class TestDay(TestLampTimerBase):
    def test_day_create(self):
        time = datetime.datetime(2016, 1, 1)
        new_day = day.Day(time, self.location)
        self.assertEqual(new_day.date, time)
        self.assertEqual(new_day.location, self.location)
