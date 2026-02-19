# Calculation Engine Audit Report

Generated: 2026-02-18

## Executive Summary

| Metric | Value |
|--------|-------|
| Strategies tested | 63 |
| Scenarios per strategy | 4 |
| Total runs | 252 |
| Build errors (crash) | 0 |
| Total checks executed | 25235 |
| Checks PASSED | 25230 |
| Checks FAILED | 5 |
| Pass rate | 100.0% |

## Category Summary

| Cat | Category Name | Total | Passed | Failed | Rate |
|-----|--------------|-------|--------|--------|------|
| A | Payoff Grid Integrity | 1992 | 1989 | 3 | 99.8% |
| B | Breakeven Validation | 1047 | 1047 | 0 | 100.0% |
| C | Max Profit / Max Loss | 1255 | 1255 | 0 | 100.0% |
| D | Net Premium & Cost/Credit | 1008 | 1008 | 0 | 100.0% |
| E | Stock P&L | 756 | 756 | 0 | 100.0% |
| F | Cross-Scenario Consistency | 2650 | 2649 | 1 | 100.0% |
| G | Capital at Risk & ROI | 1472 | 1472 | 0 | 100.0% |
| H | Key Levels | 1501 | 1501 | 0 | 100.0% |
| I | Pipeline Map Issues | 1008 | 1008 | 0 | 100.0% |
| J | Known Bugs | 12546 | 12545 | 1 | 100.0% |

## Failures by Check ID

### BUG_04 (1 failures)

- **Custom Strategy** [options_only]: Sentinel levels: zero=False, infinity=False

### CS_01 (1 failures)

- **Custom Strategy** [options_only]: Scenario table is empty

### PG_01 (1 failures)

- **Custom Strategy** [options_only]: Grid start=EMPTY, expected 0

### PG_02 (1 failures)

- **Custom Strategy** [options_only]: Grid end=EMPTY, expected ~300.0

### PG_05 (1 failures)

- **Custom Strategy** [options_only]: Grid size=0, expected >=300

## Check ID Statistics

| Check ID | Total | Passed | Failed | Description |
|----------|-------|--------|--------|-------------|
| BE_01 | 252 | 252 | 0 | Breakevens sorted |
| BE_02 | 265 | 265 | 0 | Breakevens within grid range |
| BE_03 | 265 | 265 | 0 | PnL ≈ 0 at breakeven |
| BE_04 | 265 | 265 | 0 | Sign change around breakeven |
| BUG_01 | 252 | 252 | 0 | No division-by-zero crash |
| BUG_02 | 252 | 252 | 0 | All-short capital basis > 0 |
| BUG_03 | 252 | 252 | 0 | Scenario table populated |
| BUG_04 | 252 | 251 | 1 | Sentinel rows present |
| BUG_05 | 252 | 252 | 0 | PoP in [0, 1] |
| BUG_06 | 252 | 252 | 0 | Risk/Reward present |
| BUG_07 | 11034 | 11034 | 0 | No NaN in key level fields |
| CB_01 | 252 | 252 | 0 | Capital basis > 0 |
| CB_02 | 252 | 252 | 0 | Combined basis ≥ option basis |
| CS_01 | 252 | 251 | 1 | Spot in scenario table |
| CS_02 | 480 | 480 | 0 | Strikes in scenario table |
| CS_03 | 265 | 265 | 0 | Breakevens in scenario table |
| CS_04 | 265 | 265 | 0 | PnL ≈ 0 at breakeven in scenario |
| CS_05 | 1388 | 1388 | 0 | Scenario opt+stk = combined |
| KL_01 | 252 | 252 | 0 | Spot in key levels |
| KL_02 | 480 | 480 | 0 | Strikes in key levels |
| KL_03 | 265 | 265 | 0 | Breakevens in key levels |
| KL_04 | 252 | 252 | 0 | Key levels sorted by price |
| KL_05 | 252 | 252 | 0 | Key level IDs unique |
| ML_01 | 251 | 251 | 0 | Options max loss unlimited flag |
| ML_02 | 251 | 251 | 0 | Combined max loss unlimited flag |
| MP_01 | 251 | 251 | 0 | Options max profit unlimited flag |
| MP_02 | 251 | 251 | 0 | Combined max profit unlimited flag |
| MP_03 | 251 | 251 | 0 | Options max profit ≥ 0 |
| NP_01 | 252 | 252 | 0 | Net premium per-share formula |
| NP_02 | 252 | 252 | 0 | Net premium total formula |
| NP_03 | 252 | 252 | 0 | Cost/Credit text matches sign |
| NP_04 | 252 | 252 | 0 | Net Prem/Share present |
| PG_01 | 252 | 251 | 1 | Grid starts at 0 |
| PG_02 | 252 | 251 | 1 | Grid ends at 3×spot |
| PG_03 | 252 | 252 | 0 | Grid monotonically increasing |
| PG_04 | 480 | 480 | 0 | All strikes in grid |
| PG_05 | 252 | 251 | 1 | Grid has ≥300 points |
| PG_06 | 252 | 252 | 0 | PnL array lengths match grid |
| PG_07 | 252 | 252 | 0 | combined = options + stock PnL |
| PI_01 | 252 | 252 | 0 | Stock PnL: direct vs derived |
| PI_02 | 252 | 252 | 0 | PoP was computed |
| PI_03 | 252 | 252 | 0 | Unlimited flags consistent |
| PI_04 | 252 | 252 | 0 | Net premium per share present |
| ROI_01 | 716 | 716 | 0 | ROI values finite |
| ROI_02 | 252 | 252 | 0 | No NaN/Inf in ROI |
| SP_01 | 252 | 252 | 0 | Zero stock → zero stock PnL |
| SP_02 | 252 | 252 | 0 | Stock PnL formula correctness |
| SP_03 | 252 | 252 | 0 | Stock PnL linearity |

## All Failures (Detailed)

Total: 5 failures

### Custom Strategy [options_only]

- **PG_01**: Grid start=EMPTY, expected 0
- **PG_02**: Grid end=EMPTY, expected ~300.0
- **PG_05**: Grid size=0, expected >=300
- **CS_01**: Scenario table is empty
- **BUG_04**: Sentinel levels: zero=False, infinity=False

## Numerical Results (Fact-Check Data)

Every computed value for each strategy × scenario run.

### Custom Strategy (ID=1) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: CUSTOM
- Margin Classification: unknown

**Payoff:**

- Grid Size: 0 points
- Strikes: []
- Breakevens: []
- Options Max PnL: None
- Options Min PnL: None
- Combined Max PnL: None
- Combined Min PnL: None

**Net Premium:**

- Per Share: 0
- Total: 0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | $0.00 |
| Max Loss | $0.00 | $0.00 |
| Risk Reward | N/A | N/A |
| Capital at Risk | $0.00 | $0.00 |
| Cost Credit | $0.00 | $0.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 0.0 | — |

**Probabilities:**

- PoP (raw): 0.0
- Assignment Prob: None
- P(25% Max Profit): None
- P(50% Max Profit): None
- P(100% Max Profit): None
- IV Used: None

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| spot | Current Market Price | 100.00 | 0.00% | — | — | — |

