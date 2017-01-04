from .day import Day
from calendar import monthrange

class Month(object):
    def __init__(self, month, location, shutoff_after=4):
        self.date = month
        self.location = location
        self.days = self._populate_days(shutoff_after)

    def _populate_days(self, shutoff_after):
        days = []
        days_in_month = monthrange(self.date.year, self.date.month)[1]

        for i in range(days_in_month):
            new_date = self.date.replace(day=(i+1))
            days.append(Day(new_date, self.location, shutoff_after))

        return days

    def print_as_csv(self):
        print '\nDate, Actual Dusk Time, Rounded Dusk Time'
        for day in self.days:
            print day

    def days_of_rounded_dusk_change(self):
        days = []
        last_seen_time = None
        for day in self.days:
            dusk = day.rounded_dusk_time().time()
            if dusk != last_seen_time:
                last_seen_time = dusk
                days.append(day)
        return days
