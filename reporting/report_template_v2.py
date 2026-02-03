"""UBS Client Report v2 template spec (design tokens + layout grid)."""

from __future__ import annotations

from typing import Dict, Tuple

PAGE_W = 612.0
PAGE_H = 792.0

MARGIN_LEFT = 24.0
MARGIN_RIGHT = 24.0
MARGIN_TOP = 24.0
MARGIN_BOTTOM = 18.0

CONTENT_X = MARGIN_LEFT
CONTENT_W = PAGE_W - MARGIN_LEFT - MARGIN_RIGHT

GUTTER = 8.0

CARD_RADIUS = 5.0
CARD_PAD_X = 10.0
CARD_PAD_Y = 10.0

TILE_PAD_X = 6.0
TILE_PAD_Y = 6.0
TILE_LINE_GAP = 2.0

RAIL_LINE_GAP = 10.0

TITLE_RULE_HEIGHT = 1.0
TITLE_RULE_GAP = 6.0
TITLE_RULE_RATIO = 0.4

TITLE_OFFSET_X = 12.0
TITLE_OFFSET_X_EXTRA = 6.0
SCENARIO_CARD_TITLE_OFFSET = 14.0


TABLE_PAD_X = 3.0
TABLE_PAD_Y = 2.0
TABLE_PAD_X_TIGHT = 2.0
TABLE_PAD_Y_TIGHT = 1.5

PARAGRAPH_GAP = 2.0

LINE_THIN = 0.6
LINE_GRID = 0.25

TOTAL_PAGES = 2
TILE_COUNT = 4
RAIL_TILE_COUNT = 4
SCENARIO_CARD_COUNT = 3

# Color tokens (RGB 0-255)
UBS_RED = (230, 0, 0)
TEXT_PRIMARY = (17, 24, 39)
TEXT_MUTED = (107, 114, 128)
BORDER = (229, 231, 235)
CARD_FILL = (255, 255, 255)
PAGE_BG = (255, 255, 255)
HEADER_BG = (248, 250, 252)
TILE_FILL = (249, 250, 251)
TABLE_HEADER_FILL = (243, 244, 246)
ZEBRA_FILL = (249, 250, 251)
HIGHLIGHT_FILL = (254, 243, 199)

CHART_STOCK = (156, 163, 175)
CHART_OPTIONS = (37, 99, 235)
CHART_COMBINED = (17, 24, 39)

# Typography tokens
FONT_FAMILY = "Helvetica"
FONT_BOLD = "Helvetica-Bold"

TITLE_SIZE = 14.0
SUBTITLE_SIZE = 8.0
SECTION_TITLE_SIZE = 9.0
LABEL_SIZE = 7.0
BODY_SIZE = 8.0
TABLE_SIZE = 7.0
TABLE_SIZE_TIGHT = 6.5
FOOTER_SIZE = 8.0
DISCLAIMER_SIZE = 7.5
TILE_VALUE_SIZE = 9.5
TILE_MUTED_SIZE = 7.5
DISCLAIMER_LEADING = 9.0

TITLE_SPACING = 6.0
CARD_TITLE_SPACE = CARD_PAD_Y + SECTION_TITLE_SIZE + TITLE_SPACING
LEGS_FOOTER_SPACE = 12.0
TITLE_BASELINE_OFFSET = CARD_PAD_Y + SECTION_TITLE_SIZE
LEGS_FOOTER_BASELINE = LEGS_FOOTER_SPACE / 2.0

# Legacy style spacing
STYLE_TITLE_LEADING_EXTRA = 2.0
STYLE_SECTION_LEADING_EXTRA = 2.0
STYLE_BODY_LEADING_EXTRA = 3.0
STYLE_SPACE_AFTER_TITLE = 6.0
STYLE_SPACE_BEFORE_SECTION = 10.0
STYLE_SPACE_AFTER_SECTION = 5.0

SCENARIO_CONDITION_GAP = 12.0
SCENARIO_BODY_LEADING = 9.0
DETAILS_LEADING = BODY_SIZE + TITLE_SPACING

