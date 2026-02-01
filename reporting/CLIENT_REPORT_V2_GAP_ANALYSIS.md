# Client Report v2 Gap Analysis

Last updated: 2026-02-01

This document maps the Client Report v2 template (Design/REPORT_SPEC.md + template PDF)
to available data in stores, analysis_pack, report_model, and report_pdf. It identifies
gaps, ambiguous fields, and required transformations. This is a review-only artifact.

## Sources reviewed
- Design/REPORT_SPEC.md (source-of-truth field list and layout)
- Design/figma_report_v2/2026-01-18 figma test client report v2.pdf (template)
- Design assets present:
  - Design/UBS Logo.svg
  - Design/UBS Logo Png.png
- reporting/report_model.py
- reporting/report_pdf.py
- frontend_dash/vnext/callbacks.py (PDF download callback)
- core/analysis_pack.py
- core/scenarios.py
- core/narrative.py

## Current report pipeline (evidence-based)
1) UI stores (vNext):
   - store-inputs: snapshot taken only on Run Analysis
   - store-ui: session UI state (may diverge from analysis snapshot)
   - store-market: refreshed via REFRESH DATA only
2) analysis_pack is cached under store-analysis-key; report callback uses cache_get(key)
3) report_model.build_report_model(state) normalizes fields into:
   - header, structure, payoff, metrics
   - scenario_table, scenario_analysis_cards
   - key_levels_display_rows_by_price
   - warnings, disclaimers
4) report_pdf.build_report_pdf(...) currently renders a simple report:
   - Title
   - Key/value header table
   - Trade inputs table
   - Legs table (no expiry column)
   - Summary table (min/max/PoP/margin/capital)
   - Scenario table (top 10)
   - Scenario analysis cards (if present)
   - Key levels table (if present)
   - Disclaimers

This is not the v2 template layout yet; it is a functional placeholder.

## A) Template overview (exact order from REPORT_SPEC.md)
Page 1 (Letter, portrait):
1) Header Band
2) Structure Card
3) Payoff Card
4) Payoff & Metrics
5) Disclaimers

Page 2:
1) Scenario Analysis Cards
2) Key Levels Table
3) Commentary Blocks
4) Footer

## B) Field mapping by section (template -> available data)
Legend:
- AVAILABLE: exists in data sources now
- AVAILABLE-BUT-NEEDS-MAPPING: exists but requires formatting, mapping, or plumbing
- MISSING: not present in current pipeline
- UNKNOWN: ambiguous or inconsistent; verify

### 1) Header Band
| Field | Status | Source path | Transform / Notes |
|---|---|---|---|
| report_time (analysis_as_of) | AVAILABLE-BUT-NEEDS-MAPPING | analysis_pack["as_of"] (string), store-analysis-key["as_of"] | Ensure consistent timestamp (analysis time vs report time). |
| resolved_underlying | AVAILABLE | store-inputs["resolved_ticker"], store-market["resolved_underlying"] | Prefer resolved_underlying from store-market, fallback to store-inputs. |
| underlying_ticker | AVAILABLE | store-inputs["ticker"] / store-inputs["raw_ticker"] | Clean formatting; ensure not empty. |
| last_price / spot_value | AVAILABLE | store-inputs["spot"] | Use analysis snapshot, not live UI. |
| strategy_name | AVAILABLE-BUT-NEEDS-MAPPING | analysis_pack["strategy"]["name"] | report_model pulls from pack; ensure passed through. |
| expiry (chain_expiry) | AVAILABLE | store-inputs["expiry"] | Date format YYYY-MM-DD. |
| shares (stock_position) | AVAILABLE | store-inputs["stock_position"] | Format as integer. |
| avg_cost | AVAILABLE | store-inputs["avg_cost"] | Currency formatting. |
| NAME | AVAILABLE-BUT-NEEDS-MAPPING | store-market["underlying_profile"]["NAME"] or analysis_pack["underlying"]["profile"] | Available if store-market refreshed. |
| GICS_SECTOR_NAME / INDUSTRY_SECTOR | AVAILABLE-BUT-NEEDS-MAPPING | store-market["underlying_profile"] | report_model picks GICS_SECTOR_NAME or INDUSTRY_SECTOR. |
| 52WK_HIGH / 52WK_LOW | AVAILABLE-BUT-NEEDS-MAPPING | store-market["underlying_profile"] or analysis_pack["underlying"] | Report_model supports multiple key variants. |
| DVD_YLD / EQY_DVD_YLD_IND | AVAILABLE-BUT-NEEDS-MAPPING | store-market["underlying_profile"] | Requires percent normalization. |
| EARNINGS_ANNOUNCEMENT_DATE | AVAILABLE-BUT-NEEDS-MAPPING | store-market["underlying_profile"] or analysis_pack["underlying"]["earnings_date"] | Format as date string. |
| pricing_mode / roi_policy / vol_mode | AVAILABLE | store-inputs keys | Combine into policy string. |

