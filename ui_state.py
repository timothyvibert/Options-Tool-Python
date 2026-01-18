from __future__ import annotations

from typing import MutableMapping


def _normalize_text(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip().upper()


def reset_leg_state_on_context_change(
    state: MutableMapping[str, object],
    underlying_input: str,
    resolved_underlying: str,
    expiry: str,
    leg_count: int = 4,
) -> bool:
    signature = f"{_normalize_text(underlying_input)}|{_normalize_text(resolved_underlying)}"
    prev_underlying = state.get("prev_underlying")
    prev_expiry = state.get("prev_expiry")

    if prev_underlying is None and prev_expiry is None:
        state["prev_underlying"] = signature
        state["prev_expiry"] = expiry
        return False

    changed = signature != prev_underlying or expiry != prev_expiry
    if changed:
        for idx in range(leg_count):
            for key in (
                f"bbg_ticker_{idx}",
                f"bbg_ticker_input_{idx}",
                f"bbg_ticker_val_{idx}",
            ):
                state[key] = ""
            if not state.get(f"manual_prem_{idx}", False):
                if f"prem_{idx}" in state:
                    state[f"prem_{idx}"] = 0.0

        for key in list(state.keys()):
            if key.startswith("bbg_snapshot") or key.startswith("snapshot_"):
                state.pop(key, None)
        if "option_chain_df" in state:
            state.pop("option_chain_df", None)

    state["prev_underlying"] = signature
    state["prev_expiry"] = expiry
    return changed