# Header spec
HEADER_H = 90.0
HEADER_LOGO_W = 74.0
HEADER_LOGO_H = 20.0
HEADER_RIGHT_TITLE_OFFSET = 12.0
HEADER_RIGHT_DATE_OFFSET = 24.0
HEADER_TITLE_OFFSET = 34.0
HEADER_DISCLAIMER_INSET_Y = 4.0
HEADER_DISCLAIMER_H = 32.0

# Page 1 section heights
TILE_H = 78.0
DETAILS_H = 70.0
LEGS_H = 135.0
PAYOFF_H = 240.0
RIGHT_RAIL_W = 170.0

# Page 2 section heights
SCENARIO_H = 150.0
KEY_LEVELS_H = 300.0
DISCLOSURES_H = 80.0

# Chart spec
CHART_BORDER_WIDTH = 0.5
CHART_ZERO_WIDTH = 0.5
CHART_STRIKE_WIDTH = 0.5
CHART_BREAKEVEN_WIDTH = 0.5
CHART_SPOT_WIDTH = 0.75
CHART_SERIES_WIDTH = 0.8
CHART_FONT_SIZE = 7.0
CHART_LEGEND_RIGHT_INSET = 70.0
CHART_LEGEND_TOP_INSET = 10.0
CHART_LEGEND_LINE_LEN = 12.0
CHART_LEGEND_LINE_GAP = 10.0
CHART_LEGEND_LABEL_GAP = 3.0
CHART_SPOT_LABEL_OFFSET_X = 2.0
CHART_SPOT_LABEL_TOP_INSET = 10.0

# Legacy v1 table widths (inches)
LEGACY_KEY_VALUE_COLS = (2.0, 4.5)
LEGACY_LEGS_COLS = (1.0, 1.0, 1.0, 1.0, 1.0)
LEGACY_SCENARIO_CARD_COLS = (2.4, 2.4, 2.4)
LEGACY_MARGIN = 36.0
LEGACY_SPACER_LARGE = 0.2
LEGACY_SPACER_SMALL = 0.1

# Table column widths (relative units)
LEGS_COL_UNITS = (0.9, 1.05, 0.9, 0.7, 0.7, 0.6, 0.6, 0.95)
KEY_LEVELS_COL_UNITS_WITH_STOCK = (1.6, 0.8, 0.7, 0.9, 0.9, 0.9, 0.8)
KEY_LEVELS_COL_UNITS_NO_STOCK = (1.8, 0.8, 0.7, 0.9, 0.9, 0.8)


def _box(x: float, y: float, w: float, h: float) -> Tuple[float, float, float, float]:
    return (float(x), float(y), float(w), float(h))


