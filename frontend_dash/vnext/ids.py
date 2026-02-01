"""ID constants for vNext Dash app (single source of truth)."""

# Router + layout
TABS = "vnext-tabs"
PAGE = "vnext-page"
CONTROL_PLANE = "control-plane"
PAGE_DASHBOARD = "page-dashboard"
PAGE_BLOOMBERG = "page-bloomberg"
PAGE_REPORT = "page-report"

# Stores
STORE_REF = "store-ref"
STORE_MARKET = "store-market"
STORE_ANALYSIS_KEY = "store-analysis-key"
STORE_INPUTS = "store-inputs"
STORE_UI = "store-ui"

# Market inputs
TICKER_INPUT = "ticker-input"
SPOT_STATUS = "spot-status"
SPOT_INPUT = "spot-input"
BTN_REFRESH = "refresh-button"
REFRESH_STATUS = "refresh-status"
EXPIRY_INPUT = "cp-expiry"

# Strategy selectors
STRATEGY_GROUP = "strategy-group"
STRATEGY_SUBGROUP = "strategy-subgroup"
STRATEGY_ID = "strategy-id"

# Stock overlay
STOCK_POSITION = "cp-stock-pos"
AVG_COST = "cp-avg-cost"

# Legs + pricing
LEGS_TABLE = "legs-table"
PRICING_MODE = "cp-pricing-mode"
ROI_POLICY = "cp-roi-policy"
VOL_MODE = "cp-vol-mode"
ATM_IV = "cp-atm-iv"

# Scenario + actions
SCENARIO_MODE = "cp-scenario-mode"
DOWNSIDE_TGT = "cp-downside"
UPSIDE_TGT = "cp-upside"
BTN_RUN = "run-analysis-button"

# Payoff + toggles
PAYOFF_CHART = "payoff-chart"
PNL_TOGGLES = "pnl-toggles"
ANNOTATE_TOGGLES = "annotate-toggles"

# Panels
RISK_BANNER = "risk-events-banner"
PANEL_PAYOFF_METRICS = "panel-payoff-metrics"
PANEL_MARGIN_CAPITAL = "panel-margin-capital"
PANEL_DIVIDEND = "panel-dividend"
PANEL_ELIGIBILITY = "panel-eligibility"
SCENARIO_CARDS = "scenario-cards"
PANEL_KEY_LEVELS = "panel-key-levels"

# Debug controls + panels
DEBUG_TOGGLE = "debug-mode-toggle"
DEBUG_CONTAINER = "debug-container"
BBG_MODE = "bbg-mode"
REF_DEBUG = "ref-debug"
MARKET_DEBUG = "market-debug"
REFRESH_DEBUG = "refresh-debug"
ANALYSIS_KEY_DEBUG = "analysis-key-debug"
ANALYSIS_PACK_DEBUG = "analysis-pack-debug"
ANALYSIS_RENDER_DEBUG = "analysis-render-debug"

# Bloomberg transparency
BBG_REQUEST_SUMMARY = "bbg-request-summary"
BBG_UNDERLYING_SUMMARY = "bbg-underlying-summary"
BBG_UNDERLYING_JSON = "bbg-underlying-json"
BBG_LEG_QUOTES = "bbg-leg-quotes"
BBG_ERRORS = "bbg-errors"
BTN_EXPORT_MARKET_JSON = "bbg-export-market-json"
DL_MARKET_JSON = "bbg-download-market-json"
