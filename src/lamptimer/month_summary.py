from datetime import timedelta

from lamptimer.month import Month


def format_month_summary(month: Month) -> str:
    """Return a summary of days when the rounded dusk time changes in the given month."""
    last_date_of_previous_month = month.date - timedelta(days=1)
    last_month = Month(last_date_of_previous_month, month.location)

    last_rounded = last_month.days[-1].rounded_dusk_time if last_month.days else None
    days_with_changes = []

    for day in month.days:
        if last_rounded is None or day.rounded_dusk_time.time() != last_rounded.time():
            # The times are different
            days_with_changes.append(day)
            last_rounded = day.rounded_dusk_time

    # Format the output
    lines = [f"Report for {month.date.strftime('%B %Y')}\n"]

    if not days_with_changes:
        lines.append("All days have the same dusk time. Nothing to do!")
    else:
        lines.append("Days when dusk time changes:")

        for day in days_with_changes:
            lines.append(
                f"{day.date.strftime('%Y-%m-%d')}: {day.rounded_dusk_time.strftime('%H:%M')}"
            )

    return "\n".join(lines)