---

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
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $1.00 | $10,001.00 |
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
| infinity | Stock to Infinity | — | — | 0.00 | Unlimited | Unlimited |

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
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $1.00 | $5,001.00 |
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
| infinity | Stock to Infinity | — | — | 0.00 | Unlimited | Unlimited |

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
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $1.00 | $11,501.00 |
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
| infinity | Stock to Infinity | — | — | 0.00 | Unlimited | Unlimited |

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
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $1.00 | $10,001.00 |
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
| infinity | Stock to Infinity | — | — | 0.00 | Unlimited | Unlimited |

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
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $1.00 | $10,001.00 |
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
| infinity | Stock to Infinity | — | — | 0.00 | Unlimited | Unlimited |

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
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $1.00 | $5,001.00 |
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
| infinity | Stock to Infinity | — | — | 0.00 | Unlimited | Unlimited |

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
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $1.00 | $11,501.00 |
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
| infinity | Stock to Infinity | — | — | 0.00 | Unlimited | Unlimited |

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
| Capital at Risk | $1.00 | $10,001.00 |
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
| infinity | Stock to Infinity | — | — | 0.00 | Unlimited | Unlimited |

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
| Capital at Risk | $1.00 | $10,001.00 |
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
| infinity | Stock to Infinity | — | — | 0.00 | Unlimited | Unlimited |

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
| Capital at Risk | $1.00 | $5,001.00 |
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
| infinity | Stock to Infinity | — | — | 0.00 | Unlimited | Unlimited |

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
| Capital at Risk | $1.00 | $11,501.00 |
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
| 115.00 | Upside (15%) | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | 11500.00 | 0.9999 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | 3000.00 | 0.2608 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 1500.00 | 0.1304 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 115.00 | 15.00% | 0.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 0.00 | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $250.00 | $250.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $250.00 | $10,250.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $250.00 | $5,250.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $250.00 | $11,750.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $2,250.00 | $2,250.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $5,000.00 | $15,000.00 |
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
| Capital at Risk | $5,000.00 | $10,000.00 |
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
| Capital at Risk | $5,000.00 | $16,500.00 |
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
| Capital at Risk | $250.00 | $250.00 |
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
| infinity | Stock to Infinity | — | — | -250.00 | -250.00 | -1.0000 |

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
| Risk Reward | 39.00x | Unlimited |
| Capital at Risk | $5,250.00 | $15,250.00 |
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
| infinity | Stock to Infinity | — | — | -250.00 | Unlimited | Unlimited |

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
| Risk Reward | 39.00x | Unlimited |
| Capital at Risk | $5,250.00 | $10,250.00 |
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
| infinity | Stock to Infinity | — | — | -250.00 | Unlimited | Unlimited |

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
| Risk Reward | 39.00x | Unlimited |
| Capital at Risk | $5,250.00 | $16,750.00 |
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
| infinity | Stock to Infinity | — | — | -250.00 | Unlimited | Unlimited |

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
| Capital at Risk | $10,000.00 | $10,000.00 |
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
| Risk Reward | 0.03x | Unlimited |
| Capital at Risk | $2,250.00 | $12,250.00 |
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
| infinity | Stock to Infinity | — | — | 250.00 | Unlimited | Unlimited |

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
| Risk Reward | 0.03x | Unlimited |
| Capital at Risk | $2,250.00 | $7,250.00 |
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
| infinity | Stock to Infinity | — | — | 250.00 | Unlimited | Unlimited |

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
| Risk Reward | 0.03x | Unlimited |
| Capital at Risk | $2,250.00 | $13,750.00 |
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
| infinity | Stock to Infinity | — | — | 250.00 | Unlimited | Unlimited |

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
| Max Loss | Unlimited | -$9,810.00 |
| Risk Reward | 0.01x | 0.10x |
| Capital at Risk | $5,000.00 | $15,000.00 |
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
| 98.10 | Breakeven 1 | 190.00 | -190.00 | 0.00 | 0.0380 | 0.0000 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0380 | 0.0127 |
| 108.00 | Strike | 190.00 | 800.00 | 990.00 | 0.0380 | 0.0660 |
| 115.00 | Upside (15%) | -510.00 | 1500.00 | 990.00 | -0.1020 | 0.0660 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 190.00 | -9810.00 | -0.6540 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 190.00 | -1310.00 | -0.0873 |
| breakeven_1 | Breakeven 1 | 98.10 | -1.90% | 190.00 | 0.00 | 0.0000 |
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
| Max Loss | Unlimited | -$9,810.00 |
| Risk Reward | 0.01x | 0.10x |
| Capital at Risk | $5,000.00 | $15,000.00 |
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
| 98.10 | Breakeven 1 | 190.00 | -190.00 | 0.00 | 0.0380 | 0.0000 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0380 | 0.0127 |
| 108.00 | Strike | 190.00 | 800.00 | 990.00 | 0.0380 | 0.0660 |
| 115.00 | Upside (15%) | -510.00 | 1500.00 | 990.00 | -0.1020 | 0.0660 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 190.00 | -9810.00 | -0.6540 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 190.00 | -1310.00 | -0.0873 |
| breakeven_1 | Breakeven 1 | 98.10 | -1.90% | 190.00 | 0.00 | 0.0000 |
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
| Max Loss | Unlimited | -$4,810.00 |
| Risk Reward | 0.01x | 1.25x |
| Capital at Risk | $5,000.00 | $10,000.00 |
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
| Max Loss | Unlimited | -$11,310.00 |
| Risk Reward | 0.01x | 0.05x |
| Capital at Risk | $5,000.00 | $16,500.00 |
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
| Capital at Risk | $1,390.00 | $11,390.00 |
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
| 101.90 | Breakeven 1 | 190.00 | -190.00 | 0.00 | 0.0211 | 0.0000 |
| 115.00 | Upside (15%) | 190.00 | -1500.00 | -1310.00 | 0.0211 | -0.0689 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9010.00 | 990.00 | 0.0869 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -510.00 | 990.00 | 0.0521 |
| strike_1 | Strike | 92.00 | -8.00% | 190.00 | 990.00 | 0.0521 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0100 |
| breakeven_1 | Breakeven 1 | 101.90 | 1.90% | 190.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 190.00 | -1310.00 | -0.0689 |
| infinity | Stock to Infinity | — | — | 190.00 | Unlimited | Unlimited |

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
| Capital at Risk | $1,390.00 | $11,390.00 |
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
| 101.90 | Breakeven 1 | 190.00 | -190.00 | 0.00 | 0.0211 | 0.0000 |
| 115.00 | Upside (15%) | 190.00 | -1500.00 | -1310.00 | 0.0211 | -0.0689 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9010.00 | 990.00 | 0.0869 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -510.00 | 990.00 | 0.0521 |
| strike_1 | Strike | 92.00 | -8.00% | 190.00 | 990.00 | 0.0521 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0100 |
| breakeven_1 | Breakeven 1 | 101.90 | 1.90% | 190.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 190.00 | -1310.00 | -0.0689 |
| infinity | Stock to Infinity | — | — | 190.00 | Unlimited | Unlimited |

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
| Capital at Risk | $1,390.00 | $6,390.00 |
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
| infinity | Stock to Infinity | — | — | 190.00 | Unlimited | Unlimited |

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
| Capital at Risk | $1,390.00 | $12,890.00 |
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
| 116.90 | Breakeven 1 | 190.00 | -190.00 | 0.00 | 0.0211 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9010.00 | 2490.00 | 0.1932 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -510.00 | 2490.00 | 0.1214 |
| strike_1 | Strike | 92.00 | -8.00% | 190.00 | 2490.00 | 0.1214 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 1690.00 | 0.0824 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 190.00 | 190.00 | 0.0093 |
| breakeven_1 | Breakeven 1 | 116.90 | 16.90% | 190.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 190.00 | Unlimited | Unlimited |

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
| Max Profit | Unlimited | $9,810.00 |
| Max Loss | -$190.00 | Unlimited |
| Risk Reward | Unlimited | 9.91x |
| Capital at Risk | $190.00 | $10,190.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | -990.00 | -0.0972 |

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
| Max Profit | Unlimited | $9,810.00 |
| Max Loss | -$190.00 | Unlimited |
| Risk Reward | Unlimited | 9.91x |
| Capital at Risk | $190.00 | $10,190.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | -990.00 | -0.0972 |

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
| Max Profit | Unlimited | $4,810.00 |
| Max Loss | -$190.00 | Unlimited |
| Risk Reward | Unlimited | 0.80x |
| Capital at Risk | $190.00 | $5,190.00 |
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
| 48.10 | Breakeven 1 | -190.00 | 190.00 | 0.00 | -1.0000 | 0.0000 |
| 50.00 | Scenario @ 50.00 | -190.00 | 0.00 | -190.00 | -1.0000 | -0.0366 |
| 85.00 | Downside (15%) | -190.00 | -3500.00 | -3690.00 | -1.0000 | -0.7110 |
| 100.00 | Current Market Price | -190.00 | -5000.00 | -5190.00 | -1.0000 | -1.0000 |
| 108.00 | Strike | -190.00 | -5800.00 | -5990.00 | -1.0000 | -1.1541 |
| 115.00 | Upside (15%) | 510.00 | -6500.00 | -5990.00 | 2.6842 | -1.1541 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -190.00 | 4810.00 | 0.9268 |
| breakeven_1 | Breakeven 1 | 48.10 | -51.90% | -190.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -190.00 | -3690.00 | -0.7110 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | -5190.00 | -1.0000 |
| strike_1 | Strike | 108.00 | 8.00% | -190.00 | -5990.00 | -1.1541 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 510.00 | -5990.00 | -1.1541 |
| infinity | Stock to Infinity | — | — | Unlimited | -5990.00 | -1.1541 |

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
| Max Profit | Unlimited | $11,310.00 |
| Max Loss | -$190.00 | Unlimited |
| Risk Reward | Unlimited | 22.18x |
| Capital at Risk | $190.00 | $11,690.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | 510.00 | 0.0436 |

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
| Max Loss | Unlimited | -$990.00 |
| Risk Reward | 47.42x | Unlimited |
| Capital at Risk | $5,190.00 | $15,190.00 |
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
| infinity | Stock to Infinity | — | — | -190.00 | Unlimited | Unlimited |

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
| Max Loss | Unlimited | -$990.00 |
| Risk Reward | 47.42x | Unlimited |
| Capital at Risk | $5,190.00 | $15,190.00 |
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
| infinity | Stock to Infinity | — | — | -190.00 | Unlimited | Unlimited |

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
| Max Loss | Unlimited | $4,010.00 |
| Risk Reward | 47.42x | Unlimited |
| Capital at Risk | $5,190.00 | $10,190.00 |
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
| infinity | Stock to Infinity | — | — | -190.00 | Unlimited | Unlimited |

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
| Max Loss | Unlimited | -$2,490.00 |
| Risk Reward | 47.42x | Unlimited |
| Capital at Risk | $5,190.00 | $16,690.00 |
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
| infinity | Stock to Infinity | — | — | -190.00 | Unlimited | Unlimited |

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
| Max Loss | Unlimited | -$800.00 |
| Risk Reward | 0.48x | 1.00x |
| Capital at Risk | $5,190.00 | $15,190.00 |
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
| Max Loss | Unlimited | -$800.00 |
| Risk Reward | 0.48x | 1.00x |
| Capital at Risk | $5,190.00 | $15,190.00 |
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
| Max Loss | Unlimited | $4,200.00 |
| Risk Reward | 0.48x | 1.38x |
| Capital at Risk | $5,190.00 | $10,190.00 |
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
| Max Loss | Unlimited | -$2,300.00 |
| Risk Reward | 0.48x | 0.30x |
| Capital at Risk | $5,190.00 | $16,690.00 |
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
| Capital at Risk | $800.00 | $800.00 |
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
| Risk Reward | 1.00x | Unlimited |
| Capital at Risk | $1,390.00 | $11,390.00 |
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
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | 800.00 | 800.00 | 1600.00 | 1.0000 | 0.1481 |
| 115.00 | Upside (15%) | 800.00 | 1500.00 | 2300.00 | 1.0000 | 0.2130 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -800.00 | -10800.00 | -0.9482 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -800.00 | -2300.00 | -0.2130 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -800.00 | -1600.00 | -0.1481 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 800.00 | 1600.00 | 0.1481 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 800.00 | 2300.00 | 0.2130 |
| infinity | Stock to Infinity | — | — | 800.00 | Unlimited | Unlimited |

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
| Risk Reward | 1.00x | Unlimited |
| Capital at Risk | $1,390.00 | $6,390.00 |
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
| 100.00 | Current Market Price | 0.00 | 5000.00 | 5000.00 | 0.0000 | 0.8621 |
| 108.00 | Upper Strike | 800.00 | 5800.00 | 6600.00 | 1.0000 | 1.1379 |
| 115.00 | Upside (15%) | 800.00 | 6500.00 | 7300.00 | 1.0000 | 1.2586 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -800.00 | -5800.00 | -0.9077 |
| breakeven_1 | Breakeven 1 | 58.00 | -42.00% | -800.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -800.00 | 2700.00 | 0.4655 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -800.00 | 3400.00 | 0.5862 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 0.8621 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 800.00 | 6600.00 | 1.1379 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 800.00 | 7300.00 | 1.2586 |
| infinity | Stock to Infinity | — | — | 800.00 | Unlimited | Unlimited |

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
| Risk Reward | 1.00x | Unlimited |
| Capital at Risk | $1,390.00 | $12,890.00 |
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
| 100.00 | Current Market Price | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.1220 |
| 107.50 | Breakeven 1 | 750.00 | -750.00 | 0.00 | 0.9375 | 0.0000 |
| 108.00 | Upper Strike | 800.00 | -700.00 | 100.00 | 1.0000 | 0.0081 |
| 115.00 | Upside (15%) | 800.00 | 0.00 | 800.00 | 1.0000 | 0.0650 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -800.00 | -12300.00 | -0.9542 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -800.00 | -3800.00 | -0.3089 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -800.00 | -3100.00 | -0.2520 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.1220 |
| breakeven_1 | Breakeven 1 | 107.50 | 7.50% | 750.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 800.00 | 100.00 | 0.0081 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 800.00 | 800.00 | 0.0650 |
| infinity | Stock to Infinity | — | — | 800.00 | Unlimited | Unlimited |

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
| Capital at Risk | $800.00 | $800.00 |
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
- Breakevens: [100.0]
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
| Risk Reward | 1.00x | Unlimited |
| Capital at Risk | $1,390.00 | $11,390.00 |
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
| 92.00 | Lower Strike | 800.00 | -800.00 | 0.00 | 1.0000 | 0.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | -800.00 | 800.00 | 0.00 | -1.0000 | 0.0000 |
| 115.00 | Upside (15%) | -800.00 | 1500.00 | 700.00 | -1.0000 | 0.0648 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 800.00 | -9200.00 | -0.8077 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 800.00 | -700.00 | -0.0648 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 800.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -800.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -800.00 | 700.00 | 0.0648 |
| infinity | Stock to Infinity | — | — | -800.00 | Unlimited | Unlimited |

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
| Risk Reward | 1.00x | Unlimited |
| Capital at Risk | $1,390.00 | $6,390.00 |
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
| 100.00 | Current Market Price | 0.00 | 5000.00 | 5000.00 | 0.0000 | 0.8621 |
| 108.00 | Upper Strike | -800.00 | 5800.00 | 5000.00 | -1.0000 | 0.8621 |
| 115.00 | Upside (15%) | -800.00 | 6500.00 | 5700.00 | -1.0000 | 0.9828 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 800.00 | -4200.00 | -0.6573 |
| breakeven_1 | Breakeven 1 | 42.00 | -58.00% | 800.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 800.00 | 4300.00 | 0.7414 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 800.00 | 5000.00 | 0.8621 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 0.8621 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -800.00 | 5000.00 | 0.8621 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -800.00 | 5700.00 | 0.9828 |
| infinity | Stock to Infinity | — | — | -800.00 | Unlimited | Unlimited |

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
| Risk Reward | 1.00x | Unlimited |
| Capital at Risk | $1,390.00 | $12,890.00 |
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
| 100.00 | Current Market Price | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.1220 |
| 108.00 | Upper Strike | -800.00 | -700.00 | -1500.00 | -1.0000 | -0.1220 |
| 115.00 | Upside (15%) | -800.00 | 0.00 | -800.00 | -1.0000 | -0.0650 |
| 123.00 | Breakeven 1 | -800.00 | 800.00 | 0.00 | -1.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 800.00 | -10700.00 | -0.8301 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 800.00 | -2200.00 | -0.1789 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 800.00 | -1500.00 | -0.1220 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.1220 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -800.00 | -1500.00 | -0.1220 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -800.00 | -800.00 | -0.0650 |
| breakeven_1 | Breakeven 1 | 123.00 | 23.00% | -800.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | -800.00 | Unlimited | Unlimited |

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
| Capital at Risk | $800.00 | $800.00 |
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
- Breakevens: [100.0]
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
| Risk Reward | 1.00x | Unlimited |
| Capital at Risk | $2,990.00 | $12,990.00 |
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
| 92.00 | Lower Strike | 800.00 | -800.00 | 0.00 | 1.0000 | 0.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | -800.00 | 800.00 | 0.00 | -1.0000 | 0.0000 |
| 115.00 | Upside (15%) | -800.00 | 1500.00 | 700.00 | -1.0000 | 0.0648 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 800.00 | -9200.00 | -0.7082 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 800.00 | -700.00 | -0.0648 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 800.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -800.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -800.00 | 700.00 | 0.0648 |
| infinity | Stock to Infinity | — | — | -800.00 | Unlimited | Unlimited |

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
| Risk Reward | 1.00x | Unlimited |
| Capital at Risk | $2,990.00 | $7,990.00 |
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
| infinity | Stock to Infinity | — | — | -800.00 | Unlimited | Unlimited |

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
| Risk Reward | 1.00x | Unlimited |
| Capital at Risk | $2,990.00 | $14,490.00 |
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
| infinity | Stock to Infinity | — | — | -800.00 | Unlimited | Unlimited |

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
| Capital at Risk | $800.00 | $800.00 |
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
| Risk Reward | 1.00x | Unlimited |
| Capital at Risk | $2,990.00 | $12,990.00 |
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
| infinity | Stock to Infinity | — | — | 800.00 | Unlimited | Unlimited |

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
| Risk Reward | 1.00x | Unlimited |
| Capital at Risk | $2,990.00 | $7,990.00 |
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
| infinity | Stock to Infinity | — | — | 800.00 | Unlimited | Unlimited |

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
| Risk Reward | 1.00x | Unlimited |
| Capital at Risk | $2,990.00 | $14,490.00 |
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
| infinity | Stock to Infinity | — | — | 800.00 | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $2,990.00 | $2,990.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $2,990.00 | $12,990.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $2,990.00 | $7,990.00 |
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
| 43.90 | Breakeven 1 | 610.00 | -610.00 | 0.00 | 0.6162 | 0.0000 |
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
| breakeven_1 | Breakeven 1 | 43.90 | -56.10% | 610.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 610.00 | 4110.00 | 0.6861 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 610.00 | 4810.00 | 0.8030 |
| spot | Current Market Price | 100.00 | 0.00% | -190.00 | 4810.00 | 0.8030 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -990.00 | 4810.00 | 0.8030 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -290.00 | 6210.00 | 1.0367 |
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $2,990.00 | $14,490.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $2,990.00 | $2,990.00 |
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
| infinity | Stock to Infinity | — | — | 610.00 | 610.00 | 0.2040 |

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
| Max Loss | Unlimited | -$1,790.00 |
| Risk Reward | 8.29x | Unlimited |
| Capital at Risk | $2,990.00 | $12,990.00 |
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
| infinity | Stock to Infinity | — | — | 610.00 | Unlimited | Unlimited |

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
| Max Loss | Unlimited | $3,210.00 |
| Risk Reward | 8.29x | Unlimited |
| Capital at Risk | $2,990.00 | $7,990.00 |
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
| infinity | Stock to Infinity | — | — | 610.00 | Unlimited | Unlimited |

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
| Max Loss | Unlimited | -$3,290.00 |
| Risk Reward | 8.29x | Unlimited |
| Capital at Risk | $2,990.00 | $14,490.00 |
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
| infinity | Stock to Infinity | — | — | 610.00 | Unlimited | Unlimited |

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
| Capital at Risk | $2,780.00 | $2,780.00 |
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
| 98.10 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0683 | 0.0683 |
| 108.00 | Upper Strike | 990.00 | 0.00 | 990.00 | 0.3561 | 0.3561 |
| 115.00 | Upside (15%) | 290.00 | 0.00 | 290.00 | 0.1043 | 0.1043 |
| 117.90 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -610.00 | -610.00 | -0.2194 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -610.00 | -610.00 | -0.2194 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -610.00 | -610.00 | -0.2194 |
| breakeven_1 | Breakeven 1 | 98.10 | -1.90% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0683 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 990.00 | 990.00 | 0.3561 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 290.00 | 290.00 | 0.1043 |
| breakeven_2 | Breakeven 2 | 117.90 | 17.90% | 0.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

