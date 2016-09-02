import datetime
from astral import Astral
from day import Day
from month import Month

class LampTimer:
    def __init__(self, city, from_date, to_date):
        self.from_date = from_date
        self.to_date = to_date
        self.location = self._get_astral_city(city)

    def _get_astral_city(self, city_name='Toronto'):
        a = Astral()
        a.solar_depression = 'civil'
        found_city = a[city_name]
        return found_city

def calculate_dusk_time(date, location):
    sun = location.sun(date=date, local=True)
    return sun['dusk']

def zeroify_date(date):
    return date.replace(hour=0, minute=0, second=0, microsecond=0)

def print_days_of_rounded_dusk_change(month):
    days = month.get_days_of_rounded_dusk_change()
    for day in days:
        print day

def print_days_and_times_for_lamp_change(from_date, to_date):
    if (from_date > to_date):
        print 'Invalid Dates!'
        return

    days_of_change = []

    lt = LampTimer('Toronto', from_date, to_date)

    range_of_months = month_range(from_date, to_date)

    print 'Date, Dusk Time, Rounded Dusk Time'

    for month_date in range_of_months:
        month = Month(month_date, lt.location)
        days = month.get_days_of_rounded_dusk_change()
        for day in days:
            if (len(days_of_change) == 0):
                days_of_change.append(day)
                continue
            if dusks_differ_by_one_hour(day, days_of_change[-1]):
                days_of_change.append(day)

    for day in days_of_change:
        print day

def month_range(from_date, to_date):
    l = []

    year = from_date.year
    month = from_date.month

    last_added_date = None

    while (last_added_date != to_date):
        if not last_added_date is None:
            month += 1
            if month > 12:
                month = 1
                year += 1
        last_added_date = datetime.datetime(year, month, 1)
        l.append(last_added_date)

    return l


def dusks_differ_by_one_hour(day1, day2):
    dusk1 = day1.rounded_dusk_time()
    dusk2 = day2.rounded_dusk_time()

    hour_diff = dusk1.hour - dusk2.hour
    min_diff = dusk1.minute - dusk2.minute

    return ((abs(hour_diff) == 1) and (min_diff == 0))
