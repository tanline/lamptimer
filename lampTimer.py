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

# From the given time, determine the month and year,
# and calculate the time of Dusk for each day
# Return as an array
def calculate_dusk_for_days_in_month(given_time):
    #get day and time
    first_day_of_month = datetime.datetime(given_time.year, given_time.month, 1)
    last_day_of_month = datetime.datetime(given_time.year, given_time.month, calendar.monthrange(given_time.year, 1)[1])
    print first_day_of_month
    print last_day_of_month

    calc_date = first_day_of_month

    print('Date, Actual Dusk Time, Rounded Dusk Time\n')
    while calc_date<=last_day_of_month:
        sun = city.sun(date=calc_date, local=True)
        print '{}, {}, {}'.format(calc_date.strftime('%Y-%m-%d'), str(sun['dusk']), pretty_time(sun))
        calc_date += datetime.timedelta(days=1)



    # sun = city.sun(date=new_time, local=True)
    # print('Dusk: %s' % str(sun['dusk']))
    # print('Date, Actual Dusk Time, Rounded Dusk Time\n')
    # last_day_of_month = calendar.monthrange(time.year, 1)[1]
    # print_time(sun)


if __name__ == '__main__':
    city = get_astral_city()
    print('Information for %s/%s\n' % (city.name, city.region))
    calculate_dusk_for_days_in_month(datetime.datetime.now())

    # sun = city.sun(date=datetime.datetime.now(), local=True)
    # print('Dusk: %s' % str(sun['dusk']))
    # print_time(sun)
