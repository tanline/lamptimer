import datetime

class Day(object):
    def __init__(self, date, location, shutoff_after=4):
        self.date = self._zeroify_date(date)
        self.location = location
        self._dusk = self._calculate_dusk_time()
        self.shutoff_after = shutoff_after

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

    def calculate_lamp_shutoff_time(self, hours=4):
        on_length = datetime.timedelta(seconds=(hours*3600))
        return self.rounded_dusk_time() + on_length

    def __str__(self):
        date_str = self.date.date()
        rounded_dusk_str = self.rounded_dusk_time().strftime('%X%z')
        shutoff_str = self.calculate_lamp_shutoff_time(self.shutoff_after).strftime('%X%z')
        return '{}, {}, {}'.format(date_str, rounded_dusk_str, shutoff_str)

    def __format__(self, format):
        formats = {
            'with-dusk': self._with_dusk_str,
        }
        func = formats.get(format, self.__str__)
        return func()

    def _with_dusk_str(self):
        date_str = self.date.date()
        dusk_str = self.dusk_time().strftime('%X%z')
        rounded_dusk_str = self.rounded_dusk_time().strftime('%X%z')
        shutoff_str = self.calculate_lamp_shutoff_time(self.shutoff_after).strftime('%X%z')
        return '{}, {}, {}, {}'.format(date_str, dusk_str, rounded_dusk_str, shutoff_str)

    def _calculate_dusk_time(self):
        sun = self.location.sun(date=self.date, local=True)
        return sun['dusk']

    @staticmethod
    def _zeroify_date(date):
        return date.replace(hour=0, minute=0, second=0, microsecond=0)
