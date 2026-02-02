"""Build a deterministic report contract JSON from report_model (dev tool)."""
from __future__ import annotations

import argparse
import json
import math
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

try:
    import pandas as pd
except Exception:  # pragma: no cover - optional dependency for local tooling
    pd = None  # type: ignore

from core.analysis_pack import build_analysis_pack
from core.models import OptionLeg, StrategyInput
from core.roi import NET_PREMIUM
from reporting.report_model import build_report_model


AS_OF = "2025-01-02"
EXPIRY = "2025-06-21"


def _to_jsonable(value: Any) -> Any:
    if pd is not None and isinstance(value, pd.DataFrame):
        return value.to_dict(orient="records")
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, Mapping):
        return {str(k): _to_jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_to_jsonable(item) for item in value]
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return None
        return value
    if hasattr(value, "item"):
        try:
            return _to_jsonable(value.item())
        except Exception:
            pass
    return value


def _build_contract() -> dict:
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=100.0,
        avg_cost=100.0,
        legs=[
            OptionLeg(kind="put", position=1.0, strike=90.0, premium=1.5),
            OptionLeg(kind="call", position=-1.0, strike=110.0, premium=2.0),
        ],
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={"strategy_name": "Collar", "as_of": AS_OF, "expiry": EXPIRY},
        pricing_mode="MID",
        roi_policy=NET_PREMIUM,
        vol_mode="ATM",
        atm_iv=0.2,
        underlying_profile={},
        bbg_leg_snapshots=None,
        scenario_mode="STANDARD",
        downside_tgt=0.8,
        upside_tgt=1.2,
    )
    state = {
        "analysis_pack": pack,
        "underlying_snapshot": pack.get("underlying", {}).get("profile") or {},
        "resolved_underlying": pack.get("underlying", {}).get("resolved")
        or pack.get("underlying", {}).get("ticker"),
        "underlying_ticker": pack.get("underlying", {}).get("ticker") or "TEST",
        "spot": pack.get("underlying", {}).get("spot"),
        "expiry": pack.get("strategy", {}).get("expiry") or EXPIRY,
        "strategy_name": pack.get("strategy", {}).get("name") or "Collar",
        "stock_position": strategy_input.stock_position,
        "avg_cost": strategy_input.avg_cost,
    }
    return build_report_model(state)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build a deterministic report_model JSON contract."
    )
    parser.add_argument(
        "out",
        nargs="?",
        default=str(Path("Design") / "sample_report_contract.json"),
        help="Output JSON path (default: Design/sample_report_contract.json)",
    )
    args = parser.parse_args()

    contract = _build_contract()
    payload = _to_jsonable(contract)
    json_text = json.dumps(payload, indent=2, sort_keys=True)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json_text, encoding="utf-8")
    print(json_text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
