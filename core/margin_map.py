"""Margin requirement text lookup from MarginMap_CBOE data.

Loads the exported CSV from the Excel workbook's MarginMap_CBOE sheet
and provides lookup by (strategy_code, account_type, requirement_stage).
"""
from __future__ import annotations

import csv
from pathlib import Path

_MAP_FILE = Path(__file__).resolve().parent.parent / "data" / "margin_map_cboe.csv"
_cache: dict[str, str] = {}
_loaded = False


def _load() -> None:
    global _loaded
    if _loaded:
        return
    _loaded = True
    if not _MAP_FILE.exists():
        return
    with open(_MAP_FILE, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rec = (row.get("RecordType") or "").strip().upper()
            if rec != "MARGIN_RULE":
                continue
            code = (row.get("StrategyCode") or "").strip().upper()
            acct = (row.get("AccountType") or "").strip().upper()
            stage = (row.get("RequirementStage") or "").strip().upper()
            text = (row.get("RequirementText") or "").strip()
            key = f"{code}|{acct}|{stage}"
            # First entry wins (some codes have multiple rules)
            if key not in _cache:
                _cache[key] = text


def lookup_requirement_text(strategy_code: str, account_type: str, stage: str) -> str:
    """Look up CBOE requirement text.  Returns empty string if not found."""
    _load()
    key = (
        f"{strategy_code.strip().upper()}"
        f"|{account_type.strip().upper()}"
        f"|{stage.strip().upper()}"
    )
    return _cache.get(key, "")


def list_all_codes() -> list[str]:
    """Return all unique strategy codes in the map."""
    _load()
    codes: set[str] = set()
    for key in _cache:
        codes.add(key.split("|")[0])
    return sorted(codes)
