import datetime
from datetime import timedelta
import calendar
from astral import Astral

class Day:
    def __init__(self, date, location):
        self.date = zeroify_date(date)
        self.location = location
        self._dusk = self._calculate_dusk_time()

    def __str__(self):
        return '{}, {}, {}'.format(self.date, str(self.dusk_time()), str(self.rounded_dusk_time()))

    def dusk_time(self):
        return self._dusk

    # Returns a datetime value, rounded to the nearest half-hour.
    def rounded_dusk_time(self):
        dusk_hour = self._dusk.hour
        dusk_minute = self._dusk.minute
        if dusk_minute >= 45:
            dusk_minute = 0
            dusk_hour += 1
        elif dusk_minute >=15:
            dusk_minute = 30
        else:
            dusk_minute = 0
        return self.dusk_time().replace(hour=dusk_hour, minute=dusk_minute, second=0)

    def _calculate_dusk_time(self):
        sun = self.location.sun(date=self.date, local=True)
        return sun['dusk']

class Month:
    def __init__(self, month, location):
        self.date = month
        self.location = location
        self.days = self._populate_days()

    def _populate_days(self):
        days = []
        days_in_month = calendar.monthrange(self.date.year, self.date.month)[1]

        for i in range(days_in_month):
            new_date = self.date.replace(day=(i+1))
            days.append(Day(new_date, self.location))

        return days

    def print_as_csv(self):
        print('\nDate, Actual Dusk Time, Rounded Dusk Time')
        for day in self.days:
            print day

def get_astral_city():
    city_name = 'Toronto'
    a = Astral()
    a.solar_depression = 'civil'
    found_city = a[city_name]
    return found_city

def zeroify_date(date):
    return date.replace(hour=0, minute=0, second=0, microsecond=0)

if __name__ == '__main__':
    print 'lampTimer!'
