import pytest
from datetime import datetime

from astral import LocationInfo

from lamptimer.month import Month
from lamptimer.month_summary import format_month_summary


@pytest.fixture
def london_month():
    month = Month(
        date=datetime(2023, 10, 1),
        location=LocationInfo("London", "England"),
    )

    return month


@pytest.fixture
def toronto():
    month = Month(
        date=datetime(2025, 6, 1),
        location=LocationInfo("Toronto", "Canada"),
    )

    return month


def test_format_month_summary(london_month):
    # assert that the first line is "Days when rounded dusk time changes:"
    expected_output = "\n".join(
        [
            "Report for month: 2023-10\n",
            "Days when dusk time changes:",
            "2023-10-14: 18:30",
            "2023-10-29: 17:00",
        ]
    )

    assert format_month_summary(london_month) == expected_output


def test_format_month_summary_when_no_dates_to_change(toronto):
    expected_output = "\n".join(
        [
            "Report for month: 2025-06\n",
            "All days have the same dusk time. Nothing to do!",
        ]
    )

    assert format_month_summary(toronto) == expected_output
