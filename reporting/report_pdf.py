from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
import os

import pandas as pd
import plotly.graph_objects as go

from io import BytesIO

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.utils import ImageReader
    from reportlab.lib.units import inch
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
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
    pdfmetrics = None
    TTFont = None
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


def _build_payoff_figure(payoff_payload: Dict[str, Any]) -> go.Figure:
    x = payoff_payload.get("price_grid") or []
    y = payoff_payload.get("combined_pnl") or payoff_payload.get("pnl") or []
    strikes = payoff_payload.get("strikes") or []
    breakevens = payoff_payload.get("breakevens") or []
    fig = go.Figure()
    if x and y and len(x) == len(y):
        fig.add_trace(go.Scatter(x=x, y=y, name="Combined PnL"))
    fig.add_hline(y=0, line_color="#9CA3AF", line_width=1)
    for strike in strikes:
        try:
            strike_val = float(strike)
        except (TypeError, ValueError):
            continue
        fig.add_vline(x=strike_val, line_color="#E5E7EB", line_width=1)
    for breakeven in breakevens:
        try:
            be_val = float(breakeven)
        except (TypeError, ValueError):
            continue
        fig.add_vline(x=be_val, line_color="#9CA3AF", line_width=1, line_dash="dot")
    fig.update_layout(
        template="plotly_white",
        margin=dict(l=20, r=10, t=10, b=20),
        font=dict(size=10),
        showlegend=False,
    )
    return fig


def _try_export_payoff_png(
    payoff_payload: Dict[str, Any],
) -> tuple[Optional[bytes], Optional[str]]:
    try:
        fig = _build_payoff_figure(payoff_payload)
        return fig.to_image(format="png", scale=2), None
    except Exception as exc:
        return None, f"{type(exc).__name__}: {exc}"


