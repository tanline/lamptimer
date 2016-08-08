import unittest
import lampTimer
import datetime

class TestDate(unittest.TestCase):

    def test_create(self):
        time = datetime.datetime.now()
        location = lampTimer.get_astral_city()
        newDay = lampTimer.Day(time, location)
        self.assertEqual(newDay.date, time)

if __name__ == '__main__':
    unittest.main()
