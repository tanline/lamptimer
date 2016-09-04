import datetime
from astral import Astral
from .month import Month

class LampTimer(object):
    def __init__(self, city, from_date, to_date):
        self.from_date = from_date
        self.to_date = to_date
        self._validate_dates()
        self.location = self._get_astral_city(city)
        self.months = self._populate_months()

    @staticmethod
    def _get_astral_city(city_name):
        astral = Astral()
        astral.solar_depression = 'civil'
        found_city = astral[city_name]

        return found_city

    def _populate_months(self):
        months = []
        for date in month_range(self.from_date, self.to_date):
            months.append(Month(date, self.location))

        return months

    # A list of days on which the rounded time of dusk changes
    def days_of_dusk_change(self):
        days_of_change = []
        for month in self.months:
            for day in month.days_of_rounded_dusk_change():
                days_of_change.append(day)

        return days_of_change

    # A list of days that are considered to be ideal
    # days on which to change the timer
    def days_for_lamp_change(self):
        days = []
        for day in self.days_of_dusk_change():
            if len(days) == 0:
                days.append(day)
                continue
            if dusks_differ_by_one_hour(days[-1], day):
                days.append(day)

        return days

    def _validate_dates(self):
        if self.from_date > self.to_date:
            raise ValueError('Invalid Dates. From Date is after To Date.')

# Create a list consisting of datetimes
# representing the months between the given datetimes
def month_range(from_date, to_date):
    month_list = []
    year = from_date.year
    month = from_date.month
    last_added_date = None

    while last_added_date != to_date:
        if not last_added_date is None:
            month += 1
            if month > 12:
                month = 1
                year += 1
        last_added_date = datetime.datetime(year, month, 1)
        month_list.append(last_added_date)

    return month_list

def dusks_differ_by_one_hour(day1, day2):
    dusk1 = day1.rounded_dusk_time().time()
    dusk2 = day2.rounded_dusk_time().time()

    hour_diff = abs(dusk1.hour - dusk2.hour)

    if hour_diff == 1:
        # Our dusk times are always rounded to the nearest half-hour
        return abs(dusk1.minute - dusk2.minute) == 0
    else:
        return hour_diff > 0
