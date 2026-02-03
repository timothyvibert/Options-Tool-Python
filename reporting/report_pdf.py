from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.utils import ImageReader
    from reportlab.lib.units import inch
    from reportlab.pdfgen import canvas as pdf_canvas
    from reportlab.platypus import (
        Image,
        PageBreak,
        Paragraph,
        SimpleDocTemplate,
        Spacer,
        Table,
        TableStyle,
    )
    _REPORTLAB_ERROR = None
except ImportError as exc:
    colors = None
    letter = None
    ParagraphStyle = None
    getSampleStyleSheet = None
    inch = 72
    pdf_canvas = None
    Image = None
    PageBreak = None
    ImageReader = None
    Paragraph = None
    SimpleDocTemplate = None
    Spacer = None
    Table = None
    TableStyle = None
    _REPORTLAB_ERROR = exc


# Design tokens (Report v2)
if colors is None:
    COLOR_PAGE_BG = None
    COLOR_CARD_BG = None
    COLOR_HEADER_BG = None
    COLOR_TILE_BG = None
    COLOR_BORDER = None
    COLOR_TEXT = None
    COLOR_MUTED = None
    COLOR_ACCENT = None
    COLOR_TABLE_HEADER_BG = None
    COLOR_HIGHLIGHT = None
    COLOR_CHART_STOCK = None
    COLOR_CHART_OPTIONS = None
    COLOR_CHART_COMBINED = None
else:
    COLOR_PAGE_BG = colors.white
    COLOR_CARD_BG = colors.HexColor("#FFFFFF")
    COLOR_HEADER_BG = colors.HexColor("#F8FAFC")
    COLOR_TILE_BG = colors.HexColor("#F9FAFB")
    COLOR_BORDER = colors.HexColor("#E5E7EB")
    COLOR_TEXT = colors.HexColor("#111827")
    COLOR_MUTED = colors.HexColor("#6B7280")
    COLOR_ACCENT = colors.HexColor("#E60000")
    COLOR_TABLE_HEADER_BG = colors.HexColor("#F3F4F6")
    COLOR_HIGHLIGHT = colors.HexColor("#FEF3C7")
    COLOR_CHART_STOCK = colors.HexColor("#9CA3AF")
    COLOR_CHART_OPTIONS = colors.HexColor("#2563EB")
    COLOR_CHART_COMBINED = colors.HexColor("#111827")

FONT_TITLE = 16
FONT_SECTION = 9.5
FONT_BODY = 8.5
FONT_SMALL = 7.5
FONT_TABLE_HEADER = 7.5
FONT_FOOTER = 8.5

CARD_PAD = 10
CARD_RADIUS = 5
SECTION_GAP = 10

DEFAULT_DISCLAIMERS = [
    "For informational purposes only and not an offer to sell or solicitation to buy.",
    "Options involve risk and are not suitable for all investors.",
    "Past performance is not indicative of future results.",
]

HEADER_DISCLAIMER = (
    "This material is provided for informational purposes only and does not constitute a "
    "recommendation, offer, or solicitation to buy or sell any security or investment product."
)

RISK_DISCLOSURE = (
    "Options involve risk and are not suitable for all investors. Prior to buying or selling an "
    "option, investors must receive a copy of the Options Disclosure Document. Tax treatment and "
    "investment suitability may vary; consult your financial advisor for guidance."
)


def _fmt_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:,.4f}".rstrip("0").rstrip(".")
    return str(value)


def _safe_text(value: object, fallback: str = "--") -> str:
    if value is None:
        return fallback
    text = str(value).strip()
    return text if text else fallback


def _coerce_float(value: object) -> Optional[float]:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        try:
            return float(value)
        except (TypeError, ValueError):
            return None
    if isinstance(value, str):
        text = value.strip()
        if not text or text == "--":
            return None
        text = text.replace("$", "").replace(",", "").replace("%", "")
        try:
            return float(text)
        except ValueError:
            return None
    return None


def _format_mmddyyyy(value: object) -> str:
    if value is None:
        return "--"
    if isinstance(value, datetime):
        return value.strftime("%m/%d/%Y")
    text = str(value).strip()
    if not text:
        return "--"
    head = text[:10]
    for fmt in ("%Y-%m-%d", "%m/%d/%Y"):
        try:
            parsed = datetime.strptime(head, fmt)
            return parsed.strftime("%m/%d/%Y")
        except ValueError:
            continue
    return text


def _format_currency_symbol(value: object) -> str:
    numeric = _coerce_float(value)
    if numeric is None:
        return "--"
    return f"${numeric:,.2f}"


def _format_currency_plain(value: object) -> str:
    numeric = _coerce_float(value)
    if numeric is None:
        return "--"
    return f"{numeric:,.2f}"


def _format_percent(value: object, decimals: int = 2) -> str:
    if isinstance(value, str) and "%" in value:
        return value
    numeric = _coerce_float(value)
    if numeric is None:
        return "--"
    return f"{numeric:.{decimals}f}%"


def _build_key_value_table(rows: List[List[Any]]) -> Table:
    data = [[Paragraph(f"<b>{label}</b>", _styles()["label"]), _fmt_value(value)] for label, value in rows]
    table = Table(data, colWidths=[2.0 * inch, 4.5 * inch])
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    return table


def _styles(base_font: str = "Helvetica") -> Dict[str, ParagraphStyle]:
    styles = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "title",
            parent=styles["Heading1"],
            fontName=base_font,
            fontSize=FONT_TITLE,
            leading=FONT_TITLE + 2,
            textColor=COLOR_TEXT,
            spaceAfter=6,
        ),
        "section": ParagraphStyle(
            "section",
            parent=styles["Heading2"],
            fontName=base_font,
            fontSize=FONT_SECTION,
            leading=FONT_SECTION + 2,
            textColor=COLOR_TEXT,
            spaceBefore=10,
            spaceAfter=5,
        ),
        "label": ParagraphStyle(
            "label",
            parent=styles["BodyText"],
            fontName=base_font,
            fontSize=FONT_BODY,
            leading=FONT_BODY + 2,
            textColor=COLOR_TEXT,
        ),
        "body": ParagraphStyle(
            "body",
            parent=styles["BodyText"],
            fontName=base_font,
            fontSize=FONT_BODY,
            leading=FONT_BODY + 3,
            textColor=COLOR_TEXT,
        ),
        "small": ParagraphStyle(
            "small",
            parent=styles["BodyText"],
            fontName=base_font,
            fontSize=FONT_SMALL,
            leading=FONT_SMALL + 3,
            textColor=COLOR_MUTED,
        ),
    }


