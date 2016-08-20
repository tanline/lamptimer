import datetime
import calendar
import day

class Month:
    def __init__(self, month, location):
        self.date = month
        self.location = location
        self.days = self._populate_days()

    def _populate_days(self):
        days = []
        days_in_month = calendar.monthrange(self.date.year, self.date.month)[1]

        for i in range(days_in_month):
            new_date = self.date.replace(day=(i+1))
            days.append(day.Day(new_date, self.location))

        return days

    def print_as_csv(self):
        print('\nDate, Actual Dusk Time, Rounded Dusk Time')
        for day in self.days:
            print day

    def get_days_of_rounded_dusk_change(self):
        days = []
        last_seen_time = None
        for day in self.days:
            dusk = day.rounded_dusk_time().time()
            if (dusk != last_seen_time):
                last_seen_time = dusk
                days.append(day)
        return days

