from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def _load_schema() -> Dict[str, Any]:
    schema_path = Path(__file__).with_name("schema.json")
    return json.loads(schema_path.read_text(encoding="utf-8"))


def validate_report_contract_v1(contract: Dict[str, Any]) -> None:
    try:
        import jsonschema
    except ImportError as exc:  # pragma: no cover - dependency handled in requirements
        raise RuntimeError(
            "jsonschema is required to validate report_contract_v1. "
            "Install via pip or conda (e.g., pip install jsonschema)."
        ) from exc

    schema = _load_schema()
    validator = jsonschema.Draft7Validator(schema)
    errors = sorted(validator.iter_errors(contract), key=lambda err: list(err.path))
    if errors:
        error = errors[0]
        path = ".".join([str(part) for part in error.path]) if error.path else "<root>"
        raise ValueError(f"report_contract_v1 validation error at {path}: {error.message}")
