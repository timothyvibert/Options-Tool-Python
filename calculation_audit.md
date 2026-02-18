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

## Numerical Results (Fact-Check Data)

Every computed value for each strategy × scenario run.

### Custom Strategy (ID=1) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Payoff:**

- Grid Size: 300 points
- Strikes: []
- Breakevens: [100.0]
- Options Max PnL: 0.0
- Options Min PnL: 0.0
- Combined Max PnL: 20000.0
- Combined Min PnL: -10000.0

**Net Premium:**

- Per Share: 0
- Total: 0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | $0.00 | -$10,000.00 |
| Risk Reward | N/A | 2.00x |
| Capital Basis | $1.00 | $10,001.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 47.9% | 47.9% |
| Margin Proxy | 1.0 | — |

**Probabilities:**

- PoP (raw): 0.47931
- Assignment Prob: 0.0
- P(25% Max Profit): None
- P(50% Max Profit): None
- P(100% Max Profit): None
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.1500 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 0.00 | 1500.00 | 1500.00 | 0.0000 | 0.1500 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -10000.00 | -0.9999 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | -1500.00 | -0.1500 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 1500.00 | 0.1500 |
| infinity | Stock to Infinity | — | — | 0.00 | 90000.00 | 8.9991 |

---

### Custom Strategy (ID=1) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Payoff:**

- Grid Size: 300 points
- Strikes: []
- Breakevens: [50.0]
- Options Max PnL: 0.0
- Options Min PnL: 0.0
- Combined Max PnL: 25000.0
- Combined Min PnL: -5000.0

**Net Premium:**

- Per Share: 0
- Total: 0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | $0.00 | -$5,000.00 |
| Risk Reward | N/A | 5.00x |
| Capital Basis | $1.00 | $5,001.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 1.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.0
- P(25% Max Profit): None
- P(50% Max Profit): None
- P(100% Max Profit): None
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 85.00 | Downside (15%) | 0.00 | 3500.00 | 3500.00 | 0.0000 | 0.6999 |
| 100.00 | Current Market Price | 0.00 | 5000.00 | 5000.00 | 0.0000 | 0.9998 |
| 115.00 | Upside (15%) | 0.00 | 6500.00 | 6500.00 | 0.0000 | 1.2997 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -5000.00 | -0.9998 |
| breakeven_1 | Breakeven 1 | 50.00 | -50.00% | 0.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | 3500.00 | 0.6999 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 0.9998 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 6500.00 | 1.2997 |
| infinity | Stock to Infinity | — | — | 0.00 | 95000.00 | 18.9962 |

---

### Custom Strategy (ID=1) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Payoff:**

- Grid Size: 300 points
- Strikes: []
- Breakevens: [115.0]
- Options Max PnL: 0.0
- Options Min PnL: 0.0
- Combined Max PnL: 18500.0
- Combined Min PnL: -11500.0

**Net Premium:**

- Per Share: 0
- Total: 0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | $0.00 | -$11,500.00 |
| Risk Reward | N/A | 1.61x |
| Capital Basis | $1.00 | $11,501.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 8.1% | 8.1% |
| Margin Proxy | 1.0 | — |

**Probabilities:**

- PoP (raw): 0.081123
- Assignment Prob: 0.0
- P(25% Max Profit): None
- P(50% Max Profit): None
- P(100% Max Profit): None
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 0.00 | -3000.00 | -3000.00 | 0.0000 | -0.2608 |
| 100.00 | Current Market Price | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.1304 |
| 115.00 | Upside (15%) | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -11500.00 | -0.9999 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | -3000.00 | -0.2608 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.1304 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 115.00 | 15.00% | 0.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 0.00 | 88500.00 | 7.6950 |

---

### Long Stock (ID=2) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Payoff:**

- Grid Size: 300 points
- Strikes: []
- Breakevens: [100.0]
- Options Max PnL: 0.0
- Options Min PnL: 0.0
- Combined Max PnL: 20000.0
- Combined Min PnL: -10000.0

**Net Premium:**

- Per Share: 0
- Total: 0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | $0.00 | -$10,000.00 |
| Risk Reward | N/A | 2.00x |
| Capital Basis | $1.00 | $10,001.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 47.9% | 47.9% |
| Margin Proxy | 1.0 | — |

**Probabilities:**

- PoP (raw): 0.47931
- Assignment Prob: 0.0
- P(25% Max Profit): None
- P(50% Max Profit): None
- P(100% Max Profit): None
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.1500 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 0.00 | 1500.00 | 1500.00 | 0.0000 | 0.1500 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -10000.00 | -0.9999 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | -1500.00 | -0.1500 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 1500.00 | 0.1500 |
| infinity | Stock to Infinity | — | — | 0.00 | 90000.00 | 8.9991 |

---

### Long Stock (ID=2) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Payoff:**

- Grid Size: 300 points
- Strikes: []
- Breakevens: [100.0]
- Options Max PnL: 0.0
- Options Min PnL: 0.0
- Combined Max PnL: 20000.0
- Combined Min PnL: -10000.0

**Net Premium:**

- Per Share: 0
- Total: 0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | $0.00 | -$10,000.00 |
| Risk Reward | N/A | 2.00x |
| Capital Basis | $1.00 | $10,001.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 47.9% | 47.9% |
| Margin Proxy | 1.0 | — |

**Probabilities:**

- PoP (raw): 0.47931
- Assignment Prob: 0.0
- P(25% Max Profit): None
- P(50% Max Profit): None
- P(100% Max Profit): None
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.1500 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 0.00 | 1500.00 | 1500.00 | 0.0000 | 0.1500 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -10000.00 | -0.9999 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | -1500.00 | -0.1500 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 1500.00 | 0.1500 |
| infinity | Stock to Infinity | — | — | 0.00 | 90000.00 | 8.9991 |

---

### Long Stock (ID=2) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Payoff:**

- Grid Size: 300 points
- Strikes: []
- Breakevens: [50.0]
- Options Max PnL: 0.0
- Options Min PnL: 0.0
- Combined Max PnL: 25000.0
- Combined Min PnL: -5000.0

**Net Premium:**

- Per Share: 0
- Total: 0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | $0.00 | -$5,000.00 |
| Risk Reward | N/A | 5.00x |
| Capital Basis | $1.00 | $5,001.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 1.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.0
- P(25% Max Profit): None
- P(50% Max Profit): None
- P(100% Max Profit): None
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 85.00 | Downside (15%) | 0.00 | 3500.00 | 3500.00 | 0.0000 | 0.6999 |
| 100.00 | Current Market Price | 0.00 | 5000.00 | 5000.00 | 0.0000 | 0.9998 |
| 115.00 | Upside (15%) | 0.00 | 6500.00 | 6500.00 | 0.0000 | 1.2997 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -5000.00 | -0.9998 |
| breakeven_1 | Breakeven 1 | 50.00 | -50.00% | 0.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | 3500.00 | 0.6999 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 0.9998 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 6500.00 | 1.2997 |
| infinity | Stock to Infinity | — | — | 0.00 | 95000.00 | 18.9962 |

---

### Long Stock (ID=2) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Payoff:**

- Grid Size: 300 points
- Strikes: []
- Breakevens: [115.0]
- Options Max PnL: 0.0
- Options Min PnL: 0.0
- Combined Max PnL: 18500.0
- Combined Min PnL: -11500.0

**Net Premium:**

- Per Share: 0
- Total: 0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | $0.00 | -$11,500.00 |
| Risk Reward | N/A | 1.61x |
| Capital Basis | $1.00 | $11,501.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 8.1% | 8.1% |
| Margin Proxy | 1.0 | — |

**Probabilities:**

- PoP (raw): 0.081123
- Assignment Prob: 0.0
- P(25% Max Profit): None
- P(50% Max Profit): None
- P(100% Max Profit): None
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 0.00 | -3000.00 | -3000.00 | 0.0000 | -0.2608 |
| 100.00 | Current Market Price | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.1304 |
| 115.00 | Upside (15%) | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -11500.00 | -0.9999 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | -3000.00 | -0.2608 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.1304 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 115.00 | 15.00% | 0.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 0.00 | 88500.00 | 7.6950 |

---

### Short Stock (ID=3) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 100.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Payoff:**

- Grid Size: 300 points
- Strikes: []
- Breakevens: [100.0]
- Options Max PnL: 0.0
- Options Min PnL: 0.0
- Combined Max PnL: 10000.0
- Combined Min PnL: -20000.0

**Net Premium:**

- Per Share: 0
- Total: 0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | $10,000.00 |
| Max Loss | $0.00 | Unlimited |
| Risk Reward | N/A | 0.50x |
| Capital Basis | $1.00 | $10,001.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 52.1% | 52.1% |
| Margin Proxy | 1.0 | — |

**Probabilities:**

- PoP (raw): 0.52069
- Assignment Prob: 0.0
- P(25% Max Profit): None
- P(50% Max Profit): None
- P(100% Max Profit): None
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 0.00 | 1500.00 | 1500.00 | 0.0000 | 0.1500 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.1500 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | 10000.00 | 0.9999 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | 1500.00 | 0.1500 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | -1500.00 | -0.1500 |
| infinity | Stock to Infinity | — | — | 0.00 | -90000.00 | -8.9991 |

---

### Short Stock (ID=3) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 100.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Payoff:**

- Grid Size: 300 points
- Strikes: []
- Breakevens: [100.0]
- Options Max PnL: 0.0
- Options Min PnL: 0.0
- Combined Max PnL: 10000.0
- Combined Min PnL: -20000.0

**Net Premium:**

- Per Share: 0
- Total: 0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | $10,000.00 |
| Max Loss | $0.00 | Unlimited |
| Risk Reward | N/A | 0.50x |
| Capital Basis | $1.00 | $10,001.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 52.1% | 52.1% |
| Margin Proxy | 1.0 | — |

**Probabilities:**

- PoP (raw): 0.52069
- Assignment Prob: 0.0
- P(25% Max Profit): None
- P(50% Max Profit): None
- P(100% Max Profit): None
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 0.00 | 1500.00 | 1500.00 | 0.0000 | 0.1500 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.1500 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | 10000.00 | 0.9999 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | 1500.00 | 0.1500 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | -1500.00 | -0.1500 |
| infinity | Stock to Infinity | — | — | 0.00 | -90000.00 | -8.9991 |

---

### Short Stock (ID=3) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 50.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Payoff:**

- Grid Size: 300 points
- Strikes: []
- Breakevens: [50.0]
- Options Max PnL: 0.0
- Options Min PnL: 0.0
- Combined Max PnL: 5000.0
- Combined Min PnL: -25000.0

**Net Premium:**

- Per Share: 0
- Total: 0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | $5,000.00 |
| Max Loss | $0.00 | Unlimited |
| Risk Reward | N/A | 0.20x |
| Capital Basis | $1.00 | $5,001.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 1.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.0
- P(25% Max Profit): None
- P(50% Max Profit): None
- P(100% Max Profit): None
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 85.00 | Downside (15%) | 0.00 | -3500.00 | -3500.00 | 0.0000 | -0.6999 |
| 100.00 | Current Market Price | 0.00 | -5000.00 | -5000.00 | 0.0000 | -0.9998 |
| 115.00 | Upside (15%) | 0.00 | -6500.00 | -6500.00 | 0.0000 | -1.2997 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | 5000.00 | 0.9998 |
| breakeven_1 | Breakeven 1 | 50.00 | -50.00% | 0.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | -3500.00 | -0.6999 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | -5000.00 | -0.9998 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | -6500.00 | -1.2997 |
| infinity | Stock to Infinity | — | — | 0.00 | -95000.00 | -18.9962 |

---

### Short Stock (ID=3) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 114.99999999999999
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Payoff:**

- Grid Size: 300 points
- Strikes: []
- Breakevens: [115.0]
- Options Max PnL: 0.0
- Options Min PnL: 0.0
- Combined Max PnL: 11500.0
- Combined Min PnL: -18500.0

**Net Premium:**

- Per Share: 0
- Total: 0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | $11,500.00 |
| Max Loss | $0.00 | Unlimited |
| Risk Reward | N/A | 0.62x |
| Capital Basis | $1.00 | $11,501.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 91.9% | 91.9% |
| Margin Proxy | 1.0 | — |

**Probabilities:**

- PoP (raw): 0.918877
- Assignment Prob: 0.0
- P(25% Max Profit): None
- P(50% Max Profit): None
- P(100% Max Profit): None
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 0.00 | 3000.00 | 3000.00 | 0.0000 | 0.2608 |
| 100.00 | Current Market Price | 0.00 | 1500.00 | 1500.00 | 0.0000 | 0.1304 |
| 115.00 | Upside (15%) | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 0.00 | -0.00 | -0.00 | 0.0000 | -0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | 11500.00 | 0.9999 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | 3000.00 | 0.2608 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 1500.00 | 0.1304 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 115.00 | 15.00% | 0.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 0.00 | -88500.00 | -7.6950 |

---

### Long Call (ID=4) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [102.5]
- Options Max PnL: 19750.0
- Options Min PnL: -250.0
- Combined Max PnL: 19750.0
- Combined Min PnL: -250.0

**Net Premium:**

- Per Share: 2.5
- Total: 250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$250.00 | -$250.00 |
| Risk Reward | 79.00x | 79.00x |
| Capital Basis | $250.00 | $250.00 |
| Cost Credit | Debit $250.00 | Debit $250.00 |
| Pop | 38.6% | 38.6% |
| Margin Proxy | 250.0 | — |

**Probabilities:**

- PoP (raw): 0.386034
- Assignment Prob: 0.0
- P(25% Max Profit): 2.3e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -250.00 | 0.00 | -250.00 | -1.0000 | -1.0000 |
| 100.00 | Current Market Price | -250.00 | 0.00 | -250.00 | -1.0000 | -1.0000 |
| 102.50 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 1250.00 | 0.00 | 1250.00 | 5.0000 | 5.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -250.00 | -250.00 | -1.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -250.00 | -250.00 | -1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -1.0000 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -1.0000 |
| breakeven_1 | Breakeven 1 | 102.50 | 2.50% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1250.00 | 1250.00 | 5.0000 |
| infinity | Stock to Infinity | — | — | 89750.00 | 89750.00 | 359.0000 |

---

### Long Call (ID=4) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [101.25]
- Options Max PnL: 19750.0
- Options Min PnL: -250.0
- Combined Max PnL: 39750.0
- Combined Min PnL: -10250.0

**Net Premium:**

- Per Share: 2.5
- Total: 250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$250.00 | -$10,250.00 |
| Risk Reward | 79.00x | 3.88x |
| Capital Basis | $250.00 | $10,250.00 |
| Cost Credit | Debit $250.00 | Debit $250.00 |
| Pop | 43.2% | 43.2% |
| Margin Proxy | 250.0 | — |

**Probabilities:**

- PoP (raw): 0.431901
- Assignment Prob: 0.0
- P(25% Max Profit): 2.3e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -250.00 | -1500.00 | -1750.00 | -1.0000 | -0.1707 |
| 100.00 | Current Market Price | -250.00 | 0.00 | -250.00 | -1.0000 | -0.0244 |
| 101.25 | Breakeven 1 | -125.00 | 125.00 | 0.00 | -0.5000 | 0.0000 |
| 115.00 | Upside (15%) | 1250.00 | 1500.00 | 2750.00 | 5.0000 | 0.2683 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -250.00 | -10250.00 | -1.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -250.00 | -1750.00 | -0.1707 |
| spot | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -0.0244 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -0.0244 |
| breakeven_1 | Breakeven 1 | 101.25 | 1.25% | -125.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1250.00 | 2750.00 | 0.2683 |
| infinity | Stock to Infinity | — | — | 89750.00 | 179750.00 | 17.5366 |

---

### Long Call (ID=4) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [52.5]
- Options Max PnL: 19750.0
- Options Min PnL: -250.0
- Combined Max PnL: 44750.0
- Combined Min PnL: -5250.0

**Net Premium:**

- Per Share: 2.5
- Total: 250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$250.00 | -$5,250.00 |
| Risk Reward | 79.00x | 8.52x |
| Capital Basis | $250.00 | $5,250.00 |
| Cost Credit | Debit $250.00 | Debit $250.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 250.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.0
- P(25% Max Profit): 2.3e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -250.00 | 0.00 | -250.00 | -1.0000 | -0.0476 |
| 52.50 | Breakeven 1 | -250.00 | 250.00 | 0.00 | -1.0000 | 0.0000 |
| 85.00 | Downside (15%) | -250.00 | 3500.00 | 3250.00 | -1.0000 | 0.6190 |
| 100.00 | Current Market Price | -250.00 | 5000.00 | 4750.00 | -1.0000 | 0.9048 |
| 115.00 | Upside (15%) | 1250.00 | 6500.00 | 7750.00 | 5.0000 | 1.4762 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -250.00 | -5250.00 | -1.0000 |
| breakeven_1 | Breakeven 1 | 52.50 | -47.50% | -250.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -250.00 | 3250.00 | 0.6190 |
| spot | Current Market Price | 100.00 | 0.00% | -250.00 | 4750.00 | 0.9048 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -250.00 | 4750.00 | 0.9048 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1250.00 | 7750.00 | 1.4762 |
| infinity | Stock to Infinity | — | — | 89750.00 | 184750.00 | 35.1905 |

---

### Long Call (ID=4) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [108.75]
- Options Max PnL: 19750.0
- Options Min PnL: -250.0
- Combined Max PnL: 38250.0
- Combined Min PnL: -11750.0

**Net Premium:**

- Per Share: 2.5
- Total: 250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$250.00 | -$11,750.00 |
| Risk Reward | 79.00x | 3.26x |
| Capital Basis | $250.00 | $11,750.00 |
| Cost Credit | Debit $250.00 | Debit $250.00 |
| Pop | 19.5% | 19.5% |
| Margin Proxy | 250.0 | — |

**Probabilities:**

- PoP (raw): 0.195021
- Assignment Prob: 0.0
- P(25% Max Profit): 2.3e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -250.00 | -3000.00 | -3250.00 | -1.0000 | -0.2766 |
| 100.00 | Current Market Price | -250.00 | -1500.00 | -1750.00 | -1.0000 | -0.1489 |
| 108.75 | Breakeven 1 | 625.00 | -625.00 | 0.00 | 2.5000 | 0.0000 |
| 115.00 | Upside (15%) | 1250.00 | 0.00 | 1250.00 | 5.0000 | 0.1064 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -250.00 | -11750.00 | -1.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -250.00 | -3250.00 | -0.2766 |
| spot | Current Market Price | 100.00 | 0.00% | -250.00 | -1750.00 | -0.1489 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -250.00 | -1750.00 | -0.1489 |
| breakeven_1 | Breakeven 1 | 108.75 | 8.75% | 625.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1250.00 | 1250.00 | 0.1064 |
| infinity | Stock to Infinity | — | — | 89750.00 | 178250.00 | 15.1702 |

---

### Short Call (ID=5) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [102.5]
- Options Max PnL: 250.0
- Options Min PnL: -19750.0
- Combined Max PnL: 250.0
- Combined Min PnL: -19750.0

**Net Premium:**

- Per Share: -2.5
- Total: -250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $250.00 | $250.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.01x | 0.01x |
| Capital Basis | $2,250.00 | $2,250.00 |
| Cost Credit | Credit $250.00 | Credit $250.00 |
| Pop | 61.4% | 61.4% |
| Margin Proxy | 2250.0 | — |

**Probabilities:**

- PoP (raw): 0.613966
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.59126
- P(50% Max Profit): 0.568099
- P(100% Max Profit): 0.521668
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 250.00 | 0.00 | 250.00 | 0.1111 | 0.1111 |
| 100.00 | Current Market Price | 250.00 | 0.00 | 250.00 | 0.1111 | 0.1111 |
| 102.50 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -1250.00 | 0.00 | -1250.00 | -0.5556 | -0.5556 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 250.00 | 250.00 | 0.1111 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 250.00 | 250.00 | 0.1111 |
| spot | Current Market Price | 100.00 | 0.00% | 250.00 | 250.00 | 0.1111 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 250.00 | 250.00 | 0.1111 |
| breakeven_1 | Breakeven 1 | 102.50 | 2.50% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1250.00 | -1250.00 | -0.5556 |
| infinity | Stock to Infinity | — | — | Unlimited | -89750.00 | -39.8889 |

---

### Short Call (ID=5) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [97.5]
- Options Max PnL: 250.0
- Options Min PnL: -19750.0
- Combined Max PnL: 250.0
- Combined Min PnL: -9750.0

**Net Premium:**

- Per Share: -2.5
- Total: -250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $250.00 | $250.00 |
| Max Loss | Unlimited | -$9,750.00 |
| Risk Reward | 0.01x | 0.03x |
| Capital Basis | $5,000.00 | $15,000.00 |
| Cost Credit | Credit $250.00 | Credit $250.00 |
| Pop | 57.6% | 57.6% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 0.576062
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.59126
- P(50% Max Profit): 0.568099
- P(100% Max Profit): 0.521668
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 250.00 | -1500.00 | -1250.00 | 0.0500 | -0.0833 |
| 97.50 | Breakeven 1 | 250.00 | -250.00 | 0.00 | 0.0500 | 0.0000 |
| 100.00 | Current Market Price | 250.00 | 0.00 | 250.00 | 0.0500 | 0.0167 |
| 115.00 | Upside (15%) | -1250.00 | 1500.00 | 250.00 | -0.2500 | 0.0167 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 250.00 | -9750.00 | -0.6500 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 250.00 | -1250.00 | -0.0833 |
| breakeven_1 | Breakeven 1 | 97.50 | -2.50% | 250.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 250.00 | 250.00 | 0.0167 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 250.00 | 250.00 | 0.0167 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1250.00 | 250.00 | 0.0167 |
| infinity | Stock to Infinity | — | — | Unlimited | 250.00 | 0.0167 |

---

### Short Call (ID=5) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [47.5]
- Options Max PnL: 250.0
- Options Min PnL: -19750.0
- Combined Max PnL: 5250.0
- Combined Min PnL: -4750.0

**Net Premium:**

- Per Share: -2.5
- Total: -250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $250.00 | $5,250.00 |
| Max Loss | Unlimited | -$4,750.00 |
| Risk Reward | 0.01x | 1.11x |
| Capital Basis | $5,000.00 | $10,000.00 |
| Cost Credit | Credit $250.00 | Credit $250.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.59126
- P(50% Max Profit): 0.568099
- P(100% Max Profit): 0.521668
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 47.50 | Breakeven 1 | 250.00 | -250.00 | 0.00 | 0.0500 | 0.0000 |
| 50.00 | Scenario @ 50.00 | 250.00 | 0.00 | 250.00 | 0.0500 | 0.0250 |
| 85.00 | Downside (15%) | 250.00 | 3500.00 | 3750.00 | 0.0500 | 0.3750 |
| 100.00 | Current Market Price | 250.00 | 5000.00 | 5250.00 | 0.0500 | 0.5250 |
| 115.00 | Upside (15%) | -1250.00 | 6500.00 | 5250.00 | -0.2500 | 0.5250 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 250.00 | -4750.00 | -0.4750 |
| breakeven_1 | Breakeven 1 | 47.50 | -52.50% | 250.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 250.00 | 3750.00 | 0.3750 |
| spot | Current Market Price | 100.00 | 0.00% | 250.00 | 5250.00 | 0.5250 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 250.00 | 5250.00 | 0.5250 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1250.00 | 5250.00 | 0.5250 |
| infinity | Stock to Infinity | — | — | Unlimited | 5250.00 | 0.5250 |

---

### Short Call (ID=5) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: []
- Options Max PnL: 250.0
- Options Min PnL: -19750.0
- Combined Max PnL: -1250.0
- Combined Min PnL: -11250.0

**Net Premium:**

- Per Share: -2.5
- Total: -250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $250.00 | -$1,250.00 |
| Max Loss | Unlimited | -$11,250.00 |
| Risk Reward | 0.01x | 0.11x |
| Capital Basis | $5,000.00 | $16,500.00 |
| Cost Credit | Credit $250.00 | Credit $250.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.59126
- P(50% Max Profit): 0.568099
- P(100% Max Profit): 0.521668
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 250.00 | -3000.00 | -2750.00 | 0.0500 | -0.1667 |
| 100.00 | Current Market Price | 250.00 | -1500.00 | -1250.00 | 0.0500 | -0.0758 |
| 115.00 | Upside (15%) | -1250.00 | 0.00 | -1250.00 | -0.2500 | -0.0758 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 250.00 | -11250.00 | -0.6818 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 250.00 | -2750.00 | -0.1667 |
| spot | Current Market Price | 100.00 | 0.00% | 250.00 | -1250.00 | -0.0758 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 250.00 | -1250.00 | -0.0758 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1250.00 | -1250.00 | -0.0758 |
| infinity | Stock to Infinity | — | — | Unlimited | -1250.00 | -0.0758 |

---

### Long Put (ID=6) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [97.5]
- Options Max PnL: 9750.0
- Options Min PnL: -250.0
- Combined Max PnL: 9750.0
- Combined Min PnL: -250.0

**Net Premium:**

- Per Share: 2.5
- Total: 250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $9,750.00 | $9,750.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 39.00x | 39.00x |
| Capital Basis | $250.00 | $250.00 |
| Cost Credit | Debit $250.00 | Debit $250.00 |
| Pop | 42.4% | 42.4% |
| Margin Proxy | 250.0 | — |

**Probabilities:**

- PoP (raw): 0.423938
- Assignment Prob: 0.0
- P(25% Max Profit): 0.001529
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1250.00 | 0.00 | 1250.00 | 5.0000 | 5.0000 |
| 97.50 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | -250.00 | 0.00 | -250.00 | -1.0000 | -1.0000 |
| 115.00 | Upside (15%) | -250.00 | 0.00 | -250.00 | -1.0000 | -1.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9750.00 | 9750.00 | 39.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1250.00 | 1250.00 | 5.0000 |
| breakeven_1 | Breakeven 1 | 97.50 | -2.50% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -1.0000 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -1.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -250.00 | -250.00 | -1.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | -250.00 | -1.0000 |

---

### Long Put (ID=6) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: PPRT
- Margin Classification: PPRT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [102.5]
- Options Max PnL: 9750.0
- Options Min PnL: -250.0
- Combined Max PnL: 19750.0
- Combined Min PnL: -250.0

**Net Premium:**

- Per Share: 2.5
- Total: 250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $9,750.00 | Unlimited |
| Max Loss | Unlimited | -$250.00 |
| Risk Reward | 39.00x | 79.00x |
| Capital Basis | $5,250.00 | $15,250.00 |
| Cost Credit | Debit $250.00 | Debit $250.00 |
| Pop | 38.6% | 38.6% |
| Margin Proxy | 5250.0 | — |

**Probabilities:**

- PoP (raw): 0.386034
- Assignment Prob: 0.0
- P(25% Max Profit): 0.001529
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1250.00 | -1500.00 | -250.00 | 5.0000 | -0.0244 |
| 100.00 | Current Market Price | -250.00 | 0.00 | -250.00 | -1.0000 | -0.0244 |
| 102.50 | Breakeven 1 | -250.00 | 250.00 | 0.00 | -1.0000 | 0.0000 |
| 115.00 | Upside (15%) | -250.00 | 1500.00 | 1250.00 | -1.0000 | 0.1220 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9750.00 | -250.00 | -0.0164 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1250.00 | -250.00 | -0.0244 |
| spot | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -0.0244 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -0.0244 |
| breakeven_1 | Breakeven 1 | 102.50 | 2.50% | -250.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -250.00 | 1250.00 | 0.1220 |
| infinity | Stock to Infinity | — | — | Unlimited | 89750.00 | 5.8852 |

---

### Long Put (ID=6) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: PPRT
- Margin Classification: PPRT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: []
- Options Max PnL: 9750.0
- Options Min PnL: -250.0
- Combined Max PnL: 24750.0
- Combined Min PnL: 4750.0

**Net Premium:**

- Per Share: 2.5
- Total: 250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $9,750.00 | Unlimited |
| Max Loss | Unlimited | $4,750.00 |
| Risk Reward | 39.00x | 5.21x |
| Capital Basis | $5,250.00 | $10,250.00 |
| Cost Credit | Debit $250.00 | Debit $250.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 5250.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.0
- P(25% Max Profit): 0.001529
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | 4750.00 | 0.00 | 4750.00 | 19.0000 | 0.9048 |
| 85.00 | Downside (15%) | 1250.00 | 3500.00 | 4750.00 | 5.0000 | 0.9048 |
| 100.00 | Current Market Price | -250.00 | 5000.00 | 4750.00 | -1.0000 | 0.9048 |
| 115.00 | Upside (15%) | -250.00 | 6500.00 | 6250.00 | -1.0000 | 1.1905 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9750.00 | 4750.00 | 0.4634 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1250.00 | 4750.00 | 0.9048 |
| spot | Current Market Price | 100.00 | 0.00% | -250.00 | 4750.00 | 0.9048 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -250.00 | 4750.00 | 0.9048 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -250.00 | 6250.00 | 1.1905 |
| infinity | Stock to Infinity | — | — | Unlimited | 94750.00 | 9.2439 |

---

### Long Put (ID=6) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: PPRT
- Margin Classification: PPRT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [117.5]
- Options Max PnL: 9750.0
- Options Min PnL: -250.0
- Combined Max PnL: 18250.0
- Combined Min PnL: -1750.0

**Net Premium:**

- Per Share: 2.5
- Total: 250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $9,750.00 | Unlimited |
| Max Loss | Unlimited | -$1,750.00 |
| Risk Reward | 39.00x | 10.43x |
| Capital Basis | $5,250.00 | $16,750.00 |
| Cost Credit | Debit $250.00 | Debit $250.00 |
| Pop | 5.4% | 5.4% |
| Margin Proxy | 5250.0 | — |

**Probabilities:**

- PoP (raw): 0.054289
- Assignment Prob: 0.0
- P(25% Max Profit): 0.001529
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1250.00 | -3000.00 | -1750.00 | 5.0000 | -0.1489 |
| 100.00 | Current Market Price | -250.00 | -1500.00 | -1750.00 | -1.0000 | -0.1489 |
| 115.00 | Upside (15%) | -250.00 | 0.00 | -250.00 | -1.0000 | -0.0213 |
| 117.50 | Breakeven 1 | -250.00 | 250.00 | 0.00 | -1.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9750.00 | -1750.00 | -0.1045 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1250.00 | -1750.00 | -0.1489 |
| spot | Current Market Price | 100.00 | 0.00% | -250.00 | -1750.00 | -0.1489 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -250.00 | -1750.00 | -0.1489 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -250.00 | -250.00 | -0.0213 |
| breakeven_1 | Breakeven 1 | 117.50 | 17.50% | -250.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | 88250.00 | 5.2687 |

---

### Short Put (ID=7) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: CSPT
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [97.5]
- Options Max PnL: 250.0
- Options Min PnL: -9750.0
- Combined Max PnL: 250.0
- Combined Min PnL: -9750.0

**Net Premium:**

- Per Share: -2.5
- Total: -250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $250.00 | $250.00 |
| Max Loss | -$9,750.00 | -$9,750.00 |
| Risk Reward | 0.03x | 0.03x |
| Capital Basis | $10,000.00 | $10,000.00 |
| Cost Credit | Credit $250.00 | Credit $250.00 |
| Pop | 57.6% | 57.6% |
| Margin Proxy | 2250.0 | — |

**Probabilities:**

- PoP (raw): 0.576062
- Assignment Prob: 0.520709
- P(25% Max Profit): 0.551838
- P(50% Max Profit): 0.527575
- P(100% Max Profit): 0.480251
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1250.00 | 0.00 | -1250.00 | -0.1282 | -0.1282 |
| 97.50 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | 250.00 | 0.00 | 250.00 | 0.0256 | 0.0256 |
| 115.00 | Upside (15%) | 250.00 | 0.00 | 250.00 | 0.0256 | 0.0256 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9750.00 | -9750.00 | -0.9750 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1250.00 | -1250.00 | -0.1282 |
| breakeven_1 | Breakeven 1 | 97.50 | -2.50% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 250.00 | 250.00 | 0.0256 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 250.00 | 250.00 | 0.0256 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 250.00 | 250.00 | 0.0256 |
| infinity | Stock to Infinity | — | — | 250.00 | 250.00 | 0.0250 |

---

### Short Put (ID=7) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [98.75]
- Options Max PnL: 250.0
- Options Min PnL: -9750.0
- Combined Max PnL: 20250.0
- Combined Min PnL: -19750.0

**Net Premium:**

- Per Share: -2.5
- Total: -250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $250.00 | Unlimited |
| Max Loss | -$9,750.00 | -$19,750.00 |
| Risk Reward | 0.03x | 1.03x |
| Capital Basis | $2,250.00 | $12,250.00 |
| Cost Credit | Credit $250.00 | Credit $250.00 |
| Pop | 52.8% | 52.8% |
| Margin Proxy | 2250.0 | — |

**Probabilities:**

- PoP (raw): 0.527575
- Assignment Prob: 0.520709
- P(25% Max Profit): 0.551838
- P(50% Max Profit): 0.527575
- P(100% Max Profit): 0.480251
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1250.00 | -1500.00 | -2750.00 | -0.1282 | -0.1392 |
| 98.75 | Breakeven 1 | 125.00 | -125.00 | 0.00 | 0.0128 | 0.0000 |
| 100.00 | Current Market Price | 250.00 | 0.00 | 250.00 | 0.0256 | 0.0127 |
| 115.00 | Upside (15%) | 250.00 | 1500.00 | 1750.00 | 0.0256 | 0.0886 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9750.00 | -19750.00 | -1.6122 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1250.00 | -2750.00 | -0.1392 |
| breakeven_1 | Breakeven 1 | 98.75 | -1.25% | 125.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 250.00 | 250.00 | 0.0127 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 250.00 | 250.00 | 0.0127 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 250.00 | 1750.00 | 0.0886 |
| infinity | Stock to Infinity | — | — | 250.00 | 90250.00 | 7.3673 |

---

### Short Put (ID=7) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [73.75]
- Options Max PnL: 250.0
- Options Min PnL: -9750.0
- Combined Max PnL: 25250.0
- Combined Min PnL: -14750.0

**Net Premium:**

- Per Share: -2.5
- Total: -250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $250.00 | Unlimited |
| Max Loss | -$9,750.00 | -$14,750.00 |
| Risk Reward | 0.03x | 1.71x |
| Capital Basis | $2,250.00 | $7,250.00 |
| Cost Credit | Credit $250.00 | Credit $250.00 |
| Pop | 99.8% | 99.8% |
| Margin Proxy | 2250.0 | — |

**Probabilities:**

- PoP (raw): 0.99801
- Assignment Prob: 0.520709
- P(25% Max Profit): 0.551838
- P(50% Max Profit): 0.527575
- P(100% Max Profit): 0.480251
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -4750.00 | 0.00 | -4750.00 | -0.4872 | -0.3220 |
| 73.75 | Breakeven 1 | -2375.00 | 2375.00 | 0.00 | -0.2436 | 0.0000 |
| 85.00 | Downside (15%) | -1250.00 | 3500.00 | 2250.00 | -0.1282 | 0.1525 |
| 100.00 | Current Market Price | 250.00 | 5000.00 | 5250.00 | 0.0256 | 0.3559 |
| 115.00 | Upside (15%) | 250.00 | 6500.00 | 6750.00 | 0.0256 | 0.4576 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9750.00 | -14750.00 | -2.0345 |
| breakeven_1 | Breakeven 1 | 73.75 | -26.25% | -2375.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1250.00 | 2250.00 | 0.1525 |
| spot | Current Market Price | 100.00 | 0.00% | 250.00 | 5250.00 | 0.3559 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 250.00 | 5250.00 | 0.3559 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 250.00 | 6750.00 | 0.4576 |
| infinity | Stock to Infinity | — | — | 250.00 | 95250.00 | 13.1379 |

---

### Short Put (ID=7) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [112.5]
- Options Max PnL: 250.0
- Options Min PnL: -9750.0
- Combined Max PnL: 18750.0
- Combined Min PnL: -21250.0

**Net Premium:**

- Per Share: -2.5
- Total: -250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $250.00 | Unlimited |
| Max Loss | -$9,750.00 | -$21,250.00 |
| Risk Reward | 0.03x | 0.88x |
| Capital Basis | $2,250.00 | $13,750.00 |
| Cost Credit | Credit $250.00 | Credit $250.00 |
| Pop | 11.8% | 11.8% |
| Margin Proxy | 2250.0 | — |

**Probabilities:**

- PoP (raw): 0.117822
- Assignment Prob: 0.520709
- P(25% Max Profit): 0.551838
- P(50% Max Profit): 0.527575
- P(100% Max Profit): 0.480251
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1250.00 | -3000.00 | -4250.00 | -0.1282 | -0.2000 |
| 100.00 | Current Market Price | 250.00 | -1500.00 | -1250.00 | 0.0256 | -0.0588 |
| 112.50 | Breakeven 1 | 250.00 | -250.00 | 0.00 | 0.0256 | 0.0000 |
| 115.00 | Upside (15%) | 250.00 | 0.00 | 250.00 | 0.0256 | 0.0118 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9750.00 | -21250.00 | -1.5455 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1250.00 | -4250.00 | -0.2000 |
| spot | Current Market Price | 100.00 | 0.00% | 250.00 | -1250.00 | -0.0588 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 250.00 | -1250.00 | -0.0588 |
| breakeven_1 | Breakeven 1 | 112.50 | 12.50% | 250.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 250.00 | 250.00 | 0.0118 |
| infinity | Stock to Infinity | — | — | 250.00 | 88750.00 | 6.4545 |

---

### Covered Call (ID=8) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [108.0]
- Breakevens: [98.1]
- Options Max PnL: 190.0
- Options Min PnL: -19010.0
- Combined Max PnL: 990.0
- Combined Min PnL: -9810.0

**Net Premium:**

- Per Share: -1.9
- Total: -190.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $190.00 | $990.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.01x | 0.10x |
| Capital Basis | $5,000.00 | $15,000.00 |
| Cost Credit | Credit $190.00 | Credit $190.00 |
| Pop | 55.3% | 55.3% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 0.552808
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.820983
- P(50% Max Profit): 0.80982
- P(100% Max Profit): 0.786579
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 190.00 | -1500.00 | -1310.00 | 0.0380 | -0.0873 |
| 98.10 | Breakeven 1 | 190.00 | -190.00 | -0.00 | 0.0380 | -0.0000 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0380 | 0.0127 |
| 108.00 | Strike | 190.00 | 800.00 | 990.00 | 0.0380 | 0.0660 |
| 115.00 | Upside (15%) | -510.00 | 1500.00 | 990.00 | -0.1020 | 0.0660 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 190.00 | -9810.00 | -0.6540 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 190.00 | -1310.00 | -0.0873 |
| breakeven_1 | Breakeven 1 | 98.10 | -1.90% | 190.00 | -0.00 | -0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0127 |
| strike_1 | Strike | 108.00 | 8.00% | 190.00 | 990.00 | 0.0660 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -510.00 | 990.00 | 0.0660 |
| infinity | Stock to Infinity | — | — | Unlimited | 990.00 | 0.0660 |

---

### Covered Call (ID=8) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [108.0]
- Breakevens: [98.1]
- Options Max PnL: 190.0
- Options Min PnL: -19010.0
- Combined Max PnL: 990.0
- Combined Min PnL: -9810.0

**Net Premium:**

- Per Share: -1.9
- Total: -190.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $190.00 | $990.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.01x | 0.10x |
| Capital Basis | $5,000.00 | $15,000.00 |
| Cost Credit | Credit $190.00 | Credit $190.00 |
| Pop | 55.3% | 55.3% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 0.552808
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.820983
- P(50% Max Profit): 0.80982
- P(100% Max Profit): 0.786579
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 190.00 | -1500.00 | -1310.00 | 0.0380 | -0.0873 |
| 98.10 | Breakeven 1 | 190.00 | -190.00 | -0.00 | 0.0380 | -0.0000 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0380 | 0.0127 |
| 108.00 | Strike | 190.00 | 800.00 | 990.00 | 0.0380 | 0.0660 |
| 115.00 | Upside (15%) | -510.00 | 1500.00 | 990.00 | -0.1020 | 0.0660 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 190.00 | -9810.00 | -0.6540 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 190.00 | -1310.00 | -0.0873 |
| breakeven_1 | Breakeven 1 | 98.10 | -1.90% | 190.00 | -0.00 | -0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0127 |
| strike_1 | Strike | 108.00 | 8.00% | 190.00 | 990.00 | 0.0660 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -510.00 | 990.00 | 0.0660 |
| infinity | Stock to Infinity | — | — | Unlimited | 990.00 | 0.0660 |

---

### Covered Call (ID=8) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [108.0]
- Breakevens: [48.1]
- Options Max PnL: 190.0
- Options Min PnL: -19010.0
- Combined Max PnL: 5990.0
- Combined Min PnL: -4810.0

**Net Premium:**

- Per Share: -1.9
- Total: -190.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $190.00 | $5,990.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.01x | 1.25x |
| Capital Basis | $5,000.00 | $10,000.00 |
| Cost Credit | Credit $190.00 | Credit $190.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.820983
- P(50% Max Profit): 0.80982
- P(100% Max Profit): 0.786579
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 48.10 | Breakeven 1 | 190.00 | -190.00 | 0.00 | 0.0380 | 0.0000 |
| 50.00 | Scenario @ 50.00 | 190.00 | 0.00 | 190.00 | 0.0380 | 0.0190 |
| 85.00 | Downside (15%) | 190.00 | 3500.00 | 3690.00 | 0.0380 | 0.3690 |
| 100.00 | Current Market Price | 190.00 | 5000.00 | 5190.00 | 0.0380 | 0.5190 |
| 108.00 | Strike | 190.00 | 5800.00 | 5990.00 | 0.0380 | 0.5990 |
| 115.00 | Upside (15%) | -510.00 | 6500.00 | 5990.00 | -0.1020 | 0.5990 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 190.00 | -4810.00 | -0.4810 |
| breakeven_1 | Breakeven 1 | 48.10 | -51.90% | 190.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 190.00 | 3690.00 | 0.3690 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 5190.00 | 0.5190 |
| strike_1 | Strike | 108.00 | 8.00% | 190.00 | 5990.00 | 0.5990 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -510.00 | 5990.00 | 0.5990 |
| infinity | Stock to Infinity | — | — | Unlimited | 5990.00 | 0.5990 |

---

### Covered Call (ID=8) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [108.0]
- Breakevens: []
- Options Max PnL: 190.0
- Options Min PnL: -19010.0
- Combined Max PnL: -510.0
- Combined Min PnL: -11310.0

**Net Premium:**

- Per Share: -1.9
- Total: -190.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $190.00 | -$510.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.01x | 0.05x |
| Capital Basis | $5,000.00 | $16,500.00 |
| Cost Credit | Credit $190.00 | Credit $190.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.820983
- P(50% Max Profit): 0.80982
- P(100% Max Profit): 0.786579
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 190.00 | -3000.00 | -2810.00 | 0.0380 | -0.1703 |
| 100.00 | Current Market Price | 190.00 | -1500.00 | -1310.00 | 0.0380 | -0.0794 |
| 108.00 | Strike | 190.00 | -700.00 | -510.00 | 0.0380 | -0.0309 |
| 115.00 | Upside (15%) | -510.00 | 0.00 | -510.00 | -0.1020 | -0.0309 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 190.00 | -11310.00 | -0.6855 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 190.00 | -2810.00 | -0.1703 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | -1310.00 | -0.0794 |
| strike_1 | Strike | 108.00 | 8.00% | 190.00 | -510.00 | -0.0309 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -510.00 | -510.00 | -0.0309 |
| infinity | Stock to Infinity | — | — | Unlimited | -510.00 | -0.0309 |

---

### Covered Put (ID=9) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [92.0]
- Breakevens: [101.9]
- Options Max PnL: 190.0
- Options Min PnL: -9010.0
- Combined Max PnL: 990.0
- Combined Min PnL: -19810.0

**Net Premium:**

- Per Share: -1.9
- Total: -190.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $190.00 | $990.00 |
| Max Loss | -$9,010.00 | Unlimited |
| Risk Reward | 0.02x | 0.05x |
| Capital Basis | $1,390.00 | $11,390.00 |
| Cost Credit | Credit $190.00 | Credit $190.00 |
| Pop | 59.2% | 59.2% |
| Margin Proxy | 1390.0 | — |

**Probabilities:**

- PoP (raw): 0.592177
- Assignment Prob: 0.226367
- P(25% Max Profit): 0.816249
- P(50% Max Profit): 0.802561
- P(100% Max Profit): 0.774231
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -510.00 | 1500.00 | 990.00 | -0.0566 | 0.0521 |
| 92.00 | Strike | 190.00 | 800.00 | 990.00 | 0.0211 | 0.0521 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0211 | 0.0100 |
| 101.90 | Breakeven 1 | 190.00 | -190.00 | -0.00 | 0.0211 | -0.0000 |
| 115.00 | Upside (15%) | 190.00 | -1500.00 | -1310.00 | 0.0211 | -0.0689 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9010.00 | 990.00 | 0.0869 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -510.00 | 990.00 | 0.0521 |
| strike_1 | Strike | 92.00 | -8.00% | 190.00 | 990.00 | 0.0521 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0100 |
| breakeven_1 | Breakeven 1 | 101.90 | 1.90% | 190.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 190.00 | -1310.00 | -0.0689 |
| infinity | Stock to Infinity | — | — | 190.00 | -89810.00 | -7.8850 |

---

### Covered Put (ID=9) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [92.0]
- Breakevens: [101.9]
- Options Max PnL: 190.0
- Options Min PnL: -9010.0
- Combined Max PnL: 990.0
- Combined Min PnL: -19810.0

**Net Premium:**

- Per Share: -1.9
- Total: -190.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $190.00 | $990.00 |
| Max Loss | -$9,010.00 | Unlimited |
| Risk Reward | 0.02x | 0.05x |
| Capital Basis | $1,390.00 | $11,390.00 |
| Cost Credit | Credit $190.00 | Credit $190.00 |
| Pop | 59.2% | 59.2% |
| Margin Proxy | 1390.0 | — |

**Probabilities:**

- PoP (raw): 0.592177
- Assignment Prob: 0.226367
- P(25% Max Profit): 0.816249
- P(50% Max Profit): 0.802561
- P(100% Max Profit): 0.774231
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -510.00 | 1500.00 | 990.00 | -0.0566 | 0.0521 |
| 92.00 | Strike | 190.00 | 800.00 | 990.00 | 0.0211 | 0.0521 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0211 | 0.0100 |
| 101.90 | Breakeven 1 | 190.00 | -190.00 | -0.00 | 0.0211 | -0.0000 |
| 115.00 | Upside (15%) | 190.00 | -1500.00 | -1310.00 | 0.0211 | -0.0689 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9010.00 | 990.00 | 0.0869 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -510.00 | 990.00 | 0.0521 |
| strike_1 | Strike | 92.00 | -8.00% | 190.00 | 990.00 | 0.0521 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0100 |
| breakeven_1 | Breakeven 1 | 101.90 | 1.90% | 190.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 190.00 | -1310.00 | -0.0689 |
| infinity | Stock to Infinity | — | — | 190.00 | -89810.00 | -7.8850 |

---

### Covered Put (ID=9) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [92.0]
- Breakevens: []
- Options Max PnL: 190.0
- Options Min PnL: -9010.0
- Combined Max PnL: -4010.0
- Combined Min PnL: -24810.0

**Net Premium:**

- Per Share: -1.9
- Total: -190.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $190.00 | -$4,010.00 |
| Max Loss | -$9,010.00 | Unlimited |
| Risk Reward | 0.02x | 0.16x |
| Capital Basis | $1,390.00 | $6,390.00 |
| Cost Credit | Credit $190.00 | Credit $190.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 1390.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.226367
- P(25% Max Profit): 0.816249
- P(50% Max Profit): 0.802561
- P(100% Max Profit): 0.774231
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -4010.00 | 0.00 | -4010.00 | -0.4451 | -0.2862 |
| 85.00 | Downside (15%) | -510.00 | -3500.00 | -4010.00 | -0.0566 | -0.2862 |
| 92.00 | Strike | 190.00 | -4200.00 | -4010.00 | 0.0211 | -0.2862 |
| 100.00 | Current Market Price | 190.00 | -5000.00 | -4810.00 | 0.0211 | -0.3433 |
| 115.00 | Upside (15%) | 190.00 | -6500.00 | -6310.00 | 0.0211 | -0.4504 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9010.00 | -4010.00 | -0.6275 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -510.00 | -4010.00 | -0.2862 |
| strike_1 | Strike | 92.00 | -8.00% | 190.00 | -4010.00 | -0.2862 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | -4810.00 | -0.3433 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 190.00 | -6310.00 | -0.4504 |
| infinity | Stock to Infinity | — | — | 190.00 | -94810.00 | -14.8372 |

---

### Covered Put (ID=9) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [92.0]
- Breakevens: [116.9]
- Options Max PnL: 190.0
- Options Min PnL: -9010.0
- Combined Max PnL: 2490.0
- Combined Min PnL: -18310.0

**Net Premium:**

- Per Share: -1.9
- Total: -190.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $190.00 | $2,490.00 |
| Max Loss | -$9,010.00 | Unlimited |
| Risk Reward | 0.02x | 0.14x |
| Capital Basis | $1,390.00 | $12,890.00 |
| Cost Credit | Credit $190.00 | Credit $190.00 |
| Pop | 94.0% | 94.0% |
| Margin Proxy | 1390.0 | — |

**Probabilities:**

- PoP (raw): 0.940066
- Assignment Prob: 0.226367
- P(25% Max Profit): 0.816249
- P(50% Max Profit): 0.802561
- P(100% Max Profit): 0.774231
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -510.00 | 3000.00 | 2490.00 | -0.0566 | 0.1214 |
| 92.00 | Strike | 190.00 | 2300.00 | 2490.00 | 0.0211 | 0.1214 |
| 100.00 | Current Market Price | 190.00 | 1500.00 | 1690.00 | 0.0211 | 0.0824 |
| 115.00 | Upside (15%) | 190.00 | 0.00 | 190.00 | 0.0211 | 0.0093 |
| 116.90 | Breakeven 1 | 190.00 | -190.00 | -0.00 | 0.0211 | -0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9010.00 | 2490.00 | 0.1932 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -510.00 | 2490.00 | 0.1214 |
| strike_1 | Strike | 92.00 | -8.00% | 190.00 | 2490.00 | 0.1214 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 1690.00 | 0.0824 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 190.00 | 190.00 | 0.0093 |
| breakeven_1 | Breakeven 1 | 116.90 | 16.90% | 190.00 | -0.00 | -0.0000 |
| infinity | Stock to Infinity | — | — | 190.00 | -88310.00 | -6.8510 |

---

### Protective Call (ID=10) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 100.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [108.0]
- Breakevens: [98.1]
- Options Max PnL: 19010.0
- Options Min PnL: -190.0
- Combined Max PnL: 9810.0
- Combined Min PnL: -990.0

**Net Premium:**

- Per Share: 1.9
- Total: 190.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$190.00 | Unlimited |
| Risk Reward | 100.05x | 9.91x |
| Capital Basis | $190.00 | $10,190.00 |
| Cost Credit | Debit $190.00 | Debit $190.00 |
| Pop | 44.7% | 44.7% |
| Margin Proxy | 190.0 | — |

**Probabilities:**

- PoP (raw): 0.447192
- Assignment Prob: 0.0
- P(25% Max Profit): 5e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -190.00 | 1500.00 | 1310.00 | -1.0000 | 0.1286 |
| 98.10 | Breakeven 1 | -190.00 | 190.00 | 0.00 | -1.0000 | 0.0000 |
| 100.00 | Current Market Price | -190.00 | 0.00 | -190.00 | -1.0000 | -0.0186 |
| 108.00 | Strike | -190.00 | -800.00 | -990.00 | -1.0000 | -0.0972 |
| 115.00 | Upside (15%) | 510.00 | -1500.00 | -990.00 | 2.6842 | -0.0972 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -190.00 | 9810.00 | 0.9627 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -190.00 | 1310.00 | 0.1286 |
| breakeven_1 | Breakeven 1 | 98.10 | -1.90% | -190.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | -190.00 | -0.0186 |
| strike_1 | Strike | 108.00 | 8.00% | -190.00 | -990.00 | -0.0972 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 510.00 | -990.00 | -0.0972 |
| infinity | Stock to Infinity | — | — | 97010.00 | -990.00 | -0.0972 |

---

### Protective Call (ID=10) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 100.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [108.0]
- Breakevens: [98.1]
- Options Max PnL: 19010.0
- Options Min PnL: -190.0
- Combined Max PnL: 9810.0
- Combined Min PnL: -990.0

**Net Premium:**

- Per Share: 1.9
- Total: 190.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$190.00 | Unlimited |
| Risk Reward | 100.05x | 9.91x |
| Capital Basis | $190.00 | $10,190.00 |
| Cost Credit | Debit $190.00 | Debit $190.00 |
| Pop | 44.7% | 44.7% |
| Margin Proxy | 190.0 | — |

**Probabilities:**

- PoP (raw): 0.447192
- Assignment Prob: 0.0
- P(25% Max Profit): 5e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -190.00 | 1500.00 | 1310.00 | -1.0000 | 0.1286 |
| 98.10 | Breakeven 1 | -190.00 | 190.00 | 0.00 | -1.0000 | 0.0000 |
| 100.00 | Current Market Price | -190.00 | 0.00 | -190.00 | -1.0000 | -0.0186 |
| 108.00 | Strike | -190.00 | -800.00 | -990.00 | -1.0000 | -0.0972 |
| 115.00 | Upside (15%) | 510.00 | -1500.00 | -990.00 | 2.6842 | -0.0972 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -190.00 | 9810.00 | 0.9627 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -190.00 | 1310.00 | 0.1286 |
| breakeven_1 | Breakeven 1 | 98.10 | -1.90% | -190.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | -190.00 | -0.0186 |
| strike_1 | Strike | 108.00 | 8.00% | -190.00 | -990.00 | -0.0972 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 510.00 | -990.00 | -0.0972 |
| infinity | Stock to Infinity | — | — | 97010.00 | -990.00 | -0.0972 |

---

### Protective Call (ID=10) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 50.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [108.0]
- Breakevens: [48.1]
- Options Max PnL: 19010.0
- Options Min PnL: -190.0
- Combined Max PnL: 4810.0
- Combined Min PnL: -5990.0

**Net Premium:**

- Per Share: 1.9
- Total: 190.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$190.00 | Unlimited |
| Risk Reward | 100.05x | 0.80x |
| Capital Basis | $190.00 | $5,190.00 |
| Cost Credit | Debit $190.00 | Debit $190.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 190.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.0
- P(25% Max Profit): 5e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 48.10 | Breakeven 1 | -190.00 | 190.00 | -0.00 | -1.0000 | -0.0000 |
| 50.00 | Scenario @ 50.00 | -190.00 | 0.00 | -190.00 | -1.0000 | -0.0366 |
| 85.00 | Downside (15%) | -190.00 | -3500.00 | -3690.00 | -1.0000 | -0.7110 |
| 100.00 | Current Market Price | -190.00 | -5000.00 | -5190.00 | -1.0000 | -1.0000 |
| 108.00 | Strike | -190.00 | -5800.00 | -5990.00 | -1.0000 | -1.1541 |
| 115.00 | Upside (15%) | 510.00 | -6500.00 | -5990.00 | 2.6842 | -1.1541 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -190.00 | 4810.00 | 0.9268 |
| breakeven_1 | Breakeven 1 | 48.10 | -51.90% | -190.00 | -0.00 | -0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -190.00 | -3690.00 | -0.7110 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | -5190.00 | -1.0000 |
| strike_1 | Strike | 108.00 | 8.00% | -190.00 | -5990.00 | -1.1541 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 510.00 | -5990.00 | -1.1541 |
| infinity | Stock to Infinity | — | — | 97010.00 | -5990.00 | -1.1541 |

---

### Protective Call (ID=10) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 114.99999999999999
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [108.0]
- Breakevens: []
- Options Max PnL: 19010.0
- Options Min PnL: -190.0
- Combined Max PnL: 11310.0
- Combined Min PnL: 510.0

**Net Premium:**

- Per Share: 1.9
- Total: 190.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$190.00 | Unlimited |
| Risk Reward | 100.05x | 22.18x |
| Capital Basis | $190.00 | $11,690.00 |
| Cost Credit | Debit $190.00 | Debit $190.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 190.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.0
- P(25% Max Profit): 5e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -190.00 | 3000.00 | 2810.00 | -1.0000 | 0.2404 |
| 100.00 | Current Market Price | -190.00 | 1500.00 | 1310.00 | -1.0000 | 0.1121 |
| 108.00 | Strike | -190.00 | 700.00 | 510.00 | -1.0000 | 0.0436 |
| 115.00 | Upside (15%) | 510.00 | 0.00 | 510.00 | 2.6842 | 0.0436 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -190.00 | 11310.00 | 0.9675 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -190.00 | 2810.00 | 0.2404 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | 1310.00 | 0.1121 |
| strike_1 | Strike | 108.00 | 8.00% | -190.00 | 510.00 | 0.0436 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 510.00 | 510.00 | 0.0436 |
| infinity | Stock to Infinity | — | — | 97010.00 | 510.00 | 0.0436 |

---

### Protective Put (ID=11) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: PPRT
- Margin Classification: PPRT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [92.0]
- Breakevens: [101.9]
- Options Max PnL: 9010.0
- Options Min PnL: -190.0
- Combined Max PnL: 19810.0
- Combined Min PnL: -990.0

**Net Premium:**

- Per Share: 1.9
- Total: 190.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $9,010.00 | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 47.42x | 20.01x |
| Capital Basis | $5,190.00 | $15,190.00 |
| Cost Credit | Debit $190.00 | Debit $190.00 |
| Pop | 40.8% | 40.8% |
| Margin Proxy | 5190.0 | — |

**Probabilities:**

- PoP (raw): 0.407823
- Assignment Prob: 0.0
- P(25% Max Profit): 9.9e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 510.00 | -1500.00 | -990.00 | 2.6842 | -0.0972 |
| 92.00 | Strike | -190.00 | -800.00 | -990.00 | -1.0000 | -0.0972 |
| 100.00 | Current Market Price | -190.00 | 0.00 | -190.00 | -1.0000 | -0.0186 |
| 101.90 | Breakeven 1 | -190.00 | 190.00 | 0.00 | -1.0000 | 0.0000 |
| 115.00 | Upside (15%) | -190.00 | 1500.00 | 1310.00 | -1.0000 | 0.1286 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9010.00 | -990.00 | -0.0652 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 510.00 | -990.00 | -0.0972 |
| strike_1 | Strike | 92.00 | -8.00% | -190.00 | -990.00 | -0.0972 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | -190.00 | -0.0186 |
| breakeven_1 | Breakeven 1 | 101.90 | 1.90% | -190.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -190.00 | 1310.00 | 0.1286 |
| infinity | Stock to Infinity | — | — | Unlimited | 89810.00 | 5.9124 |

---

### Protective Put (ID=11) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: PPRT
- Margin Classification: PPRT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [92.0]
- Breakevens: [101.9]
- Options Max PnL: 9010.0
- Options Min PnL: -190.0
- Combined Max PnL: 19810.0
- Combined Min PnL: -990.0

**Net Premium:**

- Per Share: 1.9
- Total: 190.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $9,010.00 | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 47.42x | 20.01x |
| Capital Basis | $5,190.00 | $15,190.00 |
| Cost Credit | Debit $190.00 | Debit $190.00 |
| Pop | 40.8% | 40.8% |
| Margin Proxy | 5190.0 | — |

**Probabilities:**

- PoP (raw): 0.407823
- Assignment Prob: 0.0
- P(25% Max Profit): 9.9e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 510.00 | -1500.00 | -990.00 | 2.6842 | -0.0972 |
| 92.00 | Strike | -190.00 | -800.00 | -990.00 | -1.0000 | -0.0972 |
| 100.00 | Current Market Price | -190.00 | 0.00 | -190.00 | -1.0000 | -0.0186 |
| 101.90 | Breakeven 1 | -190.00 | 190.00 | 0.00 | -1.0000 | 0.0000 |
| 115.00 | Upside (15%) | -190.00 | 1500.00 | 1310.00 | -1.0000 | 0.1286 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9010.00 | -990.00 | -0.0652 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 510.00 | -990.00 | -0.0972 |
| strike_1 | Strike | 92.00 | -8.00% | -190.00 | -990.00 | -0.0972 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | -190.00 | -0.0186 |
| breakeven_1 | Breakeven 1 | 101.90 | 1.90% | -190.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -190.00 | 1310.00 | 0.1286 |
| infinity | Stock to Infinity | — | — | Unlimited | 89810.00 | 5.9124 |

---

### Protective Put (ID=11) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: PPRT
- Margin Classification: PPRT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [92.0]
- Breakevens: []
- Options Max PnL: 9010.0
- Options Min PnL: -190.0
- Combined Max PnL: 24810.0
- Combined Min PnL: 4010.0

**Net Premium:**

- Per Share: 1.9
- Total: 190.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $9,010.00 | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 47.42x | 6.19x |
| Capital Basis | $5,190.00 | $10,190.00 |
| Cost Credit | Debit $190.00 | Debit $190.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 5190.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.0
- P(25% Max Profit): 9.9e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | 4010.00 | 0.00 | 4010.00 | 21.1053 | 0.7726 |
| 85.00 | Downside (15%) | 510.00 | 3500.00 | 4010.00 | 2.6842 | 0.7726 |
| 92.00 | Strike | -190.00 | 4200.00 | 4010.00 | -1.0000 | 0.7726 |
| 100.00 | Current Market Price | -190.00 | 5000.00 | 4810.00 | -1.0000 | 0.9268 |
| 115.00 | Upside (15%) | -190.00 | 6500.00 | 6310.00 | -1.0000 | 1.2158 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9010.00 | 4010.00 | 0.3935 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 510.00 | 4010.00 | 0.7726 |
| strike_1 | Strike | 92.00 | -8.00% | -190.00 | 4010.00 | 0.7726 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | 4810.00 | 0.9268 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -190.00 | 6310.00 | 1.2158 |
| infinity | Stock to Infinity | — | — | Unlimited | 94810.00 | 9.3042 |

---

### Protective Put (ID=11) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: PPRT
- Margin Classification: PPRT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [92.0]
- Breakevens: [116.9]
- Options Max PnL: 9010.0
- Options Min PnL: -190.0
- Combined Max PnL: 18310.0
- Combined Min PnL: -2490.0

**Net Premium:**

- Per Share: 1.9
- Total: 190.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $9,010.00 | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 47.42x | 7.35x |
| Capital Basis | $5,190.00 | $16,690.00 |
| Cost Credit | Debit $190.00 | Debit $190.00 |
| Pop | 6.0% | 6.0% |
| Margin Proxy | 5190.0 | — |

**Probabilities:**

- PoP (raw): 0.059934
- Assignment Prob: 0.0
- P(25% Max Profit): 9.9e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 510.00 | -3000.00 | -2490.00 | 2.6842 | -0.2130 |
| 92.00 | Strike | -190.00 | -2300.00 | -2490.00 | -1.0000 | -0.2130 |
| 100.00 | Current Market Price | -190.00 | -1500.00 | -1690.00 | -1.0000 | -0.1446 |
| 115.00 | Upside (15%) | -190.00 | 0.00 | -190.00 | -1.0000 | -0.0163 |
| 116.90 | Breakeven 1 | -190.00 | 190.00 | 0.00 | -1.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9010.00 | -2490.00 | -0.1492 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 510.00 | -2490.00 | -0.2130 |
| strike_1 | Strike | 92.00 | -8.00% | -190.00 | -2490.00 | -0.2130 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | -1690.00 | -0.1446 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -190.00 | -190.00 | -0.0163 |
| breakeven_1 | Breakeven 1 | 116.90 | 16.90% | -190.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | 88310.00 | 5.2912 |

---

### Collar (ID=12) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: COL_EQ
- Margin Classification: COL_EQ

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [100.0]
- Options Max PnL: 9200.0
- Options Min PnL: -19200.0
- Combined Max PnL: 800.0
- Combined Min PnL: -800.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $9,200.00 | $800.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.48x | 1.00x |
| Capital Basis | $5,190.00 | $15,190.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 47.9% | 47.9% |
| Margin Proxy | 5190.0 | — |

**Probabilities:**

- PoP (raw): 0.47931
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.000215
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 700.00 | -1500.00 | -800.00 | 0.1349 | -0.0527 |
| 92.00 | Lower Strike | 0.00 | -800.00 | -800.00 | 0.0000 | -0.0527 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | 0.00 | 800.00 | 800.00 | 0.0000 | 0.0527 |
| 115.00 | Upside (15%) | -700.00 | 1500.00 | 800.00 | -0.1349 | 0.0527 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9200.00 | -800.00 | -0.0527 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 700.00 | -800.00 | -0.0527 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | -800.00 | -0.0527 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 800.00 | 0.0527 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -700.00 | 800.00 | 0.0527 |
| infinity | Stock to Infinity | — | — | Unlimited | 800.00 | 0.0527 |

---

### Collar (ID=12) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: COL_EQ
- Margin Classification: COL_EQ

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [100.0]
- Options Max PnL: 9200.0
- Options Min PnL: -19200.0
- Combined Max PnL: 800.0
- Combined Min PnL: -800.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $9,200.00 | $800.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.48x | 1.00x |
| Capital Basis | $5,190.00 | $15,190.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 47.9% | 47.9% |
| Margin Proxy | 5190.0 | — |

**Probabilities:**

- PoP (raw): 0.47931
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.000215
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 700.00 | -1500.00 | -800.00 | 0.1349 | -0.0527 |
| 92.00 | Lower Strike | 0.00 | -800.00 | -800.00 | 0.0000 | -0.0527 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | 0.00 | 800.00 | 800.00 | 0.0000 | 0.0527 |
| 115.00 | Upside (15%) | -700.00 | 1500.00 | 800.00 | -0.1349 | 0.0527 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9200.00 | -800.00 | -0.0527 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 700.00 | -800.00 | -0.0527 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | -800.00 | -0.0527 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 800.00 | 0.0527 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -700.00 | 800.00 | 0.0527 |
| infinity | Stock to Infinity | — | — | Unlimited | 800.00 | 0.0527 |

---

### Collar (ID=12) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: COL_EQ
- Margin Classification: COL_EQ

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: []
- Options Max PnL: 9200.0
- Options Min PnL: -19200.0
- Combined Max PnL: 5800.0
- Combined Min PnL: 4200.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $9,200.00 | $5,800.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.48x | 1.38x |
| Capital Basis | $5,190.00 | $10,190.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 5190.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.000215
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | 4200.00 | 0.00 | 4200.00 | 0.8092 | 0.4122 |
| 85.00 | Downside (15%) | 700.00 | 3500.00 | 4200.00 | 0.1349 | 0.4122 |
| 92.00 | Lower Strike | 0.00 | 4200.00 | 4200.00 | 0.0000 | 0.4122 |
| 100.00 | Current Market Price | 0.00 | 5000.00 | 5000.00 | 0.0000 | 0.4907 |
| 108.00 | Upper Strike | 0.00 | 5800.00 | 5800.00 | 0.0000 | 0.5692 |
| 115.00 | Upside (15%) | -700.00 | 6500.00 | 5800.00 | -0.1349 | 0.5692 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9200.00 | 4200.00 | 0.4122 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 700.00 | 4200.00 | 0.4122 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | 4200.00 | 0.4122 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 0.4907 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 5800.00 | 0.5692 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -700.00 | 5800.00 | 0.5692 |
| infinity | Stock to Infinity | — | — | Unlimited | 5800.00 | 0.5692 |

---

### Collar (ID=12) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: COL_EQ
- Margin Classification: COL_EQ

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: []
- Options Max PnL: 9200.0
- Options Min PnL: -19200.0
- Combined Max PnL: -700.0
- Combined Min PnL: -2300.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $9,200.00 | -$700.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.48x | 0.30x |
| Capital Basis | $5,190.00 | $16,690.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 5190.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.000215
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 700.00 | -3000.00 | -2300.00 | 0.1349 | -0.1378 |
| 92.00 | Lower Strike | 0.00 | -2300.00 | -2300.00 | 0.0000 | -0.1378 |
| 100.00 | Current Market Price | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.0899 |
| 108.00 | Upper Strike | 0.00 | -700.00 | -700.00 | 0.0000 | -0.0419 |
| 115.00 | Upside (15%) | -700.00 | 0.00 | -700.00 | -0.1349 | -0.0419 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9200.00 | -2300.00 | -0.1378 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 700.00 | -2300.00 | -0.1378 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | -2300.00 | -0.1378 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.0899 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | -700.00 | -0.0419 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -700.00 | -700.00 | -0.0419 |
| infinity | Stock to Infinity | — | — | Unlimited | -700.00 | -0.0419 |

---

### Bull Call Spread (ID=13) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [100.0]
- Options Max PnL: 800.0
- Options Min PnL: -800.0
- Combined Max PnL: 800.0
- Combined Min PnL: -800.0

**Net Premium:**

- Per Share: 8.0
- Total: 800.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $800.00 | $800.00 |
| Max Loss | -$800.00 | -$800.00 |
| Risk Reward | 1.00x | 1.00x |
| Capital Basis | $800.00 | $800.00 |
| Cost Credit | Debit $800.00 | Debit $800.00 |
| Pop | 47.9% | 47.9% |
| Margin Proxy | 800.0 | — |

**Probabilities:**

- PoP (raw): 0.47931
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.404161
- P(50% Max Profit): 0.33376
- P(100% Max Profit): 0.215999
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -800.00 | 0.00 | -800.00 | -1.0000 | -1.0000 |
| 92.00 | Lower Strike | -800.00 | 0.00 | -800.00 | -1.0000 | -1.0000 |
| 100.00 | Current Market Price | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 108.00 | Upper Strike | 800.00 | 0.00 | 800.00 | 1.0000 | 1.0000 |
| 115.00 | Upside (15%) | 800.00 | 0.00 | 800.00 | 1.0000 | 1.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -800.00 | -800.00 | -1.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -800.00 | -800.00 | -1.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -800.00 | -800.00 | -1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -0.00 | -0.00 | -0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | -0.00 | -0.00 | -0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 800.00 | 800.00 | 1.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 800.00 | 800.00 | 1.0000 |
| infinity | Stock to Infinity | — | — | 800.00 | 800.00 | 1.0000 |

---

### Bull Call Spread (ID=13) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [100.0]
- Options Max PnL: 800.0
- Options Min PnL: -800.0
- Combined Max PnL: 20800.0
- Combined Min PnL: -10800.0

**Net Premium:**

- Per Share: 8.0
- Total: 800.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $800.00 | Unlimited |
| Max Loss | -$800.00 | -$10,800.00 |
| Risk Reward | 1.00x | 1.93x |
| Capital Basis | $1,390.00 | $11,390.00 |
| Cost Credit | Debit $800.00 | Debit $800.00 |
| Pop | 47.9% | 47.9% |
| Margin Proxy | 1390.0 | — |

**Probabilities:**

- PoP (raw): 0.47931
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.404161
- P(50% Max Profit): 0.33376
- P(100% Max Profit): 0.215999
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -800.00 | -1500.00 | -2300.00 | -1.0000 | -0.2130 |
| 92.00 | Lower Strike | -800.00 | -800.00 | -1600.00 | -1.0000 | -0.1481 |
| 100.00 | Current Market Price | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 108.00 | Upper Strike | 800.00 | 800.00 | 1600.00 | 1.0000 | 0.1481 |
| 115.00 | Upside (15%) | 800.00 | 1500.00 | 2300.00 | 1.0000 | 0.2130 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -800.00 | -10800.00 | -0.9482 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -800.00 | -2300.00 | -0.2130 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -800.00 | -1600.00 | -0.1481 |
| spot | Current Market Price | 100.00 | 0.00% | -0.00 | -0.00 | -0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | -0.00 | -0.00 | -0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 800.00 | 1600.00 | 0.1481 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 800.00 | 2300.00 | 0.2130 |
| infinity | Stock to Infinity | — | — | 800.00 | 98800.00 | 8.6743 |

---

### Bull Call Spread (ID=13) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [58.0]
- Options Max PnL: 800.0
- Options Min PnL: -800.0
- Combined Max PnL: 25800.0
- Combined Min PnL: -5800.0

**Net Premium:**

- Per Share: 8.0
- Total: 800.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $800.00 | Unlimited |
| Max Loss | -$800.00 | -$5,800.00 |
| Risk Reward | 1.00x | 4.45x |
| Capital Basis | $1,390.00 | $6,390.00 |
| Cost Credit | Debit $800.00 | Debit $800.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 1390.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.404161
- P(50% Max Profit): 0.33376
- P(100% Max Profit): 0.215999
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -800.00 | 0.00 | -800.00 | -1.0000 | -0.1379 |
| 58.00 | Breakeven 1 | -800.00 | 800.00 | 0.00 | -1.0000 | 0.0000 |
| 85.00 | Downside (15%) | -800.00 | 3500.00 | 2700.00 | -1.0000 | 0.4655 |
| 92.00 | Lower Strike | -800.00 | 4200.00 | 3400.00 | -1.0000 | 0.5862 |
| 100.00 | Current Market Price | -0.00 | 5000.00 | 5000.00 | -0.0000 | 0.8621 |
| 108.00 | Upper Strike | 800.00 | 5800.00 | 6600.00 | 1.0000 | 1.1379 |
| 115.00 | Upside (15%) | 800.00 | 6500.00 | 7300.00 | 1.0000 | 1.2586 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -800.00 | -5800.00 | -0.9077 |
| breakeven_1 | Breakeven 1 | 58.00 | -42.00% | -800.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -800.00 | 2700.00 | 0.4655 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -800.00 | 3400.00 | 0.5862 |
| spot | Current Market Price | 100.00 | 0.00% | -0.00 | 5000.00 | 0.8621 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 800.00 | 6600.00 | 1.1379 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 800.00 | 7300.00 | 1.2586 |
| infinity | Stock to Infinity | — | — | 800.00 | 103800.00 | 16.2441 |

---

### Bull Call Spread (ID=13) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [107.5]
- Options Max PnL: 800.0
- Options Min PnL: -800.0
- Combined Max PnL: 19300.0
- Combined Min PnL: -12300.0

**Net Premium:**

- Per Share: 8.0
- Total: 800.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $800.00 | Unlimited |
| Max Loss | -$800.00 | -$12,300.00 |
| Risk Reward | 1.00x | 1.57x |
| Capital Basis | $1,390.00 | $12,890.00 |
| Cost Credit | Debit $800.00 | Debit $800.00 |
| Pop | 22.7% | 22.7% |
| Margin Proxy | 1390.0 | — |

**Probabilities:**

- PoP (raw): 0.227159
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.404161
- P(50% Max Profit): 0.33376
- P(100% Max Profit): 0.215999
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -800.00 | -3000.00 | -3800.00 | -1.0000 | -0.3089 |
| 92.00 | Lower Strike | -800.00 | -2300.00 | -3100.00 | -1.0000 | -0.2520 |
| 100.00 | Current Market Price | -0.00 | -1500.00 | -1500.00 | -0.0000 | -0.1220 |
| 107.50 | Breakeven 1 | 750.00 | -750.00 | 0.00 | 0.9375 | 0.0000 |
| 108.00 | Upper Strike | 800.00 | -700.00 | 100.00 | 1.0000 | 0.0081 |
| 115.00 | Upside (15%) | 800.00 | 0.00 | 800.00 | 1.0000 | 0.0650 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -800.00 | -12300.00 | -0.9542 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -800.00 | -3800.00 | -0.3089 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -800.00 | -3100.00 | -0.2520 |
| spot | Current Market Price | 100.00 | 0.00% | -0.00 | -1500.00 | -0.1220 |
| breakeven_1 | Breakeven 1 | 107.50 | 7.50% | 750.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 800.00 | 100.00 | 0.0081 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 800.00 | 800.00 | 0.0650 |
| infinity | Stock to Infinity | — | — | 800.00 | 97300.00 | 7.5485 |

---

### Bear Put Spread (ID=14) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 108.00 | 9.90 | 100 |
| 2 | PUT | Short 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [100.0]
- Options Max PnL: 800.0
- Options Min PnL: -800.0
- Combined Max PnL: 800.0
- Combined Min PnL: -800.0

**Net Premium:**

- Per Share: 8.0
- Total: 800.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $800.00 | $800.00 |
| Max Loss | -$800.00 | -$800.00 |
| Risk Reward | 1.00x | 1.00x |
| Capital Basis | $800.00 | $800.00 |
| Cost Credit | Debit $800.00 | Debit $800.00 |
| Pop | 52.1% | 52.1% |
| Margin Proxy | 800.0 | — |

**Probabilities:**

- PoP (raw): 0.52069
- Assignment Prob: 0.226367
- P(25% Max Profit): 0.443311
- P(50% Max Profit): 0.366799
- P(100% Max Profit): 0.228893
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 800.00 | 0.00 | 800.00 | 1.0000 | 1.0000 |
| 92.00 | Lower Strike | 800.00 | 0.00 | 800.00 | 1.0000 | 1.0000 |
| 100.00 | Current Market Price | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 108.00 | Upper Strike | -800.00 | 0.00 | -800.00 | -1.0000 | -1.0000 |
| 115.00 | Upside (15%) | -800.00 | 0.00 | -800.00 | -1.0000 | -1.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 800.00 | 800.00 | 1.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 800.00 | 800.00 | 1.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 800.00 | 800.00 | 1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -0.00 | -0.00 | -0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | -0.00 | -0.00 | -0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -800.00 | -800.00 | -1.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -800.00 | -800.00 | -1.0000 |
| infinity | Stock to Infinity | — | — | -800.00 | -800.00 | -1.0000 |

---

### Bear Put Spread (ID=14) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 108.00 | 9.90 | 100 |
| 2 | PUT | Short 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [92.0, 92.307692, 94.314381, 96.32107, 97.324415, 103.344482, 105.351171, 107.35786, 108.0]
- Options Max PnL: 800.0
- Options Min PnL: -800.0
- Combined Max PnL: 19200.0
- Combined Min PnL: -9200.0

**Net Premium:**

- Per Share: 8.0
- Total: 800.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $800.00 | Unlimited |
| Max Loss | -$800.00 | -$9,200.00 |
| Risk Reward | 1.00x | 2.09x |
| Capital Basis | $1,390.00 | $11,390.00 |
| Cost Credit | Debit $800.00 | Debit $800.00 |
| Pop | 21.4% | 21.4% |
| Margin Proxy | 1390.0 | — |

**Probabilities:**

- PoP (raw): 0.213914
- Assignment Prob: 0.226367
- P(25% Max Profit): 0.443311
- P(50% Max Profit): 0.366799
- P(100% Max Profit): 0.228893
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 800.00 | -1500.00 | -700.00 | 1.0000 | -0.0648 |
| 92.00 | Breakeven 1 | 800.00 | -800.00 | 0.00 | 1.0000 | 0.0000 |
| 92.31 | Breakeven 2 | 769.23 | -769.23 | 0.00 | 0.9615 | 0.0000 |
| 94.31 | Breakeven 3 | 568.56 | -568.56 | 0.00 | 0.7107 | 0.0000 |
| 96.32 | Breakeven 4 | 367.89 | -367.89 | 0.00 | 0.4599 | 0.0000 |
| 97.32 | Breakeven 5 | 267.56 | -267.56 | 0.00 | 0.3344 | 0.0000 |
| 100.00 | Current Market Price | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 103.34 | Breakeven 6 | -334.45 | 334.45 | 0.00 | -0.4181 | 0.0000 |
| 105.35 | Breakeven 7 | -535.12 | 535.12 | 0.00 | -0.6689 | 0.0000 |
| 107.36 | Breakeven 8 | -735.79 | 735.79 | -0.00 | -0.9197 | -0.0000 |
| 108.00 | Breakeven 9 | -800.00 | 800.00 | 0.00 | -1.0000 | 0.0000 |
| 115.00 | Upside (15%) | -800.00 | 1500.00 | 700.00 | -1.0000 | 0.0648 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 800.00 | -9200.00 | -0.8077 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 800.00 | -700.00 | -0.0648 |
| strike_1 | Breakeven 1 | 92.00 | -8.00% | 800.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 92.00 | -8.00% | 800.00 | 0.00 | 0.0000 |
| breakeven_2 | Breakeven 2 | 92.31 | -7.69% | 769.23 | 0.00 | 0.0000 |
| breakeven_3 | Breakeven 3 | 94.31 | -5.69% | 568.56 | 0.00 | 0.0000 |
| breakeven_4 | Breakeven 4 | 96.32 | -3.68% | 367.89 | 0.00 | 0.0000 |
| breakeven_5 | Breakeven 5 | 97.32 | -2.68% | 267.56 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -0.00 | -0.00 | -0.0000 |
| breakeven_6 | Breakeven 6 | 103.34 | 3.34% | -334.45 | 0.00 | 0.0000 |
| breakeven_7 | Breakeven 7 | 105.35 | 5.35% | -535.12 | 0.00 | 0.0000 |
| breakeven_8 | Breakeven 8 | 107.36 | 7.36% | -735.79 | -0.00 | -0.0000 |
| strike_2 | Breakeven 9 | 108.00 | 8.00% | -800.00 | 0.00 | 0.0000 |
| breakeven_9 | Breakeven 9 | 108.00 | 8.00% | -800.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -800.00 | 700.00 | 0.0648 |
| infinity | Stock to Infinity | — | — | -800.00 | 97200.00 | 8.5338 |

---

### Bear Put Spread (ID=14) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 108.00 | 9.90 | 100 |
| 2 | PUT | Short 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [42.0]
- Options Max PnL: 800.0
- Options Min PnL: -800.0
- Combined Max PnL: 24200.0
- Combined Min PnL: -4200.0

**Net Premium:**

- Per Share: 8.0
- Total: 800.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $800.00 | Unlimited |
| Max Loss | -$800.00 | -$4,200.00 |
| Risk Reward | 1.00x | 5.76x |
| Capital Basis | $1,390.00 | $6,390.00 |
| Cost Credit | Debit $800.00 | Debit $800.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 1390.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.226367
- P(25% Max Profit): 0.443311
- P(50% Max Profit): 0.366799
- P(100% Max Profit): 0.228893
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 42.00 | Breakeven 1 | 800.00 | -800.00 | 0.00 | 1.0000 | 0.0000 |
| 50.00 | Scenario @ 50.00 | 800.00 | 0.00 | 800.00 | 1.0000 | 0.1379 |
| 85.00 | Downside (15%) | 800.00 | 3500.00 | 4300.00 | 1.0000 | 0.7414 |
| 92.00 | Lower Strike | 800.00 | 4200.00 | 5000.00 | 1.0000 | 0.8621 |
| 100.00 | Current Market Price | -0.00 | 5000.00 | 5000.00 | -0.0000 | 0.8621 |
| 108.00 | Upper Strike | -800.00 | 5800.00 | 5000.00 | -1.0000 | 0.8621 |
| 115.00 | Upside (15%) | -800.00 | 6500.00 | 5700.00 | -1.0000 | 0.9828 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 800.00 | -4200.00 | -0.6573 |
| breakeven_1 | Breakeven 1 | 42.00 | -58.00% | 800.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 800.00 | 4300.00 | 0.7414 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 800.00 | 5000.00 | 0.8621 |
| spot | Current Market Price | 100.00 | 0.00% | -0.00 | 5000.00 | 0.8621 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -800.00 | 5000.00 | 0.8621 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -800.00 | 5700.00 | 0.9828 |
| infinity | Stock to Infinity | — | — | -800.00 | 102200.00 | 15.9937 |

---

### Bear Put Spread (ID=14) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 108.00 | 9.90 | 100 |
| 2 | PUT | Short 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [123.0]
- Options Max PnL: 800.0
- Options Min PnL: -800.0
- Combined Max PnL: 17700.0
- Combined Min PnL: -10700.0

**Net Premium:**

- Per Share: 8.0
- Total: 800.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $800.00 | Unlimited |
| Max Loss | -$800.00 | -$10,700.00 |
| Risk Reward | 1.00x | 1.65x |
| Capital Basis | $1,390.00 | $12,890.00 |
| Cost Credit | Debit $800.00 | Debit $800.00 |
| Pop | 2.0% | 2.0% |
| Margin Proxy | 1390.0 | — |

**Probabilities:**

- PoP (raw): 0.020424
- Assignment Prob: 0.226367
- P(25% Max Profit): 0.443311
- P(50% Max Profit): 0.366799
- P(100% Max Profit): 0.228893
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 800.00 | -3000.00 | -2200.00 | 1.0000 | -0.1789 |
| 92.00 | Lower Strike | 800.00 | -2300.00 | -1500.00 | 1.0000 | -0.1220 |
| 100.00 | Current Market Price | -0.00 | -1500.00 | -1500.00 | -0.0000 | -0.1220 |
| 108.00 | Upper Strike | -800.00 | -700.00 | -1500.00 | -1.0000 | -0.1220 |
| 115.00 | Upside (15%) | -800.00 | 0.00 | -800.00 | -1.0000 | -0.0650 |
| 123.00 | Breakeven 1 | -800.00 | 800.00 | 0.00 | -1.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 800.00 | -10700.00 | -0.8301 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 800.00 | -2200.00 | -0.1789 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 800.00 | -1500.00 | -0.1220 |
| spot | Current Market Price | 100.00 | 0.00% | -0.00 | -1500.00 | -0.1220 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -800.00 | -1500.00 | -0.1220 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -800.00 | -800.00 | -0.0650 |
| breakeven_1 | Breakeven 1 | 123.00 | 23.00% | -800.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | -800.00 | 95700.00 | 7.4244 |

---

### Bear Call Spread (ID=15) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [100.0]
- Options Max PnL: 800.0
- Options Min PnL: -800.0
- Combined Max PnL: 800.0
- Combined Min PnL: -800.0

**Net Premium:**

- Per Share: -8.0
- Total: -800.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $800.00 | $800.00 |
| Max Loss | -$800.00 | -$800.00 |
| Risk Reward | 1.00x | 1.00x |
| Capital Basis | $800.00 | $800.00 |
| Cost Credit | Credit $800.00 | Credit $800.00 |
| Pop | 52.1% | 52.1% |
| Margin Proxy | 800.0 | — |

**Probabilities:**

- PoP (raw): 0.52069
- Assignment Prob: 0.773633
- P(25% Max Profit): 0.443311
- P(50% Max Profit): 0.366799
- P(100% Max Profit): 0.228893
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 800.00 | 0.00 | 800.00 | 1.0000 | 1.0000 |
| 92.00 | Lower Strike | 800.00 | 0.00 | 800.00 | 1.0000 | 1.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | -800.00 | 0.00 | -800.00 | -1.0000 | -1.0000 |
| 115.00 | Upside (15%) | -800.00 | 0.00 | -800.00 | -1.0000 | -1.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 800.00 | 800.00 | 1.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 800.00 | 800.00 | 1.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 800.00 | 800.00 | 1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -800.00 | -800.00 | -1.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -800.00 | -800.00 | -1.0000 |
| infinity | Stock to Infinity | — | — | -800.00 | -800.00 | -1.0000 |

---

### Bear Call Spread (ID=15) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [92.0, 93.311037, 96.32107, 103.344482, 106.354515, 108.0]
- Options Max PnL: 800.0
- Options Min PnL: -800.0
- Combined Max PnL: 19200.0
- Combined Min PnL: -9200.0

**Net Premium:**

- Per Share: -8.0
- Total: -800.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $800.00 | Unlimited |
| Max Loss | -$800.00 | -$9,200.00 |
| Risk Reward | 1.00x | 2.09x |
| Capital Basis | $2,990.00 | $12,990.00 |
| Cost Credit | Credit $800.00 | Credit $800.00 |
| Pop | 57.7% | 57.7% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 0.57705
- Assignment Prob: 0.773633
- P(25% Max Profit): 0.443311
- P(50% Max Profit): 0.366799
- P(100% Max Profit): 0.228893
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 800.00 | -1500.00 | -700.00 | 1.0000 | -0.0648 |
| 92.00 | Breakeven 1 | 800.00 | -800.00 | 0.00 | 1.0000 | 0.0000 |
| 93.31 | Breakeven 2 | 668.90 | -668.90 | 0.00 | 0.8361 | 0.0000 |
| 96.32 | Breakeven 3 | 367.89 | -367.89 | 0.00 | 0.4599 | 0.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 103.34 | Breakeven 4 | -334.45 | 334.45 | 0.00 | -0.4181 | 0.0000 |
| 106.35 | Breakeven 5 | -635.45 | 635.45 | 0.00 | -0.7943 | 0.0000 |
| 108.00 | Breakeven 6 | -800.00 | 800.00 | 0.00 | -1.0000 | 0.0000 |
| 115.00 | Upside (15%) | -800.00 | 1500.00 | 700.00 | -1.0000 | 0.0648 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 800.00 | -9200.00 | -0.7082 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 800.00 | -700.00 | -0.0648 |
| strike_1 | Breakeven 1 | 92.00 | -8.00% | 800.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 92.00 | -8.00% | 800.00 | 0.00 | 0.0000 |
| breakeven_2 | Breakeven 2 | 93.31 | -6.69% | 668.90 | 0.00 | 0.0000 |
| breakeven_3 | Breakeven 3 | 96.32 | -3.68% | 367.89 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_4 | Breakeven 4 | 103.34 | 3.34% | -334.45 | 0.00 | 0.0000 |
| breakeven_5 | Breakeven 5 | 106.35 | 6.35% | -635.45 | 0.00 | 0.0000 |
| strike_2 | Breakeven 6 | 108.00 | 8.00% | -800.00 | 0.00 | 0.0000 |
| breakeven_6 | Breakeven 6 | 108.00 | 8.00% | -800.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -800.00 | 700.00 | 0.0648 |
| infinity | Stock to Infinity | — | — | -800.00 | 97200.00 | 7.4827 |

---

### Bear Call Spread (ID=15) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [42.0]
- Options Max PnL: 800.0
- Options Min PnL: -800.0
- Combined Max PnL: 24200.0
- Combined Min PnL: -4200.0

**Net Premium:**

- Per Share: -8.0
- Total: -800.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $800.00 | Unlimited |
| Max Loss | -$800.00 | -$4,200.00 |
| Risk Reward | 1.00x | 5.76x |
| Capital Basis | $2,990.00 | $7,990.00 |
| Cost Credit | Credit $800.00 | Credit $800.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.773633
- P(25% Max Profit): 0.443311
- P(50% Max Profit): 0.366799
- P(100% Max Profit): 0.228893
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 42.00 | Breakeven 1 | 800.00 | -800.00 | 0.00 | 1.0000 | 0.0000 |
| 50.00 | Scenario @ 50.00 | 800.00 | 0.00 | 800.00 | 1.0000 | 0.1379 |
| 85.00 | Downside (15%) | 800.00 | 3500.00 | 4300.00 | 1.0000 | 0.7414 |
| 92.00 | Lower Strike | 800.00 | 4200.00 | 5000.00 | 1.0000 | 0.8621 |
| 100.00 | Current Market Price | 0.00 | 5000.00 | 5000.00 | 0.0000 | 0.8621 |
| 108.00 | Upper Strike | -800.00 | 5800.00 | 5000.00 | -1.0000 | 0.8621 |
| 115.00 | Upside (15%) | -800.00 | 6500.00 | 5700.00 | -1.0000 | 0.9828 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 800.00 | -4200.00 | -0.5257 |
| breakeven_1 | Breakeven 1 | 42.00 | -58.00% | 800.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 800.00 | 4300.00 | 0.7414 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 800.00 | 5000.00 | 0.8621 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 0.8621 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -800.00 | 5000.00 | 0.8621 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -800.00 | 5700.00 | 0.9828 |
| infinity | Stock to Infinity | — | — | -800.00 | 102200.00 | 12.7910 |

---

### Bear Call Spread (ID=15) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [123.0]
- Options Max PnL: 800.0
- Options Min PnL: -800.0
- Combined Max PnL: 17700.0
- Combined Min PnL: -10700.0

**Net Premium:**

- Per Share: -8.0
- Total: -800.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $800.00 | Unlimited |
| Max Loss | -$800.00 | -$10,700.00 |
| Risk Reward | 1.00x | 1.65x |
| Capital Basis | $2,990.00 | $14,490.00 |
| Cost Credit | Credit $800.00 | Credit $800.00 |
| Pop | 2.0% | 2.0% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 0.020424
- Assignment Prob: 0.773633
- P(25% Max Profit): 0.443311
- P(50% Max Profit): 0.366799
- P(100% Max Profit): 0.228893
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 800.00 | -3000.00 | -2200.00 | 1.0000 | -0.1789 |
| 92.00 | Lower Strike | 800.00 | -2300.00 | -1500.00 | 1.0000 | -0.1220 |
| 100.00 | Current Market Price | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.1220 |
| 108.00 | Upper Strike | -800.00 | -700.00 | -1500.00 | -1.0000 | -0.1220 |
| 115.00 | Upside (15%) | -800.00 | 0.00 | -800.00 | -1.0000 | -0.0650 |
| 123.00 | Breakeven 1 | -800.00 | 800.00 | 0.00 | -1.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 800.00 | -10700.00 | -0.7384 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 800.00 | -2200.00 | -0.1789 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 800.00 | -1500.00 | -0.1220 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.1220 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -800.00 | -1500.00 | -0.1220 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -800.00 | -800.00 | -0.0650 |
| breakeven_1 | Breakeven 1 | 123.00 | 23.00% | -800.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | -800.00 | 95700.00 | 6.6046 |

---

### Bull Put Spread (ID=16) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 108.00 | 9.90 | 100 |
| 2 | PUT | Long 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [100.0]
- Options Max PnL: 800.0
- Options Min PnL: -800.0
- Combined Max PnL: 800.0
- Combined Min PnL: -800.0

**Net Premium:**

- Per Share: -8.0
- Total: -800.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $800.00 | $800.00 |
| Max Loss | -$800.00 | -$800.00 |
| Risk Reward | 1.00x | 1.00x |
| Capital Basis | $800.00 | $800.00 |
| Cost Credit | Credit $800.00 | Credit $800.00 |
| Pop | 47.9% | 47.9% |
| Margin Proxy | 800.0 | — |

**Probabilities:**

- PoP (raw): 0.47931
- Assignment Prob: 0.786086
- P(25% Max Profit): 0.404161
- P(50% Max Profit): 0.33376
- P(100% Max Profit): 0.215999
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -800.00 | 0.00 | -800.00 | -1.0000 | -1.0000 |
| 92.00 | Lower Strike | -800.00 | 0.00 | -800.00 | -1.0000 | -1.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | 800.00 | 0.00 | 800.00 | 1.0000 | 1.0000 |
| 115.00 | Upside (15%) | 800.00 | 0.00 | 800.00 | 1.0000 | 1.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -800.00 | -800.00 | -1.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -800.00 | -800.00 | -1.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -800.00 | -800.00 | -1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 800.00 | 800.00 | 1.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 800.00 | 800.00 | 1.0000 |
| infinity | Stock to Infinity | — | — | 800.00 | 800.00 | 1.0000 |

---

### Bull Put Spread (ID=16) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 108.00 | 9.90 | 100 |
| 2 | PUT | Long 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [100.0]
- Options Max PnL: 800.0
- Options Min PnL: -800.0
- Combined Max PnL: 20800.0
- Combined Min PnL: -10800.0

**Net Premium:**

- Per Share: -8.0
- Total: -800.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $800.00 | Unlimited |
| Max Loss | -$800.00 | -$10,800.00 |
| Risk Reward | 1.00x | 1.93x |
| Capital Basis | $2,990.00 | $12,990.00 |
| Cost Credit | Credit $800.00 | Credit $800.00 |
| Pop | 47.9% | 47.9% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 0.47931
- Assignment Prob: 0.786086
- P(25% Max Profit): 0.404161
- P(50% Max Profit): 0.33376
- P(100% Max Profit): 0.215999
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -800.00 | -1500.00 | -2300.00 | -1.0000 | -0.2130 |
| 92.00 | Lower Strike | -800.00 | -800.00 | -1600.00 | -1.0000 | -0.1481 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | 800.00 | 800.00 | 1600.00 | 1.0000 | 0.1481 |
| 115.00 | Upside (15%) | 800.00 | 1500.00 | 2300.00 | 1.0000 | 0.2130 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -800.00 | -10800.00 | -0.8314 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -800.00 | -2300.00 | -0.2130 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -800.00 | -1600.00 | -0.1481 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 800.00 | 1600.00 | 0.1481 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 800.00 | 2300.00 | 0.2130 |
| infinity | Stock to Infinity | — | — | 800.00 | 98800.00 | 7.6059 |

---

### Bull Put Spread (ID=16) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 108.00 | 9.90 | 100 |
| 2 | PUT | Long 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [58.0]
- Options Max PnL: 800.0
- Options Min PnL: -800.0
- Combined Max PnL: 25800.0
- Combined Min PnL: -5800.0

**Net Premium:**

- Per Share: -8.0
- Total: -800.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $800.00 | Unlimited |
| Max Loss | -$800.00 | -$5,800.00 |
| Risk Reward | 1.00x | 4.45x |
| Capital Basis | $2,990.00 | $7,990.00 |
| Cost Credit | Credit $800.00 | Credit $800.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.786086
- P(25% Max Profit): 0.404161
- P(50% Max Profit): 0.33376
- P(100% Max Profit): 0.215999
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -800.00 | 0.00 | -800.00 | -1.0000 | -0.1379 |
| 58.00 | Breakeven 1 | -800.00 | 800.00 | 0.00 | -1.0000 | 0.0000 |
| 85.00 | Downside (15%) | -800.00 | 3500.00 | 2700.00 | -1.0000 | 0.4655 |
| 92.00 | Lower Strike | -800.00 | 4200.00 | 3400.00 | -1.0000 | 0.5862 |
| 100.00 | Current Market Price | 0.00 | 5000.00 | 5000.00 | 0.0000 | 0.8621 |
| 108.00 | Upper Strike | 800.00 | 5800.00 | 6600.00 | 1.0000 | 1.1379 |
| 115.00 | Upside (15%) | 800.00 | 6500.00 | 7300.00 | 1.0000 | 1.2586 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -800.00 | -5800.00 | -0.7259 |
| breakeven_1 | Breakeven 1 | 58.00 | -42.00% | -800.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -800.00 | 2700.00 | 0.4655 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -800.00 | 3400.00 | 0.5862 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 0.8621 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 800.00 | 6600.00 | 1.1379 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 800.00 | 7300.00 | 1.2586 |
| infinity | Stock to Infinity | — | — | 800.00 | 103800.00 | 12.9912 |

---

### Bull Put Spread (ID=16) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 108.00 | 9.90 | 100 |
| 2 | PUT | Long 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [107.5]
- Options Max PnL: 800.0
- Options Min PnL: -800.0
- Combined Max PnL: 19300.0
- Combined Min PnL: -12300.0

**Net Premium:**

- Per Share: -8.0
- Total: -800.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $800.00 | Unlimited |
| Max Loss | -$800.00 | -$12,300.00 |
| Risk Reward | 1.00x | 1.57x |
| Capital Basis | $2,990.00 | $14,490.00 |
| Cost Credit | Credit $800.00 | Credit $800.00 |
| Pop | 22.7% | 22.7% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 0.227159
- Assignment Prob: 0.786086
- P(25% Max Profit): 0.404161
- P(50% Max Profit): 0.33376
- P(100% Max Profit): 0.215999
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -800.00 | -3000.00 | -3800.00 | -1.0000 | -0.3089 |
| 92.00 | Lower Strike | -800.00 | -2300.00 | -3100.00 | -1.0000 | -0.2520 |
| 100.00 | Current Market Price | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.1220 |
| 107.50 | Breakeven 1 | 750.00 | -750.00 | 0.00 | 0.9375 | 0.0000 |
| 108.00 | Upper Strike | 800.00 | -700.00 | 100.00 | 1.0000 | 0.0081 |
| 115.00 | Upside (15%) | 800.00 | 0.00 | 800.00 | 1.0000 | 0.0650 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -800.00 | -12300.00 | -0.8489 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -800.00 | -3800.00 | -0.3089 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -800.00 | -3100.00 | -0.2520 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.1220 |
| breakeven_1 | Breakeven 1 | 107.50 | 7.50% | 750.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 800.00 | 100.00 | 0.0081 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 800.00 | 800.00 | 0.0650 |
| infinity | Stock to Infinity | — | — | 800.00 | 97300.00 | 6.7150 |

---

### Call Ratio Backspread (ID=17) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Long 2 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [98.1, 117.9]
- Options Max PnL: 18210.0
- Options Min PnL: -990.0
- Combined Max PnL: 18210.0
- Combined Min PnL: -990.0

**Net Premium:**

- Per Share: -6.1
- Total: -610.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$990.00 | -$990.00 |
| Risk Reward | 18.39x | 18.39x |
| Capital Basis | $2,990.00 | $2,990.00 |
| Cost Credit | Credit $610.00 | Credit $610.00 |
| Pop | 49.8% | 49.8% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 0.497971
- Assignment Prob: 0.773633
- P(25% Max Profit): 1e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 610.00 | 0.00 | 610.00 | 0.6162 | 0.6162 |
| 92.00 | Lower Strike | 610.00 | 0.00 | 610.00 | 0.6162 | 0.6162 |
| 98.10 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | -190.00 | 0.00 | -190.00 | -0.1919 | -0.1919 |
| 108.00 | Upper Strike | -990.00 | 0.00 | -990.00 | -1.0000 | -1.0000 |
| 115.00 | Upside (15%) | -290.00 | 0.00 | -290.00 | -0.2929 | -0.2929 |
| 117.90 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 610.00 | 610.00 | 0.2040 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 610.00 | 610.00 | 0.6162 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 610.00 | 610.00 | 0.6162 |
| breakeven_1 | Breakeven 1 | 98.10 | -1.90% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | -190.00 | -0.1919 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -990.00 | -990.00 | -1.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -290.00 | -290.00 | -0.2929 |
| breakeven_2 | Breakeven 2 | 117.90 | 17.90% | 0.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 96210.00 | 96210.00 | 32.1773 |

---

### Call Ratio Backspread (ID=17) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Long 2 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [108.95]
- Options Max PnL: 18210.0
- Options Min PnL: -990.0
- Combined Max PnL: 38210.0
- Combined Min PnL: -9390.0

**Net Premium:**

- Per Share: -6.1
- Total: -610.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$990.00 | -$9,390.00 |
| Risk Reward | 18.39x | 4.07x |
| Capital Basis | $2,990.00 | $12,990.00 |
| Cost Credit | Credit $610.00 | Credit $610.00 |
| Pop | 19.0% | 19.0% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 0.19018
- Assignment Prob: 0.773633
- P(25% Max Profit): 1e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 610.00 | -1500.00 | -890.00 | 0.6162 | -0.0810 |
| 92.00 | Lower Strike | 610.00 | -800.00 | -190.00 | 0.6162 | -0.0173 |
| 100.00 | Current Market Price | -190.00 | 0.00 | -190.00 | -0.1919 | -0.0173 |
| 108.00 | Upper Strike | -990.00 | 800.00 | -190.00 | -1.0000 | -0.0173 |
| 108.95 | Breakeven 1 | -895.00 | 895.00 | 0.00 | -0.9040 | 0.0000 |
| 115.00 | Upside (15%) | -290.00 | 1500.00 | 1210.00 | -0.2929 | 0.1101 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 610.00 | -9390.00 | -0.7229 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 610.00 | -890.00 | -0.0810 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 610.00 | -190.00 | -0.0173 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | -190.00 | -0.0173 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -990.00 | -190.00 | -0.0173 |
| breakeven_1 | Breakeven 1 | 108.95 | 8.95% | -895.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -290.00 | 1210.00 | 0.1101 |
| infinity | Stock to Infinity | — | — | 96210.00 | 194210.00 | 14.9507 |

---

### Call Ratio Backspread (ID=17) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Long 2 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [43.9]
- Options Max PnL: 18210.0
- Options Min PnL: -990.0
- Combined Max PnL: 43210.0
- Combined Min PnL: -4390.0

**Net Premium:**

- Per Share: -6.1
- Total: -610.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$990.00 | -$4,390.00 |
| Risk Reward | 18.39x | 9.84x |
| Capital Basis | $2,990.00 | $7,990.00 |
| Cost Credit | Credit $610.00 | Credit $610.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.773633
- P(25% Max Profit): 1e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 43.90 | Breakeven 1 | 610.00 | -610.00 | -0.00 | 0.6162 | -0.0000 |
| 50.00 | Scenario @ 50.00 | 610.00 | 0.00 | 610.00 | 0.6162 | 0.1018 |
| 85.00 | Downside (15%) | 610.00 | 3500.00 | 4110.00 | 0.6162 | 0.6861 |
| 92.00 | Lower Strike | 610.00 | 4200.00 | 4810.00 | 0.6162 | 0.8030 |
| 100.00 | Current Market Price | -190.00 | 5000.00 | 4810.00 | -0.1919 | 0.8030 |
| 108.00 | Upper Strike | -990.00 | 5800.00 | 4810.00 | -1.0000 | 0.8030 |
| 115.00 | Upside (15%) | -290.00 | 6500.00 | 6210.00 | -0.2929 | 1.0367 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 610.00 | -4390.00 | -0.5494 |
| breakeven_1 | Breakeven 1 | 43.90 | -56.10% | 610.00 | -0.00 | -0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 610.00 | 4110.00 | 0.6861 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 610.00 | 4810.00 | 0.8030 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | 4810.00 | 0.8030 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -990.00 | 4810.00 | 0.8030 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -290.00 | 6210.00 | 1.0367 |
| infinity | Stock to Infinity | — | — | 96210.00 | 199210.00 | 24.9324 |

---

### Call Ratio Backspread (ID=17) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Long 2 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [116.45]
- Options Max PnL: 18210.0
- Options Min PnL: -990.0
- Combined Max PnL: 36710.0
- Combined Min PnL: -10890.0

**Net Premium:**

- Per Share: -6.1
- Total: -610.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$990.00 | -$10,890.00 |
| Risk Reward | 18.39x | 3.37x |
| Capital Basis | $2,990.00 | $14,490.00 |
| Cost Credit | Credit $610.00 | Credit $610.00 |
| Pop | 6.4% | 6.4% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 0.064482
- Assignment Prob: 0.773633
- P(25% Max Profit): 1e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 610.00 | -3000.00 | -2390.00 | 0.6162 | -0.1914 |
| 92.00 | Lower Strike | 610.00 | -2300.00 | -1690.00 | 0.6162 | -0.1353 |
| 100.00 | Current Market Price | -190.00 | -1500.00 | -1690.00 | -0.1919 | -0.1353 |
| 108.00 | Upper Strike | -990.00 | -700.00 | -1690.00 | -1.0000 | -0.1353 |
| 115.00 | Upside (15%) | -290.00 | 0.00 | -290.00 | -0.2929 | -0.0232 |
| 116.45 | Breakeven 1 | -145.00 | 145.00 | 0.00 | -0.1465 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 610.00 | -10890.00 | -0.7516 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 610.00 | -2390.00 | -0.1914 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 610.00 | -1690.00 | -0.1353 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | -1690.00 | -0.1353 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -990.00 | -1690.00 | -0.1353 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -290.00 | -290.00 | -0.0232 |
| breakeven_1 | Breakeven 1 | 116.45 | 16.45% | -145.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 96210.00 | 192710.00 | 13.2995 |

---

### Put Ratio Backspread (ID=18) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 108.00 | 9.90 | 100 |
| 2 | PUT | Long 2 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [82.1, 101.9]
- Options Max PnL: 8210.0
- Options Min PnL: -990.0
- Combined Max PnL: 8210.0
- Combined Min PnL: -990.0

**Net Premium:**

- Per Share: -6.1
- Total: -610.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $8,210.00 | $8,210.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 8.29x | 8.29x |
| Capital Basis | $2,990.00 | $2,990.00 |
| Cost Credit | Credit $610.00 | Credit $610.00 |
| Pop | 44.0% | 44.0% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 0.440196
- Assignment Prob: 0.786086
- P(25% Max Profit): 2e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 82.10 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 85.00 | Downside (15%) | -290.00 | 0.00 | -290.00 | -0.2929 | -0.2929 |
| 92.00 | Lower Strike | -990.00 | 0.00 | -990.00 | -1.0000 | -1.0000 |
| 100.00 | Current Market Price | -190.00 | 0.00 | -190.00 | -0.1919 | -0.1919 |
| 101.90 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | 610.00 | 0.00 | 610.00 | 0.6162 | 0.6162 |
| 115.00 | Upside (15%) | 610.00 | 0.00 | 610.00 | 0.6162 | 0.6162 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8210.00 | 8210.00 | 2.7458 |
| breakeven_1 | Breakeven 1 | 82.10 | -17.90% | 0.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -290.00 | -290.00 | -0.2929 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -990.00 | -990.00 | -1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | -190.00 | -0.1919 |
| breakeven_2 | Breakeven 2 | 101.90 | 1.90% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 610.00 | 610.00 | 0.6162 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 610.00 | 610.00 | 0.6162 |
| infinity | Stock to Infinity | — | — | Unlimited | 610.00 | 0.2040 |

---

### Put Ratio Backspread (ID=18) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 108.00 | 9.90 | 100 |
| 2 | PUT | Long 2 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [100.95]
- Options Max PnL: 8210.0
- Options Min PnL: -990.0
- Combined Max PnL: 20610.0
- Combined Min PnL: -1790.0

**Net Premium:**

- Per Share: -6.1
- Total: -610.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $8,210.00 | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 8.29x | 11.51x |
| Capital Basis | $2,990.00 | $12,990.00 |
| Cost Credit | Credit $610.00 | Credit $610.00 |
| Pop | 44.3% | 44.3% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 0.443158
- Assignment Prob: 0.786086
- P(25% Max Profit): 2e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -290.00 | -1500.00 | -1790.00 | -0.2929 | -0.1629 |
| 92.00 | Lower Strike | -990.00 | -800.00 | -1790.00 | -1.0000 | -0.1629 |
| 100.00 | Current Market Price | -190.00 | 0.00 | -190.00 | -0.1919 | -0.0173 |
| 100.95 | Breakeven 1 | -95.00 | 95.00 | 0.00 | -0.0960 | 0.0000 |
| 108.00 | Upper Strike | 610.00 | 800.00 | 1410.00 | 0.6162 | 0.1283 |
| 115.00 | Upside (15%) | 610.00 | 1500.00 | 2110.00 | 0.6162 | 0.1920 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8210.00 | -1790.00 | -0.1378 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -290.00 | -1790.00 | -0.1629 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -990.00 | -1790.00 | -0.1629 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | -190.00 | -0.0173 |
| breakeven_1 | Breakeven 1 | 100.95 | 0.95% | -95.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 610.00 | 1410.00 | 0.1283 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 610.00 | 2110.00 | 0.1920 |
| infinity | Stock to Infinity | — | — | Unlimited | 98610.00 | 7.5912 |

---

### Put Ratio Backspread (ID=18) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 108.00 | 9.90 | 100 |
| 2 | PUT | Long 2 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: []
- Options Max PnL: 8210.0
- Options Min PnL: -990.0
- Combined Max PnL: 25610.0
- Combined Min PnL: 3210.0

**Net Premium:**

- Per Share: -6.1
- Total: -610.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $8,210.00 | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 8.29x | 7.98x |
| Capital Basis | $2,990.00 | $7,990.00 |
| Cost Credit | Credit $610.00 | Credit $610.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.786086
- P(25% Max Profit): 2e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | 3210.00 | 0.00 | 3210.00 | 3.2424 | 0.5359 |
| 85.00 | Downside (15%) | -290.00 | 3500.00 | 3210.00 | -0.2929 | 0.5359 |
| 92.00 | Lower Strike | -990.00 | 4200.00 | 3210.00 | -1.0000 | 0.5359 |
| 100.00 | Current Market Price | -190.00 | 5000.00 | 4810.00 | -0.1919 | 0.8030 |
| 108.00 | Upper Strike | 610.00 | 5800.00 | 6410.00 | 0.6162 | 1.0701 |
| 115.00 | Upside (15%) | 610.00 | 6500.00 | 7110.00 | 0.6162 | 1.1870 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8210.00 | 3210.00 | 0.4018 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -290.00 | 3210.00 | 0.5359 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -990.00 | 3210.00 | 0.5359 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | 4810.00 | 0.8030 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 610.00 | 6410.00 | 1.0701 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 610.00 | 7110.00 | 1.1870 |
| infinity | Stock to Infinity | — | — | Unlimited | 103610.00 | 12.9675 |

---

### Put Ratio Backspread (ID=18) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 108.00 | 9.90 | 100 |
| 2 | PUT | Long 2 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [108.9]
- Options Max PnL: 8210.0
- Options Min PnL: -990.0
- Combined Max PnL: 19110.0
- Combined Min PnL: -3290.0

**Net Premium:**

- Per Share: -6.1
- Total: -610.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $8,210.00 | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 8.29x | 5.81x |
| Capital Basis | $2,990.00 | $14,490.00 |
| Cost Credit | Credit $610.00 | Credit $610.00 |
| Pop | 19.1% | 19.1% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 0.191382
- Assignment Prob: 0.786086
- P(25% Max Profit): 2e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -290.00 | -3000.00 | -3290.00 | -0.2929 | -0.2634 |
| 92.00 | Lower Strike | -990.00 | -2300.00 | -3290.00 | -1.0000 | -0.2634 |
| 100.00 | Current Market Price | -190.00 | -1500.00 | -1690.00 | -0.1919 | -0.1353 |
| 108.00 | Upper Strike | 610.00 | -700.00 | -90.00 | 0.6162 | -0.0072 |
| 108.90 | Breakeven 1 | 610.00 | -610.00 | 0.00 | 0.6162 | 0.0000 |
| 115.00 | Upside (15%) | 610.00 | 0.00 | 610.00 | 0.6162 | 0.0488 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8210.00 | -3290.00 | -0.2271 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -290.00 | -3290.00 | -0.2634 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -990.00 | -3290.00 | -0.2634 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | -1690.00 | -0.1353 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 610.00 | -90.00 | -0.0072 |
| breakeven_1 | Breakeven 1 | 108.90 | 8.90% | 610.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 610.00 | 610.00 | 0.0488 |
| infinity | Stock to Infinity | — | — | Unlimited | 97110.00 | 6.7019 |

---

### Call Ratio Spread (ID=19) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Short 2 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [98.1, 117.9]
- Options Max PnL: 990.0
- Options Min PnL: -18210.0
- Combined Max PnL: 990.0
- Combined Min PnL: -18210.0

**Net Premium:**

- Per Share: 6.1
- Total: 610.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $990.00 | $990.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.05x | 0.05x |
| Capital Basis | $2,780.00 | $2,780.00 |
| Cost Credit | Debit $610.00 | Debit $610.00 |
| Pop | 50.2% | 50.2% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.502029
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.381423
- P(50% Max Profit): 0.256074
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -610.00 | 0.00 | -610.00 | -0.2194 | -0.2194 |
| 92.00 | Lower Strike | -610.00 | 0.00 | -610.00 | -0.2194 | -0.2194 |
| 98.10 | Breakeven 1 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0683 | 0.0683 |
| 108.00 | Upper Strike | 990.00 | 0.00 | 990.00 | 0.3561 | 0.3561 |
| 115.00 | Upside (15%) | 290.00 | 0.00 | 290.00 | 0.1043 | 0.1043 |
| 117.90 | Breakeven 2 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -610.00 | -610.00 | -0.2194 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -610.00 | -610.00 | -0.2194 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -610.00 | -610.00 | -0.2194 |
| breakeven_1 | Breakeven 1 | 98.10 | -1.90% | -0.00 | -0.00 | -0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0683 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 990.00 | 990.00 | 0.3561 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 290.00 | 290.00 | 0.1043 |
| breakeven_2 | Breakeven 2 | 117.90 | 17.90% | -0.00 | -0.00 | -0.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | -96210.00 | -34.6079 |

---

### Call Ratio Spread (ID=19) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Short 2 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [99.05]
- Options Max PnL: 990.0
- Options Min PnL: -18210.0
- Combined Max PnL: 1790.0
- Combined Min PnL: -10610.0

**Net Premium:**

- Per Share: 6.1
- Total: 610.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $990.00 | $1,790.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.05x | 0.17x |
| Capital Basis | $2,780.00 | $12,780.00 |
| Cost Credit | Debit $610.00 | Debit $610.00 |
| Pop | 51.6% | 51.6% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.515942
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.381423
- P(50% Max Profit): 0.256074
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -610.00 | -1500.00 | -2110.00 | -0.2194 | -0.1651 |
| 92.00 | Lower Strike | -610.00 | -800.00 | -1410.00 | -0.2194 | -0.1103 |
| 99.05 | Breakeven 1 | 95.00 | -95.00 | -0.00 | 0.0342 | -0.0000 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0683 | 0.0149 |
| 108.00 | Upper Strike | 990.00 | 800.00 | 1790.00 | 0.3561 | 0.1401 |
| 115.00 | Upside (15%) | 290.00 | 1500.00 | 1790.00 | 0.1043 | 0.1401 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -610.00 | -10610.00 | -0.8302 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -610.00 | -2110.00 | -0.1651 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -610.00 | -1410.00 | -0.1103 |
| breakeven_1 | Breakeven 1 | 99.05 | -0.95% | 95.00 | -0.00 | -0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0149 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 990.00 | 1790.00 | 0.1401 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 290.00 | 1790.00 | 0.1401 |
| infinity | Stock to Infinity | — | — | Unlimited | 1790.00 | 0.1401 |

---

### Call Ratio Spread (ID=19) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Short 2 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [56.1]
- Options Max PnL: 990.0
- Options Min PnL: -18210.0
- Combined Max PnL: 6790.0
- Combined Min PnL: -5610.0

**Net Premium:**

- Per Share: 6.1
- Total: 610.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $990.00 | $6,790.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.05x | 1.21x |
| Capital Basis | $2,780.00 | $7,780.00 |
| Cost Credit | Debit $610.00 | Debit $610.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.381423
- P(50% Max Profit): 0.256074
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -610.00 | 0.00 | -610.00 | -0.2194 | -0.0784 |
| 56.10 | Breakeven 1 | -610.00 | 610.00 | 0.00 | -0.2194 | 0.0000 |
| 85.00 | Downside (15%) | -610.00 | 3500.00 | 2890.00 | -0.2194 | 0.3715 |
| 92.00 | Lower Strike | -610.00 | 4200.00 | 3590.00 | -0.2194 | 0.4614 |
| 100.00 | Current Market Price | 190.00 | 5000.00 | 5190.00 | 0.0683 | 0.6671 |
| 108.00 | Upper Strike | 990.00 | 5800.00 | 6790.00 | 0.3561 | 0.8728 |
| 115.00 | Upside (15%) | 290.00 | 6500.00 | 6790.00 | 0.1043 | 0.8728 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -610.00 | -5610.00 | -0.7211 |
| breakeven_1 | Breakeven 1 | 56.10 | -43.90% | -610.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -610.00 | 2890.00 | 0.3715 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -610.00 | 3590.00 | 0.4614 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 5190.00 | 0.6671 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 990.00 | 6790.00 | 0.8728 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 290.00 | 6790.00 | 0.8728 |
| infinity | Stock to Infinity | — | — | Unlimited | 6790.00 | 0.8728 |

---

### Call Ratio Spread (ID=19) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Short 2 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [106.55]
- Options Max PnL: 990.0
- Options Min PnL: -18210.0
- Combined Max PnL: 290.0
- Combined Min PnL: -12110.0

**Net Premium:**

- Per Share: 6.1
- Total: 610.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $990.00 | $290.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.05x | 0.02x |
| Capital Basis | $2,780.00 | $14,280.00 |
| Cost Credit | Debit $610.00 | Debit $610.00 |
| Pop | 25.4% | 25.4% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.253738
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.381423
- P(50% Max Profit): 0.256074
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -610.00 | -3000.00 | -3610.00 | -0.2194 | -0.2528 |
| 92.00 | Lower Strike | -610.00 | -2300.00 | -2910.00 | -0.2194 | -0.2038 |
| 100.00 | Current Market Price | 190.00 | -1500.00 | -1310.00 | 0.0683 | -0.0917 |
| 106.55 | Breakeven 1 | 845.00 | -845.00 | 0.00 | 0.3040 | 0.0000 |
| 108.00 | Upper Strike | 990.00 | -700.00 | 290.00 | 0.3561 | 0.0203 |
| 115.00 | Upside (15%) | 290.00 | 0.00 | 290.00 | 0.1043 | 0.0203 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -610.00 | -12110.00 | -0.8480 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -610.00 | -3610.00 | -0.2528 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -610.00 | -2910.00 | -0.2038 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | -1310.00 | -0.0917 |
| breakeven_1 | Breakeven 1 | 106.55 | 6.55% | 845.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 990.00 | 290.00 | 0.0203 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 290.00 | 290.00 | 0.0203 |
| infinity | Stock to Infinity | — | — | Unlimited | 290.00 | 0.0203 |

---

### Put Ratio Spread (ID=20) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 108.00 | 9.90 | 100 |
| 2 | PUT | Short 2 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [82.1, 101.9]
- Options Max PnL: 990.0
- Options Min PnL: -8210.0
- Combined Max PnL: 990.0
- Combined Min PnL: -8210.0

**Net Premium:**

- Per Share: 6.1
- Total: 610.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $990.00 | $990.00 |
| Max Loss | -$8,210.00 | -$8,210.00 |
| Risk Reward | 0.12x | 0.12x |
| Capital Basis | $8,210.00 | $8,210.00 |
| Cost Credit | Debit $610.00 | Debit $610.00 |
| Pop | 56.0% | 56.0% |
| Margin Proxy | 8210.0 | — |

**Probabilities:**

- PoP (raw): 0.559804
- Assignment Prob: 0.226367
- P(25% Max Profit): 0.439314
- P(50% Max Profit): 0.303043
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 82.10 | Breakeven 1 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 85.00 | Downside (15%) | 290.00 | 0.00 | 290.00 | 0.0353 | 0.0353 |
| 92.00 | Lower Strike | 990.00 | 0.00 | 990.00 | 0.1206 | 0.1206 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0231 | 0.0231 |
| 101.90 | Breakeven 2 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 108.00 | Upper Strike | -610.00 | 0.00 | -610.00 | -0.0743 | -0.0743 |
| 115.00 | Upside (15%) | -610.00 | 0.00 | -610.00 | -0.0743 | -0.0743 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8210.00 | -8210.00 | -1.0000 |
| breakeven_1 | Breakeven 1 | 82.10 | -17.90% | -0.00 | -0.00 | -0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 290.00 | 290.00 | 0.0353 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 990.00 | 990.00 | 0.1206 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0231 |
| breakeven_2 | Breakeven 2 | 101.90 | 1.90% | -0.00 | -0.00 | -0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -610.00 | -610.00 | -0.0743 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -610.00 | -610.00 | -0.0743 |
| infinity | Stock to Infinity | — | — | -610.00 | -610.00 | -0.0743 |

---

### Put Ratio Spread (ID=20) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 108.00 | 9.90 | 100 |
| 2 | PUT | Short 2 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [91.05]
- Options Max PnL: 990.0
- Options Min PnL: -8210.0
- Combined Max PnL: 19390.0
- Combined Min PnL: -18210.0

**Net Premium:**

- Per Share: 6.1
- Total: 610.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $990.00 | Unlimited |
| Max Loss | -$8,210.00 | -$18,210.00 |
| Risk Reward | 0.12x | 1.06x |
| Capital Basis | $2,780.00 | $12,780.00 |
| Cost Credit | Debit $610.00 | Debit $610.00 |
| Pop | 80.3% | 80.3% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.802561
- Assignment Prob: 0.226367
- P(25% Max Profit): 0.439314
- P(50% Max Profit): 0.303043
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 290.00 | -1500.00 | -1210.00 | 0.0353 | -0.0664 |
| 91.05 | Breakeven 1 | 895.00 | -895.00 | -0.00 | 0.1090 | -0.0000 |
| 92.00 | Lower Strike | 990.00 | -800.00 | 190.00 | 0.1206 | 0.0104 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0231 | 0.0104 |
| 108.00 | Upper Strike | -610.00 | 800.00 | 190.00 | -0.0743 | 0.0104 |
| 115.00 | Upside (15%) | -610.00 | 1500.00 | 890.00 | -0.0743 | 0.0489 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8210.00 | -18210.00 | -1.4249 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 290.00 | -1210.00 | -0.0664 |
| breakeven_1 | Breakeven 1 | 91.05 | -8.95% | 895.00 | -0.00 | -0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 990.00 | 190.00 | 0.0104 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0104 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -610.00 | 190.00 | 0.0104 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -610.00 | 890.00 | 0.0489 |
| infinity | Stock to Infinity | — | — | -610.00 | 97390.00 | 7.6205 |

---

### Put Ratio Spread (ID=20) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 108.00 | 9.90 | 100 |
| 2 | PUT | Short 2 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [66.05]
- Options Max PnL: 990.0
- Options Min PnL: -8210.0
- Combined Max PnL: 24390.0
- Combined Min PnL: -13210.0

**Net Premium:**

- Per Share: 6.1
- Total: 610.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $990.00 | Unlimited |
| Max Loss | -$8,210.00 | -$13,210.00 |
| Risk Reward | 0.12x | 1.85x |
| Capital Basis | $2,780.00 | $7,780.00 |
| Cost Credit | Debit $610.00 | Debit $610.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.99996
- Assignment Prob: 0.226367
- P(25% Max Profit): 0.439314
- P(50% Max Profit): 0.303043
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -3210.00 | 0.00 | -3210.00 | -0.3910 | -0.2430 |
| 66.05 | Breakeven 1 | -1605.00 | 1605.00 | -0.00 | -0.1955 | -0.0000 |
| 85.00 | Downside (15%) | 290.00 | 3500.00 | 3790.00 | 0.0353 | 0.2869 |
| 92.00 | Lower Strike | 990.00 | 4200.00 | 5190.00 | 0.1206 | 0.3929 |
| 100.00 | Current Market Price | 190.00 | 5000.00 | 5190.00 | 0.0231 | 0.3929 |
| 108.00 | Upper Strike | -610.00 | 5800.00 | 5190.00 | -0.0743 | 0.3929 |
| 115.00 | Upside (15%) | -610.00 | 6500.00 | 5890.00 | -0.0743 | 0.4459 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8210.00 | -13210.00 | -1.6979 |
| breakeven_1 | Breakeven 1 | 66.05 | -33.95% | -1605.00 | -0.00 | -0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 290.00 | 3790.00 | 0.2869 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 990.00 | 5190.00 | 0.3929 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 5190.00 | 0.3929 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -610.00 | 5190.00 | 0.3929 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -610.00 | 5890.00 | 0.4459 |
| infinity | Stock to Infinity | — | — | -610.00 | 102390.00 | 13.1607 |

---

### Put Ratio Spread (ID=20) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 108.00 | 9.90 | 100 |
| 2 | PUT | Short 2 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [121.1]
- Options Max PnL: 990.0
- Options Min PnL: -8210.0
- Combined Max PnL: 17890.0
- Combined Min PnL: -19710.0

**Net Premium:**

- Per Share: 6.1
- Total: 610.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $990.00 | Unlimited |
| Max Loss | -$8,210.00 | -$19,710.00 |
| Risk Reward | 0.12x | 0.91x |
| Capital Basis | $2,780.00 | $14,280.00 |
| Cost Credit | Debit $610.00 | Debit $610.00 |
| Pop | 2.9% | 2.9% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.029034
- Assignment Prob: 0.226367
- P(25% Max Profit): 0.439314
- P(50% Max Profit): 0.303043
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 290.00 | -3000.00 | -2710.00 | 0.0353 | -0.1375 |
| 92.00 | Lower Strike | 990.00 | -2300.00 | -1310.00 | 0.1206 | -0.0665 |
| 100.00 | Current Market Price | 190.00 | -1500.00 | -1310.00 | 0.0231 | -0.0665 |
| 108.00 | Upper Strike | -610.00 | -700.00 | -1310.00 | -0.0743 | -0.0665 |
| 115.00 | Upside (15%) | -610.00 | 0.00 | -610.00 | -0.0743 | -0.0309 |
| 121.10 | Breakeven 1 | -610.00 | 610.00 | 0.00 | -0.0743 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8210.00 | -19710.00 | -1.3803 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 290.00 | -2710.00 | -0.1375 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 990.00 | -1310.00 | -0.0665 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | -1310.00 | -0.0665 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -610.00 | -1310.00 | -0.0665 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -610.00 | -610.00 | -0.0309 |
| breakeven_1 | Breakeven 1 | 121.10 | 21.10% | -610.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | -610.00 | 95890.00 | 6.7150 |

---

### Bull Call Ladder (ID=21) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 85.00 | 16.38 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |
| 3 | CALL | Short 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [97.5, 117.5]
- Options Max PnL: 250.0
- Options Min PnL: -18250.0
- Combined Max PnL: 250.0
- Combined Min PnL: -18250.0

**Net Premium:**

- Per Share: 12.5
- Total: 1250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $250.00 | $250.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.01x | 0.01x |
| Capital Basis | $3,388.00 | $3,388.00 |
| Cost Credit | Debit $1,250.00 | Debit $1,250.00 |
| Pop | 52.2% | 52.2% |
| Margin Proxy | 3388.0 | — |

**Probabilities:**

- PoP (raw): 0.521773
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.491659
- P(50% Max Profit): 0.460981
- P(100% Max Profit): 0.399442
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1250.00 | 0.00 | -1250.00 | -0.3689 | -0.3689 |
| 97.50 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | 250.00 | 0.00 | 250.00 | 0.0738 | 0.0738 |
| 115.00 | Upside (15%) | 250.00 | 0.00 | 250.00 | 0.0738 | 0.0738 |
| 115.00 | Upside (15%) | 250.00 | 0.00 | 250.00 | 0.0738 | 0.0738 |
| 117.50 | Breakeven 2 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1250.00 | -1250.00 | -0.3689 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1250.00 | -1250.00 | -0.3689 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1250.00 | -1250.00 | -0.3689 |
| breakeven_1 | Breakeven 1 | 97.50 | -2.50% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 250.00 | 250.00 | 0.0738 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 250.00 | 250.00 | 0.0738 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 250.00 | 250.00 | 0.0738 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 250.00 | 250.00 | 0.0738 |
| breakeven_2 | Breakeven 2 | 117.50 | 17.50% | -0.00 | -0.00 | -0.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | -103250.00 | -30.4752 |

---

### Bull Call Ladder (ID=21) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 85.00 | 16.38 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |
| 3 | CALL | Short 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [98.75]
- Options Max PnL: 250.0
- Options Min PnL: -18250.0
- Combined Max PnL: 1750.0
- Combined Min PnL: -11250.0

**Net Premium:**

- Per Share: 12.5
- Total: 1250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $250.00 | $1,750.00 |
| Max Loss | Unlimited | -$11,250.00 |
| Risk Reward | 0.01x | 0.16x |
| Capital Basis | $18,250.00 | $28,250.00 |
| Cost Credit | Debit $1,250.00 | Debit $1,250.00 |
| Pop | 52.8% | 52.8% |
| Margin Proxy | 18250.0 | — |

**Probabilities:**

- PoP (raw): 0.527575
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.491659
- P(50% Max Profit): 0.460981
- P(100% Max Profit): 0.399442
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1250.00 | -1500.00 | -2750.00 | -0.0685 | -0.0973 |
| 98.75 | Breakeven 1 | 125.00 | -125.00 | 0.00 | 0.0068 | 0.0000 |
| 100.00 | Current Market Price | 250.00 | 0.00 | 250.00 | 0.0137 | 0.0089 |
| 115.00 | Upside (15%) | 250.00 | 1500.00 | 1750.00 | 0.0137 | 0.0619 |
| 115.00 | Upside (15%) | 250.00 | 1500.00 | 1750.00 | 0.0137 | 0.0619 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1250.00 | -11250.00 | -0.3982 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1250.00 | -2750.00 | -0.0973 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1250.00 | -2750.00 | -0.0973 |
| breakeven_1 | Breakeven 1 | 98.75 | -1.25% | 125.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 250.00 | 250.00 | 0.0089 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 250.00 | 250.00 | 0.0089 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 250.00 | 1750.00 | 0.0619 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 250.00 | 1750.00 | 0.0619 |
| infinity | Stock to Infinity | — | — | Unlimited | 1750.00 | 0.0619 |

---

### Bull Call Ladder (ID=21) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 85.00 | 16.38 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |
| 3 | CALL | Short 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [62.5]
- Options Max PnL: 250.0
- Options Min PnL: -18250.0
- Combined Max PnL: 6750.0
- Combined Min PnL: -6250.0

**Net Premium:**

- Per Share: 12.5
- Total: 1250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $250.00 | $6,750.00 |
| Max Loss | Unlimited | -$6,250.00 |
| Risk Reward | 0.01x | 1.08x |
| Capital Basis | $18,250.00 | $23,250.00 |
| Cost Credit | Debit $1,250.00 | Debit $1,250.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 18250.0 | — |

**Probabilities:**

- PoP (raw): 0.999996
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.491659
- P(50% Max Profit): 0.460981
- P(100% Max Profit): 0.399442
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -1250.00 | 0.00 | -1250.00 | -0.0685 | -0.0538 |
| 62.50 | Breakeven 1 | -1250.00 | 1250.00 | 0.00 | -0.0685 | 0.0000 |
| 85.00 | Downside (15%) | -1250.00 | 3500.00 | 2250.00 | -0.0685 | 0.0968 |
| 100.00 | Current Market Price | 250.00 | 5000.00 | 5250.00 | 0.0137 | 0.2258 |
| 115.00 | Upside (15%) | 250.00 | 6500.00 | 6750.00 | 0.0137 | 0.2903 |
| 115.00 | Upside (15%) | 250.00 | 6500.00 | 6750.00 | 0.0137 | 0.2903 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1250.00 | -6250.00 | -0.2688 |
| breakeven_1 | Breakeven 1 | 62.50 | -37.50% | -1250.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1250.00 | 2250.00 | 0.0968 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1250.00 | 2250.00 | 0.0968 |
| spot | Current Market Price | 100.00 | 0.00% | 250.00 | 5250.00 | 0.2258 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 250.00 | 5250.00 | 0.2258 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 250.00 | 6750.00 | 0.2903 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 250.00 | 6750.00 | 0.2903 |
| infinity | Stock to Infinity | — | — | Unlimited | 6750.00 | 0.2903 |

---

### Bull Call Ladder (ID=21) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 85.00 | 16.38 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |
| 3 | CALL | Short 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [112.5]
- Options Max PnL: 250.0
- Options Min PnL: -18250.0
- Combined Max PnL: 250.0
- Combined Min PnL: -12750.0

**Net Premium:**

- Per Share: 12.5
- Total: 1250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $250.00 | $250.00 |
| Max Loss | Unlimited | -$12,750.00 |
| Risk Reward | 0.01x | 0.02x |
| Capital Basis | $18,250.00 | $29,750.00 |
| Cost Credit | Debit $1,250.00 | Debit $1,250.00 |
| Pop | 11.8% | 11.8% |
| Margin Proxy | 18250.0 | — |

**Probabilities:**

- PoP (raw): 0.117822
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.491659
- P(50% Max Profit): 0.460981
- P(100% Max Profit): 0.399442
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1250.00 | -3000.00 | -4250.00 | -0.0685 | -0.1429 |
| 100.00 | Current Market Price | 250.00 | -1500.00 | -1250.00 | 0.0137 | -0.0420 |
| 112.50 | Breakeven 1 | 250.00 | -250.00 | 0.00 | 0.0137 | 0.0000 |
| 115.00 | Upside (15%) | 250.00 | 0.00 | 250.00 | 0.0137 | 0.0084 |
| 115.00 | Upside (15%) | 250.00 | 0.00 | 250.00 | 0.0137 | 0.0084 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1250.00 | -12750.00 | -0.4286 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1250.00 | -4250.00 | -0.1429 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1250.00 | -4250.00 | -0.1429 |
| spot | Current Market Price | 100.00 | 0.00% | 250.00 | -1250.00 | -0.0420 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 250.00 | -1250.00 | -0.0420 |
| breakeven_1 | Breakeven 1 | 112.50 | 12.50% | 250.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 250.00 | 250.00 | 0.0084 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 250.00 | 250.00 | 0.0084 |
| infinity | Stock to Infinity | — | — | Unlimited | 250.00 | 0.0084 |

---

### Bear Put Ladder (ID=22) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 115.00 | 16.38 | 100 |
| 2 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 3 | PUT | Short 1 | 85.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [82.5, 102.5]
- Options Max PnL: 250.0
- Options Min PnL: -8250.0
- Combined Max PnL: 250.0
- Combined Min PnL: -8250.0

**Net Premium:**

- Per Share: 12.5
- Total: 1250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $250.00 | $250.00 |
| Max Loss | -$8,250.00 | -$8,250.00 |
| Risk Reward | 0.03x | 0.03x |
| Capital Basis | $8,250.00 | $8,250.00 |
| Cost Credit | Debit $1,250.00 | Debit $1,250.00 |
| Pop | 57.8% | 57.8% |
| Margin Proxy | 8250.0 | — |

**Probabilities:**

- PoP (raw): 0.578051
- Assignment Prob: 0.520709
- P(25% Max Profit): 0.549226
- P(50% Max Profit): 0.519181
- P(100% Max Profit): 0.456861
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 82.50 | Breakeven 1 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 85.00 | Downside (15%) | 250.00 | 0.00 | 250.00 | 0.0303 | 0.0303 |
| 100.00 | Current Market Price | 250.00 | 0.00 | 250.00 | 0.0303 | 0.0303 |
| 102.50 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -1250.00 | 0.00 | -1250.00 | -0.1515 | -0.1515 |
| 115.00 | Upside (15%) | -1250.00 | 0.00 | -1250.00 | -0.1515 | -0.1515 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8250.00 | -8250.00 | -1.0000 |
| breakeven_1 | Breakeven 1 | 82.50 | -17.50% | -0.00 | -0.00 | -0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 250.00 | 250.00 | 0.0303 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 250.00 | 250.00 | 0.0303 |
| spot | Current Market Price | 100.00 | 0.00% | 250.00 | 250.00 | 0.0303 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 250.00 | 250.00 | 0.0303 |
| breakeven_2 | Breakeven 2 | 102.50 | 2.50% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1250.00 | -1250.00 | -0.1515 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1250.00 | -1250.00 | -0.1515 |
| infinity | Stock to Infinity | — | — | -1250.00 | -1250.00 | -0.1515 |

---

### Bear Put Ladder (ID=22) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 115.00 | 16.38 | 100 |
| 2 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 3 | PUT | Short 1 | 85.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [97.5]
- Options Max PnL: 250.0
- Options Min PnL: -8250.0
- Combined Max PnL: 18750.0
- Combined Min PnL: -18250.0

**Net Premium:**

- Per Share: 12.5
- Total: 1250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $250.00 | Unlimited |
| Max Loss | -$8,250.00 | -$18,250.00 |
| Risk Reward | 0.03x | 1.03x |
| Capital Basis | $3,388.00 | $13,388.00 |
| Cost Credit | Debit $1,250.00 | Debit $1,250.00 |
| Pop | 57.6% | 57.6% |
| Margin Proxy | 3388.0 | — |

**Probabilities:**

- PoP (raw): 0.576062
- Assignment Prob: 0.520709
- P(25% Max Profit): 0.549226
- P(50% Max Profit): 0.519181
- P(100% Max Profit): 0.456861
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 250.00 | -1500.00 | -1250.00 | 0.0303 | -0.0685 |
| 97.50 | Breakeven 1 | 250.00 | -250.00 | 0.00 | 0.0303 | 0.0000 |
| 100.00 | Current Market Price | 250.00 | 0.00 | 250.00 | 0.0303 | 0.0137 |
| 115.00 | Upside (15%) | -1250.00 | 1500.00 | 250.00 | -0.1515 | 0.0137 |
| 115.00 | Upside (15%) | -1250.00 | 1500.00 | 250.00 | -0.1515 | 0.0137 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8250.00 | -18250.00 | -1.3632 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 250.00 | -1250.00 | -0.0685 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 250.00 | -1250.00 | -0.0685 |
| breakeven_1 | Breakeven 1 | 97.50 | -2.50% | 250.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 250.00 | 250.00 | 0.0137 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 250.00 | 250.00 | 0.0137 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1250.00 | 250.00 | 0.0137 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1250.00 | 250.00 | 0.0137 |
| infinity | Stock to Infinity | — | — | -1250.00 | 103750.00 | 7.7495 |

---

### Bear Put Ladder (ID=22) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 115.00 | 16.38 | 100 |
| 2 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 3 | PUT | Short 1 | 85.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [66.25]
- Options Max PnL: 250.0
- Options Min PnL: -8250.0
- Combined Max PnL: 23750.0
- Combined Min PnL: -13250.0

**Net Premium:**

- Per Share: 12.5
- Total: 1250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $250.00 | Unlimited |
| Max Loss | -$8,250.00 | -$13,250.00 |
| Risk Reward | 0.03x | 1.79x |
| Capital Basis | $3,388.00 | $8,388.00 |
| Cost Credit | Debit $1,250.00 | Debit $1,250.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 3388.0 | — |

**Probabilities:**

- PoP (raw): 0.999954
- Assignment Prob: 0.520709
- P(25% Max Profit): 0.549226
- P(50% Max Profit): 0.519181
- P(100% Max Profit): 0.456861
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -3250.00 | 0.00 | -3250.00 | -0.3939 | -0.2453 |
| 66.25 | Breakeven 1 | -1625.00 | 1625.00 | 0.00 | -0.1970 | 0.0000 |
| 85.00 | Downside (15%) | 250.00 | 3500.00 | 3750.00 | 0.0303 | 0.2830 |
| 100.00 | Current Market Price | 250.00 | 5000.00 | 5250.00 | 0.0303 | 0.3962 |
| 115.00 | Upside (15%) | -1250.00 | 6500.00 | 5250.00 | -0.1515 | 0.3962 |
| 115.00 | Upside (15%) | -1250.00 | 6500.00 | 5250.00 | -0.1515 | 0.3962 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8250.00 | -13250.00 | -1.5796 |
| breakeven_1 | Breakeven 1 | 66.25 | -33.75% | -1625.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 250.00 | 3750.00 | 0.2830 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 250.00 | 3750.00 | 0.2830 |
| spot | Current Market Price | 100.00 | 0.00% | 250.00 | 5250.00 | 0.3962 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 250.00 | 5250.00 | 0.3962 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1250.00 | 5250.00 | 0.3962 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1250.00 | 5250.00 | 0.3962 |
| infinity | Stock to Infinity | — | — | -1250.00 | 108750.00 | 12.9649 |

---

### Bear Put Ladder (ID=22) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 115.00 | 16.38 | 100 |
| 2 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 3 | PUT | Short 1 | 85.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [127.5]
- Options Max PnL: 250.0
- Options Min PnL: -8250.0
- Combined Max PnL: 17250.0
- Combined Min PnL: -19750.0

**Net Premium:**

- Per Share: 12.5
- Total: 1250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $250.00 | Unlimited |
| Max Loss | -$8,250.00 | -$19,750.00 |
| Risk Reward | 0.03x | 0.87x |
| Capital Basis | $3,388.00 | $14,888.00 |
| Cost Credit | Debit $1,250.00 | Debit $1,250.00 |
| Pop | 0.8% | 0.8% |
| Margin Proxy | 3388.0 | — |

**Probabilities:**

- PoP (raw): 0.008401
- Assignment Prob: 0.520709
- P(25% Max Profit): 0.549226
- P(50% Max Profit): 0.519181
- P(100% Max Profit): 0.456861
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 250.00 | -3000.00 | -2750.00 | 0.0303 | -0.1392 |
| 100.00 | Current Market Price | 250.00 | -1500.00 | -1250.00 | 0.0303 | -0.0633 |
| 115.00 | Upside (15%) | -1250.00 | 0.00 | -1250.00 | -0.1515 | -0.0633 |
| 115.00 | Upside (15%) | -1250.00 | 0.00 | -1250.00 | -0.1515 | -0.0633 |
| 127.50 | Breakeven 1 | -1250.00 | 1250.00 | 0.00 | -0.1515 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8250.00 | -19750.00 | -1.3266 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 250.00 | -2750.00 | -0.1392 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 250.00 | -2750.00 | -0.1392 |
| spot | Current Market Price | 100.00 | 0.00% | 250.00 | -1250.00 | -0.0633 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 250.00 | -1250.00 | -0.0633 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1250.00 | -1250.00 | -0.0633 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1250.00 | -1250.00 | -0.0633 |
| breakeven_1 | Breakeven 1 | 127.50 | 27.50% | -1250.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | -1250.00 | 102250.00 | 6.8679 |

---

### Bear Call Ladder (ID=23) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 85.00 | 16.38 | 100 |
| 2 | CALL | Long 1 | 100.00 | 2.50 | 100 |
| 3 | CALL | Long 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [97.5, 117.5]
- Options Max PnL: 18250.0
- Options Min PnL: -250.0
- Combined Max PnL: 18250.0
- Combined Min PnL: -250.0

**Net Premium:**

- Per Share: -12.5
- Total: -1250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$250.00 | -$250.00 |
| Risk Reward | 73.00x | 73.00x |
| Capital Basis | $3,638.00 | $3,638.00 |
| Cost Credit | Credit $1,250.00 | Credit $1,250.00 |
| Pop | 47.8% | 47.8% |
| Margin Proxy | 3638.0 | — |

**Probabilities:**

- PoP (raw): 0.478227
- Assignment Prob: 0.934835
- P(25% Max Profit): 1e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1250.00 | 0.00 | 1250.00 | 5.0000 | 5.0000 |
| 97.50 | Breakeven 1 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 100.00 | Current Market Price | -250.00 | 0.00 | -250.00 | -1.0000 | -1.0000 |
| 115.00 | Upside (15%) | -250.00 | 0.00 | -250.00 | -1.0000 | -1.0000 |
| 115.00 | Upside (15%) | -250.00 | 0.00 | -250.00 | -1.0000 | -1.0000 |
| 117.50 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1250.00 | 1250.00 | 0.3436 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1250.00 | 1250.00 | 5.0000 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1250.00 | 1250.00 | 5.0000 |
| breakeven_1 | Breakeven 1 | 97.50 | -2.50% | -0.00 | -0.00 | -0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -1.0000 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -1.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -250.00 | -250.00 | -1.0000 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -250.00 | -250.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 117.50 | 17.50% | 0.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 103250.00 | 103250.00 | 28.3810 |

---

### Bear Call Ladder (ID=23) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 85.00 | 16.38 | 100 |
| 2 | CALL | Long 1 | 100.00 | 2.50 | 100 |
| 3 | CALL | Long 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [102.5]
- Options Max PnL: 18250.0
- Options Min PnL: -250.0
- Combined Max PnL: 38250.0
- Combined Min PnL: -8750.0

**Net Premium:**

- Per Share: -12.5
- Total: -1250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$250.00 | -$8,750.00 |
| Risk Reward | 73.00x | 4.37x |
| Capital Basis | $3,638.00 | $13,638.00 |
| Cost Credit | Credit $1,250.00 | Credit $1,250.00 |
| Pop | 38.6% | 38.6% |
| Margin Proxy | 3638.0 | — |

**Probabilities:**

- PoP (raw): 0.386034
- Assignment Prob: 0.934835
- P(25% Max Profit): 1e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1250.00 | -1500.00 | -250.00 | 5.0000 | -0.0244 |
| 100.00 | Current Market Price | -250.00 | 0.00 | -250.00 | -1.0000 | -0.0244 |
| 102.50 | Breakeven 1 | -250.00 | 250.00 | -0.00 | -1.0000 | -0.0000 |
| 115.00 | Upside (15%) | -250.00 | 1500.00 | 1250.00 | -1.0000 | 0.1220 |
| 115.00 | Upside (15%) | -250.00 | 1500.00 | 1250.00 | -1.0000 | 0.1220 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1250.00 | -8750.00 | -0.6416 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1250.00 | -250.00 | -0.0244 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1250.00 | -250.00 | -0.0244 |
| spot | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -0.0244 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -0.0244 |
| breakeven_1 | Breakeven 1 | 102.50 | 2.50% | -250.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -250.00 | 1250.00 | 0.1220 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -250.00 | 1250.00 | 0.1220 |
| infinity | Stock to Infinity | — | — | 103250.00 | 208250.00 | 15.2698 |

---

### Bear Call Ladder (ID=23) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 85.00 | 16.38 | 100 |
| 2 | CALL | Long 1 | 100.00 | 2.50 | 100 |
| 3 | CALL | Long 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [37.5]
- Options Max PnL: 18250.0
- Options Min PnL: -250.0
- Combined Max PnL: 43250.0
- Combined Min PnL: -3750.0

**Net Premium:**

- Per Share: -12.5
- Total: -1250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$250.00 | -$3,750.00 |
| Risk Reward | 73.00x | 11.53x |
| Capital Basis | $3,638.00 | $8,638.00 |
| Cost Credit | Credit $1,250.00 | Credit $1,250.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 3638.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.934835
- P(25% Max Profit): 1e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 37.50 | Breakeven 1 | 1250.00 | -1250.00 | 0.00 | 5.0000 | 0.0000 |
| 50.00 | Scenario @ 50.00 | 1250.00 | 0.00 | 1250.00 | 5.0000 | 0.2381 |
| 85.00 | Downside (15%) | 1250.00 | 3500.00 | 4750.00 | 5.0000 | 0.9048 |
| 100.00 | Current Market Price | -250.00 | 5000.00 | 4750.00 | -1.0000 | 0.9048 |
| 115.00 | Upside (15%) | -250.00 | 6500.00 | 6250.00 | -1.0000 | 1.1905 |
| 115.00 | Upside (15%) | -250.00 | 6500.00 | 6250.00 | -1.0000 | 1.1905 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1250.00 | -3750.00 | -0.4341 |
| breakeven_1 | Breakeven 1 | 37.50 | -62.50% | 1250.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1250.00 | 4750.00 | 0.9048 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1250.00 | 4750.00 | 0.9048 |
| spot | Current Market Price | 100.00 | 0.00% | -250.00 | 4750.00 | 0.9048 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -250.00 | 4750.00 | 0.9048 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -250.00 | 6250.00 | 1.1905 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -250.00 | 6250.00 | 1.1905 |
| infinity | Stock to Infinity | — | — | 103250.00 | 213250.00 | 24.6874 |

---

### Bear Call Ladder (ID=23) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 85.00 | 16.38 | 100 |
| 2 | CALL | Long 1 | 100.00 | 2.50 | 100 |
| 3 | CALL | Long 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [116.25]
- Options Max PnL: 18250.0
- Options Min PnL: -250.0
- Combined Max PnL: 36750.0
- Combined Min PnL: -10250.0

**Net Premium:**

- Per Share: -12.5
- Total: -1250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$250.00 | -$10,250.00 |
| Risk Reward | 73.00x | 3.59x |
| Capital Basis | $3,638.00 | $15,138.00 |
| Cost Credit | Credit $1,250.00 | Credit $1,250.00 |
| Pop | 6.7% | 6.7% |
| Margin Proxy | 3638.0 | — |

**Probabilities:**

- PoP (raw): 0.066595
- Assignment Prob: 0.934835
- P(25% Max Profit): 1e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1250.00 | -3000.00 | -1750.00 | 5.0000 | -0.1489 |
| 100.00 | Current Market Price | -250.00 | -1500.00 | -1750.00 | -1.0000 | -0.1489 |
| 115.00 | Upside (15%) | -250.00 | 0.00 | -250.00 | -1.0000 | -0.0213 |
| 115.00 | Upside (15%) | -250.00 | 0.00 | -250.00 | -1.0000 | -0.0213 |
| 116.25 | Breakeven 1 | -125.00 | 125.00 | 0.00 | -0.5000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1250.00 | -10250.00 | -0.6771 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1250.00 | -1750.00 | -0.1489 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1250.00 | -1750.00 | -0.1489 |
| spot | Current Market Price | 100.00 | 0.00% | -250.00 | -1750.00 | -0.1489 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -250.00 | -1750.00 | -0.1489 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -250.00 | -250.00 | -0.0213 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -250.00 | -250.00 | -0.0213 |
| breakeven_1 | Breakeven 1 | 116.25 | 16.25% | -125.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 103250.00 | 206750.00 | 13.6577 |

---

### Bull Put Ladder (ID=24) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 115.00 | 16.38 | 100 |
| 2 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 3 | PUT | Long 1 | 85.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [82.5, 102.5]
- Options Max PnL: 8250.0
- Options Min PnL: -250.0
- Combined Max PnL: 8250.0
- Combined Min PnL: -250.0

**Net Premium:**

- Per Share: -12.5
- Total: -1250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $8,250.00 | $8,250.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 33.00x | 33.00x |
| Capital Basis | $3,638.00 | $3,638.00 |
| Cost Credit | Credit $1,250.00 | Credit $1,250.00 |
| Pop | 42.2% | 42.2% |
| Margin Proxy | 3638.0 | — |

**Probabilities:**

- PoP (raw): 0.421949
- Assignment Prob: 0.918877
- P(25% Max Profit): 2e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 82.50 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 85.00 | Downside (15%) | -250.00 | 0.00 | -250.00 | -1.0000 | -1.0000 |
| 100.00 | Current Market Price | -250.00 | 0.00 | -250.00 | -1.0000 | -1.0000 |
| 102.50 | Breakeven 2 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 115.00 | Upside (15%) | 1250.00 | 0.00 | 1250.00 | 5.0000 | 5.0000 |
| 115.00 | Upside (15%) | 1250.00 | 0.00 | 1250.00 | 5.0000 | 5.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8250.00 | 8250.00 | 2.2677 |
| breakeven_1 | Breakeven 1 | 82.50 | -17.50% | 0.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -250.00 | -250.00 | -1.0000 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -250.00 | -250.00 | -1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -1.0000 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 102.50 | 2.50% | -0.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1250.00 | 1250.00 | 5.0000 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1250.00 | 1250.00 | 5.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | 1250.00 | 0.3436 |

---

### Bull Put Ladder (ID=24) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 115.00 | 16.38 | 100 |
| 2 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 3 | PUT | Long 1 | 85.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [101.25]
- Options Max PnL: 8250.0
- Options Min PnL: -250.0
- Combined Max PnL: 21250.0
- Combined Min PnL: -1750.0

**Net Premium:**

- Per Share: -12.5
- Total: -1250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $8,250.00 | Unlimited |
| Max Loss | Unlimited | -$1,750.00 |
| Risk Reward | 33.00x | 12.14x |
| Capital Basis | $3,638.00 | $13,638.00 |
| Cost Credit | Credit $1,250.00 | Credit $1,250.00 |
| Pop | 43.2% | 43.2% |
| Margin Proxy | 3638.0 | — |

**Probabilities:**

- PoP (raw): 0.431901
- Assignment Prob: 0.918877
- P(25% Max Profit): 2e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -250.00 | -1500.00 | -1750.00 | -1.0000 | -0.1707 |
| 100.00 | Current Market Price | -250.00 | 0.00 | -250.00 | -1.0000 | -0.0244 |
| 101.25 | Breakeven 1 | -125.00 | 125.00 | -0.00 | -0.5000 | -0.0000 |
| 115.00 | Upside (15%) | 1250.00 | 1500.00 | 2750.00 | 5.0000 | 0.2683 |
| 115.00 | Upside (15%) | 1250.00 | 1500.00 | 2750.00 | 5.0000 | 0.2683 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8250.00 | -1750.00 | -0.1283 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -250.00 | -1750.00 | -0.1707 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -250.00 | -1750.00 | -0.1707 |
| spot | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -0.0244 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -0.0244 |
| breakeven_1 | Breakeven 1 | 101.25 | 1.25% | -125.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1250.00 | 2750.00 | 0.2683 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1250.00 | 2750.00 | 0.2683 |
| infinity | Stock to Infinity | — | — | Unlimited | 106250.00 | 7.7907 |

---

### Bull Put Ladder (ID=24) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 115.00 | 16.38 | 100 |
| 2 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 3 | PUT | Long 1 | 85.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: []
- Options Max PnL: 8250.0
- Options Min PnL: -250.0
- Combined Max PnL: 26250.0
- Combined Min PnL: 3250.0

**Net Premium:**

- Per Share: -12.5
- Total: -1250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $8,250.00 | Unlimited |
| Max Loss | Unlimited | $3,250.00 |
| Risk Reward | 33.00x | 8.08x |
| Capital Basis | $3,638.00 | $8,638.00 |
| Cost Credit | Credit $1,250.00 | Credit $1,250.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 3638.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.918877
- P(25% Max Profit): 2e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | 3250.00 | 0.00 | 3250.00 | 13.0000 | 0.6190 |
| 85.00 | Downside (15%) | -250.00 | 3500.00 | 3250.00 | -1.0000 | 0.6190 |
| 100.00 | Current Market Price | -250.00 | 5000.00 | 4750.00 | -1.0000 | 0.9048 |
| 115.00 | Upside (15%) | 1250.00 | 6500.00 | 7750.00 | 5.0000 | 1.4762 |
| 115.00 | Upside (15%) | 1250.00 | 6500.00 | 7750.00 | 5.0000 | 1.4762 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8250.00 | 3250.00 | 0.3762 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -250.00 | 3250.00 | 0.6190 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -250.00 | 3250.00 | 0.6190 |
| spot | Current Market Price | 100.00 | 0.00% | -250.00 | 4750.00 | 0.9048 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -250.00 | 4750.00 | 0.9048 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1250.00 | 7750.00 | 1.4762 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1250.00 | 7750.00 | 1.4762 |
| infinity | Stock to Infinity | — | — | Unlimited | 111250.00 | 12.8791 |

---

### Bull Put Ladder (ID=24) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 115.00 | 16.38 | 100 |
| 2 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 3 | PUT | Long 1 | 85.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [108.75]
- Options Max PnL: 8250.0
- Options Min PnL: -250.0
- Combined Max PnL: 19750.0
- Combined Min PnL: -3250.0

**Net Premium:**

- Per Share: -12.5
- Total: -1250.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $8,250.00 | Unlimited |
| Max Loss | Unlimited | -$3,250.00 |
| Risk Reward | 33.00x | 6.08x |
| Capital Basis | $3,638.00 | $15,138.00 |
| Cost Credit | Credit $1,250.00 | Credit $1,250.00 |
| Pop | 19.5% | 19.5% |
| Margin Proxy | 3638.0 | — |

**Probabilities:**

- PoP (raw): 0.195021
- Assignment Prob: 0.918877
- P(25% Max Profit): 2e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -250.00 | -3000.00 | -3250.00 | -1.0000 | -0.2766 |
| 100.00 | Current Market Price | -250.00 | -1500.00 | -1750.00 | -1.0000 | -0.1489 |
| 108.75 | Breakeven 1 | 625.00 | -625.00 | 0.00 | 2.5000 | 0.0000 |
| 115.00 | Upside (15%) | 1250.00 | 0.00 | 1250.00 | 5.0000 | 0.1064 |
| 115.00 | Upside (15%) | 1250.00 | 0.00 | 1250.00 | 5.0000 | 0.1064 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8250.00 | -3250.00 | -0.2147 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -250.00 | -3250.00 | -0.2766 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -250.00 | -3250.00 | -0.2766 |
| spot | Current Market Price | 100.00 | 0.00% | -250.00 | -1750.00 | -0.1489 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -250.00 | -1750.00 | -0.1489 |
| breakeven_1 | Breakeven 1 | 108.75 | 8.75% | 625.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1250.00 | 1250.00 | 0.1064 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1250.00 | 1250.00 | 0.1064 |
| infinity | Stock to Infinity | — | — | Unlimited | 104750.00 | 6.9197 |

---

### Long Call Butterfly (ID=25) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 85.00 | 16.38 | 100 |
| 2 | CALL | Short 2 | 100.00 | 2.50 | 100 |
| 3 | CALL | Long 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [97.76, 102.24]
- Options Max PnL: 224.0
- Options Min PnL: -1276.0
- Combined Max PnL: 224.0
- Combined Min PnL: -1276.0

**Net Premium:**

- Per Share: 12.76
- Total: 1276.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $224.00 | $224.00 |
| Max Loss | -$1,276.00 | -$1,276.00 |
| Risk Reward | 0.18x | 0.18x |
| Capital Basis | $1,276.00 | $1,276.00 |
| Cost Credit | Debit $1,276.00 | Debit $1,276.00 |
| Pop | 17.1% | 17.1% |
| Margin Proxy | 1276.0 | — |

**Probabilities:**

- PoP (raw): 0.170575
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.128347
- P(50% Max Profit): 0.085763
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1276.00 | 0.00 | -1276.00 | -1.0000 | -1.0000 |
| 97.76 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | 224.00 | 0.00 | 224.00 | 0.1755 | 0.1755 |
| 102.24 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -1276.00 | 0.00 | -1276.00 | -1.0000 | -1.0000 |
| 115.00 | Upside (15%) | -1276.00 | 0.00 | -1276.00 | -1.0000 | -1.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1276.00 | -1276.00 | -1.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1276.00 | -1276.00 | -1.0000 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1276.00 | -1276.00 | -1.0000 |
| breakeven_1 | Breakeven 1 | 97.76 | -2.24% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.1755 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.1755 |
| breakeven_2 | Breakeven 2 | 102.24 | 2.24% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1276.00 | -1276.00 | -1.0000 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1276.00 | -1276.00 | -1.0000 |
| infinity | Stock to Infinity | — | — | -1276.00 | -1276.00 | -1.0000 |

---

### Long Call Butterfly (ID=25) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 85.00 | 16.38 | 100 |
| 2 | CALL | Short 2 | 100.00 | 2.50 | 100 |
| 3 | CALL | Long 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [98.88]
- Options Max PnL: 224.0
- Options Min PnL: -1276.0
- Combined Max PnL: 18724.0
- Combined Min PnL: -11276.0

**Net Premium:**

- Per Share: 12.76
- Total: 1276.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $224.00 | Unlimited |
| Max Loss | -$1,276.00 | -$11,276.00 |
| Risk Reward | 0.18x | 1.66x |
| Capital Basis | $4,500.00 | $14,500.00 |
| Cost Credit | Debit $1,276.00 | Debit $1,276.00 |
| Pop | 52.3% | 52.3% |
| Margin Proxy | 4500.0 | — |

**Probabilities:**

- PoP (raw): 0.522532
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.128347
- P(50% Max Profit): 0.085763
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1276.00 | -1500.00 | -2776.00 | -1.0000 | -0.2462 |
| 98.88 | Breakeven 1 | 112.00 | -112.00 | -0.00 | 0.0878 | -0.0000 |
| 100.00 | Current Market Price | 224.00 | 0.00 | 224.00 | 0.1755 | 0.0199 |
| 115.00 | Upside (15%) | -1276.00 | 1500.00 | 224.00 | -1.0000 | 0.0199 |
| 115.00 | Upside (15%) | -1276.00 | 1500.00 | 224.00 | -1.0000 | 0.0199 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1276.00 | -11276.00 | -0.7777 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1276.00 | -2776.00 | -0.2462 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1276.00 | -2776.00 | -0.2462 |
| breakeven_1 | Breakeven 1 | 98.88 | -1.12% | 112.00 | -0.00 | -0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.0199 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.0199 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1276.00 | 224.00 | 0.0199 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1276.00 | 224.00 | 0.0199 |
| infinity | Stock to Infinity | — | — | -1276.00 | 103724.00 | 7.1534 |

---

### Long Call Butterfly (ID=25) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 85.00 | 16.38 | 100 |
| 2 | CALL | Short 2 | 100.00 | 2.50 | 100 |
| 3 | CALL | Long 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [62.76]
- Options Max PnL: 224.0
- Options Min PnL: -1276.0
- Combined Max PnL: 23724.0
- Combined Min PnL: -6276.0

**Net Premium:**

- Per Share: 12.76
- Total: 1276.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $224.00 | Unlimited |
| Max Loss | -$1,276.00 | -$6,276.00 |
| Risk Reward | 0.18x | 3.78x |
| Capital Basis | $4,500.00 | $9,500.00 |
| Cost Credit | Debit $1,276.00 | Debit $1,276.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 4500.0 | — |

**Probabilities:**

- PoP (raw): 0.999995
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.128347
- P(50% Max Profit): 0.085763
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -1276.00 | 0.00 | -1276.00 | -1.0000 | -0.2033 |
| 62.76 | Breakeven 1 | -1276.00 | 1276.00 | -0.00 | -1.0000 | -0.0000 |
| 85.00 | Downside (15%) | -1276.00 | 3500.00 | 2224.00 | -1.0000 | 0.3544 |
| 100.00 | Current Market Price | 224.00 | 5000.00 | 5224.00 | 0.1755 | 0.8324 |
| 115.00 | Upside (15%) | -1276.00 | 6500.00 | 5224.00 | -1.0000 | 0.8324 |
| 115.00 | Upside (15%) | -1276.00 | 6500.00 | 5224.00 | -1.0000 | 0.8324 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1276.00 | -6276.00 | -0.6606 |
| breakeven_1 | Breakeven 1 | 62.76 | -37.24% | -1276.00 | -0.00 | -0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1276.00 | 2224.00 | 0.3544 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1276.00 | 2224.00 | 0.3544 |
| spot | Current Market Price | 100.00 | 0.00% | 224.00 | 5224.00 | 0.8324 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 224.00 | 5224.00 | 0.8324 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1276.00 | 5224.00 | 0.8324 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1276.00 | 5224.00 | 0.8324 |
| infinity | Stock to Infinity | — | — | -1276.00 | 108724.00 | 11.4446 |

---

### Long Call Butterfly (ID=25) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 85.00 | 16.38 | 100 |
| 2 | CALL | Short 2 | 100.00 | 2.50 | 100 |
| 3 | CALL | Long 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [127.76]
- Options Max PnL: 224.0
- Options Min PnL: -1276.0
- Combined Max PnL: 17224.0
- Combined Min PnL: -12776.0

**Net Premium:**

- Per Share: 12.76
- Total: 1276.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $224.00 | Unlimited |
| Max Loss | -$1,276.00 | -$12,776.00 |
| Risk Reward | 0.18x | 1.35x |
| Capital Basis | $4,500.00 | $16,000.00 |
| Cost Credit | Debit $1,276.00 | Debit $1,276.00 |
| Pop | 0.8% | 0.8% |
| Margin Proxy | 4500.0 | — |

**Probabilities:**

- PoP (raw): 0.007962
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.128347
- P(50% Max Profit): 0.085763
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1276.00 | -3000.00 | -4276.00 | -1.0000 | -0.3347 |
| 100.00 | Current Market Price | 224.00 | -1500.00 | -1276.00 | 0.1755 | -0.0999 |
| 115.00 | Upside (15%) | -1276.00 | 0.00 | -1276.00 | -1.0000 | -0.0999 |
| 115.00 | Upside (15%) | -1276.00 | 0.00 | -1276.00 | -1.0000 | -0.0999 |
| 127.76 | Breakeven 1 | -1276.00 | 1276.00 | 0.00 | -1.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1276.00 | -12776.00 | -0.7985 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1276.00 | -4276.00 | -0.3347 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1276.00 | -4276.00 | -0.3347 |
| spot | Current Market Price | 100.00 | 0.00% | 224.00 | -1276.00 | -0.0999 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 224.00 | -1276.00 | -0.0999 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1276.00 | -1276.00 | -0.0999 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1276.00 | -1276.00 | -0.0999 |
| breakeven_1 | Breakeven 1 | 127.76 | 27.76% | -1276.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | -1276.00 | 102224.00 | 6.3890 |

---

### Long Put Butterfly (ID=26) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 85.00 | 1.38 | 100 |
| 2 | PUT | Short 2 | 100.00 | 2.50 | 100 |
| 3 | PUT | Long 1 | 115.00 | 16.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [97.76, 102.24]
- Options Max PnL: 224.0
- Options Min PnL: -1276.0
- Combined Max PnL: 224.0
- Combined Min PnL: -1276.0

**Net Premium:**

- Per Share: 12.76
- Total: 1276.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $224.00 | $224.00 |
| Max Loss | -$1,276.00 | -$1,276.00 |
| Risk Reward | 0.18x | 0.18x |
| Capital Basis | $1,276.00 | $1,276.00 |
| Cost Credit | Debit $1,276.00 | Debit $1,276.00 |
| Pop | 17.1% | 17.1% |
| Margin Proxy | 1276.0 | — |

**Probabilities:**

- PoP (raw): 0.170575
- Assignment Prob: 0.520709
- P(25% Max Profit): 0.128347
- P(50% Max Profit): 0.085763
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1276.00 | 0.00 | -1276.00 | -1.0000 | -1.0000 |
| 97.76 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | 224.00 | 0.00 | 224.00 | 0.1755 | 0.1755 |
| 102.24 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -1276.00 | 0.00 | -1276.00 | -1.0000 | -1.0000 |
| 115.00 | Upside (15%) | -1276.00 | 0.00 | -1276.00 | -1.0000 | -1.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1276.00 | -1276.00 | -1.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1276.00 | -1276.00 | -1.0000 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1276.00 | -1276.00 | -1.0000 |
| breakeven_1 | Breakeven 1 | 97.76 | -2.24% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.1755 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.1755 |
| breakeven_2 | Breakeven 2 | 102.24 | 2.24% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1276.00 | -1276.00 | -1.0000 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1276.00 | -1276.00 | -1.0000 |
| infinity | Stock to Infinity | — | — | -1276.00 | -1276.00 | -1.0000 |

---

### Long Put Butterfly (ID=26) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 85.00 | 1.38 | 100 |
| 2 | PUT | Short 2 | 100.00 | 2.50 | 100 |
| 3 | PUT | Long 1 | 115.00 | 16.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [98.88]
- Options Max PnL: 224.0
- Options Min PnL: -1276.0
- Combined Max PnL: 18724.0
- Combined Min PnL: -11276.0

**Net Premium:**

- Per Share: 12.76
- Total: 1276.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $224.00 | Unlimited |
| Max Loss | -$1,276.00 | -$11,276.00 |
| Risk Reward | 0.18x | 1.66x |
| Capital Basis | $4,500.00 | $14,500.00 |
| Cost Credit | Debit $1,276.00 | Debit $1,276.00 |
| Pop | 52.3% | 52.3% |
| Margin Proxy | 4500.0 | — |

**Probabilities:**

- PoP (raw): 0.522532
- Assignment Prob: 0.520709
- P(25% Max Profit): 0.128347
- P(50% Max Profit): 0.085763
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1276.00 | -1500.00 | -2776.00 | -1.0000 | -0.2462 |
| 98.88 | Breakeven 1 | 112.00 | -112.00 | -0.00 | 0.0878 | -0.0000 |
| 100.00 | Current Market Price | 224.00 | 0.00 | 224.00 | 0.1755 | 0.0199 |
| 115.00 | Upside (15%) | -1276.00 | 1500.00 | 224.00 | -1.0000 | 0.0199 |
| 115.00 | Upside (15%) | -1276.00 | 1500.00 | 224.00 | -1.0000 | 0.0199 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1276.00 | -11276.00 | -0.7777 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1276.00 | -2776.00 | -0.2462 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1276.00 | -2776.00 | -0.2462 |
| breakeven_1 | Breakeven 1 | 98.88 | -1.12% | 112.00 | -0.00 | -0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.0199 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.0199 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1276.00 | 224.00 | 0.0199 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1276.00 | 224.00 | 0.0199 |
| infinity | Stock to Infinity | — | — | -1276.00 | 103724.00 | 7.1534 |

---

### Long Put Butterfly (ID=26) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 85.00 | 1.38 | 100 |
| 2 | PUT | Short 2 | 100.00 | 2.50 | 100 |
| 3 | PUT | Long 1 | 115.00 | 16.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [62.76]
- Options Max PnL: 224.0
- Options Min PnL: -1276.0
- Combined Max PnL: 23724.0
- Combined Min PnL: -6276.0

**Net Premium:**

- Per Share: 12.76
- Total: 1276.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $224.00 | Unlimited |
| Max Loss | -$1,276.00 | -$6,276.00 |
| Risk Reward | 0.18x | 3.78x |
| Capital Basis | $4,500.00 | $9,500.00 |
| Cost Credit | Debit $1,276.00 | Debit $1,276.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 4500.0 | — |

**Probabilities:**

- PoP (raw): 0.999995
- Assignment Prob: 0.520709
- P(25% Max Profit): 0.128347
- P(50% Max Profit): 0.085763
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -1276.00 | 0.00 | -1276.00 | -1.0000 | -0.2033 |
| 62.76 | Breakeven 1 | -1276.00 | 1276.00 | -0.00 | -1.0000 | -0.0000 |
| 85.00 | Downside (15%) | -1276.00 | 3500.00 | 2224.00 | -1.0000 | 0.3544 |
| 100.00 | Current Market Price | 224.00 | 5000.00 | 5224.00 | 0.1755 | 0.8324 |
| 115.00 | Upside (15%) | -1276.00 | 6500.00 | 5224.00 | -1.0000 | 0.8324 |
| 115.00 | Upside (15%) | -1276.00 | 6500.00 | 5224.00 | -1.0000 | 0.8324 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1276.00 | -6276.00 | -0.6606 |
| breakeven_1 | Breakeven 1 | 62.76 | -37.24% | -1276.00 | -0.00 | -0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1276.00 | 2224.00 | 0.3544 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1276.00 | 2224.00 | 0.3544 |
| spot | Current Market Price | 100.00 | 0.00% | 224.00 | 5224.00 | 0.8324 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 224.00 | 5224.00 | 0.8324 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1276.00 | 5224.00 | 0.8324 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1276.00 | 5224.00 | 0.8324 |
| infinity | Stock to Infinity | — | — | -1276.00 | 108724.00 | 11.4446 |

---

### Long Put Butterfly (ID=26) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 85.00 | 1.38 | 100 |
| 2 | PUT | Short 2 | 100.00 | 2.50 | 100 |
| 3 | PUT | Long 1 | 115.00 | 16.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [127.76]
- Options Max PnL: 224.0
- Options Min PnL: -1276.0
- Combined Max PnL: 17224.0
- Combined Min PnL: -12776.0

**Net Premium:**

- Per Share: 12.76
- Total: 1276.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $224.00 | Unlimited |
| Max Loss | -$1,276.00 | -$12,776.00 |
| Risk Reward | 0.18x | 1.35x |
| Capital Basis | $4,500.00 | $16,000.00 |
| Cost Credit | Debit $1,276.00 | Debit $1,276.00 |
| Pop | 0.8% | 0.8% |
| Margin Proxy | 4500.0 | — |

**Probabilities:**

- PoP (raw): 0.007962
- Assignment Prob: 0.520709
- P(25% Max Profit): 0.128347
- P(50% Max Profit): 0.085763
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1276.00 | -3000.00 | -4276.00 | -1.0000 | -0.3347 |
| 100.00 | Current Market Price | 224.00 | -1500.00 | -1276.00 | 0.1755 | -0.0999 |
| 115.00 | Upside (15%) | -1276.00 | 0.00 | -1276.00 | -1.0000 | -0.0999 |
| 115.00 | Upside (15%) | -1276.00 | 0.00 | -1276.00 | -1.0000 | -0.0999 |
| 127.76 | Breakeven 1 | -1276.00 | 1276.00 | 0.00 | -1.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1276.00 | -12776.00 | -0.7985 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1276.00 | -4276.00 | -0.3347 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1276.00 | -4276.00 | -0.3347 |
| spot | Current Market Price | 100.00 | 0.00% | 224.00 | -1276.00 | -0.0999 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 224.00 | -1276.00 | -0.0999 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1276.00 | -1276.00 | -0.0999 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1276.00 | -1276.00 | -0.0999 |
| breakeven_1 | Breakeven 1 | 127.76 | 27.76% | -1276.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | -1276.00 | 102224.00 | 6.3890 |

---

### Iron Butterfly (ID=27) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 85.00 | 1.38 | 100 |
| 2 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 3 | CALL | Short 1 | 100.00 | 2.50 | 100 |
| 4 | CALL | Long 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [97.76, 102.24]
- Options Max PnL: 224.0
- Options Min PnL: -1276.0
- Combined Max PnL: 224.0
- Combined Min PnL: -1276.0

**Net Premium:**

- Per Share: -2.24
- Total: -224.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $224.00 | $224.00 |
| Max Loss | -$1,276.00 | -$1,276.00 |
| Risk Reward | 0.18x | 0.18x |
| Capital Basis | $1,276.00 | $1,276.00 |
| Cost Credit | Credit $224.00 | Credit $224.00 |
| Pop | 17.1% | 17.1% |
| Margin Proxy | 1276.0 | — |

**Probabilities:**

- PoP (raw): 0.170575
- Assignment Prob: 1.0
- P(25% Max Profit): 0.128347
- P(50% Max Profit): 0.085763
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1276.00 | 0.00 | -1276.00 | -1.0000 | -1.0000 |
| 97.76 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | 224.00 | 0.00 | 224.00 | 0.1755 | 0.1755 |
| 102.24 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -1276.00 | 0.00 | -1276.00 | -1.0000 | -1.0000 |
| 115.00 | Upside (15%) | -1276.00 | 0.00 | -1276.00 | -1.0000 | -1.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1276.00 | -1276.00 | -1.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1276.00 | -1276.00 | -1.0000 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1276.00 | -1276.00 | -1.0000 |
| breakeven_1 | Breakeven 1 | 97.76 | -2.24% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.1755 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.1755 |
| breakeven_2 | Breakeven 2 | 102.24 | 2.24% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1276.00 | -1276.00 | -1.0000 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1276.00 | -1276.00 | -1.0000 |
| infinity | Stock to Infinity | — | — | -1276.00 | -1276.00 | -1.0000 |

---

### Iron Butterfly (ID=27) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 85.00 | 1.38 | 100 |
| 2 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 3 | CALL | Short 1 | 100.00 | 2.50 | 100 |
| 4 | CALL | Long 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [98.88]
- Options Max PnL: 224.0
- Options Min PnL: -1276.0
- Combined Max PnL: 18724.0
- Combined Min PnL: -11276.0

**Net Premium:**

- Per Share: -2.24
- Total: -224.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $224.00 | Unlimited |
| Max Loss | -$1,276.00 | -$11,276.00 |
| Risk Reward | 0.18x | 1.66x |
| Capital Basis | $4,500.00 | $14,500.00 |
| Cost Credit | Credit $224.00 | Credit $224.00 |
| Pop | 52.3% | 52.3% |
| Margin Proxy | 4500.0 | — |

**Probabilities:**

- PoP (raw): 0.522532
- Assignment Prob: 1.0
- P(25% Max Profit): 0.128347
- P(50% Max Profit): 0.085763
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1276.00 | -1500.00 | -2776.00 | -1.0000 | -0.2462 |
| 98.88 | Breakeven 1 | 112.00 | -112.00 | -0.00 | 0.0878 | -0.0000 |
| 100.00 | Current Market Price | 224.00 | 0.00 | 224.00 | 0.1755 | 0.0199 |
| 115.00 | Upside (15%) | -1276.00 | 1500.00 | 224.00 | -1.0000 | 0.0199 |
| 115.00 | Upside (15%) | -1276.00 | 1500.00 | 224.00 | -1.0000 | 0.0199 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1276.00 | -11276.00 | -0.7777 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1276.00 | -2776.00 | -0.2462 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1276.00 | -2776.00 | -0.2462 |
| breakeven_1 | Breakeven 1 | 98.88 | -1.12% | 112.00 | -0.00 | -0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.0199 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.0199 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1276.00 | 224.00 | 0.0199 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1276.00 | 224.00 | 0.0199 |
| infinity | Stock to Infinity | — | — | -1276.00 | 103724.00 | 7.1534 |

---

### Iron Butterfly (ID=27) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 85.00 | 1.38 | 100 |
| 2 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 3 | CALL | Short 1 | 100.00 | 2.50 | 100 |
| 4 | CALL | Long 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [62.76]
- Options Max PnL: 224.0
- Options Min PnL: -1276.0
- Combined Max PnL: 23724.0
- Combined Min PnL: -6276.0

**Net Premium:**

- Per Share: -2.24
- Total: -224.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $224.00 | Unlimited |
| Max Loss | -$1,276.00 | -$6,276.00 |
| Risk Reward | 0.18x | 3.78x |
| Capital Basis | $4,500.00 | $9,500.00 |
| Cost Credit | Credit $224.00 | Credit $224.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 4500.0 | — |

**Probabilities:**

- PoP (raw): 0.999995
- Assignment Prob: 1.0
- P(25% Max Profit): 0.128347
- P(50% Max Profit): 0.085763
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -1276.00 | 0.00 | -1276.00 | -1.0000 | -0.2033 |
| 62.76 | Breakeven 1 | -1276.00 | 1276.00 | 0.00 | -1.0000 | 0.0000 |
| 85.00 | Downside (15%) | -1276.00 | 3500.00 | 2224.00 | -1.0000 | 0.3544 |
| 100.00 | Current Market Price | 224.00 | 5000.00 | 5224.00 | 0.1755 | 0.8324 |
| 115.00 | Upside (15%) | -1276.00 | 6500.00 | 5224.00 | -1.0000 | 0.8324 |
| 115.00 | Upside (15%) | -1276.00 | 6500.00 | 5224.00 | -1.0000 | 0.8324 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1276.00 | -6276.00 | -0.6606 |
| breakeven_1 | Breakeven 1 | 62.76 | -37.24% | -1276.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1276.00 | 2224.00 | 0.3544 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1276.00 | 2224.00 | 0.3544 |
| spot | Current Market Price | 100.00 | 0.00% | 224.00 | 5224.00 | 0.8324 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 224.00 | 5224.00 | 0.8324 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1276.00 | 5224.00 | 0.8324 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1276.00 | 5224.00 | 0.8324 |
| infinity | Stock to Infinity | — | — | -1276.00 | 108724.00 | 11.4446 |

---

### Iron Butterfly (ID=27) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 85.00 | 1.38 | 100 |
| 2 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 3 | CALL | Short 1 | 100.00 | 2.50 | 100 |
| 4 | CALL | Long 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [127.76]
- Options Max PnL: 224.0
- Options Min PnL: -1276.0
- Combined Max PnL: 17224.0
- Combined Min PnL: -12776.0

**Net Premium:**

- Per Share: -2.24
- Total: -224.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $224.00 | Unlimited |
| Max Loss | -$1,276.00 | -$12,776.00 |
| Risk Reward | 0.18x | 1.35x |
| Capital Basis | $4,500.00 | $16,000.00 |
| Cost Credit | Credit $224.00 | Credit $224.00 |
| Pop | 0.8% | 0.8% |
| Margin Proxy | 4500.0 | — |

**Probabilities:**

- PoP (raw): 0.007962
- Assignment Prob: 1.0
- P(25% Max Profit): 0.128347
- P(50% Max Profit): 0.085763
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1276.00 | -3000.00 | -4276.00 | -1.0000 | -0.3347 |
| 100.00 | Current Market Price | 224.00 | -1500.00 | -1276.00 | 0.1755 | -0.0999 |
| 115.00 | Upside (15%) | -1276.00 | 0.00 | -1276.00 | -1.0000 | -0.0999 |
| 115.00 | Upside (15%) | -1276.00 | 0.00 | -1276.00 | -1.0000 | -0.0999 |
| 127.76 | Breakeven 1 | -1276.00 | 1276.00 | 0.00 | -1.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1276.00 | -12776.00 | -0.7985 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1276.00 | -4276.00 | -0.3347 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1276.00 | -4276.00 | -0.3347 |
| spot | Current Market Price | 100.00 | 0.00% | 224.00 | -1276.00 | -0.0999 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 224.00 | -1276.00 | -0.0999 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1276.00 | -1276.00 | -0.0999 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1276.00 | -1276.00 | -0.0999 |
| breakeven_1 | Breakeven 1 | 127.76 | 27.76% | -1276.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | -1276.00 | 102224.00 | 6.3890 |

---

### Long Call Condor (ID=28) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 80.00 | 21.00 | 100 |
| 2 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 3 | CALL | Short 1 | 108.00 | 1.90 | 100 |
| 4 | CALL | Long 1 | 120.00 | 1.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [90.2, 109.8]
- Options Max PnL: 180.0
- Options Min PnL: -1020.0
- Combined Max PnL: 180.0
- Combined Min PnL: -1020.0

**Net Premium:**

- Per Share: 10.2
- Total: 1020.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $180.00 | $180.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.18x | 0.18x |
| Capital Basis | $4,380.00 | $4,380.00 |
| Cost Credit | Debit $1,020.00 | Debit $1,020.00 |
| Pop | 65.6% | 65.6% |
| Margin Proxy | 4380.0 | — |

**Probabilities:**

- PoP (raw): 0.656141
- Assignment Prob: 0.773633
- P(25% Max Profit): 0.633375
- P(50% Max Profit): 0.609707
- P(100% Max Profit): 0.560753
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | -1020.00 | 0.00 | -1020.00 | -1.0000 | -1.0000 |
| 85.00 | Downside (15%) | -520.00 | 0.00 | -520.00 | -0.5098 | -0.5098 |
| 90.20 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 92.00 | Strike (Lower Middle) | 180.00 | 0.00 | 180.00 | 0.1765 | 0.1765 |
| 100.00 | Current Market Price | 180.00 | 0.00 | 180.00 | 0.1765 | 0.1765 |
| 108.00 | Strike (Upper Middle) | 180.00 | 0.00 | 180.00 | 0.1765 | 0.1765 |
| 109.80 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -520.00 | 0.00 | -520.00 | -0.5098 | -0.5098 |
| 120.00 | Strike (Highest) | -1020.00 | 0.00 | -1020.00 | -1.0000 | -1.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1020.00 | -1020.00 | -0.2329 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | -1020.00 | -1020.00 | -1.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -520.00 | -520.00 | -0.5098 |
| breakeven_1 | Breakeven 1 | 90.20 | -9.80% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | 180.00 | 180.00 | 0.1765 |
| spot | Current Market Price | 100.00 | 0.00% | 180.00 | 180.00 | 0.1765 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | 180.00 | 180.00 | 0.1765 |
| breakeven_2 | Breakeven 2 | 109.80 | 9.80% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -520.00 | -520.00 | -0.5098 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | -1020.00 | -1020.00 | -1.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | -1020.00 | -0.2329 |

---

### Long Call Condor (ID=28) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 80.00 | 21.00 | 100 |
| 2 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 3 | CALL | Short 1 | 108.00 | 1.90 | 100 |
| 4 | CALL | Long 1 | 120.00 | 1.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [98.2]
- Options Max PnL: 180.0
- Options Min PnL: -1020.0
- Combined Max PnL: 18980.0
- Combined Min PnL: -11020.0

**Net Premium:**

- Per Share: 10.2
- Total: 1020.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $180.00 | Unlimited |
| Max Loss | Unlimited | -$11,020.00 |
| Risk Reward | 0.18x | 1.72x |
| Capital Basis | $4,380.00 | $14,380.00 |
| Cost Credit | Debit $1,020.00 | Debit $1,020.00 |
| Pop | 54.9% | 54.9% |
| Margin Proxy | 4380.0 | — |

**Probabilities:**

- PoP (raw): 0.548927
- Assignment Prob: 0.773633
- P(25% Max Profit): 0.633375
- P(50% Max Profit): 0.609707
- P(100% Max Profit): 0.560753
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | -1020.00 | -2000.00 | -3020.00 | -1.0000 | -0.2740 |
| 85.00 | Downside (15%) | -520.00 | -1500.00 | -2020.00 | -0.5098 | -0.1833 |
| 92.00 | Strike (Lower Middle) | 180.00 | -800.00 | -620.00 | 0.1765 | -0.0563 |
| 98.20 | Breakeven 1 | 180.00 | -180.00 | 0.00 | 0.1765 | 0.0000 |
| 100.00 | Current Market Price | 180.00 | 0.00 | 180.00 | 0.1765 | 0.0163 |
| 108.00 | Strike (Upper Middle) | 180.00 | 800.00 | 980.00 | 0.1765 | 0.0889 |
| 115.00 | Upside (15%) | -520.00 | 1500.00 | 980.00 | -0.5098 | 0.0889 |
| 120.00 | Strike (Highest) | -1020.00 | 2000.00 | 980.00 | -1.0000 | 0.0889 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1020.00 | -11020.00 | -0.7663 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | -1020.00 | -3020.00 | -0.2740 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -520.00 | -2020.00 | -0.1833 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | 180.00 | -620.00 | -0.0563 |
| breakeven_1 | Breakeven 1 | 98.20 | -1.80% | 180.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 180.00 | 180.00 | 0.0163 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | 180.00 | 980.00 | 0.0889 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -520.00 | 980.00 | 0.0889 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | -1020.00 | 980.00 | 0.0889 |
| infinity | Stock to Infinity | — | — | Unlimited | 108980.00 | 7.5786 |

---

### Long Call Condor (ID=28) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 80.00 | 21.00 | 100 |
| 2 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 3 | CALL | Short 1 | 108.00 | 1.90 | 100 |
| 4 | CALL | Long 1 | 120.00 | 1.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [60.2]
- Options Max PnL: 180.0
- Options Min PnL: -1020.0
- Combined Max PnL: 23980.0
- Combined Min PnL: -6020.0

**Net Premium:**

- Per Share: 10.2
- Total: 1020.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $180.00 | Unlimited |
| Max Loss | Unlimited | -$6,020.00 |
| Risk Reward | 0.18x | 3.98x |
| Capital Basis | $4,380.00 | $9,380.00 |
| Cost Credit | Debit $1,020.00 | Debit $1,020.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 4380.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.773633
- P(25% Max Profit): 0.633375
- P(50% Max Profit): 0.609707
- P(100% Max Profit): 0.560753
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -1020.00 | 0.00 | -1020.00 | -1.0000 | -0.1694 |
| 60.20 | Breakeven 1 | -1020.00 | 1020.00 | 0.00 | -1.0000 | 0.0000 |
| 80.00 | Strike (Lowest) | -1020.00 | 3000.00 | 1980.00 | -1.0000 | 0.3289 |
| 85.00 | Downside (15%) | -520.00 | 3500.00 | 2980.00 | -0.5098 | 0.4950 |
| 92.00 | Strike (Lower Middle) | 180.00 | 4200.00 | 4380.00 | 0.1765 | 0.7276 |
| 100.00 | Current Market Price | 180.00 | 5000.00 | 5180.00 | 0.1765 | 0.8605 |
| 108.00 | Strike (Upper Middle) | 180.00 | 5800.00 | 5980.00 | 0.1765 | 0.9934 |
| 115.00 | Upside (15%) | -520.00 | 6500.00 | 5980.00 | -0.5098 | 0.9934 |
| 120.00 | Strike (Highest) | -1020.00 | 7000.00 | 5980.00 | -1.0000 | 0.9934 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1020.00 | -6020.00 | -0.6418 |
| breakeven_1 | Breakeven 1 | 60.20 | -39.80% | -1020.00 | 0.00 | 0.0000 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | -1020.00 | 1980.00 | 0.3289 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -520.00 | 2980.00 | 0.4950 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | 180.00 | 4380.00 | 0.7276 |
| spot | Current Market Price | 100.00 | 0.00% | 180.00 | 5180.00 | 0.8605 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | 180.00 | 5980.00 | 0.9934 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -520.00 | 5980.00 | 0.9934 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | -1020.00 | 5980.00 | 0.9934 |
| infinity | Stock to Infinity | — | — | Unlimited | 113980.00 | 12.1514 |

---

### Long Call Condor (ID=28) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 80.00 | 21.00 | 100 |
| 2 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 3 | CALL | Short 1 | 108.00 | 1.90 | 100 |
| 4 | CALL | Long 1 | 120.00 | 1.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [125.2]
- Options Max PnL: 180.0
- Options Min PnL: -1020.0
- Combined Max PnL: 17480.0
- Combined Min PnL: -12520.0

**Net Premium:**

- Per Share: 10.2
- Total: 1020.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $180.00 | Unlimited |
| Max Loss | Unlimited | -$12,520.00 |
| Risk Reward | 0.18x | 1.40x |
| Capital Basis | $4,380.00 | $15,880.00 |
| Cost Credit | Debit $1,020.00 | Debit $1,020.00 |
| Pop | 1.3% | 1.3% |
| Margin Proxy | 4380.0 | — |

**Probabilities:**

- PoP (raw): 0.013355
- Assignment Prob: 0.773633
- P(25% Max Profit): 0.633375
- P(50% Max Profit): 0.609707
- P(100% Max Profit): 0.560753
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | -1020.00 | -3500.00 | -4520.00 | -1.0000 | -0.3610 |
| 85.00 | Downside (15%) | -520.00 | -3000.00 | -3520.00 | -0.5098 | -0.2812 |
| 92.00 | Strike (Lower Middle) | 180.00 | -2300.00 | -2120.00 | 0.1765 | -0.1693 |
| 100.00 | Current Market Price | 180.00 | -1500.00 | -1320.00 | 0.1765 | -0.1054 |
| 108.00 | Strike (Upper Middle) | 180.00 | -700.00 | -520.00 | 0.1765 | -0.0415 |
| 115.00 | Upside (15%) | -520.00 | 0.00 | -520.00 | -0.5098 | -0.0415 |
| 120.00 | Strike (Highest) | -1020.00 | 500.00 | -520.00 | -1.0000 | -0.0415 |
| 125.20 | Breakeven 1 | -1020.00 | 1020.00 | 0.00 | -1.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1020.00 | -12520.00 | -0.7884 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | -1020.00 | -4520.00 | -0.3610 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -520.00 | -3520.00 | -0.2812 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | 180.00 | -2120.00 | -0.1693 |
| spot | Current Market Price | 100.00 | 0.00% | 180.00 | -1320.00 | -0.1054 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | 180.00 | -520.00 | -0.0415 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -520.00 | -520.00 | -0.0415 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | -1020.00 | -520.00 | -0.0415 |
| breakeven_1 | Breakeven 1 | 125.20 | 25.20% | -1020.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | 107480.00 | 6.7683 |

---

### Long Put Condor (ID=29) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 80.00 | 1.00 | 100 |
| 2 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 3 | PUT | Short 1 | 108.00 | 9.90 | 100 |
| 4 | PUT | Long 1 | 120.00 | 21.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [90.2, 109.8]
- Options Max PnL: 180.0
- Options Min PnL: -1020.0
- Combined Max PnL: 180.0
- Combined Min PnL: -1020.0

**Net Premium:**

- Per Share: 10.2
- Total: 1020.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $180.00 | $180.00 |
| Max Loss | -$1,020.00 | -$1,020.00 |
| Risk Reward | 0.18x | 0.18x |
| Capital Basis | $1,020.00 | $1,020.00 |
| Cost Credit | Debit $1,020.00 | Debit $1,020.00 |
| Pop | 65.6% | 65.6% |
| Margin Proxy | 1020.0 | — |

**Probabilities:**

- PoP (raw): 0.656141
- Assignment Prob: 0.786086
- P(25% Max Profit): 0.633375
- P(50% Max Profit): 0.609707
- P(100% Max Profit): 0.560753
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | -1020.00 | 0.00 | -1020.00 | -1.0000 | -1.0000 |
| 85.00 | Downside (15%) | -520.00 | 0.00 | -520.00 | -0.5098 | -0.5098 |
| 90.20 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 92.00 | Strike (Lower Middle) | 180.00 | 0.00 | 180.00 | 0.1765 | 0.1765 |
| 100.00 | Current Market Price | 180.00 | 0.00 | 180.00 | 0.1765 | 0.1765 |
| 108.00 | Strike (Upper Middle) | 180.00 | 0.00 | 180.00 | 0.1765 | 0.1765 |
| 109.80 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -520.00 | 0.00 | -520.00 | -0.5098 | -0.5098 |
| 120.00 | Strike (Highest) | -1020.00 | 0.00 | -1020.00 | -1.0000 | -1.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1020.00 | -1020.00 | -1.0000 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | -1020.00 | -1020.00 | -1.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -520.00 | -520.00 | -0.5098 |
| breakeven_1 | Breakeven 1 | 90.20 | -9.80% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | 180.00 | 180.00 | 0.1765 |
| spot | Current Market Price | 100.00 | 0.00% | 180.00 | 180.00 | 0.1765 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | 180.00 | 180.00 | 0.1765 |
| breakeven_2 | Breakeven 2 | 109.80 | 9.80% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -520.00 | -520.00 | -0.5098 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | -1020.00 | -1020.00 | -1.0000 |
| infinity | Stock to Infinity | — | — | -1020.00 | -1020.00 | -1.0000 |

---

### Long Put Condor (ID=29) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 80.00 | 1.00 | 100 |
| 2 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 3 | PUT | Short 1 | 108.00 | 9.90 | 100 |
| 4 | PUT | Long 1 | 120.00 | 21.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [98.2]
- Options Max PnL: 180.0
- Options Min PnL: -1020.0
- Combined Max PnL: 18980.0
- Combined Min PnL: -11020.0

**Net Premium:**

- Per Share: 10.2
- Total: 1020.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $180.00 | Unlimited |
| Max Loss | -$1,020.00 | -$11,020.00 |
| Risk Reward | 0.18x | 1.72x |
| Capital Basis | $4,380.00 | $14,380.00 |
| Cost Credit | Debit $1,020.00 | Debit $1,020.00 |
| Pop | 54.9% | 54.9% |
| Margin Proxy | 4380.0 | — |

**Probabilities:**

- PoP (raw): 0.548927
- Assignment Prob: 0.786086
- P(25% Max Profit): 0.633375
- P(50% Max Profit): 0.609707
- P(100% Max Profit): 0.560753
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | -1020.00 | -2000.00 | -3020.00 | -1.0000 | -0.2740 |
| 85.00 | Downside (15%) | -520.00 | -1500.00 | -2020.00 | -0.5098 | -0.1833 |
| 92.00 | Strike (Lower Middle) | 180.00 | -800.00 | -620.00 | 0.1765 | -0.0563 |
| 98.20 | Breakeven 1 | 180.00 | -180.00 | 0.00 | 0.1765 | 0.0000 |
| 100.00 | Current Market Price | 180.00 | 0.00 | 180.00 | 0.1765 | 0.0163 |
| 108.00 | Strike (Upper Middle) | 180.00 | 800.00 | 980.00 | 0.1765 | 0.0889 |
| 115.00 | Upside (15%) | -520.00 | 1500.00 | 980.00 | -0.5098 | 0.0889 |
| 120.00 | Strike (Highest) | -1020.00 | 2000.00 | 980.00 | -1.0000 | 0.0889 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1020.00 | -11020.00 | -0.7663 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | -1020.00 | -3020.00 | -0.2740 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -520.00 | -2020.00 | -0.1833 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | 180.00 | -620.00 | -0.0563 |
| breakeven_1 | Breakeven 1 | 98.20 | -1.80% | 180.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 180.00 | 180.00 | 0.0163 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | 180.00 | 980.00 | 0.0889 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -520.00 | 980.00 | 0.0889 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | -1020.00 | 980.00 | 0.0889 |
| infinity | Stock to Infinity | — | — | -1020.00 | 108980.00 | 7.5786 |

---

### Long Put Condor (ID=29) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 80.00 | 1.00 | 100 |
| 2 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 3 | PUT | Short 1 | 108.00 | 9.90 | 100 |
| 4 | PUT | Long 1 | 120.00 | 21.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [60.2]
- Options Max PnL: 180.0
- Options Min PnL: -1020.0
- Combined Max PnL: 23980.0
- Combined Min PnL: -6020.0

**Net Premium:**

- Per Share: 10.2
- Total: 1020.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $180.00 | Unlimited |
| Max Loss | -$1,020.00 | -$6,020.00 |
| Risk Reward | 0.18x | 3.98x |
| Capital Basis | $4,380.00 | $9,380.00 |
| Cost Credit | Debit $1,020.00 | Debit $1,020.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 4380.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.786086
- P(25% Max Profit): 0.633375
- P(50% Max Profit): 0.609707
- P(100% Max Profit): 0.560753
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -1020.00 | 0.00 | -1020.00 | -1.0000 | -0.1694 |
| 60.20 | Breakeven 1 | -1020.00 | 1020.00 | -0.00 | -1.0000 | -0.0000 |
| 80.00 | Strike (Lowest) | -1020.00 | 3000.00 | 1980.00 | -1.0000 | 0.3289 |
| 85.00 | Downside (15%) | -520.00 | 3500.00 | 2980.00 | -0.5098 | 0.4950 |
| 92.00 | Strike (Lower Middle) | 180.00 | 4200.00 | 4380.00 | 0.1765 | 0.7276 |
| 100.00 | Current Market Price | 180.00 | 5000.00 | 5180.00 | 0.1765 | 0.8605 |
| 108.00 | Strike (Upper Middle) | 180.00 | 5800.00 | 5980.00 | 0.1765 | 0.9934 |
| 115.00 | Upside (15%) | -520.00 | 6500.00 | 5980.00 | -0.5098 | 0.9934 |
| 120.00 | Strike (Highest) | -1020.00 | 7000.00 | 5980.00 | -1.0000 | 0.9934 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1020.00 | -6020.00 | -0.6418 |
| breakeven_1 | Breakeven 1 | 60.20 | -39.80% | -1020.00 | -0.00 | -0.0000 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | -1020.00 | 1980.00 | 0.3289 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -520.00 | 2980.00 | 0.4950 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | 180.00 | 4380.00 | 0.7276 |
| spot | Current Market Price | 100.00 | 0.00% | 180.00 | 5180.00 | 0.8605 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | 180.00 | 5980.00 | 0.9934 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -520.00 | 5980.00 | 0.9934 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | -1020.00 | 5980.00 | 0.9934 |
| infinity | Stock to Infinity | — | — | -1020.00 | 113980.00 | 12.1514 |

---

### Long Put Condor (ID=29) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 80.00 | 1.00 | 100 |
| 2 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 3 | PUT | Short 1 | 108.00 | 9.90 | 100 |
| 4 | PUT | Long 1 | 120.00 | 21.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [125.2]
- Options Max PnL: 180.0
- Options Min PnL: -1020.0
- Combined Max PnL: 17480.0
- Combined Min PnL: -12520.0

**Net Premium:**

- Per Share: 10.2
- Total: 1020.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $180.00 | Unlimited |
| Max Loss | -$1,020.00 | -$12,520.00 |
| Risk Reward | 0.18x | 1.40x |
| Capital Basis | $4,380.00 | $15,880.00 |
| Cost Credit | Debit $1,020.00 | Debit $1,020.00 |
| Pop | 1.3% | 1.3% |
| Margin Proxy | 4380.0 | — |

**Probabilities:**

- PoP (raw): 0.013355
- Assignment Prob: 0.786086
- P(25% Max Profit): 0.633375
- P(50% Max Profit): 0.609707
- P(100% Max Profit): 0.560753
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | -1020.00 | -3500.00 | -4520.00 | -1.0000 | -0.3610 |
| 85.00 | Downside (15%) | -520.00 | -3000.00 | -3520.00 | -0.5098 | -0.2812 |
| 92.00 | Strike (Lower Middle) | 180.00 | -2300.00 | -2120.00 | 0.1765 | -0.1693 |
| 100.00 | Current Market Price | 180.00 | -1500.00 | -1320.00 | 0.1765 | -0.1054 |
| 108.00 | Strike (Upper Middle) | 180.00 | -700.00 | -520.00 | 0.1765 | -0.0415 |
| 115.00 | Upside (15%) | -520.00 | 0.00 | -520.00 | -0.5098 | -0.0415 |
| 120.00 | Strike (Highest) | -1020.00 | 500.00 | -520.00 | -1.0000 | -0.0415 |
| 125.20 | Breakeven 1 | -1020.00 | 1020.00 | 0.00 | -1.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1020.00 | -12520.00 | -0.7884 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | -1020.00 | -4520.00 | -0.3610 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -520.00 | -3520.00 | -0.2812 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | 180.00 | -2120.00 | -0.1693 |
| spot | Current Market Price | 100.00 | 0.00% | 180.00 | -1320.00 | -0.1054 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | 180.00 | -520.00 | -0.0415 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -520.00 | -520.00 | -0.0415 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | -1020.00 | -520.00 | -0.0415 |
| breakeven_1 | Breakeven 1 | 125.20 | 25.20% | -1020.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | -1020.00 | 107480.00 | 6.7683 |

---

### Iron Condor (ID=30) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 80.00 | 1.00 | 100 |
| 2 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 3 | CALL | Short 1 | 108.00 | 1.90 | 100 |
| 4 | CALL | Long 1 | 120.00 | 1.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [90.2, 109.8]
- Options Max PnL: 180.0
- Options Min PnL: -1020.0
- Combined Max PnL: 180.0
- Combined Min PnL: -1020.0

**Net Premium:**

- Per Share: -1.8
- Total: -180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $180.00 | $180.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.18x | 0.18x |
| Capital Basis | $2,780.00 | $2,780.00 |
| Cost Credit | Credit $180.00 | Credit $180.00 |
| Pop | 65.6% | 65.6% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.656141
- Assignment Prob: 0.440281
- P(25% Max Profit): 0.633375
- P(50% Max Profit): 0.609707
- P(100% Max Profit): 0.560753
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | -1020.00 | 0.00 | -1020.00 | -1.0000 | -1.0000 |
| 85.00 | Downside (15%) | -520.00 | 0.00 | -520.00 | -0.5098 | -0.5098 |
| 90.20 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 92.00 | Strike (Lower Middle) | 180.00 | 0.00 | 180.00 | 0.1765 | 0.1765 |
| 100.00 | Current Market Price | 180.00 | 0.00 | 180.00 | 0.1765 | 0.1765 |
| 108.00 | Strike (Upper Middle) | 180.00 | 0.00 | 180.00 | 0.1765 | 0.1765 |
| 109.80 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -520.00 | 0.00 | -520.00 | -0.5098 | -0.5098 |
| 120.00 | Strike (Highest) | -1020.00 | 0.00 | -1020.00 | -1.0000 | -1.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1020.00 | -1020.00 | -0.3669 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | -1020.00 | -1020.00 | -1.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -520.00 | -520.00 | -0.5098 |
| breakeven_1 | Breakeven 1 | 90.20 | -9.80% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | 180.00 | 180.00 | 0.1765 |
| spot | Current Market Price | 100.00 | 0.00% | 180.00 | 180.00 | 0.1765 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | 180.00 | 180.00 | 0.1765 |
| breakeven_2 | Breakeven 2 | 109.80 | 9.80% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -520.00 | -520.00 | -0.5098 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | -1020.00 | -1020.00 | -1.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | -1020.00 | -0.3669 |

---

### Iron Condor (ID=30) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 80.00 | 1.00 | 100 |
| 2 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 3 | CALL | Short 1 | 108.00 | 1.90 | 100 |
| 4 | CALL | Long 1 | 120.00 | 1.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [98.2]
- Options Max PnL: 180.0
- Options Min PnL: -1020.0
- Combined Max PnL: 18980.0
- Combined Min PnL: -11020.0

**Net Premium:**

- Per Share: -1.8
- Total: -180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $180.00 | Unlimited |
| Max Loss | Unlimited | -$11,020.00 |
| Risk Reward | 0.18x | 1.72x |
| Capital Basis | $2,780.00 | $12,780.00 |
| Cost Credit | Credit $180.00 | Credit $180.00 |
| Pop | 54.9% | 54.9% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.548927
- Assignment Prob: 0.440281
- P(25% Max Profit): 0.633375
- P(50% Max Profit): 0.609707
- P(100% Max Profit): 0.560753
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | -1020.00 | -2000.00 | -3020.00 | -1.0000 | -0.2740 |
| 85.00 | Downside (15%) | -520.00 | -1500.00 | -2020.00 | -0.5098 | -0.1833 |
| 92.00 | Strike (Lower Middle) | 180.00 | -800.00 | -620.00 | 0.1765 | -0.0563 |
| 98.20 | Breakeven 1 | 180.00 | -180.00 | 0.00 | 0.1765 | 0.0000 |
| 100.00 | Current Market Price | 180.00 | 0.00 | 180.00 | 0.1765 | 0.0163 |
| 108.00 | Strike (Upper Middle) | 180.00 | 800.00 | 980.00 | 0.1765 | 0.0889 |
| 115.00 | Upside (15%) | -520.00 | 1500.00 | 980.00 | -0.5098 | 0.0889 |
| 120.00 | Strike (Highest) | -1020.00 | 2000.00 | 980.00 | -1.0000 | 0.0889 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1020.00 | -11020.00 | -0.8623 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | -1020.00 | -3020.00 | -0.2740 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -520.00 | -2020.00 | -0.1833 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | 180.00 | -620.00 | -0.0563 |
| breakeven_1 | Breakeven 1 | 98.20 | -1.80% | 180.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 180.00 | 180.00 | 0.0163 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | 180.00 | 980.00 | 0.0889 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -520.00 | 980.00 | 0.0889 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | -1020.00 | 980.00 | 0.0889 |
| infinity | Stock to Infinity | — | — | Unlimited | 108980.00 | 8.5274 |

---

### Iron Condor (ID=30) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 80.00 | 1.00 | 100 |
| 2 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 3 | CALL | Short 1 | 108.00 | 1.90 | 100 |
| 4 | CALL | Long 1 | 120.00 | 1.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [60.2]
- Options Max PnL: 180.0
- Options Min PnL: -1020.0
- Combined Max PnL: 23980.0
- Combined Min PnL: -6020.0

**Net Premium:**

- Per Share: -1.8
- Total: -180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $180.00 | Unlimited |
| Max Loss | Unlimited | -$6,020.00 |
| Risk Reward | 0.18x | 3.98x |
| Capital Basis | $2,780.00 | $7,780.00 |
| Cost Credit | Credit $180.00 | Credit $180.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.440281
- P(25% Max Profit): 0.633375
- P(50% Max Profit): 0.609707
- P(100% Max Profit): 0.560753
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -1020.00 | 0.00 | -1020.00 | -1.0000 | -0.1694 |
| 60.20 | Breakeven 1 | -1020.00 | 1020.00 | 0.00 | -1.0000 | 0.0000 |
| 80.00 | Strike (Lowest) | -1020.00 | 3000.00 | 1980.00 | -1.0000 | 0.3289 |
| 85.00 | Downside (15%) | -520.00 | 3500.00 | 2980.00 | -0.5098 | 0.4950 |
| 92.00 | Strike (Lower Middle) | 180.00 | 4200.00 | 4380.00 | 0.1765 | 0.7276 |
| 100.00 | Current Market Price | 180.00 | 5000.00 | 5180.00 | 0.1765 | 0.8605 |
| 108.00 | Strike (Upper Middle) | 180.00 | 5800.00 | 5980.00 | 0.1765 | 0.9934 |
| 115.00 | Upside (15%) | -520.00 | 6500.00 | 5980.00 | -0.5098 | 0.9934 |
| 120.00 | Strike (Highest) | -1020.00 | 7000.00 | 5980.00 | -1.0000 | 0.9934 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1020.00 | -6020.00 | -0.7738 |
| breakeven_1 | Breakeven 1 | 60.20 | -39.80% | -1020.00 | 0.00 | 0.0000 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | -1020.00 | 1980.00 | 0.3289 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -520.00 | 2980.00 | 0.4950 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | 180.00 | 4380.00 | 0.7276 |
| spot | Current Market Price | 100.00 | 0.00% | 180.00 | 5180.00 | 0.8605 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | 180.00 | 5980.00 | 0.9934 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -520.00 | 5980.00 | 0.9934 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | -1020.00 | 5980.00 | 0.9934 |
| infinity | Stock to Infinity | — | — | Unlimited | 113980.00 | 14.6504 |

---

### Iron Condor (ID=30) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 80.00 | 1.00 | 100 |
| 2 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 3 | CALL | Short 1 | 108.00 | 1.90 | 100 |
| 4 | CALL | Long 1 | 120.00 | 1.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [125.2]
- Options Max PnL: 180.0
- Options Min PnL: -1020.0
- Combined Max PnL: 17480.0
- Combined Min PnL: -12520.0

**Net Premium:**

- Per Share: -1.8
- Total: -180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $180.00 | Unlimited |
| Max Loss | Unlimited | -$12,520.00 |
| Risk Reward | 0.18x | 1.40x |
| Capital Basis | $2,780.00 | $14,280.00 |
| Cost Credit | Credit $180.00 | Credit $180.00 |
| Pop | 1.3% | 1.3% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.013355
- Assignment Prob: 0.440281
- P(25% Max Profit): 0.633375
- P(50% Max Profit): 0.609707
- P(100% Max Profit): 0.560753
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | -1020.00 | -3500.00 | -4520.00 | -1.0000 | -0.3610 |
| 85.00 | Downside (15%) | -520.00 | -3000.00 | -3520.00 | -0.5098 | -0.2812 |
| 92.00 | Strike (Lower Middle) | 180.00 | -2300.00 | -2120.00 | 0.1765 | -0.1693 |
| 100.00 | Current Market Price | 180.00 | -1500.00 | -1320.00 | 0.1765 | -0.1054 |
| 108.00 | Strike (Upper Middle) | 180.00 | -700.00 | -520.00 | 0.1765 | -0.0415 |
| 115.00 | Upside (15%) | -520.00 | 0.00 | -520.00 | -0.5098 | -0.0415 |
| 120.00 | Strike (Highest) | -1020.00 | 500.00 | -520.00 | -1.0000 | -0.0415 |
| 125.20 | Breakeven 1 | -1020.00 | 1020.00 | 0.00 | -1.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1020.00 | -12520.00 | -0.8768 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | -1020.00 | -4520.00 | -0.3610 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -520.00 | -3520.00 | -0.2812 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | 180.00 | -2120.00 | -0.1693 |
| spot | Current Market Price | 100.00 | 0.00% | 180.00 | -1320.00 | -0.1054 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | 180.00 | -520.00 | -0.0415 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -520.00 | -520.00 | -0.0415 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | -1020.00 | -520.00 | -0.0415 |
| breakeven_1 | Breakeven 1 | 125.20 | 25.20% | -1020.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | 107480.00 | 7.5266 |

---

### Short Call Butterfly (ID=31) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 85.00 | 16.38 | 100 |
| 2 | CALL | Long 2 | 100.00 | 2.50 | 100 |
| 3 | CALL | Short 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [97.76, 102.24]
- Options Max PnL: 1276.0
- Options Min PnL: -224.0
- Combined Max PnL: 1276.0
- Combined Min PnL: -224.0

**Net Premium:**

- Per Share: -12.76
- Total: -1276.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,276.00 | $1,276.00 |
| Max Loss | -$224.00 | -$224.00 |
| Risk Reward | 5.70x | 5.70x |
| Capital Basis | $224.00 | $224.00 |
| Cost Credit | Credit $1,276.00 | Credit $1,276.00 |
| Pop | 82.9% | 82.9% |
| Margin Proxy | 224.0 | — |

**Probabilities:**

- PoP (raw): 0.829425
- Assignment Prob: 0.934835
- P(25% Max Profit): 0.601014
- P(50% Max Profit): 0.405469
- P(100% Max Profit): 0.149761
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 5.6964 |
| 97.76 | Breakeven 1 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 100.00 | Current Market Price | -224.00 | 0.00 | -224.00 | -1.0000 | -1.0000 |
| 102.24 | Breakeven 2 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 5.6964 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 5.6964 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1276.00 | 1276.00 | 5.6964 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1276.00 | 1276.00 | 5.6964 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1276.00 | 1276.00 | 5.6964 |
| breakeven_1 | Breakeven 1 | 97.76 | -2.24% | -0.00 | -0.00 | -0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -1.0000 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 102.24 | 2.24% | -0.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1276.00 | 1276.00 | 5.6964 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1276.00 | 1276.00 | 5.6964 |
| infinity | Stock to Infinity | — | — | 1276.00 | 1276.00 | 5.6964 |

---

### Short Call Butterfly (ID=31) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 85.00 | 16.38 | 100 |
| 2 | CALL | Long 2 | 100.00 | 2.50 | 100 |
| 3 | CALL | Short 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [101.12]
- Options Max PnL: 1276.0
- Options Min PnL: -224.0
- Combined Max PnL: 21276.0
- Combined Min PnL: -8724.0

**Net Premium:**

- Per Share: -12.76
- Total: -1276.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,276.00 | Unlimited |
| Max Loss | -$224.00 | -$8,724.00 |
| Risk Reward | 5.70x | 2.44x |
| Capital Basis | $4,776.00 | $14,776.00 |
| Cost Credit | Credit $1,276.00 | Credit $1,276.00 |
| Pop | 43.7% | 43.7% |
| Margin Proxy | 4776.0 | — |

**Probabilities:**

- PoP (raw): 0.436769
- Assignment Prob: 0.934835
- P(25% Max Profit): 0.601014
- P(50% Max Profit): 0.405469
- P(100% Max Profit): 0.149761
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1276.00 | -1500.00 | -224.00 | 5.6964 | -0.0219 |
| 100.00 | Current Market Price | -224.00 | 0.00 | -224.00 | -1.0000 | -0.0219 |
| 101.12 | Breakeven 1 | -112.00 | 112.00 | 0.00 | -0.5000 | 0.0000 |
| 115.00 | Upside (15%) | 1276.00 | 1500.00 | 2776.00 | 5.6964 | 0.2715 |
| 115.00 | Upside (15%) | 1276.00 | 1500.00 | 2776.00 | 5.6964 | 0.2715 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1276.00 | -8724.00 | -0.5904 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1276.00 | -224.00 | -0.0219 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1276.00 | -224.00 | -0.0219 |
| spot | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -0.0219 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -0.0219 |
| breakeven_1 | Breakeven 1 | 101.12 | 1.12% | -112.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1276.00 | 2776.00 | 0.2715 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1276.00 | 2776.00 | 0.2715 |
| infinity | Stock to Infinity | — | — | 1276.00 | 106276.00 | 7.1925 |

---

### Short Call Butterfly (ID=31) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 85.00 | 16.38 | 100 |
| 2 | CALL | Long 2 | 100.00 | 2.50 | 100 |
| 3 | CALL | Short 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [37.24]
- Options Max PnL: 1276.0
- Options Min PnL: -224.0
- Combined Max PnL: 26276.0
- Combined Min PnL: -3724.0

**Net Premium:**

- Per Share: -12.76
- Total: -1276.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,276.00 | Unlimited |
| Max Loss | -$224.00 | -$3,724.00 |
| Risk Reward | 5.70x | 7.06x |
| Capital Basis | $4,776.00 | $9,776.00 |
| Cost Credit | Credit $1,276.00 | Credit $1,276.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 4776.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.934835
- P(25% Max Profit): 0.601014
- P(50% Max Profit): 0.405469
- P(100% Max Profit): 0.149761
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 37.24 | Breakeven 1 | 1276.00 | -1276.00 | 0.00 | 5.6964 | 0.0000 |
| 50.00 | Scenario @ 50.00 | 1276.00 | 0.00 | 1276.00 | 5.6964 | 0.2443 |
| 85.00 | Downside (15%) | 1276.00 | 3500.00 | 4776.00 | 5.6964 | 0.9142 |
| 100.00 | Current Market Price | -224.00 | 5000.00 | 4776.00 | -1.0000 | 0.9142 |
| 115.00 | Upside (15%) | 1276.00 | 6500.00 | 7776.00 | 5.6964 | 1.4885 |
| 115.00 | Upside (15%) | 1276.00 | 6500.00 | 7776.00 | 5.6964 | 1.4885 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1276.00 | -3724.00 | -0.3809 |
| breakeven_1 | Breakeven 1 | 37.24 | -62.76% | 1276.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1276.00 | 4776.00 | 0.9142 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1276.00 | 4776.00 | 0.9142 |
| spot | Current Market Price | 100.00 | 0.00% | -224.00 | 4776.00 | 0.9142 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -224.00 | 4776.00 | 0.9142 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1276.00 | 7776.00 | 1.4885 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1276.00 | 7776.00 | 1.4885 |
| infinity | Stock to Infinity | — | — | 1276.00 | 111276.00 | 11.3826 |

---

### Short Call Butterfly (ID=31) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 85.00 | 16.38 | 100 |
| 2 | CALL | Long 2 | 100.00 | 2.50 | 100 |
| 3 | CALL | Short 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [108.62]
- Options Max PnL: 1276.0
- Options Min PnL: -224.0
- Combined Max PnL: 19776.0
- Combined Min PnL: -10224.0

**Net Premium:**

- Per Share: -12.76
- Total: -1276.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,276.00 | Unlimited |
| Max Loss | -$224.00 | -$10,224.00 |
| Risk Reward | 5.70x | 1.93x |
| Capital Basis | $4,776.00 | $16,276.00 |
| Cost Credit | Credit $1,276.00 | Credit $1,276.00 |
| Pop | 19.8% | 19.8% |
| Margin Proxy | 4776.0 | — |

**Probabilities:**

- PoP (raw): 0.198211
- Assignment Prob: 0.934835
- P(25% Max Profit): 0.601014
- P(50% Max Profit): 0.405469
- P(100% Max Profit): 0.149761
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1276.00 | -3000.00 | -1724.00 | 5.6964 | -0.1470 |
| 100.00 | Current Market Price | -224.00 | -1500.00 | -1724.00 | -1.0000 | -0.1470 |
| 108.62 | Breakeven 1 | 638.00 | -638.00 | 0.00 | 2.8482 | 0.0000 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 0.1088 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 0.1088 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1276.00 | -10224.00 | -0.6282 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1276.00 | -1724.00 | -0.1470 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1276.00 | -1724.00 | -0.1470 |
| spot | Current Market Price | 100.00 | 0.00% | -224.00 | -1724.00 | -0.1470 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -224.00 | -1724.00 | -0.1470 |
| breakeven_1 | Breakeven 1 | 108.62 | 8.62% | 638.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1276.00 | 1276.00 | 0.1088 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1276.00 | 1276.00 | 0.1088 |
| infinity | Stock to Infinity | — | — | 1276.00 | 104776.00 | 6.4375 |

---

### Short Put Butterfly (ID=32) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 85.00 | 1.38 | 100 |
| 2 | PUT | Long 2 | 100.00 | 2.50 | 100 |
| 3 | PUT | Short 1 | 115.00 | 16.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [97.76, 102.24]
- Options Max PnL: 1276.0
- Options Min PnL: -224.0
- Combined Max PnL: 1276.0
- Combined Min PnL: -224.0

**Net Premium:**

- Per Share: -12.76
- Total: -1276.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,276.00 | $1,276.00 |
| Max Loss | -$224.00 | -$224.00 |
| Risk Reward | 5.70x | 5.70x |
| Capital Basis | $224.00 | $224.00 |
| Cost Credit | Credit $1,276.00 | Credit $1,276.00 |
| Pop | 82.9% | 82.9% |
| Margin Proxy | 224.0 | — |

**Probabilities:**

- PoP (raw): 0.829425
- Assignment Prob: 0.918877
- P(25% Max Profit): 0.601014
- P(50% Max Profit): 0.405469
- P(100% Max Profit): 0.149761
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 5.6964 |
| 97.76 | Breakeven 1 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 100.00 | Current Market Price | -224.00 | 0.00 | -224.00 | -1.0000 | -1.0000 |
| 102.24 | Breakeven 2 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 5.6964 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 5.6964 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1276.00 | 1276.00 | 5.6964 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1276.00 | 1276.00 | 5.6964 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1276.00 | 1276.00 | 5.6964 |
| breakeven_1 | Breakeven 1 | 97.76 | -2.24% | -0.00 | -0.00 | -0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -1.0000 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 102.24 | 2.24% | -0.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1276.00 | 1276.00 | 5.6964 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1276.00 | 1276.00 | 5.6964 |
| infinity | Stock to Infinity | — | — | 1276.00 | 1276.00 | 5.6964 |

---

### Short Put Butterfly (ID=32) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 85.00 | 1.38 | 100 |
| 2 | PUT | Long 2 | 100.00 | 2.50 | 100 |
| 3 | PUT | Short 1 | 115.00 | 16.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [101.12]
- Options Max PnL: 1276.0
- Options Min PnL: -224.0
- Combined Max PnL: 21276.0
- Combined Min PnL: -8724.0

**Net Premium:**

- Per Share: -12.76
- Total: -1276.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,276.00 | Unlimited |
| Max Loss | -$224.00 | -$8,724.00 |
| Risk Reward | 5.70x | 2.44x |
| Capital Basis | $4,776.00 | $14,776.00 |
| Cost Credit | Credit $1,276.00 | Credit $1,276.00 |
| Pop | 43.7% | 43.7% |
| Margin Proxy | 4776.0 | — |

**Probabilities:**

- PoP (raw): 0.436769
- Assignment Prob: 0.918877
- P(25% Max Profit): 0.601014
- P(50% Max Profit): 0.405469
- P(100% Max Profit): 0.149761
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1276.00 | -1500.00 | -224.00 | 5.6964 | -0.0219 |
| 100.00 | Current Market Price | -224.00 | 0.00 | -224.00 | -1.0000 | -0.0219 |
| 101.12 | Breakeven 1 | -112.00 | 112.00 | 0.00 | -0.5000 | 0.0000 |
| 115.00 | Upside (15%) | 1276.00 | 1500.00 | 2776.00 | 5.6964 | 0.2715 |
| 115.00 | Upside (15%) | 1276.00 | 1500.00 | 2776.00 | 5.6964 | 0.2715 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1276.00 | -8724.00 | -0.5904 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1276.00 | -224.00 | -0.0219 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1276.00 | -224.00 | -0.0219 |
| spot | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -0.0219 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -0.0219 |
| breakeven_1 | Breakeven 1 | 101.12 | 1.12% | -112.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1276.00 | 2776.00 | 0.2715 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1276.00 | 2776.00 | 0.2715 |
| infinity | Stock to Infinity | — | — | 1276.00 | 106276.00 | 7.1925 |

---

### Short Put Butterfly (ID=32) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 85.00 | 1.38 | 100 |
| 2 | PUT | Long 2 | 100.00 | 2.50 | 100 |
| 3 | PUT | Short 1 | 115.00 | 16.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [37.24]
- Options Max PnL: 1276.0
- Options Min PnL: -224.0
- Combined Max PnL: 26276.0
- Combined Min PnL: -3724.0

**Net Premium:**

- Per Share: -12.76
- Total: -1276.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,276.00 | Unlimited |
| Max Loss | -$224.00 | -$3,724.00 |
| Risk Reward | 5.70x | 7.06x |
| Capital Basis | $4,776.00 | $9,776.00 |
| Cost Credit | Credit $1,276.00 | Credit $1,276.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 4776.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.918877
- P(25% Max Profit): 0.601014
- P(50% Max Profit): 0.405469
- P(100% Max Profit): 0.149761
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 37.24 | Breakeven 1 | 1276.00 | -1276.00 | 0.00 | 5.6964 | 0.0000 |
| 50.00 | Scenario @ 50.00 | 1276.00 | 0.00 | 1276.00 | 5.6964 | 0.2443 |
| 85.00 | Downside (15%) | 1276.00 | 3500.00 | 4776.00 | 5.6964 | 0.9142 |
| 100.00 | Current Market Price | -224.00 | 5000.00 | 4776.00 | -1.0000 | 0.9142 |
| 115.00 | Upside (15%) | 1276.00 | 6500.00 | 7776.00 | 5.6964 | 1.4885 |
| 115.00 | Upside (15%) | 1276.00 | 6500.00 | 7776.00 | 5.6964 | 1.4885 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1276.00 | -3724.00 | -0.3809 |
| breakeven_1 | Breakeven 1 | 37.24 | -62.76% | 1276.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1276.00 | 4776.00 | 0.9142 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1276.00 | 4776.00 | 0.9142 |
| spot | Current Market Price | 100.00 | 0.00% | -224.00 | 4776.00 | 0.9142 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -224.00 | 4776.00 | 0.9142 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1276.00 | 7776.00 | 1.4885 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1276.00 | 7776.00 | 1.4885 |
| infinity | Stock to Infinity | — | — | 1276.00 | 111276.00 | 11.3826 |

---

### Short Put Butterfly (ID=32) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 85.00 | 1.38 | 100 |
| 2 | PUT | Long 2 | 100.00 | 2.50 | 100 |
| 3 | PUT | Short 1 | 115.00 | 16.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [108.62]
- Options Max PnL: 1276.0
- Options Min PnL: -224.0
- Combined Max PnL: 19776.0
- Combined Min PnL: -10224.0

**Net Premium:**

- Per Share: -12.76
- Total: -1276.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,276.00 | Unlimited |
| Max Loss | -$224.00 | -$10,224.00 |
| Risk Reward | 5.70x | 1.93x |
| Capital Basis | $4,776.00 | $16,276.00 |
| Cost Credit | Credit $1,276.00 | Credit $1,276.00 |
| Pop | 19.8% | 19.8% |
| Margin Proxy | 4776.0 | — |

**Probabilities:**

- PoP (raw): 0.198211
- Assignment Prob: 0.918877
- P(25% Max Profit): 0.601014
- P(50% Max Profit): 0.405469
- P(100% Max Profit): 0.149761
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1276.00 | -3000.00 | -1724.00 | 5.6964 | -0.1470 |
| 100.00 | Current Market Price | -224.00 | -1500.00 | -1724.00 | -1.0000 | -0.1470 |
| 108.62 | Breakeven 1 | 638.00 | -638.00 | 0.00 | 2.8482 | 0.0000 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 0.1088 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 0.1088 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1276.00 | -10224.00 | -0.6282 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1276.00 | -1724.00 | -0.1470 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1276.00 | -1724.00 | -0.1470 |
| spot | Current Market Price | 100.00 | 0.00% | -224.00 | -1724.00 | -0.1470 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -224.00 | -1724.00 | -0.1470 |
| breakeven_1 | Breakeven 1 | 108.62 | 8.62% | 638.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1276.00 | 1276.00 | 0.1088 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1276.00 | 1276.00 | 0.1088 |
| infinity | Stock to Infinity | — | — | 1276.00 | 104776.00 | 6.4375 |

---

### Rev Iron Butterfly (ID=33) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 85.00 | 1.38 | 100 |
| 2 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 3 | CALL | Long 1 | 100.00 | 2.50 | 100 |
| 4 | CALL | Short 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [97.76, 102.24]
- Options Max PnL: 1276.0
- Options Min PnL: -224.0
- Combined Max PnL: 1276.0
- Combined Min PnL: -224.0

**Net Premium:**

- Per Share: 2.24
- Total: 224.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,276.00 | $1,276.00 |
| Max Loss | -$224.00 | -$224.00 |
| Risk Reward | 5.70x | 5.70x |
| Capital Basis | $224.00 | $224.00 |
| Cost Credit | Debit $224.00 | Debit $224.00 |
| Pop | 82.9% | 82.9% |
| Margin Proxy | 224.0 | — |

**Probabilities:**

- PoP (raw): 0.829425
- Assignment Prob: 0.146288
- P(25% Max Profit): 0.601014
- P(50% Max Profit): 0.405469
- P(100% Max Profit): 0.149761
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 5.6964 |
| 97.76 | Breakeven 1 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 100.00 | Current Market Price | -224.00 | 0.00 | -224.00 | -1.0000 | -1.0000 |
| 102.24 | Breakeven 2 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 5.6964 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 5.6964 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1276.00 | 1276.00 | 5.6964 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1276.00 | 1276.00 | 5.6964 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1276.00 | 1276.00 | 5.6964 |
| breakeven_1 | Breakeven 1 | 97.76 | -2.24% | -0.00 | -0.00 | -0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -1.0000 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 102.24 | 2.24% | -0.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1276.00 | 1276.00 | 5.6964 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1276.00 | 1276.00 | 5.6964 |
| infinity | Stock to Infinity | — | — | 1276.00 | 1276.00 | 5.6964 |

---

### Rev Iron Butterfly (ID=33) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 85.00 | 1.38 | 100 |
| 2 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 3 | CALL | Long 1 | 100.00 | 2.50 | 100 |
| 4 | CALL | Short 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [101.12]
- Options Max PnL: 1276.0
- Options Min PnL: -224.0
- Combined Max PnL: 21276.0
- Combined Min PnL: -8724.0

**Net Premium:**

- Per Share: 2.24
- Total: 224.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,276.00 | Unlimited |
| Max Loss | -$224.00 | -$8,724.00 |
| Risk Reward | 5.70x | 2.44x |
| Capital Basis | $2,276.00 | $12,276.00 |
| Cost Credit | Debit $224.00 | Debit $224.00 |
| Pop | 43.7% | 43.7% |
| Margin Proxy | 2276.0 | — |

**Probabilities:**

- PoP (raw): 0.436769
- Assignment Prob: 0.146288
- P(25% Max Profit): 0.601014
- P(50% Max Profit): 0.405469
- P(100% Max Profit): 0.149761
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1276.00 | -1500.00 | -224.00 | 5.6964 | -0.0219 |
| 100.00 | Current Market Price | -224.00 | 0.00 | -224.00 | -1.0000 | -0.0219 |
| 101.12 | Breakeven 1 | -112.00 | 112.00 | 0.00 | -0.5000 | 0.0000 |
| 115.00 | Upside (15%) | 1276.00 | 1500.00 | 2776.00 | 5.6964 | 0.2715 |
| 115.00 | Upside (15%) | 1276.00 | 1500.00 | 2776.00 | 5.6964 | 0.2715 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1276.00 | -8724.00 | -0.7107 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1276.00 | -224.00 | -0.0219 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1276.00 | -224.00 | -0.0219 |
| spot | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -0.0219 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -0.0219 |
| breakeven_1 | Breakeven 1 | 101.12 | 1.12% | -112.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1276.00 | 2776.00 | 0.2715 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1276.00 | 2776.00 | 0.2715 |
| infinity | Stock to Infinity | — | — | 1276.00 | 106276.00 | 8.6572 |

---

### Rev Iron Butterfly (ID=33) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 85.00 | 1.38 | 100 |
| 2 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 3 | CALL | Long 1 | 100.00 | 2.50 | 100 |
| 4 | CALL | Short 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [37.24]
- Options Max PnL: 1276.0
- Options Min PnL: -224.0
- Combined Max PnL: 26276.0
- Combined Min PnL: -3724.0

**Net Premium:**

- Per Share: 2.24
- Total: 224.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,276.00 | Unlimited |
| Max Loss | -$224.00 | -$3,724.00 |
| Risk Reward | 5.70x | 7.06x |
| Capital Basis | $2,276.00 | $7,276.00 |
| Cost Credit | Debit $224.00 | Debit $224.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 2276.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.146288
- P(25% Max Profit): 0.601014
- P(50% Max Profit): 0.405469
- P(100% Max Profit): 0.149761
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 37.24 | Breakeven 1 | 1276.00 | -1276.00 | 0.00 | 5.6964 | 0.0000 |
| 50.00 | Scenario @ 50.00 | 1276.00 | 0.00 | 1276.00 | 5.6964 | 0.2443 |
| 85.00 | Downside (15%) | 1276.00 | 3500.00 | 4776.00 | 5.6964 | 0.9142 |
| 100.00 | Current Market Price | -224.00 | 5000.00 | 4776.00 | -1.0000 | 0.9142 |
| 115.00 | Upside (15%) | 1276.00 | 6500.00 | 7776.00 | 5.6964 | 1.4885 |
| 115.00 | Upside (15%) | 1276.00 | 6500.00 | 7776.00 | 5.6964 | 1.4885 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1276.00 | -3724.00 | -0.5118 |
| breakeven_1 | Breakeven 1 | 37.24 | -62.76% | 1276.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1276.00 | 4776.00 | 0.9142 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1276.00 | 4776.00 | 0.9142 |
| spot | Current Market Price | 100.00 | 0.00% | -224.00 | 4776.00 | 0.9142 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -224.00 | 4776.00 | 0.9142 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1276.00 | 7776.00 | 1.4885 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1276.00 | 7776.00 | 1.4885 |
| infinity | Stock to Infinity | — | — | 1276.00 | 111276.00 | 15.2936 |

---

### Rev Iron Butterfly (ID=33) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 85.00 | 1.38 | 100 |
| 2 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 3 | CALL | Long 1 | 100.00 | 2.50 | 100 |
| 4 | CALL | Short 1 | 115.00 | 1.38 | 100 |

**Payoff:**

- Grid Size: 303 points
- Strikes: [85.0, 100.0, 115.0]
- Breakevens: [108.62]
- Options Max PnL: 1276.0
- Options Min PnL: -224.0
- Combined Max PnL: 19776.0
- Combined Min PnL: -10224.0

**Net Premium:**

- Per Share: 2.24
- Total: 224.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,276.00 | Unlimited |
| Max Loss | -$224.00 | -$10,224.00 |
| Risk Reward | 5.70x | 1.93x |
| Capital Basis | $2,276.00 | $13,776.00 |
| Cost Credit | Debit $224.00 | Debit $224.00 |
| Pop | 19.8% | 19.8% |
| Margin Proxy | 2276.0 | — |

**Probabilities:**

- PoP (raw): 0.198211
- Assignment Prob: 0.146288
- P(25% Max Profit): 0.601014
- P(50% Max Profit): 0.405469
- P(100% Max Profit): 0.149761
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1276.00 | -3000.00 | -1724.00 | 5.6964 | -0.1470 |
| 100.00 | Current Market Price | -224.00 | -1500.00 | -1724.00 | -1.0000 | -0.1470 |
| 108.62 | Breakeven 1 | 638.00 | -638.00 | 0.00 | 2.8482 | 0.0000 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 0.1088 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 0.1088 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1276.00 | -10224.00 | -0.7422 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1276.00 | -1724.00 | -0.1470 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1276.00 | -1724.00 | -0.1470 |
| spot | Current Market Price | 100.00 | 0.00% | -224.00 | -1724.00 | -0.1470 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -224.00 | -1724.00 | -0.1470 |
| breakeven_1 | Breakeven 1 | 108.62 | 8.62% | 638.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1276.00 | 1276.00 | 0.1088 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1276.00 | 1276.00 | 0.1088 |
| infinity | Stock to Infinity | — | — | 1276.00 | 104776.00 | 7.6057 |

---

### Short Call Condor (ID=34) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 80.00 | 21.00 | 100 |
| 2 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 3 | CALL | Long 1 | 108.00 | 1.90 | 100 |
| 4 | CALL | Short 1 | 120.00 | 1.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [90.2, 109.8]
- Options Max PnL: 1020.0
- Options Min PnL: -180.0
- Combined Max PnL: 1020.0
- Combined Min PnL: -180.0

**Net Premium:**

- Per Share: -10.2
- Total: -1020.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$180.00 | -$180.00 |
| Risk Reward | 5.67x | 5.67x |
| Capital Basis | $5,200.00 | $5,200.00 |
| Cost Credit | Credit $1,020.00 | Credit $1,020.00 |
| Pop | 34.4% | 34.4% |
| Margin Proxy | 5200.0 | — |

**Probabilities:**

- PoP (raw): 0.343859
- Assignment Prob: 0.981981
- P(25% Max Profit): 0.232139
- P(50% Max Profit): 0.149004
- P(100% Max Profit): 0.054568
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | 1020.00 | 0.00 | 1020.00 | 5.6667 | 5.6667 |
| 85.00 | Downside (15%) | 520.00 | 0.00 | 520.00 | 2.8889 | 2.8889 |
| 90.20 | Breakeven 1 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 92.00 | Strike (Lower Middle) | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 100.00 | Current Market Price | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 108.00 | Strike (Upper Middle) | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 109.80 | Breakeven 2 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 115.00 | Upside (15%) | 520.00 | 0.00 | 520.00 | 2.8889 | 2.8889 |
| 120.00 | Strike (Highest) | 1020.00 | 0.00 | 1020.00 | 5.6667 | 5.6667 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1020.00 | 1020.00 | 0.1962 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | 1020.00 | 5.6667 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | 520.00 | 2.8889 |
| breakeven_1 | Breakeven 1 | 90.20 | -9.80% | -0.00 | -0.00 | -0.0000 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | -180.00 | -1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | -180.00 | -1.0000 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | -180.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 109.80 | 9.80% | -0.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 520.00 | 2.8889 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 1020.00 | 5.6667 |
| infinity | Stock to Infinity | — | — | 1020.00 | 1020.00 | 0.1962 |

---

### Short Call Condor (ID=34) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 80.00 | 21.00 | 100 |
| 2 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 3 | CALL | Long 1 | 108.00 | 1.90 | 100 |
| 4 | CALL | Short 1 | 120.00 | 1.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [101.8]
- Options Max PnL: 1020.0
- Options Min PnL: -180.0
- Combined Max PnL: 21020.0
- Combined Min PnL: -8980.0

**Net Premium:**

- Per Share: -10.2
- Total: -1020.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$180.00 | -$8,980.00 |
| Risk Reward | 5.67x | 2.34x |
| Capital Basis | $5,200.00 | $15,200.00 |
| Cost Credit | Credit $1,020.00 | Credit $1,020.00 |
| Pop | 41.1% | 41.1% |
| Margin Proxy | 5200.0 | — |

**Probabilities:**

- PoP (raw): 0.411497
- Assignment Prob: 0.981981
- P(25% Max Profit): 0.232139
- P(50% Max Profit): 0.149004
- P(100% Max Profit): 0.054568
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | 1020.00 | -2000.00 | -980.00 | 5.6667 | -0.0963 |
| 85.00 | Downside (15%) | 520.00 | -1500.00 | -980.00 | 2.8889 | -0.0963 |
| 92.00 | Strike (Lower Middle) | -180.00 | -800.00 | -980.00 | -1.0000 | -0.0963 |
| 100.00 | Current Market Price | -180.00 | 0.00 | -180.00 | -1.0000 | -0.0177 |
| 101.80 | Breakeven 1 | -180.00 | 180.00 | -0.00 | -1.0000 | -0.0000 |
| 108.00 | Strike (Upper Middle) | -180.00 | 800.00 | 620.00 | -1.0000 | 0.0609 |
| 115.00 | Upside (15%) | 520.00 | 1500.00 | 2020.00 | 2.8889 | 0.1984 |
| 120.00 | Strike (Highest) | 1020.00 | 2000.00 | 3020.00 | 5.6667 | 0.2967 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1020.00 | -8980.00 | -0.5908 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | -980.00 | -0.0963 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | -980.00 | -0.0963 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | -980.00 | -0.0963 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | -180.00 | -0.0177 |
| breakeven_1 | Breakeven 1 | 101.80 | 1.80% | -180.00 | -0.00 | -0.0000 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | 620.00 | 0.0609 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 2020.00 | 0.1984 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 3020.00 | 0.2967 |
| infinity | Stock to Infinity | — | — | 1020.00 | 111020.00 | 7.3039 |

---

### Short Call Condor (ID=34) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 80.00 | 21.00 | 100 |
| 2 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 3 | CALL | Long 1 | 108.00 | 1.90 | 100 |
| 4 | CALL | Short 1 | 120.00 | 1.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [39.8]
- Options Max PnL: 1020.0
- Options Min PnL: -180.0
- Combined Max PnL: 26020.0
- Combined Min PnL: -3980.0

**Net Premium:**

- Per Share: -10.2
- Total: -1020.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$180.00 | -$3,980.00 |
| Risk Reward | 5.67x | 6.54x |
| Capital Basis | $5,200.00 | $10,200.00 |
| Cost Credit | Credit $1,020.00 | Credit $1,020.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 5200.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.981981
- P(25% Max Profit): 0.232139
- P(50% Max Profit): 0.149004
- P(100% Max Profit): 0.054568
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 39.80 | Breakeven 1 | 1020.00 | -1020.00 | -0.00 | 5.6667 | -0.0000 |
| 50.00 | Scenario @ 50.00 | 1020.00 | 0.00 | 1020.00 | 5.6667 | 0.1969 |
| 80.00 | Strike (Lowest) | 1020.00 | 3000.00 | 4020.00 | 5.6667 | 0.7761 |
| 85.00 | Downside (15%) | 520.00 | 3500.00 | 4020.00 | 2.8889 | 0.7761 |
| 92.00 | Strike (Lower Middle) | -180.00 | 4200.00 | 4020.00 | -1.0000 | 0.7761 |
| 100.00 | Current Market Price | -180.00 | 5000.00 | 4820.00 | -1.0000 | 0.9305 |
| 108.00 | Strike (Upper Middle) | -180.00 | 5800.00 | 5620.00 | -1.0000 | 1.0849 |
| 115.00 | Upside (15%) | 520.00 | 6500.00 | 7020.00 | 2.8889 | 1.3552 |
| 120.00 | Strike (Highest) | 1020.00 | 7000.00 | 8020.00 | 5.6667 | 1.5483 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1020.00 | -3980.00 | -0.3902 |
| breakeven_1 | Breakeven 1 | 39.80 | -60.20% | 1020.00 | -0.00 | -0.0000 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | 4020.00 | 0.7761 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | 4020.00 | 0.7761 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | 4020.00 | 0.7761 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | 4820.00 | 0.9305 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | 5620.00 | 1.0849 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 7020.00 | 1.3552 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 8020.00 | 1.5483 |
| infinity | Stock to Infinity | — | — | 1020.00 | 116020.00 | 11.3745 |

---

### Short Call Condor (ID=34) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 80.00 | 21.00 | 100 |
| 2 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 3 | CALL | Long 1 | 108.00 | 1.90 | 100 |
| 4 | CALL | Short 1 | 120.00 | 1.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [112.4]
- Options Max PnL: 1020.0
- Options Min PnL: -180.0
- Combined Max PnL: 19520.0
- Combined Min PnL: -10480.0

**Net Premium:**

- Per Share: -10.2
- Total: -1020.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$180.00 | -$10,480.00 |
| Risk Reward | 5.67x | 1.86x |
| Capital Basis | $5,200.00 | $16,700.00 |
| Cost Credit | Credit $1,020.00 | Credit $1,020.00 |
| Pop | 12.0% | 12.0% |
| Margin Proxy | 5200.0 | — |

**Probabilities:**

- PoP (raw): 0.119521
- Assignment Prob: 0.981981
- P(25% Max Profit): 0.232139
- P(50% Max Profit): 0.149004
- P(100% Max Profit): 0.054568
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | 1020.00 | -3500.00 | -2480.00 | 5.6667 | -0.2123 |
| 85.00 | Downside (15%) | 520.00 | -3000.00 | -2480.00 | 2.8889 | -0.2123 |
| 92.00 | Strike (Lower Middle) | -180.00 | -2300.00 | -2480.00 | -1.0000 | -0.2123 |
| 100.00 | Current Market Price | -180.00 | -1500.00 | -1680.00 | -1.0000 | -0.1438 |
| 108.00 | Strike (Upper Middle) | -180.00 | -700.00 | -880.00 | -1.0000 | -0.0753 |
| 112.40 | Breakeven 1 | 260.00 | -260.00 | 0.00 | 1.4444 | 0.0000 |
| 115.00 | Upside (15%) | 520.00 | 0.00 | 520.00 | 2.8889 | 0.0445 |
| 120.00 | Strike (Highest) | 1020.00 | 500.00 | 1520.00 | 5.6667 | 0.1301 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1020.00 | -10480.00 | -0.6275 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | -2480.00 | -0.2123 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | -2480.00 | -0.2123 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | -2480.00 | -0.2123 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | -1680.00 | -0.1438 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | -880.00 | -0.0753 |
| breakeven_1 | Breakeven 1 | 112.40 | 12.40% | 260.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 520.00 | 0.0445 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 1520.00 | 0.1301 |
| infinity | Stock to Infinity | — | — | 1020.00 | 109520.00 | 6.5581 |

---

### Short Put Condor (ID=35) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 80.00 | 1.00 | 100 |
| 2 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 3 | PUT | Long 1 | 108.00 | 9.90 | 100 |
| 4 | PUT | Short 1 | 120.00 | 21.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [90.2, 109.8]
- Options Max PnL: 1020.0
- Options Min PnL: -180.0
- Combined Max PnL: 1020.0
- Combined Min PnL: -180.0

**Net Premium:**

- Per Share: -10.2
- Total: -1020.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,020.00 | $1,020.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 5.67x | 5.67x |
| Capital Basis | $5,200.00 | $5,200.00 |
| Cost Credit | Credit $1,020.00 | Credit $1,020.00 |
| Pop | 34.4% | 34.4% |
| Margin Proxy | 5200.0 | — |

**Probabilities:**

- PoP (raw): 0.343859
- Assignment Prob: 0.964644
- P(25% Max Profit): 0.232139
- P(50% Max Profit): 0.149004
- P(100% Max Profit): 0.054568
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | 1020.00 | 0.00 | 1020.00 | 5.6667 | 5.6667 |
| 85.00 | Downside (15%) | 520.00 | 0.00 | 520.00 | 2.8889 | 2.8889 |
| 90.20 | Breakeven 1 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 92.00 | Strike (Lower Middle) | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 100.00 | Current Market Price | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 108.00 | Strike (Upper Middle) | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 109.80 | Breakeven 2 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 115.00 | Upside (15%) | 520.00 | 0.00 | 520.00 | 2.8889 | 2.8889 |
| 120.00 | Strike (Highest) | 1020.00 | 0.00 | 1020.00 | 5.6667 | 5.6667 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1020.00 | 1020.00 | 0.1962 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | 1020.00 | 5.6667 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | 520.00 | 2.8889 |
| breakeven_1 | Breakeven 1 | 90.20 | -9.80% | -0.00 | -0.00 | -0.0000 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | -180.00 | -1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | -180.00 | -1.0000 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | -180.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 109.80 | 9.80% | -0.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 520.00 | 2.8889 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 1020.00 | 5.6667 |
| infinity | Stock to Infinity | — | — | Unlimited | 1020.00 | 0.1962 |

---

### Short Put Condor (ID=35) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 80.00 | 1.00 | 100 |
| 2 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 3 | PUT | Long 1 | 108.00 | 9.90 | 100 |
| 4 | PUT | Short 1 | 120.00 | 21.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [101.8]
- Options Max PnL: 1020.0
- Options Min PnL: -180.0
- Combined Max PnL: 21020.0
- Combined Min PnL: -8980.0

**Net Premium:**

- Per Share: -10.2
- Total: -1020.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,020.00 | Unlimited |
| Max Loss | Unlimited | -$8,980.00 |
| Risk Reward | 5.67x | 2.34x |
| Capital Basis | $5,200.00 | $15,200.00 |
| Cost Credit | Credit $1,020.00 | Credit $1,020.00 |
| Pop | 41.1% | 41.1% |
| Margin Proxy | 5200.0 | — |

**Probabilities:**

- PoP (raw): 0.411497
- Assignment Prob: 0.964644
- P(25% Max Profit): 0.232139
- P(50% Max Profit): 0.149004
- P(100% Max Profit): 0.054568
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | 1020.00 | -2000.00 | -980.00 | 5.6667 | -0.0963 |
| 85.00 | Downside (15%) | 520.00 | -1500.00 | -980.00 | 2.8889 | -0.0963 |
| 92.00 | Strike (Lower Middle) | -180.00 | -800.00 | -980.00 | -1.0000 | -0.0963 |
| 100.00 | Current Market Price | -180.00 | 0.00 | -180.00 | -1.0000 | -0.0177 |
| 101.80 | Breakeven 1 | -180.00 | 180.00 | -0.00 | -1.0000 | -0.0000 |
| 108.00 | Strike (Upper Middle) | -180.00 | 800.00 | 620.00 | -1.0000 | 0.0609 |
| 115.00 | Upside (15%) | 520.00 | 1500.00 | 2020.00 | 2.8889 | 0.1984 |
| 120.00 | Strike (Highest) | 1020.00 | 2000.00 | 3020.00 | 5.6667 | 0.2967 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1020.00 | -8980.00 | -0.5908 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | -980.00 | -0.0963 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | -980.00 | -0.0963 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | -980.00 | -0.0963 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | -180.00 | -0.0177 |
| breakeven_1 | Breakeven 1 | 101.80 | 1.80% | -180.00 | -0.00 | -0.0000 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | 620.00 | 0.0609 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 2020.00 | 0.1984 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 3020.00 | 0.2967 |
| infinity | Stock to Infinity | — | — | Unlimited | 111020.00 | 7.3039 |

---

### Short Put Condor (ID=35) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 80.00 | 1.00 | 100 |
| 2 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 3 | PUT | Long 1 | 108.00 | 9.90 | 100 |
| 4 | PUT | Short 1 | 120.00 | 21.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [39.8]
- Options Max PnL: 1020.0
- Options Min PnL: -180.0
- Combined Max PnL: 26020.0
- Combined Min PnL: -3980.0

**Net Premium:**

- Per Share: -10.2
- Total: -1020.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,020.00 | Unlimited |
| Max Loss | Unlimited | -$3,980.00 |
| Risk Reward | 5.67x | 6.54x |
| Capital Basis | $5,200.00 | $10,200.00 |
| Cost Credit | Credit $1,020.00 | Credit $1,020.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 5200.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.964644
- P(25% Max Profit): 0.232139
- P(50% Max Profit): 0.149004
- P(100% Max Profit): 0.054568
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 39.80 | Breakeven 1 | 1020.00 | -1020.00 | -0.00 | 5.6667 | -0.0000 |
| 50.00 | Scenario @ 50.00 | 1020.00 | 0.00 | 1020.00 | 5.6667 | 0.1969 |
| 80.00 | Strike (Lowest) | 1020.00 | 3000.00 | 4020.00 | 5.6667 | 0.7761 |
| 85.00 | Downside (15%) | 520.00 | 3500.00 | 4020.00 | 2.8889 | 0.7761 |
| 92.00 | Strike (Lower Middle) | -180.00 | 4200.00 | 4020.00 | -1.0000 | 0.7761 |
| 100.00 | Current Market Price | -180.00 | 5000.00 | 4820.00 | -1.0000 | 0.9305 |
| 108.00 | Strike (Upper Middle) | -180.00 | 5800.00 | 5620.00 | -1.0000 | 1.0849 |
| 115.00 | Upside (15%) | 520.00 | 6500.00 | 7020.00 | 2.8889 | 1.3552 |
| 120.00 | Strike (Highest) | 1020.00 | 7000.00 | 8020.00 | 5.6667 | 1.5483 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1020.00 | -3980.00 | -0.3902 |
| breakeven_1 | Breakeven 1 | 39.80 | -60.20% | 1020.00 | -0.00 | -0.0000 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | 4020.00 | 0.7761 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | 4020.00 | 0.7761 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | 4020.00 | 0.7761 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | 4820.00 | 0.9305 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | 5620.00 | 1.0849 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 7020.00 | 1.3552 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 8020.00 | 1.5483 |
| infinity | Stock to Infinity | — | — | Unlimited | 116020.00 | 11.3745 |

---

### Short Put Condor (ID=35) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 80.00 | 1.00 | 100 |
| 2 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 3 | PUT | Long 1 | 108.00 | 9.90 | 100 |
| 4 | PUT | Short 1 | 120.00 | 21.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [112.4]
- Options Max PnL: 1020.0
- Options Min PnL: -180.0
- Combined Max PnL: 19520.0
- Combined Min PnL: -10480.0

**Net Premium:**

- Per Share: -10.2
- Total: -1020.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,020.00 | Unlimited |
| Max Loss | Unlimited | -$10,480.00 |
| Risk Reward | 5.67x | 1.86x |
| Capital Basis | $5,200.00 | $16,700.00 |
| Cost Credit | Credit $1,020.00 | Credit $1,020.00 |
| Pop | 12.0% | 12.0% |
| Margin Proxy | 5200.0 | — |

**Probabilities:**

- PoP (raw): 0.119521
- Assignment Prob: 0.964644
- P(25% Max Profit): 0.232139
- P(50% Max Profit): 0.149004
- P(100% Max Profit): 0.054568
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | 1020.00 | -3500.00 | -2480.00 | 5.6667 | -0.2123 |
| 85.00 | Downside (15%) | 520.00 | -3000.00 | -2480.00 | 2.8889 | -0.2123 |
| 92.00 | Strike (Lower Middle) | -180.00 | -2300.00 | -2480.00 | -1.0000 | -0.2123 |
| 100.00 | Current Market Price | -180.00 | -1500.00 | -1680.00 | -1.0000 | -0.1438 |
| 108.00 | Strike (Upper Middle) | -180.00 | -700.00 | -880.00 | -1.0000 | -0.0753 |
| 112.40 | Breakeven 1 | 260.00 | -260.00 | 0.00 | 1.4444 | 0.0000 |
| 115.00 | Upside (15%) | 520.00 | 0.00 | 520.00 | 2.8889 | 0.0445 |
| 120.00 | Strike (Highest) | 1020.00 | 500.00 | 1520.00 | 5.6667 | 0.1301 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1020.00 | -10480.00 | -0.6275 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | -2480.00 | -0.2123 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | -2480.00 | -0.2123 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | -2480.00 | -0.2123 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | -1680.00 | -0.1438 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | -880.00 | -0.0753 |
| breakeven_1 | Breakeven 1 | 112.40 | 12.40% | 260.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 520.00 | 0.0445 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 1520.00 | 0.1301 |
| infinity | Stock to Infinity | — | — | Unlimited | 109520.00 | 6.5581 |

---

### Rev Iron Condor (ID=36) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 80.00 | 1.00 | 100 |
| 2 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 3 | CALL | Long 1 | 108.00 | 1.90 | 100 |
| 4 | CALL | Short 1 | 120.00 | 1.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [90.2, 109.8]
- Options Max PnL: 1020.0
- Options Min PnL: -180.0
- Combined Max PnL: 1020.0
- Combined Min PnL: -180.0

**Net Premium:**

- Per Share: 1.8
- Total: 180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 5.67x | 5.67x |
| Capital Basis | $2,200.00 | $2,200.00 |
| Cost Credit | Debit $180.00 | Debit $180.00 |
| Pop | 34.4% | 34.4% |
| Margin Proxy | 2200.0 | — |

**Probabilities:**

- PoP (raw): 0.343859
- Assignment Prob: 0.053375
- P(25% Max Profit): 0.232139
- P(50% Max Profit): 0.149004
- P(100% Max Profit): 0.054568
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | 1020.00 | 0.00 | 1020.00 | 5.6667 | 5.6667 |
| 85.00 | Downside (15%) | 520.00 | 0.00 | 520.00 | 2.8889 | 2.8889 |
| 90.20 | Breakeven 1 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 92.00 | Strike (Lower Middle) | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 100.00 | Current Market Price | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 108.00 | Strike (Upper Middle) | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 109.80 | Breakeven 2 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 115.00 | Upside (15%) | 520.00 | 0.00 | 520.00 | 2.8889 | 2.8889 |
| 120.00 | Strike (Highest) | 1020.00 | 0.00 | 1020.00 | 5.6667 | 5.6667 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1020.00 | 1020.00 | 0.4636 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | 1020.00 | 5.6667 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | 520.00 | 2.8889 |
| breakeven_1 | Breakeven 1 | 90.20 | -9.80% | -0.00 | -0.00 | -0.0000 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | -180.00 | -1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | -180.00 | -1.0000 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | -180.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 109.80 | 9.80% | -0.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 520.00 | 2.8889 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 1020.00 | 5.6667 |
| infinity | Stock to Infinity | — | — | Unlimited | 1020.00 | 0.4636 |

---

### Rev Iron Condor (ID=36) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 80.00 | 1.00 | 100 |
| 2 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 3 | CALL | Long 1 | 108.00 | 1.90 | 100 |
| 4 | CALL | Short 1 | 120.00 | 1.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [101.8]
- Options Max PnL: 1020.0
- Options Min PnL: -180.0
- Combined Max PnL: 21020.0
- Combined Min PnL: -8980.0

**Net Premium:**

- Per Share: 1.8
- Total: 180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | -$8,980.00 |
| Risk Reward | 5.67x | 2.34x |
| Capital Basis | $2,200.00 | $12,200.00 |
| Cost Credit | Debit $180.00 | Debit $180.00 |
| Pop | 41.1% | 41.1% |
| Margin Proxy | 2200.0 | — |

**Probabilities:**

- PoP (raw): 0.411497
- Assignment Prob: 0.053375
- P(25% Max Profit): 0.232139
- P(50% Max Profit): 0.149004
- P(100% Max Profit): 0.054568
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | 1020.00 | -2000.00 | -980.00 | 5.6667 | -0.0963 |
| 85.00 | Downside (15%) | 520.00 | -1500.00 | -980.00 | 2.8889 | -0.0963 |
| 92.00 | Strike (Lower Middle) | -180.00 | -800.00 | -980.00 | -1.0000 | -0.0963 |
| 100.00 | Current Market Price | -180.00 | 0.00 | -180.00 | -1.0000 | -0.0177 |
| 101.80 | Breakeven 1 | -180.00 | 180.00 | -0.00 | -1.0000 | -0.0000 |
| 108.00 | Strike (Upper Middle) | -180.00 | 800.00 | 620.00 | -1.0000 | 0.0609 |
| 115.00 | Upside (15%) | 520.00 | 1500.00 | 2020.00 | 2.8889 | 0.1984 |
| 120.00 | Strike (Highest) | 1020.00 | 2000.00 | 3020.00 | 5.6667 | 0.2967 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1020.00 | -8980.00 | -0.7361 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | -980.00 | -0.0963 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | -980.00 | -0.0963 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | -980.00 | -0.0963 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | -180.00 | -0.0177 |
| breakeven_1 | Breakeven 1 | 101.80 | 1.80% | -180.00 | -0.00 | -0.0000 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | 620.00 | 0.0609 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 2020.00 | 0.1984 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 3020.00 | 0.2967 |
| infinity | Stock to Infinity | — | — | Unlimited | 111020.00 | 9.1000 |

---

### Rev Iron Condor (ID=36) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 80.00 | 1.00 | 100 |
| 2 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 3 | CALL | Long 1 | 108.00 | 1.90 | 100 |
| 4 | CALL | Short 1 | 120.00 | 1.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [39.8]
- Options Max PnL: 1020.0
- Options Min PnL: -180.0
- Combined Max PnL: 26020.0
- Combined Min PnL: -3980.0

**Net Premium:**

- Per Share: 1.8
- Total: 180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | -$3,980.00 |
| Risk Reward | 5.67x | 6.54x |
| Capital Basis | $2,200.00 | $7,200.00 |
| Cost Credit | Debit $180.00 | Debit $180.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 2200.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.053375
- P(25% Max Profit): 0.232139
- P(50% Max Profit): 0.149004
- P(100% Max Profit): 0.054568
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 39.80 | Breakeven 1 | 1020.00 | -1020.00 | -0.00 | 5.6667 | -0.0000 |
| 50.00 | Scenario @ 50.00 | 1020.00 | 0.00 | 1020.00 | 5.6667 | 0.1969 |
| 80.00 | Strike (Lowest) | 1020.00 | 3000.00 | 4020.00 | 5.6667 | 0.7761 |
| 85.00 | Downside (15%) | 520.00 | 3500.00 | 4020.00 | 2.8889 | 0.7761 |
| 92.00 | Strike (Lower Middle) | -180.00 | 4200.00 | 4020.00 | -1.0000 | 0.7761 |
| 100.00 | Current Market Price | -180.00 | 5000.00 | 4820.00 | -1.0000 | 0.9305 |
| 108.00 | Strike (Upper Middle) | -180.00 | 5800.00 | 5620.00 | -1.0000 | 1.0849 |
| 115.00 | Upside (15%) | 520.00 | 6500.00 | 7020.00 | 2.8889 | 1.3552 |
| 120.00 | Strike (Highest) | 1020.00 | 7000.00 | 8020.00 | 5.6667 | 1.5483 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1020.00 | -3980.00 | -0.5528 |
| breakeven_1 | Breakeven 1 | 39.80 | -60.20% | 1020.00 | -0.00 | -0.0000 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | 4020.00 | 0.7761 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | 4020.00 | 0.7761 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | 4020.00 | 0.7761 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | 4820.00 | 0.9305 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | 5620.00 | 1.0849 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 7020.00 | 1.3552 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 8020.00 | 1.5483 |
| infinity | Stock to Infinity | — | — | Unlimited | 116020.00 | 16.1139 |

---

### Rev Iron Condor (ID=36) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 80.00 | 1.00 | 100 |
| 2 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 3 | CALL | Long 1 | 108.00 | 1.90 | 100 |
| 4 | CALL | Short 1 | 120.00 | 1.00 | 100 |

**Payoff:**

- Grid Size: 304 points
- Strikes: [80.0, 92.0, 108.0, 120.0]
- Breakevens: [112.4]
- Options Max PnL: 1020.0
- Options Min PnL: -180.0
- Combined Max PnL: 19520.0
- Combined Min PnL: -10480.0

**Net Premium:**

- Per Share: 1.8
- Total: 180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | -$10,480.00 |
| Risk Reward | 5.67x | 1.86x |
| Capital Basis | $2,200.00 | $13,700.00 |
| Cost Credit | Debit $180.00 | Debit $180.00 |
| Pop | 12.0% | 12.0% |
| Margin Proxy | 2200.0 | — |

**Probabilities:**

- PoP (raw): 0.119521
- Assignment Prob: 0.053375
- P(25% Max Profit): 0.232139
- P(50% Max Profit): 0.149004
- P(100% Max Profit): 0.054568
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Strike (Lowest) | 1020.00 | -3500.00 | -2480.00 | 5.6667 | -0.2123 |
| 85.00 | Downside (15%) | 520.00 | -3000.00 | -2480.00 | 2.8889 | -0.2123 |
| 92.00 | Strike (Lower Middle) | -180.00 | -2300.00 | -2480.00 | -1.0000 | -0.2123 |
| 100.00 | Current Market Price | -180.00 | -1500.00 | -1680.00 | -1.0000 | -0.1438 |
| 108.00 | Strike (Upper Middle) | -180.00 | -700.00 | -880.00 | -1.0000 | -0.0753 |
| 112.40 | Breakeven 1 | 260.00 | -260.00 | 0.00 | 1.4444 | 0.0000 |
| 115.00 | Upside (15%) | 520.00 | 0.00 | 520.00 | 2.8889 | 0.0445 |
| 120.00 | Strike (Highest) | 1020.00 | 500.00 | 1520.00 | 5.6667 | 0.1301 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1020.00 | -10480.00 | -0.7650 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | -2480.00 | -0.2123 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | -2480.00 | -0.2123 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | -2480.00 | -0.2123 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | -1680.00 | -0.1438 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | -880.00 | -0.0753 |
| breakeven_1 | Breakeven 1 | 112.40 | 12.40% | 260.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 520.00 | 0.0445 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 1520.00 | 0.1301 |
| infinity | Stock to Infinity | — | — | Unlimited | 109520.00 | 7.9942 |

---

### Long Straddle (ID=37) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [95.0, 105.0]
- Options Max PnL: 19500.0
- Options Min PnL: -500.0
- Combined Max PnL: 19500.0
- Combined Min PnL: -500.0

**Net Premium:**

- Per Share: 5.0
- Total: 500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 39.00x | 39.00x |
| Capital Basis | $500.00 | $500.00 |
| Cost Credit | Debit $500.00 | Debit $500.00 |
| Pop | 63.0% | 63.0% |
| Margin Proxy | 500.0 | — |

**Probabilities:**

- PoP (raw): 0.630219
- Assignment Prob: 0.0
- P(25% Max Profit): 1.4e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1000.00 | 0.00 | 1000.00 | 2.0000 | 2.0000 |
| 95.00 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | -500.00 | 0.00 | -500.00 | -1.0000 | -1.0000 |
| 105.00 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 1000.00 | 0.00 | 1000.00 | 2.0000 | 2.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9500.00 | 9500.00 | 19.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1000.00 | 1000.00 | 2.0000 |
| breakeven_1 | Breakeven 1 | 95.00 | -5.00% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -500.00 | -500.00 | -1.0000 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -500.00 | -500.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 105.00 | 5.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1000.00 | 1000.00 | 2.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | 89500.00 | 179.0000 |

---

### Long Straddle (ID=37) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [102.5]
- Options Max PnL: 19500.0
- Options Min PnL: -500.0
- Combined Max PnL: 39500.0
- Combined Min PnL: -500.0

**Net Premium:**

- Per Share: 5.0
- Total: 500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | -$500.00 |
| Risk Reward | 39.00x | 79.00x |
| Capital Basis | $500.00 | $10,500.00 |
| Cost Credit | Debit $500.00 | Debit $500.00 |
| Pop | 38.6% | 38.6% |
| Margin Proxy | 500.0 | — |

**Probabilities:**

- PoP (raw): 0.386034
- Assignment Prob: 0.0
- P(25% Max Profit): 1.4e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1000.00 | -1500.00 | -500.00 | 2.0000 | -0.0476 |
| 100.00 | Current Market Price | -500.00 | 0.00 | -500.00 | -1.0000 | -0.0476 |
| 102.50 | Breakeven 1 | -250.00 | 250.00 | 0.00 | -0.5000 | 0.0000 |
| 115.00 | Upside (15%) | 1000.00 | 1500.00 | 2500.00 | 2.0000 | 0.2381 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9500.00 | -500.00 | -0.0476 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1000.00 | -500.00 | -0.0476 |
| spot | Current Market Price | 100.00 | 0.00% | -500.00 | -500.00 | -0.0476 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -500.00 | -500.00 | -0.0476 |
| breakeven_1 | Breakeven 1 | 102.50 | 2.50% | -250.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1000.00 | 2500.00 | 0.2381 |
| infinity | Stock to Infinity | — | — | Unlimited | 179500.00 | 17.0952 |

---

### Long Straddle (ID=37) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: []
- Options Max PnL: 19500.0
- Options Min PnL: -500.0
- Combined Max PnL: 44500.0
- Combined Min PnL: 4500.0

**Net Premium:**

- Per Share: 5.0
- Total: 500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | $4,500.00 |
| Risk Reward | 39.00x | 9.89x |
| Capital Basis | $500.00 | $5,500.00 |
| Cost Credit | Debit $500.00 | Debit $500.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 500.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.0
- P(25% Max Profit): 1.4e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | 4500.00 | 0.00 | 4500.00 | 9.0000 | 0.8182 |
| 85.00 | Downside (15%) | 1000.00 | 3500.00 | 4500.00 | 2.0000 | 0.8182 |
| 100.00 | Current Market Price | -500.00 | 5000.00 | 4500.00 | -1.0000 | 0.8182 |
| 115.00 | Upside (15%) | 1000.00 | 6500.00 | 7500.00 | 2.0000 | 1.3636 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9500.00 | 4500.00 | 0.8182 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1000.00 | 4500.00 | 0.8182 |
| spot | Current Market Price | 100.00 | 0.00% | -500.00 | 4500.00 | 0.8182 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -500.00 | 4500.00 | 0.8182 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1000.00 | 7500.00 | 1.3636 |
| infinity | Stock to Infinity | — | — | Unlimited | 184500.00 | 33.5455 |

---

### Long Straddle (ID=37) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [110.0]
- Options Max PnL: 19500.0
- Options Min PnL: -500.0
- Combined Max PnL: 38000.0
- Combined Min PnL: -2000.0

**Net Premium:**

- Per Share: 5.0
- Total: 500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | -$2,000.00 |
| Risk Reward | 39.00x | 19.00x |
| Capital Basis | $500.00 | $12,000.00 |
| Cost Credit | Debit $500.00 | Debit $500.00 |
| Pop | 16.6% | 16.6% |
| Margin Proxy | 500.0 | — |

**Probabilities:**

- PoP (raw): 0.166128
- Assignment Prob: 0.0
- P(25% Max Profit): 1.4e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1000.00 | -3000.00 | -2000.00 | 2.0000 | -0.1667 |
| 100.00 | Current Market Price | -500.00 | -1500.00 | -2000.00 | -1.0000 | -0.1667 |
| 110.00 | Breakeven 1 | 500.00 | -500.00 | 0.00 | 1.0000 | 0.0000 |
| 115.00 | Upside (15%) | 1000.00 | 0.00 | 1000.00 | 2.0000 | 0.0833 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9500.00 | -2000.00 | -0.1667 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1000.00 | -2000.00 | -0.1667 |
| spot | Current Market Price | 100.00 | 0.00% | -500.00 | -2000.00 | -0.1667 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -500.00 | -2000.00 | -0.1667 |
| breakeven_1 | Breakeven 1 | 110.00 | 10.00% | 500.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1000.00 | 1000.00 | 0.0833 |
| infinity | Stock to Infinity | — | — | Unlimited | 178000.00 | 14.8333 |

---

### Short Straddle (ID=38) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_PUT_CALL

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [95.0, 105.0]
- Options Max PnL: 500.0
- Options Min PnL: -19500.0
- Combined Max PnL: 500.0
- Combined Min PnL: -19500.0

**Net Premium:**

- Per Share: -5.0
- Total: -500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $500.00 | $500.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.03x | 0.03x |
| Capital Basis | $4,500.00 | $4,500.00 |
| Cost Credit | Credit $500.00 | Credit $500.00 |
| Pop | 37.0% | 37.0% |
| Margin Proxy | 4500.0 | — |

**Probabilities:**

- PoP (raw): 0.369781
- Assignment Prob: 1.0
- P(25% Max Profit): 0.281789
- P(50% Max Profit): 0.190029
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1000.00 | 0.00 | -1000.00 | -0.2222 | -0.2222 |
| 95.00 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | 500.00 | 0.00 | 500.00 | 0.1111 | 0.1111 |
| 105.00 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -1000.00 | 0.00 | -1000.00 | -0.2222 | -0.2222 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9500.00 | -9500.00 | -2.1111 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1000.00 | -1000.00 | -0.2222 |
| breakeven_1 | Breakeven 1 | 95.00 | -5.00% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 500.00 | 500.00 | 0.1111 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 500.00 | 500.00 | 0.1111 |
| breakeven_2 | Breakeven 2 | 105.00 | 5.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1000.00 | -1000.00 | -0.2222 |
| infinity | Stock to Infinity | — | — | Unlimited | -89500.00 | -19.8889 |

---

### Short Straddle (ID=38) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [97.5]
- Options Max PnL: 500.0
- Options Min PnL: -19500.0
- Combined Max PnL: 500.0
- Combined Min PnL: -19500.0

**Net Premium:**

- Per Share: -5.0
- Total: -500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $500.00 | $500.00 |
| Max Loss | Unlimited | -$19,500.00 |
| Risk Reward | 0.03x | 0.03x |
| Capital Basis | $19,500.00 | $29,500.00 |
| Cost Credit | Credit $500.00 | Credit $500.00 |
| Pop | 57.6% | 57.6% |
| Margin Proxy | 19500.0 | — |

**Probabilities:**

- PoP (raw): 0.576062
- Assignment Prob: 1.0
- P(25% Max Profit): 0.281789
- P(50% Max Profit): 0.190029
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1000.00 | -1500.00 | -2500.00 | -0.0513 | -0.0847 |
| 97.50 | Breakeven 1 | 250.00 | -250.00 | 0.00 | 0.0128 | 0.0000 |
| 100.00 | Current Market Price | 500.00 | 0.00 | 500.00 | 0.0256 | 0.0169 |
| 115.00 | Upside (15%) | -1000.00 | 1500.00 | 500.00 | -0.0513 | 0.0169 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9500.00 | -19500.00 | -0.6610 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1000.00 | -2500.00 | -0.0847 |
| breakeven_1 | Breakeven 1 | 97.50 | -2.50% | 250.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 500.00 | 500.00 | 0.0169 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 500.00 | 500.00 | 0.0169 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1000.00 | 500.00 | 0.0169 |
| infinity | Stock to Infinity | — | — | Unlimited | 500.00 | 0.0169 |

---

### Short Straddle (ID=38) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [72.5]
- Options Max PnL: 500.0
- Options Min PnL: -19500.0
- Combined Max PnL: 5500.0
- Combined Min PnL: -14500.0

**Net Premium:**

- Per Share: -5.0
- Total: -500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $500.00 | $5,500.00 |
| Max Loss | Unlimited | -$14,500.00 |
| Risk Reward | 0.03x | 0.38x |
| Capital Basis | $19,500.00 | $24,500.00 |
| Cost Credit | Credit $500.00 | Credit $500.00 |
| Pop | 99.9% | 99.9% |
| Margin Proxy | 19500.0 | — |

**Probabilities:**

- PoP (raw): 0.998834
- Assignment Prob: 1.0
- P(25% Max Profit): 0.281789
- P(50% Max Profit): 0.190029
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -4500.00 | 0.00 | -4500.00 | -0.2308 | -0.1837 |
| 72.50 | Breakeven 1 | -2250.00 | 2250.00 | 0.00 | -0.1154 | 0.0000 |
| 85.00 | Downside (15%) | -1000.00 | 3500.00 | 2500.00 | -0.0513 | 0.1020 |
| 100.00 | Current Market Price | 500.00 | 5000.00 | 5500.00 | 0.0256 | 0.2245 |
| 115.00 | Upside (15%) | -1000.00 | 6500.00 | 5500.00 | -0.0513 | 0.2245 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9500.00 | -14500.00 | -0.5918 |
| breakeven_1 | Breakeven 1 | 72.50 | -27.50% | -2250.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1000.00 | 2500.00 | 0.1020 |
| spot | Current Market Price | 100.00 | 0.00% | 500.00 | 5500.00 | 0.2245 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 500.00 | 5500.00 | 0.2245 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1000.00 | 5500.00 | 0.2245 |
| infinity | Stock to Infinity | — | — | Unlimited | 5500.00 | 0.2245 |

---

### Short Straddle (ID=38) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: []
- Options Max PnL: 500.0
- Options Min PnL: -19500.0
- Combined Max PnL: -1000.0
- Combined Min PnL: -21000.0

**Net Premium:**

- Per Share: -5.0
- Total: -500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $500.00 | -$1,000.00 |
| Max Loss | Unlimited | -$21,000.00 |
| Risk Reward | 0.03x | 0.05x |
| Capital Basis | $19,500.00 | $31,000.00 |
| Cost Credit | Credit $500.00 | Credit $500.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 19500.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 1.0
- P(25% Max Profit): 0.281789
- P(50% Max Profit): 0.190029
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1000.00 | -3000.00 | -4000.00 | -0.0513 | -0.1290 |
| 100.00 | Current Market Price | 500.00 | -1500.00 | -1000.00 | 0.0256 | -0.0323 |
| 115.00 | Upside (15%) | -1000.00 | 0.00 | -1000.00 | -0.0513 | -0.0323 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9500.00 | -21000.00 | -0.6774 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1000.00 | -4000.00 | -0.1290 |
| spot | Current Market Price | 100.00 | 0.00% | 500.00 | -1000.00 | -0.0323 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 500.00 | -1000.00 | -0.0323 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1000.00 | -1000.00 | -0.0323 |
| infinity | Stock to Infinity | — | — | Unlimited | -1000.00 | -0.0323 |

---

### Long Strangle (ID=39) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [88.2, 111.8]
- Options Max PnL: 18820.0
- Options Min PnL: -380.0
- Combined Max PnL: 18820.0
- Combined Min PnL: -380.0

**Net Premium:**

- Per Share: 3.8
- Total: 380.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 49.53x | 49.53x |
| Capital Basis | $380.00 | $380.00 |
| Cost Credit | Debit $380.00 | Debit $380.00 |
| Pop | 25.4% | 25.4% |
| Margin Proxy | 380.0 | — |

**Probabilities:**

- PoP (raw): 0.253752
- Assignment Prob: 0.0
- P(25% Max Profit): 3e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 320.00 | 0.00 | 320.00 | 0.8421 | 0.8421 |
| 88.20 | Breakeven 1 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 92.00 | Lower Strike | -380.00 | 0.00 | -380.00 | -1.0000 | -1.0000 |
| 100.00 | Current Market Price | -380.00 | 0.00 | -380.00 | -1.0000 | -1.0000 |
| 108.00 | Upper Strike | -380.00 | 0.00 | -380.00 | -1.0000 | -1.0000 |
| 111.80 | Breakeven 2 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 115.00 | Upside (15%) | 320.00 | 0.00 | 320.00 | 0.8421 | 0.8421 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8820.00 | 8820.00 | 23.2105 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 320.00 | 320.00 | 0.8421 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | -0.00 | -0.00 | -0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -380.00 | -380.00 | -1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -380.00 | -1.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -380.00 | -380.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | -0.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 320.00 | 320.00 | 0.8421 |
| infinity | Stock to Infinity | — | — | Unlimited | 96820.00 | 254.7895 |

---

### Long Strangle (ID=39) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [103.8]
- Options Max PnL: 18820.0
- Options Min PnL: -380.0
- Combined Max PnL: 38820.0
- Combined Min PnL: -1180.0

**Net Premium:**

- Per Share: 3.8
- Total: 380.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 49.53x | 32.90x |
| Capital Basis | $380.00 | $10,380.00 |
| Cost Credit | Debit $380.00 | Debit $380.00 |
| Pop | 34.1% | 34.1% |
| Margin Proxy | 380.0 | — |

**Probabilities:**

- PoP (raw): 0.34053
- Assignment Prob: 0.0
- P(25% Max Profit): 3e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 320.00 | -1500.00 | -1180.00 | 0.8421 | -0.1137 |
| 92.00 | Lower Strike | -380.00 | -800.00 | -1180.00 | -1.0000 | -0.1137 |
| 100.00 | Current Market Price | -380.00 | 0.00 | -380.00 | -1.0000 | -0.0366 |
| 103.80 | Breakeven 1 | -380.00 | 380.00 | -0.00 | -1.0000 | -0.0000 |
| 108.00 | Upper Strike | -380.00 | 800.00 | 420.00 | -1.0000 | 0.0405 |
| 115.00 | Upside (15%) | 320.00 | 1500.00 | 1820.00 | 0.8421 | 0.1753 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8820.00 | -1180.00 | -0.1137 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 320.00 | -1180.00 | -0.1137 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -380.00 | -1180.00 | -0.1137 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -380.00 | -0.0366 |
| breakeven_1 | Breakeven 1 | 103.80 | 3.80% | -380.00 | -0.00 | -0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -380.00 | 420.00 | 0.0405 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 320.00 | 1820.00 | 0.1753 |
| infinity | Stock to Infinity | — | — | Unlimited | 194820.00 | 18.7688 |

---

### Long Strangle (ID=39) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: []
- Options Max PnL: 18820.0
- Options Min PnL: -380.0
- Combined Max PnL: 43820.0
- Combined Min PnL: 3820.0

**Net Premium:**

- Per Share: 3.8
- Total: 380.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 49.53x | 11.47x |
| Capital Basis | $380.00 | $5,380.00 |
| Cost Credit | Debit $380.00 | Debit $380.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 380.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.0
- P(25% Max Profit): 3e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | 3820.00 | 0.00 | 3820.00 | 10.0526 | 0.7100 |
| 85.00 | Downside (15%) | 320.00 | 3500.00 | 3820.00 | 0.8421 | 0.7100 |
| 92.00 | Lower Strike | -380.00 | 4200.00 | 3820.00 | -1.0000 | 0.7100 |
| 100.00 | Current Market Price | -380.00 | 5000.00 | 4620.00 | -1.0000 | 0.8587 |
| 108.00 | Upper Strike | -380.00 | 5800.00 | 5420.00 | -1.0000 | 1.0074 |
| 115.00 | Upside (15%) | 320.00 | 6500.00 | 6820.00 | 0.8421 | 1.2677 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8820.00 | 3820.00 | 0.7100 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 320.00 | 3820.00 | 0.7100 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -380.00 | 3820.00 | 0.7100 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | 4620.00 | 0.8587 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -380.00 | 5420.00 | 1.0074 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 320.00 | 6820.00 | 1.2677 |
| infinity | Stock to Infinity | — | — | Unlimited | 199820.00 | 37.1413 |

---

### Long Strangle (ID=39) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [113.4]
- Options Max PnL: 18820.0
- Options Min PnL: -380.0
- Combined Max PnL: 37320.0
- Combined Min PnL: -2680.0

**Net Premium:**

- Per Share: 3.8
- Total: 380.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 49.53x | 13.93x |
| Capital Basis | $380.00 | $11,880.00 |
| Cost Credit | Debit $380.00 | Debit $380.00 |
| Pop | 10.3% | 10.3% |
| Margin Proxy | 380.0 | — |

**Probabilities:**

- PoP (raw): 0.103354
- Assignment Prob: 0.0
- P(25% Max Profit): 3e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 320.00 | -3000.00 | -2680.00 | 0.8421 | -0.2256 |
| 92.00 | Lower Strike | -380.00 | -2300.00 | -2680.00 | -1.0000 | -0.2256 |
| 100.00 | Current Market Price | -380.00 | -1500.00 | -1880.00 | -1.0000 | -0.1582 |
| 108.00 | Upper Strike | -380.00 | -700.00 | -1080.00 | -1.0000 | -0.0909 |
| 113.40 | Breakeven 1 | 160.00 | -160.00 | 0.00 | 0.4211 | 0.0000 |
| 115.00 | Upside (15%) | 320.00 | 0.00 | 320.00 | 0.8421 | 0.0269 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8820.00 | -2680.00 | -0.2256 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 320.00 | -2680.00 | -0.2256 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -380.00 | -2680.00 | -0.2256 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -1880.00 | -0.1582 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -380.00 | -1080.00 | -0.0909 |
| breakeven_1 | Breakeven 1 | 113.40 | 13.40% | 160.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 320.00 | 320.00 | 0.0269 |
| infinity | Stock to Infinity | — | — | Unlimited | 193320.00 | 16.2727 |

---

### Short Strangle (ID=40) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_PUT_CALL

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [88.2, 111.8]
- Options Max PnL: 380.0
- Options Min PnL: -18820.0
- Combined Max PnL: 380.0
- Combined Min PnL: -18820.0

**Net Premium:**

- Per Share: -3.8
- Total: -380.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $380.00 | $380.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.02x | 0.02x |
| Capital Basis | $2,780.00 | $2,780.00 |
| Cost Credit | Credit $380.00 | Credit $380.00 |
| Pop | 74.6% | 74.6% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.746248
- Assignment Prob: 0.440281
- P(25% Max Profit): 0.705708
- P(50% Max Profit): 0.661077
- P(100% Max Profit): 0.5619
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -320.00 | 0.00 | -320.00 | -0.1151 | -0.1151 |
| 88.20 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 92.00 | Lower Strike | 380.00 | 0.00 | 380.00 | 0.1367 | 0.1367 |
| 100.00 | Current Market Price | 380.00 | 0.00 | 380.00 | 0.1367 | 0.1367 |
| 108.00 | Upper Strike | 380.00 | 0.00 | 380.00 | 0.1367 | 0.1367 |
| 111.80 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -320.00 | 0.00 | -320.00 | -0.1151 | -0.1151 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -8820.00 | -3.1727 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | -320.00 | -0.1151 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | 0.00 | 0.00 | 0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | 380.00 | 0.1367 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 380.00 | 0.1367 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | 380.00 | 0.1367 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | -320.00 | -0.1151 |
| infinity | Stock to Infinity | — | — | Unlimited | -96820.00 | -34.8273 |

---

### Short Strangle (ID=40) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [96.2]
- Options Max PnL: 380.0
- Options Min PnL: -18820.0
- Combined Max PnL: 1180.0
- Combined Min PnL: -18820.0

**Net Premium:**

- Per Share: -3.8
- Total: -380.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $380.00 | $1,180.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.02x | 0.06x |
| Capital Basis | $2,780.00 | $12,780.00 |
| Cost Credit | Credit $380.00 | Credit $380.00 |
| Pop | 62.6% | 62.6% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.62592
- Assignment Prob: 0.440281
- P(25% Max Profit): 0.705708
- P(50% Max Profit): 0.661077
- P(100% Max Profit): 0.5619
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -320.00 | -1500.00 | -1820.00 | -0.1151 | -0.1424 |
| 92.00 | Lower Strike | 380.00 | -800.00 | -420.00 | 0.1367 | -0.0329 |
| 96.20 | Breakeven 1 | 380.00 | -380.00 | 0.00 | 0.1367 | 0.0000 |
| 100.00 | Current Market Price | 380.00 | 0.00 | 380.00 | 0.1367 | 0.0297 |
| 108.00 | Upper Strike | 380.00 | 800.00 | 1180.00 | 0.1367 | 0.0923 |
| 115.00 | Upside (15%) | -320.00 | 1500.00 | 1180.00 | -0.1151 | 0.0923 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -18820.00 | -1.4726 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | -1820.00 | -0.1424 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | -420.00 | -0.0329 |
| breakeven_1 | Breakeven 1 | 96.20 | -3.80% | 380.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 380.00 | 0.0297 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | 1180.00 | 0.0923 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | 1180.00 | 0.0923 |
| infinity | Stock to Infinity | — | — | Unlimited | 1180.00 | 0.0923 |

---

### Short Strangle (ID=40) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [69.1]
- Options Max PnL: 380.0
- Options Min PnL: -18820.0
- Combined Max PnL: 6180.0
- Combined Min PnL: -13820.0

**Net Premium:**

- Per Share: -3.8
- Total: -380.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $380.00 | $6,180.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.02x | 0.45x |
| Capital Basis | $2,780.00 | $7,780.00 |
| Cost Credit | Credit $380.00 | Credit $380.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.999773
- Assignment Prob: 0.440281
- P(25% Max Profit): 0.705708
- P(50% Max Profit): 0.661077
- P(100% Max Profit): 0.5619
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -3820.00 | 0.00 | -3820.00 | -1.3741 | -0.4910 |
| 69.10 | Breakeven 1 | -1910.00 | 1910.00 | -0.00 | -0.6871 | -0.0000 |
| 85.00 | Downside (15%) | -320.00 | 3500.00 | 3180.00 | -0.1151 | 0.4087 |
| 92.00 | Lower Strike | 380.00 | 4200.00 | 4580.00 | 0.1367 | 0.5887 |
| 100.00 | Current Market Price | 380.00 | 5000.00 | 5380.00 | 0.1367 | 0.6915 |
| 108.00 | Upper Strike | 380.00 | 5800.00 | 6180.00 | 0.1367 | 0.7943 |
| 115.00 | Upside (15%) | -320.00 | 6500.00 | 6180.00 | -0.1151 | 0.7943 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -13820.00 | -1.7764 |
| breakeven_1 | Breakeven 1 | 69.10 | -30.90% | -1910.00 | -0.00 | -0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | 3180.00 | 0.4087 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | 4580.00 | 0.5887 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 5380.00 | 0.6915 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | 6180.00 | 0.7943 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | 6180.00 | 0.7943 |
| infinity | Stock to Infinity | — | — | Unlimited | 6180.00 | 0.7943 |

---

### Short Strangle (ID=40) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: []
- Options Max PnL: 380.0
- Options Min PnL: -18820.0
- Combined Max PnL: -320.0
- Combined Min PnL: -20320.0

**Net Premium:**

- Per Share: -3.8
- Total: -380.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $380.00 | -$320.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.02x | 0.02x |
| Capital Basis | $2,780.00 | $14,280.00 |
| Cost Credit | Credit $380.00 | Credit $380.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.440281
- P(25% Max Profit): 0.705708
- P(50% Max Profit): 0.661077
- P(100% Max Profit): 0.5619
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -320.00 | -3000.00 | -3320.00 | -0.1151 | -0.2325 |
| 92.00 | Lower Strike | 380.00 | -2300.00 | -1920.00 | 0.1367 | -0.1345 |
| 100.00 | Current Market Price | 380.00 | -1500.00 | -1120.00 | 0.1367 | -0.0784 |
| 108.00 | Upper Strike | 380.00 | -700.00 | -320.00 | 0.1367 | -0.0224 |
| 115.00 | Upside (15%) | -320.00 | 0.00 | -320.00 | -0.1151 | -0.0224 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -20320.00 | -1.4230 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | -3320.00 | -0.2325 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | -1920.00 | -0.1345 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | -1120.00 | -0.0784 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | -320.00 | -0.0224 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | -320.00 | -0.0224 |
| infinity | Stock to Infinity | — | — | Unlimited | -320.00 | -0.0224 |

---

### Long Guts (ID=41) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | PUT | Long 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [88.2, 111.8]
- Options Max PnL: 18820.0
- Options Min PnL: -380.0
- Combined Max PnL: 18820.0
- Combined Min PnL: -380.0

**Net Premium:**

- Per Share: 19.8
- Total: 1980.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 49.53x | 49.53x |
| Capital Basis | $1,980.00 | $1,980.00 |
| Cost Credit | Debit $1,980.00 | Debit $1,980.00 |
| Pop | 25.4% | 25.4% |
| Margin Proxy | 1980.0 | — |

**Probabilities:**

- PoP (raw): 0.253752
- Assignment Prob: 0.0
- P(25% Max Profit): 3e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 320.00 | 0.00 | 320.00 | 0.8421 | 0.8421 |
| 88.20 | Breakeven 1 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 92.00 | Lower Strike | -380.00 | 0.00 | -380.00 | -1.0000 | -1.0000 |
| 100.00 | Current Market Price | -380.00 | 0.00 | -380.00 | -1.0000 | -1.0000 |
| 108.00 | Upper Strike | -380.00 | 0.00 | -380.00 | -1.0000 | -1.0000 |
| 111.80 | Breakeven 2 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 115.00 | Upside (15%) | 320.00 | 0.00 | 320.00 | 0.8421 | 0.8421 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8820.00 | 8820.00 | 4.4545 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 320.00 | 320.00 | 0.8421 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | -0.00 | -0.00 | -0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -380.00 | -380.00 | -1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -380.00 | -1.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -380.00 | -380.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | -0.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 320.00 | 320.00 | 0.8421 |
| infinity | Stock to Infinity | — | — | Unlimited | 96820.00 | 48.8990 |

---

### Long Guts (ID=41) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | PUT | Long 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [103.8]
- Options Max PnL: 18820.0
- Options Min PnL: -380.0
- Combined Max PnL: 38820.0
- Combined Min PnL: -1180.0

**Net Premium:**

- Per Share: 19.8
- Total: 1980.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 49.53x | 32.90x |
| Capital Basis | $1,980.00 | $11,980.00 |
| Cost Credit | Debit $1,980.00 | Debit $1,980.00 |
| Pop | 34.1% | 34.1% |
| Margin Proxy | 1980.0 | — |

**Probabilities:**

- PoP (raw): 0.34053
- Assignment Prob: 0.0
- P(25% Max Profit): 3e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 320.00 | -1500.00 | -1180.00 | 0.8421 | -0.1137 |
| 92.00 | Lower Strike | -380.00 | -800.00 | -1180.00 | -1.0000 | -0.1137 |
| 100.00 | Current Market Price | -380.00 | 0.00 | -380.00 | -1.0000 | -0.0366 |
| 103.80 | Breakeven 1 | -380.00 | 380.00 | -0.00 | -1.0000 | -0.0000 |
| 108.00 | Upper Strike | -380.00 | 800.00 | 420.00 | -1.0000 | 0.0405 |
| 115.00 | Upside (15%) | 320.00 | 1500.00 | 1820.00 | 0.8421 | 0.1753 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8820.00 | -1180.00 | -0.0985 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 320.00 | -1180.00 | -0.1137 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -380.00 | -1180.00 | -0.1137 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -380.00 | -0.0366 |
| breakeven_1 | Breakeven 1 | 103.80 | 3.80% | -380.00 | -0.00 | -0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -380.00 | 420.00 | 0.0405 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 320.00 | 1820.00 | 0.1753 |
| infinity | Stock to Infinity | — | — | Unlimited | 194820.00 | 16.2621 |

---

### Long Guts (ID=41) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | PUT | Long 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: []
- Options Max PnL: 18820.0
- Options Min PnL: -380.0
- Combined Max PnL: 43820.0
- Combined Min PnL: 3820.0

**Net Premium:**

- Per Share: 19.8
- Total: 1980.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 49.53x | 11.47x |
| Capital Basis | $1,980.00 | $6,980.00 |
| Cost Credit | Debit $1,980.00 | Debit $1,980.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 1980.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.0
- P(25% Max Profit): 3e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | 3820.00 | 0.00 | 3820.00 | 10.0526 | 0.7100 |
| 85.00 | Downside (15%) | 320.00 | 3500.00 | 3820.00 | 0.8421 | 0.7100 |
| 92.00 | Lower Strike | -380.00 | 4200.00 | 3820.00 | -1.0000 | 0.7100 |
| 100.00 | Current Market Price | -380.00 | 5000.00 | 4620.00 | -1.0000 | 0.8587 |
| 108.00 | Upper Strike | -380.00 | 5800.00 | 5420.00 | -1.0000 | 1.0074 |
| 115.00 | Upside (15%) | 320.00 | 6500.00 | 6820.00 | 0.8421 | 1.2677 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8820.00 | 3820.00 | 0.5473 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 320.00 | 3820.00 | 0.7100 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -380.00 | 3820.00 | 0.7100 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | 4620.00 | 0.8587 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -380.00 | 5420.00 | 1.0074 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 320.00 | 6820.00 | 1.2677 |
| infinity | Stock to Infinity | — | — | Unlimited | 199820.00 | 28.6275 |

---

### Long Guts (ID=41) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | PUT | Long 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [113.4]
- Options Max PnL: 18820.0
- Options Min PnL: -380.0
- Combined Max PnL: 37320.0
- Combined Min PnL: -2680.0

**Net Premium:**

- Per Share: 19.8
- Total: 1980.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 49.53x | 13.93x |
| Capital Basis | $1,980.00 | $13,480.00 |
| Cost Credit | Debit $1,980.00 | Debit $1,980.00 |
| Pop | 10.3% | 10.3% |
| Margin Proxy | 1980.0 | — |

**Probabilities:**

- PoP (raw): 0.103354
- Assignment Prob: 0.0
- P(25% Max Profit): 3e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 320.00 | -3000.00 | -2680.00 | 0.8421 | -0.2256 |
| 92.00 | Lower Strike | -380.00 | -2300.00 | -2680.00 | -1.0000 | -0.2256 |
| 100.00 | Current Market Price | -380.00 | -1500.00 | -1880.00 | -1.0000 | -0.1582 |
| 108.00 | Upper Strike | -380.00 | -700.00 | -1080.00 | -1.0000 | -0.0909 |
| 113.40 | Breakeven 1 | 160.00 | -160.00 | 0.00 | 0.4211 | 0.0000 |
| 115.00 | Upside (15%) | 320.00 | 0.00 | 320.00 | 0.8421 | 0.0269 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8820.00 | -2680.00 | -0.1988 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 320.00 | -2680.00 | -0.2256 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -380.00 | -2680.00 | -0.2256 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -1880.00 | -0.1582 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -380.00 | -1080.00 | -0.0909 |
| breakeven_1 | Breakeven 1 | 113.40 | 13.40% | 160.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 320.00 | 320.00 | 0.0269 |
| infinity | Stock to Infinity | — | — | Unlimited | 193320.00 | 14.3412 |

---

### Short Guts (ID=42) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_PUT_CALL

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | PUT | Short 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [88.2, 111.8]
- Options Max PnL: 380.0
- Options Min PnL: -18820.0
- Combined Max PnL: 380.0
- Combined Min PnL: -18820.0

**Net Premium:**

- Per Share: -19.8
- Total: -1980.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $380.00 | $380.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.02x | 0.02x |
| Capital Basis | $5,980.00 | $5,980.00 |
| Cost Credit | Credit $1,980.00 | Credit $1,980.00 |
| Pop | 74.6% | 74.6% |
| Margin Proxy | 5980.0 | — |

**Probabilities:**

- PoP (raw): 0.746248
- Assignment Prob: 1.0
- P(25% Max Profit): 0.705708
- P(50% Max Profit): 0.661077
- P(100% Max Profit): 0.5619
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -320.00 | 0.00 | -320.00 | -0.0535 | -0.0535 |
| 88.20 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 92.00 | Lower Strike | 380.00 | 0.00 | 380.00 | 0.0635 | 0.0635 |
| 100.00 | Current Market Price | 380.00 | 0.00 | 380.00 | 0.0635 | 0.0635 |
| 108.00 | Upper Strike | 380.00 | 0.00 | 380.00 | 0.0635 | 0.0635 |
| 111.80 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -320.00 | 0.00 | -320.00 | -0.0535 | -0.0535 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -8820.00 | -1.4749 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | -320.00 | -0.0535 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | 0.00 | 0.00 | 0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | 380.00 | 0.0635 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 380.00 | 0.0635 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | 380.00 | 0.0635 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | -320.00 | -0.0535 |
| infinity | Stock to Infinity | — | — | Unlimited | -96820.00 | -16.1906 |

---

### Short Guts (ID=42) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | PUT | Short 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [96.2]
- Options Max PnL: 380.0
- Options Min PnL: -18820.0
- Combined Max PnL: 1180.0
- Combined Min PnL: -18820.0

**Net Premium:**

- Per Share: -19.8
- Total: -1980.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $380.00 | $1,180.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.02x | 0.06x |
| Capital Basis | $5,980.00 | $15,980.00 |
| Cost Credit | Credit $1,980.00 | Credit $1,980.00 |
| Pop | 62.6% | 62.6% |
| Margin Proxy | 5980.0 | — |

**Probabilities:**

- PoP (raw): 0.62592
- Assignment Prob: 1.0
- P(25% Max Profit): 0.705708
- P(50% Max Profit): 0.661077
- P(100% Max Profit): 0.5619
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -320.00 | -1500.00 | -1820.00 | -0.0535 | -0.1139 |
| 92.00 | Lower Strike | 380.00 | -800.00 | -420.00 | 0.0635 | -0.0263 |
| 96.20 | Breakeven 1 | 380.00 | -380.00 | 0.00 | 0.0635 | 0.0000 |
| 100.00 | Current Market Price | 380.00 | 0.00 | 380.00 | 0.0635 | 0.0238 |
| 108.00 | Upper Strike | 380.00 | 800.00 | 1180.00 | 0.0635 | 0.0738 |
| 115.00 | Upside (15%) | -320.00 | 1500.00 | 1180.00 | -0.0535 | 0.0738 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -18820.00 | -1.1777 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | -1820.00 | -0.1139 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | -420.00 | -0.0263 |
| breakeven_1 | Breakeven 1 | 96.20 | -3.80% | 380.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 380.00 | 0.0238 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | 1180.00 | 0.0738 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | 1180.00 | 0.0738 |
| infinity | Stock to Infinity | — | — | Unlimited | 1180.00 | 0.0738 |

---

### Short Guts (ID=42) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | PUT | Short 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [69.1]
- Options Max PnL: 380.0
- Options Min PnL: -18820.0
- Combined Max PnL: 6180.0
- Combined Min PnL: -13820.0

**Net Premium:**

- Per Share: -19.8
- Total: -1980.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $380.00 | $6,180.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.02x | 0.45x |
| Capital Basis | $5,980.00 | $10,980.00 |
| Cost Credit | Credit $1,980.00 | Credit $1,980.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 5980.0 | — |

**Probabilities:**

- PoP (raw): 0.999773
- Assignment Prob: 1.0
- P(25% Max Profit): 0.705708
- P(50% Max Profit): 0.661077
- P(100% Max Profit): 0.5619
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -3820.00 | 0.00 | -3820.00 | -0.6388 | -0.3479 |
| 69.10 | Breakeven 1 | -1910.00 | 1910.00 | -0.00 | -0.3194 | -0.0000 |
| 85.00 | Downside (15%) | -320.00 | 3500.00 | 3180.00 | -0.0535 | 0.2896 |
| 92.00 | Lower Strike | 380.00 | 4200.00 | 4580.00 | 0.0635 | 0.4171 |
| 100.00 | Current Market Price | 380.00 | 5000.00 | 5380.00 | 0.0635 | 0.4900 |
| 108.00 | Upper Strike | 380.00 | 5800.00 | 6180.00 | 0.0635 | 0.5628 |
| 115.00 | Upside (15%) | -320.00 | 6500.00 | 6180.00 | -0.0535 | 0.5628 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -13820.00 | -1.2587 |
| breakeven_1 | Breakeven 1 | 69.10 | -30.90% | -1910.00 | -0.00 | -0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | 3180.00 | 0.2896 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | 4580.00 | 0.4171 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 5380.00 | 0.4900 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | 6180.00 | 0.5628 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | 6180.00 | 0.5628 |
| infinity | Stock to Infinity | — | — | Unlimited | 6180.00 | 0.5628 |

---

### Short Guts (ID=42) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | PUT | Short 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: []
- Options Max PnL: 380.0
- Options Min PnL: -18820.0
- Combined Max PnL: -320.0
- Combined Min PnL: -20320.0

**Net Premium:**

- Per Share: -19.8
- Total: -1980.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $380.00 | -$320.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.02x | 0.02x |
| Capital Basis | $5,980.00 | $17,480.00 |
| Cost Credit | Credit $1,980.00 | Credit $1,980.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 5980.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 1.0
- P(25% Max Profit): 0.705708
- P(50% Max Profit): 0.661077
- P(100% Max Profit): 0.5619
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -320.00 | -3000.00 | -3320.00 | -0.0535 | -0.1899 |
| 92.00 | Lower Strike | 380.00 | -2300.00 | -1920.00 | 0.0635 | -0.1098 |
| 100.00 | Current Market Price | 380.00 | -1500.00 | -1120.00 | 0.0635 | -0.0641 |
| 108.00 | Upper Strike | 380.00 | -700.00 | -320.00 | 0.0635 | -0.0183 |
| 115.00 | Upside (15%) | -320.00 | 0.00 | -320.00 | -0.0535 | -0.0183 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -20320.00 | -1.1625 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | -3320.00 | -0.1899 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | -1920.00 | -0.1098 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | -1120.00 | -0.0641 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | -320.00 | -0.0183 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | -320.00 | -0.0183 |
| infinity | Stock to Infinity | — | — | Unlimited | -320.00 | -0.0183 |

---

### Strip (ID=43) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 2 | 100.00 | 2.50 | 100 |
| 2 | CALL | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [96.25, 107.5]
- Options Max PnL: 19250.0
- Options Min PnL: -750.0
- Combined Max PnL: 19250.0
- Combined Min PnL: -750.0

**Net Premium:**

- Per Share: 7.5
- Total: 750.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 25.67x | 25.67x |
| Capital Basis | $750.00 | $750.00 |
| Cost Credit | Debit $750.00 | Debit $750.00 |
| Pop | 60.3% | 60.3% |
| Margin Proxy | 750.0 | — |

**Probabilities:**

- PoP (raw): 0.603137
- Assignment Prob: 0.0
- P(25% Max Profit): 0.001023
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 2250.00 | 0.00 | 2250.00 | 3.0000 | 3.0000 |
| 96.25 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | -750.00 | 0.00 | -750.00 | -1.0000 | -1.0000 |
| 107.50 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 750.00 | 0.00 | 750.00 | 1.0000 | 1.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 19250.00 | 19250.00 | 25.6667 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 2250.00 | 2250.00 | 3.0000 |
| breakeven_1 | Breakeven 1 | 96.25 | -3.75% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -750.00 | -750.00 | -1.0000 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -750.00 | -750.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 107.50 | 7.50% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 750.00 | 750.00 | 1.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | 89250.00 | 119.0000 |

---

### Strip (ID=43) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 2 | 100.00 | 2.50 | 100 |
| 2 | CALL | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [92.5, 103.75]
- Options Max PnL: 19250.0
- Options Min PnL: -750.0
- Combined Max PnL: 39250.0
- Combined Min PnL: -750.0

**Net Premium:**

- Per Share: 7.5
- Total: 750.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 25.67x | 52.33x |
| Capital Basis | $750.00 | $10,750.00 |
| Cost Credit | Debit $750.00 | Debit $750.00 |
| Pop | 58.5% | 58.5% |
| Margin Proxy | 750.0 | — |

**Probabilities:**

- PoP (raw): 0.584608
- Assignment Prob: 0.0
- P(25% Max Profit): 0.001023
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 2250.00 | -1500.00 | 750.00 | 3.0000 | 0.0698 |
| 92.50 | Breakeven 1 | 750.00 | -750.00 | 0.00 | 1.0000 | 0.0000 |
| 100.00 | Current Market Price | -750.00 | 0.00 | -750.00 | -1.0000 | -0.0698 |
| 103.75 | Breakeven 2 | -375.00 | 375.00 | 0.00 | -0.5000 | 0.0000 |
| 115.00 | Upside (15%) | 750.00 | 1500.00 | 2250.00 | 1.0000 | 0.2093 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 19250.00 | 9250.00 | 0.8605 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 2250.00 | 750.00 | 0.0698 |
| breakeven_1 | Breakeven 1 | 92.50 | -7.50% | 750.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -750.00 | -750.00 | -0.0698 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -750.00 | -750.00 | -0.0698 |
| breakeven_2 | Breakeven 2 | 103.75 | 3.75% | -375.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 750.00 | 2250.00 | 0.2093 |
| infinity | Stock to Infinity | — | — | Unlimited | 179250.00 | 16.6744 |

---

### Strip (ID=43) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 2 | 100.00 | 2.50 | 100 |
| 2 | CALL | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: []
- Options Max PnL: 19250.0
- Options Min PnL: -750.0
- Combined Max PnL: 44250.0
- Combined Min PnL: 4250.0

**Net Premium:**

- Per Share: 7.5
- Total: 750.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 25.67x | 10.41x |
| Capital Basis | $750.00 | $5,750.00 |
| Cost Credit | Debit $750.00 | Debit $750.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 750.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.0
- P(25% Max Profit): 0.001023
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | 9250.00 | 0.00 | 9250.00 | 12.3333 | 1.6087 |
| 85.00 | Downside (15%) | 2250.00 | 3500.00 | 5750.00 | 3.0000 | 1.0000 |
| 100.00 | Current Market Price | -750.00 | 5000.00 | 4250.00 | -1.0000 | 0.7391 |
| 115.00 | Upside (15%) | 750.00 | 6500.00 | 7250.00 | 1.0000 | 1.2609 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 19250.00 | 14250.00 | 2.4783 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 2250.00 | 5750.00 | 1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -750.00 | 4250.00 | 0.7391 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -750.00 | 4250.00 | 0.7391 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 750.00 | 7250.00 | 1.2609 |
| infinity | Stock to Infinity | — | — | Unlimited | 184250.00 | 32.0435 |

---

### Strip (ID=43) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 2 | 100.00 | 2.50 | 100 |
| 2 | CALL | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [77.5, 111.25]
- Options Max PnL: 19250.0
- Options Min PnL: -750.0
- Combined Max PnL: 37750.0
- Combined Min PnL: -2250.0

**Net Premium:**

- Per Share: 7.5
- Total: 750.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 25.67x | 16.78x |
| Capital Basis | $750.00 | $12,250.00 |
| Cost Credit | Debit $750.00 | Debit $750.00 |
| Pop | 14.9% | 14.9% |
| Margin Proxy | 750.0 | — |

**Probabilities:**

- PoP (raw): 0.148583
- Assignment Prob: 0.0
- P(25% Max Profit): 0.001023
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 77.50 | Breakeven 1 | 3750.00 | -3750.00 | 0.00 | 5.0000 | 0.0000 |
| 85.00 | Downside (15%) | 2250.00 | -3000.00 | -750.00 | 3.0000 | -0.0612 |
| 100.00 | Current Market Price | -750.00 | -1500.00 | -2250.00 | -1.0000 | -0.1837 |
| 111.25 | Breakeven 2 | 375.00 | -375.00 | 0.00 | 0.5000 | 0.0000 |
| 115.00 | Upside (15%) | 750.00 | 0.00 | 750.00 | 1.0000 | 0.0612 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 19250.00 | 7750.00 | 0.6327 |
| breakeven_1 | Breakeven 1 | 77.50 | -22.50% | 3750.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 2250.00 | -750.00 | -0.0612 |
| spot | Current Market Price | 100.00 | 0.00% | -750.00 | -2250.00 | -0.1837 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -750.00 | -2250.00 | -0.1837 |
| breakeven_2 | Breakeven 2 | 111.25 | 11.25% | 375.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 750.00 | 750.00 | 0.0612 |
| infinity | Stock to Infinity | — | — | Unlimited | 177750.00 | 14.5102 |

---

### Strap (ID=44) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Long 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [92.5, 103.75]
- Options Max PnL: 39250.0
- Options Min PnL: -750.0
- Combined Max PnL: 39250.0
- Combined Min PnL: -750.0

**Net Premium:**

- Per Share: 7.5
- Total: 750.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 52.33x | 52.33x |
| Capital Basis | $750.00 | $750.00 |
| Cost Credit | Debit $750.00 | Debit $750.00 |
| Pop | 58.5% | 58.5% |
| Margin Proxy | 750.0 | — |

**Probabilities:**

- PoP (raw): 0.584608
- Assignment Prob: 0.0
- P(25% Max Profit): 1.8e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 750.00 | 0.00 | 750.00 | 1.0000 | 1.0000 |
| 92.50 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | -750.00 | 0.00 | -750.00 | -1.0000 | -1.0000 |
| 103.75 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 2250.00 | 0.00 | 2250.00 | 3.0000 | 3.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9250.00 | 9250.00 | 12.3333 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 750.00 | 750.00 | 1.0000 |
| breakeven_1 | Breakeven 1 | 92.50 | -7.50% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -750.00 | -750.00 | -1.0000 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -750.00 | -750.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 103.75 | 3.75% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 2250.00 | 2250.00 | 3.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | 179250.00 | 239.0000 |

---

### Strap (ID=44) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Long 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [102.5]
- Options Max PnL: 39250.0
- Options Min PnL: -750.0
- Combined Max PnL: 59250.0
- Combined Min PnL: -750.0

**Net Premium:**

- Per Share: 7.5
- Total: 750.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | -$750.00 |
| Risk Reward | 52.33x | 79.00x |
| Capital Basis | $750.00 | $10,750.00 |
| Cost Credit | Debit $750.00 | Debit $750.00 |
| Pop | 38.6% | 38.6% |
| Margin Proxy | 750.0 | — |

**Probabilities:**

- PoP (raw): 0.386034
- Assignment Prob: 0.0
- P(25% Max Profit): 1.8e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 750.00 | -1500.00 | -750.00 | 1.0000 | -0.0698 |
| 100.00 | Current Market Price | -750.00 | 0.00 | -750.00 | -1.0000 | -0.0698 |
| 102.50 | Breakeven 1 | -250.00 | 250.00 | 0.00 | -0.3333 | 0.0000 |
| 115.00 | Upside (15%) | 2250.00 | 1500.00 | 3750.00 | 3.0000 | 0.3488 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9250.00 | -750.00 | -0.0698 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 750.00 | -750.00 | -0.0698 |
| spot | Current Market Price | 100.00 | 0.00% | -750.00 | -750.00 | -0.0698 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -750.00 | -750.00 | -0.0698 |
| breakeven_1 | Breakeven 1 | 102.50 | 2.50% | -250.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 2250.00 | 3750.00 | 0.3488 |
| infinity | Stock to Infinity | — | — | Unlimited | 269250.00 | 25.0465 |

---

### Strap (ID=44) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Long 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: []
- Options Max PnL: 39250.0
- Options Min PnL: -750.0
- Combined Max PnL: 64250.0
- Combined Min PnL: 4250.0

**Net Premium:**

- Per Share: 7.5
- Total: 750.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | $4,250.00 |
| Risk Reward | 52.33x | 15.12x |
| Capital Basis | $750.00 | $5,750.00 |
| Cost Credit | Debit $750.00 | Debit $750.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 750.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.0
- P(25% Max Profit): 1.8e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | 4250.00 | 0.00 | 4250.00 | 5.6667 | 0.7391 |
| 85.00 | Downside (15%) | 750.00 | 3500.00 | 4250.00 | 1.0000 | 0.7391 |
| 100.00 | Current Market Price | -750.00 | 5000.00 | 4250.00 | -1.0000 | 0.7391 |
| 115.00 | Upside (15%) | 2250.00 | 6500.00 | 8750.00 | 3.0000 | 1.5217 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9250.00 | 4250.00 | 0.7391 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 750.00 | 4250.00 | 0.7391 |
| spot | Current Market Price | 100.00 | 0.00% | -750.00 | 4250.00 | 0.7391 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -750.00 | 4250.00 | 0.7391 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 2250.00 | 8750.00 | 1.5217 |
| infinity | Stock to Infinity | — | — | Unlimited | 274250.00 | 47.6957 |

---

### Strap (ID=44) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Long 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [107.5]
- Options Max PnL: 39250.0
- Options Min PnL: -750.0
- Combined Max PnL: 57750.0
- Combined Min PnL: -2250.0

**Net Premium:**

- Per Share: 7.5
- Total: 750.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | Unlimited | -$2,250.00 |
| Risk Reward | 52.33x | 25.67x |
| Capital Basis | $750.00 | $12,250.00 |
| Cost Credit | Debit $750.00 | Debit $750.00 |
| Pop | 22.7% | 22.7% |
| Margin Proxy | 750.0 | — |

**Probabilities:**

- PoP (raw): 0.227159
- Assignment Prob: 0.0
- P(25% Max Profit): 1.8e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 750.00 | -3000.00 | -2250.00 | 1.0000 | -0.1837 |
| 100.00 | Current Market Price | -750.00 | -1500.00 | -2250.00 | -1.0000 | -0.1837 |
| 107.50 | Breakeven 1 | 750.00 | -750.00 | 0.00 | 1.0000 | 0.0000 |
| 115.00 | Upside (15%) | 2250.00 | 0.00 | 2250.00 | 3.0000 | 0.1837 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9250.00 | -2250.00 | -0.1837 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 750.00 | -2250.00 | -0.1837 |
| spot | Current Market Price | 100.00 | 0.00% | -750.00 | -2250.00 | -0.1837 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -750.00 | -2250.00 | -0.1837 |
| breakeven_1 | Breakeven 1 | 107.50 | 7.50% | 750.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 2250.00 | 2250.00 | 0.1837 |
| infinity | Stock to Infinity | — | — | Unlimited | 267750.00 | 21.8571 |

---

### Covered Short Straddle (ID=45) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [97.5]
- Options Max PnL: 500.0
- Options Min PnL: -19500.0
- Combined Max PnL: 500.0
- Combined Min PnL: -19500.0

**Net Premium:**

- Per Share: -5.0
- Total: -500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $500.00 | $500.00 |
| Max Loss | Unlimited | -$19,500.00 |
| Risk Reward | 0.03x | 0.03x |
| Capital Basis | $19,500.00 | $29,500.00 |
| Cost Credit | Credit $500.00 | Credit $500.00 |
| Pop | 57.6% | 57.6% |
| Margin Proxy | 19500.0 | — |

**Probabilities:**

- PoP (raw): 0.576062
- Assignment Prob: 1.0
- P(25% Max Profit): 0.281789
- P(50% Max Profit): 0.190029
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1000.00 | -1500.00 | -2500.00 | -0.0513 | -0.0847 |
| 97.50 | Breakeven 1 | 250.00 | -250.00 | 0.00 | 0.0128 | 0.0000 |
| 100.00 | Current Market Price | 500.00 | 0.00 | 500.00 | 0.0256 | 0.0169 |
| 115.00 | Upside (15%) | -1000.00 | 1500.00 | 500.00 | -0.0513 | 0.0169 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9500.00 | -19500.00 | -0.6610 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1000.00 | -2500.00 | -0.0847 |
| breakeven_1 | Breakeven 1 | 97.50 | -2.50% | 250.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 500.00 | 500.00 | 0.0169 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 500.00 | 500.00 | 0.0169 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1000.00 | 500.00 | 0.0169 |
| infinity | Stock to Infinity | — | — | Unlimited | 500.00 | 0.0169 |

---

### Covered Short Straddle (ID=45) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [97.5]
- Options Max PnL: 500.0
- Options Min PnL: -19500.0
- Combined Max PnL: 500.0
- Combined Min PnL: -19500.0

**Net Premium:**

- Per Share: -5.0
- Total: -500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $500.00 | $500.00 |
| Max Loss | Unlimited | -$19,500.00 |
| Risk Reward | 0.03x | 0.03x |
| Capital Basis | $19,500.00 | $29,500.00 |
| Cost Credit | Credit $500.00 | Credit $500.00 |
| Pop | 57.6% | 57.6% |
| Margin Proxy | 19500.0 | — |

**Probabilities:**

- PoP (raw): 0.576062
- Assignment Prob: 1.0
- P(25% Max Profit): 0.281789
- P(50% Max Profit): 0.190029
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1000.00 | -1500.00 | -2500.00 | -0.0513 | -0.0847 |
| 97.50 | Breakeven 1 | 250.00 | -250.00 | 0.00 | 0.0128 | 0.0000 |
| 100.00 | Current Market Price | 500.00 | 0.00 | 500.00 | 0.0256 | 0.0169 |
| 115.00 | Upside (15%) | -1000.00 | 1500.00 | 500.00 | -0.0513 | 0.0169 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9500.00 | -19500.00 | -0.6610 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1000.00 | -2500.00 | -0.0847 |
| breakeven_1 | Breakeven 1 | 97.50 | -2.50% | 250.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 500.00 | 500.00 | 0.0169 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 500.00 | 500.00 | 0.0169 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1000.00 | 500.00 | 0.0169 |
| infinity | Stock to Infinity | — | — | Unlimited | 500.00 | 0.0169 |

---

### Covered Short Straddle (ID=45) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [72.5]
- Options Max PnL: 500.0
- Options Min PnL: -19500.0
- Combined Max PnL: 5500.0
- Combined Min PnL: -14500.0

**Net Premium:**

- Per Share: -5.0
- Total: -500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $500.00 | $5,500.00 |
| Max Loss | Unlimited | -$14,500.00 |
| Risk Reward | 0.03x | 0.38x |
| Capital Basis | $19,500.00 | $24,500.00 |
| Cost Credit | Credit $500.00 | Credit $500.00 |
| Pop | 99.9% | 99.9% |
| Margin Proxy | 19500.0 | — |

**Probabilities:**

- PoP (raw): 0.998834
- Assignment Prob: 1.0
- P(25% Max Profit): 0.281789
- P(50% Max Profit): 0.190029
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -4500.00 | 0.00 | -4500.00 | -0.2308 | -0.1837 |
| 72.50 | Breakeven 1 | -2250.00 | 2250.00 | 0.00 | -0.1154 | 0.0000 |
| 85.00 | Downside (15%) | -1000.00 | 3500.00 | 2500.00 | -0.0513 | 0.1020 |
| 100.00 | Current Market Price | 500.00 | 5000.00 | 5500.00 | 0.0256 | 0.2245 |
| 115.00 | Upside (15%) | -1000.00 | 6500.00 | 5500.00 | -0.0513 | 0.2245 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9500.00 | -14500.00 | -0.5918 |
| breakeven_1 | Breakeven 1 | 72.50 | -27.50% | -2250.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1000.00 | 2500.00 | 0.1020 |
| spot | Current Market Price | 100.00 | 0.00% | 500.00 | 5500.00 | 0.2245 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 500.00 | 5500.00 | 0.2245 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1000.00 | 5500.00 | 0.2245 |
| infinity | Stock to Infinity | — | — | Unlimited | 5500.00 | 0.2245 |

---

### Covered Short Straddle (ID=45) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: []
- Options Max PnL: 500.0
- Options Min PnL: -19500.0
- Combined Max PnL: -1000.0
- Combined Min PnL: -21000.0

**Net Premium:**

- Per Share: -5.0
- Total: -500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $500.00 | -$1,000.00 |
| Max Loss | Unlimited | -$21,000.00 |
| Risk Reward | 0.03x | 0.05x |
| Capital Basis | $19,500.00 | $31,000.00 |
| Cost Credit | Credit $500.00 | Credit $500.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 19500.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 1.0
- P(25% Max Profit): 0.281789
- P(50% Max Profit): 0.190029
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1000.00 | -3000.00 | -4000.00 | -0.0513 | -0.1290 |
| 100.00 | Current Market Price | 500.00 | -1500.00 | -1000.00 | 0.0256 | -0.0323 |
| 115.00 | Upside (15%) | -1000.00 | 0.00 | -1000.00 | -0.0513 | -0.0323 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9500.00 | -21000.00 | -0.6774 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1000.00 | -4000.00 | -0.1290 |
| spot | Current Market Price | 100.00 | 0.00% | 500.00 | -1000.00 | -0.0323 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 500.00 | -1000.00 | -0.0323 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1000.00 | -1000.00 | -0.0323 |
| infinity | Stock to Infinity | — | — | Unlimited | -1000.00 | -0.0323 |

---

### Covered Short Strangle (ID=46) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [96.2]
- Options Max PnL: 380.0
- Options Min PnL: -18820.0
- Combined Max PnL: 1180.0
- Combined Min PnL: -18820.0

**Net Premium:**

- Per Share: -3.8
- Total: -380.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $380.00 | $1,180.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.02x | 0.06x |
| Capital Basis | $2,780.00 | $12,780.00 |
| Cost Credit | Credit $380.00 | Credit $380.00 |
| Pop | 62.6% | 62.6% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.62592
- Assignment Prob: 0.440281
- P(25% Max Profit): 0.705708
- P(50% Max Profit): 0.661077
- P(100% Max Profit): 0.5619
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -320.00 | -1500.00 | -1820.00 | -0.1151 | -0.1424 |
| 92.00 | Lower Strike | 380.00 | -800.00 | -420.00 | 0.1367 | -0.0329 |
| 96.20 | Breakeven 1 | 380.00 | -380.00 | 0.00 | 0.1367 | 0.0000 |
| 100.00 | Current Market Price | 380.00 | 0.00 | 380.00 | 0.1367 | 0.0297 |
| 108.00 | Upper Strike | 380.00 | 800.00 | 1180.00 | 0.1367 | 0.0923 |
| 115.00 | Upside (15%) | -320.00 | 1500.00 | 1180.00 | -0.1151 | 0.0923 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -18820.00 | -1.4726 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | -1820.00 | -0.1424 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | -420.00 | -0.0329 |
| breakeven_1 | Breakeven 1 | 96.20 | -3.80% | 380.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 380.00 | 0.0297 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | 1180.00 | 0.0923 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | 1180.00 | 0.0923 |
| infinity | Stock to Infinity | — | — | Unlimited | 1180.00 | 0.0923 |

---

### Covered Short Strangle (ID=46) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [96.2]
- Options Max PnL: 380.0
- Options Min PnL: -18820.0
- Combined Max PnL: 1180.0
- Combined Min PnL: -18820.0

**Net Premium:**

- Per Share: -3.8
- Total: -380.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $380.00 | $1,180.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.02x | 0.06x |
| Capital Basis | $2,780.00 | $12,780.00 |
| Cost Credit | Credit $380.00 | Credit $380.00 |
| Pop | 62.6% | 62.6% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.62592
- Assignment Prob: 0.440281
- P(25% Max Profit): 0.705708
- P(50% Max Profit): 0.661077
- P(100% Max Profit): 0.5619
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -320.00 | -1500.00 | -1820.00 | -0.1151 | -0.1424 |
| 92.00 | Lower Strike | 380.00 | -800.00 | -420.00 | 0.1367 | -0.0329 |
| 96.20 | Breakeven 1 | 380.00 | -380.00 | 0.00 | 0.1367 | 0.0000 |
| 100.00 | Current Market Price | 380.00 | 0.00 | 380.00 | 0.1367 | 0.0297 |
| 108.00 | Upper Strike | 380.00 | 800.00 | 1180.00 | 0.1367 | 0.0923 |
| 115.00 | Upside (15%) | -320.00 | 1500.00 | 1180.00 | -0.1151 | 0.0923 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -18820.00 | -1.4726 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | -1820.00 | -0.1424 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | -420.00 | -0.0329 |
| breakeven_1 | Breakeven 1 | 96.20 | -3.80% | 380.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 380.00 | 0.0297 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | 1180.00 | 0.0923 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | 1180.00 | 0.0923 |
| infinity | Stock to Infinity | — | — | Unlimited | 1180.00 | 0.0923 |

---

### Covered Short Strangle (ID=46) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [69.1]
- Options Max PnL: 380.0
- Options Min PnL: -18820.0
- Combined Max PnL: 6180.0
- Combined Min PnL: -13820.0

**Net Premium:**

- Per Share: -3.8
- Total: -380.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $380.00 | $6,180.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.02x | 0.45x |
| Capital Basis | $2,780.00 | $7,780.00 |
| Cost Credit | Credit $380.00 | Credit $380.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.999773
- Assignment Prob: 0.440281
- P(25% Max Profit): 0.705708
- P(50% Max Profit): 0.661077
- P(100% Max Profit): 0.5619
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -3820.00 | 0.00 | -3820.00 | -1.3741 | -0.4910 |
| 69.10 | Breakeven 1 | -1910.00 | 1910.00 | -0.00 | -0.6871 | -0.0000 |
| 85.00 | Downside (15%) | -320.00 | 3500.00 | 3180.00 | -0.1151 | 0.4087 |
| 92.00 | Lower Strike | 380.00 | 4200.00 | 4580.00 | 0.1367 | 0.5887 |
| 100.00 | Current Market Price | 380.00 | 5000.00 | 5380.00 | 0.1367 | 0.6915 |
| 108.00 | Upper Strike | 380.00 | 5800.00 | 6180.00 | 0.1367 | 0.7943 |
| 115.00 | Upside (15%) | -320.00 | 6500.00 | 6180.00 | -0.1151 | 0.7943 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -13820.00 | -1.7764 |
| breakeven_1 | Breakeven 1 | 69.10 | -30.90% | -1910.00 | -0.00 | -0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | 3180.00 | 0.4087 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | 4580.00 | 0.5887 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 5380.00 | 0.6915 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | 6180.00 | 0.7943 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | 6180.00 | 0.7943 |
| infinity | Stock to Infinity | — | — | Unlimited | 6180.00 | 0.7943 |

---

### Covered Short Strangle (ID=46) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: []
- Options Max PnL: 380.0
- Options Min PnL: -18820.0
- Combined Max PnL: -320.0
- Combined Min PnL: -20320.0

**Net Premium:**

- Per Share: -3.8
- Total: -380.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $380.00 | -$320.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.02x | 0.02x |
| Capital Basis | $2,780.00 | $14,280.00 |
| Cost Credit | Credit $380.00 | Credit $380.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.440281
- P(25% Max Profit): 0.705708
- P(50% Max Profit): 0.661077
- P(100% Max Profit): 0.5619
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -320.00 | -3000.00 | -3320.00 | -0.1151 | -0.2325 |
| 92.00 | Lower Strike | 380.00 | -2300.00 | -1920.00 | 0.1367 | -0.1345 |
| 100.00 | Current Market Price | 380.00 | -1500.00 | -1120.00 | 0.1367 | -0.0784 |
| 108.00 | Upper Strike | 380.00 | -700.00 | -320.00 | 0.1367 | -0.0224 |
| 115.00 | Upside (15%) | -320.00 | 0.00 | -320.00 | -0.1151 | -0.0224 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -20320.00 | -1.4230 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | -3320.00 | -0.2325 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | -1920.00 | -0.1345 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | -1120.00 | -0.0784 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | -320.00 | -0.0224 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | -320.00 | -0.0224 |
| infinity | Stock to Infinity | — | — | Unlimited | -320.00 | -0.0224 |

---

### Long Box Spread (ID=47) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |
| 3 | PUT | Long 1 | 108.00 | 9.90 | 100 |
| 4 | PUT | Short 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [0.0, 1.003344, 2.006689, 3.010033, 4.013378, 5.016722, 6.020067, 7.023411, 8.026756, 10.033445, 12.040134, 14.046823, 16.053512, 17.056856, 18.060201, 19.063545, 20.06689, 21.070234, 22.073579, 23.076923, 24.080268, 25.083612, 26.086957, 34.113712, 35.117057, 36.120401, 37.123746, 38.12709, 39.130435, 41.137124, 42.140468, 43.143813, 44.147157, 45.150502, 46.153846, 47.157191, 48.160535, 49.16388, 52.675585, 55.183946, 57.190635, 58.19398, 59.197324, 60.200669, 61.204013, 62.207358, 63.210702, 64.214047, 65.217391, 66.220736, 67.22408, 68.227425, 69.230769, 70.234114, 71.73913, 73.244147, 75.250836, 78.26087, 82.274247, 84.280936, 86.287625, 88.294314, 92.0, 103.344482, 108.0, 108.361204, 111.371237, 112.374582, 114.381271, 116.38796, 117.892977, 120.401338, 123.411371, 124.414716, 126.923077, 128.428094, 129.431438, 130.434783, 131.438127, 132.441472, 133.444816, 134.448161, 135.451505, 136.454849, 137.458194, 138.461538, 139.464883, 140.468227, 141.471572, 142.474916, 143.478261, 144.481605, 145.48495, 147.993311, 150.501672, 151.505017, 152.508361, 153.511706, 154.51505, 155.518395, 156.521739, 157.525084, 158.528428, 159.531773, 160.535117, 161.538462, 162.541806, 163.545151, 164.548495, 165.551839, 170.568562, 171.571906, 174.58194, 175.585284, 176.588629, 177.591973, 178.595318, 179.598662, 180.602007, 181.605351, 182.608696, 183.61204, 184.615385, 186.622074, 187.625418, 189.632107, 191.638796, 192.64214, 193.645485, 194.648829, 195.652174, 196.655518, 197.658863, 198.662207, 199.665552, 200.668896, 201.672241, 202.675585, 203.67893, 204.682274, 205.685619, 206.688963, 207.692308, 208.695652, 209.698997, 210.702341, 211.705686, 212.70903, 213.712375, 214.715719, 215.719064, 216.722408, 217.725753, 218.729097, 219.732441, 220.735786, 221.73913, 222.742475, 223.745819, 224.749164, 225.752508, 226.755853, 227.759197, 228.762542, 229.765886, 230.769231, 231.772575, 232.77592, 233.779264, 234.782609, 235.785953, 236.789298, 237.792642, 238.795987, 239.799331, 240.802676, 241.80602, 242.809365, 243.812709, 244.816054, 245.819398, 246.822742, 247.826087, 248.829431, 249.832776, 250.83612, 251.839465, 252.842809, 253.846154, 254.849498, 255.852843, 256.856187, 257.859532, 258.862876, 259.866221, 260.869565, 261.87291, 262.876254, 263.879599, 264.882943, 265.886288, 266.889632, 269.899666, 270.90301, 272.408027, 273.913043, 274.916388, 275.919732, 276.923077, 277.926421, 278.929766, 279.93311, 280.936455, 281.939799, 282.943144, 283.946488, 284.949833, 285.953177, 286.956522, 287.959866, 288.963211, 289.966555, 290.9699, 291.973244, 292.976589, 293.979933, 294.983278, 295.986622, 296.989967, 297.993311, 298.996656]
- Options Max PnL: 0.0
- Options Min PnL: -0.0
- Combined Max PnL: 0.0
- Combined Min PnL: -0.0

**Net Premium:**

- Per Share: 16.0
- Total: 1600.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | $0.00 |
| Max Loss | -$0.00 | -$0.00 |
| Risk Reward | 1.00x | 1.00x |
| Capital Basis | $1.00 | $1.00 |
| Cost Credit | Debit $1,600.00 | Debit $1,600.00 |
| Pop | 9.0% | 9.0% |
| Margin Proxy | 1.0 | — |

**Probabilities:**

- PoP (raw): 0.090106
- Assignment Prob: 0.440281
- P(25% Max Profit): 0.0
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 0.00 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 1.00 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 2.01 | Breakeven 3 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 3.01 | Breakeven 4 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 4.01 | Breakeven 5 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 5.02 | Breakeven 6 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 6.02 | Breakeven 7 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 7.02 | Breakeven 8 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 8.03 | Breakeven 9 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 10.03 | Breakeven 10 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 12.04 | Breakeven 11 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 14.05 | Breakeven 12 | -0.00 | 0.00 | -0.00 | -0.5000 | -0.5000 |
| 16.05 | Breakeven 13 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 17.06 | Breakeven 14 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 18.06 | Breakeven 15 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 19.06 | Breakeven 16 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 20.07 | Breakeven 17 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 21.07 | Breakeven 18 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 22.07 | Breakeven 19 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 23.08 | Breakeven 20 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 24.08 | Breakeven 21 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 25.08 | Breakeven 22 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 26.09 | Breakeven 23 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 34.11 | Breakeven 24 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 35.12 | Breakeven 25 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 36.12 | Breakeven 26 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 37.12 | Breakeven 27 | -0.00 | 0.00 | -0.00 | -0.5000 | -0.5000 |
| 38.13 | Breakeven 28 | 0.00 | 0.00 | 0.00 | 0.5000 | 0.5000 |
| 39.13 | Breakeven 29 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 41.14 | Breakeven 30 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 42.14 | Breakeven 31 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 43.14 | Breakeven 32 | 0.00 | 0.00 | 0.00 | 0.5000 | 0.5000 |
| 44.15 | Breakeven 33 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 45.15 | Breakeven 34 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 46.15 | Breakeven 35 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 47.16 | Breakeven 36 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 48.16 | Breakeven 37 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 49.16 | Breakeven 38 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 52.68 | Breakeven 39 | 0.00 | 0.00 | 0.00 | 0.2500 | 0.2500 |
| 55.18 | Breakeven 40 | -0.00 | 0.00 | -0.00 | -0.2500 | -0.2500 |
| 57.19 | Breakeven 41 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 58.19 | Breakeven 42 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 59.20 | Breakeven 43 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 60.20 | Breakeven 44 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 61.20 | Breakeven 45 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 62.21 | Breakeven 46 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 63.21 | Breakeven 47 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 64.21 | Breakeven 48 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 65.22 | Breakeven 49 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 66.22 | Breakeven 50 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 67.22 | Breakeven 51 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 68.23 | Breakeven 52 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 69.23 | Breakeven 53 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 70.23 | Breakeven 54 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 71.74 | Breakeven 55 | 0.00 | 0.00 | 0.00 | 0.1250 | 0.1250 |
| 73.24 | Breakeven 56 | -0.00 | 0.00 | -0.00 | -0.1250 | -0.1250 |
| 75.25 | Breakeven 57 | 0.00 | 0.00 | 0.00 | 0.2500 | 0.2500 |
| 78.26 | Breakeven 58 | 0.00 | 0.00 | 0.00 | 0.1250 | 0.1250 |
| 82.27 | Breakeven 59 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 84.28 | Breakeven 60 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 85.00 | Downside (15%) | 0.00 | 0.00 | 0.00 | 0.0312 | 0.0312 |
| 86.29 | Breakeven 61 | 0.00 | 0.00 | 0.00 | 0.0312 | 0.0312 |
| 88.29 | Breakeven 62 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 92.00 | Breakeven 63 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | -0.00 | 0.00 | -0.00 | -0.0312 | -0.0312 |
| 103.34 | Breakeven 64 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Breakeven 65 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.36 | Breakeven 66 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 111.37 | Breakeven 67 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 112.37 | Breakeven 68 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 114.38 | Breakeven 69 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 0.00 | 0.00 | 0.00 | 0.0625 | 0.0625 |
| 116.39 | Breakeven 70 | -0.00 | 0.00 | -0.00 | -0.0625 | -0.0625 |
| 117.89 | Breakeven 71 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 120.40 | Breakeven 72 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 123.41 | Breakeven 73 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 124.41 | Breakeven 74 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 126.92 | Breakeven 75 | 0.00 | 0.00 | 0.00 | 0.1250 | 0.1250 |
| 128.43 | Breakeven 76 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 129.43 | Breakeven 77 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 130.43 | Breakeven 78 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 131.44 | Breakeven 79 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 132.44 | Breakeven 80 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 133.44 | Breakeven 81 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 134.45 | Breakeven 82 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 135.45 | Breakeven 83 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 136.45 | Breakeven 84 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 137.46 | Breakeven 85 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 138.46 | Breakeven 86 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 139.46 | Breakeven 87 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 140.47 | Breakeven 88 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 141.47 | Breakeven 89 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 142.47 | Breakeven 90 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 143.48 | Breakeven 91 | -0.00 | 0.00 | -0.00 | -0.2500 | -0.2500 |
| 144.48 | Breakeven 92 | 0.00 | 0.00 | 0.00 | 0.2500 | 0.2500 |
| 145.48 | Breakeven 93 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 147.99 | Breakeven 94 | -0.00 | 0.00 | -0.00 | -0.2500 | -0.2500 |
| 150.50 | Breakeven 95 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 151.51 | Breakeven 96 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 152.51 | Breakeven 97 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 153.51 | Breakeven 98 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 154.52 | Breakeven 99 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 155.52 | Breakeven 100 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 156.52 | Breakeven 101 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 157.53 | Breakeven 102 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 158.53 | Breakeven 103 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 159.53 | Breakeven 104 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 160.54 | Breakeven 105 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 161.54 | Breakeven 106 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 162.54 | Breakeven 107 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 163.55 | Breakeven 108 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 164.55 | Breakeven 109 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 165.55 | Breakeven 110 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 170.57 | Breakeven 111 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 171.57 | Breakeven 112 | -0.00 | 0.00 | -0.00 | -0.5000 | -0.5000 |
| 174.58 | Breakeven 113 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 175.59 | Breakeven 114 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 176.59 | Breakeven 115 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 177.59 | Breakeven 116 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 178.60 | Breakeven 117 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 179.60 | Breakeven 118 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 180.60 | Breakeven 119 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 181.61 | Breakeven 120 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 182.61 | Breakeven 121 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 183.61 | Breakeven 122 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 184.62 | Breakeven 123 | 0.00 | 0.00 | 0.00 | 0.5000 | 0.5000 |
| 186.62 | Breakeven 124 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 187.63 | Breakeven 125 | -0.00 | 0.00 | -0.00 | -0.5000 | -0.5000 |
| 189.63 | Breakeven 126 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 191.64 | Breakeven 127 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 192.64 | Breakeven 128 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 193.65 | Breakeven 129 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 194.65 | Breakeven 130 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 195.65 | Breakeven 131 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 196.66 | Breakeven 132 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 197.66 | Breakeven 133 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 198.66 | Breakeven 134 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 199.67 | Breakeven 135 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 200.67 | Breakeven 136 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 201.67 | Breakeven 137 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 202.68 | Breakeven 138 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 203.68 | Breakeven 139 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 204.68 | Breakeven 140 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 205.69 | Breakeven 141 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 206.69 | Breakeven 142 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 207.69 | Breakeven 143 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 208.70 | Breakeven 144 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 209.70 | Breakeven 145 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 210.70 | Breakeven 146 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 211.71 | Breakeven 147 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 212.71 | Breakeven 148 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 213.71 | Breakeven 149 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 214.72 | Breakeven 150 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 215.72 | Breakeven 151 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 216.72 | Breakeven 152 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 217.73 | Breakeven 153 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 218.73 | Breakeven 154 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 219.73 | Breakeven 155 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 220.74 | Breakeven 156 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 221.74 | Breakeven 157 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 222.74 | Breakeven 158 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 223.75 | Breakeven 159 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 224.75 | Breakeven 160 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 225.75 | Breakeven 161 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 226.76 | Breakeven 162 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 227.76 | Breakeven 163 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 228.76 | Breakeven 164 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 229.77 | Breakeven 165 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 230.77 | Breakeven 166 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 231.77 | Breakeven 167 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 232.78 | Breakeven 168 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 233.78 | Breakeven 169 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 234.78 | Breakeven 170 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 235.79 | Breakeven 171 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 236.79 | Breakeven 172 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 237.79 | Breakeven 173 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 238.80 | Breakeven 174 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 239.80 | Breakeven 175 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 240.80 | Breakeven 176 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 241.81 | Breakeven 177 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 242.81 | Breakeven 178 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 243.81 | Breakeven 179 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 244.82 | Breakeven 180 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 245.82 | Breakeven 181 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 246.82 | Breakeven 182 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 247.83 | Breakeven 183 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 248.83 | Breakeven 184 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 249.83 | Breakeven 185 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 250.84 | Breakeven 186 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 251.84 | Breakeven 187 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 252.84 | Breakeven 188 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 253.85 | Breakeven 189 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 254.85 | Breakeven 190 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 255.85 | Breakeven 191 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 256.86 | Breakeven 192 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 257.86 | Breakeven 193 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 258.86 | Breakeven 194 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 259.87 | Breakeven 195 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 260.87 | Breakeven 196 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 261.87 | Breakeven 197 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 262.88 | Breakeven 198 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 263.88 | Breakeven 199 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 264.88 | Breakeven 200 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 265.89 | Breakeven 201 | -0.00 | 0.00 | -0.00 | -1.0000 | -1.0000 |
| 266.89 | Breakeven 202 | 0.00 | 0.00 | 0.00 | 1.0000 | 1.0000 |
| 269.90 | Breakeven 203 | -0.00 | 0.00 | -0.00 | -1.0000 | -1.0000 |
| 270.90 | Breakeven 204 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 272.41 | Breakeven 205 | 0.00 | 0.00 | 0.00 | 1.0000 | 1.0000 |
| 273.91 | Breakeven 206 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 274.92 | Breakeven 207 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 275.92 | Breakeven 208 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 276.92 | Breakeven 209 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 277.93 | Breakeven 210 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 278.93 | Breakeven 211 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 279.93 | Breakeven 212 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 280.94 | Breakeven 213 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 281.94 | Breakeven 214 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 282.94 | Breakeven 215 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 283.95 | Breakeven 216 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 284.95 | Breakeven 217 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 285.95 | Breakeven 218 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 286.96 | Breakeven 219 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 287.96 | Breakeven 220 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 288.96 | Breakeven 221 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 289.97 | Breakeven 222 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 290.97 | Breakeven 223 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 291.97 | Breakeven 224 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 292.98 | Breakeven 225 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 293.98 | Breakeven 226 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 294.98 | Breakeven 227 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 295.99 | Breakeven 228 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 296.99 | Breakeven 229 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 297.99 | Breakeven 230 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 299.00 | Breakeven 231 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| breakeven_1 | Breakeven 1 | 0.00 | -100.00% | 0.00 | 0.00 | 0.0000 |
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_2 | Breakeven 2 | 1.00 | -99.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_3 | Breakeven 3 | 2.01 | -97.99% | 0.00 | 0.00 | 0.0000 |
| breakeven_4 | Breakeven 4 | 3.01 | -96.99% | 0.00 | 0.00 | 0.0000 |
| breakeven_5 | Breakeven 5 | 4.01 | -95.99% | 0.00 | 0.00 | 0.0000 |
| breakeven_6 | Breakeven 6 | 5.02 | -94.98% | 0.00 | 0.00 | 0.0000 |
| breakeven_7 | Breakeven 7 | 6.02 | -93.98% | 0.00 | 0.00 | 0.0000 |
| breakeven_8 | Breakeven 8 | 7.02 | -92.98% | 0.00 | 0.00 | 0.0000 |
| breakeven_9 | Breakeven 9 | 8.03 | -91.97% | 0.00 | 0.00 | 0.0000 |
| breakeven_10 | Breakeven 10 | 10.03 | -89.97% | 0.00 | 0.00 | 0.0000 |
| breakeven_11 | Breakeven 11 | 12.04 | -87.96% | 0.00 | 0.00 | 0.0000 |
| breakeven_12 | Breakeven 12 | 14.05 | -85.95% | -0.00 | -0.00 | -0.5000 |
| breakeven_13 | Breakeven 13 | 16.05 | -83.95% | 0.00 | 0.00 | 0.0000 |
| breakeven_14 | Breakeven 14 | 17.06 | -82.94% | 0.00 | 0.00 | 0.0000 |
| breakeven_15 | Breakeven 15 | 18.06 | -81.94% | 0.00 | 0.00 | 0.0000 |
| breakeven_16 | Breakeven 16 | 19.06 | -80.94% | 0.00 | 0.00 | 0.0000 |
| breakeven_17 | Breakeven 17 | 20.07 | -79.93% | 0.00 | 0.00 | 0.0000 |
| breakeven_18 | Breakeven 18 | 21.07 | -78.93% | 0.00 | 0.00 | 0.0000 |
| breakeven_19 | Breakeven 19 | 22.07 | -77.93% | 0.00 | 0.00 | 0.0000 |
| breakeven_20 | Breakeven 20 | 23.08 | -76.92% | 0.00 | 0.00 | 0.0000 |
| breakeven_21 | Breakeven 21 | 24.08 | -75.92% | 0.00 | 0.00 | 0.0000 |
| breakeven_22 | Breakeven 22 | 25.08 | -74.92% | 0.00 | 0.00 | 0.0000 |
| breakeven_23 | Breakeven 23 | 26.09 | -73.91% | 0.00 | 0.00 | 0.0000 |
| breakeven_24 | Breakeven 24 | 34.11 | -65.89% | 0.00 | 0.00 | 0.0000 |
| breakeven_25 | Breakeven 25 | 35.12 | -64.88% | 0.00 | 0.00 | 0.0000 |
| breakeven_26 | Breakeven 26 | 36.12 | -63.88% | 0.00 | 0.00 | 0.0000 |
| breakeven_27 | Breakeven 27 | 37.12 | -62.88% | -0.00 | -0.00 | -0.5000 |
| breakeven_28 | Breakeven 28 | 38.13 | -61.87% | 0.00 | 0.00 | 0.5000 |
| breakeven_29 | Breakeven 29 | 39.13 | -60.87% | 0.00 | 0.00 | 0.0000 |
| breakeven_30 | Breakeven 30 | 41.14 | -58.86% | 0.00 | 0.00 | 0.0000 |
| breakeven_31 | Breakeven 31 | 42.14 | -57.86% | 0.00 | 0.00 | 0.0000 |
| breakeven_32 | Breakeven 32 | 43.14 | -56.86% | 0.00 | 0.00 | 0.5000 |
| breakeven_33 | Breakeven 33 | 44.15 | -55.85% | 0.00 | 0.00 | 0.0000 |
| breakeven_34 | Breakeven 34 | 45.15 | -54.85% | 0.00 | 0.00 | 0.0000 |
| breakeven_35 | Breakeven 35 | 46.15 | -53.85% | 0.00 | 0.00 | 0.0000 |
| breakeven_36 | Breakeven 36 | 47.16 | -52.84% | 0.00 | 0.00 | 0.0000 |
| breakeven_37 | Breakeven 37 | 48.16 | -51.84% | 0.00 | 0.00 | 0.0000 |
| breakeven_38 | Breakeven 38 | 49.16 | -50.84% | 0.00 | 0.00 | 0.0000 |
| breakeven_39 | Breakeven 39 | 52.68 | -47.32% | 0.00 | 0.00 | 0.2500 |
| breakeven_40 | Breakeven 40 | 55.18 | -44.82% | -0.00 | -0.00 | -0.2500 |
| breakeven_41 | Breakeven 41 | 57.19 | -42.81% | 0.00 | 0.00 | 0.0000 |
| breakeven_42 | Breakeven 42 | 58.19 | -41.81% | 0.00 | 0.00 | 0.0000 |
| breakeven_43 | Breakeven 43 | 59.20 | -40.80% | 0.00 | 0.00 | 0.0000 |
| breakeven_44 | Breakeven 44 | 60.20 | -39.80% | 0.00 | 0.00 | 0.0000 |
| breakeven_45 | Breakeven 45 | 61.20 | -38.80% | 0.00 | 0.00 | 0.0000 |
| breakeven_46 | Breakeven 46 | 62.21 | -37.79% | 0.00 | 0.00 | 0.0000 |
| breakeven_47 | Breakeven 47 | 63.21 | -36.79% | 0.00 | 0.00 | 0.0000 |
| breakeven_48 | Breakeven 48 | 64.21 | -35.79% | 0.00 | 0.00 | 0.0000 |
| breakeven_49 | Breakeven 49 | 65.22 | -34.78% | 0.00 | 0.00 | 0.0000 |
| breakeven_50 | Breakeven 50 | 66.22 | -33.78% | 0.00 | 0.00 | 0.0000 |
| breakeven_51 | Breakeven 51 | 67.22 | -32.78% | 0.00 | 0.00 | 0.0000 |
| breakeven_52 | Breakeven 52 | 68.23 | -31.77% | 0.00 | 0.00 | 0.0000 |
| breakeven_53 | Breakeven 53 | 69.23 | -30.77% | 0.00 | 0.00 | 0.0000 |
| breakeven_54 | Breakeven 54 | 70.23 | -29.77% | 0.00 | 0.00 | 0.0000 |
| breakeven_55 | Breakeven 55 | 71.74 | -28.26% | 0.00 | 0.00 | 0.1250 |
| breakeven_56 | Breakeven 56 | 73.24 | -26.76% | -0.00 | -0.00 | -0.1250 |
| breakeven_57 | Breakeven 57 | 75.25 | -24.75% | 0.00 | 0.00 | 0.2500 |
| breakeven_58 | Breakeven 58 | 78.26 | -21.74% | 0.00 | 0.00 | 0.1250 |
| breakeven_59 | Breakeven 59 | 82.27 | -17.73% | 0.00 | 0.00 | 0.0000 |
| breakeven_60 | Breakeven 60 | 84.28 | -15.72% | 0.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | 0.00 | 0.0312 |
| breakeven_61 | Breakeven 61 | 86.29 | -13.71% | 0.00 | 0.00 | 0.0312 |
| breakeven_62 | Breakeven 62 | 88.29 | -11.71% | 0.00 | 0.00 | 0.0000 |
| strike_1 | Breakeven 63 | 92.00 | -8.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_63 | Breakeven 63 | 92.00 | -8.00% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -0.00 | -0.00 | -0.0312 |
| breakeven_64 | Breakeven 64 | 103.34 | 3.34% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Breakeven 65 | 108.00 | 8.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_65 | Breakeven 65 | 108.00 | 8.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_66 | Breakeven 66 | 108.36 | 8.36% | 0.00 | 0.00 | 0.0000 |
| breakeven_67 | Breakeven 67 | 111.37 | 11.37% | 0.00 | 0.00 | 0.0000 |
| breakeven_68 | Breakeven 68 | 112.37 | 12.37% | 0.00 | 0.00 | 0.0000 |
| breakeven_69 | Breakeven 69 | 114.38 | 14.38% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 0.00 | 0.0625 |
| breakeven_70 | Breakeven 70 | 116.39 | 16.39% | -0.00 | -0.00 | -0.0625 |
| breakeven_71 | Breakeven 71 | 117.89 | 17.89% | 0.00 | 0.00 | 0.0000 |
| breakeven_72 | Breakeven 72 | 120.40 | 20.40% | 0.00 | 0.00 | 0.0000 |
| breakeven_73 | Breakeven 73 | 123.41 | 23.41% | 0.00 | 0.00 | 0.0000 |
| breakeven_74 | Breakeven 74 | 124.41 | 24.41% | 0.00 | 0.00 | 0.0000 |
| breakeven_75 | Breakeven 75 | 126.92 | 26.92% | 0.00 | 0.00 | 0.1250 |
| breakeven_76 | Breakeven 76 | 128.43 | 28.43% | 0.00 | 0.00 | 0.0000 |
| breakeven_77 | Breakeven 77 | 129.43 | 29.43% | 0.00 | 0.00 | 0.0000 |
| breakeven_78 | Breakeven 78 | 130.43 | 30.43% | 0.00 | 0.00 | 0.0000 |
| breakeven_79 | Breakeven 79 | 131.44 | 31.44% | 0.00 | 0.00 | 0.0000 |
| breakeven_80 | Breakeven 80 | 132.44 | 32.44% | 0.00 | 0.00 | 0.0000 |
| breakeven_81 | Breakeven 81 | 133.44 | 33.44% | 0.00 | 0.00 | 0.0000 |
| breakeven_82 | Breakeven 82 | 134.45 | 34.45% | 0.00 | 0.00 | 0.0000 |
| breakeven_83 | Breakeven 83 | 135.45 | 35.45% | 0.00 | 0.00 | 0.0000 |
| breakeven_84 | Breakeven 84 | 136.45 | 36.45% | 0.00 | 0.00 | 0.0000 |
| breakeven_85 | Breakeven 85 | 137.46 | 37.46% | 0.00 | 0.00 | 0.0000 |
| breakeven_86 | Breakeven 86 | 138.46 | 38.46% | 0.00 | 0.00 | 0.0000 |
| breakeven_87 | Breakeven 87 | 139.46 | 39.46% | 0.00 | 0.00 | 0.0000 |
| breakeven_88 | Breakeven 88 | 140.47 | 40.47% | 0.00 | 0.00 | 0.0000 |
| breakeven_89 | Breakeven 89 | 141.47 | 41.47% | 0.00 | 0.00 | 0.0000 |
| breakeven_90 | Breakeven 90 | 142.47 | 42.47% | 0.00 | 0.00 | 0.0000 |
| breakeven_91 | Breakeven 91 | 143.48 | 43.48% | -0.00 | -0.00 | -0.2500 |
| breakeven_92 | Breakeven 92 | 144.48 | 44.48% | 0.00 | 0.00 | 0.2500 |
| breakeven_93 | Breakeven 93 | 145.48 | 45.48% | 0.00 | 0.00 | 0.0000 |
| breakeven_94 | Breakeven 94 | 147.99 | 47.99% | -0.00 | -0.00 | -0.2500 |
| breakeven_95 | Breakeven 95 | 150.50 | 50.50% | 0.00 | 0.00 | 0.0000 |
| breakeven_96 | Breakeven 96 | 151.51 | 51.51% | 0.00 | 0.00 | 0.0000 |
| breakeven_97 | Breakeven 97 | 152.51 | 52.51% | 0.00 | 0.00 | 0.0000 |
| breakeven_98 | Breakeven 98 | 153.51 | 53.51% | 0.00 | 0.00 | 0.0000 |
| breakeven_99 | Breakeven 99 | 154.52 | 54.52% | 0.00 | 0.00 | 0.0000 |
| breakeven_100 | Breakeven 100 | 155.52 | 55.52% | 0.00 | 0.00 | 0.0000 |
| breakeven_101 | Breakeven 101 | 156.52 | 56.52% | 0.00 | 0.00 | 0.0000 |
| breakeven_102 | Breakeven 102 | 157.53 | 57.53% | 0.00 | 0.00 | 0.0000 |
| breakeven_103 | Breakeven 103 | 158.53 | 58.53% | 0.00 | 0.00 | 0.0000 |
| breakeven_104 | Breakeven 104 | 159.53 | 59.53% | 0.00 | 0.00 | 0.0000 |
| breakeven_105 | Breakeven 105 | 160.54 | 60.54% | 0.00 | 0.00 | 0.0000 |
| breakeven_106 | Breakeven 106 | 161.54 | 61.54% | 0.00 | 0.00 | 0.0000 |
| breakeven_107 | Breakeven 107 | 162.54 | 62.54% | 0.00 | 0.00 | 0.0000 |
| breakeven_108 | Breakeven 108 | 163.55 | 63.55% | 0.00 | 0.00 | 0.0000 |
| breakeven_109 | Breakeven 109 | 164.55 | 64.55% | 0.00 | 0.00 | 0.0000 |
| breakeven_110 | Breakeven 110 | 165.55 | 65.55% | 0.00 | 0.00 | 0.0000 |
| breakeven_111 | Breakeven 111 | 170.57 | 70.57% | 0.00 | 0.00 | 0.0000 |
| breakeven_112 | Breakeven 112 | 171.57 | 71.57% | -0.00 | -0.00 | -0.5000 |
| breakeven_113 | Breakeven 113 | 174.58 | 74.58% | 0.00 | 0.00 | 0.0000 |
| breakeven_114 | Breakeven 114 | 175.59 | 75.59% | 0.00 | 0.00 | 0.0000 |
| breakeven_115 | Breakeven 115 | 176.59 | 76.59% | 0.00 | 0.00 | 0.0000 |
| breakeven_116 | Breakeven 116 | 177.59 | 77.59% | 0.00 | 0.00 | 0.0000 |
| breakeven_117 | Breakeven 117 | 178.60 | 78.60% | 0.00 | 0.00 | 0.0000 |
| breakeven_118 | Breakeven 118 | 179.60 | 79.60% | 0.00 | 0.00 | 0.0000 |
| breakeven_119 | Breakeven 119 | 180.60 | 80.60% | 0.00 | 0.00 | 0.0000 |
| breakeven_120 | Breakeven 120 | 181.61 | 81.61% | 0.00 | 0.00 | 0.0000 |
| breakeven_121 | Breakeven 121 | 182.61 | 82.61% | 0.00 | 0.00 | 0.0000 |
| breakeven_122 | Breakeven 122 | 183.61 | 83.61% | 0.00 | 0.00 | 0.0000 |
| breakeven_123 | Breakeven 123 | 184.62 | 84.62% | 0.00 | 0.00 | 0.5000 |
| breakeven_124 | Breakeven 124 | 186.62 | 86.62% | 0.00 | 0.00 | 0.0000 |
| breakeven_125 | Breakeven 125 | 187.63 | 87.63% | -0.00 | -0.00 | -0.5000 |
| breakeven_126 | Breakeven 126 | 189.63 | 89.63% | 0.00 | 0.00 | 0.0000 |
| breakeven_127 | Breakeven 127 | 191.64 | 91.64% | 0.00 | 0.00 | 0.0000 |
| breakeven_128 | Breakeven 128 | 192.64 | 92.64% | 0.00 | 0.00 | 0.0000 |
| breakeven_129 | Breakeven 129 | 193.65 | 93.65% | 0.00 | 0.00 | 0.0000 |
| breakeven_130 | Breakeven 130 | 194.65 | 94.65% | 0.00 | 0.00 | 0.0000 |
| breakeven_131 | Breakeven 131 | 195.65 | 95.65% | 0.00 | 0.00 | 0.0000 |
| breakeven_132 | Breakeven 132 | 196.66 | 96.66% | 0.00 | 0.00 | 0.0000 |
| breakeven_133 | Breakeven 133 | 197.66 | 97.66% | 0.00 | 0.00 | 0.0000 |
| breakeven_134 | Breakeven 134 | 198.66 | 98.66% | 0.00 | 0.00 | 0.0000 |
| breakeven_135 | Breakeven 135 | 199.67 | 99.67% | 0.00 | 0.00 | 0.0000 |
| breakeven_136 | Breakeven 136 | 200.67 | 100.67% | 0.00 | 0.00 | 0.0000 |
| breakeven_137 | Breakeven 137 | 201.67 | 101.67% | 0.00 | 0.00 | 0.0000 |
| breakeven_138 | Breakeven 138 | 202.68 | 102.68% | 0.00 | 0.00 | 0.0000 |
| breakeven_139 | Breakeven 139 | 203.68 | 103.68% | 0.00 | 0.00 | 0.0000 |
| breakeven_140 | Breakeven 140 | 204.68 | 104.68% | 0.00 | 0.00 | 0.0000 |
| breakeven_141 | Breakeven 141 | 205.69 | 105.69% | 0.00 | 0.00 | 0.0000 |
| breakeven_142 | Breakeven 142 | 206.69 | 106.69% | 0.00 | 0.00 | 0.0000 |
| breakeven_143 | Breakeven 143 | 207.69 | 107.69% | 0.00 | 0.00 | 0.0000 |
| breakeven_144 | Breakeven 144 | 208.70 | 108.70% | 0.00 | 0.00 | 0.0000 |
| breakeven_145 | Breakeven 145 | 209.70 | 109.70% | 0.00 | 0.00 | 0.0000 |
| breakeven_146 | Breakeven 146 | 210.70 | 110.70% | 0.00 | 0.00 | 0.0000 |
| breakeven_147 | Breakeven 147 | 211.71 | 111.71% | 0.00 | 0.00 | 0.0000 |
| breakeven_148 | Breakeven 148 | 212.71 | 112.71% | 0.00 | 0.00 | 0.0000 |
| breakeven_149 | Breakeven 149 | 213.71 | 113.71% | 0.00 | 0.00 | 0.0000 |
| breakeven_150 | Breakeven 150 | 214.72 | 114.72% | 0.00 | 0.00 | 0.0000 |
| breakeven_151 | Breakeven 151 | 215.72 | 115.72% | 0.00 | 0.00 | 0.0000 |
| breakeven_152 | Breakeven 152 | 216.72 | 116.72% | 0.00 | 0.00 | 0.0000 |
| breakeven_153 | Breakeven 153 | 217.73 | 117.73% | 0.00 | 0.00 | 0.0000 |
| breakeven_154 | Breakeven 154 | 218.73 | 118.73% | 0.00 | 0.00 | 0.0000 |
| breakeven_155 | Breakeven 155 | 219.73 | 119.73% | 0.00 | 0.00 | 0.0000 |
| breakeven_156 | Breakeven 156 | 220.74 | 120.74% | 0.00 | 0.00 | 0.0000 |
| breakeven_157 | Breakeven 157 | 221.74 | 121.74% | 0.00 | 0.00 | 0.0000 |
| breakeven_158 | Breakeven 158 | 222.74 | 122.74% | 0.00 | 0.00 | 0.0000 |
| breakeven_159 | Breakeven 159 | 223.75 | 123.75% | 0.00 | 0.00 | 0.0000 |
| breakeven_160 | Breakeven 160 | 224.75 | 124.75% | 0.00 | 0.00 | 0.0000 |
| breakeven_161 | Breakeven 161 | 225.75 | 125.75% | 0.00 | 0.00 | 0.0000 |
| breakeven_162 | Breakeven 162 | 226.76 | 126.76% | 0.00 | 0.00 | 0.0000 |
| breakeven_163 | Breakeven 163 | 227.76 | 127.76% | 0.00 | 0.00 | 0.0000 |
| breakeven_164 | Breakeven 164 | 228.76 | 128.76% | 0.00 | 0.00 | 0.0000 |
| breakeven_165 | Breakeven 165 | 229.77 | 129.77% | 0.00 | 0.00 | 0.0000 |
| breakeven_166 | Breakeven 166 | 230.77 | 130.77% | 0.00 | 0.00 | 0.0000 |
| breakeven_167 | Breakeven 167 | 231.77 | 131.77% | 0.00 | 0.00 | 0.0000 |
| breakeven_168 | Breakeven 168 | 232.78 | 132.78% | 0.00 | 0.00 | 0.0000 |
| breakeven_169 | Breakeven 169 | 233.78 | 133.78% | 0.00 | 0.00 | 0.0000 |
| breakeven_170 | Breakeven 170 | 234.78 | 134.78% | 0.00 | 0.00 | 0.0000 |
| breakeven_171 | Breakeven 171 | 235.79 | 135.79% | 0.00 | 0.00 | 0.0000 |
| breakeven_172 | Breakeven 172 | 236.79 | 136.79% | 0.00 | 0.00 | 0.0000 |
| breakeven_173 | Breakeven 173 | 237.79 | 137.79% | 0.00 | 0.00 | 0.0000 |
| breakeven_174 | Breakeven 174 | 238.80 | 138.80% | 0.00 | 0.00 | 0.0000 |
| breakeven_175 | Breakeven 175 | 239.80 | 139.80% | 0.00 | 0.00 | 0.0000 |
| breakeven_176 | Breakeven 176 | 240.80 | 140.80% | 0.00 | 0.00 | 0.0000 |
| breakeven_177 | Breakeven 177 | 241.81 | 141.81% | 0.00 | 0.00 | 0.0000 |
| breakeven_178 | Breakeven 178 | 242.81 | 142.81% | 0.00 | 0.00 | 0.0000 |
| breakeven_179 | Breakeven 179 | 243.81 | 143.81% | 0.00 | 0.00 | 0.0000 |
| breakeven_180 | Breakeven 180 | 244.82 | 144.82% | 0.00 | 0.00 | 0.0000 |
| breakeven_181 | Breakeven 181 | 245.82 | 145.82% | 0.00 | 0.00 | 0.0000 |
| breakeven_182 | Breakeven 182 | 246.82 | 146.82% | 0.00 | 0.00 | 0.0000 |
| breakeven_183 | Breakeven 183 | 247.83 | 147.83% | 0.00 | 0.00 | 0.0000 |
| breakeven_184 | Breakeven 184 | 248.83 | 148.83% | 0.00 | 0.00 | 0.0000 |
| breakeven_185 | Breakeven 185 | 249.83 | 149.83% | 0.00 | 0.00 | 0.0000 |
| breakeven_186 | Breakeven 186 | 250.84 | 150.84% | 0.00 | 0.00 | 0.0000 |
| breakeven_187 | Breakeven 187 | 251.84 | 151.84% | 0.00 | 0.00 | 0.0000 |
| breakeven_188 | Breakeven 188 | 252.84 | 152.84% | 0.00 | 0.00 | 0.0000 |
| breakeven_189 | Breakeven 189 | 253.85 | 153.85% | 0.00 | 0.00 | 0.0000 |
| breakeven_190 | Breakeven 190 | 254.85 | 154.85% | 0.00 | 0.00 | 0.0000 |
| breakeven_191 | Breakeven 191 | 255.85 | 155.85% | 0.00 | 0.00 | 0.0000 |
| breakeven_192 | Breakeven 192 | 256.86 | 156.86% | 0.00 | 0.00 | 0.0000 |
| breakeven_193 | Breakeven 193 | 257.86 | 157.86% | 0.00 | 0.00 | 0.0000 |
| breakeven_194 | Breakeven 194 | 258.86 | 158.86% | 0.00 | 0.00 | 0.0000 |
| breakeven_195 | Breakeven 195 | 259.87 | 159.87% | 0.00 | 0.00 | 0.0000 |
| breakeven_196 | Breakeven 196 | 260.87 | 160.87% | 0.00 | 0.00 | 0.0000 |
| breakeven_197 | Breakeven 197 | 261.87 | 161.87% | 0.00 | 0.00 | 0.0000 |
| breakeven_198 | Breakeven 198 | 262.88 | 162.88% | 0.00 | 0.00 | 0.0000 |
| breakeven_199 | Breakeven 199 | 263.88 | 163.88% | 0.00 | 0.00 | 0.0000 |
| breakeven_200 | Breakeven 200 | 264.88 | 164.88% | 0.00 | 0.00 | 0.0000 |
| breakeven_201 | Breakeven 201 | 265.89 | 165.89% | -0.00 | -0.00 | -1.0000 |
| breakeven_202 | Breakeven 202 | 266.89 | 166.89% | 0.00 | 0.00 | 1.0000 |
| breakeven_203 | Breakeven 203 | 269.90 | 169.90% | -0.00 | -0.00 | -1.0000 |
| breakeven_204 | Breakeven 204 | 270.90 | 170.90% | 0.00 | 0.00 | 0.0000 |
| breakeven_205 | Breakeven 205 | 272.41 | 172.41% | 0.00 | 0.00 | 1.0000 |
| breakeven_206 | Breakeven 206 | 273.91 | 173.91% | 0.00 | 0.00 | 0.0000 |
| breakeven_207 | Breakeven 207 | 274.92 | 174.92% | 0.00 | 0.00 | 0.0000 |
| breakeven_208 | Breakeven 208 | 275.92 | 175.92% | 0.00 | 0.00 | 0.0000 |
| breakeven_209 | Breakeven 209 | 276.92 | 176.92% | 0.00 | 0.00 | 0.0000 |
| breakeven_210 | Breakeven 210 | 277.93 | 177.93% | 0.00 | 0.00 | 0.0000 |
| breakeven_211 | Breakeven 211 | 278.93 | 178.93% | 0.00 | 0.00 | 0.0000 |
| breakeven_212 | Breakeven 212 | 279.93 | 179.93% | 0.00 | 0.00 | 0.0000 |
| breakeven_213 | Breakeven 213 | 280.94 | 180.94% | 0.00 | 0.00 | 0.0000 |
| breakeven_214 | Breakeven 214 | 281.94 | 181.94% | 0.00 | 0.00 | 0.0000 |
| breakeven_215 | Breakeven 215 | 282.94 | 182.94% | 0.00 | 0.00 | 0.0000 |
| breakeven_216 | Breakeven 216 | 283.95 | 183.95% | 0.00 | 0.00 | 0.0000 |
| breakeven_217 | Breakeven 217 | 284.95 | 184.95% | 0.00 | 0.00 | 0.0000 |
| breakeven_218 | Breakeven 218 | 285.95 | 185.95% | 0.00 | 0.00 | 0.0000 |
| breakeven_219 | Breakeven 219 | 286.96 | 186.96% | 0.00 | 0.00 | 0.0000 |
| breakeven_220 | Breakeven 220 | 287.96 | 187.96% | 0.00 | 0.00 | 0.0000 |
| breakeven_221 | Breakeven 221 | 288.96 | 188.96% | 0.00 | 0.00 | 0.0000 |
| breakeven_222 | Breakeven 222 | 289.97 | 189.97% | 0.00 | 0.00 | 0.0000 |
| breakeven_223 | Breakeven 223 | 290.97 | 190.97% | 0.00 | 0.00 | 0.0000 |
| breakeven_224 | Breakeven 224 | 291.97 | 191.97% | 0.00 | 0.00 | 0.0000 |
| breakeven_225 | Breakeven 225 | 292.98 | 192.98% | 0.00 | 0.00 | 0.0000 |
| breakeven_226 | Breakeven 226 | 293.98 | 193.98% | 0.00 | 0.00 | 0.0000 |
| breakeven_227 | Breakeven 227 | 294.98 | 194.98% | 0.00 | 0.00 | 0.0000 |
| breakeven_228 | Breakeven 228 | 295.99 | 195.99% | 0.00 | 0.00 | 0.0000 |
| breakeven_229 | Breakeven 229 | 296.99 | 196.99% | 0.00 | 0.00 | 0.0000 |
| breakeven_230 | Breakeven 230 | 297.99 | 197.99% | 0.00 | 0.00 | 0.0000 |
| breakeven_231 | Breakeven 231 | 299.00 | 199.00% | 0.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 0.00 | 0.00 | 0.0000 |

---

### Long Box Spread (ID=47) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |
| 3 | PUT | Long 1 | 108.00 | 9.90 | 100 |
| 4 | PUT | Short 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [100.0]
- Options Max PnL: 0.0
- Options Min PnL: -0.0
- Combined Max PnL: 20000.0
- Combined Min PnL: -10000.0

**Net Premium:**

- Per Share: 16.0
- Total: 1600.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | -$0.00 | -$10,000.00 |
| Risk Reward | 1.00x | 2.00x |
| Capital Basis | $2,780.00 | $12,780.00 |
| Cost Credit | Debit $1,600.00 | Debit $1,600.00 |
| Pop | 47.9% | 47.9% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.47931
- Assignment Prob: 0.440281
- P(25% Max Profit): 0.0
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 0.00 | -1500.00 | -1500.00 | 0.0312 | -0.1500 |
| 92.00 | Lower Strike | 0.00 | -800.00 | -800.00 | 0.0000 | -0.0800 |
| 100.00 | Current Market Price | -0.00 | 0.00 | -0.00 | -0.0312 | -0.0000 |
| 108.00 | Upper Strike | 0.00 | 800.00 | 800.00 | 0.0000 | 0.0800 |
| 115.00 | Upside (15%) | 0.00 | 1500.00 | 1500.00 | 0.0625 | 0.1500 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -10000.00 | -0.7825 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | -1500.00 | -0.1500 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | -800.00 | -0.0800 |
| spot | Current Market Price | 100.00 | 0.00% | -0.00 | -0.00 | -0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | -0.00 | -0.00 | -0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 800.00 | 0.0800 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 1500.00 | 0.1500 |
| infinity | Stock to Infinity | — | — | 0.00 | 98000.00 | 7.6682 |

---

### Long Box Spread (ID=47) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |
| 3 | PUT | Long 1 | 108.00 | 9.90 | 100 |
| 4 | PUT | Short 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [50.0]
- Options Max PnL: 0.0
- Options Min PnL: -0.0
- Combined Max PnL: 25000.0
- Combined Min PnL: -5000.0

**Net Premium:**

- Per Share: 16.0
- Total: 1600.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | -$0.00 | -$5,000.00 |
| Risk Reward | 1.00x | 5.00x |
| Capital Basis | $2,780.00 | $7,780.00 |
| Cost Credit | Debit $1,600.00 | Debit $1,600.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.440281
- P(25% Max Profit): 0.0
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 85.00 | Downside (15%) | 0.00 | 3500.00 | 3500.00 | 0.0312 | 0.7000 |
| 92.00 | Lower Strike | 0.00 | 4200.00 | 4200.00 | 0.0000 | 0.8400 |
| 100.00 | Current Market Price | -0.00 | 5000.00 | 5000.00 | -0.0312 | 1.0000 |
| 108.00 | Upper Strike | 0.00 | 5800.00 | 5800.00 | 0.0000 | 1.1600 |
| 115.00 | Upside (15%) | 0.00 | 6500.00 | 6500.00 | 0.0625 | 1.3000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -5000.00 | -0.6427 |
| breakeven_1 | Breakeven 1 | 50.00 | -50.00% | 0.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | 3500.00 | 0.7000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | 4200.00 | 0.8400 |
| spot | Current Market Price | 100.00 | 0.00% | -0.00 | 5000.00 | 1.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 5800.00 | 1.1600 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 6500.00 | 1.3000 |
| infinity | Stock to Infinity | — | — | 0.00 | 103000.00 | 13.2391 |

---

### Long Box Spread (ID=47) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |
| 3 | PUT | Long 1 | 108.00 | 9.90 | 100 |
| 4 | PUT | Short 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [115.0]
- Options Max PnL: 0.0
- Options Min PnL: -0.0
- Combined Max PnL: 18500.0
- Combined Min PnL: -11500.0

**Net Premium:**

- Per Share: 16.0
- Total: 1600.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | -$0.00 | -$11,500.00 |
| Risk Reward | 1.00x | 1.61x |
| Capital Basis | $2,780.00 | $14,280.00 |
| Cost Credit | Debit $1,600.00 | Debit $1,600.00 |
| Pop | 8.1% | 8.1% |
| Margin Proxy | 2780.0 | — |

**Probabilities:**

- PoP (raw): 0.081123
- Assignment Prob: 0.440281
- P(25% Max Profit): 0.0
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 0.00 | -3000.00 | -3000.00 | 0.0312 | -0.2609 |
| 92.00 | Lower Strike | 0.00 | -2300.00 | -2300.00 | 0.0000 | -0.2000 |
| 100.00 | Current Market Price | -0.00 | -1500.00 | -1500.00 | -0.0312 | -0.1304 |
| 108.00 | Upper Strike | 0.00 | -700.00 | -700.00 | 0.0000 | -0.0609 |
| 115.00 | Upside (15%) | 0.00 | 0.00 | 0.00 | 0.0625 | 0.0000 |
| 115.00 | Upside (15%) | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -11500.00 | -0.8053 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | -3000.00 | -0.2609 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | -2300.00 | -0.2000 |
| spot | Current Market Price | 100.00 | 0.00% | -0.00 | -1500.00 | -0.1304 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | -700.00 | -0.0609 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 115.00 | 15.00% | 0.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 0.00 | 96500.00 | 6.7577 |

---

### Short Box Spread (ID=48) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |
| 3 | PUT | Short 1 | 108.00 | 9.90 | 100 |
| 4 | PUT | Long 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [0.0, 1.003344, 2.006689, 3.010033, 4.013378, 5.016722, 6.020067, 7.023411, 8.026756, 10.033445, 12.040134, 14.046823, 16.053512, 17.056856, 18.060201, 19.063545, 20.06689, 21.070234, 22.073579, 23.076923, 24.080268, 25.083612, 26.086957, 34.113712, 35.117057, 36.120401, 37.123746, 38.12709, 39.130435, 41.137124, 42.140468, 43.143813, 44.147157, 45.150502, 46.153846, 47.157191, 48.160535, 49.16388, 52.675585, 55.183946, 57.190635, 58.19398, 59.197324, 60.200669, 61.204013, 62.207358, 63.210702, 64.214047, 65.217391, 66.220736, 67.22408, 68.227425, 69.230769, 70.234114, 71.73913, 73.244147, 75.250836, 78.26087, 82.274247, 84.280936, 86.287625, 88.294314, 92.0, 103.344482, 108.0, 108.361204, 111.371237, 112.374582, 114.381271, 116.38796, 117.892977, 120.401338, 123.411371, 124.414716, 126.923077, 128.428094, 129.431438, 130.434783, 131.438127, 132.441472, 133.444816, 134.448161, 135.451505, 136.454849, 137.458194, 138.461538, 139.464883, 140.468227, 141.471572, 142.474916, 143.478261, 144.481605, 145.48495, 147.993311, 150.501672, 151.505017, 152.508361, 153.511706, 154.51505, 155.518395, 156.521739, 157.525084, 158.528428, 159.531773, 160.535117, 161.538462, 162.541806, 163.545151, 164.548495, 165.551839, 170.568562, 171.571906, 174.58194, 175.585284, 176.588629, 177.591973, 178.595318, 179.598662, 180.602007, 181.605351, 182.608696, 183.61204, 184.615385, 186.622074, 187.625418, 189.632107, 191.638796, 192.64214, 193.645485, 194.648829, 195.652174, 196.655518, 197.658863, 198.662207, 199.665552, 200.668896, 201.672241, 202.675585, 203.67893, 204.682274, 205.685619, 206.688963, 207.692308, 208.695652, 209.698997, 210.702341, 211.705686, 212.70903, 213.712375, 214.715719, 215.719064, 216.722408, 217.725753, 218.729097, 219.732441, 220.735786, 221.73913, 222.742475, 223.745819, 224.749164, 225.752508, 226.755853, 227.759197, 228.762542, 229.765886, 230.769231, 231.772575, 232.77592, 233.779264, 234.782609, 235.785953, 236.789298, 237.792642, 238.795987, 239.799331, 240.802676, 241.80602, 242.809365, 243.812709, 244.816054, 245.819398, 246.822742, 247.826087, 248.829431, 249.832776, 250.83612, 251.839465, 252.842809, 253.846154, 254.849498, 255.852843, 256.856187, 257.859532, 258.862876, 259.866221, 260.869565, 261.87291, 262.876254, 263.879599, 264.882943, 265.886288, 266.889632, 269.899666, 270.90301, 272.408027, 273.913043, 274.916388, 275.919732, 276.923077, 277.926421, 278.929766, 279.93311, 280.936455, 281.939799, 282.943144, 283.946488, 284.949833, 285.953177, 286.956522, 287.959866, 288.963211, 289.966555, 290.9699, 291.973244, 292.976589, 293.979933, 294.983278, 295.986622, 296.989967, 297.993311, 298.996656]
- Options Max PnL: 0.0
- Options Min PnL: -0.0
- Combined Max PnL: 0.0
- Combined Min PnL: -0.0

**Net Premium:**

- Per Share: -16.0
- Total: -1600.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | $0.00 |
| Max Loss | -$0.00 | -$0.00 |
| Risk Reward | 1.00x | 1.00x |
| Capital Basis | $1.00 | $1.00 |
| Cost Credit | Credit $1,600.00 | Credit $1,600.00 |
| Pop | 64.8% | 64.8% |
| Margin Proxy | 1.0 | — |

**Probabilities:**

- PoP (raw): 0.647643
- Assignment Prob: 1.0
- P(25% Max Profit): 1e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 0.00 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 1.00 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 2.01 | Breakeven 3 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 3.01 | Breakeven 4 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 4.01 | Breakeven 5 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 5.02 | Breakeven 6 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 6.02 | Breakeven 7 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 7.02 | Breakeven 8 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 8.03 | Breakeven 9 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 10.03 | Breakeven 10 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 12.04 | Breakeven 11 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 14.05 | Breakeven 12 | 0.00 | 0.00 | 0.00 | 0.5000 | 0.5000 |
| 16.05 | Breakeven 13 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 17.06 | Breakeven 14 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 18.06 | Breakeven 15 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 19.06 | Breakeven 16 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 20.07 | Breakeven 17 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 21.07 | Breakeven 18 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 22.07 | Breakeven 19 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 23.08 | Breakeven 20 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 24.08 | Breakeven 21 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 25.08 | Breakeven 22 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 26.09 | Breakeven 23 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 34.11 | Breakeven 24 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 35.12 | Breakeven 25 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 36.12 | Breakeven 26 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 37.12 | Breakeven 27 | 0.00 | 0.00 | 0.00 | 0.5000 | 0.5000 |
| 38.13 | Breakeven 28 | -0.00 | 0.00 | -0.00 | -0.5000 | -0.5000 |
| 39.13 | Breakeven 29 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 41.14 | Breakeven 30 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 42.14 | Breakeven 31 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 43.14 | Breakeven 32 | -0.00 | 0.00 | -0.00 | -0.5000 | -0.5000 |
| 44.15 | Breakeven 33 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 45.15 | Breakeven 34 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 46.15 | Breakeven 35 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 47.16 | Breakeven 36 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 48.16 | Breakeven 37 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 49.16 | Breakeven 38 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 52.68 | Breakeven 39 | -0.00 | 0.00 | -0.00 | -0.2500 | -0.2500 |
| 55.18 | Breakeven 40 | 0.00 | 0.00 | 0.00 | 0.2500 | 0.2500 |
| 57.19 | Breakeven 41 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 58.19 | Breakeven 42 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 59.20 | Breakeven 43 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 60.20 | Breakeven 44 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 61.20 | Breakeven 45 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 62.21 | Breakeven 46 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 63.21 | Breakeven 47 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 64.21 | Breakeven 48 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 65.22 | Breakeven 49 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 66.22 | Breakeven 50 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 67.22 | Breakeven 51 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 68.23 | Breakeven 52 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 69.23 | Breakeven 53 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 70.23 | Breakeven 54 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 71.74 | Breakeven 55 | -0.00 | 0.00 | -0.00 | -0.1250 | -0.1250 |
| 73.24 | Breakeven 56 | 0.00 | 0.00 | 0.00 | 0.1250 | 0.1250 |
| 75.25 | Breakeven 57 | -0.00 | 0.00 | -0.00 | -0.2500 | -0.2500 |
| 78.26 | Breakeven 58 | -0.00 | 0.00 | -0.00 | -0.1250 | -0.1250 |
| 82.27 | Breakeven 59 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 84.28 | Breakeven 60 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 85.00 | Downside (15%) | -0.00 | 0.00 | -0.00 | -0.0312 | -0.0312 |
| 86.29 | Breakeven 61 | -0.00 | 0.00 | -0.00 | -0.0312 | -0.0312 |
| 88.29 | Breakeven 62 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 92.00 | Breakeven 63 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0312 | 0.0312 |
| 103.34 | Breakeven 64 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Breakeven 65 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.36 | Breakeven 66 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 111.37 | Breakeven 67 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 112.37 | Breakeven 68 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 114.38 | Breakeven 69 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -0.00 | 0.00 | -0.00 | -0.0625 | -0.0625 |
| 116.39 | Breakeven 70 | 0.00 | 0.00 | 0.00 | 0.0625 | 0.0625 |
| 117.89 | Breakeven 71 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 120.40 | Breakeven 72 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 123.41 | Breakeven 73 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 124.41 | Breakeven 74 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 126.92 | Breakeven 75 | -0.00 | 0.00 | -0.00 | -0.1250 | -0.1250 |
| 128.43 | Breakeven 76 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 129.43 | Breakeven 77 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 130.43 | Breakeven 78 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 131.44 | Breakeven 79 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 132.44 | Breakeven 80 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 133.44 | Breakeven 81 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 134.45 | Breakeven 82 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 135.45 | Breakeven 83 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 136.45 | Breakeven 84 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 137.46 | Breakeven 85 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 138.46 | Breakeven 86 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 139.46 | Breakeven 87 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 140.47 | Breakeven 88 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 141.47 | Breakeven 89 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 142.47 | Breakeven 90 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 143.48 | Breakeven 91 | 0.00 | 0.00 | 0.00 | 0.2500 | 0.2500 |
| 144.48 | Breakeven 92 | -0.00 | 0.00 | -0.00 | -0.2500 | -0.2500 |
| 145.48 | Breakeven 93 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 147.99 | Breakeven 94 | 0.00 | 0.00 | 0.00 | 0.2500 | 0.2500 |
| 150.50 | Breakeven 95 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 151.51 | Breakeven 96 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 152.51 | Breakeven 97 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 153.51 | Breakeven 98 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 154.52 | Breakeven 99 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 155.52 | Breakeven 100 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 156.52 | Breakeven 101 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 157.53 | Breakeven 102 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 158.53 | Breakeven 103 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 159.53 | Breakeven 104 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 160.54 | Breakeven 105 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 161.54 | Breakeven 106 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 162.54 | Breakeven 107 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 163.55 | Breakeven 108 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 164.55 | Breakeven 109 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 165.55 | Breakeven 110 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 170.57 | Breakeven 111 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 171.57 | Breakeven 112 | 0.00 | 0.00 | 0.00 | 0.5000 | 0.5000 |
| 174.58 | Breakeven 113 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 175.59 | Breakeven 114 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 176.59 | Breakeven 115 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 177.59 | Breakeven 116 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 178.60 | Breakeven 117 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 179.60 | Breakeven 118 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 180.60 | Breakeven 119 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 181.61 | Breakeven 120 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 182.61 | Breakeven 121 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 183.61 | Breakeven 122 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 184.62 | Breakeven 123 | -0.00 | 0.00 | -0.00 | -0.5000 | -0.5000 |
| 186.62 | Breakeven 124 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 187.63 | Breakeven 125 | 0.00 | 0.00 | 0.00 | 0.5000 | 0.5000 |
| 189.63 | Breakeven 126 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 191.64 | Breakeven 127 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 192.64 | Breakeven 128 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 193.65 | Breakeven 129 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 194.65 | Breakeven 130 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 195.65 | Breakeven 131 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 196.66 | Breakeven 132 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 197.66 | Breakeven 133 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 198.66 | Breakeven 134 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 199.67 | Breakeven 135 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 200.67 | Breakeven 136 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 201.67 | Breakeven 137 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 202.68 | Breakeven 138 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 203.68 | Breakeven 139 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 204.68 | Breakeven 140 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 205.69 | Breakeven 141 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 206.69 | Breakeven 142 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 207.69 | Breakeven 143 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 208.70 | Breakeven 144 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 209.70 | Breakeven 145 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 210.70 | Breakeven 146 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 211.71 | Breakeven 147 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 212.71 | Breakeven 148 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 213.71 | Breakeven 149 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 214.72 | Breakeven 150 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 215.72 | Breakeven 151 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 216.72 | Breakeven 152 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 217.73 | Breakeven 153 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 218.73 | Breakeven 154 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 219.73 | Breakeven 155 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 220.74 | Breakeven 156 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 221.74 | Breakeven 157 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 222.74 | Breakeven 158 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 223.75 | Breakeven 159 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 224.75 | Breakeven 160 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 225.75 | Breakeven 161 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 226.76 | Breakeven 162 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 227.76 | Breakeven 163 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 228.76 | Breakeven 164 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 229.77 | Breakeven 165 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 230.77 | Breakeven 166 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 231.77 | Breakeven 167 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 232.78 | Breakeven 168 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 233.78 | Breakeven 169 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 234.78 | Breakeven 170 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 235.79 | Breakeven 171 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 236.79 | Breakeven 172 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 237.79 | Breakeven 173 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 238.80 | Breakeven 174 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 239.80 | Breakeven 175 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 240.80 | Breakeven 176 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 241.81 | Breakeven 177 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 242.81 | Breakeven 178 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 243.81 | Breakeven 179 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 244.82 | Breakeven 180 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 245.82 | Breakeven 181 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 246.82 | Breakeven 182 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 247.83 | Breakeven 183 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 248.83 | Breakeven 184 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 249.83 | Breakeven 185 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 250.84 | Breakeven 186 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 251.84 | Breakeven 187 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 252.84 | Breakeven 188 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 253.85 | Breakeven 189 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 254.85 | Breakeven 190 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 255.85 | Breakeven 191 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 256.86 | Breakeven 192 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 257.86 | Breakeven 193 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 258.86 | Breakeven 194 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 259.87 | Breakeven 195 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 260.87 | Breakeven 196 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 261.87 | Breakeven 197 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 262.88 | Breakeven 198 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 263.88 | Breakeven 199 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 264.88 | Breakeven 200 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 265.89 | Breakeven 201 | 0.00 | 0.00 | 0.00 | 1.0000 | 1.0000 |
| 266.89 | Breakeven 202 | -0.00 | 0.00 | -0.00 | -1.0000 | -1.0000 |
| 269.90 | Breakeven 203 | 0.00 | 0.00 | 0.00 | 1.0000 | 1.0000 |
| 270.90 | Breakeven 204 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 272.41 | Breakeven 205 | -0.00 | 0.00 | -0.00 | -1.0000 | -1.0000 |
| 273.91 | Breakeven 206 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 274.92 | Breakeven 207 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 275.92 | Breakeven 208 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 276.92 | Breakeven 209 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 277.93 | Breakeven 210 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 278.93 | Breakeven 211 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 279.93 | Breakeven 212 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 280.94 | Breakeven 213 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 281.94 | Breakeven 214 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 282.94 | Breakeven 215 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 283.95 | Breakeven 216 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 284.95 | Breakeven 217 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 285.95 | Breakeven 218 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 286.96 | Breakeven 219 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 287.96 | Breakeven 220 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 288.96 | Breakeven 221 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 289.97 | Breakeven 222 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 290.97 | Breakeven 223 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 291.97 | Breakeven 224 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 292.98 | Breakeven 225 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 293.98 | Breakeven 226 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 294.98 | Breakeven 227 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 295.99 | Breakeven 228 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 296.99 | Breakeven 229 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 297.99 | Breakeven 230 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 299.00 | Breakeven 231 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| breakeven_1 | Breakeven 1 | 0.00 | -100.00% | 0.00 | 0.00 | 0.0000 |
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_2 | Breakeven 2 | 1.00 | -99.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_3 | Breakeven 3 | 2.01 | -97.99% | 0.00 | 0.00 | 0.0000 |
| breakeven_4 | Breakeven 4 | 3.01 | -96.99% | 0.00 | 0.00 | 0.0000 |
| breakeven_5 | Breakeven 5 | 4.01 | -95.99% | 0.00 | 0.00 | 0.0000 |
| breakeven_6 | Breakeven 6 | 5.02 | -94.98% | 0.00 | 0.00 | 0.0000 |
| breakeven_7 | Breakeven 7 | 6.02 | -93.98% | 0.00 | 0.00 | 0.0000 |
| breakeven_8 | Breakeven 8 | 7.02 | -92.98% | 0.00 | 0.00 | 0.0000 |
| breakeven_9 | Breakeven 9 | 8.03 | -91.97% | 0.00 | 0.00 | 0.0000 |
| breakeven_10 | Breakeven 10 | 10.03 | -89.97% | 0.00 | 0.00 | 0.0000 |
| breakeven_11 | Breakeven 11 | 12.04 | -87.96% | 0.00 | 0.00 | 0.0000 |
| breakeven_12 | Breakeven 12 | 14.05 | -85.95% | 0.00 | 0.00 | 0.5000 |
| breakeven_13 | Breakeven 13 | 16.05 | -83.95% | 0.00 | 0.00 | 0.0000 |
| breakeven_14 | Breakeven 14 | 17.06 | -82.94% | 0.00 | 0.00 | 0.0000 |
| breakeven_15 | Breakeven 15 | 18.06 | -81.94% | 0.00 | 0.00 | 0.0000 |
| breakeven_16 | Breakeven 16 | 19.06 | -80.94% | 0.00 | 0.00 | 0.0000 |
| breakeven_17 | Breakeven 17 | 20.07 | -79.93% | 0.00 | 0.00 | 0.0000 |
| breakeven_18 | Breakeven 18 | 21.07 | -78.93% | 0.00 | 0.00 | 0.0000 |
| breakeven_19 | Breakeven 19 | 22.07 | -77.93% | 0.00 | 0.00 | 0.0000 |
| breakeven_20 | Breakeven 20 | 23.08 | -76.92% | 0.00 | 0.00 | 0.0000 |
| breakeven_21 | Breakeven 21 | 24.08 | -75.92% | 0.00 | 0.00 | 0.0000 |
| breakeven_22 | Breakeven 22 | 25.08 | -74.92% | 0.00 | 0.00 | 0.0000 |
| breakeven_23 | Breakeven 23 | 26.09 | -73.91% | 0.00 | 0.00 | 0.0000 |
| breakeven_24 | Breakeven 24 | 34.11 | -65.89% | 0.00 | 0.00 | 0.0000 |
| breakeven_25 | Breakeven 25 | 35.12 | -64.88% | 0.00 | 0.00 | 0.0000 |
| breakeven_26 | Breakeven 26 | 36.12 | -63.88% | 0.00 | 0.00 | 0.0000 |
| breakeven_27 | Breakeven 27 | 37.12 | -62.88% | 0.00 | 0.00 | 0.5000 |
| breakeven_28 | Breakeven 28 | 38.13 | -61.87% | -0.00 | -0.00 | -0.5000 |
| breakeven_29 | Breakeven 29 | 39.13 | -60.87% | 0.00 | 0.00 | 0.0000 |
| breakeven_30 | Breakeven 30 | 41.14 | -58.86% | 0.00 | 0.00 | 0.0000 |
| breakeven_31 | Breakeven 31 | 42.14 | -57.86% | 0.00 | 0.00 | 0.0000 |
| breakeven_32 | Breakeven 32 | 43.14 | -56.86% | -0.00 | -0.00 | -0.5000 |
| breakeven_33 | Breakeven 33 | 44.15 | -55.85% | 0.00 | 0.00 | 0.0000 |
| breakeven_34 | Breakeven 34 | 45.15 | -54.85% | 0.00 | 0.00 | 0.0000 |
| breakeven_35 | Breakeven 35 | 46.15 | -53.85% | 0.00 | 0.00 | 0.0000 |
| breakeven_36 | Breakeven 36 | 47.16 | -52.84% | 0.00 | 0.00 | 0.0000 |
| breakeven_37 | Breakeven 37 | 48.16 | -51.84% | 0.00 | 0.00 | 0.0000 |
| breakeven_38 | Breakeven 38 | 49.16 | -50.84% | 0.00 | 0.00 | 0.0000 |
| breakeven_39 | Breakeven 39 | 52.68 | -47.32% | -0.00 | -0.00 | -0.2500 |
| breakeven_40 | Breakeven 40 | 55.18 | -44.82% | 0.00 | 0.00 | 0.2500 |
| breakeven_41 | Breakeven 41 | 57.19 | -42.81% | 0.00 | 0.00 | 0.0000 |
| breakeven_42 | Breakeven 42 | 58.19 | -41.81% | 0.00 | 0.00 | 0.0000 |
| breakeven_43 | Breakeven 43 | 59.20 | -40.80% | 0.00 | 0.00 | 0.0000 |
| breakeven_44 | Breakeven 44 | 60.20 | -39.80% | 0.00 | 0.00 | 0.0000 |
| breakeven_45 | Breakeven 45 | 61.20 | -38.80% | 0.00 | 0.00 | 0.0000 |
| breakeven_46 | Breakeven 46 | 62.21 | -37.79% | 0.00 | 0.00 | 0.0000 |
| breakeven_47 | Breakeven 47 | 63.21 | -36.79% | 0.00 | 0.00 | 0.0000 |
| breakeven_48 | Breakeven 48 | 64.21 | -35.79% | 0.00 | 0.00 | 0.0000 |
| breakeven_49 | Breakeven 49 | 65.22 | -34.78% | 0.00 | 0.00 | 0.0000 |
| breakeven_50 | Breakeven 50 | 66.22 | -33.78% | 0.00 | 0.00 | 0.0000 |
| breakeven_51 | Breakeven 51 | 67.22 | -32.78% | 0.00 | 0.00 | 0.0000 |
| breakeven_52 | Breakeven 52 | 68.23 | -31.77% | 0.00 | 0.00 | 0.0000 |
| breakeven_53 | Breakeven 53 | 69.23 | -30.77% | 0.00 | 0.00 | 0.0000 |
| breakeven_54 | Breakeven 54 | 70.23 | -29.77% | 0.00 | 0.00 | 0.0000 |
| breakeven_55 | Breakeven 55 | 71.74 | -28.26% | -0.00 | -0.00 | -0.1250 |
| breakeven_56 | Breakeven 56 | 73.24 | -26.76% | 0.00 | 0.00 | 0.1250 |
| breakeven_57 | Breakeven 57 | 75.25 | -24.75% | -0.00 | -0.00 | -0.2500 |
| breakeven_58 | Breakeven 58 | 78.26 | -21.74% | -0.00 | -0.00 | -0.1250 |
| breakeven_59 | Breakeven 59 | 82.27 | -17.73% | 0.00 | 0.00 | 0.0000 |
| breakeven_60 | Breakeven 60 | 84.28 | -15.72% | 0.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -0.00 | -0.00 | -0.0312 |
| breakeven_61 | Breakeven 61 | 86.29 | -13.71% | -0.00 | -0.00 | -0.0312 |
| breakeven_62 | Breakeven 62 | 88.29 | -11.71% | 0.00 | 0.00 | 0.0000 |
| strike_1 | Breakeven 63 | 92.00 | -8.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_63 | Breakeven 63 | 92.00 | -8.00% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0312 |
| breakeven_64 | Breakeven 64 | 103.34 | 3.34% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Breakeven 65 | 108.00 | 8.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_65 | Breakeven 65 | 108.00 | 8.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_66 | Breakeven 66 | 108.36 | 8.36% | 0.00 | 0.00 | 0.0000 |
| breakeven_67 | Breakeven 67 | 111.37 | 11.37% | 0.00 | 0.00 | 0.0000 |
| breakeven_68 | Breakeven 68 | 112.37 | 12.37% | 0.00 | 0.00 | 0.0000 |
| breakeven_69 | Breakeven 69 | 114.38 | 14.38% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -0.00 | -0.00 | -0.0625 |
| breakeven_70 | Breakeven 70 | 116.39 | 16.39% | 0.00 | 0.00 | 0.0625 |
| breakeven_71 | Breakeven 71 | 117.89 | 17.89% | 0.00 | 0.00 | 0.0000 |
| breakeven_72 | Breakeven 72 | 120.40 | 20.40% | 0.00 | 0.00 | 0.0000 |
| breakeven_73 | Breakeven 73 | 123.41 | 23.41% | 0.00 | 0.00 | 0.0000 |
| breakeven_74 | Breakeven 74 | 124.41 | 24.41% | 0.00 | 0.00 | 0.0000 |
| breakeven_75 | Breakeven 75 | 126.92 | 26.92% | -0.00 | -0.00 | -0.1250 |
| breakeven_76 | Breakeven 76 | 128.43 | 28.43% | 0.00 | 0.00 | 0.0000 |
| breakeven_77 | Breakeven 77 | 129.43 | 29.43% | 0.00 | 0.00 | 0.0000 |
| breakeven_78 | Breakeven 78 | 130.43 | 30.43% | 0.00 | 0.00 | 0.0000 |
| breakeven_79 | Breakeven 79 | 131.44 | 31.44% | 0.00 | 0.00 | 0.0000 |
| breakeven_80 | Breakeven 80 | 132.44 | 32.44% | 0.00 | 0.00 | 0.0000 |
| breakeven_81 | Breakeven 81 | 133.44 | 33.44% | 0.00 | 0.00 | 0.0000 |
| breakeven_82 | Breakeven 82 | 134.45 | 34.45% | 0.00 | 0.00 | 0.0000 |
| breakeven_83 | Breakeven 83 | 135.45 | 35.45% | 0.00 | 0.00 | 0.0000 |
| breakeven_84 | Breakeven 84 | 136.45 | 36.45% | 0.00 | 0.00 | 0.0000 |
| breakeven_85 | Breakeven 85 | 137.46 | 37.46% | 0.00 | 0.00 | 0.0000 |
| breakeven_86 | Breakeven 86 | 138.46 | 38.46% | 0.00 | 0.00 | 0.0000 |
| breakeven_87 | Breakeven 87 | 139.46 | 39.46% | 0.00 | 0.00 | 0.0000 |
| breakeven_88 | Breakeven 88 | 140.47 | 40.47% | 0.00 | 0.00 | 0.0000 |
| breakeven_89 | Breakeven 89 | 141.47 | 41.47% | 0.00 | 0.00 | 0.0000 |
| breakeven_90 | Breakeven 90 | 142.47 | 42.47% | 0.00 | 0.00 | 0.0000 |
| breakeven_91 | Breakeven 91 | 143.48 | 43.48% | 0.00 | 0.00 | 0.2500 |
| breakeven_92 | Breakeven 92 | 144.48 | 44.48% | -0.00 | -0.00 | -0.2500 |
| breakeven_93 | Breakeven 93 | 145.48 | 45.48% | 0.00 | 0.00 | 0.0000 |
| breakeven_94 | Breakeven 94 | 147.99 | 47.99% | 0.00 | 0.00 | 0.2500 |
| breakeven_95 | Breakeven 95 | 150.50 | 50.50% | 0.00 | 0.00 | 0.0000 |
| breakeven_96 | Breakeven 96 | 151.51 | 51.51% | 0.00 | 0.00 | 0.0000 |
| breakeven_97 | Breakeven 97 | 152.51 | 52.51% | 0.00 | 0.00 | 0.0000 |
| breakeven_98 | Breakeven 98 | 153.51 | 53.51% | 0.00 | 0.00 | 0.0000 |
| breakeven_99 | Breakeven 99 | 154.52 | 54.52% | 0.00 | 0.00 | 0.0000 |
| breakeven_100 | Breakeven 100 | 155.52 | 55.52% | 0.00 | 0.00 | 0.0000 |
| breakeven_101 | Breakeven 101 | 156.52 | 56.52% | 0.00 | 0.00 | 0.0000 |
| breakeven_102 | Breakeven 102 | 157.53 | 57.53% | 0.00 | 0.00 | 0.0000 |
| breakeven_103 | Breakeven 103 | 158.53 | 58.53% | 0.00 | 0.00 | 0.0000 |
| breakeven_104 | Breakeven 104 | 159.53 | 59.53% | 0.00 | 0.00 | 0.0000 |
| breakeven_105 | Breakeven 105 | 160.54 | 60.54% | 0.00 | 0.00 | 0.0000 |
| breakeven_106 | Breakeven 106 | 161.54 | 61.54% | 0.00 | 0.00 | 0.0000 |
| breakeven_107 | Breakeven 107 | 162.54 | 62.54% | 0.00 | 0.00 | 0.0000 |
| breakeven_108 | Breakeven 108 | 163.55 | 63.55% | 0.00 | 0.00 | 0.0000 |
| breakeven_109 | Breakeven 109 | 164.55 | 64.55% | 0.00 | 0.00 | 0.0000 |
| breakeven_110 | Breakeven 110 | 165.55 | 65.55% | 0.00 | 0.00 | 0.0000 |
| breakeven_111 | Breakeven 111 | 170.57 | 70.57% | 0.00 | 0.00 | 0.0000 |
| breakeven_112 | Breakeven 112 | 171.57 | 71.57% | 0.00 | 0.00 | 0.5000 |
| breakeven_113 | Breakeven 113 | 174.58 | 74.58% | 0.00 | 0.00 | 0.0000 |
| breakeven_114 | Breakeven 114 | 175.59 | 75.59% | 0.00 | 0.00 | 0.0000 |
| breakeven_115 | Breakeven 115 | 176.59 | 76.59% | 0.00 | 0.00 | 0.0000 |
| breakeven_116 | Breakeven 116 | 177.59 | 77.59% | 0.00 | 0.00 | 0.0000 |
| breakeven_117 | Breakeven 117 | 178.60 | 78.60% | 0.00 | 0.00 | 0.0000 |
| breakeven_118 | Breakeven 118 | 179.60 | 79.60% | 0.00 | 0.00 | 0.0000 |
| breakeven_119 | Breakeven 119 | 180.60 | 80.60% | 0.00 | 0.00 | 0.0000 |
| breakeven_120 | Breakeven 120 | 181.61 | 81.61% | 0.00 | 0.00 | 0.0000 |
| breakeven_121 | Breakeven 121 | 182.61 | 82.61% | 0.00 | 0.00 | 0.0000 |
| breakeven_122 | Breakeven 122 | 183.61 | 83.61% | 0.00 | 0.00 | 0.0000 |
| breakeven_123 | Breakeven 123 | 184.62 | 84.62% | -0.00 | -0.00 | -0.5000 |
| breakeven_124 | Breakeven 124 | 186.62 | 86.62% | 0.00 | 0.00 | 0.0000 |
| breakeven_125 | Breakeven 125 | 187.63 | 87.63% | 0.00 | 0.00 | 0.5000 |
| breakeven_126 | Breakeven 126 | 189.63 | 89.63% | 0.00 | 0.00 | 0.0000 |
| breakeven_127 | Breakeven 127 | 191.64 | 91.64% | 0.00 | 0.00 | 0.0000 |
| breakeven_128 | Breakeven 128 | 192.64 | 92.64% | 0.00 | 0.00 | 0.0000 |
| breakeven_129 | Breakeven 129 | 193.65 | 93.65% | 0.00 | 0.00 | 0.0000 |
| breakeven_130 | Breakeven 130 | 194.65 | 94.65% | 0.00 | 0.00 | 0.0000 |
| breakeven_131 | Breakeven 131 | 195.65 | 95.65% | 0.00 | 0.00 | 0.0000 |
| breakeven_132 | Breakeven 132 | 196.66 | 96.66% | 0.00 | 0.00 | 0.0000 |
| breakeven_133 | Breakeven 133 | 197.66 | 97.66% | 0.00 | 0.00 | 0.0000 |
| breakeven_134 | Breakeven 134 | 198.66 | 98.66% | 0.00 | 0.00 | 0.0000 |
| breakeven_135 | Breakeven 135 | 199.67 | 99.67% | 0.00 | 0.00 | 0.0000 |
| breakeven_136 | Breakeven 136 | 200.67 | 100.67% | 0.00 | 0.00 | 0.0000 |
| breakeven_137 | Breakeven 137 | 201.67 | 101.67% | 0.00 | 0.00 | 0.0000 |
| breakeven_138 | Breakeven 138 | 202.68 | 102.68% | 0.00 | 0.00 | 0.0000 |
| breakeven_139 | Breakeven 139 | 203.68 | 103.68% | 0.00 | 0.00 | 0.0000 |
| breakeven_140 | Breakeven 140 | 204.68 | 104.68% | 0.00 | 0.00 | 0.0000 |
| breakeven_141 | Breakeven 141 | 205.69 | 105.69% | 0.00 | 0.00 | 0.0000 |
| breakeven_142 | Breakeven 142 | 206.69 | 106.69% | 0.00 | 0.00 | 0.0000 |
| breakeven_143 | Breakeven 143 | 207.69 | 107.69% | 0.00 | 0.00 | 0.0000 |
| breakeven_144 | Breakeven 144 | 208.70 | 108.70% | 0.00 | 0.00 | 0.0000 |
| breakeven_145 | Breakeven 145 | 209.70 | 109.70% | 0.00 | 0.00 | 0.0000 |
| breakeven_146 | Breakeven 146 | 210.70 | 110.70% | 0.00 | 0.00 | 0.0000 |
| breakeven_147 | Breakeven 147 | 211.71 | 111.71% | 0.00 | 0.00 | 0.0000 |
| breakeven_148 | Breakeven 148 | 212.71 | 112.71% | 0.00 | 0.00 | 0.0000 |
| breakeven_149 | Breakeven 149 | 213.71 | 113.71% | 0.00 | 0.00 | 0.0000 |
| breakeven_150 | Breakeven 150 | 214.72 | 114.72% | 0.00 | 0.00 | 0.0000 |
| breakeven_151 | Breakeven 151 | 215.72 | 115.72% | 0.00 | 0.00 | 0.0000 |
| breakeven_152 | Breakeven 152 | 216.72 | 116.72% | 0.00 | 0.00 | 0.0000 |
| breakeven_153 | Breakeven 153 | 217.73 | 117.73% | 0.00 | 0.00 | 0.0000 |
| breakeven_154 | Breakeven 154 | 218.73 | 118.73% | 0.00 | 0.00 | 0.0000 |
| breakeven_155 | Breakeven 155 | 219.73 | 119.73% | 0.00 | 0.00 | 0.0000 |
| breakeven_156 | Breakeven 156 | 220.74 | 120.74% | 0.00 | 0.00 | 0.0000 |
| breakeven_157 | Breakeven 157 | 221.74 | 121.74% | 0.00 | 0.00 | 0.0000 |
| breakeven_158 | Breakeven 158 | 222.74 | 122.74% | 0.00 | 0.00 | 0.0000 |
| breakeven_159 | Breakeven 159 | 223.75 | 123.75% | 0.00 | 0.00 | 0.0000 |
| breakeven_160 | Breakeven 160 | 224.75 | 124.75% | 0.00 | 0.00 | 0.0000 |
| breakeven_161 | Breakeven 161 | 225.75 | 125.75% | 0.00 | 0.00 | 0.0000 |
| breakeven_162 | Breakeven 162 | 226.76 | 126.76% | 0.00 | 0.00 | 0.0000 |
| breakeven_163 | Breakeven 163 | 227.76 | 127.76% | 0.00 | 0.00 | 0.0000 |
| breakeven_164 | Breakeven 164 | 228.76 | 128.76% | 0.00 | 0.00 | 0.0000 |
| breakeven_165 | Breakeven 165 | 229.77 | 129.77% | 0.00 | 0.00 | 0.0000 |
| breakeven_166 | Breakeven 166 | 230.77 | 130.77% | 0.00 | 0.00 | 0.0000 |
| breakeven_167 | Breakeven 167 | 231.77 | 131.77% | 0.00 | 0.00 | 0.0000 |
| breakeven_168 | Breakeven 168 | 232.78 | 132.78% | 0.00 | 0.00 | 0.0000 |
| breakeven_169 | Breakeven 169 | 233.78 | 133.78% | 0.00 | 0.00 | 0.0000 |
| breakeven_170 | Breakeven 170 | 234.78 | 134.78% | 0.00 | 0.00 | 0.0000 |
| breakeven_171 | Breakeven 171 | 235.79 | 135.79% | 0.00 | 0.00 | 0.0000 |
| breakeven_172 | Breakeven 172 | 236.79 | 136.79% | 0.00 | 0.00 | 0.0000 |
| breakeven_173 | Breakeven 173 | 237.79 | 137.79% | 0.00 | 0.00 | 0.0000 |
| breakeven_174 | Breakeven 174 | 238.80 | 138.80% | 0.00 | 0.00 | 0.0000 |
| breakeven_175 | Breakeven 175 | 239.80 | 139.80% | 0.00 | 0.00 | 0.0000 |
| breakeven_176 | Breakeven 176 | 240.80 | 140.80% | 0.00 | 0.00 | 0.0000 |
| breakeven_177 | Breakeven 177 | 241.81 | 141.81% | 0.00 | 0.00 | 0.0000 |
| breakeven_178 | Breakeven 178 | 242.81 | 142.81% | 0.00 | 0.00 | 0.0000 |
| breakeven_179 | Breakeven 179 | 243.81 | 143.81% | 0.00 | 0.00 | 0.0000 |
| breakeven_180 | Breakeven 180 | 244.82 | 144.82% | 0.00 | 0.00 | 0.0000 |
| breakeven_181 | Breakeven 181 | 245.82 | 145.82% | 0.00 | 0.00 | 0.0000 |
| breakeven_182 | Breakeven 182 | 246.82 | 146.82% | 0.00 | 0.00 | 0.0000 |
| breakeven_183 | Breakeven 183 | 247.83 | 147.83% | 0.00 | 0.00 | 0.0000 |
| breakeven_184 | Breakeven 184 | 248.83 | 148.83% | 0.00 | 0.00 | 0.0000 |
| breakeven_185 | Breakeven 185 | 249.83 | 149.83% | 0.00 | 0.00 | 0.0000 |
| breakeven_186 | Breakeven 186 | 250.84 | 150.84% | 0.00 | 0.00 | 0.0000 |
| breakeven_187 | Breakeven 187 | 251.84 | 151.84% | 0.00 | 0.00 | 0.0000 |
| breakeven_188 | Breakeven 188 | 252.84 | 152.84% | 0.00 | 0.00 | 0.0000 |
| breakeven_189 | Breakeven 189 | 253.85 | 153.85% | 0.00 | 0.00 | 0.0000 |
| breakeven_190 | Breakeven 190 | 254.85 | 154.85% | 0.00 | 0.00 | 0.0000 |
| breakeven_191 | Breakeven 191 | 255.85 | 155.85% | 0.00 | 0.00 | 0.0000 |
| breakeven_192 | Breakeven 192 | 256.86 | 156.86% | 0.00 | 0.00 | 0.0000 |
| breakeven_193 | Breakeven 193 | 257.86 | 157.86% | 0.00 | 0.00 | 0.0000 |
| breakeven_194 | Breakeven 194 | 258.86 | 158.86% | 0.00 | 0.00 | 0.0000 |
| breakeven_195 | Breakeven 195 | 259.87 | 159.87% | 0.00 | 0.00 | 0.0000 |
| breakeven_196 | Breakeven 196 | 260.87 | 160.87% | 0.00 | 0.00 | 0.0000 |
| breakeven_197 | Breakeven 197 | 261.87 | 161.87% | 0.00 | 0.00 | 0.0000 |
| breakeven_198 | Breakeven 198 | 262.88 | 162.88% | 0.00 | 0.00 | 0.0000 |
| breakeven_199 | Breakeven 199 | 263.88 | 163.88% | 0.00 | 0.00 | 0.0000 |
| breakeven_200 | Breakeven 200 | 264.88 | 164.88% | 0.00 | 0.00 | 0.0000 |
| breakeven_201 | Breakeven 201 | 265.89 | 165.89% | 0.00 | 0.00 | 1.0000 |
| breakeven_202 | Breakeven 202 | 266.89 | 166.89% | -0.00 | -0.00 | -1.0000 |
| breakeven_203 | Breakeven 203 | 269.90 | 169.90% | 0.00 | 0.00 | 1.0000 |
| breakeven_204 | Breakeven 204 | 270.90 | 170.90% | 0.00 | 0.00 | 0.0000 |
| breakeven_205 | Breakeven 205 | 272.41 | 172.41% | -0.00 | -0.00 | -1.0000 |
| breakeven_206 | Breakeven 206 | 273.91 | 173.91% | 0.00 | 0.00 | 0.0000 |
| breakeven_207 | Breakeven 207 | 274.92 | 174.92% | 0.00 | 0.00 | 0.0000 |
| breakeven_208 | Breakeven 208 | 275.92 | 175.92% | 0.00 | 0.00 | 0.0000 |
| breakeven_209 | Breakeven 209 | 276.92 | 176.92% | 0.00 | 0.00 | 0.0000 |
| breakeven_210 | Breakeven 210 | 277.93 | 177.93% | 0.00 | 0.00 | 0.0000 |
| breakeven_211 | Breakeven 211 | 278.93 | 178.93% | 0.00 | 0.00 | 0.0000 |
| breakeven_212 | Breakeven 212 | 279.93 | 179.93% | 0.00 | 0.00 | 0.0000 |
| breakeven_213 | Breakeven 213 | 280.94 | 180.94% | 0.00 | 0.00 | 0.0000 |
| breakeven_214 | Breakeven 214 | 281.94 | 181.94% | 0.00 | 0.00 | 0.0000 |
| breakeven_215 | Breakeven 215 | 282.94 | 182.94% | 0.00 | 0.00 | 0.0000 |
| breakeven_216 | Breakeven 216 | 283.95 | 183.95% | 0.00 | 0.00 | 0.0000 |
| breakeven_217 | Breakeven 217 | 284.95 | 184.95% | 0.00 | 0.00 | 0.0000 |
| breakeven_218 | Breakeven 218 | 285.95 | 185.95% | 0.00 | 0.00 | 0.0000 |
| breakeven_219 | Breakeven 219 | 286.96 | 186.96% | 0.00 | 0.00 | 0.0000 |
| breakeven_220 | Breakeven 220 | 287.96 | 187.96% | 0.00 | 0.00 | 0.0000 |
| breakeven_221 | Breakeven 221 | 288.96 | 188.96% | 0.00 | 0.00 | 0.0000 |
| breakeven_222 | Breakeven 222 | 289.97 | 189.97% | 0.00 | 0.00 | 0.0000 |
| breakeven_223 | Breakeven 223 | 290.97 | 190.97% | 0.00 | 0.00 | 0.0000 |
| breakeven_224 | Breakeven 224 | 291.97 | 191.97% | 0.00 | 0.00 | 0.0000 |
| breakeven_225 | Breakeven 225 | 292.98 | 192.98% | 0.00 | 0.00 | 0.0000 |
| breakeven_226 | Breakeven 226 | 293.98 | 193.98% | 0.00 | 0.00 | 0.0000 |
| breakeven_227 | Breakeven 227 | 294.98 | 194.98% | 0.00 | 0.00 | 0.0000 |
| breakeven_228 | Breakeven 228 | 295.99 | 195.99% | 0.00 | 0.00 | 0.0000 |
| breakeven_229 | Breakeven 229 | 296.99 | 196.99% | 0.00 | 0.00 | 0.0000 |
| breakeven_230 | Breakeven 230 | 297.99 | 197.99% | 0.00 | 0.00 | 0.0000 |
| breakeven_231 | Breakeven 231 | 299.00 | 199.00% | 0.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 0.00 | 0.00 | 0.0000 |

---

### Short Box Spread (ID=48) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |
| 3 | PUT | Short 1 | 108.00 | 9.90 | 100 |
| 4 | PUT | Long 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [100.0]
- Options Max PnL: 0.0
- Options Min PnL: -0.0
- Combined Max PnL: 20000.0
- Combined Min PnL: -10000.0

**Net Premium:**

- Per Share: -16.0
- Total: -1600.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | -$0.00 | -$10,000.00 |
| Risk Reward | 1.00x | 2.00x |
| Capital Basis | $5,980.00 | $15,980.00 |
| Cost Credit | Credit $1,600.00 | Credit $1,600.00 |
| Pop | 47.9% | 47.9% |
| Margin Proxy | 5980.0 | — |

**Probabilities:**

- PoP (raw): 0.47931
- Assignment Prob: 1.0
- P(25% Max Profit): 1e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -0.00 | -1500.00 | -1500.00 | -0.0312 | -0.1500 |
| 92.00 | Lower Strike | 0.00 | -800.00 | -800.00 | 0.0000 | -0.0800 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0312 | 0.0000 |
| 108.00 | Upper Strike | 0.00 | 800.00 | 800.00 | 0.0000 | 0.0800 |
| 115.00 | Upside (15%) | -0.00 | 1500.00 | 1500.00 | -0.0625 | 0.1500 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -10000.00 | -0.6258 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -0.00 | -1500.00 | -0.1500 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | -800.00 | -0.0800 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 800.00 | 0.0800 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -0.00 | 1500.00 | 0.1500 |
| infinity | Stock to Infinity | — | — | 0.00 | 98000.00 | 6.1327 |

---

### Short Box Spread (ID=48) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |
| 3 | PUT | Short 1 | 108.00 | 9.90 | 100 |
| 4 | PUT | Long 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [50.0]
- Options Max PnL: 0.0
- Options Min PnL: -0.0
- Combined Max PnL: 25000.0
- Combined Min PnL: -5000.0

**Net Premium:**

- Per Share: -16.0
- Total: -1600.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | -$0.00 | -$5,000.00 |
| Risk Reward | 1.00x | 5.00x |
| Capital Basis | $5,980.00 | $10,980.00 |
| Cost Credit | Credit $1,600.00 | Credit $1,600.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 5980.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 1.0
- P(25% Max Profit): 1e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 85.00 | Downside (15%) | -0.00 | 3500.00 | 3500.00 | -0.0312 | 0.7000 |
| 92.00 | Lower Strike | 0.00 | 4200.00 | 4200.00 | 0.0000 | 0.8400 |
| 100.00 | Current Market Price | 0.00 | 5000.00 | 5000.00 | 0.0312 | 1.0000 |
| 108.00 | Upper Strike | 0.00 | 5800.00 | 5800.00 | 0.0000 | 1.1600 |
| 115.00 | Upside (15%) | -0.00 | 6500.00 | 6500.00 | -0.0625 | 1.3000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -5000.00 | -0.4554 |
| breakeven_1 | Breakeven 1 | 50.00 | -50.00% | 0.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -0.00 | 3500.00 | 0.7000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | 4200.00 | 0.8400 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 1.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 5800.00 | 1.1600 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -0.00 | 6500.00 | 1.3000 |
| infinity | Stock to Infinity | — | — | 0.00 | 103000.00 | 9.3807 |

---

### Short Box Spread (ID=48) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |
| 3 | PUT | Short 1 | 108.00 | 9.90 | 100 |
| 4 | PUT | Long 1 | 92.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [115.0]
- Options Max PnL: 0.0
- Options Min PnL: -0.0
- Combined Max PnL: 18500.0
- Combined Min PnL: -11500.0

**Net Premium:**

- Per Share: -16.0
- Total: -1600.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | -$0.00 | -$11,500.00 |
| Risk Reward | 1.00x | 1.61x |
| Capital Basis | $5,980.00 | $17,480.00 |
| Cost Credit | Credit $1,600.00 | Credit $1,600.00 |
| Pop | 8.1% | 8.1% |
| Margin Proxy | 5980.0 | — |

**Probabilities:**

- PoP (raw): 0.081123
- Assignment Prob: 1.0
- P(25% Max Profit): 1e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -0.00 | -3000.00 | -3000.00 | -0.0312 | -0.2609 |
| 92.00 | Lower Strike | 0.00 | -2300.00 | -2300.00 | 0.0000 | -0.2000 |
| 100.00 | Current Market Price | 0.00 | -1500.00 | -1500.00 | 0.0312 | -0.1304 |
| 108.00 | Upper Strike | 0.00 | -700.00 | -700.00 | 0.0000 | -0.0609 |
| 115.00 | Upside (15%) | -0.00 | 0.00 | -0.00 | -0.0625 | -0.0000 |
| 115.00 | Upside (15%) | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -11500.00 | -0.6579 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -0.00 | -3000.00 | -0.2609 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | -2300.00 | -0.2000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.1304 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | -700.00 | -0.0609 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -0.00 | -0.00 | -0.0000 |
| breakeven_1 | Breakeven 1 | 115.00 | 15.00% | -0.00 | -0.00 | -0.0000 |
| infinity | Stock to Infinity | — | — | 0.00 | 96500.00 | 5.5206 |

---

### Synthetic Long Stock (ID=49) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [100.0]
- Options Max PnL: 20000.0
- Options Min PnL: -10000.0
- Combined Max PnL: 20000.0
- Combined Min PnL: -10000.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$10,000.00 | -$10,000.00 |
| Risk Reward | 2.00x | 2.00x |
| Capital Basis | $2,250.00 | $2,250.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 47.9% | 47.9% |
| Margin Proxy | 2250.0 | — |

**Probabilities:**

- PoP (raw): 0.47931
- Assignment Prob: 0.520709
- P(25% Max Profit): 3.9e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1500.00 | 0.00 | -1500.00 | -0.1500 | -0.1500 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 1500.00 | 0.00 | 1500.00 | 0.1500 | 0.1500 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -10000.00 | -10000.00 | -4.4444 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1500.00 | -1500.00 | -0.1500 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1500.00 | 1500.00 | 0.1500 |
| infinity | Stock to Infinity | — | — | 90000.00 | 90000.00 | 40.0000 |

---

### Synthetic Long Stock (ID=49) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [100.0]
- Options Max PnL: 20000.0
- Options Min PnL: -10000.0
- Combined Max PnL: 40000.0
- Combined Min PnL: -20000.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$10,000.00 | -$20,000.00 |
| Risk Reward | 2.00x | 2.00x |
| Capital Basis | $2,250.00 | $12,250.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 47.9% | 47.9% |
| Margin Proxy | 2250.0 | — |

**Probabilities:**

- PoP (raw): 0.47931
- Assignment Prob: 0.520709
- P(25% Max Profit): 3.9e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1500.00 | -1500.00 | -3000.00 | -0.1500 | -0.1500 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 1500.00 | 1500.00 | 3000.00 | 0.1500 | 0.1500 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -10000.00 | -20000.00 | -1.6327 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1500.00 | -3000.00 | -0.1500 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1500.00 | 3000.00 | 0.1500 |
| infinity | Stock to Infinity | — | — | 90000.00 | 180000.00 | 14.6939 |

---

### Synthetic Long Stock (ID=49) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [75.0]
- Options Max PnL: 20000.0
- Options Min PnL: -10000.0
- Combined Max PnL: 45000.0
- Combined Min PnL: -15000.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$10,000.00 | -$15,000.00 |
| Risk Reward | 2.00x | 3.00x |
| Capital Basis | $2,250.00 | $7,250.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 99.7% | 99.7% |
| Margin Proxy | 2250.0 | — |

**Probabilities:**

- PoP (raw): 0.996715
- Assignment Prob: 0.520709
- P(25% Max Profit): 3.9e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -5000.00 | 0.00 | -5000.00 | -0.5000 | -0.3333 |
| 75.00 | Breakeven 1 | -2500.00 | 2500.00 | 0.00 | -0.2500 | 0.0000 |
| 85.00 | Downside (15%) | -1500.00 | 3500.00 | 2000.00 | -0.1500 | 0.1333 |
| 100.00 | Current Market Price | 0.00 | 5000.00 | 5000.00 | 0.0000 | 0.3333 |
| 115.00 | Upside (15%) | 1500.00 | 6500.00 | 8000.00 | 0.1500 | 0.5333 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -10000.00 | -15000.00 | -2.0690 |
| breakeven_1 | Breakeven 1 | 75.00 | -25.00% | -2500.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1500.00 | 2000.00 | 0.1333 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 0.3333 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 0.3333 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1500.00 | 8000.00 | 0.5333 |
| infinity | Stock to Infinity | — | — | 90000.00 | 185000.00 | 25.5172 |

---

### Synthetic Long Stock (ID=49) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Long 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [107.5]
- Options Max PnL: 20000.0
- Options Min PnL: -10000.0
- Combined Max PnL: 38500.0
- Combined Min PnL: -21500.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$10,000.00 | -$21,500.00 |
| Risk Reward | 2.00x | 1.79x |
| Capital Basis | $2,250.00 | $13,750.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 22.7% | 22.7% |
| Margin Proxy | 2250.0 | — |

**Probabilities:**

- PoP (raw): 0.227159
- Assignment Prob: 0.520709
- P(25% Max Profit): 3.9e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1500.00 | -3000.00 | -4500.00 | -0.1500 | -0.2093 |
| 100.00 | Current Market Price | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.0698 |
| 107.50 | Breakeven 1 | 750.00 | -750.00 | 0.00 | 0.0750 | 0.0000 |
| 115.00 | Upside (15%) | 1500.00 | 0.00 | 1500.00 | 0.1500 | 0.0698 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -10000.00 | -21500.00 | -1.5636 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1500.00 | -4500.00 | -0.2093 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.0698 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.0698 |
| breakeven_1 | Breakeven 1 | 107.50 | 7.50% | 750.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1500.00 | 1500.00 | 0.0698 |
| infinity | Stock to Infinity | — | — | 90000.00 | 178500.00 | 12.9818 |

---

### Synthetic Short Stock (ID=50) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [100.0]
- Options Max PnL: 10000.0
- Options Min PnL: -20000.0
- Combined Max PnL: 10000.0
- Combined Min PnL: -20000.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $10,000.00 | $10,000.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.50x | 0.50x |
| Capital Basis | $2,250.00 | $2,250.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 52.1% | 52.1% |
| Margin Proxy | 2250.0 | — |

**Probabilities:**

- PoP (raw): 0.52069
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.003285
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1500.00 | 0.00 | 1500.00 | 0.6667 | 0.6667 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -1500.00 | 0.00 | -1500.00 | -0.6667 | -0.6667 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 10000.00 | 10000.00 | 4.4444 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1500.00 | 1500.00 | 0.6667 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1500.00 | -1500.00 | -0.6667 |
| infinity | Stock to Infinity | — | — | Unlimited | -90000.00 | -40.0000 |

---

### Synthetic Short Stock (ID=50) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: COL_EQ
- Margin Classification: COL_EQ

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [0.0, 1.003344, 2.006689, 3.010033, 4.013378, 5.016722, 6.020067, 7.023411, 8.026756, 9.0301, 10.033445, 11.036789, 12.040134, 13.043478, 14.046823, 15.050167, 17.056856, 18.060201, 19.063545, 20.06689, 21.070234, 22.073579, 23.076923, 24.080268, 25.083612, 26.086957, 27.090301, 28.093645, 29.09699, 30.100334, 31.103679, 32.107023, 33.110368, 34.113712, 35.117057, 36.120401, 37.123746, 38.12709, 39.130435, 40.133779, 41.137124, 42.140468, 43.143813, 44.147157, 45.150502, 46.153846, 47.157191, 48.160535, 49.16388, 50.167224, 51.170569, 52.173913, 53.177258, 54.180602, 55.183946, 56.187291, 58.19398, 59.197324, 60.200669, 61.204013, 62.207358, 63.210702, 64.214047, 65.217391, 66.220736, 67.22408, 68.227425, 69.230769, 70.234114, 71.237458, 72.240803, 73.244147, 74.247492, 75.250836, 76.254181, 77.257525, 78.26087, 79.264214, 80.267559, 81.270903, 82.274247, 83.277592, 84.280936, 85.284281, 86.287625, 87.29097, 88.294314, 89.297659, 90.301003, 91.304348, 92.307692, 93.311037, 94.314381, 95.317726, 96.32107, 97.324415, 98.327759, 99.331104, 100.0, 100.334448, 101.337793, 102.341137, 103.344482, 104.347826, 105.351171, 106.354515, 107.35786, 108.361204, 109.364548, 110.367893, 111.371237, 112.374582, 113.377926, 114.381271, 115.384615, 116.38796, 117.391304, 118.394649, 119.397993, 120.401338, 122.408027, 123.411371, 124.414716, 125.41806, 126.421405, 127.424749, 128.428094, 129.431438, 130.434783, 131.438127, 132.441472, 133.444816, 134.448161, 135.451505, 136.454849, 137.458194, 138.461538, 139.464883, 140.468227, 141.471572, 142.474916, 143.478261, 144.481605, 145.48495, 146.488294, 147.491639, 148.494983, 149.498328, 150.501672, 151.505017, 152.508361, 153.511706, 154.51505, 155.518395, 156.521739, 157.525084, 158.528428, 159.531773, 160.535117, 161.538462, 162.541806, 163.545151, 164.548495, 165.551839, 166.555184, 167.558528, 168.561873, 169.565217, 170.568562, 171.571906, 172.575251, 173.578595, 174.58194, 175.585284, 176.588629, 177.591973, 178.595318, 179.598662, 180.602007, 181.605351, 183.61204, 184.615385, 185.618729, 186.622074, 187.625418, 188.628763, 189.632107, 190.635452, 191.638796, 192.64214, 193.645485, 194.648829, 195.652174, 196.655518, 197.658863, 198.662207, 199.665552, 200.668896, 201.672241, 202.675585, 203.67893, 204.682274, 205.685619, 206.688963, 207.692308, 208.695652, 209.698997, 210.702341, 211.705686, 212.70903, 213.712375, 214.715719, 215.719064, 216.722408, 217.725753, 218.729097, 219.732441, 220.735786, 221.73913, 222.742475, 223.745819, 224.749164, 225.752508, 226.755853, 227.759197, 228.762542, 229.765886, 230.769231, 231.772575, 232.77592, 233.779264, 234.782609, 235.785953, 236.789298, 237.792642, 238.795987, 239.799331, 240.802676, 241.80602, 242.809365, 243.812709, 244.816054, 245.819398, 246.822742, 247.826087, 248.829431, 249.832776, 250.83612, 251.839465, 252.842809, 253.846154, 254.849498, 255.852843, 256.856187, 257.859532, 258.862876, 259.866221, 260.869565, 261.87291, 262.876254, 263.879599, 264.882943, 265.886288, 266.889632, 267.892977, 268.896321, 269.899666, 270.90301, 271.906355, 272.909699, 273.913043, 274.916388, 275.919732, 276.923077, 277.926421, 278.929766, 279.93311, 280.936455, 281.939799, 282.943144, 283.946488, 284.949833, 285.953177, 286.956522, 287.959866, 288.963211, 289.966555, 290.9699, 291.973244, 292.976589, 293.979933, 294.983278, 295.986622, 296.989967, 297.993311, 298.996656]
- Options Max PnL: 10000.0
- Options Min PnL: -20000.0
- Combined Max PnL: 0.0
- Combined Min PnL: -0.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $10,000.00 | $0.00 |
| Max Loss | Unlimited | -$0.00 |
| Risk Reward | 0.50x | 0.25x |
| Capital Basis | $5,250.00 | $15,250.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 5250.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.003285
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 0.00 | Breakeven 1 | 10000.00 | -10000.00 | 0.00 | 1.9048 | 0.0000 |
| 1.00 | Breakeven 2 | 9899.67 | -9899.67 | 0.00 | 1.8857 | 0.0000 |
| 2.01 | Breakeven 3 | 9799.33 | -9799.33 | 0.00 | 1.8665 | 0.0000 |
| 3.01 | Breakeven 4 | 9699.00 | -9699.00 | 0.00 | 1.8474 | 0.0000 |
| 4.01 | Breakeven 5 | 9598.66 | -9598.66 | 0.00 | 1.8283 | 0.0000 |
| 5.02 | Breakeven 6 | 9498.33 | -9498.33 | 0.00 | 1.8092 | 0.0000 |
| 6.02 | Breakeven 7 | 9397.99 | -9397.99 | 0.00 | 1.7901 | 0.0000 |
| 7.02 | Breakeven 8 | 9297.66 | -9297.66 | 0.00 | 1.7710 | 0.0000 |
| 8.03 | Breakeven 9 | 9197.32 | -9197.32 | 0.00 | 1.7519 | 0.0000 |
| 9.03 | Breakeven 10 | 9096.99 | -9096.99 | 0.00 | 1.7328 | 0.0000 |
| 10.03 | Breakeven 11 | 8996.66 | -8996.66 | 0.00 | 1.7136 | 0.0000 |
| 11.04 | Breakeven 12 | 8896.32 | -8896.32 | 0.00 | 1.6945 | 0.0000 |
| 12.04 | Breakeven 13 | 8795.99 | -8795.99 | 0.00 | 1.6754 | 0.0000 |
| 13.04 | Breakeven 14 | 8695.65 | -8695.65 | 0.00 | 1.6563 | 0.0000 |
| 14.05 | Breakeven 15 | 8595.32 | -8595.32 | 0.00 | 1.6372 | 0.0000 |
| 15.05 | Breakeven 16 | 8494.98 | -8494.98 | 0.00 | 1.6181 | 0.0000 |
| 17.06 | Breakeven 17 | 8294.31 | -8294.31 | 0.00 | 1.5799 | 0.0000 |
| 18.06 | Breakeven 18 | 8193.98 | -8193.98 | -0.00 | 1.5608 | -0.0000 |
| 19.06 | Breakeven 19 | 8093.65 | -8093.65 | 0.00 | 1.5416 | 0.0000 |
| 20.07 | Breakeven 20 | 7993.31 | -7993.31 | 0.00 | 1.5225 | 0.0000 |
| 21.07 | Breakeven 21 | 7892.98 | -7892.98 | 0.00 | 1.5034 | 0.0000 |
| 22.07 | Breakeven 22 | 7792.64 | -7792.64 | 0.00 | 1.4843 | 0.0000 |
| 23.08 | Breakeven 23 | 7692.31 | -7692.31 | 0.00 | 1.4652 | 0.0000 |
| 24.08 | Breakeven 24 | 7591.97 | -7591.97 | 0.00 | 1.4461 | 0.0000 |
| 25.08 | Breakeven 25 | 7491.64 | -7491.64 | 0.00 | 1.4270 | 0.0000 |
| 26.09 | Breakeven 26 | 7391.30 | -7391.30 | 0.00 | 1.4079 | 0.0000 |
| 27.09 | Breakeven 27 | 7290.97 | -7290.97 | 0.00 | 1.3888 | 0.0000 |
| 28.09 | Breakeven 28 | 7190.64 | -7190.64 | 0.00 | 1.3696 | 0.0000 |
| 29.10 | Breakeven 29 | 7090.30 | -7090.30 | 0.00 | 1.3505 | 0.0000 |
| 30.10 | Breakeven 30 | 6989.97 | -6989.97 | 0.00 | 1.3314 | 0.0000 |
| 31.10 | Breakeven 31 | 6889.63 | -6889.63 | 0.00 | 1.3123 | 0.0000 |
| 32.11 | Breakeven 32 | 6789.30 | -6789.30 | 0.00 | 1.2932 | 0.0000 |
| 33.11 | Breakeven 33 | 6688.96 | -6688.96 | 0.00 | 1.2741 | 0.0000 |
| 34.11 | Breakeven 34 | 6588.63 | -6588.63 | 0.00 | 1.2550 | 0.0000 |
| 35.12 | Breakeven 35 | 6488.29 | -6488.29 | 0.00 | 1.2359 | 0.0000 |
| 36.12 | Breakeven 36 | 6387.96 | -6387.96 | 0.00 | 1.2168 | 0.0000 |
| 37.12 | Breakeven 37 | 6287.63 | -6287.63 | 0.00 | 1.1976 | 0.0000 |
| 38.13 | Breakeven 38 | 6187.29 | -6187.29 | 0.00 | 1.1785 | 0.0000 |
| 39.13 | Breakeven 39 | 6086.96 | -6086.96 | 0.00 | 1.1594 | 0.0000 |
| 40.13 | Breakeven 40 | 5986.62 | -5986.62 | 0.00 | 1.1403 | 0.0000 |
| 41.14 | Breakeven 41 | 5886.29 | -5886.29 | 0.00 | 1.1212 | 0.0000 |
| 42.14 | Breakeven 42 | 5785.95 | -5785.95 | 0.00 | 1.1021 | 0.0000 |
| 43.14 | Breakeven 43 | 5685.62 | -5685.62 | 0.00 | 1.0830 | 0.0000 |
| 44.15 | Breakeven 44 | 5585.28 | -5585.28 | 0.00 | 1.0639 | 0.0000 |
| 45.15 | Breakeven 45 | 5484.95 | -5484.95 | 0.00 | 1.0448 | 0.0000 |
| 46.15 | Breakeven 46 | 5384.62 | -5384.62 | 0.00 | 1.0256 | 0.0000 |
| 47.16 | Breakeven 47 | 5284.28 | -5284.28 | 0.00 | 1.0065 | 0.0000 |
| 48.16 | Breakeven 48 | 5183.95 | -5183.95 | 0.00 | 0.9874 | 0.0000 |
| 49.16 | Breakeven 49 | 5083.61 | -5083.61 | 0.00 | 0.9683 | 0.0000 |
| 50.17 | Breakeven 50 | 4983.28 | -4983.28 | 0.00 | 0.9492 | 0.0000 |
| 51.17 | Breakeven 51 | 4882.94 | -4882.94 | 0.00 | 0.9301 | 0.0000 |
| 52.17 | Breakeven 52 | 4782.61 | -4782.61 | 0.00 | 0.9110 | 0.0000 |
| 53.18 | Breakeven 53 | 4682.27 | -4682.27 | 0.00 | 0.8919 | 0.0000 |
| 54.18 | Breakeven 54 | 4581.94 | -4581.94 | 0.00 | 0.8728 | 0.0000 |
| 55.18 | Breakeven 55 | 4481.61 | -4481.61 | 0.00 | 0.8536 | 0.0000 |
| 56.19 | Breakeven 56 | 4381.27 | -4381.27 | 0.00 | 0.8345 | 0.0000 |
| 58.19 | Breakeven 57 | 4180.60 | -4180.60 | 0.00 | 0.7963 | 0.0000 |
| 59.20 | Breakeven 58 | 4080.27 | -4080.27 | 0.00 | 0.7772 | 0.0000 |
| 60.20 | Breakeven 59 | 3979.93 | -3979.93 | 0.00 | 0.7581 | 0.0000 |
| 61.20 | Breakeven 60 | 3879.60 | -3879.60 | 0.00 | 0.7390 | 0.0000 |
| 62.21 | Breakeven 61 | 3779.26 | -3779.26 | 0.00 | 0.7199 | 0.0000 |
| 63.21 | Breakeven 62 | 3678.93 | -3678.93 | 0.00 | 0.7007 | 0.0000 |
| 64.21 | Breakeven 63 | 3578.60 | -3578.60 | 0.00 | 0.6816 | 0.0000 |
| 65.22 | Breakeven 64 | 3478.26 | -3478.26 | 0.00 | 0.6625 | 0.0000 |
| 66.22 | Breakeven 65 | 3377.93 | -3377.93 | 0.00 | 0.6434 | 0.0000 |
| 67.22 | Breakeven 66 | 3277.59 | -3277.59 | 0.00 | 0.6243 | 0.0000 |
| 68.23 | Breakeven 67 | 3177.26 | -3177.26 | 0.00 | 0.6052 | 0.0000 |
| 69.23 | Breakeven 68 | 3076.92 | -3076.92 | 0.00 | 0.5861 | 0.0000 |
| 70.23 | Breakeven 69 | 2976.59 | -2976.59 | 0.00 | 0.5670 | 0.0000 |
| 71.24 | Breakeven 70 | 2876.25 | -2876.25 | 0.00 | 0.5479 | 0.0000 |
| 72.24 | Breakeven 71 | 2775.92 | -2775.92 | 0.00 | 0.5287 | 0.0000 |
| 73.24 | Breakeven 72 | 2675.59 | -2675.59 | 0.00 | 0.5096 | 0.0000 |
| 74.25 | Breakeven 73 | 2575.25 | -2575.25 | 0.00 | 0.4905 | 0.0000 |
| 75.25 | Breakeven 74 | 2474.92 | -2474.92 | 0.00 | 0.4714 | 0.0000 |
| 76.25 | Breakeven 75 | 2374.58 | -2374.58 | 0.00 | 0.4523 | 0.0000 |
| 77.26 | Breakeven 76 | 2274.25 | -2274.25 | 0.00 | 0.4332 | 0.0000 |
| 78.26 | Breakeven 77 | 2173.91 | -2173.91 | 0.00 | 0.4141 | 0.0000 |
| 79.26 | Breakeven 78 | 2073.58 | -2073.58 | -0.00 | 0.3950 | -0.0000 |
| 80.27 | Breakeven 79 | 1973.24 | -1973.24 | 0.00 | 0.3759 | 0.0000 |
| 81.27 | Breakeven 80 | 1872.91 | -1872.91 | 0.00 | 0.3567 | 0.0000 |
| 82.27 | Breakeven 81 | 1772.58 | -1772.58 | 0.00 | 0.3376 | 0.0000 |
| 83.28 | Breakeven 82 | 1672.24 | -1672.24 | 0.00 | 0.3185 | 0.0000 |
| 84.28 | Breakeven 83 | 1571.91 | -1571.91 | 0.00 | 0.2994 | 0.0000 |
| 85.00 | Downside (15%) | 1500.00 | -1500.00 | 0.00 | 0.2857 | 0.0000 |
| 85.28 | Breakeven 84 | 1471.57 | -1471.57 | 0.00 | 0.2803 | 0.0000 |
| 86.29 | Breakeven 85 | 1371.24 | -1371.24 | 0.00 | 0.2612 | 0.0000 |
| 87.29 | Breakeven 86 | 1270.90 | -1270.90 | 0.00 | 0.2421 | 0.0000 |
| 88.29 | Breakeven 87 | 1170.57 | -1170.57 | 0.00 | 0.2230 | 0.0000 |
| 89.30 | Breakeven 88 | 1070.23 | -1070.23 | 0.00 | 0.2039 | 0.0000 |
| 90.30 | Breakeven 89 | 969.90 | -969.90 | 0.00 | 0.1847 | 0.0000 |
| 91.30 | Breakeven 90 | 869.57 | -869.57 | 0.00 | 0.1656 | 0.0000 |
| 92.31 | Breakeven 91 | 769.23 | -769.23 | 0.00 | 0.1465 | 0.0000 |
| 93.31 | Breakeven 92 | 668.90 | -668.90 | 0.00 | 0.1274 | 0.0000 |
| 94.31 | Breakeven 93 | 568.56 | -568.56 | 0.00 | 0.1083 | 0.0000 |
| 95.32 | Breakeven 94 | 468.23 | -468.23 | 0.00 | 0.0892 | 0.0000 |
| 96.32 | Breakeven 95 | 367.89 | -367.89 | 0.00 | 0.0701 | 0.0000 |
| 97.32 | Breakeven 96 | 267.56 | -267.56 | 0.00 | 0.0510 | 0.0000 |
| 98.33 | Breakeven 97 | 167.22 | -167.22 | 0.00 | 0.0319 | 0.0000 |
| 99.33 | Breakeven 98 | 66.89 | -66.89 | 0.00 | 0.0127 | 0.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.33 | Breakeven 100 | -33.44 | 33.44 | 0.00 | -0.0064 | 0.0000 |
| 101.34 | Breakeven 101 | -133.78 | 133.78 | 0.00 | -0.0255 | 0.0000 |
| 102.34 | Breakeven 102 | -234.11 | 234.11 | 0.00 | -0.0446 | 0.0000 |
| 103.34 | Breakeven 103 | -334.45 | 334.45 | 0.00 | -0.0637 | 0.0000 |
| 104.35 | Breakeven 104 | -434.78 | 434.78 | 0.00 | -0.0828 | 0.0000 |
| 105.35 | Breakeven 105 | -535.12 | 535.12 | 0.00 | -0.1019 | 0.0000 |
| 106.35 | Breakeven 106 | -635.45 | 635.45 | 0.00 | -0.1210 | 0.0000 |
| 107.36 | Breakeven 107 | -735.79 | 735.79 | 0.00 | -0.1401 | 0.0000 |
| 108.36 | Breakeven 108 | -836.12 | 836.12 | 0.00 | -0.1593 | 0.0000 |
| 109.36 | Breakeven 109 | -936.45 | 936.45 | 0.00 | -0.1784 | 0.0000 |
| 110.37 | Breakeven 110 | -1036.79 | 1036.79 | 0.00 | -0.1975 | 0.0000 |
| 111.37 | Breakeven 111 | -1137.12 | 1137.12 | 0.00 | -0.2166 | 0.0000 |
| 112.37 | Breakeven 112 | -1237.46 | 1237.46 | 0.00 | -0.2357 | 0.0000 |
| 113.38 | Breakeven 113 | -1337.79 | 1337.79 | 0.00 | -0.2548 | 0.0000 |
| 114.38 | Breakeven 114 | -1438.13 | 1438.13 | 0.00 | -0.2739 | 0.0000 |
| 115.00 | Upside (15%) | -1500.00 | 1500.00 | 0.00 | -0.2857 | 0.0000 |
| 115.38 | Breakeven 115 | -1538.46 | 1538.46 | 0.00 | -0.2930 | 0.0000 |
| 116.39 | Breakeven 116 | -1638.80 | 1638.80 | 0.00 | -0.3122 | 0.0000 |
| 117.39 | Breakeven 117 | -1739.13 | 1739.13 | 0.00 | -0.3313 | 0.0000 |
| 118.39 | Breakeven 118 | -1839.46 | 1839.46 | 0.00 | -0.3504 | 0.0000 |
| 119.40 | Breakeven 119 | -1939.80 | 1939.80 | 0.00 | -0.3695 | 0.0000 |
| 120.40 | Breakeven 120 | -2040.13 | 2040.13 | 0.00 | -0.3886 | 0.0000 |
| 122.41 | Breakeven 121 | -2240.80 | 2240.80 | 0.00 | -0.4268 | 0.0000 |
| 123.41 | Breakeven 122 | -2341.14 | 2341.14 | 0.00 | -0.4459 | 0.0000 |
| 124.41 | Breakeven 123 | -2441.47 | 2441.47 | 0.00 | -0.4650 | 0.0000 |
| 125.42 | Breakeven 124 | -2541.81 | 2541.81 | 0.00 | -0.4842 | 0.0000 |
| 126.42 | Breakeven 125 | -2642.14 | 2642.14 | 0.00 | -0.5033 | 0.0000 |
| 127.42 | Breakeven 126 | -2742.47 | 2742.47 | 0.00 | -0.5224 | 0.0000 |
| 128.43 | Breakeven 127 | -2842.81 | 2842.81 | 0.00 | -0.5415 | 0.0000 |
| 129.43 | Breakeven 128 | -2943.14 | 2943.14 | 0.00 | -0.5606 | 0.0000 |
| 130.43 | Breakeven 129 | -3043.48 | 3043.48 | 0.00 | -0.5797 | 0.0000 |
| 131.44 | Breakeven 130 | -3143.81 | 3143.81 | 0.00 | -0.5988 | 0.0000 |
| 132.44 | Breakeven 131 | -3244.15 | 3244.15 | 0.00 | -0.6179 | 0.0000 |
| 133.44 | Breakeven 132 | -3344.48 | 3344.48 | 0.00 | -0.6370 | 0.0000 |
| 134.45 | Breakeven 133 | -3444.82 | 3444.82 | 0.00 | -0.6562 | 0.0000 |
| 135.45 | Breakeven 134 | -3545.15 | 3545.15 | 0.00 | -0.6753 | 0.0000 |
| 136.45 | Breakeven 135 | -3645.48 | 3645.48 | 0.00 | -0.6944 | 0.0000 |
| 137.46 | Breakeven 136 | -3745.82 | 3745.82 | 0.00 | -0.7135 | 0.0000 |
| 138.46 | Breakeven 137 | -3846.15 | 3846.15 | 0.00 | -0.7326 | 0.0000 |
| 139.46 | Breakeven 138 | -3946.49 | 3946.49 | 0.00 | -0.7517 | 0.0000 |
| 140.47 | Breakeven 139 | -4046.82 | 4046.82 | 0.00 | -0.7708 | 0.0000 |
| 141.47 | Breakeven 140 | -4147.16 | 4147.16 | 0.00 | -0.7899 | 0.0000 |
| 142.47 | Breakeven 141 | -4247.49 | 4247.49 | 0.00 | -0.8090 | 0.0000 |
| 143.48 | Breakeven 142 | -4347.83 | 4347.83 | 0.00 | -0.8282 | 0.0000 |
| 144.48 | Breakeven 143 | -4448.16 | 4448.16 | 0.00 | -0.8473 | 0.0000 |
| 145.48 | Breakeven 144 | -4548.49 | 4548.49 | 0.00 | -0.8664 | 0.0000 |
| 146.49 | Breakeven 145 | -4648.83 | 4648.83 | 0.00 | -0.8855 | 0.0000 |
| 147.49 | Breakeven 146 | -4749.16 | 4749.16 | 0.00 | -0.9046 | 0.0000 |
| 148.49 | Breakeven 147 | -4849.50 | 4849.50 | 0.00 | -0.9237 | 0.0000 |
| 149.50 | Breakeven 148 | -4949.83 | 4949.83 | 0.00 | -0.9428 | 0.0000 |
| 150.50 | Breakeven 149 | -5050.17 | 5050.17 | 0.00 | -0.9619 | 0.0000 |
| 151.51 | Breakeven 150 | -5150.50 | 5150.50 | 0.00 | -0.9810 | 0.0000 |
| 152.51 | Breakeven 151 | -5250.84 | 5250.84 | 0.00 | -1.0002 | 0.0000 |
| 153.51 | Breakeven 152 | -5351.17 | 5351.17 | 0.00 | -1.0193 | 0.0000 |
| 154.52 | Breakeven 153 | -5451.51 | 5451.51 | 0.00 | -1.0384 | 0.0000 |
| 155.52 | Breakeven 154 | -5551.84 | 5551.84 | 0.00 | -1.0575 | 0.0000 |
| 156.52 | Breakeven 155 | -5652.17 | 5652.17 | 0.00 | -1.0766 | 0.0000 |
| 157.53 | Breakeven 156 | -5752.51 | 5752.51 | 0.00 | -1.0957 | 0.0000 |
| 158.53 | Breakeven 157 | -5852.84 | 5852.84 | 0.00 | -1.1148 | 0.0000 |
| 159.53 | Breakeven 158 | -5953.18 | 5953.18 | 0.00 | -1.1339 | 0.0000 |
| 160.54 | Breakeven 159 | -6053.51 | 6053.51 | 0.00 | -1.1530 | 0.0000 |
| 161.54 | Breakeven 160 | -6153.85 | 6153.85 | 0.00 | -1.1722 | 0.0000 |
| 162.54 | Breakeven 161 | -6254.18 | 6254.18 | 0.00 | -1.1913 | 0.0000 |
| 163.55 | Breakeven 162 | -6354.52 | 6354.52 | 0.00 | -1.2104 | 0.0000 |
| 164.55 | Breakeven 163 | -6454.85 | 6454.85 | 0.00 | -1.2295 | 0.0000 |
| 165.55 | Breakeven 164 | -6555.18 | 6555.18 | 0.00 | -1.2486 | 0.0000 |
| 166.56 | Breakeven 165 | -6655.52 | 6655.52 | 0.00 | -1.2677 | 0.0000 |
| 167.56 | Breakeven 166 | -6755.85 | 6755.85 | 0.00 | -1.2868 | 0.0000 |
| 168.56 | Breakeven 167 | -6856.19 | 6856.19 | 0.00 | -1.3059 | 0.0000 |
| 169.57 | Breakeven 168 | -6956.52 | 6956.52 | 0.00 | -1.3251 | 0.0000 |
| 170.57 | Breakeven 169 | -7056.86 | 7056.86 | 0.00 | -1.3442 | 0.0000 |
| 171.57 | Breakeven 170 | -7157.19 | 7157.19 | 0.00 | -1.3633 | 0.0000 |
| 172.58 | Breakeven 171 | -7257.53 | 7257.53 | 0.00 | -1.3824 | 0.0000 |
| 173.58 | Breakeven 172 | -7357.86 | 7357.86 | 0.00 | -1.4015 | 0.0000 |
| 174.58 | Breakeven 173 | -7458.19 | 7458.19 | 0.00 | -1.4206 | 0.0000 |
| 175.59 | Breakeven 174 | -7558.53 | 7558.53 | 0.00 | -1.4397 | 0.0000 |
| 176.59 | Breakeven 175 | -7658.86 | 7658.86 | 0.00 | -1.4588 | 0.0000 |
| 177.59 | Breakeven 176 | -7759.20 | 7759.20 | 0.00 | -1.4779 | 0.0000 |
| 178.60 | Breakeven 177 | -7859.53 | 7859.53 | 0.00 | -1.4971 | 0.0000 |
| 179.60 | Breakeven 178 | -7959.87 | 7959.87 | 0.00 | -1.5162 | 0.0000 |
| 180.60 | Breakeven 179 | -8060.20 | 8060.20 | 0.00 | -1.5353 | 0.0000 |
| 181.61 | Breakeven 180 | -8160.54 | 8160.54 | 0.00 | -1.5544 | 0.0000 |
| 183.61 | Breakeven 181 | -8361.20 | 8361.20 | 0.00 | -1.5926 | 0.0000 |
| 184.62 | Breakeven 182 | -8461.54 | 8461.54 | 0.00 | -1.6117 | 0.0000 |
| 185.62 | Breakeven 183 | -8561.87 | 8561.87 | 0.00 | -1.6308 | 0.0000 |
| 186.62 | Breakeven 184 | -8662.21 | 8662.21 | 0.00 | -1.6499 | 0.0000 |
| 187.63 | Breakeven 185 | -8762.54 | 8762.54 | 0.00 | -1.6691 | 0.0000 |
| 188.63 | Breakeven 186 | -8862.88 | 8862.88 | 0.00 | -1.6882 | 0.0000 |
| 189.63 | Breakeven 187 | -8963.21 | 8963.21 | 0.00 | -1.7073 | 0.0000 |
| 190.64 | Breakeven 188 | -9063.55 | 9063.55 | 0.00 | -1.7264 | 0.0000 |
| 191.64 | Breakeven 189 | -9163.88 | 9163.88 | 0.00 | -1.7455 | 0.0000 |
| 192.64 | Breakeven 190 | -9264.21 | 9264.21 | 0.00 | -1.7646 | 0.0000 |
| 193.65 | Breakeven 191 | -9364.55 | 9364.55 | 0.00 | -1.7837 | 0.0000 |
| 194.65 | Breakeven 192 | -9464.88 | 9464.88 | 0.00 | -1.8028 | 0.0000 |
| 195.65 | Breakeven 193 | -9565.22 | 9565.22 | 0.00 | -1.8219 | 0.0000 |
| 196.66 | Breakeven 194 | -9665.55 | 9665.55 | 0.00 | -1.8411 | 0.0000 |
| 197.66 | Breakeven 195 | -9765.89 | 9765.89 | 0.00 | -1.8602 | 0.0000 |
| 198.66 | Breakeven 196 | -9866.22 | 9866.22 | 0.00 | -1.8793 | 0.0000 |
| 199.67 | Breakeven 197 | -9966.56 | 9966.56 | 0.00 | -1.8984 | 0.0000 |
| 200.67 | Breakeven 198 | -10066.89 | 10066.89 | 0.00 | -1.9175 | 0.0000 |
| 201.67 | Breakeven 199 | -10167.22 | 10167.22 | 0.00 | -1.9366 | 0.0000 |
| 202.68 | Breakeven 200 | -10267.56 | 10267.56 | 0.00 | -1.9557 | 0.0000 |
| 203.68 | Breakeven 201 | -10367.89 | 10367.89 | 0.00 | -1.9748 | 0.0000 |
| 204.68 | Breakeven 202 | -10468.23 | 10468.23 | 0.00 | -1.9939 | 0.0000 |
| 205.69 | Breakeven 203 | -10568.56 | 10568.56 | 0.00 | -2.0131 | 0.0000 |
| 206.69 | Breakeven 204 | -10668.90 | 10668.90 | 0.00 | -2.0322 | 0.0000 |
| 207.69 | Breakeven 205 | -10769.23 | 10769.23 | 0.00 | -2.0513 | 0.0000 |
| 208.70 | Breakeven 206 | -10869.57 | 10869.57 | 0.00 | -2.0704 | 0.0000 |
| 209.70 | Breakeven 207 | -10969.90 | 10969.90 | 0.00 | -2.0895 | 0.0000 |
| 210.70 | Breakeven 208 | -11070.23 | 11070.23 | 0.00 | -2.1086 | 0.0000 |
| 211.71 | Breakeven 209 | -11170.57 | 11170.57 | 0.00 | -2.1277 | 0.0000 |
| 212.71 | Breakeven 210 | -11270.90 | 11270.90 | 0.00 | -2.1468 | 0.0000 |
| 213.71 | Breakeven 211 | -11371.24 | 11371.24 | 0.00 | -2.1660 | 0.0000 |
| 214.72 | Breakeven 212 | -11471.57 | 11471.57 | 0.00 | -2.1851 | 0.0000 |
| 215.72 | Breakeven 213 | -11571.91 | 11571.91 | 0.00 | -2.2042 | 0.0000 |
| 216.72 | Breakeven 214 | -11672.24 | 11672.24 | 0.00 | -2.2233 | 0.0000 |
| 217.73 | Breakeven 215 | -11772.58 | 11772.58 | 0.00 | -2.2424 | 0.0000 |
| 218.73 | Breakeven 216 | -11872.91 | 11872.91 | 0.00 | -2.2615 | 0.0000 |
| 219.73 | Breakeven 217 | -11973.24 | 11973.24 | 0.00 | -2.2806 | 0.0000 |
| 220.74 | Breakeven 218 | -12073.58 | 12073.58 | 0.00 | -2.2997 | 0.0000 |
| 221.74 | Breakeven 219 | -12173.91 | 12173.91 | 0.00 | -2.3188 | 0.0000 |
| 222.74 | Breakeven 220 | -12274.25 | 12274.25 | 0.00 | -2.3380 | 0.0000 |
| 223.75 | Breakeven 221 | -12374.58 | 12374.58 | 0.00 | -2.3571 | 0.0000 |
| 224.75 | Breakeven 222 | -12474.92 | 12474.92 | 0.00 | -2.3762 | 0.0000 |
| 225.75 | Breakeven 223 | -12575.25 | 12575.25 | 0.00 | -2.3953 | 0.0000 |
| 226.76 | Breakeven 224 | -12675.59 | 12675.59 | 0.00 | -2.4144 | 0.0000 |
| 227.76 | Breakeven 225 | -12775.92 | 12775.92 | 0.00 | -2.4335 | 0.0000 |
| 228.76 | Breakeven 226 | -12876.25 | 12876.25 | 0.00 | -2.4526 | 0.0000 |
| 229.77 | Breakeven 227 | -12976.59 | 12976.59 | 0.00 | -2.4717 | 0.0000 |
| 230.77 | Breakeven 228 | -13076.92 | 13076.92 | 0.00 | -2.4908 | 0.0000 |
| 231.77 | Breakeven 229 | -13177.26 | 13177.26 | 0.00 | -2.5100 | 0.0000 |
| 232.78 | Breakeven 230 | -13277.59 | 13277.59 | 0.00 | -2.5291 | 0.0000 |
| 233.78 | Breakeven 231 | -13377.93 | 13377.93 | 0.00 | -2.5482 | 0.0000 |
| 234.78 | Breakeven 232 | -13478.26 | 13478.26 | 0.00 | -2.5673 | 0.0000 |
| 235.79 | Breakeven 233 | -13578.60 | 13578.60 | 0.00 | -2.5864 | 0.0000 |
| 236.79 | Breakeven 234 | -13678.93 | 13678.93 | 0.00 | -2.6055 | 0.0000 |
| 237.79 | Breakeven 235 | -13779.26 | 13779.26 | 0.00 | -2.6246 | 0.0000 |
| 238.80 | Breakeven 236 | -13879.60 | 13879.60 | 0.00 | -2.6437 | 0.0000 |
| 239.80 | Breakeven 237 | -13979.93 | 13979.93 | 0.00 | -2.6628 | 0.0000 |
| 240.80 | Breakeven 238 | -14080.27 | 14080.27 | 0.00 | -2.6820 | 0.0000 |
| 241.81 | Breakeven 239 | -14180.60 | 14180.60 | 0.00 | -2.7011 | 0.0000 |
| 242.81 | Breakeven 240 | -14280.94 | 14280.94 | 0.00 | -2.7202 | 0.0000 |
| 243.81 | Breakeven 241 | -14381.27 | 14381.27 | 0.00 | -2.7393 | 0.0000 |
| 244.82 | Breakeven 242 | -14481.61 | 14481.61 | 0.00 | -2.7584 | 0.0000 |
| 245.82 | Breakeven 243 | -14581.94 | 14581.94 | 0.00 | -2.7775 | 0.0000 |
| 246.82 | Breakeven 244 | -14682.27 | 14682.27 | 0.00 | -2.7966 | 0.0000 |
| 247.83 | Breakeven 245 | -14782.61 | 14782.61 | 0.00 | -2.8157 | 0.0000 |
| 248.83 | Breakeven 246 | -14882.94 | 14882.94 | 0.00 | -2.8348 | 0.0000 |
| 249.83 | Breakeven 247 | -14983.28 | 14983.28 | 0.00 | -2.8540 | 0.0000 |
| 250.84 | Breakeven 248 | -15083.61 | 15083.61 | 0.00 | -2.8731 | 0.0000 |
| 251.84 | Breakeven 249 | -15183.95 | 15183.95 | 0.00 | -2.8922 | 0.0000 |
| 252.84 | Breakeven 250 | -15284.28 | 15284.28 | 0.00 | -2.9113 | 0.0000 |
| 253.85 | Breakeven 251 | -15384.62 | 15384.62 | 0.00 | -2.9304 | 0.0000 |
| 254.85 | Breakeven 252 | -15484.95 | 15484.95 | 0.00 | -2.9495 | 0.0000 |
| 255.85 | Breakeven 253 | -15585.28 | 15585.28 | 0.00 | -2.9686 | 0.0000 |
| 256.86 | Breakeven 254 | -15685.62 | 15685.62 | 0.00 | -2.9877 | 0.0000 |
| 257.86 | Breakeven 255 | -15785.95 | 15785.95 | 0.00 | -3.0068 | 0.0000 |
| 258.86 | Breakeven 256 | -15886.29 | 15886.29 | 0.00 | -3.0260 | 0.0000 |
| 259.87 | Breakeven 257 | -15986.62 | 15986.62 | 0.00 | -3.0451 | 0.0000 |
| 260.87 | Breakeven 258 | -16086.96 | 16086.96 | 0.00 | -3.0642 | 0.0000 |
| 261.87 | Breakeven 259 | -16187.29 | 16187.29 | 0.00 | -3.0833 | 0.0000 |
| 262.88 | Breakeven 260 | -16287.63 | 16287.63 | 0.00 | -3.1024 | 0.0000 |
| 263.88 | Breakeven 261 | -16387.96 | 16387.96 | 0.00 | -3.1215 | 0.0000 |
| 264.88 | Breakeven 262 | -16488.29 | 16488.29 | 0.00 | -3.1406 | 0.0000 |
| 265.89 | Breakeven 263 | -16588.63 | 16588.63 | 0.00 | -3.1597 | 0.0000 |
| 266.89 | Breakeven 264 | -16688.96 | 16688.96 | 0.00 | -3.1789 | 0.0000 |
| 267.89 | Breakeven 265 | -16789.30 | 16789.30 | 0.00 | -3.1980 | 0.0000 |
| 268.90 | Breakeven 266 | -16889.63 | 16889.63 | 0.00 | -3.2171 | 0.0000 |
| 269.90 | Breakeven 267 | -16989.97 | 16989.97 | 0.00 | -3.2362 | 0.0000 |
| 270.90 | Breakeven 268 | -17090.30 | 17090.30 | 0.00 | -3.2553 | 0.0000 |
| 271.91 | Breakeven 269 | -17190.64 | 17190.64 | 0.00 | -3.2744 | 0.0000 |
| 272.91 | Breakeven 270 | -17290.97 | 17290.97 | 0.00 | -3.2935 | 0.0000 |
| 273.91 | Breakeven 271 | -17391.30 | 17391.30 | 0.00 | -3.3126 | 0.0000 |
| 274.92 | Breakeven 272 | -17491.64 | 17491.64 | 0.00 | -3.3317 | 0.0000 |
| 275.92 | Breakeven 273 | -17591.97 | 17591.97 | 0.00 | -3.3509 | 0.0000 |
| 276.92 | Breakeven 274 | -17692.31 | 17692.31 | 0.00 | -3.3700 | 0.0000 |
| 277.93 | Breakeven 275 | -17792.64 | 17792.64 | 0.00 | -3.3891 | 0.0000 |
| 278.93 | Breakeven 276 | -17892.98 | 17892.98 | 0.00 | -3.4082 | 0.0000 |
| 279.93 | Breakeven 277 | -17993.31 | 17993.31 | 0.00 | -3.4273 | 0.0000 |
| 280.94 | Breakeven 278 | -18093.65 | 18093.65 | 0.00 | -3.4464 | 0.0000 |
| 281.94 | Breakeven 279 | -18193.98 | 18193.98 | 0.00 | -3.4655 | 0.0000 |
| 282.94 | Breakeven 280 | -18294.31 | 18294.31 | 0.00 | -3.4846 | 0.0000 |
| 283.95 | Breakeven 281 | -18394.65 | 18394.65 | 0.00 | -3.5037 | 0.0000 |
| 284.95 | Breakeven 282 | -18494.98 | 18494.98 | 0.00 | -3.5229 | 0.0000 |
| 285.95 | Breakeven 283 | -18595.32 | 18595.32 | 0.00 | -3.5420 | 0.0000 |
| 286.96 | Breakeven 284 | -18695.65 | 18695.65 | 0.00 | -3.5611 | 0.0000 |
| 287.96 | Breakeven 285 | -18795.99 | 18795.99 | 0.00 | -3.5802 | 0.0000 |
| 288.96 | Breakeven 286 | -18896.32 | 18896.32 | 0.00 | -3.5993 | 0.0000 |
| 289.97 | Breakeven 287 | -18996.66 | 18996.66 | 0.00 | -3.6184 | 0.0000 |
| 290.97 | Breakeven 288 | -19096.99 | 19096.99 | 0.00 | -3.6375 | 0.0000 |
| 291.97 | Breakeven 289 | -19197.32 | 19197.32 | 0.00 | -3.6566 | 0.0000 |
| 292.98 | Breakeven 290 | -19297.66 | 19297.66 | 0.00 | -3.6757 | 0.0000 |
| 293.98 | Breakeven 291 | -19397.99 | 19397.99 | 0.00 | -3.6949 | 0.0000 |
| 294.98 | Breakeven 292 | -19498.33 | 19498.33 | 0.00 | -3.7140 | 0.0000 |
| 295.99 | Breakeven 293 | -19598.66 | 19598.66 | 0.00 | -3.7331 | 0.0000 |
| 296.99 | Breakeven 294 | -19699.00 | 19699.00 | 0.00 | -3.7522 | 0.0000 |
| 297.99 | Breakeven 295 | -19799.33 | 19799.33 | 0.00 | -3.7713 | 0.0000 |
| 299.00 | Breakeven 296 | -19899.67 | 19899.67 | 0.00 | -3.7904 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| breakeven_1 | Breakeven 1 | 0.00 | -100.00% | 10000.00 | 0.00 | 0.0000 |
| zero | Stock to Zero | 0.00 | -100.00% | 10000.00 | 0.00 | 0.0000 |
| breakeven_2 | Breakeven 2 | 1.00 | -99.00% | 9899.67 | 0.00 | 0.0000 |
| breakeven_3 | Breakeven 3 | 2.01 | -97.99% | 9799.33 | 0.00 | 0.0000 |
| breakeven_4 | Breakeven 4 | 3.01 | -96.99% | 9699.00 | 0.00 | 0.0000 |
| breakeven_5 | Breakeven 5 | 4.01 | -95.99% | 9598.66 | 0.00 | 0.0000 |
| breakeven_6 | Breakeven 6 | 5.02 | -94.98% | 9498.33 | 0.00 | 0.0000 |
| breakeven_7 | Breakeven 7 | 6.02 | -93.98% | 9397.99 | 0.00 | 0.0000 |
| breakeven_8 | Breakeven 8 | 7.02 | -92.98% | 9297.66 | 0.00 | 0.0000 |
| breakeven_9 | Breakeven 9 | 8.03 | -91.97% | 9197.32 | 0.00 | 0.0000 |
| breakeven_10 | Breakeven 10 | 9.03 | -90.97% | 9096.99 | 0.00 | 0.0000 |
| breakeven_11 | Breakeven 11 | 10.03 | -89.97% | 8996.66 | 0.00 | 0.0000 |
| breakeven_12 | Breakeven 12 | 11.04 | -88.96% | 8896.32 | 0.00 | 0.0000 |
| breakeven_13 | Breakeven 13 | 12.04 | -87.96% | 8795.99 | 0.00 | 0.0000 |
| breakeven_14 | Breakeven 14 | 13.04 | -86.96% | 8695.65 | 0.00 | 0.0000 |
| breakeven_15 | Breakeven 15 | 14.05 | -85.95% | 8595.32 | 0.00 | 0.0000 |
| breakeven_16 | Breakeven 16 | 15.05 | -84.95% | 8494.98 | 0.00 | 0.0000 |
| breakeven_17 | Breakeven 17 | 17.06 | -82.94% | 8294.31 | 0.00 | 0.0000 |
| breakeven_18 | Breakeven 18 | 18.06 | -81.94% | 8193.98 | -0.00 | -0.0000 |
| breakeven_19 | Breakeven 19 | 19.06 | -80.94% | 8093.65 | 0.00 | 0.0000 |
| breakeven_20 | Breakeven 20 | 20.07 | -79.93% | 7993.31 | 0.00 | 0.0000 |
| breakeven_21 | Breakeven 21 | 21.07 | -78.93% | 7892.98 | 0.00 | 0.0000 |
| breakeven_22 | Breakeven 22 | 22.07 | -77.93% | 7792.64 | 0.00 | 0.0000 |
| breakeven_23 | Breakeven 23 | 23.08 | -76.92% | 7692.31 | 0.00 | 0.0000 |
| breakeven_24 | Breakeven 24 | 24.08 | -75.92% | 7591.97 | 0.00 | 0.0000 |
| breakeven_25 | Breakeven 25 | 25.08 | -74.92% | 7491.64 | 0.00 | 0.0000 |
| breakeven_26 | Breakeven 26 | 26.09 | -73.91% | 7391.30 | 0.00 | 0.0000 |
| breakeven_27 | Breakeven 27 | 27.09 | -72.91% | 7290.97 | 0.00 | 0.0000 |
| breakeven_28 | Breakeven 28 | 28.09 | -71.91% | 7190.64 | 0.00 | 0.0000 |
| breakeven_29 | Breakeven 29 | 29.10 | -70.90% | 7090.30 | 0.00 | 0.0000 |
| breakeven_30 | Breakeven 30 | 30.10 | -69.90% | 6989.97 | 0.00 | 0.0000 |
| breakeven_31 | Breakeven 31 | 31.10 | -68.90% | 6889.63 | 0.00 | 0.0000 |
| breakeven_32 | Breakeven 32 | 32.11 | -67.89% | 6789.30 | 0.00 | 0.0000 |
| breakeven_33 | Breakeven 33 | 33.11 | -66.89% | 6688.96 | 0.00 | 0.0000 |
| breakeven_34 | Breakeven 34 | 34.11 | -65.89% | 6588.63 | 0.00 | 0.0000 |
| breakeven_35 | Breakeven 35 | 35.12 | -64.88% | 6488.29 | 0.00 | 0.0000 |
| breakeven_36 | Breakeven 36 | 36.12 | -63.88% | 6387.96 | 0.00 | 0.0000 |
| breakeven_37 | Breakeven 37 | 37.12 | -62.88% | 6287.63 | 0.00 | 0.0000 |
| breakeven_38 | Breakeven 38 | 38.13 | -61.87% | 6187.29 | 0.00 | 0.0000 |
| breakeven_39 | Breakeven 39 | 39.13 | -60.87% | 6086.96 | 0.00 | 0.0000 |
| breakeven_40 | Breakeven 40 | 40.13 | -59.87% | 5986.62 | 0.00 | 0.0000 |
| breakeven_41 | Breakeven 41 | 41.14 | -58.86% | 5886.29 | 0.00 | 0.0000 |
| breakeven_42 | Breakeven 42 | 42.14 | -57.86% | 5785.95 | 0.00 | 0.0000 |
| breakeven_43 | Breakeven 43 | 43.14 | -56.86% | 5685.62 | 0.00 | 0.0000 |
| breakeven_44 | Breakeven 44 | 44.15 | -55.85% | 5585.28 | 0.00 | 0.0000 |
| breakeven_45 | Breakeven 45 | 45.15 | -54.85% | 5484.95 | 0.00 | 0.0000 |
| breakeven_46 | Breakeven 46 | 46.15 | -53.85% | 5384.62 | 0.00 | 0.0000 |
| breakeven_47 | Breakeven 47 | 47.16 | -52.84% | 5284.28 | 0.00 | 0.0000 |
| breakeven_48 | Breakeven 48 | 48.16 | -51.84% | 5183.95 | 0.00 | 0.0000 |
| breakeven_49 | Breakeven 49 | 49.16 | -50.84% | 5083.61 | 0.00 | 0.0000 |
| breakeven_50 | Breakeven 50 | 50.17 | -49.83% | 4983.28 | 0.00 | 0.0000 |
| breakeven_51 | Breakeven 51 | 51.17 | -48.83% | 4882.94 | 0.00 | 0.0000 |
| breakeven_52 | Breakeven 52 | 52.17 | -47.83% | 4782.61 | 0.00 | 0.0000 |
| breakeven_53 | Breakeven 53 | 53.18 | -46.82% | 4682.27 | 0.00 | 0.0000 |
| breakeven_54 | Breakeven 54 | 54.18 | -45.82% | 4581.94 | 0.00 | 0.0000 |
| breakeven_55 | Breakeven 55 | 55.18 | -44.82% | 4481.61 | 0.00 | 0.0000 |
| breakeven_56 | Breakeven 56 | 56.19 | -43.81% | 4381.27 | 0.00 | 0.0000 |
| breakeven_57 | Breakeven 57 | 58.19 | -41.81% | 4180.60 | 0.00 | 0.0000 |
| breakeven_58 | Breakeven 58 | 59.20 | -40.80% | 4080.27 | 0.00 | 0.0000 |
| breakeven_59 | Breakeven 59 | 60.20 | -39.80% | 3979.93 | 0.00 | 0.0000 |
| breakeven_60 | Breakeven 60 | 61.20 | -38.80% | 3879.60 | 0.00 | 0.0000 |
| breakeven_61 | Breakeven 61 | 62.21 | -37.79% | 3779.26 | 0.00 | 0.0000 |
| breakeven_62 | Breakeven 62 | 63.21 | -36.79% | 3678.93 | 0.00 | 0.0000 |
| breakeven_63 | Breakeven 63 | 64.21 | -35.79% | 3578.60 | 0.00 | 0.0000 |
| breakeven_64 | Breakeven 64 | 65.22 | -34.78% | 3478.26 | 0.00 | 0.0000 |
| breakeven_65 | Breakeven 65 | 66.22 | -33.78% | 3377.93 | 0.00 | 0.0000 |
| breakeven_66 | Breakeven 66 | 67.22 | -32.78% | 3277.59 | 0.00 | 0.0000 |
| breakeven_67 | Breakeven 67 | 68.23 | -31.77% | 3177.26 | 0.00 | 0.0000 |
| breakeven_68 | Breakeven 68 | 69.23 | -30.77% | 3076.92 | 0.00 | 0.0000 |
| breakeven_69 | Breakeven 69 | 70.23 | -29.77% | 2976.59 | 0.00 | 0.0000 |
| breakeven_70 | Breakeven 70 | 71.24 | -28.76% | 2876.25 | 0.00 | 0.0000 |
| breakeven_71 | Breakeven 71 | 72.24 | -27.76% | 2775.92 | 0.00 | 0.0000 |
| breakeven_72 | Breakeven 72 | 73.24 | -26.76% | 2675.59 | 0.00 | 0.0000 |
| breakeven_73 | Breakeven 73 | 74.25 | -25.75% | 2575.25 | 0.00 | 0.0000 |
| breakeven_74 | Breakeven 74 | 75.25 | -24.75% | 2474.92 | 0.00 | 0.0000 |
| breakeven_75 | Breakeven 75 | 76.25 | -23.75% | 2374.58 | 0.00 | 0.0000 |
| breakeven_76 | Breakeven 76 | 77.26 | -22.74% | 2274.25 | 0.00 | 0.0000 |
| breakeven_77 | Breakeven 77 | 78.26 | -21.74% | 2173.91 | 0.00 | 0.0000 |
| breakeven_78 | Breakeven 78 | 79.26 | -20.74% | 2073.58 | -0.00 | -0.0000 |
| breakeven_79 | Breakeven 79 | 80.27 | -19.73% | 1973.24 | 0.00 | 0.0000 |
| breakeven_80 | Breakeven 80 | 81.27 | -18.73% | 1872.91 | 0.00 | 0.0000 |
| breakeven_81 | Breakeven 81 | 82.27 | -17.73% | 1772.58 | 0.00 | 0.0000 |
| breakeven_82 | Breakeven 82 | 83.28 | -16.72% | 1672.24 | 0.00 | 0.0000 |
| breakeven_83 | Breakeven 83 | 84.28 | -15.72% | 1571.91 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1500.00 | 0.00 | 0.0000 |
| breakeven_84 | Breakeven 84 | 85.28 | -14.72% | 1471.57 | 0.00 | 0.0000 |
| breakeven_85 | Breakeven 85 | 86.29 | -13.71% | 1371.24 | 0.00 | 0.0000 |
| breakeven_86 | Breakeven 86 | 87.29 | -12.71% | 1270.90 | 0.00 | 0.0000 |
| breakeven_87 | Breakeven 87 | 88.29 | -11.71% | 1170.57 | 0.00 | 0.0000 |
| breakeven_88 | Breakeven 88 | 89.30 | -10.70% | 1070.23 | 0.00 | 0.0000 |
| breakeven_89 | Breakeven 89 | 90.30 | -9.70% | 969.90 | 0.00 | 0.0000 |
| breakeven_90 | Breakeven 90 | 91.30 | -8.70% | 869.57 | 0.00 | 0.0000 |
| breakeven_91 | Breakeven 91 | 92.31 | -7.69% | 769.23 | 0.00 | 0.0000 |
| breakeven_92 | Breakeven 92 | 93.31 | -6.69% | 668.90 | 0.00 | 0.0000 |
| breakeven_93 | Breakeven 93 | 94.31 | -5.69% | 568.56 | 0.00 | 0.0000 |
| breakeven_94 | Breakeven 94 | 95.32 | -4.68% | 468.23 | 0.00 | 0.0000 |
| breakeven_95 | Breakeven 95 | 96.32 | -3.68% | 367.89 | 0.00 | 0.0000 |
| breakeven_96 | Breakeven 96 | 97.32 | -2.68% | 267.56 | 0.00 | 0.0000 |
| breakeven_97 | Breakeven 97 | 98.33 | -1.67% | 167.22 | 0.00 | 0.0000 |
| breakeven_98 | Breakeven 98 | 99.33 | -0.67% | 66.89 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_99 | Breakeven 99 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_100 | Breakeven 100 | 100.33 | 0.33% | -33.44 | 0.00 | 0.0000 |
| breakeven_101 | Breakeven 101 | 101.34 | 1.34% | -133.78 | 0.00 | 0.0000 |
| breakeven_102 | Breakeven 102 | 102.34 | 2.34% | -234.11 | 0.00 | 0.0000 |
| breakeven_103 | Breakeven 103 | 103.34 | 3.34% | -334.45 | 0.00 | 0.0000 |
| breakeven_104 | Breakeven 104 | 104.35 | 4.35% | -434.78 | 0.00 | 0.0000 |
| breakeven_105 | Breakeven 105 | 105.35 | 5.35% | -535.12 | 0.00 | 0.0000 |
| breakeven_106 | Breakeven 106 | 106.35 | 6.35% | -635.45 | 0.00 | 0.0000 |
| breakeven_107 | Breakeven 107 | 107.36 | 7.36% | -735.79 | 0.00 | 0.0000 |
| breakeven_108 | Breakeven 108 | 108.36 | 8.36% | -836.12 | 0.00 | 0.0000 |
| breakeven_109 | Breakeven 109 | 109.36 | 9.36% | -936.45 | 0.00 | 0.0000 |
| breakeven_110 | Breakeven 110 | 110.37 | 10.37% | -1036.79 | 0.00 | 0.0000 |
| breakeven_111 | Breakeven 111 | 111.37 | 11.37% | -1137.12 | 0.00 | 0.0000 |
| breakeven_112 | Breakeven 112 | 112.37 | 12.37% | -1237.46 | 0.00 | 0.0000 |
| breakeven_113 | Breakeven 113 | 113.38 | 13.38% | -1337.79 | 0.00 | 0.0000 |
| breakeven_114 | Breakeven 114 | 114.38 | 14.38% | -1438.13 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1500.00 | 0.00 | 0.0000 |
| breakeven_115 | Breakeven 115 | 115.38 | 15.38% | -1538.46 | 0.00 | 0.0000 |
| breakeven_116 | Breakeven 116 | 116.39 | 16.39% | -1638.80 | 0.00 | 0.0000 |
| breakeven_117 | Breakeven 117 | 117.39 | 17.39% | -1739.13 | 0.00 | 0.0000 |
| breakeven_118 | Breakeven 118 | 118.39 | 18.39% | -1839.46 | 0.00 | 0.0000 |
| breakeven_119 | Breakeven 119 | 119.40 | 19.40% | -1939.80 | 0.00 | 0.0000 |
| breakeven_120 | Breakeven 120 | 120.40 | 20.40% | -2040.13 | 0.00 | 0.0000 |
| breakeven_121 | Breakeven 121 | 122.41 | 22.41% | -2240.80 | 0.00 | 0.0000 |
| breakeven_122 | Breakeven 122 | 123.41 | 23.41% | -2341.14 | 0.00 | 0.0000 |
| breakeven_123 | Breakeven 123 | 124.41 | 24.41% | -2441.47 | 0.00 | 0.0000 |
| breakeven_124 | Breakeven 124 | 125.42 | 25.42% | -2541.81 | 0.00 | 0.0000 |
| breakeven_125 | Breakeven 125 | 126.42 | 26.42% | -2642.14 | 0.00 | 0.0000 |
| breakeven_126 | Breakeven 126 | 127.42 | 27.42% | -2742.47 | 0.00 | 0.0000 |
| breakeven_127 | Breakeven 127 | 128.43 | 28.43% | -2842.81 | 0.00 | 0.0000 |
| breakeven_128 | Breakeven 128 | 129.43 | 29.43% | -2943.14 | 0.00 | 0.0000 |
| breakeven_129 | Breakeven 129 | 130.43 | 30.43% | -3043.48 | 0.00 | 0.0000 |
| breakeven_130 | Breakeven 130 | 131.44 | 31.44% | -3143.81 | 0.00 | 0.0000 |
| breakeven_131 | Breakeven 131 | 132.44 | 32.44% | -3244.15 | 0.00 | 0.0000 |
| breakeven_132 | Breakeven 132 | 133.44 | 33.44% | -3344.48 | 0.00 | 0.0000 |
| breakeven_133 | Breakeven 133 | 134.45 | 34.45% | -3444.82 | 0.00 | 0.0000 |
| breakeven_134 | Breakeven 134 | 135.45 | 35.45% | -3545.15 | 0.00 | 0.0000 |
| breakeven_135 | Breakeven 135 | 136.45 | 36.45% | -3645.48 | 0.00 | 0.0000 |
| breakeven_136 | Breakeven 136 | 137.46 | 37.46% | -3745.82 | 0.00 | 0.0000 |
| breakeven_137 | Breakeven 137 | 138.46 | 38.46% | -3846.15 | 0.00 | 0.0000 |
| breakeven_138 | Breakeven 138 | 139.46 | 39.46% | -3946.49 | 0.00 | 0.0000 |
| breakeven_139 | Breakeven 139 | 140.47 | 40.47% | -4046.82 | 0.00 | 0.0000 |
| breakeven_140 | Breakeven 140 | 141.47 | 41.47% | -4147.16 | 0.00 | 0.0000 |
| breakeven_141 | Breakeven 141 | 142.47 | 42.47% | -4247.49 | 0.00 | 0.0000 |
| breakeven_142 | Breakeven 142 | 143.48 | 43.48% | -4347.83 | 0.00 | 0.0000 |
| breakeven_143 | Breakeven 143 | 144.48 | 44.48% | -4448.16 | 0.00 | 0.0000 |
| breakeven_144 | Breakeven 144 | 145.48 | 45.48% | -4548.49 | 0.00 | 0.0000 |
| breakeven_145 | Breakeven 145 | 146.49 | 46.49% | -4648.83 | 0.00 | 0.0000 |
| breakeven_146 | Breakeven 146 | 147.49 | 47.49% | -4749.16 | 0.00 | 0.0000 |
| breakeven_147 | Breakeven 147 | 148.49 | 48.49% | -4849.50 | 0.00 | 0.0000 |
| breakeven_148 | Breakeven 148 | 149.50 | 49.50% | -4949.83 | 0.00 | 0.0000 |
| breakeven_149 | Breakeven 149 | 150.50 | 50.50% | -5050.17 | 0.00 | 0.0000 |
| breakeven_150 | Breakeven 150 | 151.51 | 51.51% | -5150.50 | 0.00 | 0.0000 |
| breakeven_151 | Breakeven 151 | 152.51 | 52.51% | -5250.84 | 0.00 | 0.0000 |
| breakeven_152 | Breakeven 152 | 153.51 | 53.51% | -5351.17 | 0.00 | 0.0000 |
| breakeven_153 | Breakeven 153 | 154.52 | 54.52% | -5451.51 | 0.00 | 0.0000 |
| breakeven_154 | Breakeven 154 | 155.52 | 55.52% | -5551.84 | 0.00 | 0.0000 |
| breakeven_155 | Breakeven 155 | 156.52 | 56.52% | -5652.17 | 0.00 | 0.0000 |
| breakeven_156 | Breakeven 156 | 157.53 | 57.53% | -5752.51 | 0.00 | 0.0000 |
| breakeven_157 | Breakeven 157 | 158.53 | 58.53% | -5852.84 | 0.00 | 0.0000 |
| breakeven_158 | Breakeven 158 | 159.53 | 59.53% | -5953.18 | 0.00 | 0.0000 |
| breakeven_159 | Breakeven 159 | 160.54 | 60.54% | -6053.51 | 0.00 | 0.0000 |
| breakeven_160 | Breakeven 160 | 161.54 | 61.54% | -6153.85 | 0.00 | 0.0000 |
| breakeven_161 | Breakeven 161 | 162.54 | 62.54% | -6254.18 | 0.00 | 0.0000 |
| breakeven_162 | Breakeven 162 | 163.55 | 63.55% | -6354.52 | 0.00 | 0.0000 |
| breakeven_163 | Breakeven 163 | 164.55 | 64.55% | -6454.85 | 0.00 | 0.0000 |
| breakeven_164 | Breakeven 164 | 165.55 | 65.55% | -6555.18 | 0.00 | 0.0000 |
| breakeven_165 | Breakeven 165 | 166.56 | 66.56% | -6655.52 | 0.00 | 0.0000 |
| breakeven_166 | Breakeven 166 | 167.56 | 67.56% | -6755.85 | 0.00 | 0.0000 |
| breakeven_167 | Breakeven 167 | 168.56 | 68.56% | -6856.19 | 0.00 | 0.0000 |
| breakeven_168 | Breakeven 168 | 169.57 | 69.57% | -6956.52 | 0.00 | 0.0000 |
| breakeven_169 | Breakeven 169 | 170.57 | 70.57% | -7056.86 | 0.00 | 0.0000 |
| breakeven_170 | Breakeven 170 | 171.57 | 71.57% | -7157.19 | 0.00 | 0.0000 |
| breakeven_171 | Breakeven 171 | 172.58 | 72.58% | -7257.53 | 0.00 | 0.0000 |
| breakeven_172 | Breakeven 172 | 173.58 | 73.58% | -7357.86 | 0.00 | 0.0000 |
| breakeven_173 | Breakeven 173 | 174.58 | 74.58% | -7458.19 | 0.00 | 0.0000 |
| breakeven_174 | Breakeven 174 | 175.59 | 75.59% | -7558.53 | 0.00 | 0.0000 |
| breakeven_175 | Breakeven 175 | 176.59 | 76.59% | -7658.86 | 0.00 | 0.0000 |
| breakeven_176 | Breakeven 176 | 177.59 | 77.59% | -7759.20 | 0.00 | 0.0000 |
| breakeven_177 | Breakeven 177 | 178.60 | 78.60% | -7859.53 | 0.00 | 0.0000 |
| breakeven_178 | Breakeven 178 | 179.60 | 79.60% | -7959.87 | 0.00 | 0.0000 |
| breakeven_179 | Breakeven 179 | 180.60 | 80.60% | -8060.20 | 0.00 | 0.0000 |
| breakeven_180 | Breakeven 180 | 181.61 | 81.61% | -8160.54 | 0.00 | 0.0000 |
| breakeven_181 | Breakeven 181 | 183.61 | 83.61% | -8361.20 | 0.00 | 0.0000 |
| breakeven_182 | Breakeven 182 | 184.62 | 84.62% | -8461.54 | 0.00 | 0.0000 |
| breakeven_183 | Breakeven 183 | 185.62 | 85.62% | -8561.87 | 0.00 | 0.0000 |
| breakeven_184 | Breakeven 184 | 186.62 | 86.62% | -8662.21 | 0.00 | 0.0000 |
| breakeven_185 | Breakeven 185 | 187.63 | 87.63% | -8762.54 | 0.00 | 0.0000 |
| breakeven_186 | Breakeven 186 | 188.63 | 88.63% | -8862.88 | 0.00 | 0.0000 |
| breakeven_187 | Breakeven 187 | 189.63 | 89.63% | -8963.21 | 0.00 | 0.0000 |
| breakeven_188 | Breakeven 188 | 190.64 | 90.64% | -9063.55 | 0.00 | 0.0000 |
| breakeven_189 | Breakeven 189 | 191.64 | 91.64% | -9163.88 | 0.00 | 0.0000 |
| breakeven_190 | Breakeven 190 | 192.64 | 92.64% | -9264.21 | 0.00 | 0.0000 |
| breakeven_191 | Breakeven 191 | 193.65 | 93.65% | -9364.55 | 0.00 | 0.0000 |
| breakeven_192 | Breakeven 192 | 194.65 | 94.65% | -9464.88 | 0.00 | 0.0000 |
| breakeven_193 | Breakeven 193 | 195.65 | 95.65% | -9565.22 | 0.00 | 0.0000 |
| breakeven_194 | Breakeven 194 | 196.66 | 96.66% | -9665.55 | 0.00 | 0.0000 |
| breakeven_195 | Breakeven 195 | 197.66 | 97.66% | -9765.89 | 0.00 | 0.0000 |
| breakeven_196 | Breakeven 196 | 198.66 | 98.66% | -9866.22 | 0.00 | 0.0000 |
| breakeven_197 | Breakeven 197 | 199.67 | 99.67% | -9966.56 | 0.00 | 0.0000 |
| breakeven_198 | Breakeven 198 | 200.67 | 100.67% | -10066.89 | 0.00 | 0.0000 |
| breakeven_199 | Breakeven 199 | 201.67 | 101.67% | -10167.22 | 0.00 | 0.0000 |
| breakeven_200 | Breakeven 200 | 202.68 | 102.68% | -10267.56 | 0.00 | 0.0000 |
| breakeven_201 | Breakeven 201 | 203.68 | 103.68% | -10367.89 | 0.00 | 0.0000 |
| breakeven_202 | Breakeven 202 | 204.68 | 104.68% | -10468.23 | 0.00 | 0.0000 |
| breakeven_203 | Breakeven 203 | 205.69 | 105.69% | -10568.56 | 0.00 | 0.0000 |
| breakeven_204 | Breakeven 204 | 206.69 | 106.69% | -10668.90 | 0.00 | 0.0000 |
| breakeven_205 | Breakeven 205 | 207.69 | 107.69% | -10769.23 | 0.00 | 0.0000 |
| breakeven_206 | Breakeven 206 | 208.70 | 108.70% | -10869.57 | 0.00 | 0.0000 |
| breakeven_207 | Breakeven 207 | 209.70 | 109.70% | -10969.90 | 0.00 | 0.0000 |
| breakeven_208 | Breakeven 208 | 210.70 | 110.70% | -11070.23 | 0.00 | 0.0000 |
| breakeven_209 | Breakeven 209 | 211.71 | 111.71% | -11170.57 | 0.00 | 0.0000 |
| breakeven_210 | Breakeven 210 | 212.71 | 112.71% | -11270.90 | 0.00 | 0.0000 |
| breakeven_211 | Breakeven 211 | 213.71 | 113.71% | -11371.24 | 0.00 | 0.0000 |
| breakeven_212 | Breakeven 212 | 214.72 | 114.72% | -11471.57 | 0.00 | 0.0000 |
| breakeven_213 | Breakeven 213 | 215.72 | 115.72% | -11571.91 | 0.00 | 0.0000 |
| breakeven_214 | Breakeven 214 | 216.72 | 116.72% | -11672.24 | 0.00 | 0.0000 |
| breakeven_215 | Breakeven 215 | 217.73 | 117.73% | -11772.58 | 0.00 | 0.0000 |
| breakeven_216 | Breakeven 216 | 218.73 | 118.73% | -11872.91 | 0.00 | 0.0000 |
| breakeven_217 | Breakeven 217 | 219.73 | 119.73% | -11973.24 | 0.00 | 0.0000 |
| breakeven_218 | Breakeven 218 | 220.74 | 120.74% | -12073.58 | 0.00 | 0.0000 |
| breakeven_219 | Breakeven 219 | 221.74 | 121.74% | -12173.91 | 0.00 | 0.0000 |
| breakeven_220 | Breakeven 220 | 222.74 | 122.74% | -12274.25 | 0.00 | 0.0000 |
| breakeven_221 | Breakeven 221 | 223.75 | 123.75% | -12374.58 | 0.00 | 0.0000 |
| breakeven_222 | Breakeven 222 | 224.75 | 124.75% | -12474.92 | 0.00 | 0.0000 |
| breakeven_223 | Breakeven 223 | 225.75 | 125.75% | -12575.25 | 0.00 | 0.0000 |
| breakeven_224 | Breakeven 224 | 226.76 | 126.76% | -12675.59 | 0.00 | 0.0000 |
| breakeven_225 | Breakeven 225 | 227.76 | 127.76% | -12775.92 | 0.00 | 0.0000 |
| breakeven_226 | Breakeven 226 | 228.76 | 128.76% | -12876.25 | 0.00 | 0.0000 |
| breakeven_227 | Breakeven 227 | 229.77 | 129.77% | -12976.59 | 0.00 | 0.0000 |
| breakeven_228 | Breakeven 228 | 230.77 | 130.77% | -13076.92 | 0.00 | 0.0000 |
| breakeven_229 | Breakeven 229 | 231.77 | 131.77% | -13177.26 | 0.00 | 0.0000 |
| breakeven_230 | Breakeven 230 | 232.78 | 132.78% | -13277.59 | 0.00 | 0.0000 |
| breakeven_231 | Breakeven 231 | 233.78 | 133.78% | -13377.93 | 0.00 | 0.0000 |
| breakeven_232 | Breakeven 232 | 234.78 | 134.78% | -13478.26 | 0.00 | 0.0000 |
| breakeven_233 | Breakeven 233 | 235.79 | 135.79% | -13578.60 | 0.00 | 0.0000 |
| breakeven_234 | Breakeven 234 | 236.79 | 136.79% | -13678.93 | 0.00 | 0.0000 |
| breakeven_235 | Breakeven 235 | 237.79 | 137.79% | -13779.26 | 0.00 | 0.0000 |
| breakeven_236 | Breakeven 236 | 238.80 | 138.80% | -13879.60 | 0.00 | 0.0000 |
| breakeven_237 | Breakeven 237 | 239.80 | 139.80% | -13979.93 | 0.00 | 0.0000 |
| breakeven_238 | Breakeven 238 | 240.80 | 140.80% | -14080.27 | 0.00 | 0.0000 |
| breakeven_239 | Breakeven 239 | 241.81 | 141.81% | -14180.60 | 0.00 | 0.0000 |
| breakeven_240 | Breakeven 240 | 242.81 | 142.81% | -14280.94 | 0.00 | 0.0000 |
| breakeven_241 | Breakeven 241 | 243.81 | 143.81% | -14381.27 | 0.00 | 0.0000 |
| breakeven_242 | Breakeven 242 | 244.82 | 144.82% | -14481.61 | 0.00 | 0.0000 |
| breakeven_243 | Breakeven 243 | 245.82 | 145.82% | -14581.94 | 0.00 | 0.0000 |
| breakeven_244 | Breakeven 244 | 246.82 | 146.82% | -14682.27 | 0.00 | 0.0000 |
| breakeven_245 | Breakeven 245 | 247.83 | 147.83% | -14782.61 | 0.00 | 0.0000 |
| breakeven_246 | Breakeven 246 | 248.83 | 148.83% | -14882.94 | 0.00 | 0.0000 |
| breakeven_247 | Breakeven 247 | 249.83 | 149.83% | -14983.28 | 0.00 | 0.0000 |
| breakeven_248 | Breakeven 248 | 250.84 | 150.84% | -15083.61 | 0.00 | 0.0000 |
| breakeven_249 | Breakeven 249 | 251.84 | 151.84% | -15183.95 | 0.00 | 0.0000 |
| breakeven_250 | Breakeven 250 | 252.84 | 152.84% | -15284.28 | 0.00 | 0.0000 |
| breakeven_251 | Breakeven 251 | 253.85 | 153.85% | -15384.62 | 0.00 | 0.0000 |
| breakeven_252 | Breakeven 252 | 254.85 | 154.85% | -15484.95 | 0.00 | 0.0000 |
| breakeven_253 | Breakeven 253 | 255.85 | 155.85% | -15585.28 | 0.00 | 0.0000 |
| breakeven_254 | Breakeven 254 | 256.86 | 156.86% | -15685.62 | 0.00 | 0.0000 |
| breakeven_255 | Breakeven 255 | 257.86 | 157.86% | -15785.95 | 0.00 | 0.0000 |
| breakeven_256 | Breakeven 256 | 258.86 | 158.86% | -15886.29 | 0.00 | 0.0000 |
| breakeven_257 | Breakeven 257 | 259.87 | 159.87% | -15986.62 | 0.00 | 0.0000 |
| breakeven_258 | Breakeven 258 | 260.87 | 160.87% | -16086.96 | 0.00 | 0.0000 |
| breakeven_259 | Breakeven 259 | 261.87 | 161.87% | -16187.29 | 0.00 | 0.0000 |
| breakeven_260 | Breakeven 260 | 262.88 | 162.88% | -16287.63 | 0.00 | 0.0000 |
| breakeven_261 | Breakeven 261 | 263.88 | 163.88% | -16387.96 | 0.00 | 0.0000 |
| breakeven_262 | Breakeven 262 | 264.88 | 164.88% | -16488.29 | 0.00 | 0.0000 |
| breakeven_263 | Breakeven 263 | 265.89 | 165.89% | -16588.63 | 0.00 | 0.0000 |
| breakeven_264 | Breakeven 264 | 266.89 | 166.89% | -16688.96 | 0.00 | 0.0000 |
| breakeven_265 | Breakeven 265 | 267.89 | 167.89% | -16789.30 | 0.00 | 0.0000 |
| breakeven_266 | Breakeven 266 | 268.90 | 168.90% | -16889.63 | 0.00 | 0.0000 |
| breakeven_267 | Breakeven 267 | 269.90 | 169.90% | -16989.97 | 0.00 | 0.0000 |
| breakeven_268 | Breakeven 268 | 270.90 | 170.90% | -17090.30 | 0.00 | 0.0000 |
| breakeven_269 | Breakeven 269 | 271.91 | 171.91% | -17190.64 | 0.00 | 0.0000 |
| breakeven_270 | Breakeven 270 | 272.91 | 172.91% | -17290.97 | 0.00 | 0.0000 |
| breakeven_271 | Breakeven 271 | 273.91 | 173.91% | -17391.30 | 0.00 | 0.0000 |
| breakeven_272 | Breakeven 272 | 274.92 | 174.92% | -17491.64 | 0.00 | 0.0000 |
| breakeven_273 | Breakeven 273 | 275.92 | 175.92% | -17591.97 | 0.00 | 0.0000 |
| breakeven_274 | Breakeven 274 | 276.92 | 176.92% | -17692.31 | 0.00 | 0.0000 |
| breakeven_275 | Breakeven 275 | 277.93 | 177.93% | -17792.64 | 0.00 | 0.0000 |
| breakeven_276 | Breakeven 276 | 278.93 | 178.93% | -17892.98 | 0.00 | 0.0000 |
| breakeven_277 | Breakeven 277 | 279.93 | 179.93% | -17993.31 | 0.00 | 0.0000 |
| breakeven_278 | Breakeven 278 | 280.94 | 180.94% | -18093.65 | 0.00 | 0.0000 |
| breakeven_279 | Breakeven 279 | 281.94 | 181.94% | -18193.98 | 0.00 | 0.0000 |
| breakeven_280 | Breakeven 280 | 282.94 | 182.94% | -18294.31 | 0.00 | 0.0000 |
| breakeven_281 | Breakeven 281 | 283.95 | 183.95% | -18394.65 | 0.00 | 0.0000 |
| breakeven_282 | Breakeven 282 | 284.95 | 184.95% | -18494.98 | 0.00 | 0.0000 |
| breakeven_283 | Breakeven 283 | 285.95 | 185.95% | -18595.32 | 0.00 | 0.0000 |
| breakeven_284 | Breakeven 284 | 286.96 | 186.96% | -18695.65 | 0.00 | 0.0000 |
| breakeven_285 | Breakeven 285 | 287.96 | 187.96% | -18795.99 | 0.00 | 0.0000 |
| breakeven_286 | Breakeven 286 | 288.96 | 188.96% | -18896.32 | 0.00 | 0.0000 |
| breakeven_287 | Breakeven 287 | 289.97 | 189.97% | -18996.66 | 0.00 | 0.0000 |
| breakeven_288 | Breakeven 288 | 290.97 | 190.97% | -19096.99 | 0.00 | 0.0000 |
| breakeven_289 | Breakeven 289 | 291.97 | 191.97% | -19197.32 | 0.00 | 0.0000 |
| breakeven_290 | Breakeven 290 | 292.98 | 192.98% | -19297.66 | 0.00 | 0.0000 |
| breakeven_291 | Breakeven 291 | 293.98 | 193.98% | -19397.99 | 0.00 | 0.0000 |
| breakeven_292 | Breakeven 292 | 294.98 | 194.98% | -19498.33 | 0.00 | 0.0000 |
| breakeven_293 | Breakeven 293 | 295.99 | 195.99% | -19598.66 | 0.00 | 0.0000 |
| breakeven_294 | Breakeven 294 | 296.99 | 196.99% | -19699.00 | 0.00 | 0.0000 |
| breakeven_295 | Breakeven 295 | 297.99 | 197.99% | -19799.33 | 0.00 | 0.0000 |
| breakeven_296 | Breakeven 296 | 299.00 | 199.00% | -19899.67 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | 0.00 | 0.0000 |

---

### Synthetic Short Stock (ID=50) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: COL_EQ
- Margin Classification: COL_EQ

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: []
- Options Max PnL: 10000.0
- Options Min PnL: -20000.0
- Combined Max PnL: 5000.0
- Combined Min PnL: 5000.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $10,000.00 | $5,000.00 |
| Max Loss | Unlimited | $5,000.00 |
| Risk Reward | 0.50x | 1.00x |
| Capital Basis | $5,250.00 | $10,250.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 5250.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.003285
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | 5000.00 | 0.00 | 5000.00 | 0.9524 | 0.4878 |
| 85.00 | Downside (15%) | 1500.00 | 3500.00 | 5000.00 | 0.2857 | 0.4878 |
| 100.00 | Current Market Price | 0.00 | 5000.00 | 5000.00 | 0.0000 | 0.4878 |
| 115.00 | Upside (15%) | -1500.00 | 6500.00 | 5000.00 | -0.2857 | 0.4878 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 10000.00 | 5000.00 | 0.4878 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1500.00 | 5000.00 | 0.4878 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 0.4878 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 0.4878 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1500.00 | 5000.00 | 0.4878 |
| infinity | Stock to Infinity | — | — | Unlimited | 5000.00 | 0.4878 |

---

### Synthetic Short Stock (ID=50) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: COL_EQ
- Margin Classification: COL_EQ

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: []
- Options Max PnL: 10000.0
- Options Min PnL: -20000.0
- Combined Max PnL: -1500.0
- Combined Min PnL: -1500.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $10,000.00 | -$1,500.00 |
| Max Loss | Unlimited | -$1,500.00 |
| Risk Reward | 0.50x | 1.00x |
| Capital Basis | $5,250.00 | $16,750.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 5250.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.003285
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1500.00 | -3000.00 | -1500.00 | 0.2857 | -0.0896 |
| 100.00 | Current Market Price | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.0896 |
| 115.00 | Upside (15%) | -1500.00 | 0.00 | -1500.00 | -0.2857 | -0.0896 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 10000.00 | -1500.00 | -0.0896 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1500.00 | -1500.00 | -0.0896 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.0896 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.0896 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1500.00 | -1500.00 | -0.0896 |
| infinity | Stock to Infinity | — | — | Unlimited | -1500.00 | -0.0896 |

---

### Long Combo (ID=51) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [92.0, 92.307692, 93.311037, 94.314381, 95.317726, 96.32107, 97.324415, 98.327759, 99.331104, 100.334448, 101.337793, 102.341137, 103.344482, 104.347826, 105.351171, 106.354515, 107.35786, 108.0]
- Options Max PnL: 19200.0
- Options Min PnL: -9200.0
- Combined Max PnL: 19200.0
- Combined Min PnL: -9200.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$9,200.00 | -$9,200.00 |
| Risk Reward | 2.09x | 2.09x |
| Capital Basis | $1,390.00 | $1,390.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 21.4% | 21.4% |
| Margin Proxy | 1390.0 | — |

**Probabilities:**

- PoP (raw): 0.213914
- Assignment Prob: 0.226367
- P(25% Max Profit): 7e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -700.00 | 0.00 | -700.00 | -0.0761 | -0.0761 |
| 92.00 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 92.31 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 93.31 | Breakeven 3 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 94.31 | Breakeven 4 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 95.32 | Breakeven 5 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 96.32 | Breakeven 6 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 97.32 | Breakeven 7 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 98.33 | Breakeven 8 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 99.33 | Breakeven 9 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.33 | Breakeven 10 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 101.34 | Breakeven 11 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 102.34 | Breakeven 12 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 103.34 | Breakeven 13 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 104.35 | Breakeven 14 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 105.35 | Breakeven 15 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 106.35 | Breakeven 16 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 107.36 | Breakeven 17 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Breakeven 18 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 700.00 | 0.00 | 700.00 | 0.0761 | 0.0761 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9200.00 | -9200.00 | -6.6187 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -700.00 | -700.00 | -0.0761 |
| strike_1 | Breakeven 1 | 92.00 | -8.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 92.00 | -8.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_2 | Breakeven 2 | 92.31 | -7.69% | 0.00 | 0.00 | 0.0000 |
| breakeven_3 | Breakeven 3 | 93.31 | -6.69% | 0.00 | 0.00 | 0.0000 |
| breakeven_4 | Breakeven 4 | 94.31 | -5.69% | 0.00 | 0.00 | 0.0000 |
| breakeven_5 | Breakeven 5 | 95.32 | -4.68% | 0.00 | 0.00 | 0.0000 |
| breakeven_6 | Breakeven 6 | 96.32 | -3.68% | 0.00 | 0.00 | 0.0000 |
| breakeven_7 | Breakeven 7 | 97.32 | -2.68% | 0.00 | 0.00 | 0.0000 |
| breakeven_8 | Breakeven 8 | 98.33 | -1.67% | 0.00 | 0.00 | 0.0000 |
| breakeven_9 | Breakeven 9 | 99.33 | -0.67% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_10 | Breakeven 10 | 100.33 | 0.33% | 0.00 | 0.00 | 0.0000 |
| breakeven_11 | Breakeven 11 | 101.34 | 1.34% | 0.00 | 0.00 | 0.0000 |
| breakeven_12 | Breakeven 12 | 102.34 | 2.34% | 0.00 | 0.00 | 0.0000 |
| breakeven_13 | Breakeven 13 | 103.34 | 3.34% | 0.00 | 0.00 | 0.0000 |
| breakeven_14 | Breakeven 14 | 104.35 | 4.35% | 0.00 | 0.00 | 0.0000 |
| breakeven_15 | Breakeven 15 | 105.35 | 5.35% | 0.00 | 0.00 | 0.0000 |
| breakeven_16 | Breakeven 16 | 106.35 | 6.35% | 0.00 | 0.00 | 0.0000 |
| breakeven_17 | Breakeven 17 | 107.36 | 7.36% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Breakeven 18 | 108.00 | 8.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_18 | Breakeven 18 | 108.00 | 8.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 700.00 | 700.00 | 0.0761 |
| infinity | Stock to Infinity | — | — | 97200.00 | 97200.00 | 69.9281 |

---

### Long Combo (ID=51) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [100.0]
- Options Max PnL: 19200.0
- Options Min PnL: -9200.0
- Combined Max PnL: 39200.0
- Combined Min PnL: -19200.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$9,200.00 | -$19,200.00 |
| Risk Reward | 2.09x | 2.04x |
| Capital Basis | $1,390.00 | $11,390.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 47.9% | 47.9% |
| Margin Proxy | 1390.0 | — |

**Probabilities:**

- PoP (raw): 0.47931
- Assignment Prob: 0.226367
- P(25% Max Profit): 7e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -700.00 | -1500.00 | -2200.00 | -0.0761 | -0.1146 |
| 92.00 | Lower Strike | 0.00 | -800.00 | -800.00 | 0.0000 | -0.0417 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | 0.00 | 800.00 | 800.00 | 0.0000 | 0.0417 |
| 115.00 | Upside (15%) | 700.00 | 1500.00 | 2200.00 | 0.0761 | 0.1146 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9200.00 | -19200.00 | -1.6857 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -700.00 | -2200.00 | -0.1146 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | -800.00 | -0.0417 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 800.00 | 0.0417 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 700.00 | 2200.00 | 0.1146 |
| infinity | Stock to Infinity | — | — | 97200.00 | 195200.00 | 17.1378 |

---

### Long Combo (ID=51) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [71.0]
- Options Max PnL: 19200.0
- Options Min PnL: -9200.0
- Combined Max PnL: 44200.0
- Combined Min PnL: -14200.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$9,200.00 | -$14,200.00 |
| Risk Reward | 2.09x | 3.11x |
| Capital Basis | $1,390.00 | $6,390.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 99.9% | 99.9% |
| Margin Proxy | 1390.0 | — |

**Probabilities:**

- PoP (raw): 0.999414
- Assignment Prob: 0.226367
- P(25% Max Profit): 7e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -4200.00 | 0.00 | -4200.00 | -0.4565 | -0.2958 |
| 71.00 | Breakeven 1 | -2100.00 | 2100.00 | 0.00 | -0.2283 | 0.0000 |
| 85.00 | Downside (15%) | -700.00 | 3500.00 | 2800.00 | -0.0761 | 0.1972 |
| 92.00 | Lower Strike | 0.00 | 4200.00 | 4200.00 | 0.0000 | 0.2958 |
| 100.00 | Current Market Price | 0.00 | 5000.00 | 5000.00 | 0.0000 | 0.3521 |
| 108.00 | Upper Strike | 0.00 | 5800.00 | 5800.00 | 0.0000 | 0.4085 |
| 115.00 | Upside (15%) | 700.00 | 6500.00 | 7200.00 | 0.0761 | 0.5070 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9200.00 | -14200.00 | -2.2222 |
| breakeven_1 | Breakeven 1 | 71.00 | -29.00% | -2100.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -700.00 | 2800.00 | 0.1972 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | 4200.00 | 0.2958 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 0.3521 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 5800.00 | 0.4085 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 700.00 | 7200.00 | 0.5070 |
| infinity | Stock to Infinity | — | — | 97200.00 | 200200.00 | 31.3302 |

---

### Long Combo (ID=51) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [111.5]
- Options Max PnL: 19200.0
- Options Min PnL: -9200.0
- Combined Max PnL: 37700.0
- Combined Min PnL: -20700.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$9,200.00 | -$20,700.00 |
| Risk Reward | 2.09x | 1.82x |
| Capital Basis | $1,390.00 | $12,890.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 13.6% | 13.6% |
| Margin Proxy | 1390.0 | — |

**Probabilities:**

- PoP (raw): 0.13567
- Assignment Prob: 0.226367
- P(25% Max Profit): 7e-06
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -700.00 | -3000.00 | -3700.00 | -0.0761 | -0.1787 |
| 92.00 | Lower Strike | 0.00 | -2300.00 | -2300.00 | 0.0000 | -0.1111 |
| 100.00 | Current Market Price | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.0725 |
| 108.00 | Upper Strike | 0.00 | -700.00 | -700.00 | 0.0000 | -0.0338 |
| 111.50 | Breakeven 1 | 350.00 | -350.00 | 0.00 | 0.0380 | 0.0000 |
| 115.00 | Upside (15%) | 700.00 | 0.00 | 700.00 | 0.0761 | 0.0338 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9200.00 | -20700.00 | -1.6059 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -700.00 | -3700.00 | -0.1787 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | -2300.00 | -0.1111 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.0725 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | -700.00 | -0.0338 |
| breakeven_1 | Breakeven 1 | 111.50 | 11.50% | 350.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 700.00 | 700.00 | 0.0338 |
| infinity | Stock to Infinity | — | — | 97200.00 | 193700.00 | 15.0272 |

---

### Short Combo (ID=52) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [92.0, 92.307692, 93.311037, 94.314381, 95.317726, 96.32107, 97.324415, 98.327759, 99.331104, 100.334448, 101.337793, 102.341137, 103.344482, 104.347826, 105.351171, 106.354515, 107.35786, 108.0]
- Options Max PnL: 9200.0
- Options Min PnL: -19200.0
- Combined Max PnL: 9200.0
- Combined Min PnL: -19200.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $9,200.00 | $9,200.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.48x | 0.48x |
| Capital Basis | $1,390.00 | $1,390.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 22.6% | 22.6% |
| Margin Proxy | 1390.0 | — |

**Probabilities:**

- PoP (raw): 0.226367
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.000215
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 700.00 | 0.00 | 700.00 | 0.5036 | 0.5036 |
| 92.00 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 92.31 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 93.31 | Breakeven 3 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 94.31 | Breakeven 4 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 95.32 | Breakeven 5 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 96.32 | Breakeven 6 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 97.32 | Breakeven 7 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 98.33 | Breakeven 8 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 99.33 | Breakeven 9 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.33 | Breakeven 10 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 101.34 | Breakeven 11 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 102.34 | Breakeven 12 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 103.34 | Breakeven 13 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 104.35 | Breakeven 14 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 105.35 | Breakeven 15 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 106.35 | Breakeven 16 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 107.36 | Breakeven 17 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Breakeven 18 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -700.00 | 0.00 | -700.00 | -0.5036 | -0.5036 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9200.00 | 9200.00 | 6.6187 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 700.00 | 700.00 | 0.5036 |
| strike_1 | Breakeven 1 | 92.00 | -8.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 92.00 | -8.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_2 | Breakeven 2 | 92.31 | -7.69% | 0.00 | 0.00 | 0.0000 |
| breakeven_3 | Breakeven 3 | 93.31 | -6.69% | 0.00 | 0.00 | 0.0000 |
| breakeven_4 | Breakeven 4 | 94.31 | -5.69% | 0.00 | 0.00 | 0.0000 |
| breakeven_5 | Breakeven 5 | 95.32 | -4.68% | 0.00 | 0.00 | 0.0000 |
| breakeven_6 | Breakeven 6 | 96.32 | -3.68% | 0.00 | 0.00 | 0.0000 |
| breakeven_7 | Breakeven 7 | 97.32 | -2.68% | 0.00 | 0.00 | 0.0000 |
| breakeven_8 | Breakeven 8 | 98.33 | -1.67% | 0.00 | 0.00 | 0.0000 |
| breakeven_9 | Breakeven 9 | 99.33 | -0.67% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_10 | Breakeven 10 | 100.33 | 0.33% | 0.00 | 0.00 | 0.0000 |
| breakeven_11 | Breakeven 11 | 101.34 | 1.34% | 0.00 | 0.00 | 0.0000 |
| breakeven_12 | Breakeven 12 | 102.34 | 2.34% | 0.00 | 0.00 | 0.0000 |
| breakeven_13 | Breakeven 13 | 103.34 | 3.34% | 0.00 | 0.00 | 0.0000 |
| breakeven_14 | Breakeven 14 | 104.35 | 4.35% | 0.00 | 0.00 | 0.0000 |
| breakeven_15 | Breakeven 15 | 105.35 | 5.35% | 0.00 | 0.00 | 0.0000 |
| breakeven_16 | Breakeven 16 | 106.35 | 6.35% | 0.00 | 0.00 | 0.0000 |
| breakeven_17 | Breakeven 17 | 107.36 | 7.36% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Breakeven 18 | 108.00 | 8.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_18 | Breakeven 18 | 108.00 | 8.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -700.00 | -700.00 | -0.5036 |
| infinity | Stock to Infinity | — | — | Unlimited | -97200.00 | -69.9281 |

---

### Short Combo (ID=52) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: COL_EQ
- Margin Classification: COL_EQ

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [100.0]
- Options Max PnL: 9200.0
- Options Min PnL: -19200.0
- Combined Max PnL: 800.0
- Combined Min PnL: -800.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $9,200.00 | $800.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.48x | 1.00x |
| Capital Basis | $5,190.00 | $15,190.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 47.9% | 47.9% |
| Margin Proxy | 5190.0 | — |

**Probabilities:**

- PoP (raw): 0.47931
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.000215
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 700.00 | -1500.00 | -800.00 | 0.1349 | -0.0527 |
| 92.00 | Lower Strike | 0.00 | -800.00 | -800.00 | 0.0000 | -0.0527 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | 0.00 | 800.00 | 800.00 | 0.0000 | 0.0527 |
| 115.00 | Upside (15%) | -700.00 | 1500.00 | 800.00 | -0.1349 | 0.0527 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9200.00 | -800.00 | -0.0527 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 700.00 | -800.00 | -0.0527 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | -800.00 | -0.0527 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 800.00 | 0.0527 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -700.00 | 800.00 | 0.0527 |
| infinity | Stock to Infinity | — | — | Unlimited | 800.00 | 0.0527 |

---

### Short Combo (ID=52) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: COL_EQ
- Margin Classification: COL_EQ

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: []
- Options Max PnL: 9200.0
- Options Min PnL: -19200.0
- Combined Max PnL: 5800.0
- Combined Min PnL: 4200.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $9,200.00 | $5,800.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.48x | 1.38x |
| Capital Basis | $5,190.00 | $10,190.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 5190.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.000215
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | 4200.00 | 0.00 | 4200.00 | 0.8092 | 0.4122 |
| 85.00 | Downside (15%) | 700.00 | 3500.00 | 4200.00 | 0.1349 | 0.4122 |
| 92.00 | Lower Strike | 0.00 | 4200.00 | 4200.00 | 0.0000 | 0.4122 |
| 100.00 | Current Market Price | 0.00 | 5000.00 | 5000.00 | 0.0000 | 0.4907 |
| 108.00 | Upper Strike | 0.00 | 5800.00 | 5800.00 | 0.0000 | 0.5692 |
| 115.00 | Upside (15%) | -700.00 | 6500.00 | 5800.00 | -0.1349 | 0.5692 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9200.00 | 4200.00 | 0.4122 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 700.00 | 4200.00 | 0.4122 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | 4200.00 | 0.4122 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 0.4907 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 5800.00 | 0.5692 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -700.00 | 5800.00 | 0.5692 |
| infinity | Stock to Infinity | — | — | Unlimited | 5800.00 | 0.5692 |

---

### Short Combo (ID=52) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: COL_EQ
- Margin Classification: COL_EQ

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: []
- Options Max PnL: 9200.0
- Options Min PnL: -19200.0
- Combined Max PnL: -700.0
- Combined Min PnL: -2300.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $9,200.00 | -$700.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.48x | 0.30x |
| Capital Basis | $5,190.00 | $16,690.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 5190.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.213914
- P(25% Max Profit): 0.000215
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 700.00 | -3000.00 | -2300.00 | 0.1349 | -0.1378 |
| 92.00 | Lower Strike | 0.00 | -2300.00 | -2300.00 | 0.0000 | -0.1378 |
| 100.00 | Current Market Price | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.0899 |
| 108.00 | Upper Strike | 0.00 | -700.00 | -700.00 | 0.0000 | -0.0419 |
| 115.00 | Upside (15%) | -700.00 | 0.00 | -700.00 | -0.1349 | -0.0419 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9200.00 | -2300.00 | -0.1378 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 700.00 | -2300.00 | -0.1378 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | -2300.00 | -0.1378 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.0899 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | -700.00 | -0.0419 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -700.00 | -700.00 | -0.0419 |
| infinity | Stock to Infinity | — | — | Unlimited | -700.00 | -0.0419 |

---

### L. Call Syn. Straddle (ID=53) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 100.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [95.0, 105.0]
- Options Max PnL: 39500.0
- Options Min PnL: -500.0
- Combined Max PnL: 19500.0
- Combined Min PnL: -500.0

**Net Premium:**

- Per Share: 5.0
- Total: 500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$500.00 | Unlimited |
| Risk Reward | 79.00x | 39.00x |
| Capital Basis | $500.00 | $10,500.00 |
| Cost Credit | Debit $500.00 | Debit $500.00 |
| Pop | 63.0% | 63.0% |
| Margin Proxy | 500.0 | — |

**Probabilities:**

- PoP (raw): 0.630219
- Assignment Prob: 0.0
- P(25% Max Profit): 2.3e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -500.00 | 1500.00 | 1000.00 | -1.0000 | 0.0952 |
| 95.00 | Breakeven 1 | -500.00 | 500.00 | 0.00 | -1.0000 | 0.0000 |
| 100.00 | Current Market Price | -500.00 | 0.00 | -500.00 | -1.0000 | -0.0476 |
| 105.00 | Breakeven 2 | 500.00 | -500.00 | 0.00 | 1.0000 | 0.0000 |
| 115.00 | Upside (15%) | 2500.00 | -1500.00 | 1000.00 | 5.0000 | 0.0952 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -500.00 | 9500.00 | 0.9048 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -500.00 | 1000.00 | 0.0952 |
| breakeven_1 | Breakeven 1 | 95.00 | -5.00% | -500.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -500.00 | -500.00 | -0.0476 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -500.00 | -500.00 | -0.0476 |
| breakeven_2 | Breakeven 2 | 105.00 | 5.00% | 500.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 2500.00 | 1000.00 | 0.0952 |
| infinity | Stock to Infinity | — | — | 179500.00 | 89500.00 | 8.5238 |

---

### L. Call Syn. Straddle (ID=53) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 100.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [95.0, 105.0]
- Options Max PnL: 39500.0
- Options Min PnL: -500.0
- Combined Max PnL: 19500.0
- Combined Min PnL: -500.0

**Net Premium:**

- Per Share: 5.0
- Total: 500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$500.00 | Unlimited |
| Risk Reward | 79.00x | 39.00x |
| Capital Basis | $500.00 | $10,500.00 |
| Cost Credit | Debit $500.00 | Debit $500.00 |
| Pop | 63.0% | 63.0% |
| Margin Proxy | 500.0 | — |

**Probabilities:**

- PoP (raw): 0.630219
- Assignment Prob: 0.0
- P(25% Max Profit): 2.3e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -500.00 | 1500.00 | 1000.00 | -1.0000 | 0.0952 |
| 95.00 | Breakeven 1 | -500.00 | 500.00 | 0.00 | -1.0000 | 0.0000 |
| 100.00 | Current Market Price | -500.00 | 0.00 | -500.00 | -1.0000 | -0.0476 |
| 105.00 | Breakeven 2 | 500.00 | -500.00 | 0.00 | 1.0000 | 0.0000 |
| 115.00 | Upside (15%) | 2500.00 | -1500.00 | 1000.00 | 5.0000 | 0.0952 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -500.00 | 9500.00 | 0.9048 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -500.00 | 1000.00 | 0.0952 |
| breakeven_1 | Breakeven 1 | 95.00 | -5.00% | -500.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -500.00 | -500.00 | -0.0476 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -500.00 | -500.00 | -0.0476 |
| breakeven_2 | Breakeven 2 | 105.00 | 5.00% | 500.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 2500.00 | 1000.00 | 0.0952 |
| infinity | Stock to Infinity | — | — | 179500.00 | 89500.00 | 8.5238 |

---

### L. Call Syn. Straddle (ID=53) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 50.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [45.0, 155.0]
- Options Max PnL: 39500.0
- Options Min PnL: -500.0
- Combined Max PnL: 14500.0
- Combined Min PnL: -5500.0

**Net Premium:**

- Per Share: 5.0
- Total: 500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$500.00 | Unlimited |
| Risk Reward | 79.00x | 2.64x |
| Capital Basis | $500.00 | $5,500.00 |
| Cost Credit | Debit $500.00 | Debit $500.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 500.0 | — |

**Probabilities:**

- PoP (raw): 1e-05
- Assignment Prob: 0.0
- P(25% Max Profit): 2.3e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 45.00 | Breakeven 1 | -500.00 | 500.00 | 0.00 | -1.0000 | 0.0000 |
| 50.00 | Scenario @ 50.00 | -500.00 | 0.00 | -500.00 | -1.0000 | -0.0909 |
| 85.00 | Downside (15%) | -500.00 | -3500.00 | -4000.00 | -1.0000 | -0.7273 |
| 100.00 | Current Market Price | -500.00 | -5000.00 | -5500.00 | -1.0000 | -1.0000 |
| 115.00 | Upside (15%) | 2500.00 | -6500.00 | -4000.00 | 5.0000 | -0.7273 |
| 155.00 | Breakeven 2 | 10500.00 | -10500.00 | 0.00 | 21.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -500.00 | 4500.00 | 0.8182 |
| breakeven_1 | Breakeven 1 | 45.00 | -55.00% | -500.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -500.00 | -4000.00 | -0.7273 |
| spot | Current Market Price | 100.00 | 0.00% | -500.00 | -5500.00 | -1.0000 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -500.00 | -5500.00 | -1.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 2500.00 | -4000.00 | -0.7273 |
| breakeven_2 | Breakeven 2 | 155.00 | 55.00% | 10500.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 179500.00 | 84500.00 | 15.3636 |

---

### L. Call Syn. Straddle (ID=53) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 114.99999999999999
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: []
- Options Max PnL: 39500.0
- Options Min PnL: -500.0
- Combined Max PnL: 21000.0
- Combined Min PnL: 1000.0

**Net Premium:**

- Per Share: 5.0
- Total: 500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$500.00 | Unlimited |
| Risk Reward | 79.00x | 21.00x |
| Capital Basis | $500.00 | $12,000.00 |
| Cost Credit | Debit $500.00 | Debit $500.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 500.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.0
- P(25% Max Profit): 2.3e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -500.00 | 3000.00 | 2500.00 | -1.0000 | 0.2083 |
| 100.00 | Current Market Price | -500.00 | 1500.00 | 1000.00 | -1.0000 | 0.0833 |
| 115.00 | Upside (15%) | 2500.00 | 0.00 | 2500.00 | 5.0000 | 0.2083 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -500.00 | 11000.00 | 0.9167 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -500.00 | 2500.00 | 0.2083 |
| spot | Current Market Price | 100.00 | 0.00% | -500.00 | 1000.00 | 0.0833 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -500.00 | 1000.00 | 0.0833 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 2500.00 | 2500.00 | 0.2083 |
| infinity | Stock to Infinity | — | — | 179500.00 | 91000.00 | 7.5833 |

---

### L. Put Syn. Straddle (ID=54) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: PPRT
- Margin Classification: PPRT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [95.0, 105.0]
- Options Max PnL: 19500.0
- Options Min PnL: -500.0
- Combined Max PnL: 19500.0
- Combined Min PnL: -500.0

**Net Premium:**

- Per Share: 5.0
- Total: 500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $19,500.00 | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 39.00x | 39.00x |
| Capital Basis | $5,500.00 | $15,500.00 |
| Cost Credit | Debit $500.00 | Debit $500.00 |
| Pop | 63.0% | 63.0% |
| Margin Proxy | 5500.0 | — |

**Probabilities:**

- PoP (raw): 0.630219
- Assignment Prob: 0.0
- P(25% Max Profit): 0.001529
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 2500.00 | -1500.00 | 1000.00 | 5.0000 | 0.0952 |
| 95.00 | Breakeven 1 | 500.00 | -500.00 | 0.00 | 1.0000 | 0.0000 |
| 100.00 | Current Market Price | -500.00 | 0.00 | -500.00 | -1.0000 | -0.0476 |
| 105.00 | Breakeven 2 | -500.00 | 500.00 | 0.00 | -1.0000 | 0.0000 |
| 115.00 | Upside (15%) | -500.00 | 1500.00 | 1000.00 | -1.0000 | 0.0952 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 19500.00 | 9500.00 | 0.6129 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 2500.00 | 1000.00 | 0.0952 |
| breakeven_1 | Breakeven 1 | 95.00 | -5.00% | 500.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -500.00 | -500.00 | -0.0476 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -500.00 | -500.00 | -0.0476 |
| breakeven_2 | Breakeven 2 | 105.00 | 5.00% | -500.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -500.00 | 1000.00 | 0.0952 |
| infinity | Stock to Infinity | — | — | Unlimited | 89500.00 | 5.7742 |

---

### L. Put Syn. Straddle (ID=54) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: PPRT
- Margin Classification: PPRT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [95.0, 105.0]
- Options Max PnL: 19500.0
- Options Min PnL: -500.0
- Combined Max PnL: 19500.0
- Combined Min PnL: -500.0

**Net Premium:**

- Per Share: 5.0
- Total: 500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $19,500.00 | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 39.00x | 39.00x |
| Capital Basis | $5,500.00 | $15,500.00 |
| Cost Credit | Debit $500.00 | Debit $500.00 |
| Pop | 63.0% | 63.0% |
| Margin Proxy | 5500.0 | — |

**Probabilities:**

- PoP (raw): 0.630219
- Assignment Prob: 0.0
- P(25% Max Profit): 0.001529
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 2500.00 | -1500.00 | 1000.00 | 5.0000 | 0.0952 |
| 95.00 | Breakeven 1 | 500.00 | -500.00 | 0.00 | 1.0000 | 0.0000 |
| 100.00 | Current Market Price | -500.00 | 0.00 | -500.00 | -1.0000 | -0.0476 |
| 105.00 | Breakeven 2 | -500.00 | 500.00 | 0.00 | -1.0000 | 0.0000 |
| 115.00 | Upside (15%) | -500.00 | 1500.00 | 1000.00 | -1.0000 | 0.0952 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 19500.00 | 9500.00 | 0.6129 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 2500.00 | 1000.00 | 0.0952 |
| breakeven_1 | Breakeven 1 | 95.00 | -5.00% | 500.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -500.00 | -500.00 | -0.0476 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -500.00 | -500.00 | -0.0476 |
| breakeven_2 | Breakeven 2 | 105.00 | 5.00% | -500.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -500.00 | 1000.00 | 0.0952 |
| infinity | Stock to Infinity | — | — | Unlimited | 89500.00 | 5.7742 |

---

### L. Put Syn. Straddle (ID=54) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: PPRT
- Margin Classification: PPRT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: []
- Options Max PnL: 19500.0
- Options Min PnL: -500.0
- Combined Max PnL: 24500.0
- Combined Min PnL: 4500.0

**Net Premium:**

- Per Share: 5.0
- Total: 500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $19,500.00 | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 39.00x | 5.44x |
| Capital Basis | $5,500.00 | $10,500.00 |
| Cost Credit | Debit $500.00 | Debit $500.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 5500.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.0
- P(25% Max Profit): 0.001529
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | 9500.00 | 0.00 | 9500.00 | 19.0000 | 1.7273 |
| 85.00 | Downside (15%) | 2500.00 | 3500.00 | 6000.00 | 5.0000 | 1.0909 |
| 100.00 | Current Market Price | -500.00 | 5000.00 | 4500.00 | -1.0000 | 0.8182 |
| 115.00 | Upside (15%) | -500.00 | 6500.00 | 6000.00 | -1.0000 | 1.0909 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 19500.00 | 14500.00 | 1.3810 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 2500.00 | 6000.00 | 1.0909 |
| spot | Current Market Price | 100.00 | 0.00% | -500.00 | 4500.00 | 0.8182 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -500.00 | 4500.00 | 0.8182 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -500.00 | 6000.00 | 1.0909 |
| infinity | Stock to Infinity | — | — | Unlimited | 94500.00 | 9.0000 |

---

### L. Put Syn. Straddle (ID=54) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: PPRT
- Margin Classification: PPRT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [80.0, 120.0]
- Options Max PnL: 19500.0
- Options Min PnL: -500.0
- Combined Max PnL: 18000.0
- Combined Min PnL: -2000.0

**Net Premium:**

- Per Share: 5.0
- Total: 500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $19,500.00 | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 39.00x | 9.00x |
| Capital Basis | $5,500.00 | $17,000.00 |
| Cost Credit | Debit $500.00 | Debit $500.00 |
| Pop | 5.3% | 5.3% |
| Margin Proxy | 5500.0 | — |

**Probabilities:**

- PoP (raw): 0.053375
- Assignment Prob: 0.0
- P(25% Max Profit): 0.001529
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Breakeven 1 | 3500.00 | -3500.00 | 0.00 | 7.0000 | 0.0000 |
| 85.00 | Downside (15%) | 2500.00 | -3000.00 | -500.00 | 5.0000 | -0.0417 |
| 100.00 | Current Market Price | -500.00 | -1500.00 | -2000.00 | -1.0000 | -0.1667 |
| 115.00 | Upside (15%) | -500.00 | 0.00 | -500.00 | -1.0000 | -0.0417 |
| 120.00 | Breakeven 2 | -500.00 | 500.00 | 0.00 | -1.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 19500.00 | 8000.00 | 0.4706 |
| breakeven_1 | Breakeven 1 | 80.00 | -20.00% | 3500.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 2500.00 | -500.00 | -0.0417 |
| spot | Current Market Price | 100.00 | 0.00% | -500.00 | -2000.00 | -0.1667 |
| strike_1 | Current Market Price | 100.00 | 0.00% | -500.00 | -2000.00 | -0.1667 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -500.00 | -500.00 | -0.0417 |
| breakeven_2 | Breakeven 2 | 120.00 | 20.00% | -500.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | 88000.00 | 5.1765 |

---

### S. Call Syn. Straddle (ID=55) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [95.0, 105.0]
- Options Max PnL: 500.0
- Options Min PnL: -39500.0
- Combined Max PnL: 500.0
- Combined Min PnL: -19500.0

**Net Premium:**

- Per Share: -5.0
- Total: -500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $500.00 | $500.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.01x | 0.03x |
| Capital Basis | $5,000.00 | $15,000.00 |
| Cost Credit | Credit $500.00 | Credit $500.00 |
| Pop | 37.0% | 37.0% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 0.369781
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.59126
- P(50% Max Profit): 0.568099
- P(100% Max Profit): 0.521668
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 500.00 | -1500.00 | -1000.00 | 0.1000 | -0.0667 |
| 95.00 | Breakeven 1 | 500.00 | -500.00 | 0.00 | 0.1000 | 0.0000 |
| 100.00 | Current Market Price | 500.00 | 0.00 | 500.00 | 0.1000 | 0.0333 |
| 105.00 | Breakeven 2 | -500.00 | 500.00 | 0.00 | -0.1000 | 0.0000 |
| 115.00 | Upside (15%) | -2500.00 | 1500.00 | -1000.00 | -0.5000 | -0.0667 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 500.00 | -9500.00 | -0.6333 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 500.00 | -1000.00 | -0.0667 |
| breakeven_1 | Breakeven 1 | 95.00 | -5.00% | 500.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 500.00 | 500.00 | 0.0333 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 500.00 | 500.00 | 0.0333 |
| breakeven_2 | Breakeven 2 | 105.00 | 5.00% | -500.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -2500.00 | -1000.00 | -0.0667 |
| infinity | Stock to Infinity | — | — | Unlimited | -89500.00 | -5.9667 |

---

### S. Call Syn. Straddle (ID=55) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [95.0, 105.0]
- Options Max PnL: 500.0
- Options Min PnL: -39500.0
- Combined Max PnL: 500.0
- Combined Min PnL: -19500.0

**Net Premium:**

- Per Share: -5.0
- Total: -500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $500.00 | $500.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.01x | 0.03x |
| Capital Basis | $5,000.00 | $15,000.00 |
| Cost Credit | Credit $500.00 | Credit $500.00 |
| Pop | 37.0% | 37.0% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 0.369781
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.59126
- P(50% Max Profit): 0.568099
- P(100% Max Profit): 0.521668
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 500.00 | -1500.00 | -1000.00 | 0.1000 | -0.0667 |
| 95.00 | Breakeven 1 | 500.00 | -500.00 | 0.00 | 0.1000 | 0.0000 |
| 100.00 | Current Market Price | 500.00 | 0.00 | 500.00 | 0.1000 | 0.0333 |
| 105.00 | Breakeven 2 | -500.00 | 500.00 | 0.00 | -0.1000 | 0.0000 |
| 115.00 | Upside (15%) | -2500.00 | 1500.00 | -1000.00 | -0.5000 | -0.0667 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 500.00 | -9500.00 | -0.6333 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 500.00 | -1000.00 | -0.0667 |
| breakeven_1 | Breakeven 1 | 95.00 | -5.00% | 500.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 500.00 | 500.00 | 0.0333 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 500.00 | 500.00 | 0.0333 |
| breakeven_2 | Breakeven 2 | 105.00 | 5.00% | -500.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -2500.00 | -1000.00 | -0.0667 |
| infinity | Stock to Infinity | — | — | Unlimited | -89500.00 | -5.9667 |

---

### S. Call Syn. Straddle (ID=55) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [45.0, 155.0]
- Options Max PnL: 500.0
- Options Min PnL: -39500.0
- Combined Max PnL: 5500.0
- Combined Min PnL: -14500.0

**Net Premium:**

- Per Share: -5.0
- Total: -500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $500.00 | $5,500.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.01x | 0.38x |
| Capital Basis | $5,000.00 | $10,000.00 |
| Cost Credit | Credit $500.00 | Credit $500.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 0.99999
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.59126
- P(50% Max Profit): 0.568099
- P(100% Max Profit): 0.521668
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 45.00 | Breakeven 1 | 500.00 | -500.00 | 0.00 | 0.1000 | 0.0000 |
| 50.00 | Scenario @ 50.00 | 500.00 | 0.00 | 500.00 | 0.1000 | 0.0500 |
| 85.00 | Downside (15%) | 500.00 | 3500.00 | 4000.00 | 0.1000 | 0.4000 |
| 100.00 | Current Market Price | 500.00 | 5000.00 | 5500.00 | 0.1000 | 0.5500 |
| 115.00 | Upside (15%) | -2500.00 | 6500.00 | 4000.00 | -0.5000 | 0.4000 |
| 155.00 | Breakeven 2 | -10500.00 | 10500.00 | 0.00 | -2.1000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 500.00 | -4500.00 | -0.4500 |
| breakeven_1 | Breakeven 1 | 45.00 | -55.00% | 500.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 500.00 | 4000.00 | 0.4000 |
| spot | Current Market Price | 100.00 | 0.00% | 500.00 | 5500.00 | 0.5500 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 500.00 | 5500.00 | 0.5500 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -2500.00 | 4000.00 | 0.4000 |
| breakeven_2 | Breakeven 2 | 155.00 | 55.00% | -10500.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | -84500.00 | -8.4500 |

---

### S. Call Syn. Straddle (ID=55) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: []
- Options Max PnL: 500.0
- Options Min PnL: -39500.0
- Combined Max PnL: -1000.0
- Combined Min PnL: -21000.0

**Net Premium:**

- Per Share: -5.0
- Total: -500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $500.00 | -$1,000.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.01x | 0.05x |
| Capital Basis | $5,000.00 | $16,500.00 |
| Cost Credit | Credit $500.00 | Credit $500.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.59126
- P(50% Max Profit): 0.568099
- P(100% Max Profit): 0.521668
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 500.00 | -3000.00 | -2500.00 | 0.1000 | -0.1515 |
| 100.00 | Current Market Price | 500.00 | -1500.00 | -1000.00 | 0.1000 | -0.0606 |
| 115.00 | Upside (15%) | -2500.00 | 0.00 | -2500.00 | -0.5000 | -0.1515 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 500.00 | -11000.00 | -0.6667 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 500.00 | -2500.00 | -0.1515 |
| spot | Current Market Price | 100.00 | 0.00% | 500.00 | -1000.00 | -0.0606 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 500.00 | -1000.00 | -0.0606 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -2500.00 | -2500.00 | -0.1515 |
| infinity | Stock to Infinity | — | — | Unlimited | -91000.00 | -5.5152 |

---

### S. Put Syn. Straddle (ID=56) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [95.0, 105.0]
- Options Max PnL: 500.0
- Options Min PnL: -19500.0
- Combined Max PnL: 500.0
- Combined Min PnL: -19500.0

**Net Premium:**

- Per Share: -5.0
- Total: -500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $500.00 | $500.00 |
| Max Loss | -$19,500.00 | Unlimited |
| Risk Reward | 0.03x | 0.03x |
| Capital Basis | $4,500.00 | $14,500.00 |
| Cost Credit | Credit $500.00 | Credit $500.00 |
| Pop | 37.0% | 37.0% |
| Margin Proxy | 4500.0 | — |

**Probabilities:**

- PoP (raw): 0.369781
- Assignment Prob: 0.520709
- P(25% Max Profit): 0.551838
- P(50% Max Profit): 0.527575
- P(100% Max Profit): 0.480251
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -2500.00 | 1500.00 | -1000.00 | -0.1282 | -0.0339 |
| 95.00 | Breakeven 1 | -500.00 | 500.00 | 0.00 | -0.0256 | 0.0000 |
| 100.00 | Current Market Price | 500.00 | 0.00 | 500.00 | 0.0256 | 0.0169 |
| 105.00 | Breakeven 2 | 500.00 | -500.00 | 0.00 | 0.0256 | 0.0000 |
| 115.00 | Upside (15%) | 500.00 | -1500.00 | -1000.00 | 0.0256 | -0.0339 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -19500.00 | -9500.00 | -0.6552 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -2500.00 | -1000.00 | -0.0339 |
| breakeven_1 | Breakeven 1 | 95.00 | -5.00% | -500.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 500.00 | 500.00 | 0.0169 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 500.00 | 500.00 | 0.0169 |
| breakeven_2 | Breakeven 2 | 105.00 | 5.00% | 500.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 500.00 | -1000.00 | -0.0339 |
| infinity | Stock to Infinity | — | — | 500.00 | -89500.00 | -6.1724 |

---

### S. Put Syn. Straddle (ID=56) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [95.0, 105.0]
- Options Max PnL: 500.0
- Options Min PnL: -19500.0
- Combined Max PnL: 500.0
- Combined Min PnL: -19500.0

**Net Premium:**

- Per Share: -5.0
- Total: -500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $500.00 | $500.00 |
| Max Loss | -$19,500.00 | Unlimited |
| Risk Reward | 0.03x | 0.03x |
| Capital Basis | $4,500.00 | $14,500.00 |
| Cost Credit | Credit $500.00 | Credit $500.00 |
| Pop | 37.0% | 37.0% |
| Margin Proxy | 4500.0 | — |

**Probabilities:**

- PoP (raw): 0.369781
- Assignment Prob: 0.520709
- P(25% Max Profit): 0.551838
- P(50% Max Profit): 0.527575
- P(100% Max Profit): 0.480251
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -2500.00 | 1500.00 | -1000.00 | -0.1282 | -0.0339 |
| 95.00 | Breakeven 1 | -500.00 | 500.00 | 0.00 | -0.0256 | 0.0000 |
| 100.00 | Current Market Price | 500.00 | 0.00 | 500.00 | 0.0256 | 0.0169 |
| 105.00 | Breakeven 2 | 500.00 | -500.00 | 0.00 | 0.0256 | 0.0000 |
| 115.00 | Upside (15%) | 500.00 | -1500.00 | -1000.00 | 0.0256 | -0.0339 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -19500.00 | -9500.00 | -0.6552 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -2500.00 | -1000.00 | -0.0339 |
| breakeven_1 | Breakeven 1 | 95.00 | -5.00% | -500.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 500.00 | 500.00 | 0.0169 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 500.00 | 500.00 | 0.0169 |
| breakeven_2 | Breakeven 2 | 105.00 | 5.00% | 500.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 500.00 | -1000.00 | -0.0339 |
| infinity | Stock to Infinity | — | — | 500.00 | -89500.00 | -6.1724 |

---

### S. Put Syn. Straddle (ID=56) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: []
- Options Max PnL: 500.0
- Options Min PnL: -19500.0
- Combined Max PnL: -4500.0
- Combined Min PnL: -24500.0

**Net Premium:**

- Per Share: -5.0
- Total: -500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $500.00 | -$4,500.00 |
| Max Loss | -$19,500.00 | Unlimited |
| Risk Reward | 0.03x | 0.18x |
| Capital Basis | $4,500.00 | $9,500.00 |
| Cost Credit | Credit $500.00 | Credit $500.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 4500.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.520709
- P(25% Max Profit): 0.551838
- P(50% Max Profit): 0.527575
- P(100% Max Profit): 0.480251
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -9500.00 | 0.00 | -9500.00 | -0.4872 | -0.3878 |
| 85.00 | Downside (15%) | -2500.00 | -3500.00 | -6000.00 | -0.1282 | -0.2449 |
| 100.00 | Current Market Price | 500.00 | -5000.00 | -4500.00 | 0.0256 | -0.1837 |
| 115.00 | Upside (15%) | 500.00 | -6500.00 | -6000.00 | 0.0256 | -0.2449 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -19500.00 | -14500.00 | -1.5263 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -2500.00 | -6000.00 | -0.2449 |
| spot | Current Market Price | 100.00 | 0.00% | 500.00 | -4500.00 | -0.1837 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 500.00 | -4500.00 | -0.1837 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 500.00 | -6000.00 | -0.2449 |
| infinity | Stock to Infinity | — | — | 500.00 | -94500.00 | -9.9474 |

---

### S. Put Syn. Straddle (ID=56) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 2 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [80.0, 120.0]
- Options Max PnL: 500.0
- Options Min PnL: -19500.0
- Combined Max PnL: 2000.0
- Combined Min PnL: -18000.0

**Net Premium:**

- Per Share: -5.0
- Total: -500.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $500.00 | $2,000.00 |
| Max Loss | -$19,500.00 | Unlimited |
| Risk Reward | 0.03x | 0.11x |
| Capital Basis | $4,500.00 | $16,000.00 |
| Cost Credit | Credit $500.00 | Credit $500.00 |
| Pop | 94.7% | 94.7% |
| Margin Proxy | 4500.0 | — |

**Probabilities:**

- PoP (raw): 0.946625
- Assignment Prob: 0.520709
- P(25% Max Profit): 0.551838
- P(50% Max Profit): 0.527575
- P(100% Max Profit): 0.480251
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 80.00 | Breakeven 1 | -3500.00 | 3500.00 | -0.00 | -0.1795 | -0.0000 |
| 85.00 | Downside (15%) | -2500.00 | 3000.00 | 500.00 | -0.1282 | 0.0161 |
| 100.00 | Current Market Price | 500.00 | 1500.00 | 2000.00 | 0.0256 | 0.0645 |
| 115.00 | Upside (15%) | 500.00 | 0.00 | 500.00 | 0.0256 | 0.0161 |
| 120.00 | Breakeven 2 | 500.00 | -500.00 | -0.00 | 0.0256 | -0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -19500.00 | -8000.00 | -0.5000 |
| breakeven_1 | Breakeven 1 | 80.00 | -20.00% | -3500.00 | -0.00 | -0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -2500.00 | 500.00 | 0.0161 |
| spot | Current Market Price | 100.00 | 0.00% | 500.00 | 2000.00 | 0.0645 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 500.00 | 2000.00 | 0.0645 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 500.00 | 500.00 | 0.0161 |
| breakeven_2 | Breakeven 2 | 120.00 | 20.00% | 500.00 | -0.00 | -0.0000 |
| infinity | Stock to Infinity | — | — | 500.00 | -88000.00 | -5.5000 |

---

### L. Call Syn. Strangle (ID=57) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 100.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [88.2, 111.8]
- Options Max PnL: 38820.0
- Options Min PnL: -1180.0
- Combined Max PnL: 18820.0
- Combined Min PnL: -380.0

**Net Premium:**

- Per Share: 11.8
- Total: 1180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$1,180.00 | Unlimited |
| Risk Reward | 32.90x | 49.53x |
| Capital Basis | $1,180.00 | $11,180.00 |
| Cost Credit | Debit $1,180.00 | Debit $1,180.00 |
| Pop | 25.4% | 25.4% |
| Margin Proxy | 1180.0 | — |

**Probabilities:**

- PoP (raw): 0.253752
- Assignment Prob: 0.0
- P(25% Max Profit): 1.1e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1180.00 | 1500.00 | 320.00 | -1.0000 | 0.0286 |
| 88.20 | Breakeven 1 | -1180.00 | 1180.00 | -0.00 | -1.0000 | -0.0000 |
| 92.00 | Lower Strike | -1180.00 | 800.00 | -380.00 | -1.0000 | -0.0340 |
| 100.00 | Current Market Price | -380.00 | 0.00 | -380.00 | -0.3220 | -0.0340 |
| 108.00 | Upper Strike | 420.00 | -800.00 | -380.00 | 0.3559 | -0.0340 |
| 111.80 | Breakeven 2 | 1180.00 | -1180.00 | -0.00 | 1.0000 | -0.0000 |
| 115.00 | Upside (15%) | 1820.00 | -1500.00 | 320.00 | 1.5424 | 0.0286 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1180.00 | 8820.00 | 0.7889 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1180.00 | 320.00 | 0.0286 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | -1180.00 | -0.00 | -0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -1180.00 | -380.00 | -0.0340 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -380.00 | -0.0340 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 420.00 | -380.00 | -0.0340 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | 1180.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1820.00 | 320.00 | 0.0286 |
| infinity | Stock to Infinity | — | — | 194820.00 | 96820.00 | 8.6601 |

---

### L. Call Syn. Strangle (ID=57) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 100.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [88.2, 111.8]
- Options Max PnL: 38820.0
- Options Min PnL: -1180.0
- Combined Max PnL: 18820.0
- Combined Min PnL: -380.0

**Net Premium:**

- Per Share: 11.8
- Total: 1180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$1,180.00 | Unlimited |
| Risk Reward | 32.90x | 49.53x |
| Capital Basis | $1,180.00 | $11,180.00 |
| Cost Credit | Debit $1,180.00 | Debit $1,180.00 |
| Pop | 25.4% | 25.4% |
| Margin Proxy | 1180.0 | — |

**Probabilities:**

- PoP (raw): 0.253752
- Assignment Prob: 0.0
- P(25% Max Profit): 1.1e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1180.00 | 1500.00 | 320.00 | -1.0000 | 0.0286 |
| 88.20 | Breakeven 1 | -1180.00 | 1180.00 | -0.00 | -1.0000 | -0.0000 |
| 92.00 | Lower Strike | -1180.00 | 800.00 | -380.00 | -1.0000 | -0.0340 |
| 100.00 | Current Market Price | -380.00 | 0.00 | -380.00 | -0.3220 | -0.0340 |
| 108.00 | Upper Strike | 420.00 | -800.00 | -380.00 | 0.3559 | -0.0340 |
| 111.80 | Breakeven 2 | 1180.00 | -1180.00 | -0.00 | 1.0000 | -0.0000 |
| 115.00 | Upside (15%) | 1820.00 | -1500.00 | 320.00 | 1.5424 | 0.0286 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1180.00 | 8820.00 | 0.7889 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1180.00 | 320.00 | 0.0286 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | -1180.00 | -0.00 | -0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -1180.00 | -380.00 | -0.0340 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -380.00 | -0.0340 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 420.00 | -380.00 | -0.0340 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | 1180.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1820.00 | 320.00 | 0.0286 |
| infinity | Stock to Infinity | — | — | 194820.00 | 96820.00 | 8.6601 |

---

### L. Call Syn. Strangle (ID=57) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 50.0
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [38.2, 161.8]
- Options Max PnL: 38820.0
- Options Min PnL: -1180.0
- Combined Max PnL: 13820.0
- Combined Min PnL: -5380.0

**Net Premium:**

- Per Share: 11.8
- Total: 1180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$1,180.00 | Unlimited |
| Risk Reward | 32.90x | 2.57x |
| Capital Basis | $1,180.00 | $6,180.00 |
| Cost Credit | Debit $1,180.00 | Debit $1,180.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 1180.0 | — |

**Probabilities:**

- PoP (raw): 1e-06
- Assignment Prob: 0.0
- P(25% Max Profit): 1.1e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 38.20 | Breakeven 1 | -1180.00 | 1180.00 | -0.00 | -1.0000 | -0.0000 |
| 50.00 | Scenario @ 50.00 | -1180.00 | 0.00 | -1180.00 | -1.0000 | -0.1909 |
| 85.00 | Downside (15%) | -1180.00 | -3500.00 | -4680.00 | -1.0000 | -0.7573 |
| 92.00 | Lower Strike | -1180.00 | -4200.00 | -5380.00 | -1.0000 | -0.8706 |
| 100.00 | Current Market Price | -380.00 | -5000.00 | -5380.00 | -0.3220 | -0.8706 |
| 108.00 | Upper Strike | 420.00 | -5800.00 | -5380.00 | 0.3559 | -0.8706 |
| 115.00 | Upside (15%) | 1820.00 | -6500.00 | -4680.00 | 1.5424 | -0.7573 |
| 161.80 | Breakeven 2 | 11180.00 | -11180.00 | 0.00 | 9.4746 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1180.00 | 3820.00 | 0.6181 |
| breakeven_1 | Breakeven 1 | 38.20 | -61.80% | -1180.00 | -0.00 | -0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1180.00 | -4680.00 | -0.7573 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -1180.00 | -5380.00 | -0.8706 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -5380.00 | -0.8706 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 420.00 | -5380.00 | -0.8706 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1820.00 | -4680.00 | -0.7573 |
| breakeven_2 | Breakeven 2 | 161.80 | 61.80% | 11180.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 194820.00 | 91820.00 | 14.8576 |

---

### L. Call Syn. Strangle (ID=57) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 114.99999999999999
- Strategy Code: LNG
- Margin Classification: LNG_LE_9M

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Long 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Long 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: []
- Options Max PnL: 38820.0
- Options Min PnL: -1180.0
- Combined Max PnL: 20320.0
- Combined Min PnL: 1120.0

**Net Premium:**

- Per Share: 11.8
- Total: 1180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | Unlimited | Unlimited |
| Max Loss | -$1,180.00 | Unlimited |
| Risk Reward | 32.90x | 18.14x |
| Capital Basis | $1,180.00 | $12,680.00 |
| Cost Credit | Debit $1,180.00 | Debit $1,180.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 1180.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.0
- P(25% Max Profit): 1.1e-05
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1180.00 | 3000.00 | 1820.00 | -1.0000 | 0.1435 |
| 92.00 | Lower Strike | -1180.00 | 2300.00 | 1120.00 | -1.0000 | 0.0883 |
| 100.00 | Current Market Price | -380.00 | 1500.00 | 1120.00 | -0.3220 | 0.0883 |
| 108.00 | Upper Strike | 420.00 | 700.00 | 1120.00 | 0.3559 | 0.0883 |
| 115.00 | Upside (15%) | 1820.00 | 0.00 | 1820.00 | 1.5424 | 0.1435 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1180.00 | 10320.00 | 0.8139 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1180.00 | 1820.00 | 0.1435 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -1180.00 | 1120.00 | 0.0883 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | 1120.00 | 0.0883 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 420.00 | 1120.00 | 0.0883 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1820.00 | 1820.00 | 0.1435 |
| infinity | Stock to Infinity | — | — | 194820.00 | 98320.00 | 7.7539 |

---

### L. Put Syn. Strangle (ID=58) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: PPRT
- Margin Classification: PPRT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 2 | PUT | Long 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [88.2, 111.8]
- Options Max PnL: 18820.0
- Options Min PnL: -1180.0
- Combined Max PnL: 18820.0
- Combined Min PnL: -380.0

**Net Premium:**

- Per Share: 11.8
- Total: 1180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $18,820.00 | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 15.95x | 49.53x |
| Capital Basis | $6,180.00 | $16,180.00 |
| Cost Credit | Debit $1,180.00 | Debit $1,180.00 |
| Pop | 25.4% | 25.4% |
| Margin Proxy | 6180.0 | — |

**Probabilities:**

- PoP (raw): 0.253752
- Assignment Prob: 0.0
- P(25% Max Profit): 0.000478
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1820.00 | -1500.00 | 320.00 | 1.5424 | 0.0286 |
| 88.20 | Breakeven 1 | 1180.00 | -1180.00 | -0.00 | 1.0000 | -0.0000 |
| 92.00 | Lower Strike | 420.00 | -800.00 | -380.00 | 0.3559 | -0.0340 |
| 100.00 | Current Market Price | -380.00 | 0.00 | -380.00 | -0.3220 | -0.0340 |
| 108.00 | Upper Strike | -1180.00 | 800.00 | -380.00 | -1.0000 | -0.0340 |
| 111.80 | Breakeven 2 | -1180.00 | 1180.00 | -0.00 | -1.0000 | -0.0000 |
| 115.00 | Upside (15%) | -1180.00 | 1500.00 | 320.00 | -1.0000 | 0.0286 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 18820.00 | 8820.00 | 0.5451 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1820.00 | 320.00 | 0.0286 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | 1180.00 | -0.00 | -0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 420.00 | -380.00 | -0.0340 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -380.00 | -0.0340 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -1180.00 | -380.00 | -0.0340 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | -1180.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1180.00 | 320.00 | 0.0286 |
| infinity | Stock to Infinity | — | — | Unlimited | 96820.00 | 5.9839 |

---

### L. Put Syn. Strangle (ID=58) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: PPRT
- Margin Classification: PPRT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 2 | PUT | Long 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [88.2, 111.8]
- Options Max PnL: 18820.0
- Options Min PnL: -1180.0
- Combined Max PnL: 18820.0
- Combined Min PnL: -380.0

**Net Premium:**

- Per Share: 11.8
- Total: 1180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $18,820.00 | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 15.95x | 49.53x |
| Capital Basis | $6,180.00 | $16,180.00 |
| Cost Credit | Debit $1,180.00 | Debit $1,180.00 |
| Pop | 25.4% | 25.4% |
| Margin Proxy | 6180.0 | — |

**Probabilities:**

- PoP (raw): 0.253752
- Assignment Prob: 0.0
- P(25% Max Profit): 0.000478
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1820.00 | -1500.00 | 320.00 | 1.5424 | 0.0286 |
| 88.20 | Breakeven 1 | 1180.00 | -1180.00 | -0.00 | 1.0000 | -0.0000 |
| 92.00 | Lower Strike | 420.00 | -800.00 | -380.00 | 0.3559 | -0.0340 |
| 100.00 | Current Market Price | -380.00 | 0.00 | -380.00 | -0.3220 | -0.0340 |
| 108.00 | Upper Strike | -1180.00 | 800.00 | -380.00 | -1.0000 | -0.0340 |
| 111.80 | Breakeven 2 | -1180.00 | 1180.00 | -0.00 | -1.0000 | -0.0000 |
| 115.00 | Upside (15%) | -1180.00 | 1500.00 | 320.00 | -1.0000 | 0.0286 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 18820.00 | 8820.00 | 0.5451 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1820.00 | 320.00 | 0.0286 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | 1180.00 | -0.00 | -0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 420.00 | -380.00 | -0.0340 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -380.00 | -0.0340 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -1180.00 | -380.00 | -0.0340 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | -1180.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1180.00 | 320.00 | 0.0286 |
| infinity | Stock to Infinity | — | — | Unlimited | 96820.00 | 5.9839 |

---

### L. Put Syn. Strangle (ID=58) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: PPRT
- Margin Classification: PPRT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 2 | PUT | Long 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: []
- Options Max PnL: 18820.0
- Options Min PnL: -1180.0
- Combined Max PnL: 23820.0
- Combined Min PnL: 4620.0

**Net Premium:**

- Per Share: 11.8
- Total: 1180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $18,820.00 | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 15.95x | 5.16x |
| Capital Basis | $6,180.00 | $11,180.00 |
| Cost Credit | Debit $1,180.00 | Debit $1,180.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 6180.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.0
- P(25% Max Profit): 0.000478
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | 8820.00 | 0.00 | 8820.00 | 7.4746 | 1.4272 |
| 85.00 | Downside (15%) | 1820.00 | 3500.00 | 5320.00 | 1.5424 | 0.8608 |
| 92.00 | Lower Strike | 420.00 | 4200.00 | 4620.00 | 0.3559 | 0.7476 |
| 100.00 | Current Market Price | -380.00 | 5000.00 | 4620.00 | -0.3220 | 0.7476 |
| 108.00 | Upper Strike | -1180.00 | 5800.00 | 4620.00 | -1.0000 | 0.7476 |
| 115.00 | Upside (15%) | -1180.00 | 6500.00 | 5320.00 | -1.0000 | 0.8608 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 18820.00 | 13820.00 | 1.2361 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1820.00 | 5320.00 | 0.8608 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 420.00 | 4620.00 | 0.7476 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | 4620.00 | 0.7476 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -1180.00 | 4620.00 | 0.7476 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1180.00 | 5320.00 | 0.8608 |
| infinity | Stock to Infinity | — | — | Unlimited | 101820.00 | 9.1073 |

---

### L. Put Syn. Strangle (ID=58) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: PPRT
- Margin Classification: PPRT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 92.00 | 1.90 | 100 |
| 2 | PUT | Long 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [73.2, 126.8]
- Options Max PnL: 18820.0
- Options Min PnL: -1180.0
- Combined Max PnL: 17320.0
- Combined Min PnL: -1880.0

**Net Premium:**

- Per Share: 11.8
- Total: 1180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $18,820.00 | Unlimited |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 15.95x | 9.21x |
| Capital Basis | $6,180.00 | $17,680.00 |
| Cost Credit | Debit $1,180.00 | Debit $1,180.00 |
| Pop | 1.1% | 1.1% |
| Margin Proxy | 6180.0 | — |

**Probabilities:**

- PoP (raw): 0.011273
- Assignment Prob: 0.0
- P(25% Max Profit): 0.000478
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 73.20 | Breakeven 1 | 4180.00 | -4180.00 | 0.00 | 3.5424 | 0.0000 |
| 85.00 | Downside (15%) | 1820.00 | -3000.00 | -1180.00 | 1.5424 | -0.0931 |
| 92.00 | Lower Strike | 420.00 | -2300.00 | -1880.00 | 0.3559 | -0.1483 |
| 100.00 | Current Market Price | -380.00 | -1500.00 | -1880.00 | -0.3220 | -0.1483 |
| 108.00 | Upper Strike | -1180.00 | -700.00 | -1880.00 | -1.0000 | -0.1483 |
| 115.00 | Upside (15%) | -1180.00 | 0.00 | -1180.00 | -1.0000 | -0.0931 |
| 126.80 | Breakeven 2 | -1180.00 | 1180.00 | 0.00 | -1.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 18820.00 | 7320.00 | 0.4140 |
| breakeven_1 | Breakeven 1 | 73.20 | -26.80% | 4180.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1820.00 | -1180.00 | -0.0931 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 420.00 | -1880.00 | -0.1483 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -1880.00 | -0.1483 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -1180.00 | -1880.00 | -0.1483 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1180.00 | -1180.00 | -0.0931 |
| breakeven_2 | Breakeven 2 | 126.80 | 26.80% | -1180.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | 95320.00 | 5.3914 |

---

### S. Call Syn. Strangle (ID=59) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [88.2, 111.8]
- Options Max PnL: 1180.0
- Options Min PnL: -38820.0
- Combined Max PnL: 380.0
- Combined Min PnL: -18820.0

**Net Premium:**

- Per Share: -11.8
- Total: -1180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,180.00 | $380.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.03x | 0.02x |
| Capital Basis | $5,000.00 | $15,000.00 |
| Cost Credit | Credit $1,180.00 | Credit $1,180.00 |
| Pop | 74.6% | 74.6% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 0.746248
- Assignment Prob: 0.773633
- P(25% Max Profit): 0.553071
- P(50% Max Profit): 0.439443
- P(100% Max Profit): 0.230098
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1180.00 | -1500.00 | -320.00 | 0.2360 | -0.0213 |
| 88.20 | Breakeven 1 | 1180.00 | -1180.00 | 0.00 | 0.2360 | 0.0000 |
| 92.00 | Lower Strike | 1180.00 | -800.00 | 380.00 | 0.2360 | 0.0253 |
| 100.00 | Current Market Price | 380.00 | 0.00 | 380.00 | 0.0760 | 0.0253 |
| 108.00 | Upper Strike | -420.00 | 800.00 | 380.00 | -0.0840 | 0.0253 |
| 111.80 | Breakeven 2 | -1180.00 | 1180.00 | 0.00 | -0.2360 | 0.0000 |
| 115.00 | Upside (15%) | -1820.00 | 1500.00 | -320.00 | -0.3640 | -0.0213 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1180.00 | -8820.00 | -0.5880 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1180.00 | -320.00 | -0.0213 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | 1180.00 | 0.00 | 0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 1180.00 | 380.00 | 0.0253 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 380.00 | 0.0253 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -420.00 | 380.00 | 0.0253 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | -1180.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1820.00 | -320.00 | -0.0213 |
| infinity | Stock to Infinity | — | — | Unlimited | -96820.00 | -6.4547 |

---

### S. Call Syn. Strangle (ID=59) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [88.2, 111.8]
- Options Max PnL: 1180.0
- Options Min PnL: -38820.0
- Combined Max PnL: 380.0
- Combined Min PnL: -18820.0

**Net Premium:**

- Per Share: -11.8
- Total: -1180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,180.00 | $380.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.03x | 0.02x |
| Capital Basis | $5,000.00 | $15,000.00 |
| Cost Credit | Credit $1,180.00 | Credit $1,180.00 |
| Pop | 74.6% | 74.6% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 0.746248
- Assignment Prob: 0.773633
- P(25% Max Profit): 0.553071
- P(50% Max Profit): 0.439443
- P(100% Max Profit): 0.230098
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1180.00 | -1500.00 | -320.00 | 0.2360 | -0.0213 |
| 88.20 | Breakeven 1 | 1180.00 | -1180.00 | 0.00 | 0.2360 | 0.0000 |
| 92.00 | Lower Strike | 1180.00 | -800.00 | 380.00 | 0.2360 | 0.0253 |
| 100.00 | Current Market Price | 380.00 | 0.00 | 380.00 | 0.0760 | 0.0253 |
| 108.00 | Upper Strike | -420.00 | 800.00 | 380.00 | -0.0840 | 0.0253 |
| 111.80 | Breakeven 2 | -1180.00 | 1180.00 | 0.00 | -0.2360 | 0.0000 |
| 115.00 | Upside (15%) | -1820.00 | 1500.00 | -320.00 | -0.3640 | -0.0213 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1180.00 | -8820.00 | -0.5880 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1180.00 | -320.00 | -0.0213 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | 1180.00 | 0.00 | 0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 1180.00 | 380.00 | 0.0253 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 380.00 | 0.0253 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -420.00 | 380.00 | 0.0253 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | -1180.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1820.00 | -320.00 | -0.0213 |
| infinity | Stock to Infinity | — | — | Unlimited | -96820.00 | -6.4547 |

---

### S. Call Syn. Strangle (ID=59) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [38.2, 161.8]
- Options Max PnL: 1180.0
- Options Min PnL: -38820.0
- Combined Max PnL: 5380.0
- Combined Min PnL: -13820.0

**Net Premium:**

- Per Share: -11.8
- Total: -1180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,180.00 | $5,380.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.03x | 0.39x |
| Capital Basis | $5,000.00 | $10,000.00 |
| Cost Credit | Credit $1,180.00 | Credit $1,180.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 0.999999
- Assignment Prob: 0.773633
- P(25% Max Profit): 0.553071
- P(50% Max Profit): 0.439443
- P(100% Max Profit): 0.230098
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 38.20 | Breakeven 1 | 1180.00 | -1180.00 | 0.00 | 0.2360 | 0.0000 |
| 50.00 | Scenario @ 50.00 | 1180.00 | 0.00 | 1180.00 | 0.2360 | 0.1180 |
| 85.00 | Downside (15%) | 1180.00 | 3500.00 | 4680.00 | 0.2360 | 0.4680 |
| 92.00 | Lower Strike | 1180.00 | 4200.00 | 5380.00 | 0.2360 | 0.5380 |
| 100.00 | Current Market Price | 380.00 | 5000.00 | 5380.00 | 0.0760 | 0.5380 |
| 108.00 | Upper Strike | -420.00 | 5800.00 | 5380.00 | -0.0840 | 0.5380 |
| 115.00 | Upside (15%) | -1820.00 | 6500.00 | 4680.00 | -0.3640 | 0.4680 |
| 161.80 | Breakeven 2 | -11180.00 | 11180.00 | 0.00 | -2.2360 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1180.00 | -3820.00 | -0.3820 |
| breakeven_1 | Breakeven 1 | 38.20 | -61.80% | 1180.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1180.00 | 4680.00 | 0.4680 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 1180.00 | 5380.00 | 0.5380 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 5380.00 | 0.5380 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -420.00 | 5380.00 | 0.5380 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1820.00 | 4680.00 | 0.4680 |
| breakeven_2 | Breakeven 2 | 161.80 | 61.80% | -11180.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | -91820.00 | -9.1820 |

---

### S. Call Syn. Strangle (ID=59) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |
| 2 | CALL | Short 1 | 108.00 | 1.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: []
- Options Max PnL: 1180.0
- Options Min PnL: -38820.0
- Combined Max PnL: -1120.0
- Combined Min PnL: -20320.0

**Net Premium:**

- Per Share: -11.8
- Total: -1180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,180.00 | -$1,120.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.03x | 0.06x |
| Capital Basis | $5,000.00 | $16,500.00 |
| Cost Credit | Credit $1,180.00 | Credit $1,180.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.773633
- P(25% Max Profit): 0.553071
- P(50% Max Profit): 0.439443
- P(100% Max Profit): 0.230098
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1180.00 | -3000.00 | -1820.00 | 0.2360 | -0.1103 |
| 92.00 | Lower Strike | 1180.00 | -2300.00 | -1120.00 | 0.2360 | -0.0679 |
| 100.00 | Current Market Price | 380.00 | -1500.00 | -1120.00 | 0.0760 | -0.0679 |
| 108.00 | Upper Strike | -420.00 | -700.00 | -1120.00 | -0.0840 | -0.0679 |
| 115.00 | Upside (15%) | -1820.00 | 0.00 | -1820.00 | -0.3640 | -0.1103 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1180.00 | -10320.00 | -0.6255 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1180.00 | -1820.00 | -0.1103 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 1180.00 | -1120.00 | -0.0679 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | -1120.00 | -0.0679 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -420.00 | -1120.00 | -0.0679 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1820.00 | -1820.00 | -0.1103 |
| infinity | Stock to Infinity | — | — | Unlimited | -98320.00 | -5.9588 |

---

### S. Put Syn. Strangle (ID=60) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 2 | PUT | Short 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [88.2, 111.8]
- Options Max PnL: 1180.0
- Options Min PnL: -18820.0
- Combined Max PnL: 380.0
- Combined Min PnL: -18820.0

**Net Premium:**

- Per Share: -11.8
- Total: -1180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,180.00 | $380.00 |
| Max Loss | -$18,820.00 | Unlimited |
| Risk Reward | 0.06x | 0.02x |
| Capital Basis | $4,380.00 | $14,380.00 |
| Cost Credit | Credit $1,180.00 | Credit $1,180.00 |
| Pop | 74.6% | 74.6% |
| Margin Proxy | 4380.0 | — |

**Probabilities:**

- PoP (raw): 0.746248
- Assignment Prob: 0.786086
- P(25% Max Profit): 0.512069
- P(50% Max Profit): 0.40051
- P(100% Max Profit): 0.216993
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1820.00 | 1500.00 | -320.00 | -0.0967 | -0.0111 |
| 88.20 | Breakeven 1 | -1180.00 | 1180.00 | 0.00 | -0.0627 | 0.0000 |
| 92.00 | Lower Strike | -420.00 | 800.00 | 380.00 | -0.0223 | 0.0132 |
| 100.00 | Current Market Price | 380.00 | 0.00 | 380.00 | 0.0202 | 0.0132 |
| 108.00 | Upper Strike | 1180.00 | -800.00 | 380.00 | 0.0627 | 0.0132 |
| 111.80 | Breakeven 2 | 1180.00 | -1180.00 | 0.00 | 0.0627 | 0.0000 |
| 115.00 | Upside (15%) | 1180.00 | -1500.00 | -320.00 | 0.0627 | -0.0111 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -18820.00 | -8820.00 | -0.6134 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1820.00 | -320.00 | -0.0111 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | -1180.00 | 0.00 | 0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -420.00 | 380.00 | 0.0132 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 380.00 | 0.0132 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 1180.00 | 380.00 | 0.0132 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | 1180.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1180.00 | -320.00 | -0.0111 |
| infinity | Stock to Infinity | — | — | 1180.00 | -96820.00 | -6.7330 |

---

### S. Put Syn. Strangle (ID=60) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 2 | PUT | Short 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [88.2, 111.8]
- Options Max PnL: 1180.0
- Options Min PnL: -18820.0
- Combined Max PnL: 380.0
- Combined Min PnL: -18820.0

**Net Premium:**

- Per Share: -11.8
- Total: -1180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,180.00 | $380.00 |
| Max Loss | -$18,820.00 | Unlimited |
| Risk Reward | 0.06x | 0.02x |
| Capital Basis | $4,380.00 | $14,380.00 |
| Cost Credit | Credit $1,180.00 | Credit $1,180.00 |
| Pop | 74.6% | 74.6% |
| Margin Proxy | 4380.0 | — |

**Probabilities:**

- PoP (raw): 0.746248
- Assignment Prob: 0.786086
- P(25% Max Profit): 0.512069
- P(50% Max Profit): 0.40051
- P(100% Max Profit): 0.216993
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1820.00 | 1500.00 | -320.00 | -0.0967 | -0.0111 |
| 88.20 | Breakeven 1 | -1180.00 | 1180.00 | 0.00 | -0.0627 | 0.0000 |
| 92.00 | Lower Strike | -420.00 | 800.00 | 380.00 | -0.0223 | 0.0132 |
| 100.00 | Current Market Price | 380.00 | 0.00 | 380.00 | 0.0202 | 0.0132 |
| 108.00 | Upper Strike | 1180.00 | -800.00 | 380.00 | 0.0627 | 0.0132 |
| 111.80 | Breakeven 2 | 1180.00 | -1180.00 | 0.00 | 0.0627 | 0.0000 |
| 115.00 | Upside (15%) | 1180.00 | -1500.00 | -320.00 | 0.0627 | -0.0111 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -18820.00 | -8820.00 | -0.6134 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1820.00 | -320.00 | -0.0111 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | -1180.00 | 0.00 | 0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -420.00 | 380.00 | 0.0132 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 380.00 | 0.0132 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 1180.00 | 380.00 | 0.0132 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | 1180.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1180.00 | -320.00 | -0.0111 |
| infinity | Stock to Infinity | — | — | 1180.00 | -96820.00 | -6.7330 |

---

### S. Put Syn. Strangle (ID=60) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 2 | PUT | Short 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: []
- Options Max PnL: 1180.0
- Options Min PnL: -18820.0
- Combined Max PnL: -4620.0
- Combined Min PnL: -23820.0

**Net Premium:**

- Per Share: -11.8
- Total: -1180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,180.00 | -$4,620.00 |
| Max Loss | -$18,820.00 | Unlimited |
| Risk Reward | 0.06x | 0.19x |
| Capital Basis | $4,380.00 | $9,380.00 |
| Cost Credit | Credit $1,180.00 | Credit $1,180.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 4380.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.786086
- P(25% Max Profit): 0.512069
- P(50% Max Profit): 0.40051
- P(100% Max Profit): 0.216993
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -8820.00 | 0.00 | -8820.00 | -0.4687 | -0.3703 |
| 85.00 | Downside (15%) | -1820.00 | -3500.00 | -5320.00 | -0.0967 | -0.2233 |
| 92.00 | Lower Strike | -420.00 | -4200.00 | -4620.00 | -0.0223 | -0.1940 |
| 100.00 | Current Market Price | 380.00 | -5000.00 | -4620.00 | 0.0202 | -0.1940 |
| 108.00 | Upper Strike | 1180.00 | -5800.00 | -4620.00 | 0.0627 | -0.1940 |
| 115.00 | Upside (15%) | 1180.00 | -6500.00 | -5320.00 | 0.0627 | -0.2233 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -18820.00 | -13820.00 | -1.4733 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1820.00 | -5320.00 | -0.2233 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -420.00 | -4620.00 | -0.1940 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | -4620.00 | -0.1940 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 1180.00 | -4620.00 | -0.1940 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1180.00 | -5320.00 | -0.2233 |
| infinity | Stock to Infinity | — | — | 1180.00 | -101820.00 | -10.8550 |

---

### S. Put Syn. Strangle (ID=60) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: -100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 92.00 | 1.90 | 100 |
| 2 | PUT | Short 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 302 points
- Strikes: [92.0, 108.0]
- Breakevens: [73.2, 126.8]
- Options Max PnL: 1180.0
- Options Min PnL: -18820.0
- Combined Max PnL: 1880.0
- Combined Min PnL: -17320.0

**Net Premium:**

- Per Share: -11.8
- Total: -1180.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $1,180.00 | $1,880.00 |
| Max Loss | -$18,820.00 | Unlimited |
| Risk Reward | 0.06x | 0.11x |
| Capital Basis | $4,380.00 | $15,880.00 |
| Cost Credit | Credit $1,180.00 | Credit $1,180.00 |
| Pop | 98.9% | 98.9% |
| Margin Proxy | 4380.0 | — |

**Probabilities:**

- PoP (raw): 0.988727
- Assignment Prob: 0.786086
- P(25% Max Profit): 0.512069
- P(50% Max Profit): 0.40051
- P(100% Max Profit): 0.216993
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 73.20 | Breakeven 1 | -4180.00 | 4180.00 | -0.00 | -0.2221 | -0.0000 |
| 85.00 | Downside (15%) | -1820.00 | 3000.00 | 1180.00 | -0.0967 | 0.0389 |
| 92.00 | Lower Strike | -420.00 | 2300.00 | 1880.00 | -0.0223 | 0.0620 |
| 100.00 | Current Market Price | 380.00 | 1500.00 | 1880.00 | 0.0202 | 0.0620 |
| 108.00 | Upper Strike | 1180.00 | 700.00 | 1880.00 | 0.0627 | 0.0620 |
| 115.00 | Upside (15%) | 1180.00 | 0.00 | 1180.00 | 0.0627 | 0.0389 |
| 126.80 | Breakeven 2 | 1180.00 | -1180.00 | -0.00 | 0.0627 | -0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -18820.00 | -7320.00 | -0.4610 |
| breakeven_1 | Breakeven 1 | 73.20 | -26.80% | -4180.00 | -0.00 | -0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1820.00 | 1180.00 | 0.0389 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -420.00 | 1880.00 | 0.0620 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 1880.00 | 0.0620 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 1180.00 | 1880.00 | 0.0620 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1180.00 | 1180.00 | 0.0389 |
| breakeven_2 | Breakeven 2 | 126.80 | 26.80% | 1180.00 | -0.00 | -0.0000 |
| infinity | Stock to Infinity | — | — | 1180.00 | -95320.00 | -6.0025 |

---

### Syn. Covered Call (ID=61) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: CSPT
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [108.0]
- Breakevens: [98.1]
- Options Max PnL: 990.0
- Options Min PnL: -9810.0
- Combined Max PnL: 990.0
- Combined Min PnL: -9810.0

**Net Premium:**

- Per Share: -9.9
- Total: -990.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $990.00 | $990.00 |
| Max Loss | -$9,810.00 | -$9,810.00 |
| Risk Reward | 0.10x | 0.10x |
| Capital Basis | $10,800.00 | $10,800.00 |
| Cost Credit | Credit $990.00 | Credit $990.00 |
| Pop | 55.3% | 55.3% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 0.552808
- Assignment Prob: 0.786086
- P(25% Max Profit): 0.457341
- P(50% Max Profit): 0.366478
- P(100% Max Profit): 0.216496
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1310.00 | 0.00 | -1310.00 | -0.1335 | -0.1335 |
| 98.10 | Breakeven 1 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0194 | 0.0194 |
| 108.00 | Strike | 990.00 | 0.00 | 990.00 | 0.1009 | 0.1009 |
| 115.00 | Upside (15%) | 990.00 | 0.00 | 990.00 | 0.1009 | 0.1009 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9810.00 | -9810.00 | -0.9083 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1310.00 | -1310.00 | -0.1335 |
| breakeven_1 | Breakeven 1 | 98.10 | -1.90% | -0.00 | -0.00 | -0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0194 |
| strike_1 | Strike | 108.00 | 8.00% | 990.00 | 990.00 | 0.1009 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 990.00 | 990.00 | 0.1009 |
| infinity | Stock to Infinity | — | — | 990.00 | 990.00 | 0.0917 |

---

### Syn. Covered Call (ID=61) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [108.0]
- Breakevens: [99.05]
- Options Max PnL: 990.0
- Options Min PnL: -9810.0
- Combined Max PnL: 20990.0
- Combined Min PnL: -19810.0

**Net Premium:**

- Per Share: -9.9
- Total: -990.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $990.00 | Unlimited |
| Max Loss | -$9,810.00 | -$19,810.00 |
| Risk Reward | 0.10x | 1.06x |
| Capital Basis | $2,990.00 | $12,990.00 |
| Cost Credit | Credit $990.00 | Credit $990.00 |
| Pop | 51.6% | 51.6% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 0.515942
- Assignment Prob: 0.786086
- P(25% Max Profit): 0.457341
- P(50% Max Profit): 0.366478
- P(100% Max Profit): 0.216496
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1310.00 | -1500.00 | -2810.00 | -0.1335 | -0.1418 |
| 99.05 | Breakeven 1 | 95.00 | -95.00 | -0.00 | 0.0097 | -0.0000 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0194 | 0.0096 |
| 108.00 | Strike | 990.00 | 800.00 | 1790.00 | 0.1009 | 0.0904 |
| 115.00 | Upside (15%) | 990.00 | 1500.00 | 2490.00 | 0.1009 | 0.1257 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9810.00 | -19810.00 | -1.5250 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1310.00 | -2810.00 | -0.1418 |
| breakeven_1 | Breakeven 1 | 99.05 | -0.95% | 95.00 | -0.00 | -0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0096 |
| strike_1 | Strike | 108.00 | 8.00% | 990.00 | 1790.00 | 0.0904 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 990.00 | 2490.00 | 0.1257 |
| infinity | Stock to Infinity | — | — | 990.00 | 98990.00 | 7.6205 |

---

### Syn. Covered Call (ID=61) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [108.0]
- Breakevens: [74.05]
- Options Max PnL: 990.0
- Options Min PnL: -9810.0
- Combined Max PnL: 25990.0
- Combined Min PnL: -14810.0

**Net Premium:**

- Per Share: -9.9
- Total: -990.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $990.00 | Unlimited |
| Max Loss | -$9,810.00 | -$14,810.00 |
| Risk Reward | 0.10x | 1.75x |
| Capital Basis | $2,990.00 | $7,990.00 |
| Cost Credit | Credit $990.00 | Credit $990.00 |
| Pop | 99.8% | 99.8% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 0.997748
- Assignment Prob: 0.786086
- P(25% Max Profit): 0.457341
- P(50% Max Profit): 0.366478
- P(100% Max Profit): 0.216496
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | -4810.00 | 0.00 | -4810.00 | -0.4903 | -0.3248 |
| 74.05 | Breakeven 1 | -2405.00 | 2405.00 | -0.00 | -0.2452 | -0.0000 |
| 85.00 | Downside (15%) | -1310.00 | 3500.00 | 2190.00 | -0.1335 | 0.1479 |
| 100.00 | Current Market Price | 190.00 | 5000.00 | 5190.00 | 0.0194 | 0.3504 |
| 108.00 | Strike | 990.00 | 5800.00 | 6790.00 | 0.1009 | 0.4585 |
| 115.00 | Upside (15%) | 990.00 | 6500.00 | 7490.00 | 0.1009 | 0.5057 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9810.00 | -14810.00 | -1.8536 |
| breakeven_1 | Breakeven 1 | 74.05 | -25.95% | -2405.00 | -0.00 | -0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1310.00 | 2190.00 | 0.1479 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 5190.00 | 0.3504 |
| strike_1 | Strike | 108.00 | 8.00% | 990.00 | 6790.00 | 0.4585 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 990.00 | 7490.00 | 0.5057 |
| infinity | Stock to Infinity | — | — | 990.00 | 103990.00 | 13.0150 |

---

### Syn. Covered Call (ID=61) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Short 1 | 108.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [108.0]
- Breakevens: [106.55]
- Options Max PnL: 990.0
- Options Min PnL: -9810.0
- Combined Max PnL: 19490.0
- Combined Min PnL: -21310.0

**Net Premium:**

- Per Share: -9.9
- Total: -990.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $990.00 | Unlimited |
| Max Loss | -$9,810.00 | -$21,310.00 |
| Risk Reward | 0.10x | 0.91x |
| Capital Basis | $2,990.00 | $14,490.00 |
| Cost Credit | Credit $990.00 | Credit $990.00 |
| Pop | 25.4% | 25.4% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 0.253738
- Assignment Prob: 0.786086
- P(25% Max Profit): 0.457341
- P(50% Max Profit): 0.366478
- P(100% Max Profit): 0.216496
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | -1310.00 | -3000.00 | -4310.00 | -0.1335 | -0.2023 |
| 100.00 | Current Market Price | 190.00 | -1500.00 | -1310.00 | 0.0194 | -0.0615 |
| 106.55 | Breakeven 1 | 845.00 | -845.00 | 0.00 | 0.0861 | 0.0000 |
| 108.00 | Strike | 990.00 | -700.00 | 290.00 | 0.1009 | 0.0136 |
| 115.00 | Upside (15%) | 990.00 | 0.00 | 990.00 | 0.1009 | 0.0465 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9810.00 | -21310.00 | -1.4707 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1310.00 | -4310.00 | -0.2023 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | -1310.00 | -0.0615 |
| breakeven_1 | Breakeven 1 | 106.55 | 6.55% | 845.00 | 0.00 | 0.0000 |
| strike_1 | Strike | 108.00 | 8.00% | 990.00 | 290.00 | 0.0136 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 990.00 | 990.00 | 0.0465 |
| infinity | Stock to Infinity | — | — | 990.00 | 97490.00 | 6.7281 |

---

### Syn. Covered Put (ID=62) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: NAK
- Margin Classification: SH_OPT

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [92.0]
- Breakevens: [101.9]
- Options Max PnL: 990.0
- Options Min PnL: -19810.0
- Combined Max PnL: 990.0
- Combined Min PnL: -19810.0

**Net Premium:**

- Per Share: -9.9
- Total: -990.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $990.00 | $990.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.05x | 0.05x |
| Capital Basis | $2,990.00 | $2,990.00 |
| Cost Credit | Credit $990.00 | Credit $990.00 |
| Pop | 59.2% | 59.2% |
| Margin Proxy | 2990.0 | — |

**Probabilities:**

- PoP (raw): 0.592177
- Assignment Prob: 0.773633
- P(25% Max Profit): 0.498569
- P(50% Max Profit): 0.402727
- P(100% Max Profit): 0.229495
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 990.00 | 0.00 | 990.00 | 0.3311 | 0.3311 |
| 92.00 | Strike | 990.00 | 0.00 | 990.00 | 0.3311 | 0.3311 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0635 | 0.0635 |
| 101.90 | Breakeven 1 | -0.00 | 0.00 | -0.00 | -0.0000 | -0.0000 |
| 115.00 | Upside (15%) | -1310.00 | 0.00 | -1310.00 | -0.4381 | -0.4381 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 990.00 | 990.00 | 0.3311 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 990.00 | 990.00 | 0.3311 |
| strike_1 | Strike | 92.00 | -8.00% | 990.00 | 990.00 | 0.3311 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0635 |
| breakeven_1 | Breakeven 1 | 101.90 | 1.90% | -0.00 | -0.00 | -0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1310.00 | -1310.00 | -0.4381 |
| infinity | Stock to Infinity | — | — | Unlimited | -89810.00 | -30.0368 |

---

### Syn. Covered Put (ID=62) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [92.0]
- Breakevens: [90.1]
- Options Max PnL: 990.0
- Options Min PnL: -19810.0
- Combined Max PnL: 190.0
- Combined Min PnL: -9010.0

**Net Premium:**

- Per Share: -9.9
- Total: -990.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $990.00 | $190.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.05x | 0.02x |
| Capital Basis | $5,000.00 | $15,000.00 |
| Cost Credit | Credit $990.00 | Credit $990.00 |
| Pop | 82.9% | 82.9% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 0.829398
- Assignment Prob: 0.773633
- P(25% Max Profit): 0.498569
- P(50% Max Profit): 0.402727
- P(100% Max Profit): 0.229495
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 990.00 | -1500.00 | -510.00 | 0.1980 | -0.0340 |
| 90.10 | Breakeven 1 | 990.00 | -990.00 | -0.00 | 0.1980 | -0.0000 |
| 92.00 | Strike | 990.00 | -800.00 | 190.00 | 0.1980 | 0.0127 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0380 | 0.0127 |
| 115.00 | Upside (15%) | -1310.00 | 1500.00 | 190.00 | -0.2620 | 0.0127 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 990.00 | -9010.00 | -0.6007 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 990.00 | -510.00 | -0.0340 |
| breakeven_1 | Breakeven 1 | 90.10 | -9.90% | 990.00 | -0.00 | -0.0000 |
| strike_1 | Strike | 92.00 | -8.00% | 990.00 | 190.00 | 0.0127 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0127 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1310.00 | 190.00 | 0.0127 |
| infinity | Stock to Infinity | — | — | Unlimited | 190.00 | 0.0127 |

---

### Syn. Covered Put (ID=62) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [92.0]
- Breakevens: [40.1]
- Options Max PnL: 990.0
- Options Min PnL: -19810.0
- Combined Max PnL: 5190.0
- Combined Min PnL: -4010.0

**Net Premium:**

- Per Share: -9.9
- Total: -990.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $990.00 | $5,190.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.05x | 1.29x |
| Capital Basis | $5,000.00 | $10,000.00 |
| Cost Credit | Credit $990.00 | Credit $990.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.773633
- P(25% Max Profit): 0.498569
- P(50% Max Profit): 0.402727
- P(100% Max Profit): 0.229495
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 40.10 | Breakeven 1 | 990.00 | -990.00 | 0.00 | 0.1980 | 0.0000 |
| 50.00 | Scenario @ 50.00 | 990.00 | 0.00 | 990.00 | 0.1980 | 0.0990 |
| 85.00 | Downside (15%) | 990.00 | 3500.00 | 4490.00 | 0.1980 | 0.4490 |
| 92.00 | Strike | 990.00 | 4200.00 | 5190.00 | 0.1980 | 0.5190 |
| 100.00 | Current Market Price | 190.00 | 5000.00 | 5190.00 | 0.0380 | 0.5190 |
| 115.00 | Upside (15%) | -1310.00 | 6500.00 | 5190.00 | -0.2620 | 0.5190 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 990.00 | -4010.00 | -0.4010 |
| breakeven_1 | Breakeven 1 | 40.10 | -59.90% | 990.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 990.00 | 4490.00 | 0.4490 |
| strike_1 | Strike | 92.00 | -8.00% | 990.00 | 5190.00 | 0.5190 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 5190.00 | 0.5190 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1310.00 | 5190.00 | 0.5190 |
| infinity | Stock to Infinity | — | — | Unlimited | 5190.00 | 0.5190 |

---

### Syn. Covered Put (ID=62) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: CCOV
- Margin Classification: CCOV

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | CALL | Short 1 | 92.00 | 9.90 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [92.0]
- Breakevens: []
- Options Max PnL: 990.0
- Options Min PnL: -19810.0
- Combined Max PnL: -1310.0
- Combined Min PnL: -10510.0

**Net Premium:**

- Per Share: -9.9
- Total: -990.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $990.00 | -$1,310.00 |
| Max Loss | Unlimited | Unlimited |
| Risk Reward | 0.05x | 0.12x |
| Capital Basis | $5,000.00 | $16,500.00 |
| Cost Credit | Credit $990.00 | Credit $990.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 5000.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.773633
- P(25% Max Profit): 0.498569
- P(50% Max Profit): 0.402727
- P(100% Max Profit): 0.229495
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 990.00 | -3000.00 | -2010.00 | 0.1980 | -0.1218 |
| 92.00 | Strike | 990.00 | -2300.00 | -1310.00 | 0.1980 | -0.0794 |
| 100.00 | Current Market Price | 190.00 | -1500.00 | -1310.00 | 0.0380 | -0.0794 |
| 115.00 | Upside (15%) | -1310.00 | 0.00 | -1310.00 | -0.2620 | -0.0794 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 990.00 | -10510.00 | -0.6370 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 990.00 | -2010.00 | -0.1218 |
| strike_1 | Strike | 92.00 | -8.00% | 990.00 | -1310.00 | -0.0794 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | -1310.00 | -0.0794 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1310.00 | -1310.00 | -0.0794 |
| infinity | Stock to Infinity | — | — | Unlimited | -1310.00 | -0.0794 |

---

### Conversion (ID=63) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: COL_EQ
- Margin Classification: COL_EQ

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [0.0, 1.003344, 2.006689, 3.010033, 4.013378, 5.016722, 6.020067, 7.023411, 8.026756, 9.0301, 10.033445, 11.036789, 12.040134, 13.043478, 14.046823, 15.050167, 17.056856, 18.060201, 19.063545, 20.06689, 21.070234, 22.073579, 23.076923, 24.080268, 25.083612, 26.086957, 27.090301, 28.093645, 29.09699, 30.100334, 31.103679, 32.107023, 33.110368, 34.113712, 35.117057, 36.120401, 37.123746, 38.12709, 39.130435, 40.133779, 41.137124, 42.140468, 43.143813, 44.147157, 45.150502, 46.153846, 47.157191, 48.160535, 49.16388, 50.167224, 51.170569, 52.173913, 53.177258, 54.180602, 55.183946, 56.187291, 58.19398, 59.197324, 60.200669, 61.204013, 62.207358, 63.210702, 64.214047, 65.217391, 66.220736, 67.22408, 68.227425, 69.230769, 70.234114, 71.237458, 72.240803, 73.244147, 74.247492, 75.250836, 76.254181, 77.257525, 78.26087, 79.264214, 80.267559, 81.270903, 82.274247, 83.277592, 84.280936, 85.284281, 86.287625, 87.29097, 88.294314, 89.297659, 90.301003, 91.304348, 92.307692, 93.311037, 94.314381, 95.317726, 96.32107, 97.324415, 98.327759, 99.331104, 100.0, 100.334448, 101.337793, 102.341137, 103.344482, 104.347826, 105.351171, 106.354515, 107.35786, 108.361204, 109.364548, 110.367893, 111.371237, 112.374582, 113.377926, 114.381271, 115.384615, 116.38796, 117.391304, 118.394649, 119.397993, 120.401338, 122.408027, 123.411371, 124.414716, 125.41806, 126.421405, 127.424749, 128.428094, 129.431438, 130.434783, 131.438127, 132.441472, 133.444816, 134.448161, 135.451505, 136.454849, 137.458194, 138.461538, 139.464883, 140.468227, 141.471572, 142.474916, 143.478261, 144.481605, 145.48495, 146.488294, 147.491639, 148.494983, 149.498328, 150.501672, 151.505017, 152.508361, 153.511706, 154.51505, 155.518395, 156.521739, 157.525084, 158.528428, 159.531773, 160.535117, 161.538462, 162.541806, 163.545151, 164.548495, 165.551839, 166.555184, 167.558528, 168.561873, 169.565217, 170.568562, 171.571906, 172.575251, 173.578595, 174.58194, 175.585284, 176.588629, 177.591973, 178.595318, 179.598662, 180.602007, 181.605351, 183.61204, 184.615385, 185.618729, 186.622074, 187.625418, 188.628763, 189.632107, 190.635452, 191.638796, 192.64214, 193.645485, 194.648829, 195.652174, 196.655518, 197.658863, 198.662207, 199.665552, 200.668896, 201.672241, 202.675585, 203.67893, 204.682274, 205.685619, 206.688963, 207.692308, 208.695652, 209.698997, 210.702341, 211.705686, 212.70903, 213.712375, 214.715719, 215.719064, 216.722408, 217.725753, 218.729097, 219.732441, 220.735786, 221.73913, 222.742475, 223.745819, 224.749164, 225.752508, 226.755853, 227.759197, 228.762542, 229.765886, 230.769231, 231.772575, 232.77592, 233.779264, 234.782609, 235.785953, 236.789298, 237.792642, 238.795987, 239.799331, 240.802676, 241.80602, 242.809365, 243.812709, 244.816054, 245.819398, 246.822742, 247.826087, 248.829431, 249.832776, 250.83612, 251.839465, 252.842809, 253.846154, 254.849498, 255.852843, 256.856187, 257.859532, 258.862876, 259.866221, 260.869565, 261.87291, 262.876254, 263.879599, 264.882943, 265.886288, 266.889632, 267.892977, 268.896321, 269.899666, 270.90301, 271.906355, 272.909699, 273.913043, 274.916388, 275.919732, 276.923077, 277.926421, 278.929766, 279.93311, 280.936455, 281.939799, 282.943144, 283.946488, 284.949833, 285.953177, 286.956522, 287.959866, 288.963211, 289.966555, 290.9699, 291.973244, 292.976589, 293.979933, 294.983278, 295.986622, 296.989967, 297.993311, 298.996656]
- Options Max PnL: 10000.0
- Options Min PnL: -20000.0
- Combined Max PnL: 0.0
- Combined Min PnL: -0.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $10,000.00 | $0.00 |
| Max Loss | Unlimited | -$0.00 |
| Risk Reward | 0.50x | 0.25x |
| Capital Basis | $5,250.00 | $15,250.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 5250.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.003285
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 0.00 | Breakeven 1 | 10000.00 | -10000.00 | 0.00 | 1.9048 | 0.0000 |
| 1.00 | Breakeven 2 | 9899.67 | -9899.67 | 0.00 | 1.8857 | 0.0000 |
| 2.01 | Breakeven 3 | 9799.33 | -9799.33 | 0.00 | 1.8665 | 0.0000 |
| 3.01 | Breakeven 4 | 9699.00 | -9699.00 | 0.00 | 1.8474 | 0.0000 |
| 4.01 | Breakeven 5 | 9598.66 | -9598.66 | 0.00 | 1.8283 | 0.0000 |
| 5.02 | Breakeven 6 | 9498.33 | -9498.33 | 0.00 | 1.8092 | 0.0000 |
| 6.02 | Breakeven 7 | 9397.99 | -9397.99 | 0.00 | 1.7901 | 0.0000 |
| 7.02 | Breakeven 8 | 9297.66 | -9297.66 | 0.00 | 1.7710 | 0.0000 |
| 8.03 | Breakeven 9 | 9197.32 | -9197.32 | 0.00 | 1.7519 | 0.0000 |
| 9.03 | Breakeven 10 | 9096.99 | -9096.99 | 0.00 | 1.7328 | 0.0000 |
| 10.03 | Breakeven 11 | 8996.66 | -8996.66 | 0.00 | 1.7136 | 0.0000 |
| 11.04 | Breakeven 12 | 8896.32 | -8896.32 | 0.00 | 1.6945 | 0.0000 |
| 12.04 | Breakeven 13 | 8795.99 | -8795.99 | 0.00 | 1.6754 | 0.0000 |
| 13.04 | Breakeven 14 | 8695.65 | -8695.65 | 0.00 | 1.6563 | 0.0000 |
| 14.05 | Breakeven 15 | 8595.32 | -8595.32 | 0.00 | 1.6372 | 0.0000 |
| 15.05 | Breakeven 16 | 8494.98 | -8494.98 | 0.00 | 1.6181 | 0.0000 |
| 17.06 | Breakeven 17 | 8294.31 | -8294.31 | 0.00 | 1.5799 | 0.0000 |
| 18.06 | Breakeven 18 | 8193.98 | -8193.98 | -0.00 | 1.5608 | -0.0000 |
| 19.06 | Breakeven 19 | 8093.65 | -8093.65 | 0.00 | 1.5416 | 0.0000 |
| 20.07 | Breakeven 20 | 7993.31 | -7993.31 | 0.00 | 1.5225 | 0.0000 |
| 21.07 | Breakeven 21 | 7892.98 | -7892.98 | 0.00 | 1.5034 | 0.0000 |
| 22.07 | Breakeven 22 | 7792.64 | -7792.64 | 0.00 | 1.4843 | 0.0000 |
| 23.08 | Breakeven 23 | 7692.31 | -7692.31 | 0.00 | 1.4652 | 0.0000 |
| 24.08 | Breakeven 24 | 7591.97 | -7591.97 | 0.00 | 1.4461 | 0.0000 |
| 25.08 | Breakeven 25 | 7491.64 | -7491.64 | 0.00 | 1.4270 | 0.0000 |
| 26.09 | Breakeven 26 | 7391.30 | -7391.30 | 0.00 | 1.4079 | 0.0000 |
| 27.09 | Breakeven 27 | 7290.97 | -7290.97 | 0.00 | 1.3888 | 0.0000 |
| 28.09 | Breakeven 28 | 7190.64 | -7190.64 | 0.00 | 1.3696 | 0.0000 |
| 29.10 | Breakeven 29 | 7090.30 | -7090.30 | 0.00 | 1.3505 | 0.0000 |
| 30.10 | Breakeven 30 | 6989.97 | -6989.97 | 0.00 | 1.3314 | 0.0000 |
| 31.10 | Breakeven 31 | 6889.63 | -6889.63 | 0.00 | 1.3123 | 0.0000 |
| 32.11 | Breakeven 32 | 6789.30 | -6789.30 | 0.00 | 1.2932 | 0.0000 |
| 33.11 | Breakeven 33 | 6688.96 | -6688.96 | 0.00 | 1.2741 | 0.0000 |
| 34.11 | Breakeven 34 | 6588.63 | -6588.63 | 0.00 | 1.2550 | 0.0000 |
| 35.12 | Breakeven 35 | 6488.29 | -6488.29 | 0.00 | 1.2359 | 0.0000 |
| 36.12 | Breakeven 36 | 6387.96 | -6387.96 | 0.00 | 1.2168 | 0.0000 |
| 37.12 | Breakeven 37 | 6287.63 | -6287.63 | 0.00 | 1.1976 | 0.0000 |
| 38.13 | Breakeven 38 | 6187.29 | -6187.29 | 0.00 | 1.1785 | 0.0000 |
| 39.13 | Breakeven 39 | 6086.96 | -6086.96 | 0.00 | 1.1594 | 0.0000 |
| 40.13 | Breakeven 40 | 5986.62 | -5986.62 | 0.00 | 1.1403 | 0.0000 |
| 41.14 | Breakeven 41 | 5886.29 | -5886.29 | 0.00 | 1.1212 | 0.0000 |
| 42.14 | Breakeven 42 | 5785.95 | -5785.95 | 0.00 | 1.1021 | 0.0000 |
| 43.14 | Breakeven 43 | 5685.62 | -5685.62 | 0.00 | 1.0830 | 0.0000 |
| 44.15 | Breakeven 44 | 5585.28 | -5585.28 | 0.00 | 1.0639 | 0.0000 |
| 45.15 | Breakeven 45 | 5484.95 | -5484.95 | 0.00 | 1.0448 | 0.0000 |
| 46.15 | Breakeven 46 | 5384.62 | -5384.62 | 0.00 | 1.0256 | 0.0000 |
| 47.16 | Breakeven 47 | 5284.28 | -5284.28 | 0.00 | 1.0065 | 0.0000 |
| 48.16 | Breakeven 48 | 5183.95 | -5183.95 | 0.00 | 0.9874 | 0.0000 |
| 49.16 | Breakeven 49 | 5083.61 | -5083.61 | 0.00 | 0.9683 | 0.0000 |
| 50.17 | Breakeven 50 | 4983.28 | -4983.28 | 0.00 | 0.9492 | 0.0000 |
| 51.17 | Breakeven 51 | 4882.94 | -4882.94 | 0.00 | 0.9301 | 0.0000 |
| 52.17 | Breakeven 52 | 4782.61 | -4782.61 | 0.00 | 0.9110 | 0.0000 |
| 53.18 | Breakeven 53 | 4682.27 | -4682.27 | 0.00 | 0.8919 | 0.0000 |
| 54.18 | Breakeven 54 | 4581.94 | -4581.94 | 0.00 | 0.8728 | 0.0000 |
| 55.18 | Breakeven 55 | 4481.61 | -4481.61 | 0.00 | 0.8536 | 0.0000 |
| 56.19 | Breakeven 56 | 4381.27 | -4381.27 | 0.00 | 0.8345 | 0.0000 |
| 58.19 | Breakeven 57 | 4180.60 | -4180.60 | 0.00 | 0.7963 | 0.0000 |
| 59.20 | Breakeven 58 | 4080.27 | -4080.27 | 0.00 | 0.7772 | 0.0000 |
| 60.20 | Breakeven 59 | 3979.93 | -3979.93 | 0.00 | 0.7581 | 0.0000 |
| 61.20 | Breakeven 60 | 3879.60 | -3879.60 | 0.00 | 0.7390 | 0.0000 |
| 62.21 | Breakeven 61 | 3779.26 | -3779.26 | 0.00 | 0.7199 | 0.0000 |
| 63.21 | Breakeven 62 | 3678.93 | -3678.93 | 0.00 | 0.7007 | 0.0000 |
| 64.21 | Breakeven 63 | 3578.60 | -3578.60 | 0.00 | 0.6816 | 0.0000 |
| 65.22 | Breakeven 64 | 3478.26 | -3478.26 | 0.00 | 0.6625 | 0.0000 |
| 66.22 | Breakeven 65 | 3377.93 | -3377.93 | 0.00 | 0.6434 | 0.0000 |
| 67.22 | Breakeven 66 | 3277.59 | -3277.59 | 0.00 | 0.6243 | 0.0000 |
| 68.23 | Breakeven 67 | 3177.26 | -3177.26 | 0.00 | 0.6052 | 0.0000 |
| 69.23 | Breakeven 68 | 3076.92 | -3076.92 | 0.00 | 0.5861 | 0.0000 |
| 70.23 | Breakeven 69 | 2976.59 | -2976.59 | 0.00 | 0.5670 | 0.0000 |
| 71.24 | Breakeven 70 | 2876.25 | -2876.25 | 0.00 | 0.5479 | 0.0000 |
| 72.24 | Breakeven 71 | 2775.92 | -2775.92 | 0.00 | 0.5287 | 0.0000 |
| 73.24 | Breakeven 72 | 2675.59 | -2675.59 | 0.00 | 0.5096 | 0.0000 |
| 74.25 | Breakeven 73 | 2575.25 | -2575.25 | 0.00 | 0.4905 | 0.0000 |
| 75.25 | Breakeven 74 | 2474.92 | -2474.92 | 0.00 | 0.4714 | 0.0000 |
| 76.25 | Breakeven 75 | 2374.58 | -2374.58 | 0.00 | 0.4523 | 0.0000 |
| 77.26 | Breakeven 76 | 2274.25 | -2274.25 | 0.00 | 0.4332 | 0.0000 |
| 78.26 | Breakeven 77 | 2173.91 | -2173.91 | 0.00 | 0.4141 | 0.0000 |
| 79.26 | Breakeven 78 | 2073.58 | -2073.58 | -0.00 | 0.3950 | -0.0000 |
| 80.27 | Breakeven 79 | 1973.24 | -1973.24 | 0.00 | 0.3759 | 0.0000 |
| 81.27 | Breakeven 80 | 1872.91 | -1872.91 | 0.00 | 0.3567 | 0.0000 |
| 82.27 | Breakeven 81 | 1772.58 | -1772.58 | 0.00 | 0.3376 | 0.0000 |
| 83.28 | Breakeven 82 | 1672.24 | -1672.24 | 0.00 | 0.3185 | 0.0000 |
| 84.28 | Breakeven 83 | 1571.91 | -1571.91 | 0.00 | 0.2994 | 0.0000 |
| 85.00 | Downside (15%) | 1500.00 | -1500.00 | 0.00 | 0.2857 | 0.0000 |
| 85.28 | Breakeven 84 | 1471.57 | -1471.57 | 0.00 | 0.2803 | 0.0000 |
| 86.29 | Breakeven 85 | 1371.24 | -1371.24 | 0.00 | 0.2612 | 0.0000 |
| 87.29 | Breakeven 86 | 1270.90 | -1270.90 | 0.00 | 0.2421 | 0.0000 |
| 88.29 | Breakeven 87 | 1170.57 | -1170.57 | 0.00 | 0.2230 | 0.0000 |
| 89.30 | Breakeven 88 | 1070.23 | -1070.23 | 0.00 | 0.2039 | 0.0000 |
| 90.30 | Breakeven 89 | 969.90 | -969.90 | 0.00 | 0.1847 | 0.0000 |
| 91.30 | Breakeven 90 | 869.57 | -869.57 | 0.00 | 0.1656 | 0.0000 |
| 92.31 | Breakeven 91 | 769.23 | -769.23 | 0.00 | 0.1465 | 0.0000 |
| 93.31 | Breakeven 92 | 668.90 | -668.90 | 0.00 | 0.1274 | 0.0000 |
| 94.31 | Breakeven 93 | 568.56 | -568.56 | 0.00 | 0.1083 | 0.0000 |
| 95.32 | Breakeven 94 | 468.23 | -468.23 | 0.00 | 0.0892 | 0.0000 |
| 96.32 | Breakeven 95 | 367.89 | -367.89 | 0.00 | 0.0701 | 0.0000 |
| 97.32 | Breakeven 96 | 267.56 | -267.56 | 0.00 | 0.0510 | 0.0000 |
| 98.33 | Breakeven 97 | 167.22 | -167.22 | 0.00 | 0.0319 | 0.0000 |
| 99.33 | Breakeven 98 | 66.89 | -66.89 | 0.00 | 0.0127 | 0.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.33 | Breakeven 100 | -33.44 | 33.44 | 0.00 | -0.0064 | 0.0000 |
| 101.34 | Breakeven 101 | -133.78 | 133.78 | 0.00 | -0.0255 | 0.0000 |
| 102.34 | Breakeven 102 | -234.11 | 234.11 | 0.00 | -0.0446 | 0.0000 |
| 103.34 | Breakeven 103 | -334.45 | 334.45 | 0.00 | -0.0637 | 0.0000 |
| 104.35 | Breakeven 104 | -434.78 | 434.78 | 0.00 | -0.0828 | 0.0000 |
| 105.35 | Breakeven 105 | -535.12 | 535.12 | 0.00 | -0.1019 | 0.0000 |
| 106.35 | Breakeven 106 | -635.45 | 635.45 | 0.00 | -0.1210 | 0.0000 |
| 107.36 | Breakeven 107 | -735.79 | 735.79 | 0.00 | -0.1401 | 0.0000 |
| 108.36 | Breakeven 108 | -836.12 | 836.12 | 0.00 | -0.1593 | 0.0000 |
| 109.36 | Breakeven 109 | -936.45 | 936.45 | 0.00 | -0.1784 | 0.0000 |
| 110.37 | Breakeven 110 | -1036.79 | 1036.79 | 0.00 | -0.1975 | 0.0000 |
| 111.37 | Breakeven 111 | -1137.12 | 1137.12 | 0.00 | -0.2166 | 0.0000 |
| 112.37 | Breakeven 112 | -1237.46 | 1237.46 | 0.00 | -0.2357 | 0.0000 |
| 113.38 | Breakeven 113 | -1337.79 | 1337.79 | 0.00 | -0.2548 | 0.0000 |
| 114.38 | Breakeven 114 | -1438.13 | 1438.13 | 0.00 | -0.2739 | 0.0000 |
| 115.00 | Upside (15%) | -1500.00 | 1500.00 | 0.00 | -0.2857 | 0.0000 |
| 115.38 | Breakeven 115 | -1538.46 | 1538.46 | 0.00 | -0.2930 | 0.0000 |
| 116.39 | Breakeven 116 | -1638.80 | 1638.80 | 0.00 | -0.3122 | 0.0000 |
| 117.39 | Breakeven 117 | -1739.13 | 1739.13 | 0.00 | -0.3313 | 0.0000 |
| 118.39 | Breakeven 118 | -1839.46 | 1839.46 | 0.00 | -0.3504 | 0.0000 |
| 119.40 | Breakeven 119 | -1939.80 | 1939.80 | 0.00 | -0.3695 | 0.0000 |
| 120.40 | Breakeven 120 | -2040.13 | 2040.13 | 0.00 | -0.3886 | 0.0000 |
| 122.41 | Breakeven 121 | -2240.80 | 2240.80 | 0.00 | -0.4268 | 0.0000 |
| 123.41 | Breakeven 122 | -2341.14 | 2341.14 | 0.00 | -0.4459 | 0.0000 |
| 124.41 | Breakeven 123 | -2441.47 | 2441.47 | 0.00 | -0.4650 | 0.0000 |
| 125.42 | Breakeven 124 | -2541.81 | 2541.81 | 0.00 | -0.4842 | 0.0000 |
| 126.42 | Breakeven 125 | -2642.14 | 2642.14 | 0.00 | -0.5033 | 0.0000 |
| 127.42 | Breakeven 126 | -2742.47 | 2742.47 | 0.00 | -0.5224 | 0.0000 |
| 128.43 | Breakeven 127 | -2842.81 | 2842.81 | 0.00 | -0.5415 | 0.0000 |
| 129.43 | Breakeven 128 | -2943.14 | 2943.14 | 0.00 | -0.5606 | 0.0000 |
| 130.43 | Breakeven 129 | -3043.48 | 3043.48 | 0.00 | -0.5797 | 0.0000 |
| 131.44 | Breakeven 130 | -3143.81 | 3143.81 | 0.00 | -0.5988 | 0.0000 |
| 132.44 | Breakeven 131 | -3244.15 | 3244.15 | 0.00 | -0.6179 | 0.0000 |
| 133.44 | Breakeven 132 | -3344.48 | 3344.48 | 0.00 | -0.6370 | 0.0000 |
| 134.45 | Breakeven 133 | -3444.82 | 3444.82 | 0.00 | -0.6562 | 0.0000 |
| 135.45 | Breakeven 134 | -3545.15 | 3545.15 | 0.00 | -0.6753 | 0.0000 |
| 136.45 | Breakeven 135 | -3645.48 | 3645.48 | 0.00 | -0.6944 | 0.0000 |
| 137.46 | Breakeven 136 | -3745.82 | 3745.82 | 0.00 | -0.7135 | 0.0000 |
| 138.46 | Breakeven 137 | -3846.15 | 3846.15 | 0.00 | -0.7326 | 0.0000 |
| 139.46 | Breakeven 138 | -3946.49 | 3946.49 | 0.00 | -0.7517 | 0.0000 |
| 140.47 | Breakeven 139 | -4046.82 | 4046.82 | 0.00 | -0.7708 | 0.0000 |
| 141.47 | Breakeven 140 | -4147.16 | 4147.16 | 0.00 | -0.7899 | 0.0000 |
| 142.47 | Breakeven 141 | -4247.49 | 4247.49 | 0.00 | -0.8090 | 0.0000 |
| 143.48 | Breakeven 142 | -4347.83 | 4347.83 | 0.00 | -0.8282 | 0.0000 |
| 144.48 | Breakeven 143 | -4448.16 | 4448.16 | 0.00 | -0.8473 | 0.0000 |
| 145.48 | Breakeven 144 | -4548.49 | 4548.49 | 0.00 | -0.8664 | 0.0000 |
| 146.49 | Breakeven 145 | -4648.83 | 4648.83 | 0.00 | -0.8855 | 0.0000 |
| 147.49 | Breakeven 146 | -4749.16 | 4749.16 | 0.00 | -0.9046 | 0.0000 |
| 148.49 | Breakeven 147 | -4849.50 | 4849.50 | 0.00 | -0.9237 | 0.0000 |
| 149.50 | Breakeven 148 | -4949.83 | 4949.83 | 0.00 | -0.9428 | 0.0000 |
| 150.50 | Breakeven 149 | -5050.17 | 5050.17 | 0.00 | -0.9619 | 0.0000 |
| 151.51 | Breakeven 150 | -5150.50 | 5150.50 | 0.00 | -0.9810 | 0.0000 |
| 152.51 | Breakeven 151 | -5250.84 | 5250.84 | 0.00 | -1.0002 | 0.0000 |
| 153.51 | Breakeven 152 | -5351.17 | 5351.17 | 0.00 | -1.0193 | 0.0000 |
| 154.52 | Breakeven 153 | -5451.51 | 5451.51 | 0.00 | -1.0384 | 0.0000 |
| 155.52 | Breakeven 154 | -5551.84 | 5551.84 | 0.00 | -1.0575 | 0.0000 |
| 156.52 | Breakeven 155 | -5652.17 | 5652.17 | 0.00 | -1.0766 | 0.0000 |
| 157.53 | Breakeven 156 | -5752.51 | 5752.51 | 0.00 | -1.0957 | 0.0000 |
| 158.53 | Breakeven 157 | -5852.84 | 5852.84 | 0.00 | -1.1148 | 0.0000 |
| 159.53 | Breakeven 158 | -5953.18 | 5953.18 | 0.00 | -1.1339 | 0.0000 |
| 160.54 | Breakeven 159 | -6053.51 | 6053.51 | 0.00 | -1.1530 | 0.0000 |
| 161.54 | Breakeven 160 | -6153.85 | 6153.85 | 0.00 | -1.1722 | 0.0000 |
| 162.54 | Breakeven 161 | -6254.18 | 6254.18 | 0.00 | -1.1913 | 0.0000 |
| 163.55 | Breakeven 162 | -6354.52 | 6354.52 | 0.00 | -1.2104 | 0.0000 |
| 164.55 | Breakeven 163 | -6454.85 | 6454.85 | 0.00 | -1.2295 | 0.0000 |
| 165.55 | Breakeven 164 | -6555.18 | 6555.18 | 0.00 | -1.2486 | 0.0000 |
| 166.56 | Breakeven 165 | -6655.52 | 6655.52 | 0.00 | -1.2677 | 0.0000 |
| 167.56 | Breakeven 166 | -6755.85 | 6755.85 | 0.00 | -1.2868 | 0.0000 |
| 168.56 | Breakeven 167 | -6856.19 | 6856.19 | 0.00 | -1.3059 | 0.0000 |
| 169.57 | Breakeven 168 | -6956.52 | 6956.52 | 0.00 | -1.3251 | 0.0000 |
| 170.57 | Breakeven 169 | -7056.86 | 7056.86 | 0.00 | -1.3442 | 0.0000 |
| 171.57 | Breakeven 170 | -7157.19 | 7157.19 | 0.00 | -1.3633 | 0.0000 |
| 172.58 | Breakeven 171 | -7257.53 | 7257.53 | 0.00 | -1.3824 | 0.0000 |
| 173.58 | Breakeven 172 | -7357.86 | 7357.86 | 0.00 | -1.4015 | 0.0000 |
| 174.58 | Breakeven 173 | -7458.19 | 7458.19 | 0.00 | -1.4206 | 0.0000 |
| 175.59 | Breakeven 174 | -7558.53 | 7558.53 | 0.00 | -1.4397 | 0.0000 |
| 176.59 | Breakeven 175 | -7658.86 | 7658.86 | 0.00 | -1.4588 | 0.0000 |
| 177.59 | Breakeven 176 | -7759.20 | 7759.20 | 0.00 | -1.4779 | 0.0000 |
| 178.60 | Breakeven 177 | -7859.53 | 7859.53 | 0.00 | -1.4971 | 0.0000 |
| 179.60 | Breakeven 178 | -7959.87 | 7959.87 | 0.00 | -1.5162 | 0.0000 |
| 180.60 | Breakeven 179 | -8060.20 | 8060.20 | 0.00 | -1.5353 | 0.0000 |
| 181.61 | Breakeven 180 | -8160.54 | 8160.54 | 0.00 | -1.5544 | 0.0000 |
| 183.61 | Breakeven 181 | -8361.20 | 8361.20 | 0.00 | -1.5926 | 0.0000 |
| 184.62 | Breakeven 182 | -8461.54 | 8461.54 | 0.00 | -1.6117 | 0.0000 |
| 185.62 | Breakeven 183 | -8561.87 | 8561.87 | 0.00 | -1.6308 | 0.0000 |
| 186.62 | Breakeven 184 | -8662.21 | 8662.21 | 0.00 | -1.6499 | 0.0000 |
| 187.63 | Breakeven 185 | -8762.54 | 8762.54 | 0.00 | -1.6691 | 0.0000 |
| 188.63 | Breakeven 186 | -8862.88 | 8862.88 | 0.00 | -1.6882 | 0.0000 |
| 189.63 | Breakeven 187 | -8963.21 | 8963.21 | 0.00 | -1.7073 | 0.0000 |
| 190.64 | Breakeven 188 | -9063.55 | 9063.55 | 0.00 | -1.7264 | 0.0000 |
| 191.64 | Breakeven 189 | -9163.88 | 9163.88 | 0.00 | -1.7455 | 0.0000 |
| 192.64 | Breakeven 190 | -9264.21 | 9264.21 | 0.00 | -1.7646 | 0.0000 |
| 193.65 | Breakeven 191 | -9364.55 | 9364.55 | 0.00 | -1.7837 | 0.0000 |
| 194.65 | Breakeven 192 | -9464.88 | 9464.88 | 0.00 | -1.8028 | 0.0000 |
| 195.65 | Breakeven 193 | -9565.22 | 9565.22 | 0.00 | -1.8219 | 0.0000 |
| 196.66 | Breakeven 194 | -9665.55 | 9665.55 | 0.00 | -1.8411 | 0.0000 |
| 197.66 | Breakeven 195 | -9765.89 | 9765.89 | 0.00 | -1.8602 | 0.0000 |
| 198.66 | Breakeven 196 | -9866.22 | 9866.22 | 0.00 | -1.8793 | 0.0000 |
| 199.67 | Breakeven 197 | -9966.56 | 9966.56 | 0.00 | -1.8984 | 0.0000 |
| 200.67 | Breakeven 198 | -10066.89 | 10066.89 | 0.00 | -1.9175 | 0.0000 |
| 201.67 | Breakeven 199 | -10167.22 | 10167.22 | 0.00 | -1.9366 | 0.0000 |
| 202.68 | Breakeven 200 | -10267.56 | 10267.56 | 0.00 | -1.9557 | 0.0000 |
| 203.68 | Breakeven 201 | -10367.89 | 10367.89 | 0.00 | -1.9748 | 0.0000 |
| 204.68 | Breakeven 202 | -10468.23 | 10468.23 | 0.00 | -1.9939 | 0.0000 |
| 205.69 | Breakeven 203 | -10568.56 | 10568.56 | 0.00 | -2.0131 | 0.0000 |
| 206.69 | Breakeven 204 | -10668.90 | 10668.90 | 0.00 | -2.0322 | 0.0000 |
| 207.69 | Breakeven 205 | -10769.23 | 10769.23 | 0.00 | -2.0513 | 0.0000 |
| 208.70 | Breakeven 206 | -10869.57 | 10869.57 | 0.00 | -2.0704 | 0.0000 |
| 209.70 | Breakeven 207 | -10969.90 | 10969.90 | 0.00 | -2.0895 | 0.0000 |
| 210.70 | Breakeven 208 | -11070.23 | 11070.23 | 0.00 | -2.1086 | 0.0000 |
| 211.71 | Breakeven 209 | -11170.57 | 11170.57 | 0.00 | -2.1277 | 0.0000 |
| 212.71 | Breakeven 210 | -11270.90 | 11270.90 | 0.00 | -2.1468 | 0.0000 |
| 213.71 | Breakeven 211 | -11371.24 | 11371.24 | 0.00 | -2.1660 | 0.0000 |
| 214.72 | Breakeven 212 | -11471.57 | 11471.57 | 0.00 | -2.1851 | 0.0000 |
| 215.72 | Breakeven 213 | -11571.91 | 11571.91 | 0.00 | -2.2042 | 0.0000 |
| 216.72 | Breakeven 214 | -11672.24 | 11672.24 | 0.00 | -2.2233 | 0.0000 |
| 217.73 | Breakeven 215 | -11772.58 | 11772.58 | 0.00 | -2.2424 | 0.0000 |
| 218.73 | Breakeven 216 | -11872.91 | 11872.91 | 0.00 | -2.2615 | 0.0000 |
| 219.73 | Breakeven 217 | -11973.24 | 11973.24 | 0.00 | -2.2806 | 0.0000 |
| 220.74 | Breakeven 218 | -12073.58 | 12073.58 | 0.00 | -2.2997 | 0.0000 |
| 221.74 | Breakeven 219 | -12173.91 | 12173.91 | 0.00 | -2.3188 | 0.0000 |
| 222.74 | Breakeven 220 | -12274.25 | 12274.25 | 0.00 | -2.3380 | 0.0000 |
| 223.75 | Breakeven 221 | -12374.58 | 12374.58 | 0.00 | -2.3571 | 0.0000 |
| 224.75 | Breakeven 222 | -12474.92 | 12474.92 | 0.00 | -2.3762 | 0.0000 |
| 225.75 | Breakeven 223 | -12575.25 | 12575.25 | 0.00 | -2.3953 | 0.0000 |
| 226.76 | Breakeven 224 | -12675.59 | 12675.59 | 0.00 | -2.4144 | 0.0000 |
| 227.76 | Breakeven 225 | -12775.92 | 12775.92 | 0.00 | -2.4335 | 0.0000 |
| 228.76 | Breakeven 226 | -12876.25 | 12876.25 | 0.00 | -2.4526 | 0.0000 |
| 229.77 | Breakeven 227 | -12976.59 | 12976.59 | 0.00 | -2.4717 | 0.0000 |
| 230.77 | Breakeven 228 | -13076.92 | 13076.92 | 0.00 | -2.4908 | 0.0000 |
| 231.77 | Breakeven 229 | -13177.26 | 13177.26 | 0.00 | -2.5100 | 0.0000 |
| 232.78 | Breakeven 230 | -13277.59 | 13277.59 | 0.00 | -2.5291 | 0.0000 |
| 233.78 | Breakeven 231 | -13377.93 | 13377.93 | 0.00 | -2.5482 | 0.0000 |
| 234.78 | Breakeven 232 | -13478.26 | 13478.26 | 0.00 | -2.5673 | 0.0000 |
| 235.79 | Breakeven 233 | -13578.60 | 13578.60 | 0.00 | -2.5864 | 0.0000 |
| 236.79 | Breakeven 234 | -13678.93 | 13678.93 | 0.00 | -2.6055 | 0.0000 |
| 237.79 | Breakeven 235 | -13779.26 | 13779.26 | 0.00 | -2.6246 | 0.0000 |
| 238.80 | Breakeven 236 | -13879.60 | 13879.60 | 0.00 | -2.6437 | 0.0000 |
| 239.80 | Breakeven 237 | -13979.93 | 13979.93 | 0.00 | -2.6628 | 0.0000 |
| 240.80 | Breakeven 238 | -14080.27 | 14080.27 | 0.00 | -2.6820 | 0.0000 |
| 241.81 | Breakeven 239 | -14180.60 | 14180.60 | 0.00 | -2.7011 | 0.0000 |
| 242.81 | Breakeven 240 | -14280.94 | 14280.94 | 0.00 | -2.7202 | 0.0000 |
| 243.81 | Breakeven 241 | -14381.27 | 14381.27 | 0.00 | -2.7393 | 0.0000 |
| 244.82 | Breakeven 242 | -14481.61 | 14481.61 | 0.00 | -2.7584 | 0.0000 |
| 245.82 | Breakeven 243 | -14581.94 | 14581.94 | 0.00 | -2.7775 | 0.0000 |
| 246.82 | Breakeven 244 | -14682.27 | 14682.27 | 0.00 | -2.7966 | 0.0000 |
| 247.83 | Breakeven 245 | -14782.61 | 14782.61 | 0.00 | -2.8157 | 0.0000 |
| 248.83 | Breakeven 246 | -14882.94 | 14882.94 | 0.00 | -2.8348 | 0.0000 |
| 249.83 | Breakeven 247 | -14983.28 | 14983.28 | 0.00 | -2.8540 | 0.0000 |
| 250.84 | Breakeven 248 | -15083.61 | 15083.61 | 0.00 | -2.8731 | 0.0000 |
| 251.84 | Breakeven 249 | -15183.95 | 15183.95 | 0.00 | -2.8922 | 0.0000 |
| 252.84 | Breakeven 250 | -15284.28 | 15284.28 | 0.00 | -2.9113 | 0.0000 |
| 253.85 | Breakeven 251 | -15384.62 | 15384.62 | 0.00 | -2.9304 | 0.0000 |
| 254.85 | Breakeven 252 | -15484.95 | 15484.95 | 0.00 | -2.9495 | 0.0000 |
| 255.85 | Breakeven 253 | -15585.28 | 15585.28 | 0.00 | -2.9686 | 0.0000 |
| 256.86 | Breakeven 254 | -15685.62 | 15685.62 | 0.00 | -2.9877 | 0.0000 |
| 257.86 | Breakeven 255 | -15785.95 | 15785.95 | 0.00 | -3.0068 | 0.0000 |
| 258.86 | Breakeven 256 | -15886.29 | 15886.29 | 0.00 | -3.0260 | 0.0000 |
| 259.87 | Breakeven 257 | -15986.62 | 15986.62 | 0.00 | -3.0451 | 0.0000 |
| 260.87 | Breakeven 258 | -16086.96 | 16086.96 | 0.00 | -3.0642 | 0.0000 |
| 261.87 | Breakeven 259 | -16187.29 | 16187.29 | 0.00 | -3.0833 | 0.0000 |
| 262.88 | Breakeven 260 | -16287.63 | 16287.63 | 0.00 | -3.1024 | 0.0000 |
| 263.88 | Breakeven 261 | -16387.96 | 16387.96 | 0.00 | -3.1215 | 0.0000 |
| 264.88 | Breakeven 262 | -16488.29 | 16488.29 | 0.00 | -3.1406 | 0.0000 |
| 265.89 | Breakeven 263 | -16588.63 | 16588.63 | 0.00 | -3.1597 | 0.0000 |
| 266.89 | Breakeven 264 | -16688.96 | 16688.96 | 0.00 | -3.1789 | 0.0000 |
| 267.89 | Breakeven 265 | -16789.30 | 16789.30 | 0.00 | -3.1980 | 0.0000 |
| 268.90 | Breakeven 266 | -16889.63 | 16889.63 | 0.00 | -3.2171 | 0.0000 |
| 269.90 | Breakeven 267 | -16989.97 | 16989.97 | 0.00 | -3.2362 | 0.0000 |
| 270.90 | Breakeven 268 | -17090.30 | 17090.30 | 0.00 | -3.2553 | 0.0000 |
| 271.91 | Breakeven 269 | -17190.64 | 17190.64 | 0.00 | -3.2744 | 0.0000 |
| 272.91 | Breakeven 270 | -17290.97 | 17290.97 | 0.00 | -3.2935 | 0.0000 |
| 273.91 | Breakeven 271 | -17391.30 | 17391.30 | 0.00 | -3.3126 | 0.0000 |
| 274.92 | Breakeven 272 | -17491.64 | 17491.64 | 0.00 | -3.3317 | 0.0000 |
| 275.92 | Breakeven 273 | -17591.97 | 17591.97 | 0.00 | -3.3509 | 0.0000 |
| 276.92 | Breakeven 274 | -17692.31 | 17692.31 | 0.00 | -3.3700 | 0.0000 |
| 277.93 | Breakeven 275 | -17792.64 | 17792.64 | 0.00 | -3.3891 | 0.0000 |
| 278.93 | Breakeven 276 | -17892.98 | 17892.98 | 0.00 | -3.4082 | 0.0000 |
| 279.93 | Breakeven 277 | -17993.31 | 17993.31 | 0.00 | -3.4273 | 0.0000 |
| 280.94 | Breakeven 278 | -18093.65 | 18093.65 | 0.00 | -3.4464 | 0.0000 |
| 281.94 | Breakeven 279 | -18193.98 | 18193.98 | 0.00 | -3.4655 | 0.0000 |
| 282.94 | Breakeven 280 | -18294.31 | 18294.31 | 0.00 | -3.4846 | 0.0000 |
| 283.95 | Breakeven 281 | -18394.65 | 18394.65 | 0.00 | -3.5037 | 0.0000 |
| 284.95 | Breakeven 282 | -18494.98 | 18494.98 | 0.00 | -3.5229 | 0.0000 |
| 285.95 | Breakeven 283 | -18595.32 | 18595.32 | 0.00 | -3.5420 | 0.0000 |
| 286.96 | Breakeven 284 | -18695.65 | 18695.65 | 0.00 | -3.5611 | 0.0000 |
| 287.96 | Breakeven 285 | -18795.99 | 18795.99 | 0.00 | -3.5802 | 0.0000 |
| 288.96 | Breakeven 286 | -18896.32 | 18896.32 | 0.00 | -3.5993 | 0.0000 |
| 289.97 | Breakeven 287 | -18996.66 | 18996.66 | 0.00 | -3.6184 | 0.0000 |
| 290.97 | Breakeven 288 | -19096.99 | 19096.99 | 0.00 | -3.6375 | 0.0000 |
| 291.97 | Breakeven 289 | -19197.32 | 19197.32 | 0.00 | -3.6566 | 0.0000 |
| 292.98 | Breakeven 290 | -19297.66 | 19297.66 | 0.00 | -3.6757 | 0.0000 |
| 293.98 | Breakeven 291 | -19397.99 | 19397.99 | 0.00 | -3.6949 | 0.0000 |
| 294.98 | Breakeven 292 | -19498.33 | 19498.33 | 0.00 | -3.7140 | 0.0000 |
| 295.99 | Breakeven 293 | -19598.66 | 19598.66 | 0.00 | -3.7331 | 0.0000 |
| 296.99 | Breakeven 294 | -19699.00 | 19699.00 | 0.00 | -3.7522 | 0.0000 |
| 297.99 | Breakeven 295 | -19799.33 | 19799.33 | 0.00 | -3.7713 | 0.0000 |
| 299.00 | Breakeven 296 | -19899.67 | 19899.67 | 0.00 | -3.7904 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| breakeven_1 | Breakeven 1 | 0.00 | -100.00% | 10000.00 | 0.00 | 0.0000 |
| zero | Stock to Zero | 0.00 | -100.00% | 10000.00 | 0.00 | 0.0000 |
| breakeven_2 | Breakeven 2 | 1.00 | -99.00% | 9899.67 | 0.00 | 0.0000 |
| breakeven_3 | Breakeven 3 | 2.01 | -97.99% | 9799.33 | 0.00 | 0.0000 |
| breakeven_4 | Breakeven 4 | 3.01 | -96.99% | 9699.00 | 0.00 | 0.0000 |
| breakeven_5 | Breakeven 5 | 4.01 | -95.99% | 9598.66 | 0.00 | 0.0000 |
| breakeven_6 | Breakeven 6 | 5.02 | -94.98% | 9498.33 | 0.00 | 0.0000 |
| breakeven_7 | Breakeven 7 | 6.02 | -93.98% | 9397.99 | 0.00 | 0.0000 |
| breakeven_8 | Breakeven 8 | 7.02 | -92.98% | 9297.66 | 0.00 | 0.0000 |
| breakeven_9 | Breakeven 9 | 8.03 | -91.97% | 9197.32 | 0.00 | 0.0000 |
| breakeven_10 | Breakeven 10 | 9.03 | -90.97% | 9096.99 | 0.00 | 0.0000 |
| breakeven_11 | Breakeven 11 | 10.03 | -89.97% | 8996.66 | 0.00 | 0.0000 |
| breakeven_12 | Breakeven 12 | 11.04 | -88.96% | 8896.32 | 0.00 | 0.0000 |
| breakeven_13 | Breakeven 13 | 12.04 | -87.96% | 8795.99 | 0.00 | 0.0000 |
| breakeven_14 | Breakeven 14 | 13.04 | -86.96% | 8695.65 | 0.00 | 0.0000 |
| breakeven_15 | Breakeven 15 | 14.05 | -85.95% | 8595.32 | 0.00 | 0.0000 |
| breakeven_16 | Breakeven 16 | 15.05 | -84.95% | 8494.98 | 0.00 | 0.0000 |
| breakeven_17 | Breakeven 17 | 17.06 | -82.94% | 8294.31 | 0.00 | 0.0000 |
| breakeven_18 | Breakeven 18 | 18.06 | -81.94% | 8193.98 | -0.00 | -0.0000 |
| breakeven_19 | Breakeven 19 | 19.06 | -80.94% | 8093.65 | 0.00 | 0.0000 |
| breakeven_20 | Breakeven 20 | 20.07 | -79.93% | 7993.31 | 0.00 | 0.0000 |
| breakeven_21 | Breakeven 21 | 21.07 | -78.93% | 7892.98 | 0.00 | 0.0000 |
| breakeven_22 | Breakeven 22 | 22.07 | -77.93% | 7792.64 | 0.00 | 0.0000 |
| breakeven_23 | Breakeven 23 | 23.08 | -76.92% | 7692.31 | 0.00 | 0.0000 |
| breakeven_24 | Breakeven 24 | 24.08 | -75.92% | 7591.97 | 0.00 | 0.0000 |
| breakeven_25 | Breakeven 25 | 25.08 | -74.92% | 7491.64 | 0.00 | 0.0000 |
| breakeven_26 | Breakeven 26 | 26.09 | -73.91% | 7391.30 | 0.00 | 0.0000 |
| breakeven_27 | Breakeven 27 | 27.09 | -72.91% | 7290.97 | 0.00 | 0.0000 |
| breakeven_28 | Breakeven 28 | 28.09 | -71.91% | 7190.64 | 0.00 | 0.0000 |
| breakeven_29 | Breakeven 29 | 29.10 | -70.90% | 7090.30 | 0.00 | 0.0000 |
| breakeven_30 | Breakeven 30 | 30.10 | -69.90% | 6989.97 | 0.00 | 0.0000 |
| breakeven_31 | Breakeven 31 | 31.10 | -68.90% | 6889.63 | 0.00 | 0.0000 |
| breakeven_32 | Breakeven 32 | 32.11 | -67.89% | 6789.30 | 0.00 | 0.0000 |
| breakeven_33 | Breakeven 33 | 33.11 | -66.89% | 6688.96 | 0.00 | 0.0000 |
| breakeven_34 | Breakeven 34 | 34.11 | -65.89% | 6588.63 | 0.00 | 0.0000 |
| breakeven_35 | Breakeven 35 | 35.12 | -64.88% | 6488.29 | 0.00 | 0.0000 |
| breakeven_36 | Breakeven 36 | 36.12 | -63.88% | 6387.96 | 0.00 | 0.0000 |
| breakeven_37 | Breakeven 37 | 37.12 | -62.88% | 6287.63 | 0.00 | 0.0000 |
| breakeven_38 | Breakeven 38 | 38.13 | -61.87% | 6187.29 | 0.00 | 0.0000 |
| breakeven_39 | Breakeven 39 | 39.13 | -60.87% | 6086.96 | 0.00 | 0.0000 |
| breakeven_40 | Breakeven 40 | 40.13 | -59.87% | 5986.62 | 0.00 | 0.0000 |
| breakeven_41 | Breakeven 41 | 41.14 | -58.86% | 5886.29 | 0.00 | 0.0000 |
| breakeven_42 | Breakeven 42 | 42.14 | -57.86% | 5785.95 | 0.00 | 0.0000 |
| breakeven_43 | Breakeven 43 | 43.14 | -56.86% | 5685.62 | 0.00 | 0.0000 |
| breakeven_44 | Breakeven 44 | 44.15 | -55.85% | 5585.28 | 0.00 | 0.0000 |
| breakeven_45 | Breakeven 45 | 45.15 | -54.85% | 5484.95 | 0.00 | 0.0000 |
| breakeven_46 | Breakeven 46 | 46.15 | -53.85% | 5384.62 | 0.00 | 0.0000 |
| breakeven_47 | Breakeven 47 | 47.16 | -52.84% | 5284.28 | 0.00 | 0.0000 |
| breakeven_48 | Breakeven 48 | 48.16 | -51.84% | 5183.95 | 0.00 | 0.0000 |
| breakeven_49 | Breakeven 49 | 49.16 | -50.84% | 5083.61 | 0.00 | 0.0000 |
| breakeven_50 | Breakeven 50 | 50.17 | -49.83% | 4983.28 | 0.00 | 0.0000 |
| breakeven_51 | Breakeven 51 | 51.17 | -48.83% | 4882.94 | 0.00 | 0.0000 |
| breakeven_52 | Breakeven 52 | 52.17 | -47.83% | 4782.61 | 0.00 | 0.0000 |
| breakeven_53 | Breakeven 53 | 53.18 | -46.82% | 4682.27 | 0.00 | 0.0000 |
| breakeven_54 | Breakeven 54 | 54.18 | -45.82% | 4581.94 | 0.00 | 0.0000 |
| breakeven_55 | Breakeven 55 | 55.18 | -44.82% | 4481.61 | 0.00 | 0.0000 |
| breakeven_56 | Breakeven 56 | 56.19 | -43.81% | 4381.27 | 0.00 | 0.0000 |
| breakeven_57 | Breakeven 57 | 58.19 | -41.81% | 4180.60 | 0.00 | 0.0000 |
| breakeven_58 | Breakeven 58 | 59.20 | -40.80% | 4080.27 | 0.00 | 0.0000 |
| breakeven_59 | Breakeven 59 | 60.20 | -39.80% | 3979.93 | 0.00 | 0.0000 |
| breakeven_60 | Breakeven 60 | 61.20 | -38.80% | 3879.60 | 0.00 | 0.0000 |
| breakeven_61 | Breakeven 61 | 62.21 | -37.79% | 3779.26 | 0.00 | 0.0000 |
| breakeven_62 | Breakeven 62 | 63.21 | -36.79% | 3678.93 | 0.00 | 0.0000 |
| breakeven_63 | Breakeven 63 | 64.21 | -35.79% | 3578.60 | 0.00 | 0.0000 |
| breakeven_64 | Breakeven 64 | 65.22 | -34.78% | 3478.26 | 0.00 | 0.0000 |
| breakeven_65 | Breakeven 65 | 66.22 | -33.78% | 3377.93 | 0.00 | 0.0000 |
| breakeven_66 | Breakeven 66 | 67.22 | -32.78% | 3277.59 | 0.00 | 0.0000 |
| breakeven_67 | Breakeven 67 | 68.23 | -31.77% | 3177.26 | 0.00 | 0.0000 |
| breakeven_68 | Breakeven 68 | 69.23 | -30.77% | 3076.92 | 0.00 | 0.0000 |
| breakeven_69 | Breakeven 69 | 70.23 | -29.77% | 2976.59 | 0.00 | 0.0000 |
| breakeven_70 | Breakeven 70 | 71.24 | -28.76% | 2876.25 | 0.00 | 0.0000 |
| breakeven_71 | Breakeven 71 | 72.24 | -27.76% | 2775.92 | 0.00 | 0.0000 |
| breakeven_72 | Breakeven 72 | 73.24 | -26.76% | 2675.59 | 0.00 | 0.0000 |
| breakeven_73 | Breakeven 73 | 74.25 | -25.75% | 2575.25 | 0.00 | 0.0000 |
| breakeven_74 | Breakeven 74 | 75.25 | -24.75% | 2474.92 | 0.00 | 0.0000 |
| breakeven_75 | Breakeven 75 | 76.25 | -23.75% | 2374.58 | 0.00 | 0.0000 |
| breakeven_76 | Breakeven 76 | 77.26 | -22.74% | 2274.25 | 0.00 | 0.0000 |
| breakeven_77 | Breakeven 77 | 78.26 | -21.74% | 2173.91 | 0.00 | 0.0000 |
| breakeven_78 | Breakeven 78 | 79.26 | -20.74% | 2073.58 | -0.00 | -0.0000 |
| breakeven_79 | Breakeven 79 | 80.27 | -19.73% | 1973.24 | 0.00 | 0.0000 |
| breakeven_80 | Breakeven 80 | 81.27 | -18.73% | 1872.91 | 0.00 | 0.0000 |
| breakeven_81 | Breakeven 81 | 82.27 | -17.73% | 1772.58 | 0.00 | 0.0000 |
| breakeven_82 | Breakeven 82 | 83.28 | -16.72% | 1672.24 | 0.00 | 0.0000 |
| breakeven_83 | Breakeven 83 | 84.28 | -15.72% | 1571.91 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1500.00 | 0.00 | 0.0000 |
| breakeven_84 | Breakeven 84 | 85.28 | -14.72% | 1471.57 | 0.00 | 0.0000 |
| breakeven_85 | Breakeven 85 | 86.29 | -13.71% | 1371.24 | 0.00 | 0.0000 |
| breakeven_86 | Breakeven 86 | 87.29 | -12.71% | 1270.90 | 0.00 | 0.0000 |
| breakeven_87 | Breakeven 87 | 88.29 | -11.71% | 1170.57 | 0.00 | 0.0000 |
| breakeven_88 | Breakeven 88 | 89.30 | -10.70% | 1070.23 | 0.00 | 0.0000 |
| breakeven_89 | Breakeven 89 | 90.30 | -9.70% | 969.90 | 0.00 | 0.0000 |
| breakeven_90 | Breakeven 90 | 91.30 | -8.70% | 869.57 | 0.00 | 0.0000 |
| breakeven_91 | Breakeven 91 | 92.31 | -7.69% | 769.23 | 0.00 | 0.0000 |
| breakeven_92 | Breakeven 92 | 93.31 | -6.69% | 668.90 | 0.00 | 0.0000 |
| breakeven_93 | Breakeven 93 | 94.31 | -5.69% | 568.56 | 0.00 | 0.0000 |
| breakeven_94 | Breakeven 94 | 95.32 | -4.68% | 468.23 | 0.00 | 0.0000 |
| breakeven_95 | Breakeven 95 | 96.32 | -3.68% | 367.89 | 0.00 | 0.0000 |
| breakeven_96 | Breakeven 96 | 97.32 | -2.68% | 267.56 | 0.00 | 0.0000 |
| breakeven_97 | Breakeven 97 | 98.33 | -1.67% | 167.22 | 0.00 | 0.0000 |
| breakeven_98 | Breakeven 98 | 99.33 | -0.67% | 66.89 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_99 | Breakeven 99 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_100 | Breakeven 100 | 100.33 | 0.33% | -33.44 | 0.00 | 0.0000 |
| breakeven_101 | Breakeven 101 | 101.34 | 1.34% | -133.78 | 0.00 | 0.0000 |
| breakeven_102 | Breakeven 102 | 102.34 | 2.34% | -234.11 | 0.00 | 0.0000 |
| breakeven_103 | Breakeven 103 | 103.34 | 3.34% | -334.45 | 0.00 | 0.0000 |
| breakeven_104 | Breakeven 104 | 104.35 | 4.35% | -434.78 | 0.00 | 0.0000 |
| breakeven_105 | Breakeven 105 | 105.35 | 5.35% | -535.12 | 0.00 | 0.0000 |
| breakeven_106 | Breakeven 106 | 106.35 | 6.35% | -635.45 | 0.00 | 0.0000 |
| breakeven_107 | Breakeven 107 | 107.36 | 7.36% | -735.79 | 0.00 | 0.0000 |
| breakeven_108 | Breakeven 108 | 108.36 | 8.36% | -836.12 | 0.00 | 0.0000 |
| breakeven_109 | Breakeven 109 | 109.36 | 9.36% | -936.45 | 0.00 | 0.0000 |
| breakeven_110 | Breakeven 110 | 110.37 | 10.37% | -1036.79 | 0.00 | 0.0000 |
| breakeven_111 | Breakeven 111 | 111.37 | 11.37% | -1137.12 | 0.00 | 0.0000 |
| breakeven_112 | Breakeven 112 | 112.37 | 12.37% | -1237.46 | 0.00 | 0.0000 |
| breakeven_113 | Breakeven 113 | 113.38 | 13.38% | -1337.79 | 0.00 | 0.0000 |
| breakeven_114 | Breakeven 114 | 114.38 | 14.38% | -1438.13 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1500.00 | 0.00 | 0.0000 |
| breakeven_115 | Breakeven 115 | 115.38 | 15.38% | -1538.46 | 0.00 | 0.0000 |
| breakeven_116 | Breakeven 116 | 116.39 | 16.39% | -1638.80 | 0.00 | 0.0000 |
| breakeven_117 | Breakeven 117 | 117.39 | 17.39% | -1739.13 | 0.00 | 0.0000 |
| breakeven_118 | Breakeven 118 | 118.39 | 18.39% | -1839.46 | 0.00 | 0.0000 |
| breakeven_119 | Breakeven 119 | 119.40 | 19.40% | -1939.80 | 0.00 | 0.0000 |
| breakeven_120 | Breakeven 120 | 120.40 | 20.40% | -2040.13 | 0.00 | 0.0000 |
| breakeven_121 | Breakeven 121 | 122.41 | 22.41% | -2240.80 | 0.00 | 0.0000 |
| breakeven_122 | Breakeven 122 | 123.41 | 23.41% | -2341.14 | 0.00 | 0.0000 |
| breakeven_123 | Breakeven 123 | 124.41 | 24.41% | -2441.47 | 0.00 | 0.0000 |
| breakeven_124 | Breakeven 124 | 125.42 | 25.42% | -2541.81 | 0.00 | 0.0000 |
| breakeven_125 | Breakeven 125 | 126.42 | 26.42% | -2642.14 | 0.00 | 0.0000 |
| breakeven_126 | Breakeven 126 | 127.42 | 27.42% | -2742.47 | 0.00 | 0.0000 |
| breakeven_127 | Breakeven 127 | 128.43 | 28.43% | -2842.81 | 0.00 | 0.0000 |
| breakeven_128 | Breakeven 128 | 129.43 | 29.43% | -2943.14 | 0.00 | 0.0000 |
| breakeven_129 | Breakeven 129 | 130.43 | 30.43% | -3043.48 | 0.00 | 0.0000 |
| breakeven_130 | Breakeven 130 | 131.44 | 31.44% | -3143.81 | 0.00 | 0.0000 |
| breakeven_131 | Breakeven 131 | 132.44 | 32.44% | -3244.15 | 0.00 | 0.0000 |
| breakeven_132 | Breakeven 132 | 133.44 | 33.44% | -3344.48 | 0.00 | 0.0000 |
| breakeven_133 | Breakeven 133 | 134.45 | 34.45% | -3444.82 | 0.00 | 0.0000 |
| breakeven_134 | Breakeven 134 | 135.45 | 35.45% | -3545.15 | 0.00 | 0.0000 |
| breakeven_135 | Breakeven 135 | 136.45 | 36.45% | -3645.48 | 0.00 | 0.0000 |
| breakeven_136 | Breakeven 136 | 137.46 | 37.46% | -3745.82 | 0.00 | 0.0000 |
| breakeven_137 | Breakeven 137 | 138.46 | 38.46% | -3846.15 | 0.00 | 0.0000 |
| breakeven_138 | Breakeven 138 | 139.46 | 39.46% | -3946.49 | 0.00 | 0.0000 |
| breakeven_139 | Breakeven 139 | 140.47 | 40.47% | -4046.82 | 0.00 | 0.0000 |
| breakeven_140 | Breakeven 140 | 141.47 | 41.47% | -4147.16 | 0.00 | 0.0000 |
| breakeven_141 | Breakeven 141 | 142.47 | 42.47% | -4247.49 | 0.00 | 0.0000 |
| breakeven_142 | Breakeven 142 | 143.48 | 43.48% | -4347.83 | 0.00 | 0.0000 |
| breakeven_143 | Breakeven 143 | 144.48 | 44.48% | -4448.16 | 0.00 | 0.0000 |
| breakeven_144 | Breakeven 144 | 145.48 | 45.48% | -4548.49 | 0.00 | 0.0000 |
| breakeven_145 | Breakeven 145 | 146.49 | 46.49% | -4648.83 | 0.00 | 0.0000 |
| breakeven_146 | Breakeven 146 | 147.49 | 47.49% | -4749.16 | 0.00 | 0.0000 |
| breakeven_147 | Breakeven 147 | 148.49 | 48.49% | -4849.50 | 0.00 | 0.0000 |
| breakeven_148 | Breakeven 148 | 149.50 | 49.50% | -4949.83 | 0.00 | 0.0000 |
| breakeven_149 | Breakeven 149 | 150.50 | 50.50% | -5050.17 | 0.00 | 0.0000 |
| breakeven_150 | Breakeven 150 | 151.51 | 51.51% | -5150.50 | 0.00 | 0.0000 |
| breakeven_151 | Breakeven 151 | 152.51 | 52.51% | -5250.84 | 0.00 | 0.0000 |
| breakeven_152 | Breakeven 152 | 153.51 | 53.51% | -5351.17 | 0.00 | 0.0000 |
| breakeven_153 | Breakeven 153 | 154.52 | 54.52% | -5451.51 | 0.00 | 0.0000 |
| breakeven_154 | Breakeven 154 | 155.52 | 55.52% | -5551.84 | 0.00 | 0.0000 |
| breakeven_155 | Breakeven 155 | 156.52 | 56.52% | -5652.17 | 0.00 | 0.0000 |
| breakeven_156 | Breakeven 156 | 157.53 | 57.53% | -5752.51 | 0.00 | 0.0000 |
| breakeven_157 | Breakeven 157 | 158.53 | 58.53% | -5852.84 | 0.00 | 0.0000 |
| breakeven_158 | Breakeven 158 | 159.53 | 59.53% | -5953.18 | 0.00 | 0.0000 |
| breakeven_159 | Breakeven 159 | 160.54 | 60.54% | -6053.51 | 0.00 | 0.0000 |
| breakeven_160 | Breakeven 160 | 161.54 | 61.54% | -6153.85 | 0.00 | 0.0000 |
| breakeven_161 | Breakeven 161 | 162.54 | 62.54% | -6254.18 | 0.00 | 0.0000 |
| breakeven_162 | Breakeven 162 | 163.55 | 63.55% | -6354.52 | 0.00 | 0.0000 |
| breakeven_163 | Breakeven 163 | 164.55 | 64.55% | -6454.85 | 0.00 | 0.0000 |
| breakeven_164 | Breakeven 164 | 165.55 | 65.55% | -6555.18 | 0.00 | 0.0000 |
| breakeven_165 | Breakeven 165 | 166.56 | 66.56% | -6655.52 | 0.00 | 0.0000 |
| breakeven_166 | Breakeven 166 | 167.56 | 67.56% | -6755.85 | 0.00 | 0.0000 |
| breakeven_167 | Breakeven 167 | 168.56 | 68.56% | -6856.19 | 0.00 | 0.0000 |
| breakeven_168 | Breakeven 168 | 169.57 | 69.57% | -6956.52 | 0.00 | 0.0000 |
| breakeven_169 | Breakeven 169 | 170.57 | 70.57% | -7056.86 | 0.00 | 0.0000 |
| breakeven_170 | Breakeven 170 | 171.57 | 71.57% | -7157.19 | 0.00 | 0.0000 |
| breakeven_171 | Breakeven 171 | 172.58 | 72.58% | -7257.53 | 0.00 | 0.0000 |
| breakeven_172 | Breakeven 172 | 173.58 | 73.58% | -7357.86 | 0.00 | 0.0000 |
| breakeven_173 | Breakeven 173 | 174.58 | 74.58% | -7458.19 | 0.00 | 0.0000 |
| breakeven_174 | Breakeven 174 | 175.59 | 75.59% | -7558.53 | 0.00 | 0.0000 |
| breakeven_175 | Breakeven 175 | 176.59 | 76.59% | -7658.86 | 0.00 | 0.0000 |
| breakeven_176 | Breakeven 176 | 177.59 | 77.59% | -7759.20 | 0.00 | 0.0000 |
| breakeven_177 | Breakeven 177 | 178.60 | 78.60% | -7859.53 | 0.00 | 0.0000 |
| breakeven_178 | Breakeven 178 | 179.60 | 79.60% | -7959.87 | 0.00 | 0.0000 |
| breakeven_179 | Breakeven 179 | 180.60 | 80.60% | -8060.20 | 0.00 | 0.0000 |
| breakeven_180 | Breakeven 180 | 181.61 | 81.61% | -8160.54 | 0.00 | 0.0000 |
| breakeven_181 | Breakeven 181 | 183.61 | 83.61% | -8361.20 | 0.00 | 0.0000 |
| breakeven_182 | Breakeven 182 | 184.62 | 84.62% | -8461.54 | 0.00 | 0.0000 |
| breakeven_183 | Breakeven 183 | 185.62 | 85.62% | -8561.87 | 0.00 | 0.0000 |
| breakeven_184 | Breakeven 184 | 186.62 | 86.62% | -8662.21 | 0.00 | 0.0000 |
| breakeven_185 | Breakeven 185 | 187.63 | 87.63% | -8762.54 | 0.00 | 0.0000 |
| breakeven_186 | Breakeven 186 | 188.63 | 88.63% | -8862.88 | 0.00 | 0.0000 |
| breakeven_187 | Breakeven 187 | 189.63 | 89.63% | -8963.21 | 0.00 | 0.0000 |
| breakeven_188 | Breakeven 188 | 190.64 | 90.64% | -9063.55 | 0.00 | 0.0000 |
| breakeven_189 | Breakeven 189 | 191.64 | 91.64% | -9163.88 | 0.00 | 0.0000 |
| breakeven_190 | Breakeven 190 | 192.64 | 92.64% | -9264.21 | 0.00 | 0.0000 |
| breakeven_191 | Breakeven 191 | 193.65 | 93.65% | -9364.55 | 0.00 | 0.0000 |
| breakeven_192 | Breakeven 192 | 194.65 | 94.65% | -9464.88 | 0.00 | 0.0000 |
| breakeven_193 | Breakeven 193 | 195.65 | 95.65% | -9565.22 | 0.00 | 0.0000 |
| breakeven_194 | Breakeven 194 | 196.66 | 96.66% | -9665.55 | 0.00 | 0.0000 |
| breakeven_195 | Breakeven 195 | 197.66 | 97.66% | -9765.89 | 0.00 | 0.0000 |
| breakeven_196 | Breakeven 196 | 198.66 | 98.66% | -9866.22 | 0.00 | 0.0000 |
| breakeven_197 | Breakeven 197 | 199.67 | 99.67% | -9966.56 | 0.00 | 0.0000 |
| breakeven_198 | Breakeven 198 | 200.67 | 100.67% | -10066.89 | 0.00 | 0.0000 |
| breakeven_199 | Breakeven 199 | 201.67 | 101.67% | -10167.22 | 0.00 | 0.0000 |
| breakeven_200 | Breakeven 200 | 202.68 | 102.68% | -10267.56 | 0.00 | 0.0000 |
| breakeven_201 | Breakeven 201 | 203.68 | 103.68% | -10367.89 | 0.00 | 0.0000 |
| breakeven_202 | Breakeven 202 | 204.68 | 104.68% | -10468.23 | 0.00 | 0.0000 |
| breakeven_203 | Breakeven 203 | 205.69 | 105.69% | -10568.56 | 0.00 | 0.0000 |
| breakeven_204 | Breakeven 204 | 206.69 | 106.69% | -10668.90 | 0.00 | 0.0000 |
| breakeven_205 | Breakeven 205 | 207.69 | 107.69% | -10769.23 | 0.00 | 0.0000 |
| breakeven_206 | Breakeven 206 | 208.70 | 108.70% | -10869.57 | 0.00 | 0.0000 |
| breakeven_207 | Breakeven 207 | 209.70 | 109.70% | -10969.90 | 0.00 | 0.0000 |
| breakeven_208 | Breakeven 208 | 210.70 | 110.70% | -11070.23 | 0.00 | 0.0000 |
| breakeven_209 | Breakeven 209 | 211.71 | 111.71% | -11170.57 | 0.00 | 0.0000 |
| breakeven_210 | Breakeven 210 | 212.71 | 112.71% | -11270.90 | 0.00 | 0.0000 |
| breakeven_211 | Breakeven 211 | 213.71 | 113.71% | -11371.24 | 0.00 | 0.0000 |
| breakeven_212 | Breakeven 212 | 214.72 | 114.72% | -11471.57 | 0.00 | 0.0000 |
| breakeven_213 | Breakeven 213 | 215.72 | 115.72% | -11571.91 | 0.00 | 0.0000 |
| breakeven_214 | Breakeven 214 | 216.72 | 116.72% | -11672.24 | 0.00 | 0.0000 |
| breakeven_215 | Breakeven 215 | 217.73 | 117.73% | -11772.58 | 0.00 | 0.0000 |
| breakeven_216 | Breakeven 216 | 218.73 | 118.73% | -11872.91 | 0.00 | 0.0000 |
| breakeven_217 | Breakeven 217 | 219.73 | 119.73% | -11973.24 | 0.00 | 0.0000 |
| breakeven_218 | Breakeven 218 | 220.74 | 120.74% | -12073.58 | 0.00 | 0.0000 |
| breakeven_219 | Breakeven 219 | 221.74 | 121.74% | -12173.91 | 0.00 | 0.0000 |
| breakeven_220 | Breakeven 220 | 222.74 | 122.74% | -12274.25 | 0.00 | 0.0000 |
| breakeven_221 | Breakeven 221 | 223.75 | 123.75% | -12374.58 | 0.00 | 0.0000 |
| breakeven_222 | Breakeven 222 | 224.75 | 124.75% | -12474.92 | 0.00 | 0.0000 |
| breakeven_223 | Breakeven 223 | 225.75 | 125.75% | -12575.25 | 0.00 | 0.0000 |
| breakeven_224 | Breakeven 224 | 226.76 | 126.76% | -12675.59 | 0.00 | 0.0000 |
| breakeven_225 | Breakeven 225 | 227.76 | 127.76% | -12775.92 | 0.00 | 0.0000 |
| breakeven_226 | Breakeven 226 | 228.76 | 128.76% | -12876.25 | 0.00 | 0.0000 |
| breakeven_227 | Breakeven 227 | 229.77 | 129.77% | -12976.59 | 0.00 | 0.0000 |
| breakeven_228 | Breakeven 228 | 230.77 | 130.77% | -13076.92 | 0.00 | 0.0000 |
| breakeven_229 | Breakeven 229 | 231.77 | 131.77% | -13177.26 | 0.00 | 0.0000 |
| breakeven_230 | Breakeven 230 | 232.78 | 132.78% | -13277.59 | 0.00 | 0.0000 |
| breakeven_231 | Breakeven 231 | 233.78 | 133.78% | -13377.93 | 0.00 | 0.0000 |
| breakeven_232 | Breakeven 232 | 234.78 | 134.78% | -13478.26 | 0.00 | 0.0000 |
| breakeven_233 | Breakeven 233 | 235.79 | 135.79% | -13578.60 | 0.00 | 0.0000 |
| breakeven_234 | Breakeven 234 | 236.79 | 136.79% | -13678.93 | 0.00 | 0.0000 |
| breakeven_235 | Breakeven 235 | 237.79 | 137.79% | -13779.26 | 0.00 | 0.0000 |
| breakeven_236 | Breakeven 236 | 238.80 | 138.80% | -13879.60 | 0.00 | 0.0000 |
| breakeven_237 | Breakeven 237 | 239.80 | 139.80% | -13979.93 | 0.00 | 0.0000 |
| breakeven_238 | Breakeven 238 | 240.80 | 140.80% | -14080.27 | 0.00 | 0.0000 |
| breakeven_239 | Breakeven 239 | 241.81 | 141.81% | -14180.60 | 0.00 | 0.0000 |
| breakeven_240 | Breakeven 240 | 242.81 | 142.81% | -14280.94 | 0.00 | 0.0000 |
| breakeven_241 | Breakeven 241 | 243.81 | 143.81% | -14381.27 | 0.00 | 0.0000 |
| breakeven_242 | Breakeven 242 | 244.82 | 144.82% | -14481.61 | 0.00 | 0.0000 |
| breakeven_243 | Breakeven 243 | 245.82 | 145.82% | -14581.94 | 0.00 | 0.0000 |
| breakeven_244 | Breakeven 244 | 246.82 | 146.82% | -14682.27 | 0.00 | 0.0000 |
| breakeven_245 | Breakeven 245 | 247.83 | 147.83% | -14782.61 | 0.00 | 0.0000 |
| breakeven_246 | Breakeven 246 | 248.83 | 148.83% | -14882.94 | 0.00 | 0.0000 |
| breakeven_247 | Breakeven 247 | 249.83 | 149.83% | -14983.28 | 0.00 | 0.0000 |
| breakeven_248 | Breakeven 248 | 250.84 | 150.84% | -15083.61 | 0.00 | 0.0000 |
| breakeven_249 | Breakeven 249 | 251.84 | 151.84% | -15183.95 | 0.00 | 0.0000 |
| breakeven_250 | Breakeven 250 | 252.84 | 152.84% | -15284.28 | 0.00 | 0.0000 |
| breakeven_251 | Breakeven 251 | 253.85 | 153.85% | -15384.62 | 0.00 | 0.0000 |
| breakeven_252 | Breakeven 252 | 254.85 | 154.85% | -15484.95 | 0.00 | 0.0000 |
| breakeven_253 | Breakeven 253 | 255.85 | 155.85% | -15585.28 | 0.00 | 0.0000 |
| breakeven_254 | Breakeven 254 | 256.86 | 156.86% | -15685.62 | 0.00 | 0.0000 |
| breakeven_255 | Breakeven 255 | 257.86 | 157.86% | -15785.95 | 0.00 | 0.0000 |
| breakeven_256 | Breakeven 256 | 258.86 | 158.86% | -15886.29 | 0.00 | 0.0000 |
| breakeven_257 | Breakeven 257 | 259.87 | 159.87% | -15986.62 | 0.00 | 0.0000 |
| breakeven_258 | Breakeven 258 | 260.87 | 160.87% | -16086.96 | 0.00 | 0.0000 |
| breakeven_259 | Breakeven 259 | 261.87 | 161.87% | -16187.29 | 0.00 | 0.0000 |
| breakeven_260 | Breakeven 260 | 262.88 | 162.88% | -16287.63 | 0.00 | 0.0000 |
| breakeven_261 | Breakeven 261 | 263.88 | 163.88% | -16387.96 | 0.00 | 0.0000 |
| breakeven_262 | Breakeven 262 | 264.88 | 164.88% | -16488.29 | 0.00 | 0.0000 |
| breakeven_263 | Breakeven 263 | 265.89 | 165.89% | -16588.63 | 0.00 | 0.0000 |
| breakeven_264 | Breakeven 264 | 266.89 | 166.89% | -16688.96 | 0.00 | 0.0000 |
| breakeven_265 | Breakeven 265 | 267.89 | 167.89% | -16789.30 | 0.00 | 0.0000 |
| breakeven_266 | Breakeven 266 | 268.90 | 168.90% | -16889.63 | 0.00 | 0.0000 |
| breakeven_267 | Breakeven 267 | 269.90 | 169.90% | -16989.97 | 0.00 | 0.0000 |
| breakeven_268 | Breakeven 268 | 270.90 | 170.90% | -17090.30 | 0.00 | 0.0000 |
| breakeven_269 | Breakeven 269 | 271.91 | 171.91% | -17190.64 | 0.00 | 0.0000 |
| breakeven_270 | Breakeven 270 | 272.91 | 172.91% | -17290.97 | 0.00 | 0.0000 |
| breakeven_271 | Breakeven 271 | 273.91 | 173.91% | -17391.30 | 0.00 | 0.0000 |
| breakeven_272 | Breakeven 272 | 274.92 | 174.92% | -17491.64 | 0.00 | 0.0000 |
| breakeven_273 | Breakeven 273 | 275.92 | 175.92% | -17591.97 | 0.00 | 0.0000 |
| breakeven_274 | Breakeven 274 | 276.92 | 176.92% | -17692.31 | 0.00 | 0.0000 |
| breakeven_275 | Breakeven 275 | 277.93 | 177.93% | -17792.64 | 0.00 | 0.0000 |
| breakeven_276 | Breakeven 276 | 278.93 | 178.93% | -17892.98 | 0.00 | 0.0000 |
| breakeven_277 | Breakeven 277 | 279.93 | 179.93% | -17993.31 | 0.00 | 0.0000 |
| breakeven_278 | Breakeven 278 | 280.94 | 180.94% | -18093.65 | 0.00 | 0.0000 |
| breakeven_279 | Breakeven 279 | 281.94 | 181.94% | -18193.98 | 0.00 | 0.0000 |
| breakeven_280 | Breakeven 280 | 282.94 | 182.94% | -18294.31 | 0.00 | 0.0000 |
| breakeven_281 | Breakeven 281 | 283.95 | 183.95% | -18394.65 | 0.00 | 0.0000 |
| breakeven_282 | Breakeven 282 | 284.95 | 184.95% | -18494.98 | 0.00 | 0.0000 |
| breakeven_283 | Breakeven 283 | 285.95 | 185.95% | -18595.32 | 0.00 | 0.0000 |
| breakeven_284 | Breakeven 284 | 286.96 | 186.96% | -18695.65 | 0.00 | 0.0000 |
| breakeven_285 | Breakeven 285 | 287.96 | 187.96% | -18795.99 | 0.00 | 0.0000 |
| breakeven_286 | Breakeven 286 | 288.96 | 188.96% | -18896.32 | 0.00 | 0.0000 |
| breakeven_287 | Breakeven 287 | 289.97 | 189.97% | -18996.66 | 0.00 | 0.0000 |
| breakeven_288 | Breakeven 288 | 290.97 | 190.97% | -19096.99 | 0.00 | 0.0000 |
| breakeven_289 | Breakeven 289 | 291.97 | 191.97% | -19197.32 | 0.00 | 0.0000 |
| breakeven_290 | Breakeven 290 | 292.98 | 192.98% | -19297.66 | 0.00 | 0.0000 |
| breakeven_291 | Breakeven 291 | 293.98 | 193.98% | -19397.99 | 0.00 | 0.0000 |
| breakeven_292 | Breakeven 292 | 294.98 | 194.98% | -19498.33 | 0.00 | 0.0000 |
| breakeven_293 | Breakeven 293 | 295.99 | 195.99% | -19598.66 | 0.00 | 0.0000 |
| breakeven_294 | Breakeven 294 | 296.99 | 196.99% | -19699.00 | 0.00 | 0.0000 |
| breakeven_295 | Breakeven 295 | 297.99 | 197.99% | -19799.33 | 0.00 | 0.0000 |
| breakeven_296 | Breakeven 296 | 299.00 | 199.00% | -19899.67 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | 0.00 | 0.0000 |

---

### Conversion (ID=63) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: COL_EQ
- Margin Classification: COL_EQ

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: [0.0, 1.003344, 2.006689, 3.010033, 4.013378, 5.016722, 6.020067, 7.023411, 8.026756, 9.0301, 10.033445, 11.036789, 12.040134, 13.043478, 14.046823, 15.050167, 17.056856, 18.060201, 19.063545, 20.06689, 21.070234, 22.073579, 23.076923, 24.080268, 25.083612, 26.086957, 27.090301, 28.093645, 29.09699, 30.100334, 31.103679, 32.107023, 33.110368, 34.113712, 35.117057, 36.120401, 37.123746, 38.12709, 39.130435, 40.133779, 41.137124, 42.140468, 43.143813, 44.147157, 45.150502, 46.153846, 47.157191, 48.160535, 49.16388, 50.167224, 51.170569, 52.173913, 53.177258, 54.180602, 55.183946, 56.187291, 58.19398, 59.197324, 60.200669, 61.204013, 62.207358, 63.210702, 64.214047, 65.217391, 66.220736, 67.22408, 68.227425, 69.230769, 70.234114, 71.237458, 72.240803, 73.244147, 74.247492, 75.250836, 76.254181, 77.257525, 78.26087, 79.264214, 80.267559, 81.270903, 82.274247, 83.277592, 84.280936, 85.284281, 86.287625, 87.29097, 88.294314, 89.297659, 90.301003, 91.304348, 92.307692, 93.311037, 94.314381, 95.317726, 96.32107, 97.324415, 98.327759, 99.331104, 100.0, 100.334448, 101.337793, 102.341137, 103.344482, 104.347826, 105.351171, 106.354515, 107.35786, 108.361204, 109.364548, 110.367893, 111.371237, 112.374582, 113.377926, 114.381271, 115.384615, 116.38796, 117.391304, 118.394649, 119.397993, 120.401338, 122.408027, 123.411371, 124.414716, 125.41806, 126.421405, 127.424749, 128.428094, 129.431438, 130.434783, 131.438127, 132.441472, 133.444816, 134.448161, 135.451505, 136.454849, 137.458194, 138.461538, 139.464883, 140.468227, 141.471572, 142.474916, 143.478261, 144.481605, 145.48495, 146.488294, 147.491639, 148.494983, 149.498328, 150.501672, 151.505017, 152.508361, 153.511706, 154.51505, 155.518395, 156.521739, 157.525084, 158.528428, 159.531773, 160.535117, 161.538462, 162.541806, 163.545151, 164.548495, 165.551839, 166.555184, 167.558528, 168.561873, 169.565217, 170.568562, 171.571906, 172.575251, 173.578595, 174.58194, 175.585284, 176.588629, 177.591973, 178.595318, 179.598662, 180.602007, 181.605351, 183.61204, 184.615385, 185.618729, 186.622074, 187.625418, 188.628763, 189.632107, 190.635452, 191.638796, 192.64214, 193.645485, 194.648829, 195.652174, 196.655518, 197.658863, 198.662207, 199.665552, 200.668896, 201.672241, 202.675585, 203.67893, 204.682274, 205.685619, 206.688963, 207.692308, 208.695652, 209.698997, 210.702341, 211.705686, 212.70903, 213.712375, 214.715719, 215.719064, 216.722408, 217.725753, 218.729097, 219.732441, 220.735786, 221.73913, 222.742475, 223.745819, 224.749164, 225.752508, 226.755853, 227.759197, 228.762542, 229.765886, 230.769231, 231.772575, 232.77592, 233.779264, 234.782609, 235.785953, 236.789298, 237.792642, 238.795987, 239.799331, 240.802676, 241.80602, 242.809365, 243.812709, 244.816054, 245.819398, 246.822742, 247.826087, 248.829431, 249.832776, 250.83612, 251.839465, 252.842809, 253.846154, 254.849498, 255.852843, 256.856187, 257.859532, 258.862876, 259.866221, 260.869565, 261.87291, 262.876254, 263.879599, 264.882943, 265.886288, 266.889632, 267.892977, 268.896321, 269.899666, 270.90301, 271.906355, 272.909699, 273.913043, 274.916388, 275.919732, 276.923077, 277.926421, 278.929766, 279.93311, 280.936455, 281.939799, 282.943144, 283.946488, 284.949833, 285.953177, 286.956522, 287.959866, 288.963211, 289.966555, 290.9699, 291.973244, 292.976589, 293.979933, 294.983278, 295.986622, 296.989967, 297.993311, 298.996656]
- Options Max PnL: 10000.0
- Options Min PnL: -20000.0
- Combined Max PnL: 0.0
- Combined Min PnL: -0.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $10,000.00 | $0.00 |
| Max Loss | Unlimited | -$0.00 |
| Risk Reward | 0.50x | 0.25x |
| Capital Basis | $5,250.00 | $15,250.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 5250.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.003285
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 0.00 | Breakeven 1 | 10000.00 | -10000.00 | 0.00 | 1.9048 | 0.0000 |
| 1.00 | Breakeven 2 | 9899.67 | -9899.67 | 0.00 | 1.8857 | 0.0000 |
| 2.01 | Breakeven 3 | 9799.33 | -9799.33 | 0.00 | 1.8665 | 0.0000 |
| 3.01 | Breakeven 4 | 9699.00 | -9699.00 | 0.00 | 1.8474 | 0.0000 |
| 4.01 | Breakeven 5 | 9598.66 | -9598.66 | 0.00 | 1.8283 | 0.0000 |
| 5.02 | Breakeven 6 | 9498.33 | -9498.33 | 0.00 | 1.8092 | 0.0000 |
| 6.02 | Breakeven 7 | 9397.99 | -9397.99 | 0.00 | 1.7901 | 0.0000 |
| 7.02 | Breakeven 8 | 9297.66 | -9297.66 | 0.00 | 1.7710 | 0.0000 |
| 8.03 | Breakeven 9 | 9197.32 | -9197.32 | 0.00 | 1.7519 | 0.0000 |
| 9.03 | Breakeven 10 | 9096.99 | -9096.99 | 0.00 | 1.7328 | 0.0000 |
| 10.03 | Breakeven 11 | 8996.66 | -8996.66 | 0.00 | 1.7136 | 0.0000 |
| 11.04 | Breakeven 12 | 8896.32 | -8896.32 | 0.00 | 1.6945 | 0.0000 |
| 12.04 | Breakeven 13 | 8795.99 | -8795.99 | 0.00 | 1.6754 | 0.0000 |
| 13.04 | Breakeven 14 | 8695.65 | -8695.65 | 0.00 | 1.6563 | 0.0000 |
| 14.05 | Breakeven 15 | 8595.32 | -8595.32 | 0.00 | 1.6372 | 0.0000 |
| 15.05 | Breakeven 16 | 8494.98 | -8494.98 | 0.00 | 1.6181 | 0.0000 |
| 17.06 | Breakeven 17 | 8294.31 | -8294.31 | 0.00 | 1.5799 | 0.0000 |
| 18.06 | Breakeven 18 | 8193.98 | -8193.98 | -0.00 | 1.5608 | -0.0000 |
| 19.06 | Breakeven 19 | 8093.65 | -8093.65 | 0.00 | 1.5416 | 0.0000 |
| 20.07 | Breakeven 20 | 7993.31 | -7993.31 | 0.00 | 1.5225 | 0.0000 |
| 21.07 | Breakeven 21 | 7892.98 | -7892.98 | 0.00 | 1.5034 | 0.0000 |
| 22.07 | Breakeven 22 | 7792.64 | -7792.64 | 0.00 | 1.4843 | 0.0000 |
| 23.08 | Breakeven 23 | 7692.31 | -7692.31 | 0.00 | 1.4652 | 0.0000 |
| 24.08 | Breakeven 24 | 7591.97 | -7591.97 | 0.00 | 1.4461 | 0.0000 |
| 25.08 | Breakeven 25 | 7491.64 | -7491.64 | 0.00 | 1.4270 | 0.0000 |
| 26.09 | Breakeven 26 | 7391.30 | -7391.30 | 0.00 | 1.4079 | 0.0000 |
| 27.09 | Breakeven 27 | 7290.97 | -7290.97 | 0.00 | 1.3888 | 0.0000 |
| 28.09 | Breakeven 28 | 7190.64 | -7190.64 | 0.00 | 1.3696 | 0.0000 |
| 29.10 | Breakeven 29 | 7090.30 | -7090.30 | 0.00 | 1.3505 | 0.0000 |
| 30.10 | Breakeven 30 | 6989.97 | -6989.97 | 0.00 | 1.3314 | 0.0000 |
| 31.10 | Breakeven 31 | 6889.63 | -6889.63 | 0.00 | 1.3123 | 0.0000 |
| 32.11 | Breakeven 32 | 6789.30 | -6789.30 | 0.00 | 1.2932 | 0.0000 |
| 33.11 | Breakeven 33 | 6688.96 | -6688.96 | 0.00 | 1.2741 | 0.0000 |
| 34.11 | Breakeven 34 | 6588.63 | -6588.63 | 0.00 | 1.2550 | 0.0000 |
| 35.12 | Breakeven 35 | 6488.29 | -6488.29 | 0.00 | 1.2359 | 0.0000 |
| 36.12 | Breakeven 36 | 6387.96 | -6387.96 | 0.00 | 1.2168 | 0.0000 |
| 37.12 | Breakeven 37 | 6287.63 | -6287.63 | 0.00 | 1.1976 | 0.0000 |
| 38.13 | Breakeven 38 | 6187.29 | -6187.29 | 0.00 | 1.1785 | 0.0000 |
| 39.13 | Breakeven 39 | 6086.96 | -6086.96 | 0.00 | 1.1594 | 0.0000 |
| 40.13 | Breakeven 40 | 5986.62 | -5986.62 | 0.00 | 1.1403 | 0.0000 |
| 41.14 | Breakeven 41 | 5886.29 | -5886.29 | 0.00 | 1.1212 | 0.0000 |
| 42.14 | Breakeven 42 | 5785.95 | -5785.95 | 0.00 | 1.1021 | 0.0000 |
| 43.14 | Breakeven 43 | 5685.62 | -5685.62 | 0.00 | 1.0830 | 0.0000 |
| 44.15 | Breakeven 44 | 5585.28 | -5585.28 | 0.00 | 1.0639 | 0.0000 |
| 45.15 | Breakeven 45 | 5484.95 | -5484.95 | 0.00 | 1.0448 | 0.0000 |
| 46.15 | Breakeven 46 | 5384.62 | -5384.62 | 0.00 | 1.0256 | 0.0000 |
| 47.16 | Breakeven 47 | 5284.28 | -5284.28 | 0.00 | 1.0065 | 0.0000 |
| 48.16 | Breakeven 48 | 5183.95 | -5183.95 | 0.00 | 0.9874 | 0.0000 |
| 49.16 | Breakeven 49 | 5083.61 | -5083.61 | 0.00 | 0.9683 | 0.0000 |
| 50.17 | Breakeven 50 | 4983.28 | -4983.28 | 0.00 | 0.9492 | 0.0000 |
| 51.17 | Breakeven 51 | 4882.94 | -4882.94 | 0.00 | 0.9301 | 0.0000 |
| 52.17 | Breakeven 52 | 4782.61 | -4782.61 | 0.00 | 0.9110 | 0.0000 |
| 53.18 | Breakeven 53 | 4682.27 | -4682.27 | 0.00 | 0.8919 | 0.0000 |
| 54.18 | Breakeven 54 | 4581.94 | -4581.94 | 0.00 | 0.8728 | 0.0000 |
| 55.18 | Breakeven 55 | 4481.61 | -4481.61 | 0.00 | 0.8536 | 0.0000 |
| 56.19 | Breakeven 56 | 4381.27 | -4381.27 | 0.00 | 0.8345 | 0.0000 |
| 58.19 | Breakeven 57 | 4180.60 | -4180.60 | 0.00 | 0.7963 | 0.0000 |
| 59.20 | Breakeven 58 | 4080.27 | -4080.27 | 0.00 | 0.7772 | 0.0000 |
| 60.20 | Breakeven 59 | 3979.93 | -3979.93 | 0.00 | 0.7581 | 0.0000 |
| 61.20 | Breakeven 60 | 3879.60 | -3879.60 | 0.00 | 0.7390 | 0.0000 |
| 62.21 | Breakeven 61 | 3779.26 | -3779.26 | 0.00 | 0.7199 | 0.0000 |
| 63.21 | Breakeven 62 | 3678.93 | -3678.93 | 0.00 | 0.7007 | 0.0000 |
| 64.21 | Breakeven 63 | 3578.60 | -3578.60 | 0.00 | 0.6816 | 0.0000 |
| 65.22 | Breakeven 64 | 3478.26 | -3478.26 | 0.00 | 0.6625 | 0.0000 |
| 66.22 | Breakeven 65 | 3377.93 | -3377.93 | 0.00 | 0.6434 | 0.0000 |
| 67.22 | Breakeven 66 | 3277.59 | -3277.59 | 0.00 | 0.6243 | 0.0000 |
| 68.23 | Breakeven 67 | 3177.26 | -3177.26 | 0.00 | 0.6052 | 0.0000 |
| 69.23 | Breakeven 68 | 3076.92 | -3076.92 | 0.00 | 0.5861 | 0.0000 |
| 70.23 | Breakeven 69 | 2976.59 | -2976.59 | 0.00 | 0.5670 | 0.0000 |
| 71.24 | Breakeven 70 | 2876.25 | -2876.25 | 0.00 | 0.5479 | 0.0000 |
| 72.24 | Breakeven 71 | 2775.92 | -2775.92 | 0.00 | 0.5287 | 0.0000 |
| 73.24 | Breakeven 72 | 2675.59 | -2675.59 | 0.00 | 0.5096 | 0.0000 |
| 74.25 | Breakeven 73 | 2575.25 | -2575.25 | 0.00 | 0.4905 | 0.0000 |
| 75.25 | Breakeven 74 | 2474.92 | -2474.92 | 0.00 | 0.4714 | 0.0000 |
| 76.25 | Breakeven 75 | 2374.58 | -2374.58 | 0.00 | 0.4523 | 0.0000 |
| 77.26 | Breakeven 76 | 2274.25 | -2274.25 | 0.00 | 0.4332 | 0.0000 |
| 78.26 | Breakeven 77 | 2173.91 | -2173.91 | 0.00 | 0.4141 | 0.0000 |
| 79.26 | Breakeven 78 | 2073.58 | -2073.58 | -0.00 | 0.3950 | -0.0000 |
| 80.27 | Breakeven 79 | 1973.24 | -1973.24 | 0.00 | 0.3759 | 0.0000 |
| 81.27 | Breakeven 80 | 1872.91 | -1872.91 | 0.00 | 0.3567 | 0.0000 |
| 82.27 | Breakeven 81 | 1772.58 | -1772.58 | 0.00 | 0.3376 | 0.0000 |
| 83.28 | Breakeven 82 | 1672.24 | -1672.24 | 0.00 | 0.3185 | 0.0000 |
| 84.28 | Breakeven 83 | 1571.91 | -1571.91 | 0.00 | 0.2994 | 0.0000 |
| 85.00 | Downside (15%) | 1500.00 | -1500.00 | 0.00 | 0.2857 | 0.0000 |
| 85.28 | Breakeven 84 | 1471.57 | -1471.57 | 0.00 | 0.2803 | 0.0000 |
| 86.29 | Breakeven 85 | 1371.24 | -1371.24 | 0.00 | 0.2612 | 0.0000 |
| 87.29 | Breakeven 86 | 1270.90 | -1270.90 | 0.00 | 0.2421 | 0.0000 |
| 88.29 | Breakeven 87 | 1170.57 | -1170.57 | 0.00 | 0.2230 | 0.0000 |
| 89.30 | Breakeven 88 | 1070.23 | -1070.23 | 0.00 | 0.2039 | 0.0000 |
| 90.30 | Breakeven 89 | 969.90 | -969.90 | 0.00 | 0.1847 | 0.0000 |
| 91.30 | Breakeven 90 | 869.57 | -869.57 | 0.00 | 0.1656 | 0.0000 |
| 92.31 | Breakeven 91 | 769.23 | -769.23 | 0.00 | 0.1465 | 0.0000 |
| 93.31 | Breakeven 92 | 668.90 | -668.90 | 0.00 | 0.1274 | 0.0000 |
| 94.31 | Breakeven 93 | 568.56 | -568.56 | 0.00 | 0.1083 | 0.0000 |
| 95.32 | Breakeven 94 | 468.23 | -468.23 | 0.00 | 0.0892 | 0.0000 |
| 96.32 | Breakeven 95 | 367.89 | -367.89 | 0.00 | 0.0701 | 0.0000 |
| 97.32 | Breakeven 96 | 267.56 | -267.56 | 0.00 | 0.0510 | 0.0000 |
| 98.33 | Breakeven 97 | 167.22 | -167.22 | 0.00 | 0.0319 | 0.0000 |
| 99.33 | Breakeven 98 | 66.89 | -66.89 | 0.00 | 0.0127 | 0.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.33 | Breakeven 100 | -33.44 | 33.44 | 0.00 | -0.0064 | 0.0000 |
| 101.34 | Breakeven 101 | -133.78 | 133.78 | 0.00 | -0.0255 | 0.0000 |
| 102.34 | Breakeven 102 | -234.11 | 234.11 | 0.00 | -0.0446 | 0.0000 |
| 103.34 | Breakeven 103 | -334.45 | 334.45 | 0.00 | -0.0637 | 0.0000 |
| 104.35 | Breakeven 104 | -434.78 | 434.78 | 0.00 | -0.0828 | 0.0000 |
| 105.35 | Breakeven 105 | -535.12 | 535.12 | 0.00 | -0.1019 | 0.0000 |
| 106.35 | Breakeven 106 | -635.45 | 635.45 | 0.00 | -0.1210 | 0.0000 |
| 107.36 | Breakeven 107 | -735.79 | 735.79 | 0.00 | -0.1401 | 0.0000 |
| 108.36 | Breakeven 108 | -836.12 | 836.12 | 0.00 | -0.1593 | 0.0000 |
| 109.36 | Breakeven 109 | -936.45 | 936.45 | 0.00 | -0.1784 | 0.0000 |
| 110.37 | Breakeven 110 | -1036.79 | 1036.79 | 0.00 | -0.1975 | 0.0000 |
| 111.37 | Breakeven 111 | -1137.12 | 1137.12 | 0.00 | -0.2166 | 0.0000 |
| 112.37 | Breakeven 112 | -1237.46 | 1237.46 | 0.00 | -0.2357 | 0.0000 |
| 113.38 | Breakeven 113 | -1337.79 | 1337.79 | 0.00 | -0.2548 | 0.0000 |
| 114.38 | Breakeven 114 | -1438.13 | 1438.13 | 0.00 | -0.2739 | 0.0000 |
| 115.00 | Upside (15%) | -1500.00 | 1500.00 | 0.00 | -0.2857 | 0.0000 |
| 115.38 | Breakeven 115 | -1538.46 | 1538.46 | 0.00 | -0.2930 | 0.0000 |
| 116.39 | Breakeven 116 | -1638.80 | 1638.80 | 0.00 | -0.3122 | 0.0000 |
| 117.39 | Breakeven 117 | -1739.13 | 1739.13 | 0.00 | -0.3313 | 0.0000 |
| 118.39 | Breakeven 118 | -1839.46 | 1839.46 | 0.00 | -0.3504 | 0.0000 |
| 119.40 | Breakeven 119 | -1939.80 | 1939.80 | 0.00 | -0.3695 | 0.0000 |
| 120.40 | Breakeven 120 | -2040.13 | 2040.13 | 0.00 | -0.3886 | 0.0000 |
| 122.41 | Breakeven 121 | -2240.80 | 2240.80 | 0.00 | -0.4268 | 0.0000 |
| 123.41 | Breakeven 122 | -2341.14 | 2341.14 | 0.00 | -0.4459 | 0.0000 |
| 124.41 | Breakeven 123 | -2441.47 | 2441.47 | 0.00 | -0.4650 | 0.0000 |
| 125.42 | Breakeven 124 | -2541.81 | 2541.81 | 0.00 | -0.4842 | 0.0000 |
| 126.42 | Breakeven 125 | -2642.14 | 2642.14 | 0.00 | -0.5033 | 0.0000 |
| 127.42 | Breakeven 126 | -2742.47 | 2742.47 | 0.00 | -0.5224 | 0.0000 |
| 128.43 | Breakeven 127 | -2842.81 | 2842.81 | 0.00 | -0.5415 | 0.0000 |
| 129.43 | Breakeven 128 | -2943.14 | 2943.14 | 0.00 | -0.5606 | 0.0000 |
| 130.43 | Breakeven 129 | -3043.48 | 3043.48 | 0.00 | -0.5797 | 0.0000 |
| 131.44 | Breakeven 130 | -3143.81 | 3143.81 | 0.00 | -0.5988 | 0.0000 |
| 132.44 | Breakeven 131 | -3244.15 | 3244.15 | 0.00 | -0.6179 | 0.0000 |
| 133.44 | Breakeven 132 | -3344.48 | 3344.48 | 0.00 | -0.6370 | 0.0000 |
| 134.45 | Breakeven 133 | -3444.82 | 3444.82 | 0.00 | -0.6562 | 0.0000 |
| 135.45 | Breakeven 134 | -3545.15 | 3545.15 | 0.00 | -0.6753 | 0.0000 |
| 136.45 | Breakeven 135 | -3645.48 | 3645.48 | 0.00 | -0.6944 | 0.0000 |
| 137.46 | Breakeven 136 | -3745.82 | 3745.82 | 0.00 | -0.7135 | 0.0000 |
| 138.46 | Breakeven 137 | -3846.15 | 3846.15 | 0.00 | -0.7326 | 0.0000 |
| 139.46 | Breakeven 138 | -3946.49 | 3946.49 | 0.00 | -0.7517 | 0.0000 |
| 140.47 | Breakeven 139 | -4046.82 | 4046.82 | 0.00 | -0.7708 | 0.0000 |
| 141.47 | Breakeven 140 | -4147.16 | 4147.16 | 0.00 | -0.7899 | 0.0000 |
| 142.47 | Breakeven 141 | -4247.49 | 4247.49 | 0.00 | -0.8090 | 0.0000 |
| 143.48 | Breakeven 142 | -4347.83 | 4347.83 | 0.00 | -0.8282 | 0.0000 |
| 144.48 | Breakeven 143 | -4448.16 | 4448.16 | 0.00 | -0.8473 | 0.0000 |
| 145.48 | Breakeven 144 | -4548.49 | 4548.49 | 0.00 | -0.8664 | 0.0000 |
| 146.49 | Breakeven 145 | -4648.83 | 4648.83 | 0.00 | -0.8855 | 0.0000 |
| 147.49 | Breakeven 146 | -4749.16 | 4749.16 | 0.00 | -0.9046 | 0.0000 |
| 148.49 | Breakeven 147 | -4849.50 | 4849.50 | 0.00 | -0.9237 | 0.0000 |
| 149.50 | Breakeven 148 | -4949.83 | 4949.83 | 0.00 | -0.9428 | 0.0000 |
| 150.50 | Breakeven 149 | -5050.17 | 5050.17 | 0.00 | -0.9619 | 0.0000 |
| 151.51 | Breakeven 150 | -5150.50 | 5150.50 | 0.00 | -0.9810 | 0.0000 |
| 152.51 | Breakeven 151 | -5250.84 | 5250.84 | 0.00 | -1.0002 | 0.0000 |
| 153.51 | Breakeven 152 | -5351.17 | 5351.17 | 0.00 | -1.0193 | 0.0000 |
| 154.52 | Breakeven 153 | -5451.51 | 5451.51 | 0.00 | -1.0384 | 0.0000 |
| 155.52 | Breakeven 154 | -5551.84 | 5551.84 | 0.00 | -1.0575 | 0.0000 |
| 156.52 | Breakeven 155 | -5652.17 | 5652.17 | 0.00 | -1.0766 | 0.0000 |
| 157.53 | Breakeven 156 | -5752.51 | 5752.51 | 0.00 | -1.0957 | 0.0000 |
| 158.53 | Breakeven 157 | -5852.84 | 5852.84 | 0.00 | -1.1148 | 0.0000 |
| 159.53 | Breakeven 158 | -5953.18 | 5953.18 | 0.00 | -1.1339 | 0.0000 |
| 160.54 | Breakeven 159 | -6053.51 | 6053.51 | 0.00 | -1.1530 | 0.0000 |
| 161.54 | Breakeven 160 | -6153.85 | 6153.85 | 0.00 | -1.1722 | 0.0000 |
| 162.54 | Breakeven 161 | -6254.18 | 6254.18 | 0.00 | -1.1913 | 0.0000 |
| 163.55 | Breakeven 162 | -6354.52 | 6354.52 | 0.00 | -1.2104 | 0.0000 |
| 164.55 | Breakeven 163 | -6454.85 | 6454.85 | 0.00 | -1.2295 | 0.0000 |
| 165.55 | Breakeven 164 | -6555.18 | 6555.18 | 0.00 | -1.2486 | 0.0000 |
| 166.56 | Breakeven 165 | -6655.52 | 6655.52 | 0.00 | -1.2677 | 0.0000 |
| 167.56 | Breakeven 166 | -6755.85 | 6755.85 | 0.00 | -1.2868 | 0.0000 |
| 168.56 | Breakeven 167 | -6856.19 | 6856.19 | 0.00 | -1.3059 | 0.0000 |
| 169.57 | Breakeven 168 | -6956.52 | 6956.52 | 0.00 | -1.3251 | 0.0000 |
| 170.57 | Breakeven 169 | -7056.86 | 7056.86 | 0.00 | -1.3442 | 0.0000 |
| 171.57 | Breakeven 170 | -7157.19 | 7157.19 | 0.00 | -1.3633 | 0.0000 |
| 172.58 | Breakeven 171 | -7257.53 | 7257.53 | 0.00 | -1.3824 | 0.0000 |
| 173.58 | Breakeven 172 | -7357.86 | 7357.86 | 0.00 | -1.4015 | 0.0000 |
| 174.58 | Breakeven 173 | -7458.19 | 7458.19 | 0.00 | -1.4206 | 0.0000 |
| 175.59 | Breakeven 174 | -7558.53 | 7558.53 | 0.00 | -1.4397 | 0.0000 |
| 176.59 | Breakeven 175 | -7658.86 | 7658.86 | 0.00 | -1.4588 | 0.0000 |
| 177.59 | Breakeven 176 | -7759.20 | 7759.20 | 0.00 | -1.4779 | 0.0000 |
| 178.60 | Breakeven 177 | -7859.53 | 7859.53 | 0.00 | -1.4971 | 0.0000 |
| 179.60 | Breakeven 178 | -7959.87 | 7959.87 | 0.00 | -1.5162 | 0.0000 |
| 180.60 | Breakeven 179 | -8060.20 | 8060.20 | 0.00 | -1.5353 | 0.0000 |
| 181.61 | Breakeven 180 | -8160.54 | 8160.54 | 0.00 | -1.5544 | 0.0000 |
| 183.61 | Breakeven 181 | -8361.20 | 8361.20 | 0.00 | -1.5926 | 0.0000 |
| 184.62 | Breakeven 182 | -8461.54 | 8461.54 | 0.00 | -1.6117 | 0.0000 |
| 185.62 | Breakeven 183 | -8561.87 | 8561.87 | 0.00 | -1.6308 | 0.0000 |
| 186.62 | Breakeven 184 | -8662.21 | 8662.21 | 0.00 | -1.6499 | 0.0000 |
| 187.63 | Breakeven 185 | -8762.54 | 8762.54 | 0.00 | -1.6691 | 0.0000 |
| 188.63 | Breakeven 186 | -8862.88 | 8862.88 | 0.00 | -1.6882 | 0.0000 |
| 189.63 | Breakeven 187 | -8963.21 | 8963.21 | 0.00 | -1.7073 | 0.0000 |
| 190.64 | Breakeven 188 | -9063.55 | 9063.55 | 0.00 | -1.7264 | 0.0000 |
| 191.64 | Breakeven 189 | -9163.88 | 9163.88 | 0.00 | -1.7455 | 0.0000 |
| 192.64 | Breakeven 190 | -9264.21 | 9264.21 | 0.00 | -1.7646 | 0.0000 |
| 193.65 | Breakeven 191 | -9364.55 | 9364.55 | 0.00 | -1.7837 | 0.0000 |
| 194.65 | Breakeven 192 | -9464.88 | 9464.88 | 0.00 | -1.8028 | 0.0000 |
| 195.65 | Breakeven 193 | -9565.22 | 9565.22 | 0.00 | -1.8219 | 0.0000 |
| 196.66 | Breakeven 194 | -9665.55 | 9665.55 | 0.00 | -1.8411 | 0.0000 |
| 197.66 | Breakeven 195 | -9765.89 | 9765.89 | 0.00 | -1.8602 | 0.0000 |
| 198.66 | Breakeven 196 | -9866.22 | 9866.22 | 0.00 | -1.8793 | 0.0000 |
| 199.67 | Breakeven 197 | -9966.56 | 9966.56 | 0.00 | -1.8984 | 0.0000 |
| 200.67 | Breakeven 198 | -10066.89 | 10066.89 | 0.00 | -1.9175 | 0.0000 |
| 201.67 | Breakeven 199 | -10167.22 | 10167.22 | 0.00 | -1.9366 | 0.0000 |
| 202.68 | Breakeven 200 | -10267.56 | 10267.56 | 0.00 | -1.9557 | 0.0000 |
| 203.68 | Breakeven 201 | -10367.89 | 10367.89 | 0.00 | -1.9748 | 0.0000 |
| 204.68 | Breakeven 202 | -10468.23 | 10468.23 | 0.00 | -1.9939 | 0.0000 |
| 205.69 | Breakeven 203 | -10568.56 | 10568.56 | 0.00 | -2.0131 | 0.0000 |
| 206.69 | Breakeven 204 | -10668.90 | 10668.90 | 0.00 | -2.0322 | 0.0000 |
| 207.69 | Breakeven 205 | -10769.23 | 10769.23 | 0.00 | -2.0513 | 0.0000 |
| 208.70 | Breakeven 206 | -10869.57 | 10869.57 | 0.00 | -2.0704 | 0.0000 |
| 209.70 | Breakeven 207 | -10969.90 | 10969.90 | 0.00 | -2.0895 | 0.0000 |
| 210.70 | Breakeven 208 | -11070.23 | 11070.23 | 0.00 | -2.1086 | 0.0000 |
| 211.71 | Breakeven 209 | -11170.57 | 11170.57 | 0.00 | -2.1277 | 0.0000 |
| 212.71 | Breakeven 210 | -11270.90 | 11270.90 | 0.00 | -2.1468 | 0.0000 |
| 213.71 | Breakeven 211 | -11371.24 | 11371.24 | 0.00 | -2.1660 | 0.0000 |
| 214.72 | Breakeven 212 | -11471.57 | 11471.57 | 0.00 | -2.1851 | 0.0000 |
| 215.72 | Breakeven 213 | -11571.91 | 11571.91 | 0.00 | -2.2042 | 0.0000 |
| 216.72 | Breakeven 214 | -11672.24 | 11672.24 | 0.00 | -2.2233 | 0.0000 |
| 217.73 | Breakeven 215 | -11772.58 | 11772.58 | 0.00 | -2.2424 | 0.0000 |
| 218.73 | Breakeven 216 | -11872.91 | 11872.91 | 0.00 | -2.2615 | 0.0000 |
| 219.73 | Breakeven 217 | -11973.24 | 11973.24 | 0.00 | -2.2806 | 0.0000 |
| 220.74 | Breakeven 218 | -12073.58 | 12073.58 | 0.00 | -2.2997 | 0.0000 |
| 221.74 | Breakeven 219 | -12173.91 | 12173.91 | 0.00 | -2.3188 | 0.0000 |
| 222.74 | Breakeven 220 | -12274.25 | 12274.25 | 0.00 | -2.3380 | 0.0000 |
| 223.75 | Breakeven 221 | -12374.58 | 12374.58 | 0.00 | -2.3571 | 0.0000 |
| 224.75 | Breakeven 222 | -12474.92 | 12474.92 | 0.00 | -2.3762 | 0.0000 |
| 225.75 | Breakeven 223 | -12575.25 | 12575.25 | 0.00 | -2.3953 | 0.0000 |
| 226.76 | Breakeven 224 | -12675.59 | 12675.59 | 0.00 | -2.4144 | 0.0000 |
| 227.76 | Breakeven 225 | -12775.92 | 12775.92 | 0.00 | -2.4335 | 0.0000 |
| 228.76 | Breakeven 226 | -12876.25 | 12876.25 | 0.00 | -2.4526 | 0.0000 |
| 229.77 | Breakeven 227 | -12976.59 | 12976.59 | 0.00 | -2.4717 | 0.0000 |
| 230.77 | Breakeven 228 | -13076.92 | 13076.92 | 0.00 | -2.4908 | 0.0000 |
| 231.77 | Breakeven 229 | -13177.26 | 13177.26 | 0.00 | -2.5100 | 0.0000 |
| 232.78 | Breakeven 230 | -13277.59 | 13277.59 | 0.00 | -2.5291 | 0.0000 |
| 233.78 | Breakeven 231 | -13377.93 | 13377.93 | 0.00 | -2.5482 | 0.0000 |
| 234.78 | Breakeven 232 | -13478.26 | 13478.26 | 0.00 | -2.5673 | 0.0000 |
| 235.79 | Breakeven 233 | -13578.60 | 13578.60 | 0.00 | -2.5864 | 0.0000 |
| 236.79 | Breakeven 234 | -13678.93 | 13678.93 | 0.00 | -2.6055 | 0.0000 |
| 237.79 | Breakeven 235 | -13779.26 | 13779.26 | 0.00 | -2.6246 | 0.0000 |
| 238.80 | Breakeven 236 | -13879.60 | 13879.60 | 0.00 | -2.6437 | 0.0000 |
| 239.80 | Breakeven 237 | -13979.93 | 13979.93 | 0.00 | -2.6628 | 0.0000 |
| 240.80 | Breakeven 238 | -14080.27 | 14080.27 | 0.00 | -2.6820 | 0.0000 |
| 241.81 | Breakeven 239 | -14180.60 | 14180.60 | 0.00 | -2.7011 | 0.0000 |
| 242.81 | Breakeven 240 | -14280.94 | 14280.94 | 0.00 | -2.7202 | 0.0000 |
| 243.81 | Breakeven 241 | -14381.27 | 14381.27 | 0.00 | -2.7393 | 0.0000 |
| 244.82 | Breakeven 242 | -14481.61 | 14481.61 | 0.00 | -2.7584 | 0.0000 |
| 245.82 | Breakeven 243 | -14581.94 | 14581.94 | 0.00 | -2.7775 | 0.0000 |
| 246.82 | Breakeven 244 | -14682.27 | 14682.27 | 0.00 | -2.7966 | 0.0000 |
| 247.83 | Breakeven 245 | -14782.61 | 14782.61 | 0.00 | -2.8157 | 0.0000 |
| 248.83 | Breakeven 246 | -14882.94 | 14882.94 | 0.00 | -2.8348 | 0.0000 |
| 249.83 | Breakeven 247 | -14983.28 | 14983.28 | 0.00 | -2.8540 | 0.0000 |
| 250.84 | Breakeven 248 | -15083.61 | 15083.61 | 0.00 | -2.8731 | 0.0000 |
| 251.84 | Breakeven 249 | -15183.95 | 15183.95 | 0.00 | -2.8922 | 0.0000 |
| 252.84 | Breakeven 250 | -15284.28 | 15284.28 | 0.00 | -2.9113 | 0.0000 |
| 253.85 | Breakeven 251 | -15384.62 | 15384.62 | 0.00 | -2.9304 | 0.0000 |
| 254.85 | Breakeven 252 | -15484.95 | 15484.95 | 0.00 | -2.9495 | 0.0000 |
| 255.85 | Breakeven 253 | -15585.28 | 15585.28 | 0.00 | -2.9686 | 0.0000 |
| 256.86 | Breakeven 254 | -15685.62 | 15685.62 | 0.00 | -2.9877 | 0.0000 |
| 257.86 | Breakeven 255 | -15785.95 | 15785.95 | 0.00 | -3.0068 | 0.0000 |
| 258.86 | Breakeven 256 | -15886.29 | 15886.29 | 0.00 | -3.0260 | 0.0000 |
| 259.87 | Breakeven 257 | -15986.62 | 15986.62 | 0.00 | -3.0451 | 0.0000 |
| 260.87 | Breakeven 258 | -16086.96 | 16086.96 | 0.00 | -3.0642 | 0.0000 |
| 261.87 | Breakeven 259 | -16187.29 | 16187.29 | 0.00 | -3.0833 | 0.0000 |
| 262.88 | Breakeven 260 | -16287.63 | 16287.63 | 0.00 | -3.1024 | 0.0000 |
| 263.88 | Breakeven 261 | -16387.96 | 16387.96 | 0.00 | -3.1215 | 0.0000 |
| 264.88 | Breakeven 262 | -16488.29 | 16488.29 | 0.00 | -3.1406 | 0.0000 |
| 265.89 | Breakeven 263 | -16588.63 | 16588.63 | 0.00 | -3.1597 | 0.0000 |
| 266.89 | Breakeven 264 | -16688.96 | 16688.96 | 0.00 | -3.1789 | 0.0000 |
| 267.89 | Breakeven 265 | -16789.30 | 16789.30 | 0.00 | -3.1980 | 0.0000 |
| 268.90 | Breakeven 266 | -16889.63 | 16889.63 | 0.00 | -3.2171 | 0.0000 |
| 269.90 | Breakeven 267 | -16989.97 | 16989.97 | 0.00 | -3.2362 | 0.0000 |
| 270.90 | Breakeven 268 | -17090.30 | 17090.30 | 0.00 | -3.2553 | 0.0000 |
| 271.91 | Breakeven 269 | -17190.64 | 17190.64 | 0.00 | -3.2744 | 0.0000 |
| 272.91 | Breakeven 270 | -17290.97 | 17290.97 | 0.00 | -3.2935 | 0.0000 |
| 273.91 | Breakeven 271 | -17391.30 | 17391.30 | 0.00 | -3.3126 | 0.0000 |
| 274.92 | Breakeven 272 | -17491.64 | 17491.64 | 0.00 | -3.3317 | 0.0000 |
| 275.92 | Breakeven 273 | -17591.97 | 17591.97 | 0.00 | -3.3509 | 0.0000 |
| 276.92 | Breakeven 274 | -17692.31 | 17692.31 | 0.00 | -3.3700 | 0.0000 |
| 277.93 | Breakeven 275 | -17792.64 | 17792.64 | 0.00 | -3.3891 | 0.0000 |
| 278.93 | Breakeven 276 | -17892.98 | 17892.98 | 0.00 | -3.4082 | 0.0000 |
| 279.93 | Breakeven 277 | -17993.31 | 17993.31 | 0.00 | -3.4273 | 0.0000 |
| 280.94 | Breakeven 278 | -18093.65 | 18093.65 | 0.00 | -3.4464 | 0.0000 |
| 281.94 | Breakeven 279 | -18193.98 | 18193.98 | 0.00 | -3.4655 | 0.0000 |
| 282.94 | Breakeven 280 | -18294.31 | 18294.31 | 0.00 | -3.4846 | 0.0000 |
| 283.95 | Breakeven 281 | -18394.65 | 18394.65 | 0.00 | -3.5037 | 0.0000 |
| 284.95 | Breakeven 282 | -18494.98 | 18494.98 | 0.00 | -3.5229 | 0.0000 |
| 285.95 | Breakeven 283 | -18595.32 | 18595.32 | 0.00 | -3.5420 | 0.0000 |
| 286.96 | Breakeven 284 | -18695.65 | 18695.65 | 0.00 | -3.5611 | 0.0000 |
| 287.96 | Breakeven 285 | -18795.99 | 18795.99 | 0.00 | -3.5802 | 0.0000 |
| 288.96 | Breakeven 286 | -18896.32 | 18896.32 | 0.00 | -3.5993 | 0.0000 |
| 289.97 | Breakeven 287 | -18996.66 | 18996.66 | 0.00 | -3.6184 | 0.0000 |
| 290.97 | Breakeven 288 | -19096.99 | 19096.99 | 0.00 | -3.6375 | 0.0000 |
| 291.97 | Breakeven 289 | -19197.32 | 19197.32 | 0.00 | -3.6566 | 0.0000 |
| 292.98 | Breakeven 290 | -19297.66 | 19297.66 | 0.00 | -3.6757 | 0.0000 |
| 293.98 | Breakeven 291 | -19397.99 | 19397.99 | 0.00 | -3.6949 | 0.0000 |
| 294.98 | Breakeven 292 | -19498.33 | 19498.33 | 0.00 | -3.7140 | 0.0000 |
| 295.99 | Breakeven 293 | -19598.66 | 19598.66 | 0.00 | -3.7331 | 0.0000 |
| 296.99 | Breakeven 294 | -19699.00 | 19699.00 | 0.00 | -3.7522 | 0.0000 |
| 297.99 | Breakeven 295 | -19799.33 | 19799.33 | 0.00 | -3.7713 | 0.0000 |
| 299.00 | Breakeven 296 | -19899.67 | 19899.67 | 0.00 | -3.7904 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| breakeven_1 | Breakeven 1 | 0.00 | -100.00% | 10000.00 | 0.00 | 0.0000 |
| zero | Stock to Zero | 0.00 | -100.00% | 10000.00 | 0.00 | 0.0000 |
| breakeven_2 | Breakeven 2 | 1.00 | -99.00% | 9899.67 | 0.00 | 0.0000 |
| breakeven_3 | Breakeven 3 | 2.01 | -97.99% | 9799.33 | 0.00 | 0.0000 |
| breakeven_4 | Breakeven 4 | 3.01 | -96.99% | 9699.00 | 0.00 | 0.0000 |
| breakeven_5 | Breakeven 5 | 4.01 | -95.99% | 9598.66 | 0.00 | 0.0000 |
| breakeven_6 | Breakeven 6 | 5.02 | -94.98% | 9498.33 | 0.00 | 0.0000 |
| breakeven_7 | Breakeven 7 | 6.02 | -93.98% | 9397.99 | 0.00 | 0.0000 |
| breakeven_8 | Breakeven 8 | 7.02 | -92.98% | 9297.66 | 0.00 | 0.0000 |
| breakeven_9 | Breakeven 9 | 8.03 | -91.97% | 9197.32 | 0.00 | 0.0000 |
| breakeven_10 | Breakeven 10 | 9.03 | -90.97% | 9096.99 | 0.00 | 0.0000 |
| breakeven_11 | Breakeven 11 | 10.03 | -89.97% | 8996.66 | 0.00 | 0.0000 |
| breakeven_12 | Breakeven 12 | 11.04 | -88.96% | 8896.32 | 0.00 | 0.0000 |
| breakeven_13 | Breakeven 13 | 12.04 | -87.96% | 8795.99 | 0.00 | 0.0000 |
| breakeven_14 | Breakeven 14 | 13.04 | -86.96% | 8695.65 | 0.00 | 0.0000 |
| breakeven_15 | Breakeven 15 | 14.05 | -85.95% | 8595.32 | 0.00 | 0.0000 |
| breakeven_16 | Breakeven 16 | 15.05 | -84.95% | 8494.98 | 0.00 | 0.0000 |
| breakeven_17 | Breakeven 17 | 17.06 | -82.94% | 8294.31 | 0.00 | 0.0000 |
| breakeven_18 | Breakeven 18 | 18.06 | -81.94% | 8193.98 | -0.00 | -0.0000 |
| breakeven_19 | Breakeven 19 | 19.06 | -80.94% | 8093.65 | 0.00 | 0.0000 |
| breakeven_20 | Breakeven 20 | 20.07 | -79.93% | 7993.31 | 0.00 | 0.0000 |
| breakeven_21 | Breakeven 21 | 21.07 | -78.93% | 7892.98 | 0.00 | 0.0000 |
| breakeven_22 | Breakeven 22 | 22.07 | -77.93% | 7792.64 | 0.00 | 0.0000 |
| breakeven_23 | Breakeven 23 | 23.08 | -76.92% | 7692.31 | 0.00 | 0.0000 |
| breakeven_24 | Breakeven 24 | 24.08 | -75.92% | 7591.97 | 0.00 | 0.0000 |
| breakeven_25 | Breakeven 25 | 25.08 | -74.92% | 7491.64 | 0.00 | 0.0000 |
| breakeven_26 | Breakeven 26 | 26.09 | -73.91% | 7391.30 | 0.00 | 0.0000 |
| breakeven_27 | Breakeven 27 | 27.09 | -72.91% | 7290.97 | 0.00 | 0.0000 |
| breakeven_28 | Breakeven 28 | 28.09 | -71.91% | 7190.64 | 0.00 | 0.0000 |
| breakeven_29 | Breakeven 29 | 29.10 | -70.90% | 7090.30 | 0.00 | 0.0000 |
| breakeven_30 | Breakeven 30 | 30.10 | -69.90% | 6989.97 | 0.00 | 0.0000 |
| breakeven_31 | Breakeven 31 | 31.10 | -68.90% | 6889.63 | 0.00 | 0.0000 |
| breakeven_32 | Breakeven 32 | 32.11 | -67.89% | 6789.30 | 0.00 | 0.0000 |
| breakeven_33 | Breakeven 33 | 33.11 | -66.89% | 6688.96 | 0.00 | 0.0000 |
| breakeven_34 | Breakeven 34 | 34.11 | -65.89% | 6588.63 | 0.00 | 0.0000 |
| breakeven_35 | Breakeven 35 | 35.12 | -64.88% | 6488.29 | 0.00 | 0.0000 |
| breakeven_36 | Breakeven 36 | 36.12 | -63.88% | 6387.96 | 0.00 | 0.0000 |
| breakeven_37 | Breakeven 37 | 37.12 | -62.88% | 6287.63 | 0.00 | 0.0000 |
| breakeven_38 | Breakeven 38 | 38.13 | -61.87% | 6187.29 | 0.00 | 0.0000 |
| breakeven_39 | Breakeven 39 | 39.13 | -60.87% | 6086.96 | 0.00 | 0.0000 |
| breakeven_40 | Breakeven 40 | 40.13 | -59.87% | 5986.62 | 0.00 | 0.0000 |
| breakeven_41 | Breakeven 41 | 41.14 | -58.86% | 5886.29 | 0.00 | 0.0000 |
| breakeven_42 | Breakeven 42 | 42.14 | -57.86% | 5785.95 | 0.00 | 0.0000 |
| breakeven_43 | Breakeven 43 | 43.14 | -56.86% | 5685.62 | 0.00 | 0.0000 |
| breakeven_44 | Breakeven 44 | 44.15 | -55.85% | 5585.28 | 0.00 | 0.0000 |
| breakeven_45 | Breakeven 45 | 45.15 | -54.85% | 5484.95 | 0.00 | 0.0000 |
| breakeven_46 | Breakeven 46 | 46.15 | -53.85% | 5384.62 | 0.00 | 0.0000 |
| breakeven_47 | Breakeven 47 | 47.16 | -52.84% | 5284.28 | 0.00 | 0.0000 |
| breakeven_48 | Breakeven 48 | 48.16 | -51.84% | 5183.95 | 0.00 | 0.0000 |
| breakeven_49 | Breakeven 49 | 49.16 | -50.84% | 5083.61 | 0.00 | 0.0000 |
| breakeven_50 | Breakeven 50 | 50.17 | -49.83% | 4983.28 | 0.00 | 0.0000 |
| breakeven_51 | Breakeven 51 | 51.17 | -48.83% | 4882.94 | 0.00 | 0.0000 |
| breakeven_52 | Breakeven 52 | 52.17 | -47.83% | 4782.61 | 0.00 | 0.0000 |
| breakeven_53 | Breakeven 53 | 53.18 | -46.82% | 4682.27 | 0.00 | 0.0000 |
| breakeven_54 | Breakeven 54 | 54.18 | -45.82% | 4581.94 | 0.00 | 0.0000 |
| breakeven_55 | Breakeven 55 | 55.18 | -44.82% | 4481.61 | 0.00 | 0.0000 |
| breakeven_56 | Breakeven 56 | 56.19 | -43.81% | 4381.27 | 0.00 | 0.0000 |
| breakeven_57 | Breakeven 57 | 58.19 | -41.81% | 4180.60 | 0.00 | 0.0000 |
| breakeven_58 | Breakeven 58 | 59.20 | -40.80% | 4080.27 | 0.00 | 0.0000 |
| breakeven_59 | Breakeven 59 | 60.20 | -39.80% | 3979.93 | 0.00 | 0.0000 |
| breakeven_60 | Breakeven 60 | 61.20 | -38.80% | 3879.60 | 0.00 | 0.0000 |
| breakeven_61 | Breakeven 61 | 62.21 | -37.79% | 3779.26 | 0.00 | 0.0000 |
| breakeven_62 | Breakeven 62 | 63.21 | -36.79% | 3678.93 | 0.00 | 0.0000 |
| breakeven_63 | Breakeven 63 | 64.21 | -35.79% | 3578.60 | 0.00 | 0.0000 |
| breakeven_64 | Breakeven 64 | 65.22 | -34.78% | 3478.26 | 0.00 | 0.0000 |
| breakeven_65 | Breakeven 65 | 66.22 | -33.78% | 3377.93 | 0.00 | 0.0000 |
| breakeven_66 | Breakeven 66 | 67.22 | -32.78% | 3277.59 | 0.00 | 0.0000 |
| breakeven_67 | Breakeven 67 | 68.23 | -31.77% | 3177.26 | 0.00 | 0.0000 |
| breakeven_68 | Breakeven 68 | 69.23 | -30.77% | 3076.92 | 0.00 | 0.0000 |
| breakeven_69 | Breakeven 69 | 70.23 | -29.77% | 2976.59 | 0.00 | 0.0000 |
| breakeven_70 | Breakeven 70 | 71.24 | -28.76% | 2876.25 | 0.00 | 0.0000 |
| breakeven_71 | Breakeven 71 | 72.24 | -27.76% | 2775.92 | 0.00 | 0.0000 |
| breakeven_72 | Breakeven 72 | 73.24 | -26.76% | 2675.59 | 0.00 | 0.0000 |
| breakeven_73 | Breakeven 73 | 74.25 | -25.75% | 2575.25 | 0.00 | 0.0000 |
| breakeven_74 | Breakeven 74 | 75.25 | -24.75% | 2474.92 | 0.00 | 0.0000 |
| breakeven_75 | Breakeven 75 | 76.25 | -23.75% | 2374.58 | 0.00 | 0.0000 |
| breakeven_76 | Breakeven 76 | 77.26 | -22.74% | 2274.25 | 0.00 | 0.0000 |
| breakeven_77 | Breakeven 77 | 78.26 | -21.74% | 2173.91 | 0.00 | 0.0000 |
| breakeven_78 | Breakeven 78 | 79.26 | -20.74% | 2073.58 | -0.00 | -0.0000 |
| breakeven_79 | Breakeven 79 | 80.27 | -19.73% | 1973.24 | 0.00 | 0.0000 |
| breakeven_80 | Breakeven 80 | 81.27 | -18.73% | 1872.91 | 0.00 | 0.0000 |
| breakeven_81 | Breakeven 81 | 82.27 | -17.73% | 1772.58 | 0.00 | 0.0000 |
| breakeven_82 | Breakeven 82 | 83.28 | -16.72% | 1672.24 | 0.00 | 0.0000 |
| breakeven_83 | Breakeven 83 | 84.28 | -15.72% | 1571.91 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1500.00 | 0.00 | 0.0000 |
| breakeven_84 | Breakeven 84 | 85.28 | -14.72% | 1471.57 | 0.00 | 0.0000 |
| breakeven_85 | Breakeven 85 | 86.29 | -13.71% | 1371.24 | 0.00 | 0.0000 |
| breakeven_86 | Breakeven 86 | 87.29 | -12.71% | 1270.90 | 0.00 | 0.0000 |
| breakeven_87 | Breakeven 87 | 88.29 | -11.71% | 1170.57 | 0.00 | 0.0000 |
| breakeven_88 | Breakeven 88 | 89.30 | -10.70% | 1070.23 | 0.00 | 0.0000 |
| breakeven_89 | Breakeven 89 | 90.30 | -9.70% | 969.90 | 0.00 | 0.0000 |
| breakeven_90 | Breakeven 90 | 91.30 | -8.70% | 869.57 | 0.00 | 0.0000 |
| breakeven_91 | Breakeven 91 | 92.31 | -7.69% | 769.23 | 0.00 | 0.0000 |
| breakeven_92 | Breakeven 92 | 93.31 | -6.69% | 668.90 | 0.00 | 0.0000 |
| breakeven_93 | Breakeven 93 | 94.31 | -5.69% | 568.56 | 0.00 | 0.0000 |
| breakeven_94 | Breakeven 94 | 95.32 | -4.68% | 468.23 | 0.00 | 0.0000 |
| breakeven_95 | Breakeven 95 | 96.32 | -3.68% | 367.89 | 0.00 | 0.0000 |
| breakeven_96 | Breakeven 96 | 97.32 | -2.68% | 267.56 | 0.00 | 0.0000 |
| breakeven_97 | Breakeven 97 | 98.33 | -1.67% | 167.22 | 0.00 | 0.0000 |
| breakeven_98 | Breakeven 98 | 99.33 | -0.67% | 66.89 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_99 | Breakeven 99 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_100 | Breakeven 100 | 100.33 | 0.33% | -33.44 | 0.00 | 0.0000 |
| breakeven_101 | Breakeven 101 | 101.34 | 1.34% | -133.78 | 0.00 | 0.0000 |
| breakeven_102 | Breakeven 102 | 102.34 | 2.34% | -234.11 | 0.00 | 0.0000 |
| breakeven_103 | Breakeven 103 | 103.34 | 3.34% | -334.45 | 0.00 | 0.0000 |
| breakeven_104 | Breakeven 104 | 104.35 | 4.35% | -434.78 | 0.00 | 0.0000 |
| breakeven_105 | Breakeven 105 | 105.35 | 5.35% | -535.12 | 0.00 | 0.0000 |
| breakeven_106 | Breakeven 106 | 106.35 | 6.35% | -635.45 | 0.00 | 0.0000 |
| breakeven_107 | Breakeven 107 | 107.36 | 7.36% | -735.79 | 0.00 | 0.0000 |
| breakeven_108 | Breakeven 108 | 108.36 | 8.36% | -836.12 | 0.00 | 0.0000 |
| breakeven_109 | Breakeven 109 | 109.36 | 9.36% | -936.45 | 0.00 | 0.0000 |
| breakeven_110 | Breakeven 110 | 110.37 | 10.37% | -1036.79 | 0.00 | 0.0000 |
| breakeven_111 | Breakeven 111 | 111.37 | 11.37% | -1137.12 | 0.00 | 0.0000 |
| breakeven_112 | Breakeven 112 | 112.37 | 12.37% | -1237.46 | 0.00 | 0.0000 |
| breakeven_113 | Breakeven 113 | 113.38 | 13.38% | -1337.79 | 0.00 | 0.0000 |
| breakeven_114 | Breakeven 114 | 114.38 | 14.38% | -1438.13 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1500.00 | 0.00 | 0.0000 |
| breakeven_115 | Breakeven 115 | 115.38 | 15.38% | -1538.46 | 0.00 | 0.0000 |
| breakeven_116 | Breakeven 116 | 116.39 | 16.39% | -1638.80 | 0.00 | 0.0000 |
| breakeven_117 | Breakeven 117 | 117.39 | 17.39% | -1739.13 | 0.00 | 0.0000 |
| breakeven_118 | Breakeven 118 | 118.39 | 18.39% | -1839.46 | 0.00 | 0.0000 |
| breakeven_119 | Breakeven 119 | 119.40 | 19.40% | -1939.80 | 0.00 | 0.0000 |
| breakeven_120 | Breakeven 120 | 120.40 | 20.40% | -2040.13 | 0.00 | 0.0000 |
| breakeven_121 | Breakeven 121 | 122.41 | 22.41% | -2240.80 | 0.00 | 0.0000 |
| breakeven_122 | Breakeven 122 | 123.41 | 23.41% | -2341.14 | 0.00 | 0.0000 |
| breakeven_123 | Breakeven 123 | 124.41 | 24.41% | -2441.47 | 0.00 | 0.0000 |
| breakeven_124 | Breakeven 124 | 125.42 | 25.42% | -2541.81 | 0.00 | 0.0000 |
| breakeven_125 | Breakeven 125 | 126.42 | 26.42% | -2642.14 | 0.00 | 0.0000 |
| breakeven_126 | Breakeven 126 | 127.42 | 27.42% | -2742.47 | 0.00 | 0.0000 |
| breakeven_127 | Breakeven 127 | 128.43 | 28.43% | -2842.81 | 0.00 | 0.0000 |
| breakeven_128 | Breakeven 128 | 129.43 | 29.43% | -2943.14 | 0.00 | 0.0000 |
| breakeven_129 | Breakeven 129 | 130.43 | 30.43% | -3043.48 | 0.00 | 0.0000 |
| breakeven_130 | Breakeven 130 | 131.44 | 31.44% | -3143.81 | 0.00 | 0.0000 |
| breakeven_131 | Breakeven 131 | 132.44 | 32.44% | -3244.15 | 0.00 | 0.0000 |
| breakeven_132 | Breakeven 132 | 133.44 | 33.44% | -3344.48 | 0.00 | 0.0000 |
| breakeven_133 | Breakeven 133 | 134.45 | 34.45% | -3444.82 | 0.00 | 0.0000 |
| breakeven_134 | Breakeven 134 | 135.45 | 35.45% | -3545.15 | 0.00 | 0.0000 |
| breakeven_135 | Breakeven 135 | 136.45 | 36.45% | -3645.48 | 0.00 | 0.0000 |
| breakeven_136 | Breakeven 136 | 137.46 | 37.46% | -3745.82 | 0.00 | 0.0000 |
| breakeven_137 | Breakeven 137 | 138.46 | 38.46% | -3846.15 | 0.00 | 0.0000 |
| breakeven_138 | Breakeven 138 | 139.46 | 39.46% | -3946.49 | 0.00 | 0.0000 |
| breakeven_139 | Breakeven 139 | 140.47 | 40.47% | -4046.82 | 0.00 | 0.0000 |
| breakeven_140 | Breakeven 140 | 141.47 | 41.47% | -4147.16 | 0.00 | 0.0000 |
| breakeven_141 | Breakeven 141 | 142.47 | 42.47% | -4247.49 | 0.00 | 0.0000 |
| breakeven_142 | Breakeven 142 | 143.48 | 43.48% | -4347.83 | 0.00 | 0.0000 |
| breakeven_143 | Breakeven 143 | 144.48 | 44.48% | -4448.16 | 0.00 | 0.0000 |
| breakeven_144 | Breakeven 144 | 145.48 | 45.48% | -4548.49 | 0.00 | 0.0000 |
| breakeven_145 | Breakeven 145 | 146.49 | 46.49% | -4648.83 | 0.00 | 0.0000 |
| breakeven_146 | Breakeven 146 | 147.49 | 47.49% | -4749.16 | 0.00 | 0.0000 |
| breakeven_147 | Breakeven 147 | 148.49 | 48.49% | -4849.50 | 0.00 | 0.0000 |
| breakeven_148 | Breakeven 148 | 149.50 | 49.50% | -4949.83 | 0.00 | 0.0000 |
| breakeven_149 | Breakeven 149 | 150.50 | 50.50% | -5050.17 | 0.00 | 0.0000 |
| breakeven_150 | Breakeven 150 | 151.51 | 51.51% | -5150.50 | 0.00 | 0.0000 |
| breakeven_151 | Breakeven 151 | 152.51 | 52.51% | -5250.84 | 0.00 | 0.0000 |
| breakeven_152 | Breakeven 152 | 153.51 | 53.51% | -5351.17 | 0.00 | 0.0000 |
| breakeven_153 | Breakeven 153 | 154.52 | 54.52% | -5451.51 | 0.00 | 0.0000 |
| breakeven_154 | Breakeven 154 | 155.52 | 55.52% | -5551.84 | 0.00 | 0.0000 |
| breakeven_155 | Breakeven 155 | 156.52 | 56.52% | -5652.17 | 0.00 | 0.0000 |
| breakeven_156 | Breakeven 156 | 157.53 | 57.53% | -5752.51 | 0.00 | 0.0000 |
| breakeven_157 | Breakeven 157 | 158.53 | 58.53% | -5852.84 | 0.00 | 0.0000 |
| breakeven_158 | Breakeven 158 | 159.53 | 59.53% | -5953.18 | 0.00 | 0.0000 |
| breakeven_159 | Breakeven 159 | 160.54 | 60.54% | -6053.51 | 0.00 | 0.0000 |
| breakeven_160 | Breakeven 160 | 161.54 | 61.54% | -6153.85 | 0.00 | 0.0000 |
| breakeven_161 | Breakeven 161 | 162.54 | 62.54% | -6254.18 | 0.00 | 0.0000 |
| breakeven_162 | Breakeven 162 | 163.55 | 63.55% | -6354.52 | 0.00 | 0.0000 |
| breakeven_163 | Breakeven 163 | 164.55 | 64.55% | -6454.85 | 0.00 | 0.0000 |
| breakeven_164 | Breakeven 164 | 165.55 | 65.55% | -6555.18 | 0.00 | 0.0000 |
| breakeven_165 | Breakeven 165 | 166.56 | 66.56% | -6655.52 | 0.00 | 0.0000 |
| breakeven_166 | Breakeven 166 | 167.56 | 67.56% | -6755.85 | 0.00 | 0.0000 |
| breakeven_167 | Breakeven 167 | 168.56 | 68.56% | -6856.19 | 0.00 | 0.0000 |
| breakeven_168 | Breakeven 168 | 169.57 | 69.57% | -6956.52 | 0.00 | 0.0000 |
| breakeven_169 | Breakeven 169 | 170.57 | 70.57% | -7056.86 | 0.00 | 0.0000 |
| breakeven_170 | Breakeven 170 | 171.57 | 71.57% | -7157.19 | 0.00 | 0.0000 |
| breakeven_171 | Breakeven 171 | 172.58 | 72.58% | -7257.53 | 0.00 | 0.0000 |
| breakeven_172 | Breakeven 172 | 173.58 | 73.58% | -7357.86 | 0.00 | 0.0000 |
| breakeven_173 | Breakeven 173 | 174.58 | 74.58% | -7458.19 | 0.00 | 0.0000 |
| breakeven_174 | Breakeven 174 | 175.59 | 75.59% | -7558.53 | 0.00 | 0.0000 |
| breakeven_175 | Breakeven 175 | 176.59 | 76.59% | -7658.86 | 0.00 | 0.0000 |
| breakeven_176 | Breakeven 176 | 177.59 | 77.59% | -7759.20 | 0.00 | 0.0000 |
| breakeven_177 | Breakeven 177 | 178.60 | 78.60% | -7859.53 | 0.00 | 0.0000 |
| breakeven_178 | Breakeven 178 | 179.60 | 79.60% | -7959.87 | 0.00 | 0.0000 |
| breakeven_179 | Breakeven 179 | 180.60 | 80.60% | -8060.20 | 0.00 | 0.0000 |
| breakeven_180 | Breakeven 180 | 181.61 | 81.61% | -8160.54 | 0.00 | 0.0000 |
| breakeven_181 | Breakeven 181 | 183.61 | 83.61% | -8361.20 | 0.00 | 0.0000 |
| breakeven_182 | Breakeven 182 | 184.62 | 84.62% | -8461.54 | 0.00 | 0.0000 |
| breakeven_183 | Breakeven 183 | 185.62 | 85.62% | -8561.87 | 0.00 | 0.0000 |
| breakeven_184 | Breakeven 184 | 186.62 | 86.62% | -8662.21 | 0.00 | 0.0000 |
| breakeven_185 | Breakeven 185 | 187.63 | 87.63% | -8762.54 | 0.00 | 0.0000 |
| breakeven_186 | Breakeven 186 | 188.63 | 88.63% | -8862.88 | 0.00 | 0.0000 |
| breakeven_187 | Breakeven 187 | 189.63 | 89.63% | -8963.21 | 0.00 | 0.0000 |
| breakeven_188 | Breakeven 188 | 190.64 | 90.64% | -9063.55 | 0.00 | 0.0000 |
| breakeven_189 | Breakeven 189 | 191.64 | 91.64% | -9163.88 | 0.00 | 0.0000 |
| breakeven_190 | Breakeven 190 | 192.64 | 92.64% | -9264.21 | 0.00 | 0.0000 |
| breakeven_191 | Breakeven 191 | 193.65 | 93.65% | -9364.55 | 0.00 | 0.0000 |
| breakeven_192 | Breakeven 192 | 194.65 | 94.65% | -9464.88 | 0.00 | 0.0000 |
| breakeven_193 | Breakeven 193 | 195.65 | 95.65% | -9565.22 | 0.00 | 0.0000 |
| breakeven_194 | Breakeven 194 | 196.66 | 96.66% | -9665.55 | 0.00 | 0.0000 |
| breakeven_195 | Breakeven 195 | 197.66 | 97.66% | -9765.89 | 0.00 | 0.0000 |
| breakeven_196 | Breakeven 196 | 198.66 | 98.66% | -9866.22 | 0.00 | 0.0000 |
| breakeven_197 | Breakeven 197 | 199.67 | 99.67% | -9966.56 | 0.00 | 0.0000 |
| breakeven_198 | Breakeven 198 | 200.67 | 100.67% | -10066.89 | 0.00 | 0.0000 |
| breakeven_199 | Breakeven 199 | 201.67 | 101.67% | -10167.22 | 0.00 | 0.0000 |
| breakeven_200 | Breakeven 200 | 202.68 | 102.68% | -10267.56 | 0.00 | 0.0000 |
| breakeven_201 | Breakeven 201 | 203.68 | 103.68% | -10367.89 | 0.00 | 0.0000 |
| breakeven_202 | Breakeven 202 | 204.68 | 104.68% | -10468.23 | 0.00 | 0.0000 |
| breakeven_203 | Breakeven 203 | 205.69 | 105.69% | -10568.56 | 0.00 | 0.0000 |
| breakeven_204 | Breakeven 204 | 206.69 | 106.69% | -10668.90 | 0.00 | 0.0000 |
| breakeven_205 | Breakeven 205 | 207.69 | 107.69% | -10769.23 | 0.00 | 0.0000 |
| breakeven_206 | Breakeven 206 | 208.70 | 108.70% | -10869.57 | 0.00 | 0.0000 |
| breakeven_207 | Breakeven 207 | 209.70 | 109.70% | -10969.90 | 0.00 | 0.0000 |
| breakeven_208 | Breakeven 208 | 210.70 | 110.70% | -11070.23 | 0.00 | 0.0000 |
| breakeven_209 | Breakeven 209 | 211.71 | 111.71% | -11170.57 | 0.00 | 0.0000 |
| breakeven_210 | Breakeven 210 | 212.71 | 112.71% | -11270.90 | 0.00 | 0.0000 |
| breakeven_211 | Breakeven 211 | 213.71 | 113.71% | -11371.24 | 0.00 | 0.0000 |
| breakeven_212 | Breakeven 212 | 214.72 | 114.72% | -11471.57 | 0.00 | 0.0000 |
| breakeven_213 | Breakeven 213 | 215.72 | 115.72% | -11571.91 | 0.00 | 0.0000 |
| breakeven_214 | Breakeven 214 | 216.72 | 116.72% | -11672.24 | 0.00 | 0.0000 |
| breakeven_215 | Breakeven 215 | 217.73 | 117.73% | -11772.58 | 0.00 | 0.0000 |
| breakeven_216 | Breakeven 216 | 218.73 | 118.73% | -11872.91 | 0.00 | 0.0000 |
| breakeven_217 | Breakeven 217 | 219.73 | 119.73% | -11973.24 | 0.00 | 0.0000 |
| breakeven_218 | Breakeven 218 | 220.74 | 120.74% | -12073.58 | 0.00 | 0.0000 |
| breakeven_219 | Breakeven 219 | 221.74 | 121.74% | -12173.91 | 0.00 | 0.0000 |
| breakeven_220 | Breakeven 220 | 222.74 | 122.74% | -12274.25 | 0.00 | 0.0000 |
| breakeven_221 | Breakeven 221 | 223.75 | 123.75% | -12374.58 | 0.00 | 0.0000 |
| breakeven_222 | Breakeven 222 | 224.75 | 124.75% | -12474.92 | 0.00 | 0.0000 |
| breakeven_223 | Breakeven 223 | 225.75 | 125.75% | -12575.25 | 0.00 | 0.0000 |
| breakeven_224 | Breakeven 224 | 226.76 | 126.76% | -12675.59 | 0.00 | 0.0000 |
| breakeven_225 | Breakeven 225 | 227.76 | 127.76% | -12775.92 | 0.00 | 0.0000 |
| breakeven_226 | Breakeven 226 | 228.76 | 128.76% | -12876.25 | 0.00 | 0.0000 |
| breakeven_227 | Breakeven 227 | 229.77 | 129.77% | -12976.59 | 0.00 | 0.0000 |
| breakeven_228 | Breakeven 228 | 230.77 | 130.77% | -13076.92 | 0.00 | 0.0000 |
| breakeven_229 | Breakeven 229 | 231.77 | 131.77% | -13177.26 | 0.00 | 0.0000 |
| breakeven_230 | Breakeven 230 | 232.78 | 132.78% | -13277.59 | 0.00 | 0.0000 |
| breakeven_231 | Breakeven 231 | 233.78 | 133.78% | -13377.93 | 0.00 | 0.0000 |
| breakeven_232 | Breakeven 232 | 234.78 | 134.78% | -13478.26 | 0.00 | 0.0000 |
| breakeven_233 | Breakeven 233 | 235.79 | 135.79% | -13578.60 | 0.00 | 0.0000 |
| breakeven_234 | Breakeven 234 | 236.79 | 136.79% | -13678.93 | 0.00 | 0.0000 |
| breakeven_235 | Breakeven 235 | 237.79 | 137.79% | -13779.26 | 0.00 | 0.0000 |
| breakeven_236 | Breakeven 236 | 238.80 | 138.80% | -13879.60 | 0.00 | 0.0000 |
| breakeven_237 | Breakeven 237 | 239.80 | 139.80% | -13979.93 | 0.00 | 0.0000 |
| breakeven_238 | Breakeven 238 | 240.80 | 140.80% | -14080.27 | 0.00 | 0.0000 |
| breakeven_239 | Breakeven 239 | 241.81 | 141.81% | -14180.60 | 0.00 | 0.0000 |
| breakeven_240 | Breakeven 240 | 242.81 | 142.81% | -14280.94 | 0.00 | 0.0000 |
| breakeven_241 | Breakeven 241 | 243.81 | 143.81% | -14381.27 | 0.00 | 0.0000 |
| breakeven_242 | Breakeven 242 | 244.82 | 144.82% | -14481.61 | 0.00 | 0.0000 |
| breakeven_243 | Breakeven 243 | 245.82 | 145.82% | -14581.94 | 0.00 | 0.0000 |
| breakeven_244 | Breakeven 244 | 246.82 | 146.82% | -14682.27 | 0.00 | 0.0000 |
| breakeven_245 | Breakeven 245 | 247.83 | 147.83% | -14782.61 | 0.00 | 0.0000 |
| breakeven_246 | Breakeven 246 | 248.83 | 148.83% | -14882.94 | 0.00 | 0.0000 |
| breakeven_247 | Breakeven 247 | 249.83 | 149.83% | -14983.28 | 0.00 | 0.0000 |
| breakeven_248 | Breakeven 248 | 250.84 | 150.84% | -15083.61 | 0.00 | 0.0000 |
| breakeven_249 | Breakeven 249 | 251.84 | 151.84% | -15183.95 | 0.00 | 0.0000 |
| breakeven_250 | Breakeven 250 | 252.84 | 152.84% | -15284.28 | 0.00 | 0.0000 |
| breakeven_251 | Breakeven 251 | 253.85 | 153.85% | -15384.62 | 0.00 | 0.0000 |
| breakeven_252 | Breakeven 252 | 254.85 | 154.85% | -15484.95 | 0.00 | 0.0000 |
| breakeven_253 | Breakeven 253 | 255.85 | 155.85% | -15585.28 | 0.00 | 0.0000 |
| breakeven_254 | Breakeven 254 | 256.86 | 156.86% | -15685.62 | 0.00 | 0.0000 |
| breakeven_255 | Breakeven 255 | 257.86 | 157.86% | -15785.95 | 0.00 | 0.0000 |
| breakeven_256 | Breakeven 256 | 258.86 | 158.86% | -15886.29 | 0.00 | 0.0000 |
| breakeven_257 | Breakeven 257 | 259.87 | 159.87% | -15986.62 | 0.00 | 0.0000 |
| breakeven_258 | Breakeven 258 | 260.87 | 160.87% | -16086.96 | 0.00 | 0.0000 |
| breakeven_259 | Breakeven 259 | 261.87 | 161.87% | -16187.29 | 0.00 | 0.0000 |
| breakeven_260 | Breakeven 260 | 262.88 | 162.88% | -16287.63 | 0.00 | 0.0000 |
| breakeven_261 | Breakeven 261 | 263.88 | 163.88% | -16387.96 | 0.00 | 0.0000 |
| breakeven_262 | Breakeven 262 | 264.88 | 164.88% | -16488.29 | 0.00 | 0.0000 |
| breakeven_263 | Breakeven 263 | 265.89 | 165.89% | -16588.63 | 0.00 | 0.0000 |
| breakeven_264 | Breakeven 264 | 266.89 | 166.89% | -16688.96 | 0.00 | 0.0000 |
| breakeven_265 | Breakeven 265 | 267.89 | 167.89% | -16789.30 | 0.00 | 0.0000 |
| breakeven_266 | Breakeven 266 | 268.90 | 168.90% | -16889.63 | 0.00 | 0.0000 |
| breakeven_267 | Breakeven 267 | 269.90 | 169.90% | -16989.97 | 0.00 | 0.0000 |
| breakeven_268 | Breakeven 268 | 270.90 | 170.90% | -17090.30 | 0.00 | 0.0000 |
| breakeven_269 | Breakeven 269 | 271.91 | 171.91% | -17190.64 | 0.00 | 0.0000 |
| breakeven_270 | Breakeven 270 | 272.91 | 172.91% | -17290.97 | 0.00 | 0.0000 |
| breakeven_271 | Breakeven 271 | 273.91 | 173.91% | -17391.30 | 0.00 | 0.0000 |
| breakeven_272 | Breakeven 272 | 274.92 | 174.92% | -17491.64 | 0.00 | 0.0000 |
| breakeven_273 | Breakeven 273 | 275.92 | 175.92% | -17591.97 | 0.00 | 0.0000 |
| breakeven_274 | Breakeven 274 | 276.92 | 176.92% | -17692.31 | 0.00 | 0.0000 |
| breakeven_275 | Breakeven 275 | 277.93 | 177.93% | -17792.64 | 0.00 | 0.0000 |
| breakeven_276 | Breakeven 276 | 278.93 | 178.93% | -17892.98 | 0.00 | 0.0000 |
| breakeven_277 | Breakeven 277 | 279.93 | 179.93% | -17993.31 | 0.00 | 0.0000 |
| breakeven_278 | Breakeven 278 | 280.94 | 180.94% | -18093.65 | 0.00 | 0.0000 |
| breakeven_279 | Breakeven 279 | 281.94 | 181.94% | -18193.98 | 0.00 | 0.0000 |
| breakeven_280 | Breakeven 280 | 282.94 | 182.94% | -18294.31 | 0.00 | 0.0000 |
| breakeven_281 | Breakeven 281 | 283.95 | 183.95% | -18394.65 | 0.00 | 0.0000 |
| breakeven_282 | Breakeven 282 | 284.95 | 184.95% | -18494.98 | 0.00 | 0.0000 |
| breakeven_283 | Breakeven 283 | 285.95 | 185.95% | -18595.32 | 0.00 | 0.0000 |
| breakeven_284 | Breakeven 284 | 286.96 | 186.96% | -18695.65 | 0.00 | 0.0000 |
| breakeven_285 | Breakeven 285 | 287.96 | 187.96% | -18795.99 | 0.00 | 0.0000 |
| breakeven_286 | Breakeven 286 | 288.96 | 188.96% | -18896.32 | 0.00 | 0.0000 |
| breakeven_287 | Breakeven 287 | 289.97 | 189.97% | -18996.66 | 0.00 | 0.0000 |
| breakeven_288 | Breakeven 288 | 290.97 | 190.97% | -19096.99 | 0.00 | 0.0000 |
| breakeven_289 | Breakeven 289 | 291.97 | 191.97% | -19197.32 | 0.00 | 0.0000 |
| breakeven_290 | Breakeven 290 | 292.98 | 192.98% | -19297.66 | 0.00 | 0.0000 |
| breakeven_291 | Breakeven 291 | 293.98 | 193.98% | -19397.99 | 0.00 | 0.0000 |
| breakeven_292 | Breakeven 292 | 294.98 | 194.98% | -19498.33 | 0.00 | 0.0000 |
| breakeven_293 | Breakeven 293 | 295.99 | 195.99% | -19598.66 | 0.00 | 0.0000 |
| breakeven_294 | Breakeven 294 | 296.99 | 196.99% | -19699.00 | 0.00 | 0.0000 |
| breakeven_295 | Breakeven 295 | 297.99 | 197.99% | -19799.33 | 0.00 | 0.0000 |
| breakeven_296 | Breakeven 296 | 299.00 | 199.00% | -19899.67 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | 0.00 | 0.0000 |

---

### Conversion (ID=63) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: COL_EQ
- Margin Classification: COL_EQ

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: []
- Options Max PnL: 10000.0
- Options Min PnL: -20000.0
- Combined Max PnL: 5000.0
- Combined Min PnL: 5000.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $10,000.00 | $5,000.00 |
| Max Loss | Unlimited | $5,000.00 |
| Risk Reward | 0.50x | 1.00x |
| Capital Basis | $5,250.00 | $10,250.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 5250.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.003285
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Scenario @ 50.00 | 5000.00 | 0.00 | 5000.00 | 0.9524 | 0.4878 |
| 85.00 | Downside (15%) | 1500.00 | 3500.00 | 5000.00 | 0.2857 | 0.4878 |
| 100.00 | Current Market Price | 0.00 | 5000.00 | 5000.00 | 0.0000 | 0.4878 |
| 115.00 | Upside (15%) | -1500.00 | 6500.00 | 5000.00 | -0.2857 | 0.4878 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 10000.00 | 5000.00 | 0.4878 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1500.00 | 5000.00 | 0.4878 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 0.4878 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 0.4878 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1500.00 | 5000.00 | 0.4878 |
| infinity | Stock to Infinity | — | — | Unlimited | 5000.00 | 0.4878 |

---

### Conversion (ID=63) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: COL_EQ
- Margin Classification: COL_EQ

**Legs:**

| # | Kind | Position | Strike | Premium | Multiplier |
|---|------|----------|--------|---------|------------|
| 1 | PUT | Long 1 | 100.00 | 2.50 | 100 |
| 2 | CALL | Short 1 | 100.00 | 2.50 | 100 |

**Payoff:**

- Grid Size: 301 points
- Strikes: [100.0]
- Breakevens: []
- Options Max PnL: 10000.0
- Options Min PnL: -20000.0
- Combined Max PnL: -1500.0
- Combined Min PnL: -1500.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $10,000.00 | -$1,500.00 |
| Max Loss | Unlimited | -$1,500.00 |
| Risk Reward | 0.50x | 1.00x |
| Capital Basis | $5,250.00 | $16,750.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 5250.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: 0.479291
- P(25% Max Profit): 0.003285
- P(50% Max Profit): 0.0
- P(100% Max Profit): 0.0
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 1500.00 | -3000.00 | -1500.00 | 0.2857 | -0.0896 |
| 100.00 | Current Market Price | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.0896 |
| 115.00 | Upside (15%) | -1500.00 | 0.00 | -1500.00 | -0.2857 | -0.0896 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 10000.00 | -1500.00 | -0.0896 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1500.00 | -1500.00 | -0.0896 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.0896 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.0896 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1500.00 | -1500.00 | -0.0896 |
| infinity | Stock to Infinity | — | — | Unlimited | -1500.00 | -0.0896 |

---

