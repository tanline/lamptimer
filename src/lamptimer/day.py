from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Day:
    date: datetime
    shutoff_after: int = 4
    _dusk: datetime = field(init=False)

    def __post_init__(self):
        self.date = self._normalize_date(self.date)

    @staticmethod
    def _normalize_date(date: datetime) -> datetime:
        """Set the time of the date to midnight."""
        return date.replace(hour=0, minute=0, second=0, microsecond=0)