---

### Call Ratio Spread (ID=19) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: SPR
- Margin Classification: SPR

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
| Max Loss | Unlimited | -$10,610.00 |
| Risk Reward | 0.05x | 0.17x |
| Capital at Risk | $18,210.00 | $28,210.00 |
| Cost Credit | Debit $610.00 | Debit $610.00 |
| Pop | 51.6% | 51.6% |
| Margin Proxy | 18210.0 | — |

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
| 85.00 | Downside (15%) | -610.00 | -1500.00 | -2110.00 | -0.0335 | -0.0748 |
| 92.00 | Lower Strike | -610.00 | -800.00 | -1410.00 | -0.0335 | -0.0500 |
| 99.05 | Breakeven 1 | 95.00 | -95.00 | 0.00 | 0.0052 | 0.0000 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0104 | 0.0067 |
| 108.00 | Upper Strike | 990.00 | 800.00 | 1790.00 | 0.0544 | 0.0635 |
| 115.00 | Upside (15%) | 290.00 | 1500.00 | 1790.00 | 0.0159 | 0.0635 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -610.00 | -10610.00 | -0.3761 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -610.00 | -2110.00 | -0.0748 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -610.00 | -1410.00 | -0.0500 |
| breakeven_1 | Breakeven 1 | 99.05 | -0.95% | 95.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0067 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 990.00 | 1790.00 | 0.0635 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 290.00 | 1790.00 | 0.0635 |
| infinity | Stock to Infinity | — | — | Unlimited | 1790.00 | 0.0635 |

---

### Call Ratio Spread (ID=19) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: SPR
- Margin Classification: SPR

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
| Max Loss | Unlimited | -$5,610.00 |
| Risk Reward | 0.05x | 1.21x |
| Capital at Risk | $18,210.00 | $23,210.00 |
| Cost Credit | Debit $610.00 | Debit $610.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 18210.0 | — |

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
| 50.00 | Scenario @ 50.00 | -610.00 | 0.00 | -610.00 | -0.0335 | -0.0263 |
| 56.10 | Breakeven 1 | -610.00 | 610.00 | 0.00 | -0.0335 | 0.0000 |
| 85.00 | Downside (15%) | -610.00 | 3500.00 | 2890.00 | -0.0335 | 0.1245 |
| 92.00 | Lower Strike | -610.00 | 4200.00 | 3590.00 | -0.0335 | 0.1547 |
| 100.00 | Current Market Price | 190.00 | 5000.00 | 5190.00 | 0.0104 | 0.2236 |
| 108.00 | Upper Strike | 990.00 | 5800.00 | 6790.00 | 0.0544 | 0.2925 |
| 115.00 | Upside (15%) | 290.00 | 6500.00 | 6790.00 | 0.0159 | 0.2925 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -610.00 | -5610.00 | -0.2417 |
| breakeven_1 | Breakeven 1 | 56.10 | -43.90% | -610.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -610.00 | 2890.00 | 0.1245 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -610.00 | 3590.00 | 0.1547 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 5190.00 | 0.2236 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 990.00 | 6790.00 | 0.2925 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 290.00 | 6790.00 | 0.2925 |
| infinity | Stock to Infinity | — | — | Unlimited | 6790.00 | 0.2925 |

---

### Call Ratio Spread (ID=19) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: SPR
- Margin Classification: SPR

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
| Max Loss | Unlimited | -$12,110.00 |
| Risk Reward | 0.05x | 0.02x |
| Capital at Risk | $18,210.00 | $29,710.00 |
| Cost Credit | Debit $610.00 | Debit $610.00 |
| Pop | 25.4% | 25.4% |
| Margin Proxy | 18210.0 | — |

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
| 85.00 | Downside (15%) | -610.00 | -3000.00 | -3610.00 | -0.0335 | -0.1215 |
| 92.00 | Lower Strike | -610.00 | -2300.00 | -2910.00 | -0.0335 | -0.0979 |
| 100.00 | Current Market Price | 190.00 | -1500.00 | -1310.00 | 0.0104 | -0.0441 |
| 106.55 | Breakeven 1 | 845.00 | -845.00 | 0.00 | 0.0464 | 0.0000 |
| 108.00 | Upper Strike | 990.00 | -700.00 | 290.00 | 0.0544 | 0.0098 |
| 115.00 | Upside (15%) | 290.00 | 0.00 | 290.00 | 0.0159 | 0.0098 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -610.00 | -12110.00 | -0.4076 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -610.00 | -3610.00 | -0.1215 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -610.00 | -2910.00 | -0.0979 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | -1310.00 | -0.0441 |
| breakeven_1 | Breakeven 1 | 106.55 | 6.55% | 845.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 990.00 | 290.00 | 0.0098 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 290.00 | 290.00 | 0.0098 |
| infinity | Stock to Infinity | — | — | Unlimited | 290.00 | 0.0098 |

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
| Capital at Risk | $8,210.00 | $8,210.00 |
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
| 82.10 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 85.00 | Downside (15%) | 290.00 | 0.00 | 290.00 | 0.0353 | 0.0353 |
| 92.00 | Lower Strike | 990.00 | 0.00 | 990.00 | 0.1206 | 0.1206 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0231 | 0.0231 |
| 101.90 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | -610.00 | 0.00 | -610.00 | -0.0743 | -0.0743 |
| 115.00 | Upside (15%) | -610.00 | 0.00 | -610.00 | -0.0743 | -0.0743 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8210.00 | -8210.00 | -1.0000 |
| breakeven_1 | Breakeven 1 | 82.10 | -17.90% | 0.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 290.00 | 290.00 | 0.0353 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 990.00 | 990.00 | 0.1206 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0231 |
| breakeven_2 | Breakeven 2 | 101.90 | 1.90% | 0.00 | 0.00 | 0.0000 |
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
| Risk Reward | 0.12x | Unlimited |
| Capital at Risk | $2,780.00 | $12,780.00 |
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
| 91.05 | Breakeven 1 | 895.00 | -895.00 | 0.00 | 0.1090 | 0.0000 |
| 92.00 | Lower Strike | 990.00 | -800.00 | 190.00 | 0.1206 | 0.0104 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0231 | 0.0104 |
| 108.00 | Upper Strike | -610.00 | 800.00 | 190.00 | -0.0743 | 0.0104 |
| 115.00 | Upside (15%) | -610.00 | 1500.00 | 890.00 | -0.0743 | 0.0489 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8210.00 | -18210.00 | -1.4249 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 290.00 | -1210.00 | -0.0664 |
| breakeven_1 | Breakeven 1 | 91.05 | -8.95% | 895.00 | 0.00 | 0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 990.00 | 190.00 | 0.0104 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0104 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -610.00 | 190.00 | 0.0104 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -610.00 | 890.00 | 0.0489 |
| infinity | Stock to Infinity | — | — | -610.00 | Unlimited | Unlimited |

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
| Risk Reward | 0.12x | Unlimited |
| Capital at Risk | $2,780.00 | $7,780.00 |
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
| 66.05 | Breakeven 1 | -1605.00 | 1605.00 | 0.00 | -0.1955 | 0.0000 |
| 85.00 | Downside (15%) | 290.00 | 3500.00 | 3790.00 | 0.0353 | 0.2869 |
| 92.00 | Lower Strike | 990.00 | 4200.00 | 5190.00 | 0.1206 | 0.3929 |
| 100.00 | Current Market Price | 190.00 | 5000.00 | 5190.00 | 0.0231 | 0.3929 |
| 108.00 | Upper Strike | -610.00 | 5800.00 | 5190.00 | -0.0743 | 0.3929 |
| 115.00 | Upside (15%) | -610.00 | 6500.00 | 5890.00 | -0.0743 | 0.4459 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8210.00 | -13210.00 | -1.6979 |
| breakeven_1 | Breakeven 1 | 66.05 | -33.95% | -1605.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 290.00 | 3790.00 | 0.2869 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 990.00 | 5190.00 | 0.3929 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 5190.00 | 0.3929 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -610.00 | 5190.00 | 0.3929 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -610.00 | 5890.00 | 0.4459 |
| infinity | Stock to Infinity | — | — | -610.00 | Unlimited | Unlimited |

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
| Risk Reward | 0.12x | Unlimited |
| Capital at Risk | $2,780.00 | $14,280.00 |
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
| infinity | Stock to Infinity | — | — | -610.00 | Unlimited | Unlimited |

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
| Capital at Risk | $3,388.00 | $3,388.00 |
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
| 117.50 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |

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
| breakeven_2 | Breakeven 2 | 117.50 | 17.50% | 0.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $18,250.00 | $28,250.00 |
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
| Capital at Risk | $18,250.00 | $23,250.00 |
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
| Capital at Risk | $18,250.00 | $29,750.00 |
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
| Capital at Risk | $8,250.00 | $8,250.00 |
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
| 82.50 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 85.00 | Downside (15%) | 250.00 | 0.00 | 250.00 | 0.0303 | 0.0303 |
| 100.00 | Current Market Price | 250.00 | 0.00 | 250.00 | 0.0303 | 0.0303 |
| 102.50 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -1250.00 | 0.00 | -1250.00 | -0.1515 | -0.1515 |
| 115.00 | Upside (15%) | -1250.00 | 0.00 | -1250.00 | -0.1515 | -0.1515 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8250.00 | -8250.00 | -1.0000 |
| breakeven_1 | Breakeven 1 | 82.50 | -17.50% | 0.00 | 0.00 | 0.0000 |
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
| Risk Reward | 0.03x | Unlimited |
| Capital at Risk | $3,388.00 | $13,388.00 |
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
| infinity | Stock to Infinity | — | — | -1250.00 | Unlimited | Unlimited |

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
| Risk Reward | 0.03x | Unlimited |
| Capital at Risk | $3,388.00 | $8,388.00 |
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
| infinity | Stock to Infinity | — | — | -1250.00 | Unlimited | Unlimited |

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
| Risk Reward | 0.03x | Unlimited |
| Capital at Risk | $3,388.00 | $14,888.00 |
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
| infinity | Stock to Infinity | — | — | -1250.00 | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $3,638.00 | $3,638.00 |
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
| 97.50 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
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
| breakeven_1 | Breakeven 1 | 97.50 | -2.50% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -1.0000 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -250.00 | -250.00 | -1.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -250.00 | -250.00 | -1.0000 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -250.00 | -250.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 117.50 | 17.50% | 0.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $3,638.00 | $13,638.00 |
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
| 102.50 | Breakeven 1 | -250.00 | 250.00 | 0.00 | -1.0000 | 0.0000 |
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
| breakeven_1 | Breakeven 1 | 102.50 | 2.50% | -250.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -250.00 | 1250.00 | 0.1220 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -250.00 | 1250.00 | 0.1220 |
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $3,638.00 | $8,638.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $3,638.00 | $15,138.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $3,638.00 | $3,638.00 |
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
| 102.50 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
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
| breakeven_2 | Breakeven 2 | 102.50 | 2.50% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1250.00 | 1250.00 | 5.0000 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1250.00 | 1250.00 | 5.0000 |
| infinity | Stock to Infinity | — | — | 1250.00 | 1250.00 | 0.3436 |

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
| Risk Reward | 33.00x | Unlimited |
| Capital at Risk | $3,638.00 | $13,638.00 |
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
| 101.25 | Breakeven 1 | -125.00 | 125.00 | 0.00 | -0.5000 | 0.0000 |
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
| breakeven_1 | Breakeven 1 | 101.25 | 1.25% | -125.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1250.00 | 2750.00 | 0.2683 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | 1250.00 | 2750.00 | 0.2683 |
| infinity | Stock to Infinity | — | — | 1250.00 | Unlimited | Unlimited |

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
| Risk Reward | 33.00x | Unlimited |
| Capital at Risk | $3,638.00 | $8,638.00 |
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
| infinity | Stock to Infinity | — | — | 1250.00 | Unlimited | Unlimited |

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
| Risk Reward | 33.00x | Unlimited |
| Capital at Risk | $3,638.00 | $15,138.00 |
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
| infinity | Stock to Infinity | — | — | 1250.00 | Unlimited | Unlimited |

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
| Capital at Risk | $1,276.00 | $1,276.00 |
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
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $4,500.00 | $14,500.00 |
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
| 98.88 | Breakeven 1 | 112.00 | -112.00 | 0.00 | 0.0878 | 0.0000 |
| 100.00 | Current Market Price | 224.00 | 0.00 | 224.00 | 0.1755 | 0.0199 |
| 115.00 | Upside (15%) | -1276.00 | 1500.00 | 224.00 | -1.0000 | 0.0199 |
| 115.00 | Upside (15%) | -1276.00 | 1500.00 | 224.00 | -1.0000 | 0.0199 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1276.00 | -11276.00 | -0.7777 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1276.00 | -2776.00 | -0.2462 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1276.00 | -2776.00 | -0.2462 |
| breakeven_1 | Breakeven 1 | 98.88 | -1.12% | 112.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.0199 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.0199 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1276.00 | 224.00 | 0.0199 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1276.00 | 224.00 | 0.0199 |
| infinity | Stock to Infinity | — | — | -1276.00 | Unlimited | Unlimited |

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
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $4,500.00 | $9,500.00 |
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
| infinity | Stock to Infinity | — | — | -1276.00 | Unlimited | Unlimited |

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
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $4,500.00 | $16,000.00 |
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
| infinity | Stock to Infinity | — | — | -1276.00 | Unlimited | Unlimited |

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
| Capital at Risk | $1,276.00 | $1,276.00 |
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
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $4,500.00 | $14,500.00 |
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
| 98.88 | Breakeven 1 | 112.00 | -112.00 | 0.00 | 0.0878 | 0.0000 |
| 100.00 | Current Market Price | 224.00 | 0.00 | 224.00 | 0.1755 | 0.0199 |
| 115.00 | Upside (15%) | -1276.00 | 1500.00 | 224.00 | -1.0000 | 0.0199 |
| 115.00 | Upside (15%) | -1276.00 | 1500.00 | 224.00 | -1.0000 | 0.0199 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1276.00 | -11276.00 | -0.7777 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1276.00 | -2776.00 | -0.2462 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1276.00 | -2776.00 | -0.2462 |
| breakeven_1 | Breakeven 1 | 98.88 | -1.12% | 112.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.0199 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.0199 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1276.00 | 224.00 | 0.0199 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1276.00 | 224.00 | 0.0199 |
| infinity | Stock to Infinity | — | — | -1276.00 | Unlimited | Unlimited |

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
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $4,500.00 | $9,500.00 |
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
| infinity | Stock to Infinity | — | — | -1276.00 | Unlimited | Unlimited |

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
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $4,500.00 | $16,000.00 |
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
| infinity | Stock to Infinity | — | — | -1276.00 | Unlimited | Unlimited |

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
| Capital at Risk | $1,276.00 | $1,276.00 |
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
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $4,500.00 | $14,500.00 |
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
| 98.88 | Breakeven 1 | 112.00 | -112.00 | 0.00 | 0.0878 | 0.0000 |
| 100.00 | Current Market Price | 224.00 | 0.00 | 224.00 | 0.1755 | 0.0199 |
| 115.00 | Upside (15%) | -1276.00 | 1500.00 | 224.00 | -1.0000 | 0.0199 |
| 115.00 | Upside (15%) | -1276.00 | 1500.00 | 224.00 | -1.0000 | 0.0199 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1276.00 | -11276.00 | -0.7777 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1276.00 | -2776.00 | -0.2462 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | -1276.00 | -2776.00 | -0.2462 |
| breakeven_1 | Breakeven 1 | 98.88 | -1.12% | 112.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.0199 |
| strike_2 | Current Market Price | 100.00 | 0.00% | 224.00 | 224.00 | 0.0199 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1276.00 | 224.00 | 0.0199 |
| strike_3 | Upside (15%) | 115.00 | 15.00% | -1276.00 | 224.00 | 0.0199 |
| infinity | Stock to Infinity | — | — | -1276.00 | Unlimited | Unlimited |

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
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $4,500.00 | $9,500.00 |
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
| infinity | Stock to Infinity | — | — | -1276.00 | Unlimited | Unlimited |

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
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $4,500.00 | $16,000.00 |
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
| infinity | Stock to Infinity | — | — | -1276.00 | Unlimited | Unlimited |

