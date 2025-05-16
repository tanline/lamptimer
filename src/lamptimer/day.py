from dataclasses import dataclass, field
from datetime import datetime

from astral import LocationInfo
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

    @staticmethod
    def _normalize_date(date: datetime) -> datetime:
        """Set the time of the date to midnight."""
        return date.replace(hour=0, minute=0, second=0, microsecond=0)

    def _calculate_dusk_time(self) -> datetime:
        """Calculate the dusk time for the given date and location."""
        sun_info = sun(self.location.observer, date=self.date)
        return sun_info['dusk']