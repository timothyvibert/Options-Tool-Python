from __future__ import annotations

import math
from dataclasses import asdict, is_dataclass
from datetime import date, datetime
from decimal import Decimal
from typing import Mapping

try:
    import numpy as np
except Exception:  # pragma: no cover - optional dependency
    np = None

try:
    import pandas as pd
except Exception:  # pragma: no cover - optional dependency
    pd = None


def to_jsonable(obj):
    if obj is None or isinstance(obj, (bool, int, str)):
        return obj
    if isinstance(obj, float):
        if not math.isfinite(obj):
            return None
        return obj
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if isinstance(obj, Decimal):
        return float(obj)
    if np is not None and isinstance(obj, np.ndarray):
        return [to_jsonable(item) for item in obj.tolist()]
    if np is not None and isinstance(obj, np.generic):
        return to_jsonable(obj.item())
    if pd is not None and isinstance(obj, pd.DataFrame):
        return {
            "__type__": "DataFrame",
            "columns": [str(col) for col in obj.columns],
            "records": obj.to_dict("records"),
        }
    if pd is not None and isinstance(obj, pd.Series):
        return {"__type__": "Series", "data": obj.to_dict()}
    if isinstance(obj, Mapping):
        return {str(key): to_jsonable(value) for key, value in obj.items()}
    if isinstance(obj, (list, tuple, set)):
        return [to_jsonable(item) for item in obj]
    if is_dataclass(obj):
        return to_jsonable(asdict(obj))
    return str(obj)


def analysis_pack_to_store(pack: dict) -> dict:
    if not isinstance(pack, dict):
        return {"error": "invalid pack"}
    return to_jsonable(pack)