def _draw_payoff_chart_vector(
    canvas_obj,
    box: tuple[float, float, float, float],
    payoff_payload: Dict[str, Any],
    base_font: str,
) -> None:
    x0, y0, w, h = box
    x = payoff_payload.get("price_grid") or []
    combined = payoff_payload.get("combined_pnl") or payoff_payload.get("pnl") or []
    stock = payoff_payload.get("stock_pnl") or []
    options = payoff_payload.get("options_pnl") or payoff_payload.get("option_pnl") or []
    if not x or not combined or len(x) != len(combined):
        canvas_obj.setFont(base_font, 9)
        canvas_obj.drawCentredString(x0 + w / 2, y0 + h / 2, "Payoff chart unavailable")
        return
    try:
        x_vals = [float(v) for v in x]
        combined_vals = [float(v) for v in combined]
        stock_vals = (
            [float(v) for v in stock] if stock and len(stock) == len(x_vals) else None
        )
        option_vals = (
            [float(v) for v in options] if options and len(options) == len(x_vals) else None
        )
    except Exception:
        canvas_obj.setFont(base_font, 9)
        canvas_obj.drawCentredString(x0 + w / 2, y0 + h / 2, "Payoff chart unavailable")
        return

    series = [
        ("Stock", stock_vals, COLOR_CHART_STOCK),
        ("Options", option_vals, COLOR_CHART_OPTIONS),
        ("Combined", combined_vals, COLOR_CHART_COMBINED),
    ]
    series = [item for item in series if item[1] is not None]
    all_y = []
    for _, vals, _ in series:
        all_y.extend(vals)
    if not all_y:
        canvas_obj.setFont(base_font, 9)
        canvas_obj.drawCentredString(x0 + w / 2, y0 + h / 2, "Payoff chart unavailable")
        return

    x_min = min(x_vals)
    x_max = max(x_vals)
    if x_min == x_max:
        x_min -= 1.0
        x_max += 1.0
    y_min = min(all_y)
    y_max = max(all_y)
    if y_min == y_max:
        y_min -= 1.0
        y_max += 1.0
    y_pad = (y_max - y_min) * 0.1
    y_min -= y_pad
    y_max += y_pad

    def x_to_px(val: float) -> float:
        return x0 + (val - x_min) / (x_max - x_min) * w

    def y_to_px(val: float) -> float:
        return y0 + (val - y_min) / (y_max - y_min) * h

    canvas_obj.setStrokeColor(colors.lightgrey)
    canvas_obj.setLineWidth(0.5)
    canvas_obj.rect(x0, y0, w, h, stroke=1, fill=0)

    if y_min <= 0 <= y_max:
        y_zero = y_to_px(0.0)
        canvas_obj.setStrokeColor(colors.grey)
        canvas_obj.setLineWidth(0.5)
        canvas_obj.line(x0, y_zero, x0 + w, y_zero)

    strikes = payoff_payload.get("strikes") or []
    breakevens = payoff_payload.get("breakevens") or []
    spot = payoff_payload.get("spot")
    for value in strikes:
        try:
            val = float(value)
        except Exception:
            continue
        if x_min <= val <= x_max:
            canvas_obj.setStrokeColor(colors.lightgrey)
            canvas_obj.setLineWidth(0.5)
            canvas_obj.line(x_to_px(val), y0, x_to_px(val), y0 + h)
    for value in breakevens:
        try:
            val = float(value)
        except Exception:
            continue
        if x_min <= val <= x_max:
            canvas_obj.setStrokeColor(colors.grey)
            canvas_obj.setLineWidth(0.5)
            canvas_obj.line(x_to_px(val), y0, x_to_px(val), y0 + h)
    try:
        spot_val = float(spot)
    except Exception:
        spot_val = None
    if spot_val is not None and x_min <= spot_val <= x_max:
        canvas_obj.setStrokeColor(colors.darkgrey)
        canvas_obj.setLineWidth(0.75)
        canvas_obj.line(x_to_px(spot_val), y0, x_to_px(spot_val), y0 + h)
        canvas_obj.setFont(base_font, 7)
        canvas_obj.drawString(x_to_px(spot_val) + 2, y0 + h - 10, "Spot")

    canvas_obj.setLineWidth(0.8)
    for label, vals, color in series:
        canvas_obj.setStrokeColor(color)
        path = canvas_obj.beginPath()
        first_x, first_y = x_vals[0], vals[0]
        path.moveTo(x_to_px(first_x), y_to_px(first_y))
        for px, py in zip(x_vals[1:], vals[1:]):
            path.lineTo(x_to_px(px), y_to_px(py))
        canvas_obj.drawPath(path, stroke=1, fill=0)

    legend_x = x0 + w - 70
    legend_y = y0 + h - 10
    canvas_obj.setFont(base_font, 7)
    for label, _, color in series:
        canvas_obj.setStrokeColor(color)
        canvas_obj.line(legend_x, legend_y, legend_x + 12, legend_y)
        canvas_obj.setFillColor(COLOR_TEXT)
        canvas_obj.drawString(legend_x + 15, legend_y - 3, label)
        legend_y -= 10


def _draw_card(
    canvas_obj,
    x: float,
    y: float,
    w: float,
    h: float,
    title: str | None,
    base_font: str,
    *,
    fill_color=COLOR_CARD_BG,
    border_color=COLOR_BORDER,
    title_color=COLOR_TEXT,
    title_size: float = FONT_SECTION,
) -> None:
    canvas_obj.setFillColor(fill_color)
    canvas_obj.setStrokeColor(border_color)
    canvas_obj.setLineWidth(0.6)
    canvas_obj.roundRect(x, y, w, h, CARD_RADIUS, stroke=1, fill=1)
    if title:
        canvas_obj.setFillColor(title_color)
        canvas_obj.setFont("Helvetica-Bold", title_size)
        canvas_obj.drawString(x + CARD_PAD, y + h - (CARD_PAD + 4), title)


def _draw_table(
    canvas_obj,
    table: Table,
    x: float,
    y: float,
    w: float,
    h: float,
) -> None:
    tw, th = table.wrap(w, h)
    if th > h:
        table.setStyle(
            TableStyle(
                [
                    ("FONTSIZE", (0, 0), (-1, -1), 7),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                    ("TOPPADDING", (0, 0), (-1, -1), 2),
                ]
            )
        )
        tw, th = table.wrap(w, h)
    table.drawOn(canvas_obj, x, y + h - th)


def _draw_paragraphs(
    canvas_obj,
    paragraphs: list[Paragraph],
    x: float,
    y: float,
    w: float,
    h: float,
    leading: float,
) -> None:
    cursor = y + h - leading
    for para in paragraphs:
        tw, th = para.wrap(w, h)
        if cursor - th < y:
            break
        para.drawOn(canvas_obj, x, cursor - th)
        cursor -= th + 2


def _wrap_lines(
    canvas_obj,
    text: str,
    max_width: float,
    font_name: str,
    font_size: float,
) -> list[str]:
    words = text.split()
    if not words:
        return [""]
    lines: list[str] = []
    line = ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if canvas_obj.stringWidth(candidate, font_name, font_size) <= max_width:
            line = candidate
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def _draw_wrapped_text(
    canvas_obj,
    text: str,
    x: float,
    y: float,
    w: float,
    h: float,
    font_name: str,
    font_size: float,
    leading: float,
    color=COLOR_TEXT,
) -> None:
    canvas_obj.setFillColor(color)
    canvas_obj.setFont(font_name, font_size)
    lines: list[str] = []
    for raw_line in str(text).splitlines():
        if raw_line.strip() == "":
            lines.append("")
            continue
        lines.extend(_wrap_lines(canvas_obj, raw_line, w, font_name, font_size))
    cursor = y + h - font_size
    for line in lines:
        if cursor < y:
            break
        canvas_obj.drawString(x, cursor, line)
        cursor -= leading


