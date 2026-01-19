# Client Report UI/PDF Spec (Source of Truth: PDF)

Source PDF: `Design/figma_report_v2/2026-01-18 figma test client report v2.pdf`

Note: The PDF media box is 612 x 792 pt (8.5 x 11 in). This spec uses Letter size only; do not scale to A4.

## Page Size, Margins, and Grid
- Page size: 612 x 792 pt, portrait.
- Content padding: 30 pt left/right, 24 pt top, 18 pt bottom (matches px-10 / py-8 / pb-6).
- Section vertical spacing: 9 pt between major blocks (matches 12 px).
- Card padding: 9 pt (p-3) for standard cards, 15 pt (p-5) for scenario analysis block.
- Card corner radius: 6 pt (rounded-md) or 8 pt (rounded-lg) depending on block.
- Footer: 9 pt text, uppercase, tracking +0.05em, left/right aligned.

## Typography Rules (sizes in px, 96 dpi)
- Font family: system sans (UI sans serif).
- Page title (strategy name): 24 px, bold, color #E60000.
- Section header (card titles): 12 px to 14 px, bold, uppercase, color #111827.
- Subheader/labels: 10.5 px, medium, color #6B7280.
- Body text: 10.5 px, color #374151.
- Table header: 10 px, bold, uppercase, color #6B7280, background #F3F4F6.
- Table body: 10 px, color #111827.
- Fine print/disclaimer: 9.5 px, color #6B7280.
- Footer: 9 px, uppercase, color #9CA3AF.

## Color Tokens (hex)
- Primary red: #E60000 (strategy title, section headers, bearish indicators).
- Primary text: #111827.
- Secondary text: #6B7280.
- Muted text: #9CA3AF.
- Border: #E5E7EB.
- Light border: #D1D5DB.
- Card background: #FFFFFF.
- Page background: #F3F4F6 (gray-100).
- Highlight row: #FEF9C3 (current market price in key levels table).
- Bullish dot: #00A550.
- Stock line: #93C5FD.
- Options line: #C4B5FD.
- Combined line: #4B5563.
- Strike lines: #E5E7EB.
- Breakeven lines: #9CA3AF.
- Chart grid: #E5E7EB.

## Page 1: Sections, Order, Purpose
1) Header Band (dense strip)
   - Purpose: identify report, underlying, strategy, timing, and key equity stats.
   - Layout: single row with multiple columns; includes a second row for name/sector/52w/dvd/earnings and a third row for policies/title.
   - Data fields:
     - Report time: `analysis_as_of` (or current timestamp).
     - Underlying ticker: `resolved_underlying` else `underlying_ticker`.
     - Last price: `spot_value`.
     - Strategy name: `analysis_strategy_name`.
     - Expiry: `chain_expiry` (YYYY-MM-DD).
     - Shares: `stock_position`.
     - Avg cost: `avg_cost`.
     - Name: underlying snapshot `NAME`.
     - Sector: `GICS_SECTOR_NAME` (fallback `INDUSTRY_SECTOR`).
     - 52W high/low: `52WK_HIGH`, `52WK_LOW`.
     - Dividend yield: `DVD_YLD` (fallback `EQY_DVD_YLD_IND`).
     - Earnings date: `EARNINGS_ANNOUNCEMENT_DATE`.
     - Policies: `pricing_mode`, `roi_policy`, `vol_mode`.

2) Structure Card (left)
   - Purpose: summarize option legs and net premium.
   - Layout: compact table with legs 1-4 (always show 1-4; use "--" if unused).
   - Table columns (exact order): Leg, Side, Expiry, Strike, Premium.
   - Data fields:
     - Side: `pos_i` (Long/Short).
     - Expiry: `chain_expiry`.
     - Strike: `strike_i`.
     - Premium: `prem_i`.
   - Net premium lines below table:
     - Net premium total: `compute_net_premium(strategy) * multiplier`.
     - Net premium per share: `compute_net_premium(strategy)`.

