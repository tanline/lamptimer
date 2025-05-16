from datetime import datetime

from astral import LocationInfo
from src.lamptimer.day import Day

def test_normalize_date():
    location = LocationInfo("London", "England", "Europe/London", 51.5, -0.116)

    # Test with a date that has a time component
    date_with_time = datetime(2023, 10, 5, 15, 30, 45)
    normalized_date = Day(date=date_with_time, location=location).date
    assert normalized_date == datetime(2023, 10, 5, 0, 0, 0)

    # Test with a date that is already at midnight
    date_at_midnight = datetime(2023, 10, 5)
    normalized_date = Day(date=date_at_midnight, location=location).date
    assert normalized_date == datetime(2023, 10, 5, 0, 0, 0)

def test_dusk_time():
    location = LocationInfo("London", "England", "Europe/London", 51.5, -0.116)
    date = datetime(2023, 10, 5)
    expected_dusk_time = datetime(2023, 10, 5, 18, 3, 28)

    day = Day(date=date, location=location)


    assert day.dusk_time.date() == expected_dusk_time.date()
    assert day.dusk_time.time().hour == expected_dusk_time.hour
    assert day.dusk_time.time().minute == expected_dusk_time.minute
    assert day.dusk_time.time().second == expected_dusk_time.second