def build_report_pdf(
    path: str,
    title: str,
    as_of: str,
    inputs: Dict[str, Any],
    summary: Dict[str, Any],
    scenario_df: pd.DataFrame,
    notes: List[str],
    report_model: Optional[Dict[str, Any]] = None,
) -> None:
    if _REPORTLAB_ERROR is not None:
        raise RuntimeError(
            "reportlab is required to build PDF reports. Install reportlab to continue."
        ) from _REPORTLAB_ERROR
    # Disable PDF page compression to reduce cross-version variance and satisfy minimum-size smoke test.
    doc = SimpleDocTemplate(
        path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36,
        pageCompression=0,
    )
    styles = _styles()
    story: List[Any] = []

    story.append(Paragraph(title, styles["title"]))
    header_rows = [
        ["Ticker", inputs.get("ticker", "")],
        ["Resolved Ticker", inputs.get("resolved_ticker", "")],
        ["Strategy", inputs.get("strategy_name", "")],
        ["Expiry", inputs.get("expiry", "")],
        ["Pricing Mode", inputs.get("pricing_mode", "")],
        ["As Of", as_of],
    ]
    if isinstance(report_model, dict):
        stock_banner = report_model.get("stock_banner")
        if isinstance(stock_banner, dict):
            dividend_yield = stock_banner.get("dividend_yield")
            if dividend_yield:
                header_rows.append(["Dividend Yield", dividend_yield])
            week_52_range = stock_banner.get("week_52_range")
            if week_52_range and week_52_range != "--":
                header_rows.append(["52W High/Low", week_52_range])
            high_dt_52week = stock_banner.get("high_dt_52week")
            if high_dt_52week and high_dt_52week != "--":
                header_rows.append(["52W High Date", high_dt_52week])
            low_dt_52week = stock_banner.get("low_dt_52week")
            if low_dt_52week and low_dt_52week != "--":
                header_rows.append(["52W Low Date", low_dt_52week])
            chg_pct_ytd = stock_banner.get("chg_pct_ytd")
            if chg_pct_ytd and chg_pct_ytd != "--":
                header_rows.append(["YTD Change", chg_pct_ytd])
            earnings_date = stock_banner.get("earnings_date")
            if earnings_date and earnings_date != "--":
                header_rows.append(["Earnings Date", earnings_date])
            if stock_banner.get("has_stock_position"):
                shares = stock_banner.get("shares")
                avg_cost = stock_banner.get("avg_cost")
                if shares and shares != "--":
                    header_rows.append(["Shares", shares])
                if avg_cost and avg_cost != "--":
                    header_rows.append(["Avg Cost", avg_cost])
    story.append(_build_key_value_table(header_rows))
    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("Trade Inputs", styles["section"]))
    input_rows = [
        ["Spot", inputs.get("spot")],
        ["Stock Position", inputs.get("stock_position")],
        ["Average Cost", inputs.get("avg_cost")],
        ["ROI Policy", inputs.get("roi_policy")],
    ]
    story.append(_build_key_value_table(input_rows))
    story.append(Spacer(1, 0.1 * inch))

    legs = inputs.get("legs", [])
    legs_data = [["Type", "Side", "Qty", "Strike", "Premium"]]
    for leg in legs:
        legs_data.append(
            [
                _fmt_value(leg.get("type")),
                _fmt_value(leg.get("side")),
                _fmt_value(leg.get("qty")),
                _fmt_value(leg.get("strike")),
                _fmt_value(leg.get("premium")),
            ]
        )
    legs_table = Table(legs_data, colWidths=[1.0 * inch] * 5)
    legs_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.append(legs_table)

    story.append(Paragraph("Summary", styles["section"]))
    summary_rows = [
        ["Min PnL", summary.get("min_pnl")],
        ["Max PnL", summary.get("max_pnl")],
        ["Breakevens", summary.get("breakevens")],
        ["PoP", summary.get("pop")],
        ["Margin Proxy", summary.get("margin_proxy")],
        ["Capital Basis", summary.get("capital_basis")],
    ]
    story.append(_build_key_value_table(summary_rows))

    story.append(Paragraph("Scenario Table (First 10 Rows)", styles["section"]))
    if scenario_df is None or scenario_df.empty:
        story.append(Paragraph("No scenario data available.", styles["body"]))
    else:
        display_df = scenario_df.head(10).copy()
        if "commentary" in display_df.columns:
            display_df["commentary"] = display_df["commentary"].fillna("")
        columns = list(display_df.columns)
        table_data = [columns]
        for _, row in display_df.iterrows():
            row_data = []
            for col in columns:
                value = row[col]
                if col == "commentary":
                    row_data.append(Paragraph(str(value), styles["small"]))
                else:
                    row_data.append(_fmt_value(value))
            table_data.append(row_data)
        table = Table(table_data, repeatRows=1)
        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                    ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ]
            )
        )
        story.append(table)

    scenario_cards = []
    key_levels_rows = []
    has_stock_position = True
    if isinstance(report_model, dict):
        scenario_cards = report_model.get("scenario_analysis_cards") or []
        key_levels_rows = report_model.get("key_levels_display_rows_by_price") or report_model.get(
            "key_levels_display_rows"
        ) or []
        if "has_stock_position" in report_model:
            has_stock_position = bool(report_model.get("has_stock_position"))

    if isinstance(scenario_cards, list) and scenario_cards:
        story.append(Paragraph("Scenario Analysis", styles["section"]))
        card_cells = []
        for card in scenario_cards[:3]:
            if not isinstance(card, dict):
                card_cells.append(Paragraph("", styles["body"]))
                continue
            title_text = str(card.get("title") or "")
            condition_text = str(card.get("condition") or "")
            body_text = str(card.get("body") or "")
            parts = []
            if title_text:
                parts.append(f"<b>{title_text}</b>")
            if condition_text:
                parts.append(condition_text)
            if body_text:
                parts.append(body_text)
            card_cells.append(Paragraph("<br/>".join(parts), styles["small"]))
        card_table = Table([card_cells], colWidths=[2.4 * inch, 2.4 * inch, 2.4 * inch])
        card_table.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                    ("LEFTPADDING", (0, 0), (-1, -1), 6),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]
            )
        )
        story.append(card_table)

    if isinstance(key_levels_rows, list) and key_levels_rows:
        story.append(Paragraph("Key Levels", styles["section"]))
        if has_stock_position:
            columns = [
                "Scenario",
                "Price",
                "Move %",
                "Stock PnL",
                "Option PnL",
                "Option ROI",
                "Net PnL",
                "Net ROI",
            ]
        else:
            columns = [
                "Scenario",
                "Price",
                "Move %",
                "Option PnL",
                "Option ROI",
                "Net PnL",
                "Net ROI",
            ]
        table_data = [columns]
        for row in key_levels_rows:
            if not isinstance(row, dict):
                continue
            table_data.append(
                [
                    _fmt_value(row.get("Scenario", row.get("scenario", ""))),
                    _fmt_value(row.get("Price", row.get("price", ""))),
                    _fmt_value(row.get("Move %", row.get("move_pct", ""))),
                    *(
                        [_fmt_value(row.get("Stock PnL", row.get("stock_pnl", "")))]
                        if has_stock_position
                        else []
                    ),
                    _fmt_value(row.get("Option PnL", row.get("option_pnl", ""))),
                    _fmt_value(row.get("Option ROI", row.get("option_roi", ""))),
                    _fmt_value(row.get("Net PnL", row.get("net_pnl", ""))),
                    _fmt_value(row.get("Net ROI", row.get("net_roi", ""))),
                ]
            )
        key_table = Table(table_data, repeatRows=1)
        key_table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                    ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ]
            )
        )
        story.append(key_table)

    story.append(Paragraph("Assumptions & Disclaimers", styles["section"]))
    warning_text = summary.get("warning")
    if warning_text:
        story.append(Paragraph(str(warning_text), styles["small"]))
    for note in notes:
        story.append(Paragraph(f"- {note}", styles["small"]))

    doc.build(story)


