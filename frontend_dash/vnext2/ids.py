"""Component IDs for v2 DMC layout (all prefixed v2-)."""

# ─── Stores ───────────────────────────────────────────────
STORE_REF = "v2-store-ref"
STORE_MARKET = "v2-store-market"
STORE_ANALYSIS_KEY = "v2-store-analysis-key"
STORE_UI = "v2-store-ui"
STORE_INPUTS = "v2-store-inputs"

# ─── Market inputs ────────────────────────────────────────
TICKER_INPUT = "v2-ticker-input"
SPOT_DISPLAY = "v2-spot-display"
EXPIRY_SELECT = "v2-expiry-select"

# ─── Strategy inputs ─────────────────────────────────────
GROUP_SELECT = "v2-group-select"
SUBGROUP_SELECT = "v2-subgroup-select"
STRATEGY_SELECT = "v2-strategy-select"
STRATEGY_CLEAR = "v2-strategy-clear"

# ─── Stock overlay ────────────────────────────────────────
SHARES_INPUT = "v2-shares-input"
AVG_COST_INPUT = "v2-avg-cost-input"

# ─── Output & Tracking ─────────────────────────────────────
FA_NAME_INPUT = "v2-fa-name-input"
ACCT_NUMBER_INPUT = "v2-acct-number-input"
FA_ID_INPUT = "v2-fa-id-input"

# ─── Action buttons ───────────────────────────────────────
BTN_REFRESH = "v2-btn-refresh"
BTN_ANALYZE = "v2-btn-analyze"
BTN_PDF = "v2-btn-pdf"
BTN_CLEAR = "v2-btn-clear"

# ─── Legs table ──────────────────────────────────────────
LEGS_TABLE = "v2-legs-table"

# ─── Pricing ─────────────────────────────────────────────
PRICING_MODE = "v2-pricing-mode"
PAY_COLLECT = "v2-pay-collect"
PREMIUM_MODE = "v2-premium-mode"
VOL_MODE = "v2-vol-mode"
VOL_INPUT = "v2-vol-input"

# ─── Scenario ────────────────────────────────────────────
SCENARIO_MODE = "v2-scenario-mode"
SCENARIO_SELECT = "v2-scenario-select"
DOWNSIDE_TARGET = "v2-downside-target"
UPSIDE_TARGET = "v2-upside-target"

# ─── Payoff chart trace toggles ─────────────────────────
CHK_OPTIONS = "v2-chk-options-pnl"
CHK_STOCK = "v2-chk-stock-pnl"
CHK_COMBINED = "v2-chk-combined-pnl"
CHK_BE_OPTIONS = "v2-chk-be-options"
CHK_BE_COMBINED = "v2-chk-be-combined"

# ─── Outputs ─────────────────────────────────────────────
PAYOFF_CHART = "v2-payoff-chart"
METRICS_TABLE = "v2-metrics-table"
SCENARIO_CARDS = "v2-scenario-cards"
KEY_LEVELS_TABLE = "v2-key-levels-table"
MARGIN_CARD = "v2-margin-card"
DIVIDEND_CARD = "v2-dividend-card"
ELIGIBILITY_TABLE = "v2-eligibility-table"
RISK_BANNER = "v2-risk-banner"

# ── Margin Calculator ──────────────────────────────────────
MARGIN_MODE_SELECT     = "v2-margin-mode-select"
MARGIN_FULL_TABLE      = "v2-margin-full-table"
MARGIN_CLASSIFICATION  = "v2-margin-classification"
HOUSE_INTRADAY_SECTION = "v2-house-intraday-section"

# House Intraday Check inputs
HOUSE_HOUSECALL        = "v2-house-housecall"
HOUSE_SMA              = "v2-house-sma"
HOUSE_TODAYS_CHANGE    = "v2-house-todays-change"
HOUSE_NEW_CASH         = "v2-house-new-cash"

# House Intraday Check outputs
HOUSE_INTRADAY_TABLE   = "v2-house-intraday-table"

# ─── Theme ────────────────────────────────────────────────
THEME_TOGGLE = "v2-theme-toggle"
MANTINE_PROVIDER = "v2-mantine-provider"

# ─── Tabs ─────────────────────────────────────────────────
TABS = "v2-tabs"

# ─── CIO ──────────────────────────────────────────────────
CIO_RATING_INPUT = "v2-cio-rating-input"

# ─── Downloads ───────────────────────────────────────────
DL_REPORT_PDF = "v2-dl-report-pdf"
DL_MARKET_JSON = "v2-dl-market-json"

# ─── Excel Template ─────────────────────────────────────
EXCEL_TEMPLATE_SELECT = "v2-excel-template-select"
BTN_EXCEL_PDF = "v2-btn-excel-pdf"
DL_EXCEL_PDF = "v2-dl-excel-pdf"
EXCEL_STATUS = "v2-excel-status"

# ─── Status displays ────────────────────────────────────
SPOT_STATUS = "v2-spot-status"

# ─── Stock info stats ─────────────────────────────────
STOCK_INFO_ROW = "v2-stock-info-row"
STAT_YTD = "v2-stat-ytd"
STAT_52WK_LOW = "v2-stat-52wk-low"
STAT_52WK_HIGH = "v2-stat-52wk-high"
STAT_3M_IV = "v2-stat-3m-iv"
REFRESH_STATUS = "v2-refresh-status"
REPORT_STATUS = "v2-report-status"

# ─── Bloomberg tab ──────────────────────────────────────
BBG_REQUEST_SUMMARY = "v2-bbg-request-summary"
BBG_UNDERLYING_SUMMARY = "v2-bbg-underlying-summary"
BBG_UNDERLYING_JSON = "v2-bbg-underlying-json"
BBG_LEG_QUOTES = "v2-bbg-leg-quotes"
BBG_ERRORS = "v2-bbg-errors"
BBG_DEBUG_TOGGLE = "v2-bbg-debug-toggle"

# ─── Report tab ─────────────────────────────────────────
REPORT_PREVIEW = "v2-report-preview"

# ─── Shutdown ──────────────────────────────────────────────
BTN_SHUTDOWN      = "v2-btn-shutdown"
SHUTDOWN_CONFIRM  = "v2-shutdown-confirm"
SHUTDOWN_YES      = "v2-shutdown-yes"
SHUTDOWN_CANCEL   = "v2-shutdown-cancel"

# ─── Activity Log tab ─────────────────────────────────────
LOG_TABLE         = "v2-log-table"
LOG_STORE         = "v2-log-store"
BTN_DOWNLOAD_CSV  = "v2-btn-download-csv"
BTN_CLEAR_LOG     = "v2-btn-clear-log"
DL_ACTIVITY_CSV   = "v2-dl-activity-csv"
CLEAR_LOG_CONFIRM = "v2-clear-log-confirm"
LOG_SUMMARY       = "v2-log-summary"
CLEAR_LOG_CANCEL  = "v2-clear-log-cancel"
CLEAR_LOG_YES     = "v2-clear-log-yes"

# ─── Probability bar ─────────────────────────────────────
PROBABILITY_PANEL  = "v2-probability-panel"
PROB_POP           = "v2-prob-pop"
PROB_ASSIGN        = "v2-prob-assign"
PROB_25            = "v2-prob-25"
PROB_50            = "v2-prob-50"
PROB_100           = "v2-prob-100"
PROB_IV            = "v2-prob-iv"
