from datetime import timedelta

from lamptimer.day import Day
from lamptimer.month import Month


def find_days_with_dusk_time_changes(month: Month) -> list[Day]:
    """Return a list of days in the month where the rounded dusk time changes."""
    last_date_of_previous_month = month.date - timedelta(days=1)
    last_day = Day(date=last_date_of_previous_month, location=month.location)

    last_rounded = last_day.rounded_dusk_time
    days_with_changes = []

    for day in month.days:
        if last_rounded is None or day.rounded_dusk_time.time() != last_rounded.time():
            # The times are different
            days_with_changes.append(day)
            last_rounded = day.rounded_dusk_time

    return days_with_changes


def format_month_summary(month: Month, shutoff_after: int) -> str:
    """Return a summary of days when the rounded dusk time changes in the given month."""
    days_with_changes = find_days_with_dusk_time_changes(month)

    # Format the output
    lines = [f"Report for {month.date.strftime('%B %Y')}\n"]

    if not days_with_changes:
        lines.append("All days have the same dusk time. Nothing to do!")
    else:
        lines.append("Days when dusk time changes:")

        for day in days_with_changes:
            date_str = day.date.strftime("%Y-%m-%d")
            rounded_dusk_time = day.rounded_dusk_time.strftime("%H:%M")
            shutoff_time = (
                day.rounded_dusk_time + timedelta(hours=shutoff_after)
            ).strftime("%H:%M")

            lines.append(
                f"{date_str} | Dusk: {rounded_dusk_time} | Shutoff: {shutoff_time}"
            )

    return "\n".join(lines)