def _build_report_pdf_v2_legacy(
    path: str,
    *,
    report_model: Dict[str, Any],
    logo_path: Optional[str] = None,
) -> None:
    if _REPORTLAB_ERROR is not None:
        raise RuntimeError(
            "reportlab is required to build PDF reports. Install reportlab to continue."
        ) from _REPORTLAB_ERROR

    base_font = "Helvetica"

    styles = _styles(base_font=base_font)

    if pdf_canvas is None:
        raise RuntimeError("reportlab canvas unavailable")

    resolved_logo_path = None
    if logo_path:
        resolved_logo_path = Path(logo_path)
    else:
        repo_root = Path(__file__).resolve().parents[1]
        resolved_logo_path = repo_root / "Design" / "UBS Logo Png.png"
    if resolved_logo_path and not resolved_logo_path.exists():
        resolved_logo_path = None

    header = report_model.get("header", {}) if isinstance(report_model, dict) else {}
    ticker = header.get("ticker", "--")
    resolved = header.get("resolved_underlying", header.get("ticker", "--"))
    strategy_name = header.get("strategy_name", "--")
    expiry = header.get("expiry", "--")
    spot = header.get("last_price", "--")
    as_of = header.get("report_time", "--")
    policies = header.get("policies", "--")

    PAGE_W, PAGE_H = letter
    margin_left = 30
    margin_right = 30
    margin_top = 26
    margin_bottom = 18
    content_w = PAGE_W - margin_left - margin_right

    header_h = 84
    gap = SECTION_GAP

    structure_w = 220
    structure_h = 170
    payoff_h = 290
    metrics_h = 150
    disclaim_h = 70

    scenario_cards_h = 150
    key_levels_h = 260

    def _draw_header(c):
        x = margin_left
        y = PAGE_H - margin_top - header_h
        c.setFillColor(COLOR_HEADER_BG)
        c.setStrokeColor(COLOR_BORDER)
        c.setLineWidth(0.6)
        c.rect(x, y, content_w, header_h, stroke=1, fill=1)
        logo_w = 78
        logo_h = 24
        if resolved_logo_path and Image is not None:
            try:
                c.drawImage(
                    str(resolved_logo_path),
                    x + 10,
                    y + header_h - logo_h - 10,
                    width=logo_w,
                    height=logo_h,
                    preserveAspectRatio=True,
                    mask="auto",
                )
            except Exception:
                pass
        def _display(value: object) -> str:
            if value is None or value == "":
                return "--"
            return str(value)

        left_x = x + logo_w + 18
        right_x = x + content_w * 0.64
        right_w = x + content_w - right_x - 10

        primary_y = y + header_h - 18
        strategy_y = primary_y - 18
        meta_y = strategy_y - 14

        c.setFillColor(COLOR_TEXT)
        c.setFont("Helvetica-Bold", FONT_SECTION + 1)
        c.drawString(left_x, primary_y, _display(resolved))

        c.setFillColor(COLOR_ACCENT)
        c.setFont("Helvetica-Bold", FONT_TITLE)
        c.drawString(left_x, strategy_y, _display(strategy_name))

        c.setFillColor(COLOR_MUTED)
        c.setFont(base_font, FONT_BODY)
        c.drawString(
            left_x,
            meta_y,
            f"Expiry: {_display(expiry)} | Spot: {_display(spot)} | As-of: {_display(as_of)}",
        )
        c.setFont(base_font, FONT_SMALL)
        c.drawString(left_x, y + 8, f"Policies: {_display(policies)}")

        profile_lines = [
            f"Name: {_display(header.get('name'))}",
            f"Sector: {_display(header.get('sector'))}",
            f"52W H/L: {_display(header.get('high_52w'))} / {_display(header.get('low_52w'))}",
            f"Div Yld: {_display(header.get('dividend_yield'))}",
            f"Earnings: {_display(header.get('earnings_date'))}",
        ]
        profile_paras = [Paragraph(line, styles["small"]) for line in profile_lines]
        _draw_paragraphs(c, profile_paras, right_x, y + 8, right_w, header_h - 16, 10)

    def _draw_footer(c, page_num):
        c.setFont(base_font, FONT_FOOTER)
        c.setFillColor(COLOR_MUTED)
        c.drawString(margin_left, margin_bottom, "UBS Financial Services Inc.")
        c.drawRightString(PAGE_W - margin_right, margin_bottom, f"Page {page_num} of 2")

    def _page1(c):
        _draw_header(c)
        y_top = PAGE_H - margin_top - header_h - gap

        # Structure card (left)
        struct_x = margin_left
        struct_y = y_top - structure_h
        _draw_card(c, struct_x, struct_y, structure_w, structure_h, "Structure", base_font)
        structure = report_model.get("structure", {}) if isinstance(report_model, dict) else {}
        legs_rows = structure.get("legs") if isinstance(structure, dict) else []
        legs_rows = legs_rows if isinstance(legs_rows, list) else []
        legs_data = [["Leg", "Side", "Expiry", "Strike", "Premium"]]
        for leg in legs_rows[:4]:
            if not isinstance(leg, dict):
                continue
            legs_data.append(
                [
                    _fmt_value(leg.get("leg")),
                    _fmt_value(leg.get("side")),
                    _fmt_value(leg.get("Expiry") or leg.get("expiry")),
                    _fmt_value(leg.get("strike")),
                    _fmt_value(leg.get("premium")),
                ]
            )
        if len(legs_data) == 1:
            legs_data.append(["--", "--", "--", "--", "--"])
        legs_table = Table(
            legs_data,
            colWidths=[0.45 * inch, 0.8 * inch, 1.1 * inch, 1.0 * inch, 1.0 * inch],
        )
        zebra = colors.HexColor("#F9FAFB")
        table_style = [
            ("BACKGROUND", (0, 0), (-1, 0), COLOR_TABLE_HEADER_BG),
            ("TEXTCOLOR", (0, 0), (-1, 0), COLOR_MUTED),
            ("GRID", (0, 0), (-1, -1), 0.25, COLOR_BORDER),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTNAME", (0, 1), (-1, -1), base_font),
            ("FONTSIZE", (0, 0), (-1, 0), FONT_TABLE_HEADER),
            ("FONTSIZE", (0, 1), (-1, -1), FONT_SMALL),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("ALIGN", (0, 1), (0, -1), "RIGHT"),
            ("ALIGN", (3, 1), (4, -1), "RIGHT"),
        ]
        for row in range(1, len(legs_data), 2):
            table_style.append(("BACKGROUND", (0, row), (-1, row), zebra))
        legs_table.setStyle(
            TableStyle(table_style)
        )
        _draw_table(c, legs_table, struct_x + CARD_PAD, struct_y + CARD_PAD, structure_w - 2 * CARD_PAD, structure_h - 24)

        # Payoff card (right)
        payoff_x = margin_left + structure_w + gap
        payoff_w = content_w - structure_w - gap
        payoff_y = y_top - payoff_h
        _draw_card(c, payoff_x, payoff_y, payoff_w, payoff_h, "Payoff", base_font)
        payoff_payload = report_model.get("payoff_payload") if isinstance(report_model, dict) else None
        if not isinstance(payoff_payload, dict):
            payoff_payload = report_model.get("payoff") if isinstance(report_model, dict) else {}
        png_bytes, _ = _try_export_payoff_png(payoff_payload if isinstance(payoff_payload, dict) else {})
        if png_bytes and ImageReader is not None:
            try:
                img = ImageReader(BytesIO(png_bytes))
                iw, ih = img.getSize()
                scale = min(payoff_w / iw, (payoff_h - 18) / ih)
                draw_w = iw * scale
                draw_h = ih * scale
                draw_x = payoff_x + (payoff_w - draw_w) / 2
                draw_y = payoff_y + (payoff_h - 18 - draw_h) / 2
                c.drawImage(img, draw_x, draw_y, width=draw_w, height=draw_h)
            except Exception:
                _draw_payoff_chart_vector(
                    c,
                    (payoff_x + CARD_PAD, payoff_y + CARD_PAD, payoff_w - 2 * CARD_PAD, payoff_h - 24),
                    payoff_payload if isinstance(payoff_payload, dict) else {},
                    base_font,
                )
        else:
            _draw_payoff_chart_vector(
                c,
                (payoff_x + CARD_PAD, payoff_y + CARD_PAD, payoff_w - 2 * CARD_PAD, payoff_h - 24),
                payoff_payload if isinstance(payoff_payload, dict) else {},
                base_font,
            )

        y_next = y_top - payoff_h - gap

        # Metrics card
        metrics_y = y_next - metrics_h
        _draw_card(c, margin_left, metrics_y, content_w, metrics_h, "Payoff & Metrics", base_font)
        metrics = report_model.get("metrics", {}) if isinstance(report_model, dict) else {}
        metrics_rows = metrics.get("rows") if isinstance(metrics, dict) else []
        metrics_data = [["Metric", "Options", "Combined"]]
        if isinstance(metrics_rows, list) and metrics_rows:
            for row in metrics_rows[:9]:
                if not isinstance(row, dict):
                    continue
                metrics_data.append(
                    [
                        _fmt_value(row.get("metric")),
                        _fmt_value(row.get("options")),
                        _fmt_value(row.get("combined")),
                    ]
                )
        else:
            metrics_data.append(["--", "--", "--"])
        metrics_table = Table(
            metrics_data,
            colWidths=[2.6 * inch, 2.0 * inch, 2.0 * inch],
        )
        table_style = [
            ("BACKGROUND", (0, 0), (-1, 0), COLOR_TABLE_HEADER_BG),
            ("TEXTCOLOR", (0, 0), (-1, 0), COLOR_MUTED),
            ("GRID", (0, 0), (-1, -1), 0.25, COLOR_BORDER),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTNAME", (0, 1), (-1, -1), base_font),
            ("FONTSIZE", (0, 0), (-1, 0), FONT_TABLE_HEADER),
            ("FONTSIZE", (0, 1), (-1, -1), FONT_SMALL),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
        ]
        for row in range(1, len(metrics_data), 2):
            table_style.append(("BACKGROUND", (0, row), (-1, row), zebra))
        metrics_table.setStyle(TableStyle(table_style))
        _draw_table(c, metrics_table, margin_left + CARD_PAD, metrics_y + CARD_PAD, content_w - 2 * CARD_PAD, metrics_h - 22)

        # Disclaimers
        disclaim_y = metrics_y - gap - disclaim_h
        _draw_card(c, margin_left, disclaim_y, content_w, disclaim_h, "Disclaimers", base_font)
        disclaimers = report_model.get("disclaimers") if isinstance(report_model, dict) else []
        if (
            not isinstance(disclaimers, list)
            or not disclaimers
            or disclaimers == ["--"]
        ):
            disclaimers = DEFAULT_DISCLAIMERS
        paras = [Paragraph(f"- {note}", styles["small"]) for note in disclaimers[:4]]
        _draw_paragraphs(c, paras, margin_left + CARD_PAD, disclaim_y + CARD_PAD, content_w - 2 * CARD_PAD, disclaim_h - 20, 10)

        _draw_footer(c, 1)

    def _page2(c):
        _draw_header(c)
        y_top = PAGE_H - margin_top - header_h - gap
        zebra = colors.HexColor("#F9FAFB")

        # Scenario cards row
        cards_y = y_top - scenario_cards_h
        _draw_card(c, margin_left, cards_y, content_w, scenario_cards_h, "Scenario Analysis", base_font)
        cards = report_model.get("scenario_analysis_cards") if isinstance(report_model, dict) else []
        card_cells = []
        if isinstance(cards, list) and cards:
            for card in cards[:3]:
                if not isinstance(card, dict):
                    card_cells.append(Paragraph("", styles["small"]))
                    continue
                title_text = str(card.get("title") or "")
                condition_text = str(card.get("condition") or "")
                body_text = str(card.get("body") or "")
                parts = []
                if title_text:
                    parts.append(f"<b>{title_text}</b>")
                if condition_text:
                    parts.append(condition_text)
                if body_text:
                    parts.append(body_text)
                card_cells.append(Paragraph("<br/>".join(parts), styles["small"]))
        else:
            card_cells = [
                Paragraph("--", styles["small"]),
                Paragraph("--", styles["small"]),
                Paragraph("--", styles["small"]),
            ]
        card_table = Table([card_cells], colWidths=[2.4 * inch, 2.4 * inch, 2.4 * inch])
        card_table.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("GRID", (0, 0), (-1, -1), 0.25, COLOR_BORDER),
                    ("LEFTPADDING", (0, 0), (-1, -1), 6),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]
            )
        )
        _draw_table(c, card_table, margin_left + CARD_PAD, cards_y + CARD_PAD, content_w - 2 * CARD_PAD, scenario_cards_h - 24)

        y_next = cards_y - gap

        # Key levels table
        key_y = y_next - key_levels_h
        _draw_card(c, margin_left, key_y, content_w, key_levels_h, "Key Levels", base_font)
        key_levels_rows = report_model.get("key_levels_display_rows_by_price") or report_model.get(
            "key_levels_display_rows"
        )
        if not isinstance(key_levels_rows, list):
            key_levels_rows = []
        has_stock_position = bool(report_model.get("has_stock_position", True))
        if has_stock_position:
            columns = [
                "Scenario",
                "Price",
                "Move %",
                "Stock PnL",
                "Option PnL",
                "Option ROI",
                "Net PnL",
                "Net ROI",
            ]
        else:
            columns = [
                "Scenario",
                "Price",
                "Move %",
                "Option PnL",
                "Option ROI",
                "Net PnL",
                "Net ROI",
            ]
        table_data = [columns]
        highlight_row = None
        for idx, row in enumerate(key_levels_rows[:10], start=1):
            if not isinstance(row, dict):
                continue
            scenario_label = row.get("Scenario") or row.get("scenario")
            if isinstance(scenario_label, str) and scenario_label.strip() == "Current Market Price":
                highlight_row = idx
            row_values = [
                _fmt_value(scenario_label),
                _fmt_value(row.get("Price", row.get("price", ""))),
                _fmt_value(row.get("Move %", row.get("move_pct", ""))),
            ]
            if has_stock_position:
                row_values.append(_fmt_value(row.get("Stock PnL", row.get("stock_pnl", ""))))
            row_values.extend(
                [
                    _fmt_value(row.get("Option PnL", row.get("option_pnl", ""))),
                    _fmt_value(row.get("Option ROI", row.get("option_roi", ""))),
                    _fmt_value(row.get("Net PnL", row.get("net_pnl", ""))),
                    _fmt_value(row.get("Net ROI", row.get("net_roi", ""))),
                ]
            )
            table_data.append(row_values)
        if len(table_data) == 1:
            table_data.append(["--"] * len(columns))
        key_table = Table(table_data, repeatRows=1)
        table_style = [
            ("BACKGROUND", (0, 0), (-1, 0), COLOR_TABLE_HEADER_BG),
            ("TEXTCOLOR", (0, 0), (-1, 0), COLOR_MUTED),
            ("GRID", (0, 0), (-1, -1), 0.25, COLOR_BORDER),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTNAME", (0, 1), (-1, -1), base_font),
            ("FONTSIZE", (0, 0), (-1, 0), FONT_TABLE_HEADER),
            ("FONTSIZE", (0, 1), (-1, -1), FONT_SMALL),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
        ]
        for row in range(1, len(table_data), 2):
            table_style.append(("BACKGROUND", (0, row), (-1, row), zebra))
        if highlight_row is not None:
            table_style.append(
                ("BACKGROUND", (0, highlight_row), (-1, highlight_row), COLOR_HIGHLIGHT)
            )
        key_table.setStyle(TableStyle(table_style))
        _draw_table(c, key_table, margin_left + CARD_PAD, key_y + CARD_PAD, content_w - 2 * CARD_PAD, key_levels_h - 22)

        _draw_footer(c, 2)

    c = pdf_canvas.Canvas(path, pagesize=letter, pageCompression=0)
    _page1(c)
    c.showPage()
    _page2(c)
    c.save()


