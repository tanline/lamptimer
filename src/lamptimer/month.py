from calendar import monthrange
from dataclasses import dataclass, field
from datetime import datetime

from astral import LocationInfo

from .day import Day


@dataclass
class Month:
    date: datetime
    location: LocationInfo
    days: list[Day] = field(init=False)

    def __post_init__(self):
        self.days = self._populate_days()

    def _populate_days(self) -> list[Day]:
        """Populate the month with Day objects."""
        days = []
        days_in_month = monthrange(self.date.year, self.date.month)[1]

        for i in range(days_in_month):
            new_date = self.date.replace(day=(i + 1))
            day = Day(date=new_date, location=self.location)
            days.append(day)

        return days
