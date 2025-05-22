import pytest

from astral import LocationInfo

@pytest.fixture
def london_location():
    return LocationInfo("London", "England", "Europe/London", 51.5, -0.116)