def _metric_lookup(metrics_rows: list[dict], label: str) -> str:
    target = label.strip().lower()
    for row in metrics_rows:
        if not isinstance(row, dict):
            continue
        metric = str(row.get("metric", "")).strip().lower()
        if metric == target:
            value = row.get("combined")
            if value in (None, "", "--"):
                value = row.get("options")
            return _safe_text(value)
    return "--"


def _calc_rr_ratio(max_profit: str, max_loss: str) -> str:
    profit_val = _coerce_float(max_profit)
    loss_val = _coerce_float(max_loss)
    if profit_val is None or loss_val is None or abs(loss_val) < 1e-9:
        return "--"
    return f"{abs(profit_val / loss_val):.2f}x"


def _draw_header(
    canvas_obj,
    report_model: Dict[str, Any],
    logo_path: Optional[Path],
    layout: Dict[str, float],
    base_font: str,
    *,
    show_disclaimer: bool,
) -> None:
    header = report_model.get("header", {}) if isinstance(report_model, dict) else {}
    page_h = layout["page_h"]
    margin_x = layout["margin_x"]
    margin_top = layout["margin_top"]
    content_w = layout["content_w"]
    header_h = layout["header_h"]

    x = margin_x
    y = page_h - margin_top - header_h

    logo_w = 74
    logo_h = 20
    if logo_path and Image is not None:
        try:
            canvas_obj.drawImage(
                str(logo_path),
                x,
                y + header_h - logo_h,
                width=logo_w,
                height=logo_h,
                preserveAspectRatio=True,
                mask="auto",
            )
        except Exception:
            pass

    right_x = x + content_w
    canvas_obj.setFillColor(COLOR_MUTED)
    canvas_obj.setFont(base_font, 8)
    canvas_obj.drawRightString(
        right_x,
        y + header_h - 12,
        "Wealth Management Option Strategy",
    )
    canvas_obj.drawRightString(
        right_x,
        y + header_h - 24,
        _format_mmddyyyy(header.get("report_time")),
    )

    title_x = x + logo_w + 12
    title_y = y + header_h - 34
    canvas_obj.setFillColor(COLOR_ACCENT)
    canvas_obj.setFont("Helvetica-Bold", 14)
    canvas_obj.drawString(title_x, title_y, _safe_text(header.get("strategy_name")))

    if show_disclaimer:
        _draw_wrapped_text(
            canvas_obj,
            HEADER_DISCLAIMER,
            title_x,
            y + 4,
            content_w - (title_x - x),
            header_h - 40,
            base_font,
            7.5,
            9,
            color=COLOR_MUTED,
        )

    canvas_obj.setStrokeColor(COLOR_BORDER)
    canvas_obj.setLineWidth(0.6)
    canvas_obj.line(x, y, x + content_w, y)


