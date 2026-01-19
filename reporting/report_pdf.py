from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

import pandas as pd

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
    _REPORTLAB_ERROR = None
except ImportError as exc:
    colors = None
    letter = None
    ParagraphStyle = None
    getSampleStyleSheet = None
    inch = 72
    Paragraph = None
    SimpleDocTemplate = None
    Spacer = None
    Table = None
    TableStyle = None
    _REPORTLAB_ERROR = exc


def _fmt_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:,.4f}".rstrip("0").rstrip(".")
    return str(value)


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


def _styles() -> Dict[str, ParagraphStyle]:
    styles = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "title",
            parent=styles["Heading1"],
            spaceAfter=6,
        ),
        "section": ParagraphStyle(
            "section",
            parent=styles["Heading2"],
            spaceBefore=12,
            spaceAfter=6,
        ),
        "label": ParagraphStyle(
            "label",
            parent=styles["BodyText"],
        ),
        "body": ParagraphStyle(
            "body",
            parent=styles["BodyText"],
            leading=12,
        ),
        "small": ParagraphStyle(
            "small",
            parent=styles["BodyText"],
            fontSize=9,
            leading=11,
        ),
    }


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
    doc = SimpleDocTemplate(
        path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36,
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