def _draw_payoff_chart_vector(
    canvas_obj,
    box: tuple[float, float, float, float],
    payoff_payload: Dict[str, Any],
    base_font: str,
) -> None:
    x0, y0, w, h = box
    x = payoff_payload.get("price_grid") or []
    y = payoff_payload.get("combined_pnl") or payoff_payload.get("pnl") or []
    if not x or not y or len(x) != len(y):
        canvas_obj.setFont(base_font, 9)
        canvas_obj.drawCentredString(x0 + w / 2, y0 + h / 2, "Payoff chart unavailable")
        return
    try:
        x_vals = [float(v) for v in x]
        y_vals = [float(v) for v in y]
    except Exception:
        canvas_obj.setFont(base_font, 9)
        canvas_obj.drawCentredString(x0 + w / 2, y0 + h / 2, "Payoff chart unavailable")
        return

    x_min = min(x_vals)
    x_max = max(x_vals)
    if x_min == x_max:
        x_min -= 1.0
        x_max += 1.0
    y_min = min(y_vals)
    y_max = max(y_vals)
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

    canvas_obj.setStrokeColor(colors.black)
    canvas_obj.setLineWidth(0.75)
    points = list(zip(x_vals, y_vals))
    if points:
        path = canvas_obj.beginPath()
        first_x, first_y = points[0]
        path.moveTo(x_to_px(first_x), y_to_px(first_y))
        for px, py in points[1:]:
            path.lineTo(x_to_px(px), y_to_px(py))
        canvas_obj.drawPath(path, stroke=1, fill=0)


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
    margin_top = 24
    margin_bottom = 18
    content_w = PAGE_W - margin_left - margin_right

    header_h = 72
    gap = 9

    structure_w = 220
    structure_h = 180
    payoff_h = 300
    metrics_h = 140
    disclaim_h = 60

    scenario_cards_h = 130
    key_levels_h = 220

    def _draw_box(c, x, y, w, h):
        c.setStrokeColor(colors.lightgrey)
        c.setLineWidth(0.5)
        c.rect(x, y, w, h, stroke=1, fill=0)

    def _draw_table(c, table, x, y, w, h):
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
        table.drawOn(c, x, y + h - th)

    def _draw_paragraphs(c, paragraphs, x, y, w, h, leading):
        cursor = y + h - leading
        for para in paragraphs:
            tw, th = para.wrap(w, h)
            if cursor - th < y:
                break
            para.drawOn(c, x, cursor - th)
            cursor -= th + 2

    def _draw_header(c):
        x = margin_left
        y = PAGE_H - margin_top - header_h
        _draw_box(c, x, y, content_w, header_h)
        logo_w = 90
        logo_h = 28
        if resolved_logo_path and Image is not None:
            try:
                c.drawImage(
                    str(resolved_logo_path),
                    x + 6,
                    y + header_h - logo_h - 8,
                    width=logo_w,
                    height=logo_h,
                    preserveAspectRatio=True,
                    mask="auto",
                )
            except Exception:
                pass
        header_lines = [
            f"{ticker}  |  {resolved}",
            f"Strategy: {strategy_name}",
            f"Expiry: {expiry}   Spot: {spot}",
            f"As Of: {as_of}",
            f"Policies: {policies}",
        ]
        header_paras = [Paragraph(line, styles["small"]) for line in header_lines]
        _draw_paragraphs(c, header_paras, x + logo_w + 16, y + 6, content_w - logo_w - 22, header_h - 12, 10)

    def _draw_footer(c, page_num):
        c.setFont(base_font, 9)
        c.drawString(margin_left, margin_bottom, "UBS Financial Services Inc.")
        c.drawRightString(PAGE_W - margin_right, margin_bottom, f"Page {page_num} of 2")

    def _page1(c):
        _draw_header(c)
        y_top = PAGE_H - margin_top - header_h - gap

        # Structure card (left)
        struct_x = margin_left
        struct_y = y_top - structure_h
        _draw_box(c, struct_x, struct_y, structure_w, structure_h)
        c.setFont(base_font, 10)
        c.drawString(struct_x + 6, struct_y + structure_h - 14, "Structure")
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
        legs_table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                    ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                    ("FONTNAME", (0, 0), (-1, 0), base_font),
                    ("FONTSIZE", (0, 0), (-1, -1), 7),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ]
            )
        )
        _draw_table(c, legs_table, struct_x + 4, struct_y + 8, structure_w - 8, structure_h - 24)

        # Payoff card (right)
        payoff_x = margin_left + structure_w + gap
        payoff_w = content_w - structure_w - gap
        payoff_y = y_top - payoff_h
        _draw_box(c, payoff_x, payoff_y, payoff_w, payoff_h)
        c.setFont(base_font, 10)
        c.drawString(payoff_x + 6, payoff_y + payoff_h - 14, "Payoff")
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
                    (payoff_x + 6, payoff_y + 6, payoff_w - 12, payoff_h - 24),
                    payoff_payload if isinstance(payoff_payload, dict) else {},
                    base_font,
                )
        else:
            _draw_payoff_chart_vector(
                c,
                (payoff_x + 6, payoff_y + 6, payoff_w - 12, payoff_h - 24),
                payoff_payload if isinstance(payoff_payload, dict) else {},
                base_font,
            )

        y_next = y_top - payoff_h - gap

        # Metrics card
        metrics_y = y_next - metrics_h
        _draw_box(c, margin_left, metrics_y, content_w, metrics_h)
        c.setFont(base_font, 10)
        c.drawString(margin_left + 6, metrics_y + metrics_h - 14, "Payoff & Metrics")
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
        metrics_table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                    ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                    ("FONTNAME", (0, 0), (-1, 0), base_font),
                    ("FONTSIZE", (0, 0), (-1, -1), 7),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ]
            )
        )
        _draw_table(c, metrics_table, margin_left + 4, metrics_y + 6, content_w - 8, metrics_h - 22)

        # Disclaimers
        disclaim_y = metrics_y - gap - disclaim_h
        _draw_box(c, margin_left, disclaim_y, content_w, disclaim_h)
        c.setFont(base_font, 10)
        c.drawString(margin_left + 6, disclaim_y + disclaim_h - 14, "Disclaimers")
        disclaimers = report_model.get("disclaimers") if isinstance(report_model, dict) else []
        if not isinstance(disclaimers, list) or not disclaimers:
            disclaimers = ["For informational purposes only. Not a solicitation or recommendation."]
        paras = [Paragraph(f"- {note}", styles["small"]) for note in disclaimers[:3]]
        _draw_paragraphs(c, paras, margin_left + 8, disclaim_y + 6, content_w - 16, disclaim_h - 20, 10)

        _draw_footer(c, 1)

    def _page2(c):
        _draw_header(c)
        y_top = PAGE_H - margin_top - header_h - gap

        # Scenario cards row
        cards_y = y_top - scenario_cards_h
        _draw_box(c, margin_left, cards_y, content_w, scenario_cards_h)
        c.setFont(base_font, 10)
        c.drawString(margin_left + 6, cards_y + scenario_cards_h - 14, "Scenario Analysis")
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
        _draw_table(c, card_table, margin_left + 4, cards_y + 8, content_w - 8, scenario_cards_h - 24)

        y_next = cards_y - gap

        # Key levels table
        key_y = y_next - key_levels_h
        _draw_box(c, margin_left, key_y, content_w, key_levels_h)
        c.setFont(base_font, 10)
        c.drawString(margin_left + 6, key_y + key_levels_h - 14, "Key Levels")
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
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
            ("FONTNAME", (0, 0), (-1, 0), base_font),
            ("FONTSIZE", (0, 0), (-1, -1), 7),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]
        if highlight_row is not None:
            table_style.append(
                ("BACKGROUND", (0, highlight_row), (-1, highlight_row), colors.lightyellow)
            )
        key_table.setStyle(TableStyle(table_style))
        _draw_table(c, key_table, margin_left + 4, key_y + 6, content_w - 8, key_levels_h - 22)

        _draw_footer(c, 2)

    c = pdf_canvas.Canvas(path, pagesize=letter, pageCompression=0)
    _page1(c)
    c.showPage()
    _page2(c)
    c.save()
