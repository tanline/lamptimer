import unittest
import datetime
from astral import Astral
from lamptimer import lamptimer, day

class TestLampTimerBase(unittest.TestCase):
    def setUp(self):
        self.location = self.get_astral_city()

    def create_day(self, time):
        return day.Day(time, self.location)

    @staticmethod
    def get_astral_city():
        city_name = 'Toronto'
        astral = Astral()
        astral.solar_depression = 'civil'
        found_city = astral[city_name]
        return found_city

class TestLampTimer(TestLampTimerBase):
    def test_lamp_timer_create(self):
        from_time = datetime.datetime(2016, 1, 1)
        to_time = datetime.datetime(2017, 1, 1)
        ltimer = lamptimer.LampTimer('Toronto', from_time, to_time)

        self.assertEqual(from_time, ltimer.from_date)
        self.assertEqual(to_time, ltimer.to_date)
        self.assertEqual(13, len(ltimer.months))

        with self.assertRaises(ValueError):
            lamptimer.LampTimer('Toronto', to_time, from_time)

    def test_dusks_differ_by_one_hour(self):
        day1 = self.create_day(datetime.datetime(2016, 1, 1))
        day2 = self.create_day(datetime.datetime(2016, 1, 5))
        day3 = self.create_day(datetime.datetime(2016, 1, 25))
        day4 = self.create_day(datetime.datetime(2016, 3, 15))

        self.assertEqual(False, lamptimer.dusks_differ_by_one_hour(day1, day2))
        self.assertEqual(False, lamptimer.dusks_differ_by_one_hour(day1, day3))
        self.assertEqual(True, lamptimer.dusks_differ_by_one_hour(day3, day4))

    def test_month_range(self):
        months = lamptimer.month_range(datetime.datetime(2016, 11, 1),
                                       datetime.datetime(2017, 2, 1))

        expected_months = [
            datetime.datetime(2016, 11, 1),
            datetime.datetime(2016, 12, 1),
            datetime.datetime(2017, 1, 1),
            datetime.datetime(2017, 2, 1)
        ]

        self.assertEqual(expected_months, months)

if __name__ == '__main__':
    unittest.main()
