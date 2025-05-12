from datetime import datetime
from src.lamptimer.day import Day

def test_normalize_date():
    # Test with a date that has a time component
    date_with_time = datetime(2023, 10, 5, 15, 30, 45)
    normalized_date = Day(date=date_with_time).date
    assert normalized_date == datetime(2023, 10, 5, 0, 0, 0)

    # Test with a date that is already at midnight
    date_at_midnight = datetime(2023, 10, 5)
    normalized_date = Day(date=date_at_midnight).date
    assert normalized_date == datetime(2023, 10, 5, 0, 0, 0)
