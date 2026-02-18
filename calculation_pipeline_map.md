# Calculation Pipeline Map

> **Generated**: 2026-02-17
> **Scope**: Every computed value in the Alpha Engine — where it's calculated, how it flows, and where it's displayed.
> **Read-only investigation** — no code was changed.

---

## Core Modules

| Module | Purpose | Key Entry Points | Outputs |
|--------|---------|-----------------|---------|
| `core/models.py` | Foundational data structures | `OptionLeg(kind, position, strike, premium, multiplier=100)`, `StrategyInput(spot, stock_position, avg_cost, legs)` | Frozen dataclasses used as input to all other modules |
| `core/payoff.py` | P&L across a price grid; breakeven detection; unlimited-exposure flags | `compute_payoff(strategy: StrategyInput) → dict` | `{price_grid, pnl, breakevens, unlimited_upside, unlimited_downside, unlimited_loss_upside}` |
| `core/pricing.py` | Selects option premium from bid/ask/mid based on position direction | `select_price(pos, bid, mid, ask, mode) → float` | Single float (selected premium) |
| `core/roi.py` | Capital basis and net premium | `compute_net_premium(input)`, `capital_basis(input, payoff, policy)`, `combined_capital_basis(input, option_basis)` | Net premium (float), capital basis (float) by policy (NET_PREMIUM / CASH_SECURED / RISK_MAX_LOSS / MARGIN_PROXY) |
| `core/margin.py` | CBOE & House margin requirements per FINRA rules; strategy classification | `classify_strategy(input) → str` (7 codes), `classify_strategy_refined(input, **kw) → str` (30 codes), `compute_margin_full(input, **kw) → dict`, `compute_margin_proxy(input, payoff) → float` | `{classification, classification_refined, cboe:{cash_initial, margin_initial, margin_maintenance}, house:{margin_initial, margin_maintenance}}` — each entry: `{amount, allowed, notes, requirement_text}` |
| `core/margin_map.py` | CBOE margin requirement text lookup from CSV | `lookup_requirement_text(strategy_code, account_type, stage) → str` | Human-readable requirement text string |
| `core/scenarios.py` | Scenario analysis tables — P&L at key price points | `build_scenario_points(input, payoff, mode) → list[float]`, `compute_scenario_table(input, points, payoff, roi_policy) → DataFrame` | DataFrame: `[price, option_pnl, stock_pnl, combined_pnl, margin_requirement, option_roi, net_roi, commentary, scenario]` |
| `core/advisory.py` | Legacy template-based scenario commentary (still used by scenario table) | `resolve_archetype(input, strategy_row)`, `compute_scenario_key(...)`, `select_template(...)`, `render_commentary(template, context)` | Archetype string, scenario key, rendered commentary text per scenario row |
| `core/probability.py` | Black-Scholes Greeks, PoP (numerical integration), assignment risk, target probabilities | `strategy_pop(input, payoff_fn, S0, r, q, sigma, t) → float`, `compute_all_probabilities(input, payoff_fn, legs, spot, r, q, sigma, t) → dict`, `bs_delta/gamma/theta/rho(...)` | `{pop, pop_pct, assignment_prob, assignment_prob_pct, prob_25/50/100_profit, iv_used, iv_used_pct, max_profit_ref}` |
| `core/eligibility.py` | Maps strategies to eligible account types | `determine_strategy_code(input, roi_policy) → str`, `get_account_eligibility(code) → DataFrame` | Eligibility code (LNG/NAK/CSPT/etc.); DataFrame: `[account_type, eligibility]` |
| `core/strategy_map.py` | Strategy metadata lookup from CSV | `load_strategy_map()`, `list_groups()`, `list_strategies(group)`, `get_strategy(id)`, `get_strategy_description(name)` | DataFrames/lists of strategy names, IDs, descriptions, groups |
| `core/commentary_v2.py` | Payoff-driven natural-language commentary — no templates | `build_commentary_v2(pack) → dict` | `{narrative_scenarios: [{kind, condition, body}×3], commentary_blocks: [{level, text}]}` |
| `core/analysis_pack.py` | **Orchestrator** — calls every module above, assembles the pack | `build_analysis_pack(strategy_input, strategy_meta, pricing_mode, roi_policy, vol_mode, atm_iv, underlying_profile, bbg_leg_snapshots, scenario_mode, downside_tgt, upside_tgt, risk_free_rate, treasury_label) → dict` | ~30-key dict described in full below |

---

## Analysis Pack Keys

The output of `build_analysis_pack()` — the single source of truth for the entire system.