def _draw_footer(canvas_obj, layout: Dict[str, float], page_num: int, base_font: str) -> None:
    margin_x = layout["margin_x"]
    margin_bottom = layout["margin_bottom"]
    page_w = layout["page_w"]
    canvas_obj.setFont(base_font, FONT_FOOTER)
    canvas_obj.setFillColor(COLOR_MUTED)
    canvas_obj.drawString(margin_x, margin_bottom, "UBS Financial Services Inc.")
    canvas_obj.drawRightString(
        page_w - margin_x,
        margin_bottom,
        f"PAGE {page_num} OF 2",
    )


def _draw_page1(
    canvas_obj,
    report_model: Dict[str, Any],
    logo_path: Optional[Path],
    layout: Dict[str, float],
    base_font: str,
) -> None:
    page_w = layout["page_w"]
    page_h = layout["page_h"]
    margin_x = layout["margin_x"]
    margin_top = layout["margin_top"]
    content_w = layout["content_w"]
    gap = layout["gap"]
    header_h = layout["header_h"]
    tile_h = layout["tile_h"]
    details_h = layout["details_h"]
    legs_h = layout["legs_h"]
    payoff_h = layout["payoff_h"]
    right_rail_w = layout["right_rail_w"]

    canvas_obj.setFillColor(COLOR_PAGE_BG)
    canvas_obj.rect(0, 0, page_w, page_h, stroke=0, fill=1)

    _draw_header(
        canvas_obj,
        report_model,
        logo_path,
        layout,
        base_font,
        show_disclaimer=True,
    )

    header = report_model.get("header", {}) if isinstance(report_model, dict) else {}
    stock_banner = report_model.get("stock_banner", {}) if isinstance(report_model, dict) else {}
    metrics_rows = (
        report_model.get("metrics", {}).get("rows", [])
        if isinstance(report_model, dict)
        else []
    )
    structure = report_model.get("structure", {}) if isinstance(report_model, dict) else {}
    legs_rows = structure.get("legs", []) if isinstance(structure, dict) else []
    scenario_cards = report_model.get("scenario_analysis_cards") if isinstance(report_model, dict) else []
    payoff_payload = report_model.get("payoff") if isinstance(report_model, dict) else {}

    def _draw_tile(x: float, y: float, w: float, h: float, title: str, lines: list[object]) -> None:
        _draw_card(
            canvas_obj,
            x,
            y,
            w,
            h,
            None,
            base_font,
            fill_color=COLOR_TILE_BG,
            border_color=COLOR_BORDER,
        )
        canvas_obj.setFillColor(COLOR_MUTED)
        canvas_obj.setFont("Helvetica-Bold", 7)
        canvas_obj.drawString(x + 6, y + h - 12, title)
        line_y = y + h - 24
        for entry in lines:
            if isinstance(entry, tuple):
                text, font_name, font_size, color = entry
            else:
                text = str(entry)
                font_name = base_font
                font_size = 7.5
                color = COLOR_TEXT
            if not text:
                continue
            canvas_obj.setFillColor(color)
            canvas_obj.setFont(font_name, font_size)
            canvas_obj.drawString(x + 6, line_y, text)
            line_y -= font_size + 2

    cursor = page_h - margin_top - header_h - gap
    tile_y = cursor - tile_h
    tile_w = (content_w - 3 * gap) / 4

    ticker = _safe_text(header.get("ticker"))
    last_price = _safe_text(header.get("last_price"))
    underlying_lines = [
        (f"{ticker} {last_price}", "Helvetica-Bold", 9.5, COLOR_TEXT),
        ("Change: 0.00%", base_font, 7.5, COLOR_MUTED),
        _safe_text(header.get("name")),
        _safe_text(header.get("sector")),
        f"Earnings: {_safe_text(header.get('earnings_date'))}",
    ]
    _draw_tile(
        margin_x,
        tile_y,
        tile_w,
        tile_h,
        "Underlying",
        underlying_lines,
    )

    analyst_lines = [
        f"UBS Rating: {_safe_text(header.get('ubs_rating'))}",
        f"Target: {_safe_text(header.get('target'))}",
        f"CIO Rating: {_safe_text(header.get('cio_rating'))}",
    ]
    _draw_tile(
        margin_x + (tile_w + gap),
        tile_y,
        tile_w,
        tile_h,
        "Analyst View",
        analyst_lines,
    )

    week_range = stock_banner.get("week_52_range") if isinstance(stock_banner, dict) else None
    if not week_range or week_range == "--":
        high = _safe_text(header.get("high_52w"))
        low = _safe_text(header.get("low_52w"))
        if "--" in (high, low):
            week_range = "--"
        else:
            week_range = f"{high} / {low}"
    key_data_lines = [
        f"52W High/Low: {week_range}",
        f"Dividend Yield: {_safe_text(header.get('dividend_yield'))}",
    ]
    _draw_tile(
        margin_x + 2 * (tile_w + gap),
        tile_y,
        tile_w,
        tile_h,
        "Key Data",
        key_data_lines,
    )

    shares_text = _safe_text(stock_banner.get("shares") if isinstance(stock_banner, dict) else None)
    avg_cost_text = _safe_text(stock_banner.get("avg_cost") if isinstance(stock_banner, dict) else None)
    shares_val = _coerce_float(shares_text)
    last_price_val = _coerce_float(header.get("last_price"))
    avg_cost_val = _coerce_float(avg_cost_text)
    market_value_text = "--"
    total_pnl_text = "--"
    if shares_val is not None and last_price_val is not None:
        market_value_text = _format_currency_symbol(shares_val * last_price_val)
    if shares_val is not None and last_price_val is not None and avg_cost_val is not None:
        total_pnl_text = _format_currency_symbol((last_price_val - avg_cost_val) * shares_val)
    client_lines = [
        f"Market Value: {market_value_text}",
        f"Total P&L: {total_pnl_text}",
        f"Shares: {shares_text}",
        f"Avg Cost: {avg_cost_text}",
    ]
    _draw_tile(
        margin_x + 3 * (tile_w + gap),
        tile_y,
        tile_w,
        tile_h,
        "Client Position",
        client_lines,
    )

    details_y = tile_y - gap - details_h
    _draw_card(
        canvas_obj,
        margin_x,
        details_y,
        content_w,
        details_h,
        "Option Strategy Details",
        base_font,
    )
    detail_text = ""
    if isinstance(scenario_cards, list) and len(scenario_cards) > 1:
        card = scenario_cards[1]
        if isinstance(card, dict):
            detail_text = card.get("body") or card.get("condition") or card.get("title") or ""
    if not detail_text:
        detail_text = "Scenario narrative unavailable for this strategy."
    _draw_wrapped_text(
        canvas_obj,
        detail_text,
        margin_x + CARD_PAD,
        details_y + CARD_PAD,
        content_w - 2 * CARD_PAD,
        details_h - 20,
        base_font,
        8,
        10,
        color=COLOR_TEXT,
    )

    legs_y = details_y - gap - legs_h
    _draw_card(
        canvas_obj,
        margin_x,
        legs_y,
        content_w,
        legs_h,
        "Option Legs",
        base_font,
    )

    def _action_from_side(side: object) -> str:
        text = str(side or "").strip().lower()
        if text in {"long", "buy", "bto"}:
            return "Buy"
        if text in {"short", "sell", "sto"}:
            return "Sell"
        if text:
            return text.title()
        return "--"

    legs_data = [["Action", "Expiration", "Strike", "Type", "Price", "Delta", "OTM %", "Premium"]]
    for leg in legs_rows[:4]:
        if not isinstance(leg, dict):
            continue
        action = _action_from_side(leg.get("side"))
        expiry = _safe_text(leg.get("expiry") or leg.get("Expiry"))
        strike = _safe_text(leg.get("strike"))
        leg_type = _safe_text(leg.get("type") or leg.get("kind"))
        price_text = _format_currency_plain(leg.get("premium"))
        qty_val = _coerce_float(leg.get("qty"))
        price_val = _coerce_float(leg.get("premium"))
        premium_total = None
        if qty_val is not None and price_val is not None:
            sign = -1.0 if action.lower() == "buy" else 1.0
            premium_total = price_val * qty_val * 100.0 * sign
        premium_text = _format_currency_plain(premium_total) if premium_total is not None else price_text
        legs_data.append(
            [
                action,
                expiry,
                strike,
                leg_type,
                price_text,
                "--",
                "--",
                premium_text,
            ]
        )
    if len(legs_data) == 1:
        legs_data.append(["--"] * 8)

    col_base = [0.9, 1.05, 0.9, 0.7, 0.7, 0.6, 0.6, 0.95]
    col_widths = [w * inch for w in col_base]
    col_total = sum(col_widths)
    table_w = content_w - 2 * CARD_PAD
    if col_total > 0:
        col_widths = [w * table_w / col_total for w in col_widths]
    legs_table = Table(legs_data, colWidths=col_widths)
    legs_style = [
        ("BACKGROUND", (0, 0), (-1, 0), COLOR_TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLOR_MUTED),
        ("GRID", (0, 0), (-1, -1), 0.25, COLOR_BORDER),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), base_font),
        ("FONTSIZE", (0, 0), (-1, 0), FONT_TABLE_HEADER),
        ("FONTSIZE", (0, 1), (-1, -1), FONT_SMALL),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("ALIGN", (2, 1), (-1, -1), "RIGHT"),
    ]
    for row in range(1, len(legs_data), 2):
        legs_style.append(("BACKGROUND", (0, row), (-1, row), colors.HexColor("#F9FAFB")))
    legs_table.setStyle(TableStyle(legs_style))
    _draw_table(
        canvas_obj,
        legs_table,
        margin_x + CARD_PAD,
        legs_y + CARD_PAD + 10,
        content_w - 2 * CARD_PAD,
        legs_h - 30,
    )

    net_premium = _safe_text(structure.get("net_premium_total") if isinstance(structure, dict) else None)
    canvas_obj.setFillColor(COLOR_TEXT)
    canvas_obj.setFont("Helvetica-Bold", 8)
    canvas_obj.drawRightString(
        margin_x + content_w - CARD_PAD,
        legs_y + 6,
        f"Net Premium: {net_premium}",
    )

    payoff_y = legs_y - gap - payoff_h
    payoff_w = content_w - right_rail_w - gap
    payoff_x = margin_x
    right_x = payoff_x + payoff_w + gap

    _draw_card(
        canvas_obj,
        payoff_x,
        payoff_y,
        payoff_w,
        payoff_h,
        "Payoff Diagram",
        base_font,
    )
    _draw_payoff_chart_vector(
        canvas_obj,
        (
            payoff_x + CARD_PAD,
            payoff_y + CARD_PAD,
            payoff_w - 2 * CARD_PAD,
            payoff_h - 24,
        ),
        payoff_payload if isinstance(payoff_payload, dict) else {},
        base_font,
    )

    rail_tile_h = (payoff_h - 3 * gap) / 4

    def _draw_rail_tile(index: int, title: str, rows: list[tuple[str, str]]) -> None:
        tile_y = payoff_y + payoff_h - (index + 1) * rail_tile_h - index * gap
        _draw_card(
            canvas_obj,
            right_x,
            tile_y,
            right_rail_w,
            rail_tile_h,
            None,
            base_font,
            fill_color=COLOR_TILE_BG,
            border_color=COLOR_BORDER,
        )
        canvas_obj.setFillColor(COLOR_MUTED)
        canvas_obj.setFont("Helvetica-Bold", 7.5)
        canvas_obj.drawString(right_x + 6, tile_y + rail_tile_h - 12, title)
        line_y = tile_y + rail_tile_h - 24
        for label, value in rows:
            canvas_obj.setFillColor(COLOR_TEXT)
            canvas_obj.setFont(base_font, 7)
            canvas_obj.drawString(right_x + 6, line_y, f"{label}: {value}")
            line_y -= 10

    max_profit = _metric_lookup(metrics_rows, "Max Profit")
    max_loss = _metric_lookup(metrics_rows, "Max Loss")
    rr_ratio = _calc_rr_ratio(max_profit, max_loss)
    _draw_rail_tile(
        0,
        "Risk & Reward",
        [
            ("Max Profit", max_profit),
            ("Max Loss", max_loss),
            ("R/R Ratio", rr_ratio),
        ],
    )

    _draw_rail_tile(
        1,
        "Return Metrics",
        [
            ("Max ROI", _metric_lookup(metrics_rows, "Max ROI")),
            ("Min ROI", _metric_lookup(metrics_rows, "Min ROI")),
        ],
    )

    _draw_rail_tile(
        2,
        "Capital",
        [
            ("Capital Basis", _metric_lookup(metrics_rows, "Capital Basis")),
            ("Net Cost", _metric_lookup(metrics_rows, "Cost/Credit")),
        ],
    )

    net_prem_share = _metric_lookup(metrics_rows, "Net Prem/Share")
    if net_prem_share == "--":
        net_prem_share = _safe_text(structure.get("net_premium_per_share"))
    _draw_rail_tile(
        3,
        "Premium",
        [
            ("Net Prem/Share", net_prem_share),
            ("Yield %", _metric_lookup(metrics_rows, "Net Prem % Spot")),
        ],
    )

    _draw_footer(canvas_obj, layout, 1, base_font)