---

### Long Call Condor (ID=28) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

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
| Max Loss | -$1,020.00 | -$1,020.00 |
| Risk Reward | 0.18x | 0.18x |
| Capital at Risk | $1,020.00 | $1,020.00 |
| Cost Credit | Debit $1,020.00 | Debit $1,020.00 |
| Pop | 65.6% | 65.6% |
| Margin Proxy | 1020.0 | — |

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
| Max Loss | -$1,020.00 | -$11,020.00 |
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $4,380.00 | $14,380.00 |
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
| infinity | Stock to Infinity | — | — | -1020.00 | Unlimited | Unlimited |

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
| Max Loss | -$1,020.00 | -$6,020.00 |
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $4,380.00 | $9,380.00 |
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
| infinity | Stock to Infinity | — | — | -1020.00 | Unlimited | Unlimited |

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
| Max Loss | -$1,020.00 | -$12,520.00 |
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $4,380.00 | $15,880.00 |
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
| infinity | Stock to Infinity | — | — | -1020.00 | Unlimited | Unlimited |

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
| Capital at Risk | $1,020.00 | $1,020.00 |
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
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $4,380.00 | $14,380.00 |
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
| infinity | Stock to Infinity | — | — | -1020.00 | Unlimited | Unlimited |

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
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $4,380.00 | $9,380.00 |
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
| infinity | Stock to Infinity | — | — | -1020.00 | Unlimited | Unlimited |

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
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $4,380.00 | $15,880.00 |
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
| infinity | Stock to Infinity | — | — | -1020.00 | Unlimited | Unlimited |

---

### Iron Condor (ID=30) — options_only

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
| Max Loss | -$1,020.00 | -$1,020.00 |
| Risk Reward | 0.18x | 0.18x |
| Capital at Risk | $1,020.00 | $1,020.00 |
| Cost Credit | Credit $180.00 | Credit $180.00 |
| Pop | 65.6% | 65.6% |
| Margin Proxy | 1020.0 | — |

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
| Max Loss | -$1,020.00 | -$11,020.00 |
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $2,780.00 | $12,780.00 |
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
| infinity | Stock to Infinity | — | — | -1020.00 | Unlimited | Unlimited |

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
| Max Loss | -$1,020.00 | -$6,020.00 |
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $2,780.00 | $7,780.00 |
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
| infinity | Stock to Infinity | — | — | -1020.00 | Unlimited | Unlimited |

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
| Max Loss | -$1,020.00 | -$12,520.00 |
| Risk Reward | 0.18x | Unlimited |
| Capital at Risk | $2,780.00 | $14,280.00 |
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
| infinity | Stock to Infinity | — | — | -1020.00 | Unlimited | Unlimited |

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
| Capital at Risk | $224.00 | $224.00 |
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
| 97.76 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | -224.00 | 0.00 | -224.00 | -1.0000 | -1.0000 |
| 102.24 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 5.6964 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 5.6964 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1276.00 | 1276.00 | 5.6964 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1276.00 | 1276.00 | 5.6964 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1276.00 | 1276.00 | 5.6964 |
| breakeven_1 | Breakeven 1 | 97.76 | -2.24% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -1.0000 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 102.24 | 2.24% | 0.00 | 0.00 | 0.0000 |
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
| Risk Reward | 5.70x | Unlimited |
| Capital at Risk | $4,776.00 | $14,776.00 |
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
| infinity | Stock to Infinity | — | — | 1276.00 | Unlimited | Unlimited |

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
| Risk Reward | 5.70x | Unlimited |
| Capital at Risk | $4,776.00 | $9,776.00 |
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
| infinity | Stock to Infinity | — | — | 1276.00 | Unlimited | Unlimited |

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
| Risk Reward | 5.70x | Unlimited |
| Capital at Risk | $4,776.00 | $16,276.00 |
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
| infinity | Stock to Infinity | — | — | 1276.00 | Unlimited | Unlimited |

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
| Capital at Risk | $224.00 | $224.00 |
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
| 97.76 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | -224.00 | 0.00 | -224.00 | -1.0000 | -1.0000 |
| 102.24 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 5.6964 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 5.6964 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1276.00 | 1276.00 | 5.6964 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1276.00 | 1276.00 | 5.6964 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1276.00 | 1276.00 | 5.6964 |
| breakeven_1 | Breakeven 1 | 97.76 | -2.24% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -1.0000 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 102.24 | 2.24% | 0.00 | 0.00 | 0.0000 |
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
| Risk Reward | 5.70x | Unlimited |
| Capital at Risk | $4,776.00 | $14,776.00 |
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
| infinity | Stock to Infinity | — | — | 1276.00 | Unlimited | Unlimited |

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
| Risk Reward | 5.70x | Unlimited |
| Capital at Risk | $4,776.00 | $9,776.00 |
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
| infinity | Stock to Infinity | — | — | 1276.00 | Unlimited | Unlimited |

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
| Risk Reward | 5.70x | Unlimited |
| Capital at Risk | $4,776.00 | $16,276.00 |
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
| infinity | Stock to Infinity | — | — | 1276.00 | Unlimited | Unlimited |

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
| Capital at Risk | $224.00 | $224.00 |
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
| 97.76 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | -224.00 | 0.00 | -224.00 | -1.0000 | -1.0000 |
| 102.24 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 5.6964 |
| 115.00 | Upside (15%) | 1276.00 | 0.00 | 1276.00 | 5.6964 | 5.6964 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1276.00 | 1276.00 | 5.6964 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1276.00 | 1276.00 | 5.6964 |
| strike_1 | Downside (15%) | 85.00 | -15.00% | 1276.00 | 1276.00 | 5.6964 |
| breakeven_1 | Breakeven 1 | 97.76 | -2.24% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -1.0000 |
| strike_2 | Current Market Price | 100.00 | 0.00% | -224.00 | -224.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 102.24 | 2.24% | 0.00 | 0.00 | 0.0000 |
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
| Risk Reward | 5.70x | Unlimited |
| Capital at Risk | $2,276.00 | $12,276.00 |
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
| infinity | Stock to Infinity | — | — | 1276.00 | Unlimited | Unlimited |

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
| Risk Reward | 5.70x | Unlimited |
| Capital at Risk | $2,276.00 | $7,276.00 |
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
| infinity | Stock to Infinity | — | — | 1276.00 | Unlimited | Unlimited |

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
| Risk Reward | 5.70x | Unlimited |
| Capital at Risk | $2,276.00 | $13,776.00 |
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
| infinity | Stock to Infinity | — | — | 1276.00 | Unlimited | Unlimited |

---

### Short Call Condor (ID=34) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

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
| Max Profit | $1,020.00 | $1,020.00 |
| Max Loss | -$180.00 | -$180.00 |
| Risk Reward | 5.67x | 5.67x |
| Capital at Risk | $180.00 | $180.00 |
| Cost Credit | Credit $1,020.00 | Credit $1,020.00 |
| Pop | 34.4% | 34.4% |
| Margin Proxy | 180.0 | — |

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
| 90.20 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 92.00 | Strike (Lower Middle) | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 100.00 | Current Market Price | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 108.00 | Strike (Upper Middle) | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 109.80 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 520.00 | 0.00 | 520.00 | 2.8889 | 2.8889 |
| 120.00 | Strike (Highest) | 1020.00 | 0.00 | 1020.00 | 5.6667 | 5.6667 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1020.00 | 1020.00 | 5.6667 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | 1020.00 | 5.6667 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | 520.00 | 2.8889 |
| breakeven_1 | Breakeven 1 | 90.20 | -9.80% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | -180.00 | -1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | -180.00 | -1.0000 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | -180.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 109.80 | 9.80% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 520.00 | 2.8889 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 1020.00 | 5.6667 |
| infinity | Stock to Infinity | — | — | 1020.00 | 1020.00 | 5.6667 |

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
| Max Profit | $1,020.00 | Unlimited |
| Max Loss | -$180.00 | -$8,980.00 |
| Risk Reward | 5.67x | Unlimited |
| Capital at Risk | $5,200.00 | $15,200.00 |
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
| 101.80 | Breakeven 1 | -180.00 | 180.00 | 0.00 | -1.0000 | 0.0000 |
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
| breakeven_1 | Breakeven 1 | 101.80 | 1.80% | -180.00 | 0.00 | 0.0000 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | 620.00 | 0.0609 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 2020.00 | 0.1984 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 3020.00 | 0.2967 |
| infinity | Stock to Infinity | — | — | 1020.00 | Unlimited | Unlimited |

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
| Max Profit | $1,020.00 | Unlimited |
| Max Loss | -$180.00 | -$3,980.00 |
| Risk Reward | 5.67x | Unlimited |
| Capital at Risk | $5,200.00 | $10,200.00 |
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
| 39.80 | Breakeven 1 | 1020.00 | -1020.00 | 0.00 | 5.6667 | 0.0000 |
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
| breakeven_1 | Breakeven 1 | 39.80 | -60.20% | 1020.00 | 0.00 | 0.0000 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | 4020.00 | 0.7761 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | 4020.00 | 0.7761 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | 4020.00 | 0.7761 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | 4820.00 | 0.9305 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | 5620.00 | 1.0849 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 7020.00 | 1.3552 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 8020.00 | 1.5483 |
| infinity | Stock to Infinity | — | — | 1020.00 | Unlimited | Unlimited |

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
| Max Profit | $1,020.00 | Unlimited |
| Max Loss | -$180.00 | -$10,480.00 |
| Risk Reward | 5.67x | Unlimited |
| Capital at Risk | $5,200.00 | $16,700.00 |
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
| infinity | Stock to Infinity | — | — | 1020.00 | Unlimited | Unlimited |

---

### Short Put Condor (ID=35) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

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
| Max Loss | -$180.00 | -$180.00 |
| Risk Reward | 5.67x | 5.67x |
| Capital at Risk | $180.00 | $180.00 |
| Cost Credit | Credit $1,020.00 | Credit $1,020.00 |
| Pop | 34.4% | 34.4% |
| Margin Proxy | 180.0 | — |

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
| 90.20 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 92.00 | Strike (Lower Middle) | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 100.00 | Current Market Price | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 108.00 | Strike (Upper Middle) | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 109.80 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 520.00 | 0.00 | 520.00 | 2.8889 | 2.8889 |
| 120.00 | Strike (Highest) | 1020.00 | 0.00 | 1020.00 | 5.6667 | 5.6667 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1020.00 | 1020.00 | 5.6667 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | 1020.00 | 5.6667 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | 520.00 | 2.8889 |
| breakeven_1 | Breakeven 1 | 90.20 | -9.80% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | -180.00 | -1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | -180.00 | -1.0000 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | -180.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 109.80 | 9.80% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 520.00 | 2.8889 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 1020.00 | 5.6667 |
| infinity | Stock to Infinity | — | — | 1020.00 | 1020.00 | 5.6667 |

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
| Max Loss | -$180.00 | -$8,980.00 |
| Risk Reward | 5.67x | Unlimited |
| Capital at Risk | $5,200.00 | $15,200.00 |
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
| 101.80 | Breakeven 1 | -180.00 | 180.00 | 0.00 | -1.0000 | 0.0000 |
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
| breakeven_1 | Breakeven 1 | 101.80 | 1.80% | -180.00 | 0.00 | 0.0000 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | 620.00 | 0.0609 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 2020.00 | 0.1984 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 3020.00 | 0.2967 |
| infinity | Stock to Infinity | — | — | 1020.00 | Unlimited | Unlimited |

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
| Max Loss | -$180.00 | -$3,980.00 |
| Risk Reward | 5.67x | Unlimited |
| Capital at Risk | $5,200.00 | $10,200.00 |
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
| 39.80 | Breakeven 1 | 1020.00 | -1020.00 | 0.00 | 5.6667 | 0.0000 |
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
| breakeven_1 | Breakeven 1 | 39.80 | -60.20% | 1020.00 | 0.00 | 0.0000 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | 4020.00 | 0.7761 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | 4020.00 | 0.7761 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | 4020.00 | 0.7761 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | 4820.00 | 0.9305 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | 5620.00 | 1.0849 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 7020.00 | 1.3552 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 8020.00 | 1.5483 |
| infinity | Stock to Infinity | — | — | 1020.00 | Unlimited | Unlimited |

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
| Max Loss | -$180.00 | -$10,480.00 |
| Risk Reward | 5.67x | Unlimited |
| Capital at Risk | $5,200.00 | $16,700.00 |
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
| infinity | Stock to Infinity | — | — | 1020.00 | Unlimited | Unlimited |

