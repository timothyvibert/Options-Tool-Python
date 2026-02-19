# CLAUDE.md — Alpha Engine (Options Strategy Builder)

## What this project is
Institutional-grade options analytics platform for UBS Equities & Options Sales desk.
63 named strategies + custom. Bloomberg data → deterministic engine → Dash dashboard + PDF reports.
Python 3.13, Dash 2.18, Dash Mantine Components (Mantine v8), WeasyPrint, ReportLab (fallback).

## Entrypoints
- **Run app**: `python -m frontend_dash.run_vnext`
- **Run tests**: `python -m pytest -q` (all must pass, zero xfail/skip expected)
- **Run calculation audit**: `python tools/calculation_audit.py` (63 strategies × 4 cost-basis scenarios = 252 runs, ~25,000 checks)
- **Render sample PDF**: `python tools/render_report_html_v2.py --contract Design/sample_report_contract.json --out out/report_html_v2.pdf`
- **Build sample contract**: `python tools/build_report_contract_json.py`

## Environment
- OS: Windows
- Python: 3.13.x (conda env: "options-tool")
- Activate: `conda activate options-tool`
- Key deps: Dash 2.18.x, DMC (Mantine v8), ReportLab 4.4.x, WeasyPrint (conda-forge), Jinja2, jsonschema

---

## Non-negotiable rules
1. **Core purity**: `core/` has zero imports from UI, Bloomberg, PDF, or frontend. Verified clean. Changes to core/ require tests.
2. **No recomputation in reporting**: Report generation consumes cached analysis_pack only. Never triggers Bloomberg or re-runs analysis.
3. **HTML/WeasyPrint is default renderer**. ReportLab is silent fallback only. Do not extend ReportLab.
4. **Contract-first rendering**: contract_v1 drives all visibility and field values. Renderers are dumb — they format, they do not infer business meaning.
5. **No runtime JS/Node/Playwright/Kaleido**: PDF pipeline must be pure Python at runtime.
6. **Bloomberg boundaries**: Spot lookup only on ticker commit (blur/enter) via `_v2_ping_spot`. Market refresh only on explicit BTN_REFRESH via `_v2_refresh_market`. No Bloomberg calls from dropdown changes, UI toggles, or report generation. Gated by `bloomberg_available` bool.
7. **One change at a time**: Make a single PR-sized change, run tests, validate, then move on.
8. **No circular imports**: Strict unidirectional DAG. Verified clean.

---

## Architecture — Computation pipeline

```
User inputs (Dash UI)
  → frontend_dash/vnext2/callbacks.py        [28 callbacks, closure-based registration]
  → core/analysis_pack.build_analysis_pack() [master orchestrator, returns 18-key dict]
      Internally calls:
      → core/payoff.compute_payoff()         [P&L arrays, breakevens, unlimited flags]
      → core/scenarios.build_scenario_points() + compute_scenario_table()
      → core/roi.capital_basis() + compute_net_premium()
      → core/probability.strategy_pop() + compute_all_probabilities()
      → core/commentary_v2.build_commentary_v2()
      → core/margin.classify_strategy() + compute_margin_full()
      → core/advisory.select_template() + resolve_archetype()
      → core/eligibility.get_account_eligibility()
  → Pack cached server-side with UUID key (MAX=20, TTL=1800s)

  Report path (separate from dashboard):
  → reporting/report_model.build_report_model()           [normalize pack to display dict]
  → reporting/contract_v1/adapter.build_report_contract_v1()  [strict TypedDict contract]
  → reporting/contract_v1/validate.validate_report_contract_v1()  [JSON Schema Draft 7]
  → reporting/html_v2/view_model.build_view_model_from_contract()  [template-ready]
  → reporting/html_v2/renderer.build_report_pdf_html()    [Jinja2 + WeasyPrint → PDF]
  → (silent fallback: ReportLab if WeasyPrint fails)
```

---

## Analysis pack structure (18 top-level keys)

Returned by `build_analysis_pack()`. This is the central data dict consumed by everything downstream.