def _draw_page2(
    canvas_obj,
    report_model: Dict[str, Any],
    logo_path: Optional[Path],
    layout: Dict[str, float],
    base_font: str,
) -> None:
    page_w = layout["page_w"]
    page_h = layout["page_h"]
    margin_x = layout["margin_x"]
    margin_top = layout["margin_top"]
    content_w = layout["content_w"]
    gap = layout["gap"]
    header_h = layout["header_h"]
    scenario_h = layout["scenario_h"]
    key_levels_h = layout["key_levels_h"]
    disclosures_h = layout["disclosures_h"]

    canvas_obj.setFillColor(COLOR_PAGE_BG)
    canvas_obj.rect(0, 0, page_w, page_h, stroke=0, fill=1)

    _draw_header(
        canvas_obj,
        report_model,
        logo_path,
        layout,
        base_font,
        show_disclaimer=False,
    )

    cursor = page_h - margin_top - header_h - gap
    cards_y = cursor - scenario_h
    _draw_card(
        canvas_obj,
        margin_x,
        cards_y,
        content_w,
        scenario_h,
        "Scenario Analysis",
        base_font,
    )

    cards = report_model.get("scenario_analysis_cards") if isinstance(report_model, dict) else []
    if not isinstance(cards, list):
        cards = []
    while len(cards) < 3:
        cards.append({"title": "--", "condition": "--", "body": "--"})

    inner_x = margin_x + CARD_PAD
    title_offset = 14
    inner_y = cards_y + CARD_PAD
    inner_w = content_w - 2 * CARD_PAD
    inner_h = scenario_h - 2 * CARD_PAD - title_offset
    card_w = (inner_w - 2 * gap) / 3

    for idx, card in enumerate(cards[:3]):
        card_x = inner_x + idx * (card_w + gap)
        card_y = inner_y
        _draw_card(
            canvas_obj,
            card_x,
            card_y,
            card_w,
            inner_h,
            None,
            base_font,
            fill_color=COLOR_TILE_BG,
            border_color=COLOR_BORDER,
        )
        title = _safe_text(card.get("title")) if isinstance(card, dict) else "--"
        condition = _safe_text(card.get("condition")) if isinstance(card, dict) else "--"
        body = _safe_text(card.get("body")) if isinstance(card, dict) else "--"
        canvas_obj.setFillColor(COLOR_TEXT)
        canvas_obj.setFont("Helvetica-Bold", 8)
        canvas_obj.drawString(card_x + 6, card_y + inner_h - 14, title)
        canvas_obj.setFillColor(COLOR_MUTED)
        canvas_obj.setFont(base_font, 7)
        canvas_obj.drawString(card_x + 6, card_y + inner_h - 26, condition)
        _draw_wrapped_text(
            canvas_obj,
            body,
            card_x + 6,
            card_y + 6,
            card_w - 12,
            inner_h - 36,
            base_font,
            7,
            9,
            color=COLOR_TEXT,
        )

    key_y = cards_y - gap - key_levels_h
    _draw_card(
        canvas_obj,
        margin_x,
        key_y,
        content_w,
        key_levels_h,
        "Option Strategy Key Levels",
        base_font,
    )

    key_rows = report_model.get("key_levels_display_rows_by_price") if isinstance(report_model, dict) else None
    if not isinstance(key_rows, list):
        key_rows = report_model.get("key_levels_display_rows") if isinstance(report_model, dict) else []
    if not isinstance(key_rows, list):
        key_rows = []
    has_stock_position = bool(report_model.get("has_stock_position", False)) if isinstance(report_model, dict) else False

    if has_stock_position:
        columns = ["Scenario", "Price", "Move %", "Stock PnL", "Option PnL", "Net PnL", "Net ROI"]
    else:
        columns = ["Scenario", "Price", "Move %", "Option PnL", "Net PnL", "Net ROI"]
    table_data = [columns]
    highlight_row = None
    for idx, row in enumerate(key_rows[:10], start=1):
        if not isinstance(row, dict):
            continue
        scenario_label = _safe_text(row.get("Scenario") or row.get("scenario"))
        if scenario_label.strip().lower() == "current market price":
            highlight_row = idx
        row_values = [
            scenario_label,
            _safe_text(row.get("Price")),
            _safe_text(row.get("Move %")),
        ]
        if has_stock_position:
            row_values.append(_safe_text(row.get("Stock PnL")))
        row_values.extend(
            [
                _safe_text(row.get("Option PnL")),
                _safe_text(row.get("Net PnL")),
                _safe_text(row.get("Net ROI")),
            ]
        )
        table_data.append(row_values)
    if len(table_data) == 1:
        table_data.append(["--"] * len(columns))

    col_base = [1.6, 0.8, 0.7, 0.9, 0.9, 0.9, 0.8] if has_stock_position else [1.8, 0.8, 0.7, 0.9, 0.9, 0.8]
    col_widths = [w * inch for w in col_base]
    col_total = sum(col_widths)
    table_w = content_w - 2 * CARD_PAD
    if col_total > 0:
        col_widths = [w * table_w / col_total for w in col_widths]

    key_table = Table(table_data, colWidths=col_widths, repeatRows=1)
    key_style = [
        ("BACKGROUND", (0, 0), (-1, 0), COLOR_TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLOR_MUTED),
        ("GRID", (0, 0), (-1, -1), 0.25, COLOR_BORDER),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), base_font),
        ("FONTSIZE", (0, 0), (-1, 0), FONT_TABLE_HEADER),
        ("FONTSIZE", (0, 1), (-1, -1), FONT_SMALL),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
    ]
    for row in range(1, len(table_data), 2):
        key_style.append(("BACKGROUND", (0, row), (-1, row), colors.HexColor("#F9FAFB")))
    if highlight_row is not None:
        key_style.append(("BACKGROUND", (0, highlight_row), (-1, highlight_row), COLOR_HIGHLIGHT))
    key_table.setStyle(TableStyle(key_style))
    _draw_table(
        canvas_obj,
        key_table,
        margin_x + CARD_PAD,
        key_y + CARD_PAD,
        content_w - 2 * CARD_PAD,
        key_levels_h - 22,
    )

    disclosures_y = key_y - gap - disclosures_h
    _draw_card(
        canvas_obj,
        margin_x,
        disclosures_y,
        content_w,
        disclosures_h,
        "Risk Disclosures",
        base_font,
    )
    _draw_wrapped_text(
        canvas_obj,
        RISK_DISCLOSURE,
        margin_x + CARD_PAD,
        disclosures_y + CARD_PAD,
        content_w - 2 * CARD_PAD,
        disclosures_h - 20,
        base_font,
        7.5,
        9,
        color=COLOR_TEXT,
    )

    _draw_footer(canvas_obj, layout, 2, base_font)


