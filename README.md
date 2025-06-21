# Lamp Timer

Lamp Timer is a CLI tool that calculates the best times to turn your outdoor lamp on and off, based on astronomical dusk for your location. For any city and month, it:

- Calculates daily dusk times using precise astronomical data
- Rounds dusk times to the nearest half-hour
- Supports output as table, CSV, JSON, or JSONL
- Highlights days when dusk time changes
- Lets you fully configure the location (city, region, timezone, latitude, longitude)

Perfect for automating or optimizing outdoor lighting based on real sunset times.

## Installation (Local Development)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tanline/lamptimer.git
   cd lamptimer
   ```

2. **Install dependencies using uv:**
   ```bash
   uv pip install -e .[dev]
   ```
   Or, if you prefer pip:
   ```bash
   pip install -e .[dev]
   ```

3. **(Optional) Activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

## Running the CLI

You can run the CLI locally with:
```bash
uv run lamptimer-cli
```
Or, if installed with pip:
```bash
lamptimer-cli
```

## Running the Test Suite

To run all tests:
```bash
pytest
```

To run a specific test file:
```bash
pytest tests/test_day.py
```

## Code Style

This project uses [ruff](https://github.com/astral-sh/ruff) for linting. To check code style:
```bash
ruff check .
```
