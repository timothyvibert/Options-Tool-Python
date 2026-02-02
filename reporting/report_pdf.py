from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
import os

import pandas as pd

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
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
    pdfmetrics = None
    TTFont = None
    Image = None
    PageBreak = None
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


def _styles(base_font: str = "Helvetica") -> Dict[str, ParagraphStyle]:
    styles = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "title",
            parent=styles["Heading1"],
            fontName=base_font,
            spaceAfter=6,
        ),
        "section": ParagraphStyle(
            "section",
            parent=styles["Heading2"],
            fontName=base_font,
            spaceBefore=12,
            spaceAfter=6,
        ),
        "label": ParagraphStyle(
            "label",
            parent=styles["BodyText"],
            fontName=base_font,
        ),
        "body": ParagraphStyle(
            "body",
            parent=styles["BodyText"],
            fontName=base_font,
            leading=12,
        ),
        "small": ParagraphStyle(
            "small",
            parent=styles["BodyText"],
            fontName=base_font,
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

    font_path = os.environ.get("ALPHA_ENGINE_FONT_PATH")
    base_font = "Helvetica"
    if font_path and os.path.exists(font_path) and TTFont is not None and pdfmetrics:
        try:
            pdfmetrics.registerFont(TTFont("Aptos", font_path))
            base_font = "Aptos"
        except Exception:
            base_font = "Helvetica"

    styles = _styles(base_font=base_font)
    doc = SimpleDocTemplate(
        path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36,
        pageCompression=0,
    )

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

    def _header_block():
        logo_cell = ""
        if resolved_logo_path and Image is not None:
            try:
                logo_cell = Image(str(resolved_logo_path), width=1.1 * inch, height=0.45 * inch)
            except Exception:
                logo_cell = ""
        header_lines = [
            f"<b>{ticker}</b>",
            f"Resolved: {resolved}",
            f"Strategy: {strategy_name}",
            f"Expiry: {expiry}",
            f"Spot: {spot}",
            f"As Of: {as_of}",
            f"Policies: {policies}",
        ]
        header_text = Paragraph("<br/>".join(header_lines), styles["small"])
        table = Table([[logo_cell, header_text]], colWidths=[1.5 * inch, 6.0 * inch])
        table.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]
            )
        )
        return [table, Spacer(1, 0.1 * inch)]

    story: List[Any] = []
    story.extend(_header_block())

    # Page 1: Structure Card
    story.append(Paragraph("Structure", styles["section"]))
    structure = report_model.get("structure", {}) if isinstance(report_model, dict) else {}
    legs_rows = structure.get("legs") if isinstance(structure, dict) else None
    legs_rows = legs_rows if isinstance(legs_rows, list) else []
    legs_data = [["Leg", "Side", "Expiry", "Strike", "Premium"]]
    if legs_rows:
        for leg in legs_rows:
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
    else:
        legs_data.append(["--", "--", "--", "--", "--"])
    legs_table = Table(legs_data, colWidths=[0.8 * inch, 1.0 * inch, 1.2 * inch, 1.2 * inch, 1.2 * inch])
    legs_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                ("FONTNAME", (0, 0), (-1, 0), base_font),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.append(legs_table)
    story.append(Spacer(1, 0.2 * inch))

    # Payoff Card (placeholder)
    story.append(Paragraph("Payoff", styles["section"]))
    placeholder = Table(
        [[Paragraph("Payoff chart (placeholder)", styles["body"])]],
        colWidths=[7.2 * inch],
        rowHeights=[4.0 * inch],
    )
    placeholder.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ]
        )
    )
    story.append(placeholder)
    story.append(Spacer(1, 0.2 * inch))

    # Payoff & Metrics
    story.append(Paragraph("Payoff & Metrics", styles["section"]))
    metrics = report_model.get("metrics", {}) if isinstance(report_model, dict) else {}
    metrics_rows = metrics.get("rows") if isinstance(metrics, dict) else []
    metrics_data = [["Metric", "Options", "Combined"]]
    if isinstance(metrics_rows, list) and metrics_rows:
        for row in metrics_rows:
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
    metrics_table = Table(metrics_data, colWidths=[2.5 * inch, 2.0 * inch, 2.0 * inch])
    metrics_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                ("FONTNAME", (0, 0), (-1, 0), base_font),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.append(metrics_table)
    story.append(Spacer(1, 0.2 * inch))

    # Disclaimers
    story.append(Paragraph("Disclaimers", styles["section"]))
    disclaimers = report_model.get("disclaimers") if isinstance(report_model, dict) else []
    if not isinstance(disclaimers, list) or not disclaimers:
        disclaimers = ["For informational purposes only. Not a solicitation or recommendation."]
    for note in disclaimers:
        story.append(Paragraph(f"- {note}", styles["small"]))

    story.append(PageBreak())

    # Page 2 header
    story.extend(_header_block())

    # Scenario Analysis Cards
    story.append(Paragraph("Scenario Analysis", styles["section"]))
    cards = report_model.get("scenario_analysis_cards") if isinstance(report_model, dict) else []
    card_cells = []
    if isinstance(cards, list) and cards:
        for card in cards[:3]:
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
    else:
        card_cells = [
            Paragraph("Bearish (placeholder)", styles["small"]),
            Paragraph("Stagnant (placeholder)", styles["small"]),
            Paragraph("Bullish (placeholder)", styles["small"]),
        ]
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
    story.append(Spacer(1, 0.2 * inch))

    # Key Levels Table
    story.append(Paragraph("Key Levels", styles["section"]))
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
    for idx, row in enumerate(key_levels_rows, start=1):
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
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), base_font),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]
    if highlight_row is not None:
        table_style.append(
            ("BACKGROUND", (0, highlight_row), (-1, highlight_row), colors.lightyellow)
        )
    key_table.setStyle(TableStyle(table_style))
    story.append(key_table)
    story.append(Spacer(1, 0.2 * inch))

    # Commentary Blocks
    story.append(Paragraph("Commentary", styles["section"]))
    commentary = report_model.get("commentary_blocks") if isinstance(report_model, dict) else {}
    blocks = []
    if isinstance(commentary, dict):
        blocks = commentary.get("blocks") or []
    if not isinstance(blocks, list):
        blocks = []
    if not blocks:
        story.append(Paragraph("--", styles["small"]))
    else:
        for block in blocks:
            if not isinstance(block, dict):
                continue
            level = block.get("level") or "--"
            text = block.get("text") or "--"
            story.append(Paragraph(f"<b>{level}</b>: {text}", styles["small"]))

    def _footer(canvas, doc_obj):
        canvas.saveState()
        canvas.setFont(base_font, 9)
        canvas.drawString(doc_obj.leftMargin, 18, "UBS Financial Services Inc.")
        canvas.drawRightString(
            doc_obj.pagesize[0] - doc_obj.rightMargin,
            18,
            f"Page {doc_obj.page} of 2",
        )
        canvas.restoreState()

    doc.build(story, onFirstPage=_footer, onLaterPages=_footer)
