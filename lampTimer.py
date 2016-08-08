import datetime
from datetime import timedelta
import calendar
from astral import Astral

def get_astral_city():
    city_name = 'Toronto'
    a = Astral()
    a.solar_depression = 'civil'
    found_city = a[city_name]
    return found_city

# From the given time, determine the month and year,
# and calculate the time of Dusk for each day
# Return a list of the same size of the number of days in the given month, where
# each index contains the calculated datetime for the given day (note: index 0 is the first of the month)
def calculate_dusk_for_days_in_month(given_time):
    # Get the last day of the given month
    last_day_of_month = datetime.datetime(given_time.year, given_time.month, calendar.monthrange(given_time.year, 1)[1])
    # Start calculation from the first day of the given month
    calc_date = datetime.datetime(given_time.year, given_time.month, 1)

    dusk_times = []
    print('Date, Actual Dusk Time, Rounded Dusk Time\n')
    while calc_date<=last_day_of_month:
        sun = city.sun(date=calc_date, local=True)
        tuple = [calc_date.strftime('%Y-%m-%d'), sun]
        dusk_times.append(tuple)
        # print '{}, {}, {}'.format(calc_date.strftime('%Y-%m-%d'), str(sun['dusk']), pretty_time(sun))
        calc_date += datetime.timedelta(days=1)

    return dusk_times

# Returns an integer representing the number of seconds
# between midnight and the given time.
def get_seconds_since_midnight(time):
    midnight = time.replace(hour=0, minute=0, second=0, microsecond=0)
    x = (time - midnight).seconds
    print x
    return x

def get_time_from_seconds_since_midnight(seconds_since_midnight):
    midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    delta = timedelta(seconds=seconds_since_midnight)
    print midnight + delta

def print_as_csv(dusk_times_for_month):
    print('Date, Actual Dusk Time, Rounded Dusk Time\n')
    for day in dusk_times_for_month:
        print '{}, {}, {}'.format(day[0], str(day[1]['dusk']), str(round_time(day[1])))

class Day:
    def __init__(self, date, location):
        self.date = date
        self._dusk = None
        self.location = location

    def dusk_time(self):
        if self._dusk == None:
            sun = self.location.sun(date=calc_date, local=True)
            self.dusk = sun['dusk']
        return self._dusk

    # Returns a datetime value, rounded to the nearest half-hour.
    def rounded_dusk_time(time):
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


# if __name__ == '__main__':
    # get_time_from_seconds_since_midnight(get_seconds_since_midnight(datetime.datetime.now()))
    # print('Information for %s/%s\n' % (city.name, city.region))
    # x = calculate_dusk_for_days_in_month(datetime.datetime.now())
    # print_as_csv(x)
    # sun = city.sun(date=datetime.datetime.now(), local=True)
    # print('Dusk: %s' % str(sun['dusk']))
