import unittest
import datetime
from lamptimer import month
from .test_lamptimer import TestLampTimerBase

class TestMonth(TestLampTimerBase):
    def test_month_create(self):
        time = datetime.datetime(2016, 1, 1)
        new_month = month.Month(time, self.location)
        self.assertEqual(new_month.date, time)
        self.assertEqual(new_month.location, self.location)
        self.assertEqual(len(new_month.days), 31)