---

### Rev Iron Condor (ID=36) — options_only

**Inputs:**

- Spot: 100.0
- Stock Position: 0.0
- Avg Cost: 0.0
- Strategy Code: SPR
- Margin Classification: SPR

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
| Max Profit | $1,020.00 | $1,020.00 |
| Max Loss | -$180.00 | -$180.00 |
| Risk Reward | 5.67x | 5.67x |
| Capital at Risk | $180.00 | $180.00 |
| Cost Credit | Debit $180.00 | Debit $180.00 |
| Pop | 34.4% | 34.4% |
| Margin Proxy | 180.0 | — |

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
| 90.20 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 92.00 | Strike (Lower Middle) | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 100.00 | Current Market Price | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 108.00 | Strike (Upper Middle) | -180.00 | 0.00 | -180.00 | -1.0000 | -1.0000 |
| 109.80 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 520.00 | 0.00 | 520.00 | 2.8889 | 2.8889 |
| 120.00 | Strike (Highest) | 1020.00 | 0.00 | 1020.00 | 5.6667 | 5.6667 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 1020.00 | 1020.00 | 5.6667 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | 1020.00 | 5.6667 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | 520.00 | 2.8889 |
| breakeven_1 | Breakeven 1 | 90.20 | -9.80% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | -180.00 | -1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | -180.00 | -1.0000 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | -180.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 109.80 | 9.80% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 520.00 | 2.8889 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 1020.00 | 5.6667 |
| infinity | Stock to Infinity | — | — | 1020.00 | 1020.00 | 5.6667 |

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
| Max Profit | $1,020.00 | Unlimited |
| Max Loss | -$180.00 | -$8,980.00 |
| Risk Reward | 5.67x | Unlimited |
| Capital at Risk | $2,200.00 | $12,200.00 |
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
| 101.80 | Breakeven 1 | -180.00 | 180.00 | 0.00 | -1.0000 | 0.0000 |
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
| breakeven_1 | Breakeven 1 | 101.80 | 1.80% | -180.00 | 0.00 | 0.0000 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | 620.00 | 0.0609 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 2020.00 | 0.1984 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 3020.00 | 0.2967 |
| infinity | Stock to Infinity | — | — | 1020.00 | Unlimited | Unlimited |

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
| Max Profit | $1,020.00 | Unlimited |
| Max Loss | -$180.00 | -$3,980.00 |
| Risk Reward | 5.67x | Unlimited |
| Capital at Risk | $2,200.00 | $7,200.00 |
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
| 39.80 | Breakeven 1 | 1020.00 | -1020.00 | 0.00 | 5.6667 | 0.0000 |
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
| breakeven_1 | Breakeven 1 | 39.80 | -60.20% | 1020.00 | 0.00 | 0.0000 |
| strike_1 | Strike (Lowest) | 80.00 | -20.00% | 1020.00 | 4020.00 | 0.7761 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 520.00 | 4020.00 | 0.7761 |
| strike_2 | Strike (Lower Middle) | 92.00 | -8.00% | -180.00 | 4020.00 | 0.7761 |
| spot | Current Market Price | 100.00 | 0.00% | -180.00 | 4820.00 | 0.9305 |
| strike_3 | Strike (Upper Middle) | 108.00 | 8.00% | -180.00 | 5620.00 | 1.0849 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 520.00 | 7020.00 | 1.3552 |
| strike_4 | Strike (Highest) | 120.00 | 20.00% | 1020.00 | 8020.00 | 1.5483 |
| infinity | Stock to Infinity | — | — | 1020.00 | Unlimited | Unlimited |

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
| Max Profit | $1,020.00 | Unlimited |
| Max Loss | -$180.00 | -$10,480.00 |
| Risk Reward | 5.67x | Unlimited |
| Capital at Risk | $2,200.00 | $13,700.00 |
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
| infinity | Stock to Infinity | — | — | 1020.00 | Unlimited | Unlimited |

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
| Risk Reward | N/A | N/A |
| Capital at Risk | $500.00 | $500.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $500.00 | $10,500.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $500.00 | $5,500.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $500.00 | $12,000.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $4,500.00 | $4,500.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $19,500.00 | $29,500.00 |
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
| Capital at Risk | $19,500.00 | $24,500.00 |
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
| Capital at Risk | $19,500.00 | $31,000.00 |
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
| Risk Reward | N/A | N/A |
| Capital at Risk | $380.00 | $380.00 |
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
| 88.20 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 92.00 | Lower Strike | -380.00 | 0.00 | -380.00 | -1.0000 | -1.0000 |
| 100.00 | Current Market Price | -380.00 | 0.00 | -380.00 | -1.0000 | -1.0000 |
| 108.00 | Upper Strike | -380.00 | 0.00 | -380.00 | -1.0000 | -1.0000 |
| 111.80 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 320.00 | 0.00 | 320.00 | 0.8421 | 0.8421 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8820.00 | 8820.00 | 23.2105 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 320.00 | 320.00 | 0.8421 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | 0.00 | 0.00 | 0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -380.00 | -380.00 | -1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -380.00 | -1.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -380.00 | -380.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 320.00 | 320.00 | 0.8421 |
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Max Loss | Unlimited | -$1,180.00 |
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $380.00 | $10,380.00 |
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
| 103.80 | Breakeven 1 | -380.00 | 380.00 | 0.00 | -1.0000 | 0.0000 |
| 108.00 | Upper Strike | -380.00 | 800.00 | 420.00 | -1.0000 | 0.0405 |
| 115.00 | Upside (15%) | 320.00 | 1500.00 | 1820.00 | 0.8421 | 0.1753 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8820.00 | -1180.00 | -0.1137 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 320.00 | -1180.00 | -0.1137 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -380.00 | -1180.00 | -0.1137 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -380.00 | -0.0366 |
| breakeven_1 | Breakeven 1 | 103.80 | 3.80% | -380.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -380.00 | 420.00 | 0.0405 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 320.00 | 1820.00 | 0.1753 |
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Max Loss | Unlimited | $3,820.00 |
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $380.00 | $5,380.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Max Loss | Unlimited | -$2,680.00 |
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $380.00 | $11,880.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $2,780.00 | $2,780.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

---

### Short Strangle (ID=40) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: SPR
- Margin Classification: SPR

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
| Max Loss | Unlimited | -$18,820.00 |
| Risk Reward | 0.02x | 0.06x |
| Capital at Risk | $18,820.00 | $28,820.00 |
| Cost Credit | Credit $380.00 | Credit $380.00 |
| Pop | 62.6% | 62.6% |
| Margin Proxy | 18820.0 | — |

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
| 85.00 | Downside (15%) | -320.00 | -1500.00 | -1820.00 | -0.0170 | -0.0632 |
| 92.00 | Lower Strike | 380.00 | -800.00 | -420.00 | 0.0202 | -0.0146 |
| 96.20 | Breakeven 1 | 380.00 | -380.00 | 0.00 | 0.0202 | 0.0000 |
| 100.00 | Current Market Price | 380.00 | 0.00 | 380.00 | 0.0202 | 0.0132 |
| 108.00 | Upper Strike | 380.00 | 800.00 | 1180.00 | 0.0202 | 0.0409 |
| 115.00 | Upside (15%) | -320.00 | 1500.00 | 1180.00 | -0.0170 | 0.0409 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -18820.00 | -0.6530 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | -1820.00 | -0.0632 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | -420.00 | -0.0146 |
| breakeven_1 | Breakeven 1 | 96.20 | -3.80% | 380.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 380.00 | 0.0132 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | 1180.00 | 0.0409 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | 1180.00 | 0.0409 |
| infinity | Stock to Infinity | — | — | Unlimited | 1180.00 | 0.0409 |

---

### Short Strangle (ID=40) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: SPR
- Margin Classification: SPR

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
| Max Loss | Unlimited | -$13,820.00 |
| Risk Reward | 0.02x | 0.45x |
| Capital at Risk | $18,820.00 | $23,820.00 |
| Cost Credit | Credit $380.00 | Credit $380.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 18820.0 | — |

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
| 50.00 | Scenario @ 50.00 | -3820.00 | 0.00 | -3820.00 | -0.2030 | -0.1604 |
| 69.10 | Breakeven 1 | -1910.00 | 1910.00 | 0.00 | -0.1015 | 0.0000 |
| 85.00 | Downside (15%) | -320.00 | 3500.00 | 3180.00 | -0.0170 | 0.1335 |
| 92.00 | Lower Strike | 380.00 | 4200.00 | 4580.00 | 0.0202 | 0.1923 |
| 100.00 | Current Market Price | 380.00 | 5000.00 | 5380.00 | 0.0202 | 0.2259 |
| 108.00 | Upper Strike | 380.00 | 5800.00 | 6180.00 | 0.0202 | 0.2594 |
| 115.00 | Upside (15%) | -320.00 | 6500.00 | 6180.00 | -0.0170 | 0.2594 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -13820.00 | -0.5802 |
| breakeven_1 | Breakeven 1 | 69.10 | -30.90% | -1910.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | 3180.00 | 0.1335 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | 4580.00 | 0.1923 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 5380.00 | 0.2259 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | 6180.00 | 0.2594 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | 6180.00 | 0.2594 |
| infinity | Stock to Infinity | — | — | Unlimited | 6180.00 | 0.2594 |

---

### Short Strangle (ID=40) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: SPR
- Margin Classification: SPR

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
| Max Loss | Unlimited | -$20,320.00 |
| Risk Reward | 0.02x | 0.02x |
| Capital at Risk | $18,820.00 | $30,320.00 |
| Cost Credit | Credit $380.00 | Credit $380.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 18820.0 | — |

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
| 85.00 | Downside (15%) | -320.00 | -3000.00 | -3320.00 | -0.0170 | -0.1095 |
| 92.00 | Lower Strike | 380.00 | -2300.00 | -1920.00 | 0.0202 | -0.0633 |
| 100.00 | Current Market Price | 380.00 | -1500.00 | -1120.00 | 0.0202 | -0.0369 |
| 108.00 | Upper Strike | 380.00 | -700.00 | -320.00 | 0.0202 | -0.0106 |
| 115.00 | Upside (15%) | -320.00 | 0.00 | -320.00 | -0.0170 | -0.0106 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -20320.00 | -0.6702 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | -3320.00 | -0.1095 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | -1920.00 | -0.0633 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | -1120.00 | -0.0369 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | -320.00 | -0.0106 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | -320.00 | -0.0106 |
| infinity | Stock to Infinity | — | — | Unlimited | -320.00 | -0.0106 |

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
| Risk Reward | N/A | N/A |
| Capital at Risk | $1,980.00 | $1,980.00 |
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
| 88.20 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 92.00 | Lower Strike | -380.00 | 0.00 | -380.00 | -1.0000 | -1.0000 |
| 100.00 | Current Market Price | -380.00 | 0.00 | -380.00 | -1.0000 | -1.0000 |
| 108.00 | Upper Strike | -380.00 | 0.00 | -380.00 | -1.0000 | -1.0000 |
| 111.80 | Breakeven 2 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 320.00 | 0.00 | 320.00 | 0.8421 | 0.8421 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8820.00 | 8820.00 | 4.4545 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 320.00 | 320.00 | 0.8421 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | 0.00 | 0.00 | 0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -380.00 | -380.00 | -1.0000 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -380.00 | -1.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -380.00 | -380.00 | -1.0000 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 320.00 | 320.00 | 0.8421 |
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Max Loss | Unlimited | -$1,180.00 |
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $1,980.00 | $11,980.00 |
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
| 103.80 | Breakeven 1 | -380.00 | 380.00 | 0.00 | -1.0000 | 0.0000 |
| 108.00 | Upper Strike | -380.00 | 800.00 | 420.00 | -1.0000 | 0.0405 |
| 115.00 | Upside (15%) | 320.00 | 1500.00 | 1820.00 | 0.8421 | 0.1753 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 8820.00 | -1180.00 | -0.0985 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 320.00 | -1180.00 | -0.1137 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -380.00 | -1180.00 | -0.1137 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -380.00 | -0.0366 |
| breakeven_1 | Breakeven 1 | 103.80 | 3.80% | -380.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -380.00 | 420.00 | 0.0405 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 320.00 | 1820.00 | 0.1753 |
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Max Loss | Unlimited | $3,820.00 |
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $1,980.00 | $6,980.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Max Loss | Unlimited | -$2,680.00 |
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $1,980.00 | $13,480.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $5,980.00 | $5,980.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

---