| Key | Type | Description |
|-----|------|-------------|
| `as_of` | str | ISO date or "--" |
| `underlying` | dict | 35+ fields: spot, 52wk, YTD%, IV, earnings_risk, dividend_risk, profile |
| `strategy` | dict | group, subgroup, name, id, strategy_code, expiry |
| `policies` | dict | pricing_mode, roi_policy, vol_mode, risk_free_rate, auto_capital_basis |
| `legs` | list[dict] | Per-leg: kind, side, ratio, strike, premium, delta/gamma/theta/vega/rho |
| `payoff` | dict | price_grid (300 pts), options_pnl, stock_pnl, combined_pnl, strikes, breakevens |
| `summary` | dict | 13+ metric rows: Max Profit/Loss, Risk/Reward, ROI, PoP, Breakeven, Cost/Credit, etc. |
| `margin` | dict | classification, margin_proxy, full breakdown |
| `probabilities` | dict | pop, pop_pct, iv_source, iv_used_pct, max_profit_prob, max_loss_prob |
| `scenario` | dict | df (DataFrame), top10, key_levels |
| `eligibility` | dict | strategy_code, table (DataFrame), error |
| `key_levels` | dict | meta (spot, has_stock, shares, avg_cost) + levels[] with id/label/price/move_pct/pnl/roi |
| `dividend_schedule` | dict\|None | Populated post-pack by callbacks |
| `vol_surface` | dict | atm_iv_at_expiry, source |
| `commentary_v2` | list[dict] | 3 scenarios: bearish/stagnant/bullish with kind, condition, body |
| `commentary_blocks_v2` | list[dict] | 5 blocks: Spot, Strikes, Breakevens, Low, High |

**Empty pack**: When no legs and no stock position, `_build_empty_pack()` returns minimal pack with empty arrays and "$0.00" / "N/A" values.

**Unlimited handling** (from `_detect_unlimited()` in payoff.py):
Flags indicating whether P&L diverges at price extremes. These are consumed by `analysis_pack.py` to set "Unlimited" strings in the summary. If modifying, check both `payoff.py` (flag production) and `analysis_pack.py` (flag consumption).

**Sentinel rows** in key_levels/scenarios:
- "zero" row (price=0.0) — computed via `_row_for_price(0.0)`
- "infinity" row (price=None) — uses proxy `max(max_strike * 10, spot * 10)`

---

## Core module inventory (14 files, ~5,353 lines)

| File | Lines | Purpose | Key functions |
|------|-------|---------|---------------|
| `analysis_pack.py` | 1,247 | Master orchestrator | `build_analysis_pack()` |
| `commentary_v2.py` | 1,164 | Zone-based narrative engine | `build_commentary_v2()` |
| `margin.py` | 939 | FINRA 4210 margin (30 CBOE codes) | `classify_strategy()`, `compute_margin_full()` |
| `probability.py` | 505 | Black-Scholes Greeks, PoP | `strategy_pop()`, `compute_all_probabilities()`, `effective_sigma()` |
| `scenarios.py` | ~300 | Scenario table builder | `build_scenario_points()`, `compute_scenario_table()` |
| `payoff.py` | ~350 | Payoff grid + breakevens + unlimited detection | `compute_payoff()` |
| `roi.py` | ~200 | Capital basis + ROI | `capital_basis()`, `compute_net_premium()` |
| `advisory.py` | ~350 | Template-based advisory | `load_advisory_templates()`, `select_template()`, `resolve_archetype()` |
| `eligibility.py` | ~150 | Account eligibility lookup | `determine_strategy_code()`, `get_account_eligibility()` |
| `strategy_map.py` | ~150 | CSV strategy catalog (63 strategies, 9 groups) | `list_groups()`, `list_strategies()`, `get_strategy()` |
| `pricing.py` | ~100 | Bid/mid/ask selection | `select_price()` |
| `margin_map.py` | ~80 | CBOE margin text lookup | `lookup_requirement_text()`, `list_all_codes()` |
| `models.py` | ~50 | Frozen dataclasses | `OptionLeg`, `StrategyInput` |

---

## Dashboard — callbacks (28 total)

File: `frontend_dash/vnext2/callbacks.py` (2,729 lines)

Registration: `register_v2_callbacks(app, cache_get, cache_put, bloomberg_available, bbg_resolve_security, bbg_fetch_spot)` — all 28 callbacks defined as closures inside this function.