### 2) Structure Card
| Field | Status | Source path | Transform / Notes |
|---|---|---|---|
| Legs table (Leg, Side, Expiry, Strike, Premium) | AVAILABLE-BUT-NEEDS-MAPPING | analysis_pack["legs"] OR store-inputs["legs"] | report_model uses pack legs; report_pdf legs table lacks expiry column (gap). |
| Net premium total | AVAILABLE-BUT-NEEDS-MAPPING | analysis_pack["summary"]["net_premium_total"] | Value is string "Credit X"; needs numeric if required. |
| Net premium per share | AVAILABLE-BUT-NEEDS-MAPPING | analysis_pack["summary"]["net_premium_per_share"] | Currently formatted string; may need numeric. |

### 3) Payoff Card (Chart)
| Field | Status | Source path | Transform / Notes |
|---|---|---|---|
| price_grid (x) | AVAILABLE | analysis_pack["payoff"]["price_grid"] | Present in analysis_pack. |
| combined_pnl (y) | AVAILABLE | analysis_pack["payoff"]["combined_pnl"] | Present in analysis_pack. |
| strikes | AVAILABLE | analysis_pack["payoff"]["strikes"] | Present in analysis_pack. |
| breakevens | AVAILABLE | analysis_pack["payoff"]["breakevens"] | Present in analysis_pack. |
| chart render in PDF | MISSING | n/a | report_pdf has no chart rendering. Needs Plotly export or native ReportLab chart. |

### 4) Payoff & Metrics
| Field | Status | Source path | Transform / Notes |
|---|---|---|---|
| Max Profit / Max Loss | AVAILABLE | analysis_pack["summary"]["rows"] | Rows contain string values; need currency formatting. |
| Capital Basis (options/combined) | AVAILABLE | analysis_pack["summary"]["rows"] | Present as strings. |
| Max ROI / Min ROI | AVAILABLE | analysis_pack["summary"]["rows"] | Present as strings. |
| Cost/Credit | AVAILABLE | analysis_pack["summary"]["rows"] | Present as "Credit/Debit" string. |
| Notional Exposure | AVAILABLE | analysis_pack["summary"]["rows"] | Present as string. |
| Net Prem/Share | AVAILABLE | analysis_pack["summary"]["rows"] | Present as string. |
| Net Prem % Spot | AVAILABLE | analysis_pack["summary"]["rows"] | Present as percent string. |
| PoP | AVAILABLE | analysis_pack["summary"]["rows"] | Present as percent string. |
| Rendered table in PDF | AVAILABLE-BUT-NEEDS-MAPPING | report_model["metrics"]["rows"] | report_pdf does not use full metrics table; only summary subset. |

### 5) Disclaimers
| Field | Status | Source path | Transform / Notes |
|---|---|---|---|
| Disclaimers block | AVAILABLE-BUT-NEEDS-MAPPING | report_model["disclaimers"] | Defaults to "--" if not provided; report_pdf uses notes list. |

### 6) Scenario Analysis Cards (Page 2)
| Field | Status | Source path | Transform / Notes |
|---|---|---|---|
| Bearish / Stagnant / Bullish text | AVAILABLE-BUT-NEEDS-MAPPING | analysis_pack["narrative_scenarios"] -> report_model["scenario_analysis_cards"] | report_pdf renders cards if present. Verify narrative_scenarios present. |

### 7) Key Levels Table (Page 2)
| Field | Status | Source path | Transform / Notes |
|---|---|---|---|
| Scenario label | AVAILABLE | analysis_pack["key_levels"]["levels"] | report_model builds key_levels_display_rows_by_price. |
| Price | AVAILABLE | analysis_pack["key_levels"]["levels"] | Formatting required. |
| Move % | AVAILABLE-BUT-NEEDS-MAPPING | analysis_pack["key_levels"]["levels"]["move_pct"] | Computed in analysis_pack key_levels. |
| Stock PnL / Option PnL / Net PnL | AVAILABLE | analysis_pack["key_levels"]["levels"] | Present (stock_pnl, option_pnl, net_pnl). |
| Option ROI / Net ROI | AVAILABLE | analysis_pack["key_levels"]["levels"] | Present (net_roi). Option ROI may require derivation. |
| Highlight Current Market Price row | MISSING | n/a | report_pdf does not style rows. |

