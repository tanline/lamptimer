import datetime
from astral import Astral

def get_astral_city():
    city_name = 'Toronto'
    a = Astral()
    a.solar_depression = 'civil'
    city = a[city_name]
    return city


if __name__ == '__main__':
    city = get_astral_city()
    print('Information for %s/%s\n' % (city.name, city.region))
    sun = city.sun(date=datetime.datetime.now(), local=True)
    print('Dusk: %s' % str(sun['dusk']))
