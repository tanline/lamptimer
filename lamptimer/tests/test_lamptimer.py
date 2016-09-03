import unittest
import datetime
from astral import Astral
from lamptimer import *

class TestLampTimerBase(unittest.TestCase):
    def setUp(self):
        self.location = self.get_astral_city()

    def create_date(self, time):
        time = lamptimer.zeroify_date(time)
        return lamptimer.Day(time, self.location)

    @staticmethod
    def get_astral_city():
        city_name = 'Toronto'
        a = Astral()
        a.solar_depression = 'civil'
        found_city = a[city_name]
        return found_city

class TestLampTimer(TestLampTimerBase):
    def test_lamp_timer_create(self):
        from_time = lamptimer.zeroify_date(datetime.datetime(2016,01,01))
        to_time = lamptimer.zeroify_date(datetime.datetime(2017,01,01))
        lt = lamptimer.LampTimer('Toronto', from_time, to_time)

        self.assertEqual(from_time, lt.from_date)
        self.assertEqual(to_time, lt.to_date)
        self.assertEqual(13, len(lt.months))

        with self.assertRaises(ValueError):
            lamptimer.LampTimer('Toronto', to_time, from_time)

    def test_dusks_differ_by_one_hour(self):
        d1 = self.create_date(datetime.datetime(2016,01,01))
        d2 = self.create_date(datetime.datetime(2016,01,05))
        d3 = self.create_date(datetime.datetime(2016,01,25))
        d4 = self.create_date(datetime.datetime(2016,03,15))

        self.assertEqual(False, lamptimer.dusks_differ_by_one_hour(d1, d2))
        self.assertEqual(False, lamptimer.dusks_differ_by_one_hour(d1, d3))
        self.assertEqual(True, lamptimer.dusks_differ_by_one_hour(d3, d4))

    def test_month_range(self):
        months = lamptimer.month_range(datetime.datetime(2016,11,1), datetime.datetime(2017,2,1))

        expected_months = [
            datetime.datetime(2016,11,1),
            datetime.datetime(2016,12,1),
            datetime.datetime(2017,1,1),
            datetime.datetime(2017,2,1)
        ]

        self.assertEqual(expected_months, months)

    def test_zeroify_date(self):
        date = datetime.datetime(2017,2,1, 12, 30, 05)
        zero_date = lamptimer.zeroify_date(date)

        self.assertEqual(0, zero_date.hour)
        self.assertEqual(0, zero_date.minute)
        self.assertEqual(0, zero_date.second)
        self.assertEqual(0, zero_date.microsecond)


class TestDate(TestLampTimerBase):
    def test_date_create(self):
        time = lamptimer.zeroify_date(datetime.datetime(2016,01,01))
        newDay = lamptimer.Day(time, self.location)
        self.assertEqual(newDay.date, time)
        self.assertEqual(newDay.location, self.location)


class TestMonth(TestLampTimerBase):
    def test_month_create(self):
        time = lamptimer.zeroify_date(datetime.datetime(2016,01,01))
        newMonth = lamptimer.Month(time, self.location)
        self.assertEqual(newMonth.date, time)
        self.assertEqual(newMonth.location, self.location)
        self.assertEqual(len(newMonth.days), 31)

if __name__ == '__main__':
    unittest.main()
