from datetime import datetime

from lamptimer.month import Month
from lamptimer.day import Day


def test_month_initialization(london_location):
    date = datetime(2023, 10, 1)
    month = Month(date=date, location=london_location)

    assert month.date == date
    assert month.location == london_location
    assert len(month.days) == 31
    assert all(isinstance(day, Day) for day in month.days)
    assert month.days[0].date == datetime(2023, 10, 1)


def test_month_date_normalization(london_location):
    # Test with a date that has a time component
    date_with_time = datetime(2023, 10, 5, 15, 30, 45)
    month = Month(date=date_with_time, location=london_location)

    assert month.date == datetime(2023, 10, 1, 0, 0, 0)
    assert len(month.days) == 31
    assert month.days[4].date == datetime(2023, 10, 5)


def test_month_initialization_for_leap_year(london_location):
    # Test for February in a leap year
    date = datetime(2024, 2, 1)
    month = Month(date=date, location=london_location)

    assert len(month.days) == 29
    assert month.days[0].date == datetime(2024, 2, 1)
