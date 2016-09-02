import datetime
import lamptimer

class Day:
    def __init__(self, date, location):
        self.date = lamptimer.zeroify_date(date)
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