### Short Guts (ID=42) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: SPR
- Margin Classification: SPR

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
| Max Loss | Unlimited | -$18,820.00 |
| Risk Reward | 0.02x | 0.06x |
| Capital at Risk | $18,820.00 | $28,820.00 |
| Cost Credit | Credit $1,980.00 | Credit $1,980.00 |
| Pop | 62.6% | 62.6% |
| Margin Proxy | 18820.0 | — |

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
| 85.00 | Downside (15%) | -320.00 | -1500.00 | -1820.00 | -0.0170 | -0.0632 |
| 92.00 | Lower Strike | 380.00 | -800.00 | -420.00 | 0.0202 | -0.0146 |
| 96.20 | Breakeven 1 | 380.00 | -380.00 | 0.00 | 0.0202 | 0.0000 |
| 100.00 | Current Market Price | 380.00 | 0.00 | 380.00 | 0.0202 | 0.0132 |
| 108.00 | Upper Strike | 380.00 | 800.00 | 1180.00 | 0.0202 | 0.0409 |
| 115.00 | Upside (15%) | -320.00 | 1500.00 | 1180.00 | -0.0170 | 0.0409 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -18820.00 | -0.6530 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | -1820.00 | -0.0632 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | -420.00 | -0.0146 |
| breakeven_1 | Breakeven 1 | 96.20 | -3.80% | 380.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 380.00 | 0.0132 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | 1180.00 | 0.0409 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | 1180.00 | 0.0409 |
| infinity | Stock to Infinity | — | — | Unlimited | 1180.00 | 0.0409 |

---

### Short Guts (ID=42) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: SPR
- Margin Classification: SPR

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
| Max Loss | Unlimited | -$13,820.00 |
| Risk Reward | 0.02x | 0.45x |
| Capital at Risk | $18,820.00 | $23,820.00 |
| Cost Credit | Credit $1,980.00 | Credit $1,980.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 18820.0 | — |

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
| 50.00 | Scenario @ 50.00 | -3820.00 | 0.00 | -3820.00 | -0.2030 | -0.1604 |
| 69.10 | Breakeven 1 | -1910.00 | 1910.00 | 0.00 | -0.1015 | 0.0000 |
| 85.00 | Downside (15%) | -320.00 | 3500.00 | 3180.00 | -0.0170 | 0.1335 |
| 92.00 | Lower Strike | 380.00 | 4200.00 | 4580.00 | 0.0202 | 0.1923 |
| 100.00 | Current Market Price | 380.00 | 5000.00 | 5380.00 | 0.0202 | 0.2259 |
| 108.00 | Upper Strike | 380.00 | 5800.00 | 6180.00 | 0.0202 | 0.2594 |
| 115.00 | Upside (15%) | -320.00 | 6500.00 | 6180.00 | -0.0170 | 0.2594 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -13820.00 | -0.5802 |
| breakeven_1 | Breakeven 1 | 69.10 | -30.90% | -1910.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | 3180.00 | 0.1335 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | 4580.00 | 0.1923 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 5380.00 | 0.2259 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | 6180.00 | 0.2594 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | 6180.00 | 0.2594 |
| infinity | Stock to Infinity | — | — | Unlimited | 6180.00 | 0.2594 |

---

### Short Guts (ID=42) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: SPR
- Margin Classification: SPR

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
| Max Loss | Unlimited | -$20,320.00 |
| Risk Reward | 0.02x | 0.02x |
| Capital at Risk | $18,820.00 | $30,320.00 |
| Cost Credit | Credit $1,980.00 | Credit $1,980.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 18820.0 | — |

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
| 85.00 | Downside (15%) | -320.00 | -3000.00 | -3320.00 | -0.0170 | -0.1095 |
| 92.00 | Lower Strike | 380.00 | -2300.00 | -1920.00 | 0.0202 | -0.0633 |
| 100.00 | Current Market Price | 380.00 | -1500.00 | -1120.00 | 0.0202 | -0.0369 |
| 108.00 | Upper Strike | 380.00 | -700.00 | -320.00 | 0.0202 | -0.0106 |
| 115.00 | Upside (15%) | -320.00 | 0.00 | -320.00 | -0.0170 | -0.0106 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -20320.00 | -0.6702 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | -3320.00 | -0.1095 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | -1920.00 | -0.0633 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | -1120.00 | -0.0369 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | -320.00 | -0.0106 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | -320.00 | -0.0106 |
| infinity | Stock to Infinity | — | — | Unlimited | -320.00 | -0.0106 |

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
| Risk Reward | N/A | N/A |
| Capital at Risk | $750.00 | $750.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | N/A | N/A |
| Capital at Risk | $750.00 | $10,750.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | N/A | N/A |
| Capital at Risk | $750.00 | $5,750.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | N/A | N/A |
| Capital at Risk | $750.00 | $12,250.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | N/A | N/A |
| Capital at Risk | $750.00 | $750.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $750.00 | $10,750.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $750.00 | $5,750.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $750.00 | $12,250.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $19,500.00 | $29,500.00 |
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
| Capital at Risk | $19,500.00 | $29,500.00 |
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
| Capital at Risk | $19,500.00 | $24,500.00 |
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
| Capital at Risk | $19,500.00 | $31,000.00 |
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
- Strategy Code: SPR
- Margin Classification: SPR

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
| Max Loss | Unlimited | -$18,820.00 |
| Risk Reward | 0.02x | 0.06x |
| Capital at Risk | $18,820.00 | $28,820.00 |
| Cost Credit | Credit $380.00 | Credit $380.00 |
| Pop | 62.6% | 62.6% |
| Margin Proxy | 18820.0 | — |

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
| 85.00 | Downside (15%) | -320.00 | -1500.00 | -1820.00 | -0.0170 | -0.0632 |
| 92.00 | Lower Strike | 380.00 | -800.00 | -420.00 | 0.0202 | -0.0146 |
| 96.20 | Breakeven 1 | 380.00 | -380.00 | 0.00 | 0.0202 | 0.0000 |
| 100.00 | Current Market Price | 380.00 | 0.00 | 380.00 | 0.0202 | 0.0132 |
| 108.00 | Upper Strike | 380.00 | 800.00 | 1180.00 | 0.0202 | 0.0409 |
| 115.00 | Upside (15%) | -320.00 | 1500.00 | 1180.00 | -0.0170 | 0.0409 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -18820.00 | -0.6530 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | -1820.00 | -0.0632 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | -420.00 | -0.0146 |
| breakeven_1 | Breakeven 1 | 96.20 | -3.80% | 380.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 380.00 | 0.0132 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | 1180.00 | 0.0409 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | 1180.00 | 0.0409 |
| infinity | Stock to Infinity | — | — | Unlimited | 1180.00 | 0.0409 |

---

### Covered Short Strangle (ID=46) — avg_cost=spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 100.0
- Strategy Code: SPR
- Margin Classification: SPR

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
| Max Loss | Unlimited | -$18,820.00 |
| Risk Reward | 0.02x | 0.06x |
| Capital at Risk | $18,820.00 | $28,820.00 |
| Cost Credit | Credit $380.00 | Credit $380.00 |
| Pop | 62.6% | 62.6% |
| Margin Proxy | 18820.0 | — |

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
| 85.00 | Downside (15%) | -320.00 | -1500.00 | -1820.00 | -0.0170 | -0.0632 |
| 92.00 | Lower Strike | 380.00 | -800.00 | -420.00 | 0.0202 | -0.0146 |
| 96.20 | Breakeven 1 | 380.00 | -380.00 | 0.00 | 0.0202 | 0.0000 |
| 100.00 | Current Market Price | 380.00 | 0.00 | 380.00 | 0.0202 | 0.0132 |
| 108.00 | Upper Strike | 380.00 | 800.00 | 1180.00 | 0.0202 | 0.0409 |
| 115.00 | Upside (15%) | -320.00 | 1500.00 | 1180.00 | -0.0170 | 0.0409 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -18820.00 | -0.6530 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | -1820.00 | -0.0632 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | -420.00 | -0.0146 |
| breakeven_1 | Breakeven 1 | 96.20 | -3.80% | 380.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 380.00 | 0.0132 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | 1180.00 | 0.0409 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | 1180.00 | 0.0409 |
| infinity | Stock to Infinity | — | — | Unlimited | 1180.00 | 0.0409 |

---

### Covered Short Strangle (ID=46) — avg_cost=0.5×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 50.0
- Strategy Code: SPR
- Margin Classification: SPR

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
| Max Loss | Unlimited | -$13,820.00 |
| Risk Reward | 0.02x | 0.45x |
| Capital at Risk | $18,820.00 | $23,820.00 |
| Cost Credit | Credit $380.00 | Credit $380.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 18820.0 | — |

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
| 50.00 | Scenario @ 50.00 | -3820.00 | 0.00 | -3820.00 | -0.2030 | -0.1604 |
| 69.10 | Breakeven 1 | -1910.00 | 1910.00 | 0.00 | -0.1015 | 0.0000 |
| 85.00 | Downside (15%) | -320.00 | 3500.00 | 3180.00 | -0.0170 | 0.1335 |
| 92.00 | Lower Strike | 380.00 | 4200.00 | 4580.00 | 0.0202 | 0.1923 |
| 100.00 | Current Market Price | 380.00 | 5000.00 | 5380.00 | 0.0202 | 0.2259 |
| 108.00 | Upper Strike | 380.00 | 5800.00 | 6180.00 | 0.0202 | 0.2594 |
| 115.00 | Upside (15%) | -320.00 | 6500.00 | 6180.00 | -0.0170 | 0.2594 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -13820.00 | -0.5802 |
| breakeven_1 | Breakeven 1 | 69.10 | -30.90% | -1910.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | 3180.00 | 0.1335 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | 4580.00 | 0.1923 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 5380.00 | 0.2259 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | 6180.00 | 0.2594 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | 6180.00 | 0.2594 |
| infinity | Stock to Infinity | — | — | Unlimited | 6180.00 | 0.2594 |

---

### Covered Short Strangle (ID=46) — avg_cost=1.15×spot

**Inputs:**

- Spot: 100.0
- Stock Position: 100.0
- Avg Cost: 114.99999999999999
- Strategy Code: SPR
- Margin Classification: SPR

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
| Max Loss | Unlimited | -$20,320.00 |
| Risk Reward | 0.02x | 0.02x |
| Capital at Risk | $18,820.00 | $30,320.00 |
| Cost Credit | Credit $380.00 | Credit $380.00 |
| Pop | 0.0% | 0.0% |
| Margin Proxy | 18820.0 | — |

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
| 85.00 | Downside (15%) | -320.00 | -3000.00 | -3320.00 | -0.0170 | -0.1095 |
| 92.00 | Lower Strike | 380.00 | -2300.00 | -1920.00 | 0.0202 | -0.0633 |
| 100.00 | Current Market Price | 380.00 | -1500.00 | -1120.00 | 0.0202 | -0.0369 |
| 108.00 | Upper Strike | 380.00 | -700.00 | -320.00 | 0.0202 | -0.0106 |
| 115.00 | Upside (15%) | -320.00 | 0.00 | -320.00 | -0.0170 | -0.0106 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -8820.00 | -20320.00 | -0.6702 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -320.00 | -3320.00 | -0.1095 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 380.00 | -1920.00 | -0.0633 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | -1120.00 | -0.0369 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 380.00 | -320.00 | -0.0106 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -320.00 | -320.00 | -0.0106 |
| infinity | Stock to Infinity | — | — | Unlimited | -320.00 | -0.0106 |

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
- Breakevens: []
- Options Max PnL: 0.0
- Options Min PnL: 0.0
- Combined Max PnL: 0.0
- Combined Min PnL: 0.0

**Net Premium:**

- Per Share: 16.0
- Total: 1600.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | $0.00 |
| Max Loss | $0.00 | $0.00 |
| Risk Reward | N/A | N/A |
| Capital at Risk | $1.00 | $1.00 |
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
| 85.00 | Downside (15%) | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 92.00 | Lower Strike | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | 0.00 | 0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 0.00 | 0.0000 |
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
- Options Min PnL: 0.0
- Combined Max PnL: 20000.0
- Combined Min PnL: -10000.0

**Net Premium:**

- Per Share: 16.0
- Total: 1600.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | $0.00 | -$10,000.00 |
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $2,780.00 | $12,780.00 |
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
| 85.00 | Downside (15%) | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.1500 |
| 92.00 | Lower Strike | 0.00 | -800.00 | -800.00 | 0.0000 | -0.0800 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | 0.00 | 800.00 | 800.00 | 0.0000 | 0.0800 |
| 115.00 | Upside (15%) | 0.00 | 1500.00 | 1500.00 | 0.0000 | 0.1500 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -10000.00 | -0.7825 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | -1500.00 | -0.1500 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | -800.00 | -0.0800 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 800.00 | 0.0800 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 1500.00 | 0.1500 |
| infinity | Stock to Infinity | — | — | 0.00 | Unlimited | Unlimited |

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
- Options Min PnL: 0.0
- Combined Max PnL: 25000.0
- Combined Min PnL: -5000.0

**Net Premium:**

- Per Share: 16.0
- Total: 1600.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | $0.00 | -$5,000.00 |
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $2,780.00 | $7,780.00 |
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
| 85.00 | Downside (15%) | 0.00 | 3500.00 | 3500.00 | 0.0000 | 0.7000 |
| 92.00 | Lower Strike | 0.00 | 4200.00 | 4200.00 | 0.0000 | 0.8400 |
| 100.00 | Current Market Price | 0.00 | 5000.00 | 5000.00 | 0.0000 | 1.0000 |
| 108.00 | Upper Strike | 0.00 | 5800.00 | 5800.00 | 0.0000 | 1.1600 |
| 115.00 | Upside (15%) | 0.00 | 6500.00 | 6500.00 | 0.0000 | 1.3000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -5000.00 | -0.6427 |
| breakeven_1 | Breakeven 1 | 50.00 | -50.00% | 0.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | 3500.00 | 0.7000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | 4200.00 | 0.8400 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 1.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 5800.00 | 1.1600 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 6500.00 | 1.3000 |
| infinity | Stock to Infinity | — | — | 0.00 | Unlimited | Unlimited |

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
- Options Min PnL: 0.0
- Combined Max PnL: 18500.0
- Combined Min PnL: -11500.0

