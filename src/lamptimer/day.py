from dataclasses import dataclass, field
from datetime import datetime

from astral import LocationInfo
from astral.location import Location
from astral.sun import sun


@dataclass
class Day:
    date: datetime
    shutoff_after: int = 4
    _dusk: datetime = field(init=False)
    location: LocationInfo = field(default_factory=LocationInfo)

    def __post_init__(self):
        self.date = self._normalize_date(self.date)
        self._dusk = self._calculate_dusk_time()

    @property
    def dusk_time(self) -> datetime:
        """Return the calculated dusk time."""
        return self._dusk

    @property
    def rounded_dusk_time(self) -> datetime:
        """Return the rounded dusk time, adjusted to the nearest half-hour."""
        dusk_hour = self.dusk_time.hour
        dusk_minute = self.dusk_time.minute

        if dusk_minute >= 45:
            dusk_minute = 0
            dusk_hour += 1
        elif dusk_minute >= 15:
            dusk_minute = 30
        else:
            dusk_minute = 0

        # Rounded to nearest half-hour include the timezone
        return datetime(
            self.dusk_time.year,
            self.dusk_time.month,
            self.dusk_time.day,
            dusk_hour,
            dusk_minute,
            0,
            0,
            tzinfo=self.dusk_time.tzinfo,
        )

    @staticmethod
    def _normalize_date(date: datetime) -> datetime:
        """Set the time of the date to midnight."""
        return date.replace(hour=0, minute=0, second=0, microsecond=0)

    def _calculate_dusk_time(self) -> datetime:
        """Calculate the dusk time for the given date and location."""
        timezone = Location(self.location).timezone
        sun_info = sun(self.location.observer, date=self.date, tzinfo=timezone)
        return sun_info["dusk"]