**29 helper functions** in the same file: formatting (7), normalization (3), schema conversion (4), quote handling (4), strategy (3), chart (2), table (2), other (4).

**Key callbacks by stage:**

| Stage | # | Function | Trigger → Output |
|-------|---|----------|------------------|
| Input | 0 | `_v2_toggle_theme` | THEME_TOGGLE → MANTINE_PROVIDER |
| Input | 1 | `_v2_update_strategies` | GROUP_SELECT → STRATEGY_SELECT |
| Input | 2 | `_v2_apply_legs_updates` | STRATEGY_SELECT/STORE_MARKET/BTN_CLEAR → LEGS_TABLE |
| Input | 3 | `_v2_ping_spot` | TICKER_INPUT n_submit/n_blur → STORE_REF |
| Input | 4 | `_v2_display_spot` | STORE_REF → SPOT_DISPLAY |
| Market | 5 | `_v2_refresh_market` | BTN_REFRESH → STORE_MARKET |
| Market | 25 | `_v2_render_stock_info` | STORE_MARKET → stat cards |
| **Analysis** | **10** | **`_v2_run_analysis`** | **BTN_ANALYZE → STORE_ANALYSIS_KEY, STORE_INPUTS** |
| Render | 11 | `_v2_render_chart` | STORE_ANALYSIS_KEY + checkboxes → PAYOFF_CHART (267 lines, largest) |
| Render | 14 | `_v2_render_panels` | STORE_ANALYSIS_KEY → METRICS_TABLE, DIVIDEND_CARD |
| Render | 15 | `_v2_render_probabilities` | STORE_ANALYSIS_KEY → probability bar values |
| Render | 16 | `_v2_render_margin` | STORE_ANALYSIS_KEY + MARGIN_MODE → MARGIN_FULL_TABLE |
| Render | 17 | `_v2_render_house_intraday` | STORE_ANALYSIS_KEY + inputs → HOUSE_INTRADAY_TABLE |
| Render | 18 | `_v2_render_risk_banner` | STORE_ANALYSIS_KEY → RISK_BANNER |
| Render | 19 | `_v2_render_scenario_cards` | STORE_ANALYSIS_KEY → SCENARIO_CARDS |
| Render | 20 | `_v2_render_key_levels` | STORE_ANALYSIS_KEY → KEY_LEVELS_TABLE |
| BBG | 6 | `_v2_render_bbg_tab` | STORE_MARKET + STORE_INPUTS + STORE_ANALYSIS_KEY → BBG panels |
| Report | 7 | `_v2_download_report_pdf` | BTN_PDF → DL_REPORT_PDF |
| Report | 8 | `_v2_auto_select_excel_template` | STORE_ANALYSIS_KEY → EXCEL_TEMPLATE_SELECT |
| Report | 9 | `_v2_generate_excel_pdf` | BTN_EXCEL_PDF → DL_EXCEL_PDF |
| Report | 21 | `_v2_render_eligibility` | STORE_ANALYSIS_KEY → ELIGIBILITY_TABLE |
| UI State | 12 | `_v2_sync_ui` | All inputs → STORE_UI |
| UI State | 13 | `_v2_hydrate_ui` | TABS.value → restores all inputs |
| Log | 22-24 | Activity log callbacks | LOG_STORE / BTN_CLEAR_LOG / BTN_DOWNLOAD_CSV |
| Shutdown | 26-27 | Shutdown modal + server kill | BTN_SHUTDOWN / SHUTDOWN_YES |

**5 Dash stores**: STORE_REF, STORE_MARKET, STORE_ANALYSIS_KEY, STORE_UI, STORE_INPUTS
**152 component IDs**: all `v2-` prefixed, defined in `frontend_dash/vnext2/ids.py`

**`suppress_callback_exceptions=True` is required** — callbacks reference components across tabs.

### Other vnext2 files
| File | Lines | Purpose |
|------|-------|---------|
| `layout.py` | 1,093 | Full Dash layout tree (DMC components), 4 tabs |
| `ids.py` | 152 | Component ID constants |
| `theme.py` | 56 | Mantine theme config, dark palette |
| `activity_log.py` | 63 | CSV-based activity log |

---

## Server-side cache

