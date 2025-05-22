from datetime import datetime

from lamptimer.month import Month
from lamptimer.day import Day

from astral import LocationInfo

def test_month_initialization():
    location = LocationInfo("London", "England", "Europe/London", 51.5, -0.116)
    date = datetime(2023, 10, 1)
    month = Month(date=date, location=location)

    assert month.date == date
    assert month.location == location
    assert len(month.days) == 31
    assert all(isinstance(day, Day) for day in month.days)
    assert month.days[0].date == datetime(2023, 10, 1)

def test_month_initialization_for_leap_year():
    # Test for February in a leap year
    location = LocationInfo("London", "England", "Europe/London", 51.5, -0.116)
    date = datetime(2024, 2, 1)
    month = Month(date=date, location=location)

    assert len(month.days) == 29
    assert month.days[0].date == datetime(2024, 2, 1)
