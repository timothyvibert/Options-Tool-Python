from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional

DEFAULT_DISCLOSURE = (
    "Options involve risk and are not suitable for all investors. Past performance "
    "is not indicative of future results."
)


def _ensure_dict(report_model: object) -> Dict[str, Any]:
    if isinstance(report_model, dict):
        return report_model
    to_dict = getattr(report_model, "to_dict", None)
    if callable(to_dict):
        try:
            return to_dict()
        except Exception:
            pass
    raw = getattr(report_model, "__dict__", None)
    if isinstance(raw, dict):
        return dict(raw)
    return {}


def _safe_text(value: object, default: str = "--") -> str:
    if value is None:
        return default
    text = str(value).strip()
    return text if text else default


def _format_mmddyyyy(value: object) -> str:
    if value is None:
        return "--"
    if isinstance(value, datetime):
        return value.strftime("%m/%d/%Y")
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return "--"
        for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%Y/%m/%d"):
            try:
                parsed = datetime.strptime(text[:10], fmt)
                return parsed.strftime("%m/%d/%Y")
            except ValueError:
                continue
        try:
            parsed = datetime.fromisoformat(text[:10])
            return parsed.strftime("%m/%d/%Y")
        except ValueError:
            return text
    return str(value)


def _strip_markdown(text: str) -> str:
    return text.replace("**", "").replace("__", "")


def _pick_value(row: Mapping[str, object], keys: Iterable[str]) -> object:
    for key in keys:
        if key in row:
            return row.get(key)
    return None


def _metric_map(rows: object) -> Dict[str, Mapping[str, object]]:
    if not isinstance(rows, list):
        return {}
    mapping: Dict[str, Mapping[str, object]] = {}
    for row in rows:
        if not isinstance(row, Mapping):
            continue
        label = row.get("metric")
        if isinstance(label, str) and label:
            mapping[label] = row
    return mapping


def _metric_value(metric_lookup: Dict[str, Mapping[str, object]], label: str) -> str:
    row = metric_lookup.get(label)
    if not row:
        return "--"
    value = row.get("combined", row.get("options"))
    return _safe_text(value)


def _scenario_cards(raw_cards: object) -> List[Dict[str, str]]:
    cards: List[Dict[str, str]] = []
    if isinstance(raw_cards, list):
        for card in raw_cards:
            if not isinstance(card, Mapping):
                continue
            cards.append(
                {
                    "title": _safe_text(card.get("title")),
                    "condition": _safe_text(card.get("condition"), default=""),
                    "body": _safe_text(card.get("body"), default=""),
                }
            )
    labels = ["Bearish", "Stagnant", "Bullish"]
    while len(cards) < 3:
        label = labels[len(cards)]
        cards.append({"title": label, "condition": "", "body": "--"})
    return cards[:3]


def _details_text(report_model: Mapping[str, object]) -> str:
    commentary = report_model.get("commentary_blocks")
    if isinstance(commentary, Mapping):
        blocks = commentary.get("blocks")
        if isinstance(blocks, list) and blocks:
            first = blocks[0]
            if isinstance(first, Mapping):
                text = str(first.get("text") or "").strip()
                if text:
                    return _strip_markdown(text)
    return "Strategy details are based on current market conditions and may change."


def _disclosure_text(report_model: Mapping[str, object]) -> str:
    disclaimers = report_model.get("disclaimers")
    if isinstance(disclaimers, list):
        cleaned = [str(item).strip() for item in disclaimers if str(item).strip()]
        cleaned = [item for item in cleaned if item != "--"]
        if cleaned:
            return " ".join(cleaned)
    return DEFAULT_DISCLOSURE


def _legs_rows(report_model: Mapping[str, object]) -> List[Dict[str, str]]:
    structure = report_model.get("structure")
    legs = structure.get("legs") if isinstance(structure, Mapping) else None
    rows: List[Dict[str, str]] = []
    if isinstance(legs, list) and legs:
        for leg in legs:
            if not isinstance(leg, Mapping):
                continue
            premium = _safe_text(leg.get("premium"))
            rows.append(
                {
                    "action": _safe_text(leg.get("side")),
                    "expiration": _safe_text(leg.get("Expiry") or leg.get("expiry")),
                    "strike": _safe_text(leg.get("strike")),
                    "type": _safe_text(leg.get("type")),
                    "price": premium,
                    "delta": "--",
                    "otm": "--",
                    "premium": premium,
                }
            )
    if not rows:
        rows.append(
            {
                "action": "--",
                "expiration": "--",
                "strike": "--",
                "type": "--",
                "price": "--",
                "delta": "--",
                "otm": "--",
                "premium": "--",
            }
        )
    return rows


