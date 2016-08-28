import unittest
import datetime
from astral import Astral
from lamptimer import *

class TestLampTimer(unittest.TestCase):
    def setUp(self):
        self.location = self.get_astral_city()

    @staticmethod
    def get_astral_city():
        city_name='Toronto'
        a = Astral()
        a.solar_depression = 'civil'
        found_city = a[city_name]
        return found_city


class TestDate(TestLampTimer):
    def test_date_create(self):
        time = lamptimer.zeroify_date(datetime.datetime(2016,01,01))
        newDay = lamptimer.Day(time, self.location)
        self.assertEqual(newDay.date, time)
        self.assertEqual(newDay.location, self.location)

class TestMonth(TestLampTimer):
    def test_month_create(self):
        time = lamptimer.zeroify_date(datetime.datetime(2016,01,01))
        newMonth = lamptimer.Month(time, self.location)
        self.assertEqual(newMonth.date, time)
        self.assertEqual(newMonth.location, self.location)
        self.assertEqual(len(newMonth.days), 31)

if __name__ == '__main__':
    unittest.main()
