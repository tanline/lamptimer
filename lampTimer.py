import datetime
from astral import Astral

def get_astral_city():
    city_name = 'Toronto'
    a = Astral()
    a.solar_depression = 'civil'
    city = a[city_name]
    return city

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

if __name__ == '__main__':
    city = get_astral_city()
    print('Information for %s/%s\n' % (city.name, city.region))
    sun = city.sun(date=datetime.datetime.now(), local=True)
    print('Dusk: %s' % str(sun['dusk']))
    print_time(sun)
