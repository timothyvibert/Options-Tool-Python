from __future__ import annotations

from pathlib import Path
from typing import Optional

import pandas as pd

from core.margin import classify_strategy
from core.models import StrategyInput
from core.roi import CASH_SECURED, is_pure_short_puts


_ACCOUNT_MAP: Optional[pd.DataFrame] = None


def load_account_map() -> pd.DataFrame:
    global _ACCOUNT_MAP
    if _ACCOUNT_MAP is None:
        path = Path(__file__).resolve().parents[1] / "data" / "account_map.csv"
        _ACCOUNT_MAP = pd.read_csv(path)
    return _ACCOUNT_MAP


def determine_strategy_code(input: StrategyInput, roi_policy: str) -> str:
    base_code = classify_strategy(input)
    if roi_policy.upper() == CASH_SECURED and is_pure_short_puts(input):
        return "CSPT"
    mapping = {
        "LNG_LE_9M": "LNG",
        "SH_OPT": "NAK",
        "SH_PUT_CALL": "NAK",
    }
    return mapping.get(base_code, base_code)


def get_account_eligibility(strategy_code: str) -> pd.DataFrame:
    account_map = load_account_map()
    code = strategy_code.strip().upper()
    return account_map.loc[
        account_map["strategy_code"] == code, ["account_type", "eligibility"]
    ].copy()
