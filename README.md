# Lamp Timer

Lamp Timer is a CLI tool that calculates the best times to turn your outdoor lamp on and off, based on astronomical dusk for your location. For any city and month, it:

- Calculates daily dusk times using [astral](https://github.com/sffjunkie/astral)
- Rounds dusk to the nearest half-hour
- Outputs as table, CSV, JSON, or JSONL
- Marks days with dusk time changes and lamp shutoff times
- Fully configurable location (city, region, timezone, lat/lon)

Perfect for automating or optimizing outdoor lighting based on real sunset times.

## Installation (Local Development)

### Prerequistes
- Python 3.11
- [uv package manager](https://github.com/astral-sh/uv)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tanline/lamptimer.git
   cd lamptimer
   ```

2. **Install dependencies using uv:**
   ```bash
   uv sync
   ```

## Running the CLI

You can run the CLI locally with:
```bash
uv run lamptimer-cli
```

## CLI Help

To see all available commands and options, run:
```bash
uv run lamptimer-cli --help
```

## Running the Test Suite

To run all tests:
```bash
uv run pytest
```

To run a specific test file:
```bash
uv run pytest tests/test_day.py
```

## Code Style

This project uses [ruff](https://github.com/astral-sh/ruff) for linting. To check code style:
```bash
uv run ruff check
```