Location: `frontend_dash/run_vnext.py`
- `_ANALYSIS_CACHE: dict[str, dict]` — key → pack
- `_ANALYSIS_CACHE_TS: dict[str, float]` — key → timestamp
- `MAX_CACHE_ENTRIES = 20`, `CACHE_TTL_SECONDS = 1800` (30 min)
- `_cache_put(pack)` → returns UUID hex key
- `_cache_get(key)` → returns pack or None
- Pruning: time-based + size-based on every put/get

---

## Data files

| File | Rows | Cols | Loader |
|------|------|------|--------|
| `data/strategy_map.csv` | 63 | 22 | `core/strategy_map.py` (lazy) |
| `data/account_map.csv` | ~30 | 5 | `core/eligibility.py` |
| `data/margin_map_cboe.csv` | ~30 | 5 | `core/margin_map.py` (lazy) |
| `data/scenario_advisory_map.csv` | ~50 | varies | `core/advisory.py` (lazy) |

All CSV loads use lazy initialization (_loaded flag or _CACHE global set on first call). No import-time side effects.

---

## Reporting pipeline

```
_v2_download_report_pdf()                            [callbacks.py]
  → build_report_model(state)                        [report_model.py, 1,040 lines]
  → build_report_pdf_html(report_model)              [renderer.py, 261 lines]
      → build_payoff_chart_png_data_uri(model)       [view_model.py — matplotlib PNG]
      → build_report_contract_v1(report_model)       [adapter.py, 475 lines]
      → validate_report_contract_v1(contract)        [validate.py — JSON Schema Draft 7]
      → build_view_model_from_contract(contract)     [view_model.py, 1,282 lines]
      → Jinja2 template render                       [templates/base.html]
      → WeasyPrint HTML→PDF                          [figma_v2_print.css]
      → (fallback: ReportLab if WeasyPrint fails)
```

**Contract schema**: 16 TypedDict types in `reporting/contract_v1/types.py`. Validated against `reporting/contract_v1/schema.json` (~800 lines, JSON Schema Draft 7).

**Excel export** (Windows-only, optional): 6 templates via openpyxl + win32com Excel COM.

**Dead code**: `build_payoff_svg_data_uri()` in view_model.py (lines 814-1044, ~231 lines). Replaced by matplotlib PNG version. Never called. Safe to delete.

### Report design references
- **Figma source of truth**: `Design/figma_report_v2/2026-01-18 figma test client report v2.pdf`
- **Design spec**: `Design/REPORT_SPEC.md`
- **HTML template export**: `Design/figma_report_v2/figma_HTML_report_template.html` (uses Tailwind CDN — must convert to static CSS for WeasyPrint)
- **Sample contract**: `Design/sample_report_contract.json`
- **Gap analysis**: `reporting/CLIENT_REPORT_V2_GAP_ANALYSIS.md`

---

## Testing

Always run `python -m pytest -q` after changes. All tests must pass. No `@pytest.mark.skip` or `@pytest.mark.xfail` expected.

**Full engine audit**: `python tools/calculation_audit.py` — runs 63 strategies × 4 cost-basis scenarios (options_only, avg_cost=spot, avg_cost=0.5×spot, avg_cost=1.15×spot). Produces `calculation_audit.md` (~20,000 lines).

### Coverage by module

| Core module | Test files | Level |
|-------------|-----------|-------|
| analysis_pack.py | test_analysis_pack (30), test_analysis_pack_greeks (7), test_analysis_pack_events_and_eligibility (2), test_dedup_key_levels (17) | Excellent |
| commentary_v2.py | test_commentary_v2 (27 + 63-strategy parametrized regression) | Excellent |
| payoff.py | test_payoff (11) | Good |
| scenarios.py | test_scenarios (7) | Good |
| probability.py | test_probability (6), test_probability_ui_logic (2) | Good |
| margin.py | test_margin (4) | Good |
| roi.py | test_roi (5), test_new_metrics (13) | Good |
| pricing.py | test_pricing (4) | Good |
| strategy_map.py | test_strategy_queries (4) | Good |
| eligibility.py | test_eligibility (2) | Minimal |
| advisory.py | test_advisory (3) | Partial |
| **margin_map.py** | — | **UNTESTED** |
| **models.py** | — | **UNTESTED** (used indirectly) |

