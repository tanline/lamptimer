from datetime import datetime
from enum import Enum

import typer
from astral import LocationInfo
from typing_extensions import Annotated
from rich.console import Console

from lamptimer.day import Day
from lamptimer.month import Month
from lamptimer.formatters import (
    format_day_summary,
    format_month_csv,
    format_location_info,
    format_month_table,
    format_month_json,
    format_month_jsonl,
)


class OutputFormat(str, Enum):
    csv = "csv"
    json = "json"
    jsonl = "jsonl"
    table = "table"


cli = typer.Typer()
console = Console()

toronto_location = LocationInfo(
    "Toronto", "Canada", "America/Toronto", 43.641897, -79.386324
)


@cli.command()
def month(
    format: Annotated[
        OutputFormat, typer.Option(help="Output format of data.")
    ] = OutputFormat.table,
):
    """Prints the current month's dusk times."""
    location = toronto_location
    date_with_time = datetime.now()
    month = Month(date=date_with_time, location=location)

    print(format_location_info(location))

    if format == "csv":
        print(format_month_csv(month))
    elif format == "json":
        print(format_month_json(month))
    elif format == "jsonl":
        print(format_month_jsonl(month))
    else:
        console.print(format_month_table(month))


@cli.command()
def today():
    """Prints today's dusk time."""
    location = toronto_location
    date_with_time = datetime.now()
    day = Day(date=date_with_time, location=location)

    print(format_location_info(location))
    print(format_day_summary(day))


if __name__ == "__main__":
    cli()
