import unittest
import lampTimer
import datetime

class TestDate(unittest.TestCase):

    def test_date_create(self):
        time = lampTimer.zeroify_date(datetime.datetime(2016,01,01))
        location = lampTimer.get_astral_city()
        newDay = lampTimer.Day(time, location)
        self.assertEqual(newDay.date, time)
        self.assertEqual(newDay.location, location)

class TestMonth(unittest.TestCase):

    def test_month_create(self):
        time = lampTimer.zeroify_date(datetime.datetime(2016,01,01))
        location = lampTimer.get_astral_city()
        newMonth = lampTimer.Month(time, location)
        self.assertEqual(newMonth.date, time)
        self.assertEqual(newMonth.location, location)
        self.assertEqual(len(newMonth.days), 31)

if __name__ == '__main__':
    unittest.main()
