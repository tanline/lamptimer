import unittest
import datetime
from .test_lamptimer import TestLampTimerBase
from ..day import Day

class TestDay(TestLampTimerBase):
    def test_day_create(self):
        time = datetime.datetime(2016, 01, 01)
        day = Day(time, self.location)
        self.assertEqual(day.date, time)
        self.assertEqual(day.location, self.location)
