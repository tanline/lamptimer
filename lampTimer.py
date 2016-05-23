import datetime
import calendar
from astral import Astral

def get_astral_city():
    city_name = 'Toronto'
    a = Astral()
    a.solar_depression = 'civil'
    found_city = a[city_name]
    return found_city

def print_time(time):
    hour = time['dusk'].hour
    minute = time['dusk'].minute
    if minute >= 45:
        minute = 0
        hour += 1
    elif minute >=15:
        minute = 30
    else:
        minute = 0
    print('Dusk: %02d:%02d' % (hour, minute))

def pretty_time(time):
    hour = time['dusk'].hour
    minute = time['dusk'].minute
    if minute >= 45:
        minute = 0
        hour += 1
    elif minute >=15:
        minute = 30
    else:
        minute = 0
    return '{}:{}'.format(str(hour).zfill(2), str(minute).zfill(2))

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

def print_as_csv(dusk_times_for_month):
    print('Date, Actual Dusk Time, Rounded Dusk Time\n')
    for day in dusk_times_for_month:
        print '{}, {}, {}'.format(day[0], str(day[1]['dusk']), pretty_time(day[1]))


if __name__ == '__main__':
    city = get_astral_city()
    print('Information for %s/%s\n' % (city.name, city.region))
    x = calculate_dusk_for_days_in_month(datetime.datetime.now())
    print_as_csv(x)
    # sun = city.sun(date=datetime.datetime.now(), local=True)
    # print('Dusk: %s' % str(sun['dusk']))
    # print_time(sun)