3) Payoff Card (right)
   - Purpose: combined payoff curve with key levels annotated.
   - Layout: large chart area, 420 px height, full card width.
   - Data fields:
     - X: `analysis_results.price_grid`.
     - Y: `analysis_results.pnl` (combined).
     - Strikes: active leg strikes (numeric).
     - Breakevens: `analysis_results.breakevens`.
   - Default annotations:
     - Strike labels: K1..K4 (max 6 labels).
     - Breakeven labels: BE1..BE4 (max 4 labels).

4) Payoff & Metrics (full width card)
   - Purpose: Excel-style metrics table with Options vs Combined columns.
   - Columns: Metric | Options | Combined.
   - Rows:
     - Max Profit: max(options_pnl) / max(combined_pnl).
     - Max Loss: min(options_pnl) / min(combined_pnl).
     - Capital Basis: `capital_basis()` / `combined_capital_basis()`.
     - Max ROI: max(option_roi) / max(net_roi).
     - Min ROI: min(option_roi) / min(net_roi).
     - Cost/Credit: net premium total (sign indicates credit/debit) for both.
     - Notional Exposure: sum(abs(q)*strike*multiplier) / + stock notional.
     - Net Prem/Share: `compute_net_premium()`.
     - Net Prem % Spot: net prem per share / spot.
     - PoP: `analysis_summary_payload.pop`.

5) Disclaimers (small text block)
   - Purpose: legal/risk statements.
   - Content: use the PDF disclosure paragraph, 9.5 px text, justified.

## Page 2: Sections, Order, Purpose
1) Scenario Analysis Cards (top)
   - Purpose: narrative summaries for bearish/stagnant/bullish cases.
   - Layout: 3 columns, equal height cards, 9 pt gaps.
   - Data fields: derived from scenario commentary (if available) or placeholders.

2) Key Levels Table (full width)
   - Purpose: tabular scenario outcomes with ROI.
   - Columns (exact order): Scenario | Price | Move % | Stock PnL | Option PnL | Option ROI | Net PnL | Net ROI.
   - Highlight row: "Current Market Price" row uses #FEF9C3 background.
   - Data fields: from `analysis_scenario_table`:
     - Scenario label: Spot / Strike / BE / Low / High mapping.
     - Price: `price`.
     - Move %: (price / spot_value - 1) * 100.
     - Stock PnL: `stock_pnl`.
     - Option PnL: `option_pnl`.
     - Option ROI: `option_roi`.
     - Net PnL: `combined_pnl`.
     - Net ROI: `net_roi`.

3) Commentary Blocks (below table)
   - Purpose: readable commentary grouped by key levels.
   - Order: Spot, Strikes (first 4), Breakevens (first 4), Low, High.
   - Content: scenario_table.commentary closest to each price.
   - Layout: label (bold) followed by paragraph text; no table framing.

4) Footer
   - Left: "UBS Financial Services Inc."
   - Right: "Page X of Y"

## Mapping to Existing Outputs
- `analysis_results`: price_grid, pnl, breakevens.
- `analysis_scenario_table`: price, option_pnl, stock_pnl, combined_pnl, option_roi, net_roi, commentary.
- `analysis_summary_payload`: min_pnl, max_pnl, breakevens, pop, margin_proxy, capital_basis.
- Inputs/state: `underlying_ticker`, `resolved_underlying`, `spot_value`, `chain_expiry`, `stock_position`, `avg_cost`, `pricing_mode`, `roi_policy`, `vol_mode`.
- Underlying snapshot: `fetch_underlying_snapshot()` (fields listed above).

## Implementation Notes
- Use `st.container()` as cards with white background, 1 px border (#E5E7EB), rounded 8 px, and 9 pt padding.
- Use a fixed content width equal to page width (8.5 in) with content padding as above.
- Chart annotations should default to ON for strikes and breakevens.
- All missing fields render as "--" (double dash), not blank.
