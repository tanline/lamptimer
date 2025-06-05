import json
import pytest
from datetime import datetime

from astral import LocationInfo
from rich.table import Table

from lamptimer.cli_output import (
    format_location_info,
    format_day_summary,
    format_day_csv,
    format_month_csv,
    format_month_table,
    format_day_json_data,
    format_month_json,
    format_month_jsonl,
)
from lamptimer.day import Day
from lamptimer.month import Month


@pytest.fixture
def london_day():
    return Day(
        date=datetime(2023, 10, 5),
        location=LocationInfo("London", "England"),
    )


@pytest.fixture
def london_month():
    month = Month(
        date=datetime(2023, 10, 1),
        location=LocationInfo("London", "England"),
    )

    month.days = [
        Day(date=datetime(2023, 10, i), location=month.location) for i in range(1, 6)
    ]

    return month


@pytest.fixture
def london_expected_json_data():
    return [
        {"date": "2023-10-01", "dusk_time": "19:12:00", "rounded_dusk_time": "19:00"},
        {"date": "2023-10-02", "dusk_time": "19:09:44", "rounded_dusk_time": "19:00"},
        {"date": "2023-10-03", "dusk_time": "19:07:29", "rounded_dusk_time": "19:00"},
        {"date": "2023-10-04", "dusk_time": "19:05:15", "rounded_dusk_time": "19:00"},
        {"date": "2023-10-05", "dusk_time": "19:03:01", "rounded_dusk_time": "19:00"},
    ]


def test_format_location_info(london_location):
    expected_output = (
        "City: London\n"
        "Region: England\n"
        "Timezone: Europe/London\n"
        "Coordinates (Lat/Long): (51.5, -0.116)"
    )
    assert format_location_info(london_location) == expected_output


def test_format_day_summary(london_day):
    expected_output = "Date: 2023-10-05\nDusk Time: 19:03:01\nRounded Dusk Time: 19:00"
    assert format_day_summary(london_day) == expected_output


def test_format_day_csv(london_day):
    expected_output = "2023-10-05,19:03:01,19:00"
    assert format_day_csv(london_day) == expected_output


def test_format_month_csv(london_month):
    london_month.days = [
        Day(date=datetime(2023, 10, i), location=london_month.location)
        for i in range(1, 6)
    ]

    expected_output = (
        "Date,Dusk Time,Rounded Dusk Time\n"
        "2023-10-01,19:12:00,19:00\n"
        "2023-10-02,19:09:44,19:00\n"
        "2023-10-03,19:07:29,19:00\n"
        "2023-10-04,19:05:15,19:00\n"
        "2023-10-05,19:03:01,19:00"
    )

    assert format_month_csv(london_month) == expected_output
    assert format_month_csv(london_month).startswith("Date,Dusk Time,Rounded Dusk Time")


def test_format_month_table(london_month):
    london_month.days = [
        Day(date=datetime(2023, 10, i), location=london_month.location)
        for i in range(1, 6)
    ]

    table = format_month_table(london_month)

    assert isinstance(table, Table)
    assert table.title == "Dusk Times for October 2023"
    assert len(table.columns) == 3
    assert table.columns[0].header == "Date"
    assert table.columns[1].header == "Dusk Time"
    assert table.columns[2].header == "Rounded Dusk Time"
    assert len(table.rows) == 5


def test_format_day_json_data(london_day):
    expected_output = {
        "date": "2023-10-05",
        "dusk_time": "19:03:01",
        "rounded_dusk_time": "19:00",
    }
    assert format_day_json_data(london_day) == expected_output


def test_format_month_json(london_month, london_expected_json_data):
    london_month.days = [
        Day(date=datetime(2023, 10, i), location=london_month.location)
        for i in range(1, 6)
    ]

    expected_output = json.dumps(london_expected_json_data, indent=4, default=str)

    assert format_month_json(london_month) == expected_output


def test_format_month_jsonl(london_month, london_expected_json_data):
    london_month.days = [
        Day(date=datetime(2023, 10, i), location=london_month.location)
        for i in range(1, 6)
    ]

    expected_lines = [json.dumps(day, default=str) for day in london_expected_json_data]
    expected_output = "\n".join(expected_lines)

    assert format_month_jsonl(london_month) == expected_output
