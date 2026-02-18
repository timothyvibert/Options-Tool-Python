# Calculation Engine Audit Report

Generated: 2026-02-17

## Executive Summary

| Metric | Value |
|--------|-------|
| Strategies tested | 63 |
| Scenarios per strategy | 4 |
| Total runs | 252 |
| Build errors (crash) | 1 |
| Total checks executed | 43693 |
| Checks PASSED | 43693 |
| Checks FAILED | 0 |
| Pass rate | 100.0% |

## Category Summary

| Cat | Category Name | Total | Passed | Failed | Rate |
|-----|--------------|-------|--------|--------|------|
| A | Payoff Grid Integrity | 1986 | 1986 | 0 | 100.0% |
| B | Breakeven Validation | 5237 | 5237 | 0 | 100.0% |
| C | Max Profit / Max Loss | 1255 | 1255 | 0 | 100.0% |
| D | Net Premium & Cost/Credit | 1004 | 1004 | 0 | 100.0% |
| E | Stock P&L | 753 | 753 | 0 | 100.0% |
| F | Cross-Scenario Consistency | 6829 | 6829 | 0 | 100.0% |
| G | Capital Basis & ROI | 1468 | 1468 | 0 | 100.0% |
| H | Key Levels | 2895 | 2895 | 0 | 100.0% |
| I | Pipeline Map Issues | 1004 | 1004 | 0 | 100.0% |
| J | Known Bugs | 21262 | 21262 | 0 | 100.0% |

## Build Errors (analysis_pack crash)

- **Custom Strategy** (ID=1, scenario=options_only)
  `No legs and no stock`

## Failures by Check ID

No failures detected.

## Check ID Statistics

| Check ID | Total | Passed | Failed | Description |
|----------|-------|--------|--------|-------------|
| BE_01 | 251 | 251 | 0 | Breakevens sorted |
| BE_02 | 1662 | 1662 | 0 | Breakevens within grid range |
| BE_03 | 1662 | 1662 | 0 | PnL ≈ 0 at breakeven |
| BE_04 | 1662 | 1662 | 0 | Sign change around breakeven |
| BUG_01 | 251 | 251 | 0 | No division-by-zero crash |
| BUG_02 | 251 | 251 | 0 | All-short capital basis > 0 |
| BUG_03 | 251 | 251 | 0 | Scenario table populated |
| BUG_04 | 251 | 251 | 0 | Sentinel rows present |
| BUG_05 | 251 | 251 | 0 | PoP in [0, 1] |
| BUG_06 | 251 | 251 | 0 | Risk/Reward present |
| BUG_07 | 19756 | 19756 | 0 | No NaN in key level fields |
| CB_01 | 251 | 251 | 0 | Capital basis > 0 |
| CB_02 | 251 | 251 | 0 | Combined basis ≥ option basis |
| CS_01 | 251 | 251 | 0 | Spot in scenario table |
| CS_02 | 480 | 480 | 0 | Strikes in scenario table |
| CS_03 | 1662 | 1662 | 0 | Breakevens in scenario table |
| CS_04 | 1662 | 1662 | 0 | PnL ≈ 0 at breakeven in scenario |
| CS_05 | 2774 | 2774 | 0 | Scenario opt+stk = combined |
| KL_01 | 251 | 251 | 0 | Spot in key levels |
| KL_02 | 480 | 480 | 0 | Strikes in key levels |
| KL_03 | 1662 | 1662 | 0 | Breakevens in key levels |
| KL_04 | 251 | 251 | 0 | Key levels sorted by price |
| KL_05 | 251 | 251 | 0 | Key level IDs unique |
| ML_01 | 251 | 251 | 0 | Options max loss unlimited flag |
| ML_02 | 251 | 251 | 0 | Combined max loss unlimited flag |
| MP_01 | 251 | 251 | 0 | Options max profit unlimited flag |
| MP_02 | 251 | 251 | 0 | Combined max profit unlimited flag |
| MP_03 | 251 | 251 | 0 | Options max profit ≥ 0 |
| NP_01 | 251 | 251 | 0 | Net premium per-share formula |
| NP_02 | 251 | 251 | 0 | Net premium total formula |
| NP_03 | 251 | 251 | 0 | Cost/Credit text matches sign |
| NP_04 | 251 | 251 | 0 | Net Prem/Share present |
| PG_01 | 251 | 251 | 0 | Grid starts at 0 |
| PG_02 | 251 | 251 | 0 | Grid ends at 3×spot |
| PG_03 | 251 | 251 | 0 | Grid monotonically increasing |
| PG_04 | 480 | 480 | 0 | All strikes in grid |
| PG_05 | 251 | 251 | 0 | Grid has ≥300 points |
| PG_06 | 251 | 251 | 0 | PnL array lengths match grid |
| PG_07 | 251 | 251 | 0 | combined = options + stock PnL |
| PI_01 | 251 | 251 | 0 | Stock PnL: direct vs derived |
| PI_02 | 251 | 251 | 0 | PoP was computed |
| PI_03 | 251 | 251 | 0 | Unlimited flags consistent |
| PI_04 | 251 | 251 | 0 | Net premium per share present |
| ROI_01 | 715 | 715 | 0 | ROI values finite |
| ROI_02 | 251 | 251 | 0 | No NaN/Inf in ROI |
| SP_01 | 251 | 251 | 0 | Zero stock → zero stock PnL |
| SP_02 | 251 | 251 | 0 | Stock PnL formula correctness |
| SP_03 | 251 | 251 | 0 | Stock PnL linearity |

## All Failures (Detailed)

No failures.

