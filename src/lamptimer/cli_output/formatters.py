import json

from astral import LocationInfo
from rich.table import Table

from lamptimer.day import Day
from lamptimer.month import Month


def format_location_info(location: LocationInfo) -> str:
    return (
        f"City: {location.name}\n"
        f"Region: {location.region}\n"
        f"Timezone: {location.timezone}\n"
        f"Coordinates (Lat/Long): ({location.latitude}, {location.longitude})"
    )


def format_day_summary(day: Day) -> str:
    return (
        f"Date: {day.date.strftime('%Y-%m-%d')}\n"
        f"Dusk Time: {day.dusk_time.strftime('%H:%M:%S')}\n"
        f"Rounded Dusk Time: {day.rounded_dusk_time.strftime('%H:%M')}"
    )


def format_day_csv(day: Day) -> str:
    return f"{day.date.strftime('%Y-%m-%d')},{day.dusk_time.strftime('%H:%M:%S')},{day.rounded_dusk_time.strftime('%H:%M')}"


def format_month_csv(month: Month) -> str:
    lines = ["Date,Dusk Time,Rounded Dusk Time"]
    for day in month.days:
        lines.append(format_day_csv(day))
    return "\n".join(lines)


def format_day_json_data(day: Day) -> dict:
    return {
        "date": day.date.strftime("%Y-%m-%d"),
        "dusk_time": day.dusk_time.strftime("%H:%M:%S"),
        "rounded_dusk_time": day.rounded_dusk_time.strftime("%H:%M"),
    }


def format_month_json(month: Month) -> str:
    data = []
    for day in month.days:
        data.append(format_day_json_data(day))

    return json.dumps(data, indent=4, default=str)


def format_month_jsonl(month: Month) -> str:
    lines = []
    for day in month.days:
        data = format_day_json_data(day)
        lines.append(json.dumps(data, default=str))
    return "\n".join(lines)


def format_month_table(month: Month) -> Table:
    table = Table(title=f"Dusk Times for {month.date.strftime('%B %Y')}")
    table.add_column("Date", justify="left")
    table.add_column("Dusk Time", justify="left")
    table.add_column("Rounded Dusk Time", justify="left")

    for day in month.days:
        table.add_row(
            day.date.strftime("%Y-%m-%d"),
            day.dusk_time.strftime("%H:%M:%S"),
            day.rounded_dusk_time.strftime("%H:%M"),
        )

    return table
