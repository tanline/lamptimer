import pytest
from datetime import datetime

from astral import LocationInfo

from lamptimer.month import Month
from lamptimer.cli_output import (
    format_month_summary,
    find_days_with_dusk_time_changes,
)


@pytest.fixture
def london_month():
    month = Month(
        date=datetime(2023, 10, 1),
        location=LocationInfo("London", "England"),
    )

    return month


@pytest.fixture
def toronto_month():
    month = Month(
        date=datetime(2025, 6, 1),
        location=LocationInfo("Toronto", "Canada"),
    )

    return month


def test_format_month_summary(london_month):
    # assert that the first line is "Days when rounded dusk time changes:"
    expected_output = "\n".join(
        [
            "Report for October 2023\n",
            "Days when dusk time changes:",
            "2023-10-14 | Dusk: 18:30 | Shutoff: 22:30",
            "2023-10-29 | Dusk: 17:00 | Shutoff: 21:00",
        ]
    )

    assert format_month_summary(london_month, 4) == expected_output


def test_format_month_summary_when_no_dates_to_change(toronto_month):
    expected_output = "\n".join(
        [
            "Report for June 2025\n",
            "All days have the same dusk time. Nothing to do!",
        ]
    )

    assert format_month_summary(toronto_month, 2) == expected_output


def test_find_days_with_dusk_time_changes(london_month):
    days_with_changes = find_days_with_dusk_time_changes(london_month)

    assert len(days_with_changes) == 2
    assert days_with_changes[0].date == datetime(2023, 10, 14)
    assert days_with_changes[1].date == datetime(2023, 10, 29)


def test_find_days_with_dusk_time_changes_no_changes(toronto_month):
    days_with_changes = find_days_with_dusk_time_changes(toronto_month)

    assert len(days_with_changes) == 0
