import datetime
from astral import Astral
from day import Day
from month import Month

def get_astral_city():
    city_name = 'Toronto'
    a = Astral()
    a.solar_depression = 'civil'
    found_city = a[city_name]
    return found_city

def calculate_dusk_time(date, location):
    sun = location.sun(date=date, local=True)
    return sun['dusk']

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
