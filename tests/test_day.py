from datetime import datetime

from lamptimer.day import Day


def test_normalize_date(london_location):
    # Test with a date that has a time component
    date_with_time = datetime(2023, 10, 5, 15, 30, 45)
    normalized_date = Day(date=date_with_time, location=london_location).date
    assert normalized_date == datetime(2023, 10, 5, 0, 0, 0)

    # Test with a date that is already at midnight
    date_at_midnight = datetime(2023, 10, 5)
    normalized_date = Day(date=date_at_midnight, location=london_location).date
    assert normalized_date == datetime(2023, 10, 5, 0, 0, 0)


def test_dusk_time(london_location):
    date = datetime(2023, 10, 5)
    expected_dusk_time = datetime(2023, 10, 5, 19, 3, 28)
    day = Day(date=date, location=london_location)

    assert day.dusk_time.date() == expected_dusk_time.date()
    assert day.dusk_time.time().hour == expected_dusk_time.hour
    assert day.dusk_time.time().minute == expected_dusk_time.minute
    assert day.dusk_time.time().second == expected_dusk_time.second


def test_rounded_dusk_time(london_location):
    date = datetime(2023, 10, 5)
    expected_rounded_dusk_time = datetime(
        2023, 10, 5, 19, 0, 0
    )  # Rounded to nearest half-hour
    day = Day(date=date, location=london_location)

    assert day.rounded_dusk_time.date() == expected_rounded_dusk_time.date()
    assert day.rounded_dusk_time.time().hour == expected_rounded_dusk_time.hour
    assert day.rounded_dusk_time.time().minute == expected_rounded_dusk_time.minute
    assert day.rounded_dusk_time.time().second == expected_rounded_dusk_time.second
