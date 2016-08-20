import unittest
import datetime
from lamptimer import *

class TestDate(unittest.TestCase):

    def test_date_create(self):
        time = lamptimer.zeroify_date(datetime.datetime(2016,01,01))
        location = lamptimer.get_astral_city()
        newDay = lamptimer.Day(time, location)
        self.assertEqual(newDay.date, time)
        self.assertEqual(newDay.location, location)

class TestMonth(unittest.TestCase):

    def test_month_create(self):
        time = lamptimer.zeroify_date(datetime.datetime(2016,01,01))
        location = lamptimer.get_astral_city()
        newMonth = lamptimer.Month(time, location)
        self.assertEqual(newMonth.date, time)
        self.assertEqual(newMonth.location, location)
        self.assertEqual(len(newMonth.days), 31)

if __name__ == '__main__':
    unittest.main()