### 8) Commentary Blocks (Page 2)
| Field | Status | Source path | Transform / Notes |
|---|---|---|---|
| Spot / Strikes / Breakevens / Low / High commentary | AVAILABLE-BUT-NEEDS-MAPPING | analysis_pack["commentary_blocks"] | report_model uses commentary_blocks but report_pdf does not render. |

### 9) Footer
| Field | Status | Source path | Transform / Notes |
|---|---|---|---|
| "UBS Financial Services Inc." | MISSING | n/a | Not in report_pdf. |
| "Page X of Y" | MISSING | n/a | Not in report_pdf. |

## C) Required tables vs availability
### Legs table
Spec columns: Leg, Side, Expiry, Strike, Premium
Current availability:
- analysis_pack["legs"] includes side/kind/ratio/strike/premium, but expiry not stored per leg.
- store-inputs["expiry"] exists; can be used as single expiry value for each leg.
Gap:
- report_pdf legs table does NOT include expiry column.

### Key Levels table
Spec columns:
Scenario | Price | Move % | Stock PnL | Option PnL | Option ROI | Net PnL | Net ROI
Current availability:
- analysis_pack["key_levels"]["levels"] has price, move_pct, stock_pnl, option_pnl, net_pnl, net_roi.
- report_model calculates option_roi if needed when stock position present.
Gap:
- PDF row highlighting for "Current Market Price" not implemented.

### Scenario table
Spec columns:
scenario, price, move_pct, stock_pnl, option_pnl, option_roi, combined_pnl, net_roi, commentary
Current availability:
- analysis_pack["scenario"]["df"] columns: price, option_pnl, stock_pnl, combined_pnl, margin_requirement, option_roi, net_roi, commentary, scenario
Gap:
- move_pct is not computed in core.scenarios (missing in scenario_df), so report_model cannot populate it unless computed later.

## D) Chart requirements
Spec: Payoff chart on Page 1 with strikes/breakevens labels.
Current status:
- UI has Plotly chart (PAYOFF_CHART), but PDF does not render any chart.
- report_pdf uses ReportLab and has no chart drawing.
Status: MISSING
Possible approaches:
- Export Plotly figure via kaleido (new dependency) and embed PNG.
- Draw payoff line using ReportLab primitives (manual scaling).

## E) Assets + typography
- Logo assets exist in Design/ (SVG + PNG).
- Frutiger is required by spec, but ReportLab does not register it.
Status:
  - Logo: AVAILABLE-BUT-NEEDS-MAPPING (must load PNG/SVG)
  - Font: MISSING (requires TTF/OTF and registration)
Notes:
  - ReportLab can embed TTF via pdfmetrics.registerFont.
  - If Frutiger not licensed, define fallback (Helvetica) and note in output.

## F) Missing / ambiguous items (actionable)
1) Report time vs analysis time vs market refreshed_at
   - analysis_pack["as_of"] exists, store-market["refreshed_at"] exists.
   - Spec requires analysis_as_of; decide display precedence.
2) Scenario table move_pct
   - core.scenarios.compute_scenario_table does not compute move_pct.
3) Payoff chart in PDF
   - No export path exists; must choose approach (kaleido or ReportLab drawing).
4) Commentary blocks
   - analysis_pack["commentary_blocks"] exists but report_pdf ignores.
5) Footer
   - Not implemented (company name + page number).
6) Structure card expiry column
   - Only single expiry stored; report_pdf legs table lacks expiry column.
7) Net premium numeric vs formatted string
   - analysis_pack summary stores string; spec wants numeric display/format control.
8) Logo placement + scaling
   - Spec requires UBS branding; not implemented in PDF.
9) Frutiger font availability
   - Requires font file and license; currently unknown.

## G) Recommended implementation plan (PR-sized steps)
1) Normalize report_model outputs to match template fields
   - Add move_pct to scenario_df or compute in report_model.
   - Ensure structure legs include expiry column (from pack strategy expiry).
   Acceptance: report_model returns a complete field set with placeholders.

2) Implement report_pdf v2 skeleton
   - Two pages, header band layout, card blocks, footer.
   - Use placeholder values from report_model.
   Acceptance: PDF layout matches section order and spacing.

3) Wire actual fields + formatting
   - Map header band, structure, metrics, key levels, commentary.
   - Add "Current Market Price" row highlight.
   Acceptance: data appears correctly with "--" for missing.

4) Add payoff chart export
   - Decide on kaleido vs native drawing.
   - Embed chart into PDF Payoff Card.
   Acceptance: chart renders with strikes/breakevens labels.

5) Add assets + typography
   - Load UBS logo PNG; add placement.
   - Register Frutiger (or explicit fallback).
   Acceptance: branding + fonts in output.

---
End of gap analysis.