### Integration tests
| Test file | Scope |
|-----------|-------|
| test_golden_strategies.py (10) | Full pack for 8 strategy archetypes |
| test_report_model.py (54) | report_model normalization |
| test_report_contract_v1_validation.py (3) | pack → model → contract → validate |
| test_report_pdf_html_v2_content.py (6) | PDF structure, disclaimers, headers |
| test_report_pdf_html_v2_smoke.py (1) | PDF generation smoke |

**Conditional skips**: `pytest.importorskip("weasyprint")`, `pytest.importorskip("jinja2")`, `pytest.skip()` for missing pypdf/PyPDF2.

---

## ⚠ Fragile patterns — handle with care

**HIGH RISK — String matching on metric labels:**
- `reporting/report_model.py:909` — hardcoded `"Max Profit"` / `"Max ROI"` string comparison for unlimited cap logic
- `frontend_dash/vnext2/callbacks.py:2125` — same metric label string matching
- If you rename a metric label in `analysis_pack.py`, you MUST grep for the old string in report_model.py and callbacks.py

**MEDIUM RISK — MISSING sentinel inconsistency:**
- `reporting/html_v2/view_model.py:8` uses `"—"` (em-dash)
- `reporting/report_model.py:14` uses `"--"` (double-dash)
- These are not interchangeable. Match the convention of the file you're editing.

**MEDIUM RISK — Bloomberg adapter:**
- `adapters/bloomberg.py:394` — `_TREASURY_MAP[-1]` without empty-list guard

**Scattered constants (not centralized):**
| Constant | Locations | Note |
|----------|-----------|------|
| Grid size 300 | `payoff.py:8,150`, `calculation_audit.py:317` | Inline default + hardcoded |
| Grid range 3.0× | `payoff.py:9` | Magic number |
| Breakeven tolerance 0.50 | `payoff.py:50` | Named `_BE_TOLERANCE` but local |
| Epsilon 1e-6 | `payoff.py`, `advisory.py`, `report_model.py` (4+ files) | Repeated |
| Flatness threshold 0.01 | `commentary_v2.py` (10+ places) | Hardcoded throughout |
| Multiplier default 100 | `models.py:13`, `margin.py`, `roi.py` | Repeated in 3 files |

---

## ⚠ Known non-bugs (do NOT fix these)

These appear in audit output and look wrong but are mathematically correct:

1. **Negative combined max profit** when avg_cost >> spot — unrealized stock losses exceed option gains
2. **Capital at Risk = $1.00 floor** — prevents division-by-zero in ROI for zero-premium positions
3. **Assignment Probability = 0.0 for long-only strategies** — correct, you can't be assigned on long options
4. **PoP = 0% for extreme avg_cost scenarios** — mathematically correct when breakeven requires impossibly large move
5. **5 audit failures for Custom Strategy options_only** — expected empty pack behavior

---

## Verification after changes

After any engine change (core/ files), always:
1. `python -m pytest -q` — all tests must pass
2. `python tools/calculation_audit.py` — review `calculation_audit.md` for regressions
3. Check the 5 expected Custom Strategy empty-pack failures are the ONLY failures

The audit checks 10 categories (A–J) across all 63 strategies × 4 cost-basis scenarios. If a fix introduces new failures, investigate before committing.

---

## Code quality notes

- **43 silent exception blocks** (`except Exception: pass`) — 12 in analysis_adapter.py, 11 in calculation_audit.py, 7 in bloomberg.py, 5 in analysis_pack.py, 8 elsewhere
- **Dormant logger**: `analysis_pack.py` imports logging and creates `logger = logging.getLogger(__name__)` but zero actual log calls anywhere in the codebase
- **Zero dead code in core/** — all public functions called. One dead function in reporting (SVG builder, see above).
- **Zero TODOs/FIXMEs** in codebase
- **Type annotations ~96% in core** — return types on ~93 of ~97 functions, no mypy enforcement
- **Naming conventions**: excellent consistency — snake_case functions, UPPER_CASE constants, PascalCase classes

---

## Git conventions
- Commit messages: `type(scope): description` (e.g., `fix(payoff): directional unlimited flags`)
- Types: feat, fix, refactor, test, docs, chore
- Do not commit: `out/`, `node_modules/`, `__pycache__/`, `.env`