def build_report_pdf_v2(
    path: str,
    *,
    report_model: Dict[str, Any],
    logo_path: Optional[str] = None,
) -> None:
    if _REPORTLAB_ERROR is not None:
        raise RuntimeError(
            "reportlab is required to build PDF reports. Install reportlab to continue."
        ) from _REPORTLAB_ERROR

    base_font = "Helvetica"

    if pdf_canvas is None:
        raise RuntimeError("reportlab canvas unavailable")

    resolved_logo_path = None
    if logo_path:
        resolved_logo_path = Path(logo_path)
    else:
        repo_root = Path(__file__).resolve().parents[1]
        resolved_logo_path = repo_root / "Design" / "UBS Logo Png.png"
    if resolved_logo_path and not resolved_logo_path.exists():
        resolved_logo_path = None

    PAGE_W, PAGE_H = letter
    layout = {
        "page_w": PAGE_W,
        "page_h": PAGE_H,
        "margin_x": 24,
        "margin_top": 24,
        "margin_bottom": 18,
        "content_w": PAGE_W - 48,
        "gap": 8,
        "header_h": 90,
        "tile_h": 78,
        "details_h": 70,
        "legs_h": 135,
        "payoff_h": 240,
        "right_rail_w": 170,
        "scenario_h": 150,
        "key_levels_h": 300,
        "disclosures_h": 80,
    }

    canvas_obj = pdf_canvas.Canvas(path, pagesize=letter, pageCompression=0)
    _draw_page1(canvas_obj, report_model, resolved_logo_path, layout, base_font)
    canvas_obj.showPage()
    _draw_page2(canvas_obj, report_model, resolved_logo_path, layout, base_font)
    canvas_obj.save()