| Pack Key | Data Type | Source Module | Description | Used By |
|----------|-----------|--------------|-------------|---------|
| `as_of` | `str` | Input (strategy_meta) | ISO date "YYYY-MM-DD" | Report header, PDF filename |
| **`underlying`** | `dict` | Input + Bloomberg profile | Underlying stock information (sub-keys below) | Dashboard (risk banner, stock stats), Report (header, stock details) |
| `underlying.ticker` | `str` | Input | User-entered ticker | Dashboard (SPOT_DISPLAY), Report |
| `underlying.resolved` | `str` | Input | Bloomberg-resolved ticker (e.g., "AAPL US Equity") | Report (header.ticker) |
| `underlying.spot` | `float` | Input (strategy_input.spot) | Current stock price | Chart x-axis scaling, all P&L calculations |
| `underlying.high_52week` / `low_52week` | `float\|None` | Bloomberg profile | 52-week high/low | Dashboard (STAT_52WK_HIGH/LOW), Report |
| `underlying.chg_pct_ytd` | `float\|None` | Bloomberg profile | Year-to-date % change | Dashboard (STAT_YTD), Report (move_pct) |
| `underlying.impvol_3m_atm` | `float\|None` | Bloomberg profile | 3-month ATM implied vol | Dashboard (STAT_3M_IV), ATM IV fallback |
| `underlying.ubs_rating` / `ubs_target` | `str\|None` / `float\|None` | Bloomberg profile | UBS analyst rating & price target | Report (analyst section) |
| `underlying.earnings_risk` | `dict` | Computed in analysis_pack | `{earnings_date, days_to_earnings, before_expiry}` | Dashboard (RISK_BANNER) |
| `underlying.dividend_risk` | `dict` | Computed in analysis_pack | `{ex_div_date, days_to_dividend, before_expiry, projected_dividend}` | Dashboard (DIVIDEND_CARD, RISK_BANNER), Report (warning) |
| `underlying.vol_percentile` | `float\|None` | Bloomberg profile | Volatility rank (0-100) | Report |
| `underlying.mov_avg_200d` | `float\|None` | Bloomberg profile | 200-day moving average | Report |
| `underlying.put_call_oi_ratio` / `put_call_vol_ratio` | `float\|None` | Bloomberg profile | Put/call open interest & volume ratios | Report |
| `underlying.realized_vol_3m` / `iv_rv_spread` | `float\|None` | Bloomberg profile | Realized vol & IV-RV spread | Report |
| `underlying.profile` | `dict` | Bloomberg | Full raw Bloomberg profile dict | Bloomberg tab (JSON dump) |
| **`strategy`** | `dict` | Input + strategy_map | Strategy metadata | Dashboard, Report |
| `strategy.group` / `subgroup` / `name` / `id` | `str` / `str` / `str` / `int` | strategy_map.csv | Strategy classification & name | PDF filename, activity log |
| `strategy.strategy_code` | `str` | eligibility.py | Eligibility code (LNG, NAK, CSPT, etc.) | Eligibility table |
| `strategy.expiry` | `date\|str` | Input | Option expiration date | Report, key levels |
| **`policies`** | `dict` | Input | Computation policy settings | Report (header.policies) |
| `policies.pricing_mode` | `str` | Input | "MID" or "DEALABLE" | Report |
| `policies.roi_policy` | `str` | Input | "NET_PREMIUM", "CASH_SECURED", etc. | ROI calculations |
| `policies.vol_mode` | `str` | Input | "ATM", "VEGA_WEIGHTED", "SURFACE_ATM" | Probability calculations |
| `policies.risk_free_rate` | `float` | Bloomberg (treasury) | e.g., 0.045 for 4.5% | Probability & treasury obligation |
| `policies.treasury_label` | `str` | Bloomberg | e.g., "3M T-Bill" | Report |
| `policies.auto_capital_basis` | `dict` | analysis_pack.py | `{mode, amount, label}` — auto-selected basis | Report |
| **`legs`** | `list[dict]` | Input + analysis_pack | Normalized option legs | Dashboard (legs table), Report (structure) |
| `legs[i].index` / `kind` / `side` / `ratio` / `strike` / `premium` | various | Input | Leg description (1-indexed) | Dashboard, Report |
| `legs[i].delta` / `gamma` / `theta` / `vega` / `rho` | `float\|None` | Bloomberg leg quotes | Greeks from market data | Report, Bloomberg tab |
| **`payoff`** | `dict` | payoff.py | Payoff analysis | Dashboard (chart), Report (chart) |
| `payoff.price_grid` | `list[float]` | payoff.py | 300+ prices from ~0 to 3×spot | Chart x-axis |
| `payoff.options_pnl` | `list[float]` | payoff.py | Options-only P&L at each grid point | Chart (blue line) |
| `payoff.stock_pnl` | `list[float]` | payoff.py | Stock-only P&L at each grid point | Chart (gray dashed) |
| `payoff.combined_pnl` | `list[float]` | payoff.py | Full position P&L (stock + options) | Chart (purple line) |
| `payoff.strikes` | `list[float]` | payoff.py | Sorted unique strike prices | Chart annotations (red K labels) |
| `payoff.breakevens` | `list[float]` | payoff.py | Prices where combined P&L crosses zero | Chart annotations (yellow/cyan BE labels) |
| **`summary`** | `dict` | analysis_pack.py | Formatted metrics table | Dashboard (METRICS_TABLE), Report (metrics) |
| `summary.rows` | `list[dict]` | analysis_pack.py | `[{metric, options, combined}]` — rows: Max Profit, Max Loss, Risk/Reward, Capital Basis, Max ROI, Min ROI, Cost/Credit, Notional Exposure, Net Prem/Share, Net Prem % Spot, PoP, Closest Breakeven, BE Distance %, Treasury Obligation/Interest/Return% | Dashboard (METRICS_TABLE), Report (17 metrics fields) |
| `summary.net_premium_total` | `str` | analysis_pack.py | "Credit $X" or "Debit $X" | Report (net_premium_total) |
| `summary.net_premium_total_value` | `float` | analysis_pack.py | Numeric net premium (negative = credit) | Report |
| `summary.net_premium_per_share` | `str` | analysis_pack.py | Formatted "$X" (options-only) | Report |
| **`margin`** | `dict` | margin.py | Margin requirements & strategy classification | Dashboard (MARGIN_FULL_TABLE, House Intraday) |
| `margin.classification` | `str` | margin.py | 7-code base classification (backward-compat) | Dashboard (MARGIN_CLASSIFICATION badge) |
| `margin.margin_proxy` | `float` | margin.py | CBOE Margin Initial simplified proxy | Capital basis (MARGIN_PROXY policy) |
| `margin.full` | `dict` | margin.py | All CBOE + House margin combos | Dashboard (MARGIN_FULL_TABLE) |
| `margin.full.classification_refined` | `str` | margin.py | 30-code refined classification | Dashboard (badge text) |
| `margin.full.cboe.cash_initial` | `dict` | margin.py | `{amount, allowed, notes, requirement_text}` | Dashboard (row 1) |
| `margin.full.cboe.margin_initial` / `margin_maintenance` | `dict` | margin.py | Same structure | Dashboard (rows 2-3) |
| `margin.full.house.margin_initial` / `margin_maintenance` | `dict` | margin.py | Same structure | Dashboard (House mode rows), House Intraday calc |
| **`probabilities`** | `dict` | probability.py | All probability metrics | Dashboard (PROB_* badges) |
| `probabilities.pop` / `pop_pct` | `float` / `str` | probability.py | Probability of profit (0-1) / "45.2%" | Dashboard (PROB_POP, color-coded) |
| `probabilities.assignment_prob` / `assignment_prob_pct` | `float` / `str` | probability.py | P(any short finishes ITM) | Dashboard (PROB_ASSIGN, inverse color) |
| `probabilities.prob_25/50/100_profit` / `*_pct` | `float\|None` / `str` | probability.py | P(PnL > 25/50/100% of max profit) | Dashboard (PROB_25/50/100, color-coded) |
| `probabilities.iv_used` / `iv_used_pct` | `float` / `str` | probability.py | Effective sigma used | Dashboard (PROB_IV) |
| `probabilities.iv_source` | `str` | analysis_pack.py | "vega_weighted" or "atm_fallback" | Debug info |
| **`scenario`** | `dict` | scenarios.py | Scenario analysis data | Dashboard (KEY_LEVELS_TABLE), Report (key_levels) |
| `scenario.df` | `DataFrame` | scenarios.py | Full scenario table (N rows) | Report |
| `scenario.top10` | `DataFrame` | scenarios.py | First 10 scenario rows | Report |
| `scenario.key_levels` | `list[dict]` | analysis_pack.py | `[{Scenario, Price, Move%, Stock PnL, Option PnL, Option ROI, Net PnL, Net ROI}]` — includes spot, strikes, breakevens, downside/upside, zero, infinity sentinels | Dashboard (KEY_LEVELS_TABLE), Report (key_levels section) |
| **`key_levels`** | `dict` | analysis_pack.py | Detailed key levels with metadata | Dashboard (#23), Report |
| `key_levels.meta` | `dict` | analysis_pack.py | `{as_of, expiry, spot, has_stock_position, shares, avg_cost}` | Report context |
| `key_levels.levels` | `list[dict]` | analysis_pack.py | `[{id, label, price, move_pct, stock_pnl, option_pnl, net_pnl, net_roi, source}]` — deduplicated | Dashboard (KEY_LEVELS_TABLE with 8 columns) |
| **`eligibility`** | `dict` | eligibility.py | Account eligibility info | Dashboard (ELIGIBILITY_TABLE) |
| `eligibility.strategy_code` | `str` | eligibility.py | Eligibility code | Display |
| `eligibility.table` | `DataFrame` | eligibility.py | `[account_type, eligibility]` | Dashboard (Allowed/Restricted/Not allowed) |
| **`commentary_v2`** | `list[dict]` | commentary_v2.py | 3 narrative scenarios | Dashboard (SCENARIO_CARDS), Report (scenario_analysis) |
| `commentary_v2[i].kind` | `str` | commentary_v2.py | "bearish" / "stagnant" / "bullish" | Card badge color (red/gray/green) |
| `commentary_v2[i].condition` | `str` | commentary_v2.py | "If AAPL falls below $150.00" | Card condition text |
| `commentary_v2[i].body` | `str` | commentary_v2.py | Multi-sentence mechanics + numbers narrative | Card body |
| **`commentary_blocks_v2`** | `list[dict]` | commentary_v2.py | Detail blocks by level | Report (commentary_blocks section) |
| `commentary_blocks_v2[i].level` | `str` | commentary_v2.py | "Spot" / "Strikes" / "Breakevens" / "Low" / "High" | Report |
| `commentary_blocks_v2[i].text` | `str` | commentary_v2.py | P&L at specific price level | Report |
| **`dividend_schedule`** | `dict\|None` | Callback layer (Bloomberg) | `{dividend_sum, dividend_count}` — injected post-pack | Bloomberg tab (underlying summary) |
| **`vol_surface`** | `dict` | Callback layer | `{atm_iv_at_expiry, source}` | IV source tracking |

---

## Dashboard Display

Every UI element that displays computed data and how it gets there.

### Row 1: Market & Stock Info Stats

| UI Element | Component ID | Pack Key Read | Formatting Applied | Final Display |
|-----------|-------------|---------------|-------------------|---------------|
| Spot price | `SPOT_DISPLAY` | `STORE_REF["spot"]` (not from pack) | `f"Spot: {float(spot):,.2f}"` | "Spot: 423.50" |
| YTD change | `STAT_YTD` | `STORE_MARKET["underlying_profile"]["chg_pct_ytd"]` | `f"{sign}{val:.1f}%"`, green if ≥0, red if <0 | "+12.3%" (green) |
| 52wk Low | `STAT_52WK_LOW` | `STORE_MARKET["underlying_profile"]["low_52week"]` | `f"${val:,.2f}"` | "$315.25" |
| 52wk High | `STAT_52WK_HIGH` | `STORE_MARKET["underlying_profile"]["high_52week"]` | `f"${val:,.2f}"` | "$475.80" |
| 3M IV | `STAT_3M_IV` | `STORE_MARKET["underlying_profile"]["impvol_3m_atm"]` | `f"{val:.1f}%"` | "22.5%" |

### Payoff Chart

| UI Element | Component ID | Pack Key Read | Formatting Applied | Final Display |
|-----------|-------------|---------------|-------------------|---------------|
| Stock PnL trace | `PAYOFF_CHART` | `pack["payoff"]["stock_pnl"]` | Gray dashed line, width 1.5 | Plotly Scatter |
| Options PnL trace | `PAYOFF_CHART` | `pack["payoff"]["options_pnl"]` | Blue solid line, width 2.5 | Plotly Scatter |
| Combined PnL trace | `PAYOFF_CHART` | `pack["payoff"]["combined_pnl"]` | Purple solid line, width 3 | Plotly Scatter |
| Strike annotations | `PAYOFF_CHART` | `pack["payoff"]["strikes"]` | Red dotted vline + `f"K ${s:,.0f}"` label, staggered if within 6% x-range | Red vertical lines |
| Options breakevens | `PAYOFF_CHART` | Recomputed from `options_pnl` | Cyan dashed vline + `f"OBE ${be:,.2f}"` | Cyan vertical lines |
| Combined breakevens | `PAYOFF_CHART` | `pack["payoff"]["breakevens"]` | Yellow dashed vline + `f"BE ${be:,.2f}"` | Yellow vertical lines |
| X-axis range | `PAYOFF_CHART` | `pack["underlying"]["spot"]` + strikes | spot ± strikes with 15% padding, min 10% spread, snapped to nice grid | Dynamic axis |
| Y-axis range | `PAYOFF_CHART` | Visible traces within x-range | ±10% padding, snapped to nice grid | Dynamic axis |

### Metrics Table

| UI Element | Component ID | Pack Key Read | Formatting Applied | Final Display |
|-----------|-------------|---------------|-------------------|---------------|
| Max Profit | `METRICS_TABLE` | `pack["summary"]["rows"][0]` | `_fmt_money_signed()` — green if positive, red if negative | "$5,000.00" (green) |
| Max Loss | `METRICS_TABLE` | `pack["summary"]["rows"][1]` | `_fmt_money_signed()` — green/red | "-$2,500.00" (red) |
| Capital Basis | `METRICS_TABLE` | `pack["summary"]["rows"][...]` | `_fmt_money()` — no color | "$3,200.00" |
| Max ROI / Min ROI | `METRICS_TABLE` | `pack["summary"]["rows"][...]` | `_fmt_percent_ratio()` — `f"{val*100:.1f}%"`, green/red | "156.3%" (green) |
| Cost/Credit | `METRICS_TABLE` | `pack["summary"]["rows"][...]` | Special: "Credit" → green text, "Debit" → red text | "Credit $1,250" (green) |
| Notional Exposure | `METRICS_TABLE` | `pack["summary"]["rows"][...]` | `_fmt_money()` | "$42,350.00" |
| Net Prem/Share | `METRICS_TABLE` | `pack["summary"]["rows"][...]` | `_fmt_money()` | "$12.50" |
| Net Prem % Spot | `METRICS_TABLE` | `pack["summary"]["rows"][...]` | Passthrough if "%" in text, else `_fmt_percent_point()` — no color | "2.9%" |

### Probability Panel

| UI Element | Component ID | Pack Key Read | Formatting Applied | Final Display |
|-----------|-------------|---------------|-------------------|---------------|
| PoP | `PROB_POP` | `pack["probabilities"]["pop"]` / `["pop_pct"]` | Color: green if >0.6, yellow if >0.4, red otherwise | "52.3%" (yellow) |
| Assignment | `PROB_ASSIGN` | `pack["probabilities"]["assignment_prob"]` / `["assignment_prob_pct"]` | **Inverse** color: red if >0.5, yellow if >0.3, green otherwise | "35.1%" (yellow) |
| Prob 25% | `PROB_25` | `pack["probabilities"]["prob_25_pct"]` | Same as PoP coloring | "60.3%" (green) |
| Prob 50% | `PROB_50` | `pack["probabilities"]["prob_50_pct"]` | Same as PoP coloring | "38.2%" (red) |
| Prob 100% | `PROB_100` | `pack["probabilities"]["prob_100_pct"]` | Same as PoP coloring | "15.7%" (red) |
| IV Used | `PROB_IV` | `pack["probabilities"]["iv_used_pct"]` | No coloring | "22.5%" |

### Scenario Commentary Cards

| UI Element | Component ID | Pack Key Read | Formatting Applied | Final Display |
|-----------|-------------|---------------|-------------------|---------------|
| Bearish card | `SCENARIO_CARDS` | `pack["commentary_v2"][kind="bearish"]` | Red badge, condition as dimmed subtext, body as text | Card with 3 sections |
| Stagnant card | `SCENARIO_CARDS` | `pack["commentary_v2"][kind="stagnant"]` | Gray badge | Card with 3 sections |
| Bullish card | `SCENARIO_CARDS` | `pack["commentary_v2"][kind="bullish"]` | Green badge | Card with 3 sections |

### Key Levels Table

| UI Element | Component ID | Pack Key Read | Formatting Applied | Final Display |
|-----------|-------------|---------------|-------------------|---------------|
| Label | `KEY_LEVELS_TABLE` | `pack["key_levels"]["levels"][i]["label"]` | Passthrough | "Current Market Price" |
| Price | `KEY_LEVELS_TABLE` | `pack["key_levels"]["levels"][i]["price"]` | `_fmt_money()` → `f"{val:,.2f}"` | "$423.50" |
| Move % | `KEY_LEVELS_TABLE` | `pack["key_levels"]["levels"][i]["move_pct"]` | `_fmt_percent_point()` → `f"{val:.1f}%"` | "-5.2%" |
| Stock PnL | `KEY_LEVELS_TABLE` | `pack["key_levels"]["levels"][i]["stock_pnl"]` | `_fmt_money_signed()` | "-$2,117.50" |
| Option PnL | `KEY_LEVELS_TABLE` | `pack["key_levels"]["levels"][i]["option_pnl"]` | `_fmt_money_signed()` | "+$3,500.00" |
| Net PnL | `KEY_LEVELS_TABLE` | `pack["key_levels"]["levels"][i]["net_pnl"]` | `_fmt_money_signed()` | "+$1,382.50" |
| Net ROI | `KEY_LEVELS_TABLE` | `pack["key_levels"]["levels"][i]["net_roi"]` | `_fmt_percent_ratio()` → `f"{val*100:.1f}%"` | "43.2%" |
| Source | `KEY_LEVELS_TABLE` | `pack["key_levels"]["levels"][i]["source"]` | Passthrough | "strike" |

### Margin & Capital Panel

| UI Element | Component ID | Pack Key Read | Formatting Applied | Final Display |
|-----------|-------------|---------------|-------------------|---------------|
| Classification badge | `MARGIN_CLASSIFICATION` | `pack["margin"]["full"]["classification_refined"]` | Badge text | "SPR" |
| CBOE Cash Initial | `MARGIN_FULL_TABLE` | `pack["margin"]["full"]["cboe"]["cash_initial"]` | `f"${amount:,.2f}"` or "N/A" | "$15,000.00" |
| CBOE Margin Initial | `MARGIN_FULL_TABLE` | `pack["margin"]["full"]["cboe"]["margin_initial"]` | Same | "$7,500.00" |
| CBOE Margin Maint | `MARGIN_FULL_TABLE` | `pack["margin"]["full"]["cboe"]["margin_maintenance"]` | Same | "$6,000.00" |
| House Margin Initial | `MARGIN_FULL_TABLE` | `pack["margin"]["full"]["house"]["margin_initial"]` | Same (shown in House mode) | "$7,500.00" |
| House Margin Maint | `MARGIN_FULL_TABLE` | `pack["margin"]["full"]["house"]["margin_maintenance"]` | Same (shown in House mode) | "$6,000.00" |
| House Intraday OK | `HOUSE_INTRADAY_TABLE` | `pack["margin"]["full"]["house"]["margin_initial"]["amount"]` | Compared to user-entered intraday values → "OK"/"Failed" badge | Green/Red badge |

### Risk Banner & Event Alerts

| UI Element | Component ID | Pack Key Read | Formatting Applied | Final Display |
|-----------|-------------|---------------|-------------------|---------------|
| Risk banner | `RISK_BANNER` | `pack["underlying"]["earnings_risk"]`, `pack["underlying"]["dividend_risk"]` | If `before_expiry=True`: `f"Earnings in {days}d"` / `f"Ex-div in {days}d"` joined by " \| " | Red badge "Earnings in 12d \| Ex-div in 5d" or green "No risk events" |

### Dividend Card

| UI Element | Component ID | Pack Key Read | Formatting Applied | Final Display |
|-----------|-------------|---------------|-------------------|---------------|
| Ex-div Date | `DIVIDEND_CARD` | `pack["underlying"]["dividend_risk"]["ex_div_date"]` | Passthrough | "2026-03-15" |
| Days to Dividend | `DIVIDEND_CARD` | `pack["underlying"]["dividend_risk"]["days_to_dividend"]` | Passthrough | "26" |
| Before Expiry | `DIVIDEND_CARD` | `pack["underlying"]["dividend_risk"]["before_expiry"]` | Passthrough | "True" |

### Eligibility Table

| UI Element | Component ID | Pack Key Read | Formatting Applied | Final Display |
|-----------|-------------|---------------|-------------------|---------------|
| Account Type | `ELIGIBILITY_TABLE` | `pack["eligibility"]["table"]` records | Column: `account_type` | "Cash", "Margin", "IRA" |
| Eligible | `ELIGIBILITY_TABLE` | `pack["eligibility"]["table"]` records | Column: `eligibility` → "Allowed" / "Restricted" / "Not allowed" | Text |

### Bloomberg Data Tab

| UI Element | Component ID | Pack Key Read | Formatting Applied | Final Display |
|-----------|-------------|---------------|-------------------|---------------|
| Underlying fields | `BBG_UNDERLYING_SUMMARY` | `STORE_MARKET["underlying_profile"]` + `pack["dividend_schedule"]` | `str(value)` or "--" | Table rows |
| Dividends to Expiry | `BBG_UNDERLYING_SUMMARY` | `pack["dividend_schedule"]["dividend_sum"]` | Passthrough | "$2.40" |
| # Div Payments | `BBG_UNDERLYING_SUMMARY` | `pack["dividend_schedule"]["dividend_count"]` | Passthrough | "2" |
| Leg quotes | `BBG_LEG_QUOTES` | `STORE_MARKET["leg_quotes"]` | bid/ask/mid: `f"{val:.2f}"`, iv: `f"{val:.1f}%"`, delta: `f"{val:.4f}"`, OTM%: `abs(k-s)/s*100` → `f"{val:.1f}%"` | DataTable |
| Raw JSON | `BBG_UNDERLYING_JSON` | `STORE_MARKET` + `STORE_INPUTS` | `json.dumps(raw, indent=2)` | Preformatted text |

### Activity Log (Generated on PDF export)

| UI Element | Component ID | Pack Key Read | Formatting Applied | Final Display |
|-----------|-------------|---------------|-------------------|---------------|
| Net Premium | `LOG_TABLE` | `pack["summary"]["net_premium_total"]` | Passthrough | "Credit $1,250" |
| Max Profit | `LOG_TABLE` | `pack["summary"]["rows"][0]["options"]` | Passthrough | "$5,000" |
| Max Loss | `LOG_TABLE` | `pack["summary"]["rows"][1]["options"]` | Passthrough | "-$2,500" |
| Strategy | `LOG_TABLE` | `pack["strategy"]["name"]` | Passthrough | "Bull Call Spread" |
| Contracts | `LOG_TABLE` | `sum(abs(leg["position"]))` from inputs | `str(int(total))` | "2" |

---

## Report Display

The PDF report pipeline: `pack → report_model → contract_v1 → view_model → Jinja2 template → WeasyPrint → PDF`

### Report Header (Page 1, Top Banner)

| Report Section | Field | Pack Key Read | Transformations | Final Format |
|---------------|-------|---------------|-----------------|--------------|
| Header | Strategy Name | `pack["strategy"]["name"]` | Passthrough | "Iron Condor" |
| Header | Ticker | `pack["underlying"]["resolved"]` | Passthrough | "AAPL US Equity" |
| Header | Last Price | `pack["underlying"]["spot"]` | `_format_currency(decimals=2)` | "$175.50" |
| Header | Company Name | `profile["NAME"]` | Passthrough | "Apple Inc" |
| Header | Sector | `profile["GICS_SECTOR_NAME"]` | Passthrough | "Information Technology" |
| Header | Report Date | `pack["as_of"]` | `_format_long_date()` | "February 17, 2026" |
| Header | Expiry | `pack["strategy"]["expiry"]` | `_format_date()` | "2026-03-20" |

### Stock Details (Page 1)

| Report Section | Field | Pack Key Read | Transformations | Final Format |
|---------------|-------|---------------|-----------------|--------------|
| Stock Details | 52-Week High | `profile["PX_52W_HIGH"]` | `_format_currency(decimals=0)` | "$199" |
| Stock Details | 52-Week Low | `profile["PX_52W_LOW"]` | `_format_currency(decimals=0)` | "$125" |
| Stock Details | YTD Change | `profile["CHG_PCT_YTD"]` | `_format_percent(decimals=2)` + " YTD", color class: "change-up"/"change-down" | "+12.34% YTD" (green) |
| Stock Details | Dividend Yield | `profile["EQY_DVD_YLD_IND"]` | Heuristic: if 0<val≤0.2, multiply by 100 → `f"{val:.1f}%"` | "1.5%" |
| Stock Details | Earnings Date | `profile["EXPECTED_REPORT_DT"]` | `_format_date()` | "2026-04-25" |
| Analyst View | UBS Rating | `pack["underlying"]["ubs_rating"]` | `.title()` applied | "Buy" |
| Analyst View | Price Target | `pack["underlying"]["ubs_target"]` | `_format_currency(decimals=2)` | "$200.00" |
| Analyst View | CIO View | `state["cio_rating"]` | Passthrough | "Most Preferred" |

### Client Position (Page 1, conditional)

| Report Section | Field | Pack Key Read | Transformations | Final Format |
|---------------|-------|---------------|-----------------|--------------|
| Client Position | Shares | `state["stock_position"]` | `_format_number(decimals=0)` | "500" |
| Client Position | Avg Cost | `state["avg_cost"]` | `_format_currency(decimals=2)` | "$150.00" |
| Client Position | Market Value | Computed: `shares × spot` | `_format_currency(decimals=2)` | "$87,750.00" |
| Client Position | P&L ($) | Computed: `(shares × spot) - (shares × avg_cost)` | `_format_currency`, "value-positive"/"value-negative" class | "+$12,750.00" |
| Client Position | P&L (%) | Computed: `pnl_dollar / cost × 100` | `_format_percent(decimals=2)` | "+17.00%" |

**Visibility**: Hidden (all fields `not_applicable`) when shares = 0. Layout switches to `analyst_only` mode.

### Option Legs Table (Page 1)

| Report Section | Field | Pack Key Read | Transformations | Final Format |
|---------------|-------|---------------|-----------------|--------------|
| Legs | Action | `pack["legs"][i]["side"]` | Normalize: "SHORT"→"Sell", "LONG"→"Buy" | "Buy" |
| Legs | Type | `pack["legs"][i]["kind"]` | Normalize: "CALL"/"PUT" | "CALL" |
| Legs | Quantity | `pack["legs"][i]["ratio"]` | `_format_number(decimals=0)` | "2" |
| Legs | Expiry | `pack["legs"][i]["expiry"]` or header | Passthrough | "2026-03-20" |
| Legs | Strike | `pack["legs"][i]["strike"]` | `_format_currency(decimals=2)` | "$175.00" |
| Legs | Price | `pack["legs"][i]["premium"]` | `abs(premium)` → `_format_currency(decimals=2)` | "$3.45" |
| Legs | Delta | `pack["legs"][i]["delta_mid"]` | `_format_number(decimals=2)` | "0.52" |
| Legs | OTM % | Computed: `abs(strike - spot) / spot × 100` | `_format_percent(decimals=2)` | "2.86%" |
| Legs | Premium (total) | Computed in view_model: `qty × price × 100` | `_format_currency(decimals=2)`, colored: Buy=red(debit), Sell=green(credit) | "-$690.00" |
| Legs | Net Premium | Accumulated: `Σ(±total_premium)` | `_format_currency(decimals=2)`, "value-positive"/"value-negative" | "Credit $1,250.00" |

### Metrics (Page 1)

| Report Section | Field | Contract Key | Pack Source | Transformations | Final Format |
|---------------|-------|-------------|------------|-----------------|--------------|
| Metrics | Max Profit | `metrics.max_profit` | `summary["Max Profit"].combined` | `_format_currency(decimals=0)` | "$5,000" |
| Metrics | Max Loss | `metrics.max_loss` | `summary["Max Loss"].combined` | `_format_currency(decimals=0)` | "-$2,500" |
| Metrics | Reward/Risk | `metrics.reward_risk` | `summary["Risk/Reward"].combined` or fallback: `abs(max_profit/max_loss)` | `_format_number(decimals=2)` | "2.00" |
| Metrics | Max ROI | `metrics.max_roi` | `summary["Max ROI"].combined` | `_format_percent(decimals=2)` after `_to_percent_ratio()` | "200.00%" |
| Metrics | Min ROI | `metrics.min_roi` | `summary["Min ROI"].combined` | Same | "-100.00%" |
| Metrics | Capital Basis | `metrics.capital_basis` | `summary["Capital Basis"].combined` | `_format_currency(decimals=0)` | "$2,500" |
| Metrics | Cost/Credit | `metrics.net_cost` | `summary["Cost/Credit"].combined` | `_format_currency(decimals=0)` | "Credit $1,250" |
| Metrics | Net Prem/Share | `metrics.net_premium_per_share` | `summary.net_premium_per_share` | `_format_currency(decimals=0)` | "$12" |
| Metrics | Yield % | `metrics.yield_percent` | `summary["Net Prem % Spot"].combined` | `_format_percent(decimals=2)` | "2.95%" |

When `has_stock_component=True`, the report shows split columns: "Options" vs "Combined" for each metric using the `*_options` variants.

### Payoff Chart (Page 1)

| Report Section | Pack Key Read | Transformations | Final Format |
|---------------|---------------|-----------------|--------------|
| Payoff chart | `pack["payoff"]["price_grid"]`, `["options_pnl"]`, `["stock_pnl"]`, `["combined_pnl"]`, `["strikes"]`, `["breakevens"]` | matplotlib PNG generation → base64 data URI | Embedded PNG image in HTML |

### Key Levels Table (Page 1)

| Report Section | Field | Contract Key | Pack Source | Transformations | Final Format |
|---------------|-------|-------------|------------|-----------------|--------------|
| Key Levels | Scenario | `key_levels.rows[i].label` | `pack["key_levels"]["levels"][i]["label"]` | Passthrough | "Current Market Price" |
| Key Levels | Price | `key_levels.rows[i].underlying_price` | `pack["key_levels"]["levels"][i]["price"]` | `_format_currency(decimals=2)` | "$423.50" |
| Key Levels | Move % | `key_levels.rows[i].move_pct` | `pack["key_levels"]["levels"][i]["move_pct"]` | `_format_percent(decimals=2)` | "-5.00%" |
| Key Levels | Stock PnL | `key_levels.rows[i].stock_pnl` | Same | `_format_currency(decimals=2)` + value class | "$0.00" |
| Key Levels | Option PnL | `key_levels.rows[i].option_pnl` | Same | Same | "+$3,500.00" |
| Key Levels | Option ROI | `key_levels.rows[i].option_roi` | Same | `_format_percent(decimals=2)` | "140.00%" |
| Key Levels | Net PnL | `key_levels.rows[i].net_pnl` | Same | `_format_currency(decimals=2)` + value class | "+$3,500.00" |
| Key Levels | Net ROI | `key_levels.rows[i].net_roi` | Same | `_format_percent(decimals=2)` | "140.00%" |

Current market price row gets CSS class `wm-row-highlight`.

### Scenario Commentary (Page 1)

| Report Section | Pack Key Read | Transformations | Final Format |
|---------------|---------------|-----------------|--------------|
| Bearish scenario | `pack["commentary_v2"][kind="bearish"]` | `.title` → title, `.body` → description; dot-class "dot-red" | Card with red dot |
| Stagnant scenario | `pack["commentary_v2"][kind="stagnant"]` | dot-class "dot-gray" | Card with gray dot |
| Bullish scenario | `pack["commentary_v2"][kind="bullish"]` | dot-class "dot-green" | Card with green dot |

Always padded to exactly 3 scenarios. Missing scenarios show "—" placeholder.

### Strategy Description (Page 1)

| Report Section | Pack Key Read | Transformations | Final Format |
|---------------|---------------|-----------------|--------------|
| Strategy Description | `core.strategy_map.get_strategy_description(name)` or `pack["commentary_blocks_v2"]` | Passthrough | Narrative text |

### Disclosures (Page 2)

| Report Section | Pack Key Read | Transformations | Final Format |
|---------------|---------------|-----------------|--------------|
| Disclaimers | `state["disclaimers"]` | Joined into single text block | Rendered on page 2 |

---

## Calculation Flow

```
Bloomberg Data (External)
    │
    ├─ bbg_resolve_security(ticker) ───────────────→ STORE_REF.resolved_ticker
    ├─ bbg_fetch_spot(resolved) ───────────────────→ STORE_REF.spot
    │
    └─ [BTN_REFRESH] ─→ refresh_leg_premiums()
         ├─ fetch_underlying_snapshot() ───────────→ STORE_MARKET.underlying_profile
         ├─ resolve_option_ticker_from_strike() ───→ STORE_MARKET.leg_tickers
         ├─ fetch_option_snapshot() ───────────────→ STORE_MARKET.leg_quotes
         ├─ fetch_vol_surface() ──────────────────→ STORE_MARKET._vol_surface_records
         └─ select_premium(quote, position, mode) → LEGS_TABLE.premium (per-leg)

    [BTN_ANALYZE] ─→ Build StrategyInput + call build_analysis_pack()
    │
    ╔═══════════════════════════════════════════════════════════════════╗
    ║  build_analysis_pack()  — Computation Order (Dependency Chain)  ║
    ╠═══════════════════════════════════════════════════════════════════╣
    ║                                                                   ║
    ║  1. Parse inputs → strategy_meta, underlying_profile, expiry      ║
    ║  2. Compute time-to-expiry: t = dte / 365.0                      ║
    ║  3. compute_payoff(strategy_input)                                ║
    ║     └─ price_grid, combined_pnl, options_pnl, stock_pnl,         ║
    ║        breakevens, unlimited flags                                ║
    ║  4. determine_strategy_code(input, roi_policy) → eligibility code ║
    ║  5. capital_basis(input, payoff, policy)                          ║
    ║     ├─ NET_PREMIUM: abs(net_prem × mult)                         ║
    ║     ├─ CASH_SECURED: strike × qty × mult (short puts)            ║
    ║     ├─ RISK_MAX_LOSS: abs(min PnL)                               ║
    ║     └─ MARGIN_PROXY: → compute_margin_proxy()                    ║
    ║  6. combined_capital_basis(input, option_basis)                   ║
    ║     └─ stock_basis + option_basis                                 ║
    ║  7. Auto-select capital basis by strategy code                    ║
    ║  8. compute_margin_full(input, **kwargs)                          ║
    ║     ├─ classify_strategy() → 7-code base                         ║
    ║     ├─ classify_strategy_refined() → 30-code refined             ║
    ║     ├─ CBOE: cash_initial, margin_initial, margin_maintenance    ║
    ║     └─ House: margin_initial, margin_maintenance                 ║
    ║  9. build_scenario_points() → key price list                     ║
    ║     └─ spot + avg_cost + strikes + breakevens + targets/infinity  ║
    ║ 10. compute_scenario_table(input, points, payoff, roi_policy)    ║
    ║     └─ DataFrame: price, pnl, roi, commentary per point          ║
    ║ 11. Resolve effective sigma (vega-weighted or ATM IV)            ║
    ║ 12. strategy_pop(combined payoff) → PoP                          ║
    ║ 13. compute_all_probabilities() → all prob metrics               ║
    ║ 14. Summary metrics assembly                                     ║
    ║     └─ Max Profit/Loss, Risk/Reward, ROI, Cost/Credit,          ║
    ║        Notional, Net Prem, PoP, Breakeven, Treasury              ║
    ║ 15. Key levels assembly + deduplication                          ║
    ║     └─ spot, strikes, breakevens, downside/upside, zero, ∞       ║
    ║ 16. get_account_eligibility(strategy_code) → eligibility table   ║
    ║ 17. build_commentary_v2(pack)                                    ║
    ║     └─ 3 narrative scenarios + detail blocks                     ║
    ║                                                                   ║
    ╚═══════════════════════════════════════════════════════════════════╝
    │
    └─→ Cached pack (server-side memory)
         │
         ├─→ Dashboard Callbacks (display only, no recomputation)
         │    ├─ #17  Payoff Chart (Plotly)
         │    ├─ #20  Metrics Table (dmc.Table)
         │    ├─ #20a Probability Panel (colored badges)
         │    ├─ #20b Margin Panel (dmc.Table + House Intraday)
         │    ├─ #21  Risk Banner (earnings/dividend alerts)
         │    ├─ #22  Scenario Commentary Cards (3 cards)
         │    ├─ #23  Key Levels Table (8-column table)
         │    ├─ #24  Eligibility Table
         │    ├─ #13  Bloomberg Tab (market data display)
         │    └─ #25  Stock Info Stats (market snapshot only)
         │
         └─→ [BTN_PDF] → Report Pipeline
              ├─ build_report_model(state + pack) → normalized display dict
              ├─ build_report_contract_v1(report_model) → strict contract with field status
              ├─ validate_report_contract_v1(contract) → JSON schema check
              ├─ build_view_model(contract) → Jinja2 template context
              ├─ build_payoff_chart_png_data_uri() → matplotlib chart as base64 PNG
              └─ Jinja2 template + WeasyPrint → PDF bytes
```

---

## Potential Issues Noted

### 1. Dividend Yield Heuristic — Fragile Threshold
**File**: `reporting/report_model.py` (`_fmt_dividend_yield`)
**Issue**: If `0 < value ≤ 0.2`, the value is multiplied by 100 (assuming it's a decimal that needs conversion to percentage). This means a stock with a genuine 15% dividend yield (0.15 raw) would be correctly converted, but a stock with a 0.15% yield (already in percentage points) would be incorrectly multiplied to 15%. The heuristic also breaks for yields above 20% (passed through as-is), creating an inconsistency at the 0.2 boundary.

### 2. Duplicate Breakeven Computation
**File**: `frontend_dash/vnext2/callbacks.py` (chart callback #17)
**Issue**: Options breakevens are **recomputed** from the options PnL trace using `_detect_breakevens()` in the chart callback, rather than reading `pack["payoff"]["breakevens"]` which is the combined breakeven. This is intentional (options-only vs combined breakevens), but the recomputation in the frontend duplicates logic from `core/payoff.py`. If the breakeven detection algorithm diverges, the chart and the pack could show different values.

### 3. Premium Sign Convention Complexity
**Files**: `core/roi.py`, `core/analysis_pack.py`, `reporting/html_v2/view_model.py`
**Issue**: Three different sign conventions exist:
  - `core/roi.py`: `net_premium = Σ(position × premium)` — positive = debit, negative = credit
  - `core/analysis_pack.py`: Formats as "Credit $X" or "Debit $X" (inverts sign for display)
  - `reporting/html_v2/view_model.py`: Recomputes premium accumulation with `Buy = -total`, `Sell = +total`

  The view_model recomputation from `qty × price × 100` could theoretically diverge from the pack's `net_premium_total_value` if rounding or abs() handling differs.

### 4. OTM% Computed in Multiple Places
**Files**: `reporting/report_model.py`, `frontend_dash/vnext2/callbacks.py` (BBG tab)
**Issue**: OTM percentage (`abs(strike - spot) / spot × 100`) is computed independently in both the report model and the Bloomberg tab callback. Neither reads a pre-computed value from the analysis pack. If the spot reference differs (market_spot vs pack spot), results could diverge.

### 5. IV Percent vs Decimal Boundary
**Files**: `frontend_dash/analysis_adapter.py`, `frontend_dash/vnext2/callbacks.py`
**Issue**: Bloomberg returns IV as a percentage (e.g., 22.5 for 22.5%). The adapter stores `per_leg_iv` as decimal (`iv/100`). The callback then extracts ATM IV from the vol surface (percentage) and divides by 100. Meanwhile, `underlying_profile["impvol_3m_atm"]` is stored as percentage and divided by 100 as fallback. This multi-step conversion at different points creates risk of double-conversion or missed conversion. A default of `0.2` (20% IV) is used when nothing else is available.

### 6. Unused Pack Keys
**File**: `core/analysis_pack.py`
**Issue**: Several underlying profile fields are extracted and stored in the pack but never displayed in either the dashboard or the PDF report:
  - `iv_skew_3m`, `iv_term_premium`, `iv_rv_percentile`, `iv_skew_percentile`, `iv_term_premium_percentile`
  - `eqy_trr_pct_1yr`, `chg_pct_1yr`, `chg_pct_5d`, `chg_pct_3m`
  - `put_call_oi_ratio`, `put_call_vol_ratio`, `realized_vol_3m`, `iv_rv_spread`

  These are stored but have no consumer. May be intended for future use.

### 7. Reward/Risk Fallback in Contract Adapter
**File**: `reporting/contract_v1/adapter.py`
**Issue**: If the "Risk/Reward" metric is missing from the pack summary, the adapter computes a fallback as `abs(max_profit / max_loss)`. However, the pack summary already computes "Risk/Reward" — the fallback exists for robustness. If both are present but computed differently (e.g., different rounding), the adapter's fallback would never trigger, but the dual-computation path is a maintenance concern.

### 8. Scenario Key Levels vs Key Levels — Two Separate Structures
**File**: `core/analysis_pack.py`
**Issue**: The pack contains both `pack["scenario"]["key_levels"]` (from the scenario table, with `Scenario`/`Price` column names) and `pack["key_levels"]["levels"]` (a separate structure with `id`/`label`/`source` fields). The dashboard uses `pack["key_levels"]["levels"]`, while the report uses `pack["scenario"]["key_levels"]` via `key_levels_display_rows_by_price`. These are built from the same underlying data but formatted differently, creating two sources of truth for key level displays.

### 9. PoP Uses Combined Payoff — Not Options-Only
**File**: `core/analysis_pack.py` (lines ~537-600)
**Issue**: The probability of profit (`strategy_pop()`) is computed using the **combined** payoff function (stock + options), not the options-only payoff. This is correct for position accuracy, but the metric appears in the summary under "PoP" without clarifying that it reflects the total position including stock. For covered calls or protective puts, this gives a different result than options-only PoP.

### 10. Hardcoded Default IV
**File**: `frontend_dash/vnext2/callbacks.py` (analysis callback)
**Issue**: When no IV is available from Bloomberg (no vol surface, no 3M ATM IV), the system defaults to `0.2` (20% implied volatility). This affects all probability calculations and could produce significantly misleading PoP/assignment metrics for high-vol stocks. The default is not flagged to the user.

### 11. Treasury Obligation Only for Cash-Secured
**File**: `core/analysis_pack.py`
**Issue**: The summary rows for "Treasury Obligation", "Treasury Interest", and "Treasury Return %" are only populated for cash-secured strategies. For other strategies, these rows exist but with empty/zero values, which creates unnecessary clutter in the metrics table.

### 12. Report Model Recomputes Metrics from Options-Only to Combined "Unlimited"
**File**: `reporting/report_model.py`
**Issue**: When `has_stock_position=True` and the key levels include an infinity level, the report model overrides `Max Profit` and `Max ROI` to "Unlimited" for the combined column. This override uses call-leg flags to decide, but it doesn't check if the infinity level represents unlimited profit or unlimited loss. The logic `not (has_short_call and not has_long_call)` approximates this but could be incorrect for exotic multi-leg strategies.