**Net Premium:**

- Per Share: 16.0
- Total: 1600.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | $0.00 | -$11,500.00 |
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $2,780.00 | $14,280.00 |
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
| 85.00 | Downside (15%) | 0.00 | -3000.00 | -3000.00 | 0.0000 | -0.2609 |
| 92.00 | Lower Strike | 0.00 | -2300.00 | -2300.00 | 0.0000 | -0.2000 |
| 100.00 | Current Market Price | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.1304 |
| 108.00 | Upper Strike | 0.00 | -700.00 | -700.00 | 0.0000 | -0.0609 |
| 115.00 | Upside (15%) | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -11500.00 | -0.8053 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | -3000.00 | -0.2609 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | -2300.00 | -0.2000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.1304 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | -700.00 | -0.0609 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 115.00 | 15.00% | 0.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 0.00 | Unlimited | Unlimited |

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
- Breakevens: []
- Options Max PnL: 0.0
- Options Min PnL: 0.0
- Combined Max PnL: 0.0
- Combined Min PnL: 0.0

**Net Premium:**

- Per Share: -16.0
- Total: -1600.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | $0.00 |
| Max Loss | $0.00 | $0.00 |
| Risk Reward | N/A | N/A |
| Capital at Risk | $1.00 | $1.00 |
| Cost Credit | Credit $1,600.00 | Credit $1,600.00 |
| Pop | 64.8% | 64.8% |
| Margin Proxy | 1.0 | — |

**Probabilities:**

- PoP (raw): 0.647643
- Assignment Prob: 1.0
- P(25% Max Profit): 1e-06
- P(50% Max Profit): 1e-06
- P(100% Max Profit): 1e-06
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 92.00 | Lower Strike | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | 0.00 | 0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 0.00 | 0.0000 |
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
- Options Min PnL: 0.0
- Combined Max PnL: 20000.0
- Combined Min PnL: -10000.0

**Net Premium:**

- Per Share: -16.0
- Total: -1600.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | $0.00 | -$10,000.00 |
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $5,980.00 | $15,980.00 |
| Cost Credit | Credit $1,600.00 | Credit $1,600.00 |
| Pop | 47.9% | 47.9% |
| Margin Proxy | 5980.0 | — |

**Probabilities:**

- PoP (raw): 0.47931
- Assignment Prob: 1.0
- P(25% Max Profit): 1e-06
- P(50% Max Profit): 1e-06
- P(100% Max Profit): 1e-06
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.1500 |
| 92.00 | Lower Strike | 0.00 | -800.00 | -800.00 | 0.0000 | -0.0800 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | 0.00 | 800.00 | 800.00 | 0.0000 | 0.0800 |
| 115.00 | Upside (15%) | 0.00 | 1500.00 | 1500.00 | 0.0000 | 0.1500 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -10000.00 | -0.6258 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | -1500.00 | -0.1500 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | -800.00 | -0.0800 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 800.00 | 0.0800 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 1500.00 | 0.1500 |
| infinity | Stock to Infinity | — | — | 0.00 | Unlimited | Unlimited |

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
- Options Min PnL: 0.0
- Combined Max PnL: 25000.0
- Combined Min PnL: -5000.0

**Net Premium:**

- Per Share: -16.0
- Total: -1600.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | $0.00 | -$5,000.00 |
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $5,980.00 | $10,980.00 |
| Cost Credit | Credit $1,600.00 | Credit $1,600.00 |
| Pop | 100.0% | 100.0% |
| Margin Proxy | 5980.0 | — |

**Probabilities:**

- PoP (raw): 1.0
- Assignment Prob: 1.0
- P(25% Max Profit): 1e-06
- P(50% Max Profit): 1e-06
- P(100% Max Profit): 1e-06
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 50.00 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 85.00 | Downside (15%) | 0.00 | 3500.00 | 3500.00 | 0.0000 | 0.7000 |
| 92.00 | Lower Strike | 0.00 | 4200.00 | 4200.00 | 0.0000 | 0.8400 |
| 100.00 | Current Market Price | 0.00 | 5000.00 | 5000.00 | 0.0000 | 1.0000 |
| 108.00 | Upper Strike | 0.00 | 5800.00 | 5800.00 | 0.0000 | 1.1600 |
| 115.00 | Upside (15%) | 0.00 | 6500.00 | 6500.00 | 0.0000 | 1.3000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -5000.00 | -0.4554 |
| breakeven_1 | Breakeven 1 | 50.00 | -50.00% | 0.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | 3500.00 | 0.7000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | 4200.00 | 0.8400 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 5000.00 | 1.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 5800.00 | 1.1600 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 6500.00 | 1.3000 |
| infinity | Stock to Infinity | — | — | 0.00 | Unlimited | Unlimited |

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
- Options Min PnL: 0.0
- Combined Max PnL: 18500.0
- Combined Min PnL: -11500.0

**Net Premium:**

- Per Share: -16.0
- Total: -1600.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $0.00 | Unlimited |
| Max Loss | $0.00 | -$11,500.00 |
| Risk Reward | N/A | Unlimited |
| Capital at Risk | $5,980.00 | $17,480.00 |
| Cost Credit | Credit $1,600.00 | Credit $1,600.00 |
| Pop | 8.1% | 8.1% |
| Margin Proxy | 5980.0 | — |

**Probabilities:**

- PoP (raw): 0.081123
- Assignment Prob: 1.0
- P(25% Max Profit): 1e-06
- P(50% Max Profit): 1e-06
- P(100% Max Profit): 1e-06
- IV Used: 0.25

**Scenario Table:**

| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |
|-------|----------|---------|-----------|--------------|---------|--------|
| 85.00 | Downside (15%) | 0.00 | -3000.00 | -3000.00 | 0.0000 | -0.2609 |
| 92.00 | Lower Strike | 0.00 | -2300.00 | -2300.00 | 0.0000 | -0.2000 |
| 100.00 | Current Market Price | 0.00 | -1500.00 | -1500.00 | 0.0000 | -0.1304 |
| 108.00 | Upper Strike | 0.00 | -700.00 | -700.00 | 0.0000 | -0.0609 |
| 115.00 | Upside (15%) | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 0.00 | -11500.00 | -0.6579 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 0.00 | -3000.00 | -0.2609 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | -2300.00 | -0.2000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | -1500.00 | -0.1304 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | -700.00 | -0.0609 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 115.00 | 15.00% | 0.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 0.00 | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $2,250.00 | $2,250.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $2,250.00 | $12,250.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $2,250.00 | $7,250.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $2,250.00 | $13,750.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $2,250.00 | $2,250.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
- Breakevens: []
- Options Max PnL: 10000.0
- Options Min PnL: -20000.0
- Combined Max PnL: 0.0
- Combined Min PnL: 0.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $10,000.00 | $0.00 |
| Max Loss | Unlimited | $0.00 |
| Risk Reward | 0.50x | N/A |
| Capital at Risk | $5,250.00 | $15,250.00 |
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
| 85.00 | Downside (15%) | 1500.00 | -1500.00 | 0.00 | 0.2857 | 0.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -1500.00 | 1500.00 | 0.00 | -0.2857 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 10000.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1500.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1500.00 | 0.00 | 0.0000 |
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
| Capital at Risk | $5,250.00 | $10,250.00 |
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
| Capital at Risk | $5,250.00 | $16,750.00 |
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
- Breakevens: [100.0]
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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $1,390.00 | $1,390.00 |
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
| 92.00 | Lower Strike | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | 700.00 | 0.00 | 700.00 | 0.0761 | 0.0761 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9200.00 | -9200.00 | -6.6187 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -700.00 | -700.00 | -0.0761 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 700.00 | 700.00 | 0.0761 |
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $1,390.00 | $11,390.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $1,390.00 | $6,390.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | Unlimited |
| Capital at Risk | $1,390.00 | $12,890.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
- Breakevens: [100.0]
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
| Capital at Risk | $1,390.00 | $1,390.00 |
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
| 92.00 | Lower Strike | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 108.00 | Upper Strike | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -700.00 | 0.00 | -700.00 | -0.5036 | -0.5036 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 9200.00 | 9200.00 | 6.6187 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 700.00 | 700.00 | 0.5036 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 0.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| breakeven_1 | Breakeven 1 | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -700.00 | -700.00 | -0.5036 |
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Max Loss | Unlimited | -$800.00 |
| Risk Reward | 0.48x | 1.00x |
| Capital at Risk | $5,190.00 | $15,190.00 |
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
| Max Loss | Unlimited | $4,200.00 |
| Risk Reward | 0.48x | 1.38x |
| Capital at Risk | $5,190.00 | $10,190.00 |
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
| Max Loss | Unlimited | -$2,300.00 |
| Risk Reward | 0.48x | 0.30x |
| Capital at Risk | $5,190.00 | $16,690.00 |
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
| Risk Reward | Unlimited | N/A |
| Capital at Risk | $500.00 | $10,500.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | N/A |
| Capital at Risk | $500.00 | $10,500.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | N/A |
| Capital at Risk | $500.00 | $5,500.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | N/A |
| Capital at Risk | $500.00 | $12,000.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | 39.00x | N/A |
| Capital at Risk | $5,500.00 | $15,500.00 |
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
| infinity | Stock to Infinity | — | — | -500.00 | Unlimited | Unlimited |

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
| Risk Reward | 39.00x | N/A |
| Capital at Risk | $5,500.00 | $15,500.00 |
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
| infinity | Stock to Infinity | — | — | -500.00 | Unlimited | Unlimited |

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
| Risk Reward | 39.00x | N/A |
| Capital at Risk | $5,500.00 | $10,500.00 |
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
| infinity | Stock to Infinity | — | — | -500.00 | Unlimited | Unlimited |

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
| Risk Reward | 39.00x | N/A |
| Capital at Risk | $5,500.00 | $17,000.00 |
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
| infinity | Stock to Infinity | — | — | -500.00 | Unlimited | Unlimited |

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
| Capital at Risk | $5,000.00 | $15,000.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $5,000.00 | $15,000.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $5,000.00 | $10,000.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $5,000.00 | $16,500.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $4,500.00 | $14,500.00 |
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
| infinity | Stock to Infinity | — | — | 500.00 | Unlimited | Unlimited |

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
| Capital at Risk | $4,500.00 | $14,500.00 |
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
| infinity | Stock to Infinity | — | — | 500.00 | Unlimited | Unlimited |

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
| Capital at Risk | $4,500.00 | $9,500.00 |
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
| infinity | Stock to Infinity | — | — | 500.00 | Unlimited | Unlimited |

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
| Capital at Risk | $4,500.00 | $16,000.00 |
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
| 80.00 | Breakeven 1 | -3500.00 | 3500.00 | 0.00 | -0.1795 | 0.0000 |
| 85.00 | Downside (15%) | -2500.00 | 3000.00 | 500.00 | -0.1282 | 0.0161 |
| 100.00 | Current Market Price | 500.00 | 1500.00 | 2000.00 | 0.0256 | 0.0645 |
| 115.00 | Upside (15%) | 500.00 | 0.00 | 500.00 | 0.0256 | 0.0161 |
| 120.00 | Breakeven 2 | 500.00 | -500.00 | 0.00 | 0.0256 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -19500.00 | -8000.00 | -0.5000 |
| breakeven_1 | Breakeven 1 | 80.00 | -20.00% | -3500.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -2500.00 | 500.00 | 0.0161 |
| spot | Current Market Price | 100.00 | 0.00% | 500.00 | 2000.00 | 0.0645 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 500.00 | 2000.00 | 0.0645 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 500.00 | 500.00 | 0.0161 |
| breakeven_2 | Breakeven 2 | 120.00 | 20.00% | 500.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 500.00 | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | N/A |
| Capital at Risk | $1,180.00 | $11,180.00 |
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
| 88.20 | Breakeven 1 | -1180.00 | 1180.00 | 0.00 | -1.0000 | 0.0000 |
| 92.00 | Lower Strike | -1180.00 | 800.00 | -380.00 | -1.0000 | -0.0340 |
| 100.00 | Current Market Price | -380.00 | 0.00 | -380.00 | -0.3220 | -0.0340 |
| 108.00 | Upper Strike | 420.00 | -800.00 | -380.00 | 0.3559 | -0.0340 |
| 111.80 | Breakeven 2 | 1180.00 | -1180.00 | 0.00 | 1.0000 | 0.0000 |
| 115.00 | Upside (15%) | 1820.00 | -1500.00 | 320.00 | 1.5424 | 0.0286 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1180.00 | 8820.00 | 0.7889 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1180.00 | 320.00 | 0.0286 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | -1180.00 | 0.00 | 0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -1180.00 | -380.00 | -0.0340 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -380.00 | -0.0340 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 420.00 | -380.00 | -0.0340 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | 1180.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1820.00 | 320.00 | 0.0286 |
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | N/A |
| Capital at Risk | $1,180.00 | $11,180.00 |
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
| 88.20 | Breakeven 1 | -1180.00 | 1180.00 | 0.00 | -1.0000 | 0.0000 |
| 92.00 | Lower Strike | -1180.00 | 800.00 | -380.00 | -1.0000 | -0.0340 |
| 100.00 | Current Market Price | -380.00 | 0.00 | -380.00 | -0.3220 | -0.0340 |
| 108.00 | Upper Strike | 420.00 | -800.00 | -380.00 | 0.3559 | -0.0340 |
| 111.80 | Breakeven 2 | 1180.00 | -1180.00 | 0.00 | 1.0000 | 0.0000 |
| 115.00 | Upside (15%) | 1820.00 | -1500.00 | 320.00 | 1.5424 | 0.0286 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -1180.00 | 8820.00 | 0.7889 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1180.00 | 320.00 | 0.0286 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | -1180.00 | 0.00 | 0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -1180.00 | -380.00 | -0.0340 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -380.00 | -0.0340 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 420.00 | -380.00 | -0.0340 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | 1180.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1820.00 | 320.00 | 0.0286 |
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | N/A |
| Capital at Risk | $1,180.00 | $6,180.00 |
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
| 38.20 | Breakeven 1 | -1180.00 | 1180.00 | 0.00 | -1.0000 | 0.0000 |
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
| breakeven_1 | Breakeven 1 | 38.20 | -61.80% | -1180.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1180.00 | -4680.00 | -0.7573 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -1180.00 | -5380.00 | -0.8706 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -5380.00 | -0.8706 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 420.00 | -5380.00 | -0.8706 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1820.00 | -4680.00 | -0.7573 |
| breakeven_2 | Breakeven 2 | 161.80 | 61.80% | 11180.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | Unlimited | N/A |
| Capital at Risk | $1,180.00 | $12,680.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Risk Reward | 15.95x | N/A |
| Capital at Risk | $6,180.00 | $16,180.00 |
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
| 88.20 | Breakeven 1 | 1180.00 | -1180.00 | 0.00 | 1.0000 | 0.0000 |
| 92.00 | Lower Strike | 420.00 | -800.00 | -380.00 | 0.3559 | -0.0340 |
| 100.00 | Current Market Price | -380.00 | 0.00 | -380.00 | -0.3220 | -0.0340 |
| 108.00 | Upper Strike | -1180.00 | 800.00 | -380.00 | -1.0000 | -0.0340 |
| 111.80 | Breakeven 2 | -1180.00 | 1180.00 | 0.00 | -1.0000 | 0.0000 |
| 115.00 | Upside (15%) | -1180.00 | 1500.00 | 320.00 | -1.0000 | 0.0286 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 18820.00 | 8820.00 | 0.5451 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1820.00 | 320.00 | 0.0286 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | 1180.00 | 0.00 | 0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 420.00 | -380.00 | -0.0340 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -380.00 | -0.0340 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -1180.00 | -380.00 | -0.0340 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | -1180.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1180.00 | 320.00 | 0.0286 |
| infinity | Stock to Infinity | — | — | -1180.00 | Unlimited | Unlimited |

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
| Risk Reward | 15.95x | N/A |
| Capital at Risk | $6,180.00 | $16,180.00 |
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
| 88.20 | Breakeven 1 | 1180.00 | -1180.00 | 0.00 | 1.0000 | 0.0000 |
| 92.00 | Lower Strike | 420.00 | -800.00 | -380.00 | 0.3559 | -0.0340 |
| 100.00 | Current Market Price | -380.00 | 0.00 | -380.00 | -0.3220 | -0.0340 |
| 108.00 | Upper Strike | -1180.00 | 800.00 | -380.00 | -1.0000 | -0.0340 |
| 111.80 | Breakeven 2 | -1180.00 | 1180.00 | 0.00 | -1.0000 | 0.0000 |
| 115.00 | Upside (15%) | -1180.00 | 1500.00 | 320.00 | -1.0000 | 0.0286 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 18820.00 | 8820.00 | 0.5451 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1820.00 | 320.00 | 0.0286 |
| breakeven_1 | Breakeven 1 | 88.20 | -11.80% | 1180.00 | 0.00 | 0.0000 |
| strike_1 | Lower Strike | 92.00 | -8.00% | 420.00 | -380.00 | -0.0340 |
| spot | Current Market Price | 100.00 | 0.00% | -380.00 | -380.00 | -0.0340 |
| strike_2 | Upper Strike | 108.00 | 8.00% | -1180.00 | -380.00 | -0.0340 |
| breakeven_2 | Breakeven 2 | 111.80 | 11.80% | -1180.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1180.00 | 320.00 | 0.0286 |
| infinity | Stock to Infinity | — | — | -1180.00 | Unlimited | Unlimited |

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
| Risk Reward | 15.95x | N/A |
| Capital at Risk | $6,180.00 | $11,180.00 |
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
| infinity | Stock to Infinity | — | — | -1180.00 | Unlimited | Unlimited |

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
| Risk Reward | 15.95x | N/A |
| Capital at Risk | $6,180.00 | $17,680.00 |
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
| infinity | Stock to Infinity | — | — | -1180.00 | Unlimited | Unlimited |

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
| Capital at Risk | $5,000.00 | $15,000.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $5,000.00 | $15,000.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $5,000.00 | $10,000.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $5,000.00 | $16,500.00 |
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
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Capital at Risk | $4,380.00 | $14,380.00 |
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
| infinity | Stock to Infinity | — | — | 1180.00 | Unlimited | Unlimited |

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
| Capital at Risk | $4,380.00 | $14,380.00 |
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
| infinity | Stock to Infinity | — | — | 1180.00 | Unlimited | Unlimited |

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
| Capital at Risk | $4,380.00 | $9,380.00 |
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
| infinity | Stock to Infinity | — | — | 1180.00 | Unlimited | Unlimited |

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
| Capital at Risk | $4,380.00 | $15,880.00 |
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
| 73.20 | Breakeven 1 | -4180.00 | 4180.00 | 0.00 | -0.2221 | 0.0000 |
| 85.00 | Downside (15%) | -1820.00 | 3000.00 | 1180.00 | -0.0967 | 0.0389 |
| 92.00 | Lower Strike | -420.00 | 2300.00 | 1880.00 | -0.0223 | 0.0620 |
| 100.00 | Current Market Price | 380.00 | 1500.00 | 1880.00 | 0.0202 | 0.0620 |
| 108.00 | Upper Strike | 1180.00 | 700.00 | 1880.00 | 0.0627 | 0.0620 |
| 115.00 | Upside (15%) | 1180.00 | 0.00 | 1180.00 | 0.0627 | 0.0389 |
| 126.80 | Breakeven 2 | 1180.00 | -1180.00 | 0.00 | 0.0627 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -18820.00 | -7320.00 | -0.4610 |
| breakeven_1 | Breakeven 1 | 73.20 | -26.80% | -4180.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1820.00 | 1180.00 | 0.0389 |
| strike_1 | Lower Strike | 92.00 | -8.00% | -420.00 | 1880.00 | 0.0620 |
| spot | Current Market Price | 100.00 | 0.00% | 380.00 | 1880.00 | 0.0620 |
| strike_2 | Upper Strike | 108.00 | 8.00% | 1180.00 | 1880.00 | 0.0620 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 1180.00 | 1180.00 | 0.0389 |
| breakeven_2 | Breakeven 2 | 126.80 | 26.80% | 1180.00 | 0.00 | 0.0000 |
| infinity | Stock to Infinity | — | — | 1180.00 | Unlimited | Unlimited |

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
| Capital at Risk | $10,800.00 | $10,800.00 |
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
| 98.10 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0194 | 0.0194 |
| 108.00 | Strike | 990.00 | 0.00 | 990.00 | 0.1009 | 0.1009 |
| 115.00 | Upside (15%) | 990.00 | 0.00 | 990.00 | 0.1009 | 0.1009 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9810.00 | -9810.00 | -0.9083 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1310.00 | -1310.00 | -0.1335 |
| breakeven_1 | Breakeven 1 | 98.10 | -1.90% | 0.00 | 0.00 | 0.0000 |
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
| Risk Reward | 0.10x | Unlimited |
| Capital at Risk | $2,990.00 | $12,990.00 |
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
| 99.05 | Breakeven 1 | 95.00 | -95.00 | 0.00 | 0.0097 | 0.0000 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0194 | 0.0096 |
| 108.00 | Strike | 990.00 | 800.00 | 1790.00 | 0.1009 | 0.0904 |
| 115.00 | Upside (15%) | 990.00 | 1500.00 | 2490.00 | 0.1009 | 0.1257 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9810.00 | -19810.00 | -1.5250 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1310.00 | -2810.00 | -0.1418 |
| breakeven_1 | Breakeven 1 | 99.05 | -0.95% | 95.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0096 |
| strike_1 | Strike | 108.00 | 8.00% | 990.00 | 1790.00 | 0.0904 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 990.00 | 2490.00 | 0.1257 |
| infinity | Stock to Infinity | — | — | 990.00 | Unlimited | Unlimited |

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
| Risk Reward | 0.10x | Unlimited |
| Capital at Risk | $2,990.00 | $7,990.00 |
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
| 74.05 | Breakeven 1 | -2405.00 | 2405.00 | 0.00 | -0.2452 | 0.0000 |
| 85.00 | Downside (15%) | -1310.00 | 3500.00 | 2190.00 | -0.1335 | 0.1479 |
| 100.00 | Current Market Price | 190.00 | 5000.00 | 5190.00 | 0.0194 | 0.3504 |
| 108.00 | Strike | 990.00 | 5800.00 | 6790.00 | 0.1009 | 0.4585 |
| 115.00 | Upside (15%) | 990.00 | 6500.00 | 7490.00 | 0.1009 | 0.5057 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | -9810.00 | -14810.00 | -1.8536 |
| breakeven_1 | Breakeven 1 | 74.05 | -25.95% | -2405.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | -1310.00 | 2190.00 | 0.1479 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 5190.00 | 0.3504 |
| strike_1 | Strike | 108.00 | 8.00% | 990.00 | 6790.00 | 0.4585 |
| upside | Upside Target (15%) | 115.00 | 15.00% | 990.00 | 7490.00 | 0.5057 |
| infinity | Stock to Infinity | — | — | 990.00 | Unlimited | Unlimited |

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
| Risk Reward | 0.10x | Unlimited |
| Capital at Risk | $2,990.00 | $14,490.00 |
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
| infinity | Stock to Infinity | — | — | 990.00 | Unlimited | Unlimited |

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
| Capital at Risk | $2,990.00 | $2,990.00 |
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
| 101.90 | Breakeven 1 | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -1310.00 | 0.00 | -1310.00 | -0.4381 | -0.4381 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 990.00 | 990.00 | 0.3311 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 990.00 | 990.00 | 0.3311 |
| strike_1 | Strike | 92.00 | -8.00% | 990.00 | 990.00 | 0.3311 |
| spot | Current Market Price | 100.00 | 0.00% | 190.00 | 190.00 | 0.0635 |
| breakeven_1 | Breakeven 1 | 101.90 | 1.90% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1310.00 | -1310.00 | -0.4381 |
| infinity | Stock to Infinity | — | — | Unlimited | Unlimited | Unlimited |

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
| Max Loss | Unlimited | -$9,010.00 |
| Risk Reward | 0.05x | 0.02x |
| Capital at Risk | $5,000.00 | $15,000.00 |
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
| 90.10 | Breakeven 1 | 990.00 | -990.00 | 0.00 | 0.1980 | 0.0000 |
| 92.00 | Strike | 990.00 | -800.00 | 190.00 | 0.1980 | 0.0127 |
| 100.00 | Current Market Price | 190.00 | 0.00 | 190.00 | 0.0380 | 0.0127 |
| 115.00 | Upside (15%) | -1310.00 | 1500.00 | 190.00 | -0.2620 | 0.0127 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 990.00 | -9010.00 | -0.6007 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 990.00 | -510.00 | -0.0340 |
| breakeven_1 | Breakeven 1 | 90.10 | -9.90% | 990.00 | 0.00 | 0.0000 |
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
| Max Loss | Unlimited | -$4,010.00 |
| Risk Reward | 0.05x | 1.29x |
| Capital at Risk | $5,000.00 | $10,000.00 |
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
| Max Loss | Unlimited | -$10,510.00 |
| Risk Reward | 0.05x | 0.12x |
| Capital at Risk | $5,000.00 | $16,500.00 |
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
- Breakevens: []
- Options Max PnL: 10000.0
- Options Min PnL: -20000.0
- Combined Max PnL: 0.0
- Combined Min PnL: 0.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $10,000.00 | $0.00 |
| Max Loss | Unlimited | $0.00 |
| Risk Reward | 0.50x | N/A |
| Capital at Risk | $5,250.00 | $15,250.00 |
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
| 85.00 | Downside (15%) | 1500.00 | -1500.00 | 0.00 | 0.2857 | 0.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -1500.00 | 1500.00 | 0.00 | -0.2857 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 10000.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1500.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1500.00 | 0.00 | 0.0000 |
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
- Breakevens: []
- Options Max PnL: 10000.0
- Options Min PnL: -20000.0
- Combined Max PnL: 0.0
- Combined Min PnL: 0.0

**Net Premium:**

- Per Share: 0.0
- Total: 0.0

**Summary Metrics:**

| Metric | Options | Combined |
|--------|---------|----------|
| Max Profit | $10,000.00 | $0.00 |
| Max Loss | Unlimited | $0.00 |
| Risk Reward | 0.50x | N/A |
| Capital at Risk | $5,250.00 | $15,250.00 |
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
| 85.00 | Downside (15%) | 1500.00 | -1500.00 | 0.00 | 0.2857 | 0.0000 |
| 100.00 | Current Market Price | 0.00 | 0.00 | 0.00 | 0.0000 | 0.0000 |
| 115.00 | Upside (15%) | -1500.00 | 1500.00 | 0.00 | -0.2857 | 0.0000 |

**Key Levels:**

| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |
|----|-------|-------|--------|---------|---------|--------|
| zero | Stock to Zero | 0.00 | -100.00% | 10000.00 | 0.00 | 0.0000 |
| downside | Downside Target (15%) | 85.00 | -15.00% | 1500.00 | 0.00 | 0.0000 |
| spot | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| strike_1 | Current Market Price | 100.00 | 0.00% | 0.00 | 0.00 | 0.0000 |
| upside | Upside Target (15%) | 115.00 | 15.00% | -1500.00 | 0.00 | 0.0000 |
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
| Capital at Risk | $5,250.00 | $10,250.00 |
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
| Capital at Risk | $5,250.00 | $16,750.00 |
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