def _page1_boxes() -> Dict[str, Tuple[float, float, float, float]]:
    header_x = CONTENT_X
    header_y = PAGE_H - MARGIN_TOP - HEADER_H
    header_box = _box(header_x, header_y, CONTENT_W, HEADER_H)

    tile_y = header_y - GUTTER - TILE_H
    tile_w = (CONTENT_W - (TILE_COUNT - 1) * GUTTER) / TILE_COUNT

    details_y = tile_y - GUTTER - DETAILS_H
    legs_y = details_y - GUTTER - LEGS_H
    payoff_y = legs_y - GUTTER - PAYOFF_H

    payoff_w = CONTENT_W - RIGHT_RAIL_W - GUTTER
    rail_x = CONTENT_X + payoff_w + GUTTER
    rail_h = (PAYOFF_H - (RAIL_TILE_COUNT - 1) * GUTTER) / RAIL_TILE_COUNT

    boxes: Dict[str, Tuple[float, float, float, float]] = {
        "header": header_box,
        "tiles_row": _box(CONTENT_X, tile_y, CONTENT_W, TILE_H),
        "tile_underlying": _box(CONTENT_X, tile_y, tile_w, TILE_H),
        "tile_analyst": _box(CONTENT_X + (tile_w + GUTTER), tile_y, tile_w, TILE_H),
        "tile_key_data": _box(CONTENT_X + 2 * (tile_w + GUTTER), tile_y, tile_w, TILE_H),
        "tile_client": _box(CONTENT_X + 3 * (tile_w + GUTTER), tile_y, tile_w, TILE_H),
        "details": _box(CONTENT_X, details_y, CONTENT_W, DETAILS_H),
        "legs": _box(CONTENT_X, legs_y, CONTENT_W, LEGS_H),
        "payoff": _box(CONTENT_X, payoff_y, payoff_w, PAYOFF_H),
        "rail_0": _box(rail_x, payoff_y + PAYOFF_H - rail_h, RIGHT_RAIL_W, rail_h),
        "rail_1": _box(rail_x, payoff_y + PAYOFF_H - 2 * rail_h - GUTTER, RIGHT_RAIL_W, rail_h),
        "rail_2": _box(rail_x, payoff_y + PAYOFF_H - 3 * rail_h - 2 * GUTTER, RIGHT_RAIL_W, rail_h),
        "rail_3": _box(rail_x, payoff_y + PAYOFF_H - 4 * rail_h - 3 * GUTTER, RIGHT_RAIL_W, rail_h),
    }

    title_x = header_x + HEADER_LOGO_W + TITLE_OFFSET_X + TITLE_OFFSET_X_EXTRA
    title_y = header_y + HEADER_H - HEADER_TITLE_OFFSET
    disclaimer_w = CONTENT_W - (title_x - header_x)
    boxes.update(
        {
            "title_pos": _box(title_x, title_y, 0.0, 0.0),
            "title_rule": _box(title_x, title_y - TITLE_RULE_GAP, disclaimer_w * TITLE_RULE_RATIO, TITLE_RULE_HEIGHT),
            "disclaimer": _box(
                title_x,
                header_y + HEADER_DISCLAIMER_INSET_Y,
                disclaimer_w,
                HEADER_DISCLAIMER_H,
            ),
            "header_right_title": _box(
                header_x + CONTENT_W,
                header_y + HEADER_H - HEADER_RIGHT_TITLE_OFFSET,
                0.0,
                0.0,
            ),
            "header_right_date": _box(
                header_x + CONTENT_W,
                header_y + HEADER_H - HEADER_RIGHT_DATE_OFFSET,
                0.0,
                0.0,
            ),
            "logo": _box(
                header_x,
                header_y + HEADER_H - HEADER_LOGO_H,
                HEADER_LOGO_W,
                HEADER_LOGO_H,
            ),
            "footer_y": _box(0.0, MARGIN_BOTTOM, 0.0, 0.0),
        }
    )
    return boxes


def _page2_boxes() -> Dict[str, Tuple[float, float, float, float]]:
    header_x = CONTENT_X
    header_y = PAGE_H - MARGIN_TOP - HEADER_H
    header_box = _box(header_x, header_y, CONTENT_W, HEADER_H)

    scenario_y = header_y - GUTTER - SCENARIO_H
    key_y = scenario_y - GUTTER - KEY_LEVELS_H
    disclosures_y = key_y - GUTTER - DISCLOSURES_H

    inner_w = CONTENT_W - 2 * CARD_PAD_X
    card_w = (inner_w - 2 * GUTTER) / SCENARIO_CARD_COUNT
    card_h = SCENARIO_H - 2 * CARD_PAD_Y - SCENARIO_CARD_TITLE_OFFSET
    card_y = scenario_y + CARD_PAD_Y
    card_x = CONTENT_X + CARD_PAD_X

    boxes: Dict[str, Tuple[float, float, float, float]] = {
        "header": header_box,
        "scenario": _box(CONTENT_X, scenario_y, CONTENT_W, SCENARIO_H),
        "scenario_card_1": _box(card_x, card_y, card_w, card_h),
        "scenario_card_2": _box(card_x + (card_w + GUTTER), card_y, card_w, card_h),
        "scenario_card_3": _box(card_x + 2 * (card_w + GUTTER), card_y, card_w, card_h),
        "key_levels": _box(CONTENT_X, key_y, CONTENT_W, KEY_LEVELS_H),
        "disclosures": _box(CONTENT_X, disclosures_y, CONTENT_W, DISCLOSURES_H),
        "footer_y": _box(0.0, MARGIN_BOTTOM, 0.0, 0.0),
    }
    return boxes


PAGE1 = _page1_boxes()
PAGE2 = _page2_boxes()
for key in (
    "logo",
    "title_pos",
    "title_rule",
    "disclaimer",
    "header_right_title",
    "header_right_date",
):
    PAGE2[key] = PAGE1[key]
