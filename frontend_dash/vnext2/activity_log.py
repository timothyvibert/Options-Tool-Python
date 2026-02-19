"""Activity log — local CSV storage for illustration tracking."""
from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path

# Log file location — in project root, gitignored
LOG_DIR = Path(__file__).resolve().parent.parent.parent  # project root
LOG_FILE = LOG_DIR / "activity_log.csv"

FIELDNAMES = [
    "timestamp",
    "fa_name",
    "fa_id",
    "acct_number",
    "ticker",
    "strategy",
    "expiry",
    "contracts",
    "net_premium",
    "max_profit",
    "max_loss",
]


def _ensure_file():
    """Create CSV with headers if it doesn't exist."""
    if not LOG_FILE.exists():
        with open(LOG_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def append_entry(entry: dict) -> None:
    """Append a single log entry. Entry keys should match FIELDNAMES."""
    _ensure_file()
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        row = {k: entry.get(k, "") for k in FIELDNAMES}
        if not row["timestamp"]:
            row["timestamp"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        writer.writerow(row)


def read_all() -> list[dict]:
    """Read all log entries. Returns list of dicts."""
    _ensure_file()
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def clear_log() -> None:
    """Delete all entries, keep headers."""
    with open(LOG_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()


def get_csv_path() -> str:
    """Return the absolute path to the CSV file."""
    _ensure_file()
    return str(LOG_FILE)