def _key_levels_rows(report_model: Mapping[str, object]) -> List[Dict[str, str]]:
    raw = report_model.get("key_levels_display_rows")
    if not isinstance(raw, list):
        raw = report_model.get("key_levels")
    rows: List[Dict[str, str]] = []
    if isinstance(raw, list):
        for item in raw:
            if not isinstance(item, Mapping):
                continue
            scenario = _safe_text(_pick_value(item, ["Scenario", "scenario"]))
            rows.append(
                {
                    "scenario": scenario,
                    "price": _safe_text(_pick_value(item, ["Price", "price"])),
                    "move_pct": _safe_text(_pick_value(item, ["Move %", "move_pct"])),
                    "stock_pnl": _safe_text(_pick_value(item, ["Stock PnL", "stock_pnl"])),
                    "option_pnl": _safe_text(_pick_value(item, ["Option PnL", "option_pnl"])),
                    "net_pnl": _safe_text(_pick_value(item, ["Net PnL", "net_pnl"])),
                    "net_roi": _safe_text(_pick_value(item, ["Net ROI", "net_roi"])),
                    "is_current": scenario == "Current Market Price",
                }
            )
    if not rows:
        rows.append(
            {
                "scenario": "--",
                "price": "--",
                "move_pct": "--",
                "stock_pnl": "--",
                "option_pnl": "--",
                "net_pnl": "--",
                "net_roi": "--",
                "is_current": False,
            }
        )
    return rows


def _build_context(report_model: Mapping[str, object]) -> Dict[str, object]:
    header = report_model.get("header")
    header = header if isinstance(header, Mapping) else {}
    metrics = report_model.get("metrics")
    metrics = metrics if isinstance(metrics, Mapping) else {}
    metric_lookup = _metric_map(metrics.get("rows"))

    repo_root = Path(__file__).resolve().parents[2]
    logo_path = repo_root / "Design" / "UBS Logo Png.png"
    logo_ref = "Design/UBS Logo Png.png" if logo_path.exists() else ""

    return {
        "logo_path": logo_ref,
        "as_of": _format_mmddyyyy(header.get("report_time")),
        "strategy_name": _safe_text(header.get("strategy_name")),
        "ticker": _safe_text(header.get("ticker")),
        "spot": _safe_text(header.get("last_price")),
        "details_text": _details_text(report_model),
        "metric_tiles": [
            {"label": "Max Profit", "value": _metric_value(metric_lookup, "Max Profit")},
            {"label": "Max Loss", "value": _metric_value(metric_lookup, "Max Loss")},
            {"label": "Max ROI", "value": _metric_value(metric_lookup, "Max ROI")},
            {"label": "Min ROI", "value": _metric_value(metric_lookup, "Min ROI")},
        ],
        "legs": _legs_rows(report_model),
        "scenario_cards": _scenario_cards(report_model.get("scenario_analysis_cards")),
        "key_levels": _key_levels_rows(report_model),
        "disclosures_text": _disclosure_text(report_model),
    }


def build_report_pdf_html(report_model: Mapping[str, object], *, out_path: Optional[str] = None) -> bytes:
    try:
        from jinja2 import Environment, FileSystemLoader, select_autoescape
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise RuntimeError(
            "Jinja2 not installed. Install via conda or pip (e.g., conda install jinja2)."
        ) from exc

    try:
        from weasyprint import HTML
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise RuntimeError(
            "WeasyPrint not installed. Install via conda or pip (e.g., conda install weasyprint)."
        ) from exc

    model = _ensure_dict(report_model)
    context = _build_context(model)

    template_dir = Path(__file__).resolve().parent / "templates"
    asset_dir = Path(__file__).resolve().parent / "assets"
    css_path = asset_dir / "report.css"
    css_text = css_path.read_text(encoding="utf-8")

    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("base.html")
    html_text = template.render(report=context, css=css_text)

    base_url = str(Path(__file__).resolve().parents[2])
    html = HTML(string=html_text, base_url=base_url)
    try:
        pdf_bytes = html.write_pdf()
    except (OSError, RuntimeError) as exc:  # pragma: no cover - environment dependent
        raise RuntimeError(
            "WeasyPrint installed but required system libraries are missing on Windows. "
            "Recommended conda install: conda install -c conda-forge weasyprint jinja2."
        ) from exc

    if out_path:
        Path(out_path).write_bytes(pdf_bytes)
    return pdf_bytes
