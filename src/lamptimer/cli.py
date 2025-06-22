"""
Main CLI entrypoint and command definitions for Lamp Timer.
"""

from datetime import datetime

import typer
from astral import LocationInfo
from typing_extensions import Annotated
from rich.console import Console

from lamptimer.day import Day
from lamptimer.month import Month
from lamptimer.cli_output import (
    format_day_summary,
    format_month_csv,
    format_location_info,
    format_month_table,
    format_month_json,
    format_month_jsonl,
    format_month_summary,
)
from lamptimer.cli_output.output_format import OutputFormat


cli = typer.Typer()
current_date_with_time = datetime.now()
console = Console()


def create_context_obj(ctx: typer.Context, location: LocationInfo) -> None:
    """Create a context object with location and current date."""
    ctx.obj = {
        "location": location,
        "current_date": current_date_with_time,
    }


def get_time_from_options(month: str, year: int) -> datetime:
    """Returns a datetime object for the given month and year."""
    return datetime.strptime(f"{year} {month}", "%Y %B")


@cli.command()
def month_summary(
    ctx: typer.Context,
    month: Annotated[
        str, typer.Option(help="Month to summarize, defaults to current month.")
    ] = current_date_with_time.strftime("%B"),
    year: Annotated[
        int, typer.Option(help="Year to summarize, defaults to current year.")
    ] = current_date_with_time.year,
    shutoff_after: Annotated[
        int,
        typer.Option(
            help="Number of hours after dusk to shut off lights, defaults to 4."
        ),
    ] = 4,
):
    """Prints a summary of the current month's dusk times."""
    date_with_time = get_time_from_options(month, year)
    month_data = Month(date=date_with_time, location=ctx.obj["location"])

    print(format_month_summary(month_data, shutoff_after))


@cli.command()
def month(
    ctx: typer.Context,
    format: Annotated[
        OutputFormat, typer.Option(help="Output format of data.")
    ] = OutputFormat.table,
    month: Annotated[
        str, typer.Option(help="Month to summarize, defaults to current month.")
    ] = current_date_with_time.strftime("%B"),
    year: Annotated[
        int, typer.Option(help="Year to summarize, defaults to current year.")
    ] = current_date_with_time.year,
):
    """Prints the current month's dusk times."""
    date_with_time = get_time_from_options(month, year)
    month_data = Month(date=date_with_time, location=ctx.obj["location"])

    if format == OutputFormat.csv:
        print(format_month_csv(month_data))
    elif format == OutputFormat.json:
        print(format_month_json(month_data))
    elif format == OutputFormat.jsonl:
        print(format_month_jsonl(month_data))
    else:
        console.print(format_month_table(month_data))


@cli.command()
def today(ctx: typer.Context):
    """Prints today's dusk time."""
    day = Day(date=ctx.obj["current_date"], location=ctx.obj["location"])

    print(format_day_summary(day))


@cli.callback()
def main(
    ctx: typer.Context,
    city: str = typer.Option("Toronto", help="City name for location info."),
    region: str = typer.Option("Canada", help="Region name for location info."),
    timezone: str = typer.Option("America/Toronto", help="Timezone for location info."),
    latitude: float = typer.Option(43.6532, help="Latitude for location info."),
    longitude: float = typer.Option(-79.3832, help="Longitude for location info."),
    show_location: bool = typer.Option(False, help="Show location info at startup."),
):
    """Lamptimer CLI for managing dusk times."""
    location = LocationInfo(city, region, timezone, latitude, longitude)

    create_context_obj(ctx, location)

    if show_location:
        print(format_location_info(location))


if __name__ == "__main__":
    cli()
