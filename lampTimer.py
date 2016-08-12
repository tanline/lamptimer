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

    def get_days_of_rounded_dusk_change(self):
        days = []
        last_seen_time = None
        for day in self.days:
            dusk = day.rounded_dusk_time().time()
            if (dusk != last_seen_time):
                # print 'CHANGE'
                # print last_seen_time
                # print "to"
                # print dusk
                # print "-------------------"
                last_seen_time = dusk
                days.append(day)
        return days

def get_astral_city():
    city_name = 'Toronto'
    a = Astral()
    a.solar_depression = 'civil'
    found_city = a[city_name]
    return found_city

def zeroify_date(date):
    return date.replace(hour=0, minute=0, second=0, microsecond=0)

def print_months(first_month, last_month, year):
    if (first_month > last_month):
        return

    location = get_astral_city()
    for i in range(first_month,last_month+1):
        month = Month(datetime.datetime(year, i, 1), location)
        month.print_as_csv()
        print '\n'

def print_days_of_rounded_dusk_change(month):
    days = month.get_days_of_rounded_dusk_change()
    for day in days:
        print day

def print_days_and_times_for_lamp_change(first_month, last_month, year):
    if (first_month > last_month):
        return

    location = get_astral_city()
    days_of_change = []

    for i in range(first_month, last_month+1):
        month = Month(datetime.datetime(year, i, 1), location)
        days = month.get_days_of_rounded_dusk_change()
        for day in days:
            if (len(days_of_change) == 0):
                days_of_change.append(day)
                continue
            if dusks_differ_by_one_hour(day, days_of_change[-1]):
                days_of_change.append(day)

    for day in days_of_change:
        print day

def dusks_differ_by_one_hour(day1, day2):
    dusk1 = day1.rounded_dusk_time()
    dusk2 = day2.rounded_dusk_time()

    hour_diff = dusk1.hour - dusk2.hour
    min_diff = dusk1.minute - dusk2.minute

    return ((abs(hour_diff) == 1) and (min_diff == 0))

if __name__ == '__main__':
    print 'lampTimer!'
    # print_months(9,9)
    print_days_and_times_for_lamp_change(9,12,2016)

