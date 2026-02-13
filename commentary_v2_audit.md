# Commentary V2 Audit Report

Generated: 2026-02-13

## Summary
- Total runs (strategy x scenario): 155
- Total test cases: 465 (strategies x scenarios x zones)
- Issues found: 1033
- Unique strategies with issues: 63 / 63
- Clean strategies: 0 / 63
- Errors: 0

## Issue Categories
| Check ID | Count | Example Strategy |
|----------|-------|------------------|
| CAPITAL_AT_RISK | 154 | Short Stock |
| DECLINE_RISING | 14 | Short Put |
| ENHANCEMENT | 40 | Covered Call |
| GAIN_NEGATIVE | 24 | Covered Call |
| LOCKED_IN | 18 | Short Call |
| LOSS_POSITIVE | 18 | Covered Call |
| MD_BOLD | 602 | Custom Strategy |
| MISLEADING_DOWNSIDE | 9 | Custom Strategy |
| RETURN_ON_CAPITAL | 136 | Short Stock |
| SIGNIFICANT_LEVERAGE | 18 | Long Put |

## Detailed Findings

### Strategy: Custom Strategy (ID=1) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum loss is **−$10,000.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$10,000.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum loss is **−$10,000.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot)."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,500.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). There is no cap on upside gains."

### Strategy: Custom Strategy (ID=1) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$3,000.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$3,000.00** — the shares lose −$3,000.00 and the options add $0.00. Maximum loss is **−$11,500.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$11,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$3,000.00** — the shares lose −$3,000.00 and the options add $0.00. Maximum loss is **−$11,500.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,500.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $115.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $115.00 (15.0% above spot). There is no cap on upside gains."

### Strategy: Custom Strategy (ID=1) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$6,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$6,500.00** — the shares lose −$6,500.00 and the options add $0.00. Maximum loss is **−$15,000.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$15,000.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$6,500.00** — the shares lose −$6,500.00 and the options add $0.00. Maximum loss is **−$15,000.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$5,000.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **−$5,000.00** — the shares lose −$5,000.00 and the options add $0.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$3,500.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $115.00, the client's combined position is **−$3,500.00** — the shares lose −$3,500.00 and the options add $0.00. Breakeven is $150.00 (50.0% above spot). There is no cap on upside gains."

### Strategy: Custom Strategy (ID=1) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $85.00 (15.0% below spot). Maximum loss is **−$8,500.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$8,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $85.00 (15.0% below spot). Maximum loss is **−$8,500.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,500.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$3,000.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$3,000.00** — the shares gain +$3,000.00 and the options add $0.00. There is no cap on upside gains."

### Strategy: Custom Strategy (ID=1) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$3,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **+$3,500.00** — the shares gain +$3,500.00 and the options add $0.00. Breakeven is $50.00 (50.0% below spot). Maximum loss is **−$5,000.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$5,000.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **+$3,500.00** — the shares gain +$3,500.00 and the options add $0.00. Breakeven is $50.00 (50.0% below spot). Maximum loss is **−$5,000.00**."

**Zone**: bearish
**Check**: MISLEADING_DOWNSIDE
**Text**: "full downside exposure (avg_cost=50, spot=100.0)"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **+$3,500.00** — the shares gain +$3,500.00 and the options add $0.00. Breakeven is $50.00 (50.0% below spot). Maximum loss is **−$5,000.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,000.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **+$5,000.00** — the shares gain +$5,000.00 and the options add $0.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$6,500.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$6,500.00** — the shares gain +$6,500.00 and the options add $0.00. There is no cap on upside gains."

### Strategy: Protective Call (ID=10) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$10.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $98.00, the client's combined position is **+$10.00** — the shares gain +$200.00 and the options cost −$190.00. Breakeven is $98.10 (1.9% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$190.00**"
**Full body**: "Between $100.00 and $108.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is **−$190.00** — the shares gain $0.00 and the options cost −$190.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$990.00**"
**Full body**: "At any price above $108.00, the client's losses are capped at **−$990.00**."

### Strategy: Protective Call (ID=10) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,510.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $98.00, the client's combined position is **+$1,510.00** — the shares gain +$1,700.00 and the options cost −$190.00. There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,310.00**"
**Full body**: "Between $100.00 and $108.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is **+$1,310.00** — the shares gain +$1,500.00 and the options cost −$190.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$510.00**"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$510.00**."

### Strategy: Protective Call (ID=10) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$5,010.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $98.00, the client's combined position is **+$5,010.00** — the shares gain +$5,200.00 and the options cost −$190.00. There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$4,810.00**"
**Full body**: "Between $100.00 and $108.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is **+$4,810.00** — the shares gain +$5,000.00 and the options cost −$190.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$4,010.00**"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$4,010.00**."

### Strategy: Protective Call (ID=10) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,490.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $98.00, the client's combined position is **−$1,490.00** — the shares lose −$1,300.00 and the options cost −$190.00. Breakeven is $83.10 (16.9% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,690.00**"
**Full body**: "Between $100.00 and $108.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is **−$1,690.00** — the shares lose −$1,500.00 and the options cost −$190.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$2,490.00**"
**Full body**: "At any price above $108.00, the client's losses are capped at **−$2,490.00**."

### Strategy: Protective Call (ID=10) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$4,990.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $98.00, the client's combined position is **−$4,990.00** — the shares lose −$4,800.00 and the options cost −$190.00. Breakeven is $48.10 (51.9% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$5,190.00**"
**Full body**: "Between $100.00 and $108.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is **−$5,190.00** — the shares lose −$5,000.00 and the options cost −$190.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$5,990.00**"
**Full body**: "At any price above $108.00, the client's losses are capped at **−$5,990.00**."

### Strategy: Protective Call (ID=10) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$190.00**"
**Full body**: "Below $100.00. Maximum loss is **−$190.00** at any price below $108.00."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$190.00**"
**Full body**: "Between $100.00 and $108.00, losses are stable at **−$190.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$510.00**"
**Full body**: "Above $108.00, the position rises with the stock. At $115.00, the position is **+$510.00**. Breakeven is $109.90 (9.9% above spot). There is no cap on upside gains."

### Strategy: Protective Put (ID=11) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$990.00**"
**Full body**: "At any price below $92.00, the client's losses are capped at **−$990.00** — the long $92.00 put provides a hard floor."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$190.00**"
**Full body**: "Between $92.00 and $100.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is **−$190.00** — the shares gain $0.00 and the options cost −$190.00. The cost of protection: $190.00 (1.9% of the position) for a guaranteed loss limit at $92.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$10.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $102.00, the client's combined position is **+$10.00** — the shares gain +$200.00 and the options cost −$190.00. Breakeven is $101.90 (1.9% above spot). There is no cap on upside gains."

### Strategy: Protective Put (ID=11) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$2,490.00**"
**Full body**: "At any price below $92.00, the client's losses are capped at **−$2,490.00** — the long $92.00 put provides a hard floor."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,690.00**"
**Full body**: "Between $92.00 and $100.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is **−$1,690.00** — the shares lose −$1,500.00 and the options cost −$190.00. The cost of protection: $190.00 (1.9% of the position) for a guaranteed loss limit at $92.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,490.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $102.00, the client's combined position is **−$1,490.00** — the shares lose −$1,300.00 and the options cost −$190.00. Breakeven is $116.90 (16.9% above spot). There is no cap on upside gains."

### Strategy: Protective Put (ID=11) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$5,990.00**"
**Full body**: "At any price below $92.00, the client's losses are capped at **−$5,990.00** — the long $92.00 put provides a hard floor."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$5,190.00**"
**Full body**: "Between $92.00 and $100.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is **−$5,190.00** — the shares lose −$5,000.00 and the options cost −$190.00. The cost of protection: $190.00 (1.9% of the position) for a guaranteed loss limit at $92.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$4,990.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $102.00, the client's combined position is **−$4,990.00** — the shares lose −$4,800.00 and the options cost −$190.00. Breakeven is $151.90 (51.9% above spot). There is no cap on upside gains."

### Strategy: Protective Put (ID=11) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$510.00**"
**Full body**: "At any price below $92.00, the client's gains are locked in at **+$510.00**. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $92.00, the client's gains are locked in at **+$510.00**. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,310.00**"
**Full body**: "Between $92.00 and $100.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is **+$1,310.00** — the shares gain +$1,500.00 and the options cost −$190.00. The cost of protection: $190.00 (1.9% of the position) for a guaranteed loss limit at $92.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,510.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $102.00, the client's combined position is **+$1,510.00** — the shares gain +$1,700.00 and the options cost −$190.00. There is no cap on upside gains."

### Strategy: Protective Put (ID=11) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$4,010.00**"
**Full body**: "At any price below $92.00, the client's gains are locked in at **+$4,010.00**. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $92.00, the client's gains are locked in at **+$4,010.00**. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$4,810.00**"
**Full body**: "Between $92.00 and $100.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is **+$4,810.00** — the shares gain +$5,000.00 and the options cost −$190.00. The cost of protection: $190.00 (1.9% of the position) for a guaranteed loss limit at $92.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$5,010.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $102.00, the client's combined position is **+$5,010.00** — the shares gain +$5,200.00 and the options cost −$190.00. There is no cap on upside gains."

### Strategy: Protective Put (ID=11) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$510.00**"
**Full body**: "Below $92.00, the position gains value as the stock falls. At $85.00, the position is **+$510.00**. Breakeven is $90.10 (9.9% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$190.00**"
**Full body**: "Between $92.00 and $100.00, losses are stable at **−$190.00**. That represents significant leverage on the $190.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $100.00, losses are stable at **−$190.00**. That represents significant leverage on the $190.00 capital at risk."

**Zone**: stagnant
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $190"
**Full body**: "Between $92.00 and $100.00, losses are stable at **−$190.00**. That represents significant leverage on the $190.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$190.00**"
**Full body**: "Above $100.00. Maximum loss is **−$190.00** at any price above $92.00. That represents significant leverage on the $190.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00. Maximum loss is **−$190.00** at any price above $92.00. That represents significant leverage on the $190.00 capital at risk."

**Zone**: bullish
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $190"
**Full body**: "Above $100.00. Maximum loss is **−$190.00** at any price above $92.00. That represents significant leverage on the $190.00 capital at risk."

### Strategy: Collar (ID=12) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$800.00**"
**Full body**: "At any price below $92.00, the client's losses are capped at **−$800.00** — the long $92.00 put provides a hard floor."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 5.3% return on the $15,190.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$800.00**"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 5.3% return on the $15,190.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 5.3% return on the $15,190.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $15,190.00"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 5.3% return on the $15,190.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$800.00**"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$800.00** — the short call limits further upside. The trade-off: downside protection below $92.00 in exchange for capping gains above $108.00. That represents a 5.3% return on the $15,190.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$800.00** — the short call limits further upside. The trade-off: downside protection below $92.00 in exchange for capping gains above $108.00. That represents a 5.3% return on the $15,190.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $15,190.00"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$800.00** — the short call limits further upside. The trade-off: downside protection below $92.00 in exchange for capping gains above $108.00. That represents a 5.3% return on the $15,190.00 capital at risk."

### Strategy: Collar (ID=12) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$2,300.00**"
**Full body**: "At any price below $92.00, the client's losses are capped at **−$2,300.00** — the long $92.00 put provides a hard floor."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,500.00**"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Maximum gain is **−$700.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$700.00**"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Maximum gain is **−$700.00**."

**Zone**: stagnant
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$700.00"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Maximum gain is **−$700.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$700.00**"
**Full body**: "At any price above $108.00, the client's losses are capped at **−$700.00**. The trade-off: downside protection below $92.00 in exchange for capping gains above $108.00."

### Strategy: Collar (ID=12) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$5,800.00**"
**Full body**: "At any price below $92.00, the client's losses are capped at **−$5,800.00** — the long $92.00 put provides a hard floor."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$5,000.00**"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **−$5,000.00** — the shares lose −$5,000.00 and the options add $0.00. Maximum gain is **−$4,200.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$4,200.00**"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **−$5,000.00** — the shares lose −$5,000.00 and the options add $0.00. Maximum gain is **−$4,200.00**."

**Zone**: stagnant
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$4,200.00"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **−$5,000.00** — the shares lose −$5,000.00 and the options add $0.00. Maximum gain is **−$4,200.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$4,200.00**"
**Full body**: "At any price above $108.00, the client's losses are capped at **−$4,200.00**. The trade-off: downside protection below $92.00 in exchange for capping gains above $108.00."

### Strategy: Collar (ID=12) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$700.00**"
**Full body**: "At any price below $92.00, the client's gains are locked in at **+$700.00**. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $92.00, the client's gains are locked in at **+$700.00**. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,500.00**"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Maximum gain is **+$2,300.00**. That represents a 16.8% return on the $13,690.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$2,300.00**"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Maximum gain is **+$2,300.00**. That represents a 16.8% return on the $13,690.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Maximum gain is **+$2,300.00**. That represents a 16.8% return on the $13,690.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $13,690.00"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Maximum gain is **+$2,300.00**. That represents a 16.8% return on the $13,690.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$2,300.00**"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$2,300.00** — the short call limits further upside. The trade-off: downside protection below $92.00 in exchange for capping gains above $108.00. That represents a 16.8% return on the $13,690.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$2,300.00** — the short call limits further upside. The trade-off: downside protection below $92.00 in exchange for capping gains above $108.00. That represents a 16.8% return on the $13,690.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $13,690.00"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$2,300.00** — the short call limits further upside. The trade-off: downside protection below $92.00 in exchange for capping gains above $108.00. That represents a 16.8% return on the $13,690.00 capital at risk."

### Strategy: Collar (ID=12) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$4,200.00**"
**Full body**: "At any price below $92.00, the client's gains are locked in at **+$4,200.00**. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $92.00, the client's gains are locked in at **+$4,200.00**. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,000.00**"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **+$5,000.00** — the shares gain +$5,000.00 and the options add $0.00. Maximum gain is **+$5,800.00**. That represents a 56.9% return on the $10,190.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,800.00**"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **+$5,000.00** — the shares gain +$5,000.00 and the options add $0.00. Maximum gain is **+$5,800.00**. That represents a 56.9% return on the $10,190.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **+$5,000.00** — the shares gain +$5,000.00 and the options add $0.00. Maximum gain is **+$5,800.00**. That represents a 56.9% return on the $10,190.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $10,190.00"
**Full body**: "Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **+$5,000.00** — the shares gain +$5,000.00 and the options add $0.00. Maximum gain is **+$5,800.00**. That represents a 56.9% return on the $10,190.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$5,800.00**"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$5,800.00** — the short call limits further upside. The trade-off: downside protection below $92.00 in exchange for capping gains above $108.00. That represents a 56.9% return on the $10,190.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$5,800.00** — the short call limits further upside. The trade-off: downside protection below $92.00 in exchange for capping gains above $108.00. That represents a 56.9% return on the $10,190.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $10,190.00"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$5,800.00** — the short call limits further upside. The trade-off: downside protection below $92.00 in exchange for capping gains above $108.00. That represents a 56.9% return on the $10,190.00 capital at risk."

### Strategy: Collar (ID=12) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$700.00**"
**Full body**: "Below $92.00, the position gains value as the stock falls. At $85.00, the position is **+$700.00**. Breakeven is $92.00 (8.0% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Between $92.00 and $108.00, the position captures its maximum gain of **$0.00**. Breakevens are $99.33 (0.7% below spot) and $100.33 (0.3% above spot) (among multiple breakevens). That represents significant leverage on the $1,390.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, the position captures its maximum gain of **$0.00**. Breakevens are $99.33 (0.7% below spot) and $100.33 (0.3% above spot) (among multiple breakevens). That represents significant leverage on the $1,390.00 capital at risk."

**Zone**: stagnant
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $1,390"
**Full body**: "Between $92.00 and $108.00, the position captures its maximum gain of **$0.00**. Breakevens are $99.33 (0.7% below spot) and $100.33 (0.3% above spot) (among multiple breakevens). That represents significant leverage on the $1,390.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$700.00**"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$700.00**. Breakeven is $108.00 (8.0% above spot). Maximum gain is **+$9,200.00**. That represents significant leverage on the $1,390.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$9,200.00**"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$700.00**. Breakeven is $108.00 (8.0% above spot). Maximum gain is **+$9,200.00**. That represents significant leverage on the $1,390.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$700.00**. Breakeven is $108.00 (8.0% above spot). Maximum gain is **+$9,200.00**. That represents significant leverage on the $1,390.00 capital at risk."

**Zone**: bullish
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $1,390"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$700.00**. Breakeven is $108.00 (8.0% above spot). Maximum gain is **+$9,200.00**. That represents significant leverage on the $1,390.00 capital at risk."

### Strategy: Bull Call Spread (ID=13) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$800.00**"
**Full body**: "At any price below $92.00, losses are capped at **−$800.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$800.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $800.00"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$800.00**"
**Full body**: "At any price above $108.00, gains are capped at **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, gains are capped at **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $800.00"
**Full body**: "At any price above $108.00, gains are capped at **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

### Strategy: Bear Put Spread (ID=14) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$800.00**"
**Full body**: "At any price below $92.00, gains are locked in at **+$800.00**."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $92.00, gains are locked in at **+$800.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$800.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $800.00"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$800.00**"
**Full body**: "At any price above $108.00, losses are capped at **−$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, losses are capped at **−$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $800.00"
**Full body**: "At any price above $108.00, losses are capped at **−$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

### Strategy: Bear Call Spread (ID=15) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$800.00**"
**Full body**: "At any price below $92.00, gains are locked in at **+$800.00**."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $92.00, gains are locked in at **+$800.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$800.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $800.00"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$800.00**"
**Full body**: "At any price above $108.00, losses are capped at **−$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, losses are capped at **−$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $800.00"
**Full body**: "At any price above $108.00, losses are capped at **−$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

### Strategy: Bull Put Spread (ID=16) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$800.00**"
**Full body**: "At any price below $92.00, losses are capped at **−$800.00** — the long $92.00 put provides a hard floor."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$800.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $800.00"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$800.00**"
**Full body**: "At any price above $108.00, gains are capped at **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, gains are capped at **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $800.00"
**Full body**: "At any price above $108.00, gains are capped at **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk."

### Strategy: Call Ratio Backspread (ID=17) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$610.00**"
**Full body**: "At any price below $92.00, gains are locked in at **+$610.00**."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $92.00, gains are locked in at **+$610.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$190.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **−$190.00**. Breakeven is $98.10 (1.9% below spot)."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$290.00**"
**Full body**: "Above $108.00, the position rises with the stock. At $115.00, the position is **−$290.00**. Breakeven is $117.90 (17.9% above spot). There is no cap on upside gains."

### Strategy: Put Ratio Backspread (ID=18) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$290.00**"
**Full body**: "Below $92.00, the position gains value as the stock falls. At $85.00, the position is **−$290.00**. Breakeven is $82.10 (17.9% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$190.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **−$190.00**. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$8,210.00**. That represents a 274.6% return on the $2,990.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$8,210.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **−$190.00**. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$8,210.00**. That represents a 274.6% return on the $2,990.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **−$190.00**. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$8,210.00**. That represents a 274.6% return on the $2,990.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,990.00"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **−$190.00**. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$8,210.00**. That represents a 274.6% return on the $2,990.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$610.00**"
**Full body**: "At any price above $108.00, gains are capped at **+$610.00**. That represents a 274.6% return on the $2,990.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, gains are capped at **+$610.00**. That represents a 274.6% return on the $2,990.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,990.00"
**Full body**: "At any price above $108.00, gains are capped at **+$610.00**. That represents a 274.6% return on the $2,990.00 capital at risk."

### Strategy: Call Ratio Spread (ID=19) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$610.00**"
**Full body**: "At any price below $92.00, losses are capped at **−$610.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$190.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **+$190.00**. Breakeven is $98.10 (1.9% below spot). Maximum gain is **+$990.00**. That represents a 35.6% return on the $2,780.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$990.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **+$190.00**. Breakeven is $98.10 (1.9% below spot). Maximum gain is **+$990.00**. That represents a 35.6% return on the $2,780.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **+$190.00**. Breakeven is $98.10 (1.9% below spot). Maximum gain is **+$990.00**. That represents a 35.6% return on the $2,780.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,780.00"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **+$190.00**. Breakeven is $98.10 (1.9% below spot). Maximum gain is **+$990.00**. That represents a 35.6% return on the $2,780.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$290.00**"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **+$290.00**. Breakeven is $117.90 (17.9% above spot). Maximum gain is **+$990.00**. That represents a 35.6% return on the $2,780.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$990.00**"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **+$290.00**. Breakeven is $117.90 (17.9% above spot). Maximum gain is **+$990.00**. That represents a 35.6% return on the $2,780.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **+$290.00**. Breakeven is $117.90 (17.9% above spot). Maximum gain is **+$990.00**. That represents a 35.6% return on the $2,780.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,780.00"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **+$290.00**. Breakeven is $117.90 (17.9% above spot). Maximum gain is **+$990.00**. That represents a 35.6% return on the $2,780.00 capital at risk."

### Strategy: Long Stock (ID=2) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum loss is **−$10,000.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$10,000.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum loss is **−$10,000.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot)."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,500.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). There is no cap on upside gains."

### Strategy: Long Stock (ID=2) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$3,000.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$3,000.00** — the shares lose −$3,000.00 and the options add $0.00. Maximum loss is **−$11,500.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$11,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$3,000.00** — the shares lose −$3,000.00 and the options add $0.00. Maximum loss is **−$11,500.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,500.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $115.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $115.00 (15.0% above spot). There is no cap on upside gains."

### Strategy: Long Stock (ID=2) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$6,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$6,500.00** — the shares lose −$6,500.00 and the options add $0.00. Maximum loss is **−$15,000.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$15,000.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$6,500.00** — the shares lose −$6,500.00 and the options add $0.00. Maximum loss is **−$15,000.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$5,000.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **−$5,000.00** — the shares lose −$5,000.00 and the options add $0.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$3,500.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $115.00, the client's combined position is **−$3,500.00** — the shares lose −$3,500.00 and the options add $0.00. Breakeven is $150.00 (50.0% above spot). There is no cap on upside gains."

### Strategy: Long Stock (ID=2) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $85.00 (15.0% below spot). Maximum loss is **−$8,500.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$8,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $85.00 (15.0% below spot). Maximum loss is **−$8,500.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,500.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$3,000.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$3,000.00** — the shares gain +$3,000.00 and the options add $0.00. There is no cap on upside gains."

### Strategy: Long Stock (ID=2) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$3,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **+$3,500.00** — the shares gain +$3,500.00 and the options add $0.00. Breakeven is $50.00 (50.0% below spot). Maximum loss is **−$5,000.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$5,000.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **+$3,500.00** — the shares gain +$3,500.00 and the options add $0.00. Breakeven is $50.00 (50.0% below spot). Maximum loss is **−$5,000.00**."

**Zone**: bearish
**Check**: MISLEADING_DOWNSIDE
**Text**: "full downside exposure (avg_cost=50, spot=100.0)"
**Full body**: "Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **+$3,500.00** — the shares gain +$3,500.00 and the options add $0.00. Breakeven is $50.00 (50.0% below spot). Maximum loss is **−$5,000.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,000.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **+$5,000.00** — the shares gain +$5,000.00 and the options add $0.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$6,500.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$6,500.00** — the shares gain +$6,500.00 and the options add $0.00. There is no cap on upside gains."

### Strategy: Put Ratio Spread (ID=20) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$290.00**"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **+$290.00**. Breakeven is $82.10 (17.9% below spot). Maximum loss is **−$8,210.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$8,210.00**"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **+$290.00**. Breakeven is $82.10 (17.9% below spot). Maximum loss is **−$8,210.00**."

**Zone**: bearish
**Check**: DECLINE_RISING
**Text**: "'position declines' but P&L rises (-5200->690)"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **+$290.00**. Breakeven is $82.10 (17.9% below spot). Maximum loss is **−$8,210.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$190.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **+$190.00**. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$990.00**. That represents a 12.1% return on the $8,210.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$990.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **+$190.00**. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$990.00**. That represents a 12.1% return on the $8,210.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **+$190.00**. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$990.00**. That represents a 12.1% return on the $8,210.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $8,210.00"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **+$190.00**. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$990.00**. That represents a 12.1% return on the $8,210.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$610.00**"
**Full body**: "At any price above $108.00, losses are capped at **−$610.00**. That represents a 12.1% return on the $8,210.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, losses are capped at **−$610.00**. That represents a 12.1% return on the $8,210.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $8,210.00"
**Full body**: "At any price above $108.00, losses are capped at **−$610.00**. That represents a 12.1% return on the $8,210.00 capital at risk."

### Strategy: Bull Call Ladder (ID=21) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,250.00**"
**Full body**: "At any price below $85.00, losses are capped at **−$1,250.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$250.00**"
**Full body**: "Between $85.00 and $115.00, the position gains value as the stock moves higher. At $100.00, the position is **+$250.00**. Breakeven is $97.50 (2.5% below spot). Maximum gain is **+$250.00**. That represents a 7.4% return on the $3,388.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$250.00**"
**Full body**: "Between $85.00 and $115.00, the position gains value as the stock moves higher. At $100.00, the position is **+$250.00**. Breakeven is $97.50 (2.5% below spot). Maximum gain is **+$250.00**. That represents a 7.4% return on the $3,388.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $85.00 and $115.00, the position gains value as the stock moves higher. At $100.00, the position is **+$250.00**. Breakeven is $97.50 (2.5% below spot). Maximum gain is **+$250.00**. That represents a 7.4% return on the $3,388.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $3,388.00"
**Full body**: "Between $85.00 and $115.00, the position gains value as the stock moves higher. At $100.00, the position is **+$250.00**. Breakeven is $97.50 (2.5% below spot). Maximum gain is **+$250.00**. That represents a 7.4% return on the $3,388.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$250.00**"
**Full body**: "Above $115.00, losses increase as the stock rises. At $115.00, the position is **+$250.00**. Breakeven is $117.50 (17.5% above spot). Maximum gain is **+$250.00**. That represents a 7.4% return on the $3,388.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$250.00**"
**Full body**: "Above $115.00, losses increase as the stock rises. At $115.00, the position is **+$250.00**. Breakeven is $117.50 (17.5% above spot). Maximum gain is **+$250.00**. That represents a 7.4% return on the $3,388.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $115.00, losses increase as the stock rises. At $115.00, the position is **+$250.00**. Breakeven is $117.50 (17.5% above spot). Maximum gain is **+$250.00**. That represents a 7.4% return on the $3,388.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $3,388.00"
**Full body**: "Above $115.00, losses increase as the stock rises. At $115.00, the position is **+$250.00**. Breakeven is $117.50 (17.5% above spot). Maximum gain is **+$250.00**. That represents a 7.4% return on the $3,388.00 capital at risk."

### Strategy: Bear Put Ladder (ID=22) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$250.00**"
**Full body**: "Below $85.00, the position declines with the stock. At $85.00, the position is **+$250.00**. Breakeven is $82.50 (17.5% below spot). Maximum loss is **−$8,250.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$8,250.00**"
**Full body**: "Below $85.00, the position declines with the stock. At $85.00, the position is **+$250.00**. Breakeven is $82.50 (17.5% below spot). Maximum loss is **−$8,250.00**."

**Zone**: bearish
**Check**: DECLINE_RISING
**Text**: "'position declines' but P&L rises (-5240->250)"
**Full body**: "Below $85.00, the position declines with the stock. At $85.00, the position is **+$250.00**. Breakeven is $82.50 (17.5% below spot). Maximum loss is **−$8,250.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$250.00**"
**Full body**: "Between $85.00 and $115.00, the position gains value as the stock moves lower. At $100.00, the position is **+$250.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$250.00**. That represents a 3.0% return on the $8,250.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$250.00**"
**Full body**: "Between $85.00 and $115.00, the position gains value as the stock moves lower. At $100.00, the position is **+$250.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$250.00**. That represents a 3.0% return on the $8,250.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $85.00 and $115.00, the position gains value as the stock moves lower. At $100.00, the position is **+$250.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$250.00**. That represents a 3.0% return on the $8,250.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $8,250.00"
**Full body**: "Between $85.00 and $115.00, the position gains value as the stock moves lower. At $100.00, the position is **+$250.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$250.00**. That represents a 3.0% return on the $8,250.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,250.00**"
**Full body**: "At any price above $115.00, losses are capped at **−$1,250.00**. That represents a 3.0% return on the $8,250.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $115.00, losses are capped at **−$1,250.00**. That represents a 3.0% return on the $8,250.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $8,250.00"
**Full body**: "At any price above $115.00, losses are capped at **−$1,250.00**. That represents a 3.0% return on the $8,250.00 capital at risk."

### Strategy: Bear Call Ladder (ID=23) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,250.00**"
**Full body**: "At any price below $85.00, gains are locked in at **+$1,250.00**."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $85.00, gains are locked in at **+$1,250.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$250.00**"
**Full body**: "Between $85.00 and $115.00, the position gains value as the stock moves lower. At $100.00, the position is **−$250.00**. Breakeven is $97.50 (2.5% below spot)."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$250.00**"
**Full body**: "Above $115.00, the position rises with the stock. At $115.00, the position is **−$250.00**. Breakeven is $117.50 (17.5% above spot). There is no cap on upside gains."

### Strategy: Bull Put Ladder (ID=24) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$250.00**"
**Full body**: "Below $85.00, the position gains value as the stock falls. At $85.00, the position is **−$250.00**. Breakeven is $82.50 (17.5% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$250.00**"
**Full body**: "Between $85.00 and $115.00, the position gains value as the stock moves higher. At $100.00, the position is **−$250.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$8,250.00**. That represents a 226.8% return on the $3,638.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$8,250.00**"
**Full body**: "Between $85.00 and $115.00, the position gains value as the stock moves higher. At $100.00, the position is **−$250.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$8,250.00**. That represents a 226.8% return on the $3,638.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $85.00 and $115.00, the position gains value as the stock moves higher. At $100.00, the position is **−$250.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$8,250.00**. That represents a 226.8% return on the $3,638.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $3,638.00"
**Full body**: "Between $85.00 and $115.00, the position gains value as the stock moves higher. At $100.00, the position is **−$250.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$8,250.00**. That represents a 226.8% return on the $3,638.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,250.00**"
**Full body**: "At any price above $115.00, gains are capped at **+$1,250.00**. That represents a 226.8% return on the $3,638.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $115.00, gains are capped at **+$1,250.00**. That represents a 226.8% return on the $3,638.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $3,638.00"
**Full body**: "At any price above $115.00, gains are capped at **+$1,250.00**. That represents a 226.8% return on the $3,638.00 capital at risk."

### Strategy: Long Call Butterfly (ID=25) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,276.00**"
**Full body**: "At any price below $85.00, losses are capped at **−$1,276.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$224.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$224.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$224.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $1,276.00"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,276.00**"
**Full body**: "At any price above $115.00, losses are capped at **−$1,276.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $115.00, losses are capped at **−$1,276.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $1,276.00"
**Full body**: "At any price above $115.00, losses are capped at **−$1,276.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

### Strategy: Long Put Butterfly (ID=26) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,276.00**"
**Full body**: "At any price below $85.00, losses are capped at **−$1,276.00** — the long $85.00 put provides a hard floor."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$224.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$224.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$224.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $1,276.00"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,276.00**"
**Full body**: "At any price above $115.00, losses are capped at **−$1,276.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $115.00, losses are capped at **−$1,276.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $1,276.00"
**Full body**: "At any price above $115.00, losses are capped at **−$1,276.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

### Strategy: Iron Butterfly (ID=27) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,276.00**"
**Full body**: "At any price below $85.00, losses are capped at **−$1,276.00** — the long $85.00 put provides a hard floor."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$224.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$224.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$224.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $1,276.00"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,276.00**"
**Full body**: "At any price above $115.00, losses are capped at **−$1,276.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $115.00, losses are capped at **−$1,276.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $1,276.00"
**Full body**: "At any price above $115.00, losses are capped at **−$1,276.00**. That represents a 17.6% return on the $1,276.00 capital at risk."

### Strategy: Long Call Condor (ID=28) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,020.00**"
**Full body**: "Below $92.00. Maximum loss is **−$1,020.00** at any price below $80.00. Breakeven is $90.20 (9.8% below spot)."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$180.00**"
**Full body**: "Between $92.00 and $108.00, the position captures its maximum gain of **+$180.00**. That represents a 4.1% return on the $4,380.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, the position captures its maximum gain of **+$180.00**. That represents a 4.1% return on the $4,380.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $4,380.00"
**Full body**: "Between $92.00 and $108.00, the position captures its maximum gain of **+$180.00**. That represents a 4.1% return on the $4,380.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,020.00**"
**Full body**: "Above $108.00, the short $108.00 call drives losses, but the long $120.00 call caps the damage. Maximum loss is **−$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot). That represents a 4.1% return on the $4,380.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00, the short $108.00 call drives losses, but the long $120.00 call caps the damage. Maximum loss is **−$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot). That represents a 4.1% return on the $4,380.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $4,380.00"
**Full body**: "Above $108.00, the short $108.00 call drives losses, but the long $120.00 call caps the damage. Maximum loss is **−$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot). That represents a 4.1% return on the $4,380.00 capital at risk."

### Strategy: Long Put Condor (ID=29) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,020.00**"
**Full body**: "Below $92.00, the short $92.00 put drives losses, but the long $80.00 put provides a hard floor. Maximum loss is **−$1,020.00** at any price below $80.00. Breakeven is $90.20 (9.8% below spot)."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$180.00**"
**Full body**: "Between $92.00 and $108.00, the position captures its maximum gain of **+$180.00**. That represents a 17.6% return on the $1,020.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, the position captures its maximum gain of **+$180.00**. That represents a 17.6% return on the $1,020.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $1,020.00"
**Full body**: "Between $92.00 and $108.00, the position captures its maximum gain of **+$180.00**. That represents a 17.6% return on the $1,020.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,020.00**"
**Full body**: "Above $108.00. Maximum loss is **−$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot). That represents a 17.6% return on the $1,020.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00. Maximum loss is **−$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot). That represents a 17.6% return on the $1,020.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $1,020.00"
**Full body**: "Above $108.00. Maximum loss is **−$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot). That represents a 17.6% return on the $1,020.00 capital at risk."

### Strategy: Short Stock (ID=3) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,500.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 100.0% return on the $10,001.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$10,000.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 100.0% return on the $10,001.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 100.0% return on the $10,001.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $10,001.00"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 100.0% return on the $10,001.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,500.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 100.0% return on the $10,001.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$10,000.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 100.0% return on the $10,001.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 100.0% return on the $10,001.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $10,001.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 100.0% return on the $10,001.00 capital at risk."

### Strategy: Short Stock (ID=3) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$3,000.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **+$3,000.00** — the shares gain +$3,000.00 and the options add $0.00. There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,500.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Maximum gain is **+$11,500.00**. That represents a 100.0% return on the $11,501.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$11,500.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Maximum gain is **+$11,500.00**. That represents a 100.0% return on the $11,501.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Maximum gain is **+$11,500.00**. That represents a 100.0% return on the $11,501.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $11,501.00"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Maximum gain is **+$11,500.00**. That represents a 100.0% return on the $11,501.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $115.00 (15.0% above spot). Maximum gain is **+$11,500.00**. That represents a 100.0% return on the $11,501.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$11,500.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $115.00 (15.0% above spot). Maximum gain is **+$11,500.00**. That represents a 100.0% return on the $11,501.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $115.00 (15.0% above spot). Maximum gain is **+$11,500.00**. That represents a 100.0% return on the $11,501.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $11,501.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $115.00 (15.0% above spot). Maximum gain is **+$11,500.00**. That represents a 100.0% return on the $11,501.00 capital at risk."

### Strategy: Short Stock (ID=3) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$6,500.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **+$6,500.00** — the shares gain +$6,500.00 and the options add $0.00. There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,000.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **+$5,000.00** — the shares gain +$5,000.00 and the options add $0.00. Maximum gain is **+$15,000.00**. That represents a 100.0% return on the $15,001.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$15,000.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **+$5,000.00** — the shares gain +$5,000.00 and the options add $0.00. Maximum gain is **+$15,000.00**. That represents a 100.0% return on the $15,001.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **+$5,000.00** — the shares gain +$5,000.00 and the options add $0.00. Maximum gain is **+$15,000.00**. That represents a 100.0% return on the $15,001.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $15,001.00"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **+$5,000.00** — the shares gain +$5,000.00 and the options add $0.00. Maximum gain is **+$15,000.00**. That represents a 100.0% return on the $15,001.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$3,500.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$3,500.00** — the shares gain +$3,500.00 and the options add $0.00. Breakeven is $150.00 (50.0% above spot). Maximum gain is **+$15,000.00**. That represents a 100.0% return on the $15,001.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$15,000.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$3,500.00** — the shares gain +$3,500.00 and the options add $0.00. Breakeven is $150.00 (50.0% above spot). Maximum gain is **+$15,000.00**. That represents a 100.0% return on the $15,001.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$3,500.00** — the shares gain +$3,500.00 and the options add $0.00. Breakeven is $150.00 (50.0% above spot). Maximum gain is **+$15,000.00**. That represents a 100.0% return on the $15,001.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $15,001.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$3,500.00** — the shares gain +$3,500.00 and the options add $0.00. Breakeven is $150.00 (50.0% above spot). Maximum gain is **+$15,000.00**. That represents a 100.0% return on the $15,001.00 capital at risk."

### Strategy: Short Stock (ID=3) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $85.00 (15.0% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,500.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Maximum gain is **+$8,500.00**. That represents a 100.0% return on the $8,501.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$8,500.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Maximum gain is **+$8,500.00**. That represents a 100.0% return on the $8,501.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Maximum gain is **+$8,500.00**. That represents a 100.0% return on the $8,501.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $8,501.00"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Maximum gain is **+$8,500.00**. That represents a 100.0% return on the $8,501.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$3,000.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$3,000.00** — the shares lose −$3,000.00 and the options add $0.00. Maximum gain is **+$8,500.00**. That represents a 100.0% return on the $8,501.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$8,500.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$3,000.00** — the shares lose −$3,000.00 and the options add $0.00. Maximum gain is **+$8,500.00**. That represents a 100.0% return on the $8,501.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$3,000.00** — the shares lose −$3,000.00 and the options add $0.00. Maximum gain is **+$8,500.00**. That represents a 100.0% return on the $8,501.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $8,501.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$3,000.00** — the shares lose −$3,000.00 and the options add $0.00. Maximum gain is **+$8,500.00**. That represents a 100.0% return on the $8,501.00 capital at risk."

### Strategy: Short Stock (ID=3) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$3,500.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **−$3,500.00** — the shares lose −$3,500.00 and the options add $0.00. Breakeven is $50.00 (50.0% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$5,000.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **−$5,000.00** — the shares lose −$5,000.00 and the options add $0.00. Maximum gain is **+$5,000.00**. That represents a 100.0% return on the $5,001.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,000.00**"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **−$5,000.00** — the shares lose −$5,000.00 and the options add $0.00. Maximum gain is **+$5,000.00**. That represents a 100.0% return on the $5,001.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **−$5,000.00** — the shares lose −$5,000.00 and the options add $0.00. Maximum gain is **+$5,000.00**. That represents a 100.0% return on the $5,001.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $5,001.00"
**Full body**: "Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **−$5,000.00** — the shares lose −$5,000.00 and the options add $0.00. Maximum gain is **+$5,000.00**. That represents a 100.0% return on the $5,001.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$6,500.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$6,500.00** — the shares lose −$6,500.00 and the options add $0.00. Maximum gain is **+$5,000.00**. That represents a 100.0% return on the $5,001.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$5,000.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$6,500.00** — the shares lose −$6,500.00 and the options add $0.00. Maximum gain is **+$5,000.00**. That represents a 100.0% return on the $5,001.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$6,500.00** — the shares lose −$6,500.00 and the options add $0.00. Maximum gain is **+$5,000.00**. That represents a 100.0% return on the $5,001.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $5,001.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$6,500.00** — the shares lose −$6,500.00 and the options add $0.00. Maximum gain is **+$5,000.00**. That represents a 100.0% return on the $5,001.00 capital at risk."

### Strategy: Iron Condor (ID=30) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,020.00**"
**Full body**: "Below $92.00, the short $92.00 put drives losses, but the long $80.00 put provides a hard floor. Maximum loss is **−$1,020.00** at any price below $80.00. Breakeven is $90.20 (9.8% below spot)."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $180.00 credit is retained. That represents a 6.5% return on the $2,780.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,780.00"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $180.00 credit is retained. That represents a 6.5% return on the $2,780.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,020.00**"
**Full body**: "Above $108.00, the short $108.00 call drives losses, but the long $120.00 call caps the damage. Maximum loss is **−$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot). That represents a 6.5% return on the $2,780.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00, the short $108.00 call drives losses, but the long $120.00 call caps the damage. Maximum loss is **−$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot). That represents a 6.5% return on the $2,780.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,780.00"
**Full body**: "Above $108.00, the short $108.00 call drives losses, but the long $120.00 call caps the damage. Maximum loss is **−$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot). That represents a 6.5% return on the $2,780.00 capital at risk."

### Strategy: Short Call Butterfly (ID=31) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,276.00**"
**Full body**: "At any price below $85.00, gains are locked in at **+$1,276.00**."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $85.00, gains are locked in at **+$1,276.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$224.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$224.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,276.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: stagnant
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $224"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,276.00**"
**Full body**: "At any price above $115.00, gains are capped at **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $115.00, gains are capped at **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: bullish
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $224"
**Full body**: "At any price above $115.00, gains are capped at **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

### Strategy: Short Put Butterfly (ID=32) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,276.00**"
**Full body**: "At any price below $85.00, gains are locked in at **+$1,276.00**."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $85.00, gains are locked in at **+$1,276.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$224.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$224.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,276.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: stagnant
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $224"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,276.00**"
**Full body**: "At any price above $115.00, gains are capped at **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $115.00, gains are capped at **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: bullish
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $224"
**Full body**: "At any price above $115.00, gains are capped at **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

### Strategy: Rev Iron Butterfly (ID=33) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,276.00**"
**Full body**: "At any price below $85.00, gains are locked in at **+$1,276.00**."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $85.00, gains are locked in at **+$1,276.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$224.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$224.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,276.00**"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: stagnant
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $224"
**Full body**: "Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,276.00**"
**Full body**: "At any price above $115.00, gains are capped at **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $115.00, gains are capped at **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

**Zone**: bullish
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $224"
**Full body**: "At any price above $115.00, gains are capped at **+$1,276.00**. That represents significant leverage on the $224.00 capital at risk."

### Strategy: Short Call Condor (ID=34) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,020.00**"
**Full body**: "Below $92.00. Maximum loss is **+$1,020.00** at any price below $80.00. Breakeven is $90.20 (9.8% below spot)."

**Zone**: bearish
**Check**: LOSS_POSITIVE
**Text**: "loss is **+$1,020.00"
**Full body**: "Below $92.00. Maximum loss is **+$1,020.00** at any price below $80.00. Breakeven is $90.20 (9.8% below spot)."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$180.00**"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$180.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,020.00**"
**Full body**: "Above $108.00, the short $120.00 call drives losses, but the long $108.00 call caps the damage. Maximum loss is **+$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot)."

**Zone**: bullish
**Check**: LOSS_POSITIVE
**Text**: "loss is **+$1,020.00"
**Full body**: "Above $108.00, the short $120.00 call drives losses, but the long $108.00 call caps the damage. Maximum loss is **+$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot)."

### Strategy: Short Put Condor (ID=35) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,020.00**"
**Full body**: "Below $92.00, the short $80.00 put drives losses, but the long $92.00 put provides a hard floor. Maximum loss is **+$1,020.00** at any price below $80.00. Breakeven is $90.20 (9.8% below spot)."

**Zone**: bearish
**Check**: LOSS_POSITIVE
**Text**: "loss is **+$1,020.00"
**Full body**: "Below $92.00, the short $80.00 put drives losses, but the long $92.00 put provides a hard floor. Maximum loss is **+$1,020.00** at any price below $80.00. Breakeven is $90.20 (9.8% below spot)."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$180.00**"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$180.00**. That represents a 19.6% return on the $5,200.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$180.00**. That represents a 19.6% return on the $5,200.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $5,200.00"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$180.00**. That represents a 19.6% return on the $5,200.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,020.00**"
**Full body**: "Above $108.00. Maximum loss is **+$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot). That represents a 19.6% return on the $5,200.00 capital at risk."

**Zone**: bullish
**Check**: LOSS_POSITIVE
**Text**: "loss is **+$1,020.00"
**Full body**: "Above $108.00. Maximum loss is **+$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot). That represents a 19.6% return on the $5,200.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00. Maximum loss is **+$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot). That represents a 19.6% return on the $5,200.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $5,200.00"
**Full body**: "Above $108.00. Maximum loss is **+$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot). That represents a 19.6% return on the $5,200.00 capital at risk."

### Strategy: Rev Iron Condor (ID=36) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,020.00**"
**Full body**: "Below $92.00, the short $80.00 put drives losses, but the long $92.00 put provides a hard floor. Maximum loss is **+$1,020.00** at any price below $80.00. Breakeven is $90.20 (9.8% below spot)."

**Zone**: bearish
**Check**: LOSS_POSITIVE
**Text**: "loss is **+$1,020.00"
**Full body**: "Below $92.00, the short $80.00 put drives losses, but the long $92.00 put provides a hard floor. Maximum loss is **+$1,020.00** at any price below $80.00. Breakeven is $90.20 (9.8% below spot)."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$180.00**"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$180.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,020.00**"
**Full body**: "Above $108.00, the short $120.00 call drives losses, but the long $108.00 call caps the damage. Maximum loss is **+$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot)."

**Zone**: bullish
**Check**: LOSS_POSITIVE
**Text**: "loss is **+$1,020.00"
**Full body**: "Above $108.00, the short $120.00 call drives losses, but the long $108.00 call caps the damage. Maximum loss is **+$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot)."

### Strategy: Long Straddle (ID=37) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Below $100.00, the position gains value as the stock falls. At $90.00, the position is **+$500.00**. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$500.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **−$500.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Above $100.00, the position rises with the stock. At $110.00, the position is **+$500.00**. Breakeven is $105.00 (5.0% above spot). There is no cap on upside gains."

### Strategy: Short Straddle (ID=38) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$500.00**"
**Full body**: "Below $100.00, the position declines with the stock. At $90.00, the position is **−$500.00**. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk."

**Zone**: bearish
**Check**: DECLINE_RISING
**Text**: "'position declines' but P&L rises (-6490->0)"
**Full body**: "Below $100.00, the position declines with the stock. At $90.00, the position is **−$500.00**. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$500.00**. Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$500.00**. Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$500.00**. Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $4,500.00"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$500.00**. Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$500.00**"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$500.00**. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$500.00**. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$500.00**. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $4,500.00"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$500.00**. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

### Strategy: Long Strangle (ID=39) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$320.00**"
**Full body**: "Below $92.00, the position gains value as the stock falls. At $85.00, the position is **+$320.00**. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$380.00**"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$380.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$320.00**"
**Full body**: "Above $108.00, the position rises with the stock. At $115.00, the position is **+$320.00**. Breakeven is $111.80 (11.8% above spot). There is no cap on upside gains."

### Strategy: Long Call (ID=4) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$250.00**"
**Full body**: "At any price below $100.00, losses are capped at **−$250.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$250.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **−$250.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$750.00**"
**Full body**: "Above $100.00, the position rises with the stock. At $110.00, the position is **+$750.00**. Breakeven is $102.50 (2.5% above spot). There is no cap on upside gains."

### Strategy: Short Strangle (ID=40) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$320.00**"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **−$320.00**. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk."

**Zone**: bearish
**Check**: DECLINE_RISING
**Text**: "'position declines' but P&L rises (-5810->380)"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **−$320.00**. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $380.00 credit is retained. That represents a 13.7% return on the $2,780.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,780.00"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $380.00 credit is retained. That represents a 13.7% return on the $2,780.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$320.00**"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$320.00**. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 13.7% return on the $2,780.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$380.00**"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$320.00**. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 13.7% return on the $2,780.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$320.00**. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 13.7% return on the $2,780.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,780.00"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$320.00**. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 13.7% return on the $2,780.00 capital at risk."

### Strategy: Long Guts (ID=41) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$320.00**"
**Full body**: "Below $92.00, the position gains value as the stock falls. At $85.00, the position is **+$320.00**. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$380.00**"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$380.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$320.00**"
**Full body**: "Above $108.00, the position rises with the stock. At $115.00, the position is **+$320.00**. Breakeven is $111.80 (11.8% above spot). There is no cap on upside gains."

### Strategy: Short Guts (ID=42) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$320.00**"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **−$320.00**. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk."

**Zone**: bearish
**Check**: DECLINE_RISING
**Text**: "'position declines' but P&L rises (-5810->380)"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **−$320.00**. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,980.00 credit is retained. That represents a 6.4% return on the $5,980.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $5,980.00"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,980.00 credit is retained. That represents a 6.4% return on the $5,980.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$320.00**"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$320.00**. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 6.4% return on the $5,980.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$380.00**"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$320.00**. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 6.4% return on the $5,980.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$320.00**. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 6.4% return on the $5,980.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $5,980.00"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$320.00**. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 6.4% return on the $5,980.00 capital at risk."

### Strategy: Strip (ID=43) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,250.00**"
**Full body**: "Below $100.00, the position gains value as the stock falls. At $90.00, the position is **+$1,250.00**. Breakeven is $96.25 (3.8% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$750.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **−$750.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$250.00**"
**Full body**: "Above $100.00, the position rises with the stock. At $110.00, the position is **+$250.00**. Breakeven is $107.50 (7.5% above spot). There is no cap on upside gains."

### Strategy: Strap (ID=44) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$250.00**"
**Full body**: "Below $100.00, the position gains value as the stock falls. At $90.00, the position is **+$250.00**. Breakeven is $92.50 (7.5% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$750.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **−$750.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,250.00**"
**Full body**: "Above $100.00, the position rises with the stock. At $110.00, the position is **+$1,250.00**. Breakeven is $103.75 (3.8% above spot). There is no cap on upside gains."

### Strategy: Covered Short Straddle (ID=45) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$1,500.00** — the shares lose −$1,000.00 and the options cost −$500.00. Breakeven is $97.50 (2.5% below spot). Maximum loss is **−$19,500.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$19,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$1,500.00** — the shares lose −$1,000.00 and the options cost −$500.00. Breakeven is $97.50 (2.5% below spot). Maximum loss is **−$19,500.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 1.7% return on the $29,500.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 1.7% return on the $29,500.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 1.7% return on the $29,500.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 1.7% return on the $29,500.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $29,500.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 1.7% return on the $29,500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "At any price above $100.00, the client's gains are capped at **+$500.00** — the short call limits further upside. The trade-off: $500.00 in collected premium in exchange for giving up gains above $100.00. That represents a 1.7% return on the $29,500.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $100.00, the client's gains are capped at **+$500.00** — the short call limits further upside. The trade-off: $500.00 in collected premium in exchange for giving up gains above $100.00. That represents a 1.7% return on the $29,500.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $29,500.00"
**Full body**: "At any price above $100.00, the client's gains are capped at **+$500.00** — the short call limits further upside. The trade-off: $500.00 in collected premium in exchange for giving up gains above $100.00. That represents a 1.7% return on the $29,500.00 capital at risk."

### Strategy: Covered Short Straddle (ID=45) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$3,000.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$3,000.00** — the shares lose −$2,500.00 and the options cost −$500.00. Maximum loss is **−$21,000.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$21,000.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$3,000.00** — the shares lose −$2,500.00 and the options cost −$500.00. Maximum loss is **−$21,000.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,000.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,000.00** — the shares lose −$1,500.00 and the options add +$500.00. Maximum gain is **−$1,000.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,000.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,000.00** — the shares lose −$1,500.00 and the options add +$500.00. Maximum gain is **−$1,000.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$1,000.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,000.00** — the shares lose −$1,500.00 and the options add +$500.00. Maximum gain is **−$1,000.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,000.00** — the shares lose −$1,500.00 and the options add +$500.00. Maximum gain is **−$1,000.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,000.00**"
**Full body**: "At any price above $100.00, the client's losses are capped at **−$1,000.00**. The trade-off: $500.00 in collected premium in exchange for giving up gains above $100.00."

### Strategy: Covered Short Straddle (ID=45) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$6,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$6,500.00** — the shares lose −$6,000.00 and the options cost −$500.00. Maximum loss is **−$24,500.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$24,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$6,500.00** — the shares lose −$6,000.00 and the options cost −$500.00. Maximum loss is **−$24,500.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$4,500.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,500.00** — the shares lose −$5,000.00 and the options add +$500.00. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,500.00** — the shares lose −$5,000.00 and the options add +$500.00. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$4,500.00**"
**Full body**: "At any price above $100.00, the client's losses are capped at **−$4,500.00**. The trade-off: $500.00 in collected premium in exchange for giving up gains above $100.00."

### Strategy: Covered Short Straddle (ID=45) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **$0.00** — the shares gain +$500.00 and the options cost −$500.00. Breakeven is $90.00 (10.0% below spot). Maximum loss is **−$18,000.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$18,000.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **$0.00** — the shares gain +$500.00 and the options cost −$500.00. Breakeven is $90.00 (10.0% below spot). Maximum loss is **−$18,000.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$2,000.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$2,000.00** — the shares gain +$1,500.00 and the options add +$500.00. Maximum gain is **+$2,000.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 7.1% return on the $28,000.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$2,000.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$2,000.00** — the shares gain +$1,500.00 and the options add +$500.00. Maximum gain is **+$2,000.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 7.1% return on the $28,000.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$2,000.00** — the shares gain +$1,500.00 and the options add +$500.00. Maximum gain is **+$2,000.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 7.1% return on the $28,000.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$2,000.00** — the shares gain +$1,500.00 and the options add +$500.00. Maximum gain is **+$2,000.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 7.1% return on the $28,000.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $28,000.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$2,000.00** — the shares gain +$1,500.00 and the options add +$500.00. Maximum gain is **+$2,000.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 7.1% return on the $28,000.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$2,000.00**"
**Full body**: "At any price above $100.00, the client's gains are capped at **+$2,000.00** — the short call limits further upside. The trade-off: $500.00 in collected premium in exchange for giving up gains above $100.00. That represents a 7.1% return on the $28,000.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $100.00, the client's gains are capped at **+$2,000.00** — the short call limits further upside. The trade-off: $500.00 in collected premium in exchange for giving up gains above $100.00. That represents a 7.1% return on the $28,000.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $28,000.00"
**Full body**: "At any price above $100.00, the client's gains are capped at **+$2,000.00** — the short call limits further upside. The trade-off: $500.00 in collected premium in exchange for giving up gains above $100.00. That represents a 7.1% return on the $28,000.00 capital at risk."

### Strategy: Covered Short Straddle (ID=45) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$3,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **+$3,500.00** — the shares gain +$4,000.00 and the options cost −$500.00. Breakeven is $72.50 (27.5% below spot). Maximum loss is **−$14,500.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$14,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **+$3,500.00** — the shares gain +$4,000.00 and the options cost −$500.00. Breakeven is $72.50 (27.5% below spot). Maximum loss is **−$14,500.00**."

**Zone**: bearish
**Check**: MISLEADING_DOWNSIDE
**Text**: "full downside exposure (avg_cost=50, spot=100.0)"
**Full body**: "Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **+$3,500.00** — the shares gain +$4,000.00 and the options cost −$500.00. Breakeven is $72.50 (27.5% below spot). Maximum loss is **−$14,500.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,500.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,500.00** — the shares gain +$5,000.00 and the options add +$500.00. Maximum gain is **+$5,500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 22.4% return on the $24,500.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,500.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,500.00** — the shares gain +$5,000.00 and the options add +$500.00. Maximum gain is **+$5,500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 22.4% return on the $24,500.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,500.00** — the shares gain +$5,000.00 and the options add +$500.00. Maximum gain is **+$5,500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 22.4% return on the $24,500.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,500.00** — the shares gain +$5,000.00 and the options add +$500.00. Maximum gain is **+$5,500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 22.4% return on the $24,500.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $24,500.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,500.00** — the shares gain +$5,000.00 and the options add +$500.00. Maximum gain is **+$5,500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 22.4% return on the $24,500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$5,500.00**"
**Full body**: "At any price above $100.00, the client's gains are capped at **+$5,500.00** — the short call limits further upside. The trade-off: $500.00 in collected premium in exchange for giving up gains above $100.00. That represents a 22.4% return on the $24,500.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $100.00, the client's gains are capped at **+$5,500.00** — the short call limits further upside. The trade-off: $500.00 in collected premium in exchange for giving up gains above $100.00. That represents a 22.4% return on the $24,500.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $24,500.00"
**Full body**: "At any price above $100.00, the client's gains are capped at **+$5,500.00** — the short call limits further upside. The trade-off: $500.00 in collected premium in exchange for giving up gains above $100.00. That represents a 22.4% return on the $24,500.00 capital at risk."

### Strategy: Covered Short Straddle (ID=45) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$500.00**"
**Full body**: "Below $100.00, the position declines with the stock. At $90.00, the position is **−$500.00**. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk."

**Zone**: bearish
**Check**: DECLINE_RISING
**Text**: "'position declines' but P&L rises (-6490->0)"
**Full body**: "Below $100.00, the position declines with the stock. At $90.00, the position is **−$500.00**. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$500.00**. Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$500.00**. Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$500.00**. Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $4,500.00"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$500.00**. Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$500.00**"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$500.00**. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$500.00**. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$500.00**. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $4,500.00"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$500.00**. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

### Strategy: Covered Short Strangle (ID=46) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,820.00**"
**Full body**: "Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$1,820.00** — the shares lose −$1,500.00 and the options cost −$320.00. There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$380.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$380.00** — the shares gain $0.00 and the options add +$380.00. Breakeven is $96.20 (3.8% below spot). Maximum gain is **+$1,180.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 9.2% return on the $12,780.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,180.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$380.00** — the shares gain $0.00 and the options add +$380.00. Breakeven is $96.20 (3.8% below spot). Maximum gain is **+$1,180.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 9.2% return on the $12,780.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$380.00** — the shares gain $0.00 and the options add +$380.00. Breakeven is $96.20 (3.8% below spot). Maximum gain is **+$1,180.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 9.2% return on the $12,780.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$380.00** — the shares gain $0.00 and the options add +$380.00. Breakeven is $96.20 (3.8% below spot). Maximum gain is **+$1,180.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 9.2% return on the $12,780.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $12,780.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$380.00** — the shares gain $0.00 and the options add +$380.00. Breakeven is $96.20 (3.8% below spot). Maximum gain is **+$1,180.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 9.2% return on the $12,780.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,180.00**"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$1,180.00** — the short call limits further upside. The trade-off: $380.00 in collected premium in exchange for giving up gains above $108.00. That represents a 9.2% return on the $12,780.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$1,180.00** — the short call limits further upside. The trade-off: $380.00 in collected premium in exchange for giving up gains above $108.00. That represents a 9.2% return on the $12,780.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $12,780.00"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$1,180.00** — the short call limits further upside. The trade-off: $380.00 in collected premium in exchange for giving up gains above $108.00. That represents a 9.2% return on the $12,780.00 capital at risk."

### Strategy: Covered Short Strangle (ID=46) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$3,320.00**"
**Full body**: "Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$3,320.00** — the shares lose −$3,000.00 and the options cost −$320.00. There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,120.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,120.00** — the shares lose −$1,500.00 and the options add +$380.00. Maximum gain is **−$320.00**. The premium adds a 3.8% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$320.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,120.00** — the shares lose −$1,500.00 and the options add +$380.00. Maximum gain is **−$320.00**. The premium adds a 3.8% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$320.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,120.00** — the shares lose −$1,500.00 and the options add +$380.00. Maximum gain is **−$320.00**. The premium adds a 3.8% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,120.00** — the shares lose −$1,500.00 and the options add +$380.00. Maximum gain is **−$320.00**. The premium adds a 3.8% enhancement over holding the stock alone."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$320.00**"
**Full body**: "At any price above $108.00, the client's losses are capped at **−$320.00**. The trade-off: $380.00 in collected premium in exchange for giving up gains above $108.00."

### Strategy: Covered Short Strangle (ID=46) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$6,820.00**"
**Full body**: "Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$6,820.00** — the shares lose −$6,500.00 and the options cost −$320.00. There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$4,620.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,620.00** — the shares lose −$5,000.00 and the options add +$380.00. Maximum gain is **−$3,820.00**. The premium adds a 3.8% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$3,820.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,620.00** — the shares lose −$5,000.00 and the options add +$380.00. Maximum gain is **−$3,820.00**. The premium adds a 3.8% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$3,820.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,620.00** — the shares lose −$5,000.00 and the options add +$380.00. Maximum gain is **−$3,820.00**. The premium adds a 3.8% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,620.00** — the shares lose −$5,000.00 and the options add +$380.00. Maximum gain is **−$3,820.00**. The premium adds a 3.8% enhancement over holding the stock alone."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$3,820.00**"
**Full body**: "At any price above $108.00, the client's losses are capped at **−$3,820.00**. The trade-off: $380.00 in collected premium in exchange for giving up gains above $108.00."

### Strategy: Covered Short Strangle (ID=46) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$320.00**"
**Full body**: "Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$320.00** — the shares gain $0.00 and the options cost −$320.00. Breakeven is $86.60 (13.4% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,880.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$1,880.00** — the shares gain +$1,500.00 and the options add +$380.00. Maximum gain is **+$2,680.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 23.8% return on the $11,280.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$2,680.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$1,880.00** — the shares gain +$1,500.00 and the options add +$380.00. Maximum gain is **+$2,680.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 23.8% return on the $11,280.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$1,880.00** — the shares gain +$1,500.00 and the options add +$380.00. Maximum gain is **+$2,680.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 23.8% return on the $11,280.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$1,880.00** — the shares gain +$1,500.00 and the options add +$380.00. Maximum gain is **+$2,680.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 23.8% return on the $11,280.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $11,280.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$1,880.00** — the shares gain +$1,500.00 and the options add +$380.00. Maximum gain is **+$2,680.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 23.8% return on the $11,280.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$2,680.00**"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$2,680.00** — the short call limits further upside. The trade-off: $380.00 in collected premium in exchange for giving up gains above $108.00. That represents a 23.8% return on the $11,280.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$2,680.00** — the short call limits further upside. The trade-off: $380.00 in collected premium in exchange for giving up gains above $108.00. That represents a 23.8% return on the $11,280.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $11,280.00"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$2,680.00** — the short call limits further upside. The trade-off: $380.00 in collected premium in exchange for giving up gains above $108.00. That represents a 23.8% return on the $11,280.00 capital at risk."

### Strategy: Covered Short Strangle (ID=46) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$3,180.00**"
**Full body**: "Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **+$3,180.00** — the shares gain +$3,500.00 and the options cost −$320.00. Breakeven is $69.10 (30.9% below spot). There is no cap on downside risk."

**Zone**: bearish
**Check**: MISLEADING_DOWNSIDE
**Text**: "full downside exposure (avg_cost=50, spot=100.0)"
**Full body**: "Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **+$3,180.00** — the shares gain +$3,500.00 and the options cost −$320.00. Breakeven is $69.10 (30.9% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,380.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,380.00** — the shares gain +$5,000.00 and the options add +$380.00. Maximum gain is **+$6,180.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 79.4% return on the $7,780.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$6,180.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,380.00** — the shares gain +$5,000.00 and the options add +$380.00. Maximum gain is **+$6,180.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 79.4% return on the $7,780.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,380.00** — the shares gain +$5,000.00 and the options add +$380.00. Maximum gain is **+$6,180.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 79.4% return on the $7,780.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,380.00** — the shares gain +$5,000.00 and the options add +$380.00. Maximum gain is **+$6,180.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 79.4% return on the $7,780.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $7,780.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,380.00** — the shares gain +$5,000.00 and the options add +$380.00. Maximum gain is **+$6,180.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 79.4% return on the $7,780.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$6,180.00**"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$6,180.00** — the short call limits further upside. The trade-off: $380.00 in collected premium in exchange for giving up gains above $108.00. That represents a 79.4% return on the $7,780.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$6,180.00** — the short call limits further upside. The trade-off: $380.00 in collected premium in exchange for giving up gains above $108.00. That represents a 79.4% return on the $7,780.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $7,780.00"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$6,180.00** — the short call limits further upside. The trade-off: $380.00 in collected premium in exchange for giving up gains above $108.00. That represents a 79.4% return on the $7,780.00 capital at risk."

### Strategy: Covered Short Strangle (ID=46) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$320.00**"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **−$320.00**. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk."

**Zone**: bearish
**Check**: DECLINE_RISING
**Text**: "'position declines' but P&L rises (-5810->380)"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **−$320.00**. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $380.00 credit is retained. That represents a 13.7% return on the $2,780.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,780.00"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $380.00 credit is retained. That represents a 13.7% return on the $2,780.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$320.00**"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$320.00**. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 13.7% return on the $2,780.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$380.00**"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$320.00**. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 13.7% return on the $2,780.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$320.00**. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 13.7% return on the $2,780.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,780.00"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$320.00**. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 13.7% return on the $2,780.00 capital at risk."

### Strategy: Long Box Spread (ID=47) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Below $92.00, the short $92.00 put drives losses, but the long $108.00 put provides a hard floor. Maximum loss is **$0.00** at any price below $300.00. Breakevens are $88.29 (11.7% below spot) and $92.00 (8.0% below spot) (among multiple breakevens)."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Between $92.00 and $108.00, losses are stable at **$0.00**. Breakevens are $92.00 (8.0% below spot) and $103.34 (3.3% above spot) and $108.00 (8.0% above spot)."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Above $108.00, the short $108.00 call drives losses, but the long $92.00 call caps the damage. Maximum loss is **$0.00** at any price above $0.00. Breakevens are $108.00 (8.0% above spot) and $108.36 (8.4% above spot) (among multiple breakevens)."

### Strategy: Short Box Spread (ID=48) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Below $92.00, the short $108.00 put drives losses, but the long $92.00 put provides a hard floor. Maximum loss is **$0.00** at any price below $300.00. Breakevens are $88.29 (11.7% below spot) and $92.00 (8.0% below spot) (among multiple breakevens)."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Above $108.00, the short $92.00 call drives losses, but the long $108.00 call caps the damage. Maximum loss is **$0.00** at any price above $0.00. Breakevens are $108.00 (8.0% above spot) and $108.36 (8.4% above spot) (among multiple breakevens)."

### Strategy: Synthetic Long Stock (ID=49) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,000.00**"
**Full body**: "Below $100.00, the position declines with the stock. At $90.00, the position is **−$1,000.00**. Breakeven is $100.00 (0.0% above spot). Maximum loss is **−$10,000.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$10,000.00**"
**Full body**: "Below $100.00, the position declines with the stock. At $90.00, the position is **−$1,000.00**. Breakeven is $100.00 (0.0% above spot). Maximum loss is **−$10,000.00**."

**Zone**: bearish
**Check**: DECLINE_RISING
**Text**: "'position declines' but P&L rises (-6990->-500)"
**Full body**: "Below $100.00, the position declines with the stock. At $90.00, the position is **−$1,000.00**. Breakeven is $100.00 (0.0% above spot). Maximum loss is **−$10,000.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot)."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,000.00**"
**Full body**: "Above $100.00, the position rises with the stock. At $110.00, the position is **+$1,000.00**. Breakeven is $100.00 (0.0% above spot). There is no cap on upside gains."

### Strategy: Short Call (ID=5) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$250.00**"
**Full body**: "At any price below $100.00, gains are locked in at **+$250.00**."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $100.00, gains are locked in at **+$250.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$250.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$250.00**. Maximum gain is **+$250.00**. That represents an 11.1% return on the $2,250.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$250.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$250.00**. Maximum gain is **+$250.00**. That represents an 11.1% return on the $2,250.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$250.00**. Maximum gain is **+$250.00**. That represents an 11.1% return on the $2,250.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,250.00"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$250.00**. Maximum gain is **+$250.00**. That represents an 11.1% return on the $2,250.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$750.00**"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$750.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$250.00**. That represents an 11.1% return on the $2,250.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$250.00**"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$750.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$250.00**. That represents an 11.1% return on the $2,250.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$750.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$250.00**. That represents an 11.1% return on the $2,250.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,250.00"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$750.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$250.00**. That represents an 11.1% return on the $2,250.00 capital at risk."

### Strategy: Synthetic Short Stock (ID=50) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,000.00**"
**Full body**: "Below $100.00, the position gains value as the stock falls. At $90.00, the position is **+$1,000.00**. Breakeven is $100.00 (0.0% above spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$10,000.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,250.00"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,000.00**"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$1,000.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$10,000.00**"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$1,000.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$1,000.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,250.00"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$1,000.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk."

### Strategy: Long Combo (ID=51) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$700.00**"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **−$700.00**. Breakeven is $92.00 (8.0% below spot). Maximum loss is **−$9,200.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$9,200.00**"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **−$700.00**. Breakeven is $92.00 (8.0% below spot). Maximum loss is **−$9,200.00**."

**Zone**: bearish
**Check**: DECLINE_RISING
**Text**: "'position declines' but P&L rises (-6190->0)"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **−$700.00**. Breakeven is $92.00 (8.0% below spot). Maximum loss is **−$9,200.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Between $92.00 and $108.00, the position captures its maximum gain of **$0.00**. Breakevens are $99.33 (0.7% below spot) and $100.33 (0.3% above spot) (among multiple breakevens)."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$700.00**"
**Full body**: "Above $108.00, the position rises with the stock. At $115.00, the position is **+$700.00**. Breakeven is $108.00 (8.0% above spot). There is no cap on upside gains."

### Strategy: Short Combo (ID=52) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$700.00**"
**Full body**: "Below $92.00, the position gains value as the stock falls. At $85.00, the position is **+$700.00**. Breakeven is $92.00 (8.0% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Between $92.00 and $108.00, the position captures its maximum gain of **$0.00**. Breakevens are $99.33 (0.7% below spot) and $100.33 (0.3% above spot) (among multiple breakevens). That represents significant leverage on the $1,390.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, the position captures its maximum gain of **$0.00**. Breakevens are $99.33 (0.7% below spot) and $100.33 (0.3% above spot) (among multiple breakevens). That represents significant leverage on the $1,390.00 capital at risk."

**Zone**: stagnant
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $1,390"
**Full body**: "Between $92.00 and $108.00, the position captures its maximum gain of **$0.00**. Breakevens are $99.33 (0.7% below spot) and $100.33 (0.3% above spot) (among multiple breakevens). That represents significant leverage on the $1,390.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$700.00**"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$700.00**. Breakeven is $108.00 (8.0% above spot). Maximum gain is **+$9,200.00**. That represents significant leverage on the $1,390.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$9,200.00**"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$700.00**. Breakeven is $108.00 (8.0% above spot). Maximum gain is **+$9,200.00**. That represents significant leverage on the $1,390.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$700.00**. Breakeven is $108.00 (8.0% above spot). Maximum gain is **+$9,200.00**. That represents significant leverage on the $1,390.00 capital at risk."

**Zone**: bullish
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $1,390"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$700.00**. Breakeven is $108.00 (8.0% above spot). Maximum gain is **+$9,200.00**. That represents significant leverage on the $1,390.00 capital at risk."

### Strategy: L. Call Syn. Straddle (ID=53) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is **+$500.00** — the shares gain +$1,000.00 and the options cost −$500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$500.00**"
**Full body**: "Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is **−$500.00** — the shares gain $0.00 and the options cost −$500.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **+$500.00** — the shares lose −$1,000.00 and the options add +$1,500.00. Breakeven is $105.00 (5.0% above spot). There is no cap on upside gains."

### Strategy: L. Call Syn. Straddle (ID=53) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$2,000.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is **+$2,000.00** — the shares gain +$2,500.00 and the options cost −$500.00. There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,000.00**"
**Full body**: "Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is **+$1,000.00** — the shares gain +$1,500.00 and the options cost −$500.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$2,000.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **+$2,000.00** — the shares gain +$500.00 and the options add +$1,500.00. There is no cap on upside gains."

### Strategy: L. Call Syn. Straddle (ID=53) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$5,500.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is **+$5,500.00** — the shares gain +$6,000.00 and the options cost −$500.00. There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$4,500.00**"
**Full body**: "Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is **+$4,500.00** — the shares gain +$5,000.00 and the options cost −$500.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$5,500.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **+$5,500.00** — the shares gain +$4,000.00 and the options add +$1,500.00. There is no cap on upside gains."

### Strategy: L. Call Syn. Straddle (ID=53) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,000.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is **−$1,000.00** — the shares lose −$500.00 and the options cost −$500.00. Breakeven is $80.00 (20.0% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$2,000.00**"
**Full body**: "Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is **−$2,000.00** — the shares lose −$1,500.00 and the options cost −$500.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,000.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **−$1,000.00** — the shares lose −$2,500.00 and the options add +$1,500.00. Breakeven is $120.00 (20.0% above spot). There is no cap on upside gains."

### Strategy: L. Call Syn. Straddle (ID=53) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$4,500.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is **−$4,500.00** — the shares lose −$4,000.00 and the options cost −$500.00. Breakeven is $45.00 (55.0% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$5,500.00**"
**Full body**: "Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is **−$5,500.00** — the shares lose −$5,000.00 and the options cost −$500.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$4,500.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **−$4,500.00** — the shares lose −$6,000.00 and the options add +$1,500.00. Breakeven is $155.00 (55.0% above spot). There is no cap on upside gains."

### Strategy: L. Call Syn. Straddle (ID=53) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$500.00**"
**Full body**: "At any price below $100.00, losses are capped at **−$500.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$500.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **−$500.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,500.00**"
**Full body**: "Above $100.00, the position rises with the stock. At $110.00, the position is **+$1,500.00**. Breakeven is $102.50 (2.5% above spot). There is no cap on upside gains."

### Strategy: L. Put Syn. Straddle (ID=54) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is **+$500.00** — the shares lose −$1,000.00 and the options add +$1,500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk. Without the put, a drop to $90.00 would mean a −$1,000.00 loss on the shares alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$500.00**"
**Full body**: "Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is **−$500.00** — the shares gain $0.00 and the options cost −$500.00. The cost of protection: $500.00 (5.0% of the position) for a guaranteed loss limit at $100.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **+$500.00** — the shares gain +$1,000.00 and the options cost −$500.00. Breakeven is $105.00 (5.0% above spot). There is no cap on upside gains."

### Strategy: L. Put Syn. Straddle (ID=54) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,000.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is **−$1,000.00** — the shares lose −$2,500.00 and the options add +$1,500.00. Breakeven is $80.00 (20.0% below spot). There is no cap on downside risk. Without the put, a drop to $90.00 would mean a −$2,500.00 loss on the shares alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$2,000.00**"
**Full body**: "Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is **−$2,000.00** — the shares lose −$1,500.00 and the options cost −$500.00. The cost of protection: $500.00 (5.0% of the position) for a guaranteed loss limit at $100.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,000.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **−$1,000.00** — the shares lose −$500.00 and the options cost −$500.00. Breakeven is $120.00 (20.0% above spot). There is no cap on upside gains."

### Strategy: L. Put Syn. Straddle (ID=54) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$4,500.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is **−$4,500.00** — the shares lose −$6,000.00 and the options add +$1,500.00. Breakeven is $45.00 (55.0% below spot). There is no cap on downside risk. Without the put, a drop to $90.00 would mean a −$6,000.00 loss on the shares alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$5,500.00**"
**Full body**: "Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is **−$5,500.00** — the shares lose −$5,000.00 and the options cost −$500.00. The cost of protection: $500.00 (5.0% of the position) for a guaranteed loss limit at $100.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$4,500.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **−$4,500.00** — the shares lose −$4,000.00 and the options cost −$500.00. Breakeven is $155.00 (55.0% above spot). There is no cap on upside gains."

### Strategy: L. Put Syn. Straddle (ID=54) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$2,000.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is **+$2,000.00** — the shares gain +$500.00 and the options add +$1,500.00. There is no cap on downside risk. Without the put, a drop to $90.00 would mean a +$500.00 loss on the shares alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,000.00**"
**Full body**: "Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is **+$1,000.00** — the shares gain +$1,500.00 and the options cost −$500.00. The cost of protection: $500.00 (5.0% of the position) for a guaranteed loss limit at $100.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$2,000.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **+$2,000.00** — the shares gain +$2,500.00 and the options cost −$500.00. There is no cap on upside gains."

### Strategy: L. Put Syn. Straddle (ID=54) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$5,500.00**"
**Full body**: "Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is **+$5,500.00** — the shares gain +$4,000.00 and the options add +$1,500.00. There is no cap on downside risk. Without the put, a drop to $90.00 would mean a +$4,000.00 loss on the shares alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$4,500.00**"
**Full body**: "Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is **+$4,500.00** — the shares gain +$5,000.00 and the options cost −$500.00. The cost of protection: $500.00 (5.0% of the position) for a guaranteed loss limit at $100.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$5,500.00**"
**Full body**: "Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **+$5,500.00** — the shares gain +$6,000.00 and the options cost −$500.00. There is no cap on upside gains."

### Strategy: L. Put Syn. Straddle (ID=54) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,500.00**"
**Full body**: "Below $100.00, the position gains value as the stock falls. At $90.00, the position is **+$1,500.00**. Breakeven is $97.50 (2.5% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$500.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **−$500.00**. Maximum gain is **+$19,500.00**. That represents significant leverage on the $500.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$19,500.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **−$500.00**. Maximum gain is **+$19,500.00**. That represents significant leverage on the $500.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **−$500.00**. Maximum gain is **+$19,500.00**. That represents significant leverage on the $500.00 capital at risk."

**Zone**: stagnant
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $500"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **−$500.00**. Maximum gain is **+$19,500.00**. That represents significant leverage on the $500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$500.00**"
**Full body**: "At any price above $100.00, losses are capped at **−$500.00**. That represents significant leverage on the $500.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $100.00, losses are capped at **−$500.00**. That represents significant leverage on the $500.00 capital at risk."

**Zone**: bullish
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $500"
**Full body**: "At any price above $100.00, losses are capped at **−$500.00**. That represents significant leverage on the $500.00 capital at risk."

### Strategy: S. Call Syn. Straddle (ID=55) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure, but the +$500.00 from the options cushions the move. At $90.00, the client's combined position is **−$500.00** — the shares lose −$1,000.00 and the options add +$500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk. Without the options, the loss would be −$1,000.00."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 3.3% return on the $15,000.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 3.3% return on the $15,000.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 3.3% return on the $15,000.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 3.3% return on the $15,000.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $15,000.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 3.3% return on the $15,000.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$500.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$500.00** — the shares gain +$1,000.00 and the options cost −$1,500.00. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents a 3.3% return on the $15,000.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$500.00** — the shares gain +$1,000.00 and the options cost −$1,500.00. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents a 3.3% return on the $15,000.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$500.00** — the shares gain +$1,000.00 and the options cost −$1,500.00. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents a 3.3% return on the $15,000.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $15,000.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$500.00** — the shares gain +$1,000.00 and the options cost −$1,500.00. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents a 3.3% return on the $15,000.00 capital at risk."

### Strategy: S. Call Syn. Straddle (ID=55) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$2,000.00**"
**Full body**: "Below $100.00, the client still has full downside exposure, but the +$500.00 from the options cushions the move. At $90.00, the client's combined position is **−$2,000.00** — the shares lose −$2,500.00 and the options add +$500.00. There is no cap on downside risk. Without the options, the loss would be −$2,500.00."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,000.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,000.00** — the shares lose −$1,500.00 and the options add +$500.00. Maximum gain is **−$1,000.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,000.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,000.00** — the shares lose −$1,500.00 and the options add +$500.00. Maximum gain is **−$1,000.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$1,000.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,000.00** — the shares lose −$1,500.00 and the options add +$500.00. Maximum gain is **−$1,000.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,000.00** — the shares lose −$1,500.00 and the options add +$500.00. Maximum gain is **−$1,000.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$2,000.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$2,000.00** — the shares lose −$500.00 and the options cost −$1,500.00. Maximum gain is **−$1,000.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,000.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$2,000.00** — the shares lose −$500.00 and the options cost −$1,500.00. Maximum gain is **−$1,000.00**."

**Zone**: bullish
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$1,000.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$2,000.00** — the shares lose −$500.00 and the options cost −$1,500.00. Maximum gain is **−$1,000.00**."

### Strategy: S. Call Syn. Straddle (ID=55) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$5,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure, but the +$500.00 from the options cushions the move. At $90.00, the client's combined position is **−$5,500.00** — the shares lose −$6,000.00 and the options add +$500.00. There is no cap on downside risk. Without the options, the loss would be −$6,000.00."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$4,500.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,500.00** — the shares lose −$5,000.00 and the options add +$500.00. Maximum gain is **−$4,500.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$4,500.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,500.00** — the shares lose −$5,000.00 and the options add +$500.00. Maximum gain is **−$4,500.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$4,500.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,500.00** — the shares lose −$5,000.00 and the options add +$500.00. Maximum gain is **−$4,500.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,500.00** — the shares lose −$5,000.00 and the options add +$500.00. Maximum gain is **−$4,500.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$5,500.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$5,500.00** — the shares lose −$4,000.00 and the options cost −$1,500.00. Maximum gain is **−$4,500.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$4,500.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$5,500.00** — the shares lose −$4,000.00 and the options cost −$1,500.00. Maximum gain is **−$4,500.00**."

**Zone**: bullish
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$4,500.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$5,500.00** — the shares lose −$4,000.00 and the options cost −$1,500.00. Maximum gain is **−$4,500.00**."

### Strategy: S. Call Syn. Straddle (ID=55) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,000.00**"
**Full body**: "Below $100.00, the client still has full downside exposure, but the +$500.00 from the options cushions the move. At $90.00, the client's combined position is **+$1,000.00** — the shares gain +$500.00 and the options add +$500.00. Breakeven is $80.00 (20.0% below spot). There is no cap on downside risk. Without the options, the loss would be +$500.00."

**Zone**: bearish
**Check**: LOSS_POSITIVE
**Text**: "loss would be +$500.00"
**Full body**: "Below $100.00, the client still has full downside exposure, but the +$500.00 from the options cushions the move. At $90.00, the client's combined position is **+$1,000.00** — the shares gain +$500.00 and the options add +$500.00. Breakeven is $80.00 (20.0% below spot). There is no cap on downside risk. Without the options, the loss would be +$500.00."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$2,000.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$2,000.00** — the shares gain +$1,500.00 and the options add +$500.00. Maximum gain is **+$2,000.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 14.8% return on the $13,500.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$2,000.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$2,000.00** — the shares gain +$1,500.00 and the options add +$500.00. Maximum gain is **+$2,000.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 14.8% return on the $13,500.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$2,000.00** — the shares gain +$1,500.00 and the options add +$500.00. Maximum gain is **+$2,000.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 14.8% return on the $13,500.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$2,000.00** — the shares gain +$1,500.00 and the options add +$500.00. Maximum gain is **+$2,000.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 14.8% return on the $13,500.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $13,500.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$2,000.00** — the shares gain +$1,500.00 and the options add +$500.00. Maximum gain is **+$2,000.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 14.8% return on the $13,500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,000.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **+$1,000.00** — the shares gain +$2,500.00 and the options cost −$1,500.00. Breakeven is $120.00 (20.0% above spot). Maximum gain is **+$2,000.00**. That represents a 14.8% return on the $13,500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$2,000.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **+$1,000.00** — the shares gain +$2,500.00 and the options cost −$1,500.00. Breakeven is $120.00 (20.0% above spot). Maximum gain is **+$2,000.00**. That represents a 14.8% return on the $13,500.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **+$1,000.00** — the shares gain +$2,500.00 and the options cost −$1,500.00. Breakeven is $120.00 (20.0% above spot). Maximum gain is **+$2,000.00**. That represents a 14.8% return on the $13,500.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $13,500.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **+$1,000.00** — the shares gain +$2,500.00 and the options cost −$1,500.00. Breakeven is $120.00 (20.0% above spot). Maximum gain is **+$2,000.00**. That represents a 14.8% return on the $13,500.00 capital at risk."

### Strategy: S. Call Syn. Straddle (ID=55) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$4,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure, but the +$500.00 from the options cushions the move. At $90.00, the client's combined position is **+$4,500.00** — the shares gain +$4,000.00 and the options add +$500.00. Breakeven is $45.00 (55.0% below spot). There is no cap on downside risk. Without the options, the loss would be +$4,000.00."

**Zone**: bearish
**Check**: LOSS_POSITIVE
**Text**: "loss would be +$4,000.00"
**Full body**: "Below $100.00, the client still has full downside exposure, but the +$500.00 from the options cushions the move. At $90.00, the client's combined position is **+$4,500.00** — the shares gain +$4,000.00 and the options add +$500.00. Breakeven is $45.00 (55.0% below spot). There is no cap on downside risk. Without the options, the loss would be +$4,000.00."

**Zone**: bearish
**Check**: MISLEADING_DOWNSIDE
**Text**: "full downside exposure (avg_cost=50, spot=100.0)"
**Full body**: "Below $100.00, the client still has full downside exposure, but the +$500.00 from the options cushions the move. At $90.00, the client's combined position is **+$4,500.00** — the shares gain +$4,000.00 and the options add +$500.00. Breakeven is $45.00 (55.0% below spot). There is no cap on downside risk. Without the options, the loss would be +$4,000.00."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,500.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,500.00** — the shares gain +$5,000.00 and the options add +$500.00. Maximum gain is **+$5,500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 55.0% return on the $10,000.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,500.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,500.00** — the shares gain +$5,000.00 and the options add +$500.00. Maximum gain is **+$5,500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 55.0% return on the $10,000.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,500.00** — the shares gain +$5,000.00 and the options add +$500.00. Maximum gain is **+$5,500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 55.0% return on the $10,000.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,500.00** — the shares gain +$5,000.00 and the options add +$500.00. Maximum gain is **+$5,500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 55.0% return on the $10,000.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $10,000.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,500.00** — the shares gain +$5,000.00 and the options add +$500.00. Maximum gain is **+$5,500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 55.0% return on the $10,000.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$4,500.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **+$4,500.00** — the shares gain +$6,000.00 and the options cost −$1,500.00. Breakeven is $155.00 (55.0% above spot). Maximum gain is **+$5,500.00**. That represents a 55.0% return on the $10,000.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$5,500.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **+$4,500.00** — the shares gain +$6,000.00 and the options cost −$1,500.00. Breakeven is $155.00 (55.0% above spot). Maximum gain is **+$5,500.00**. That represents a 55.0% return on the $10,000.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **+$4,500.00** — the shares gain +$6,000.00 and the options cost −$1,500.00. Breakeven is $155.00 (55.0% above spot). Maximum gain is **+$5,500.00**. That represents a 55.0% return on the $10,000.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $10,000.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **+$4,500.00** — the shares gain +$6,000.00 and the options cost −$1,500.00. Breakeven is $155.00 (55.0% above spot). Maximum gain is **+$5,500.00**. That represents a 55.0% return on the $10,000.00 capital at risk."

### Strategy: S. Call Syn. Straddle (ID=55) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "At any price below $100.00, gains are locked in at **+$500.00**."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $100.00, gains are locked in at **+$500.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$500.00**. Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$500.00**. Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$500.00**. Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $4,500.00"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$500.00**. Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,500.00**"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$1,500.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$1,500.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$1,500.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $4,500.00"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$1,500.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$500.00**. That represents an 11.1% return on the $4,500.00 capital at risk."

### Strategy: S. Put Syn. Straddle (ID=56) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$500.00** — the shares gain +$1,000.00 and the options cost −$1,500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 3.4% return on the $14,500.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 3.4% return on the $14,500.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 3.4% return on the $14,500.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 3.4% return on the $14,500.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $14,500.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 3.4% return on the $14,500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$500.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$500.00** — the shares lose −$1,000.00 and the options add +$500.00. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents a 3.4% return on the $14,500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$500.00** — the shares lose −$1,000.00 and the options add +$500.00. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents a 3.4% return on the $14,500.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$500.00** — the shares lose −$1,000.00 and the options add +$500.00. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents a 3.4% return on the $14,500.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $14,500.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$500.00** — the shares lose −$1,000.00 and the options add +$500.00. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents a 3.4% return on the $14,500.00 capital at risk."

### Strategy: S. Put Syn. Straddle (ID=56) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,000.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **+$1,000.00** — the shares gain +$2,500.00 and the options cost −$1,500.00. Breakeven is $80.00 (20.0% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$2,000.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$2,000.00** — the shares gain +$1,500.00 and the options add +$500.00. Maximum gain is **+$2,000.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 12.5% return on the $16,000.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$2,000.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$2,000.00** — the shares gain +$1,500.00 and the options add +$500.00. Maximum gain is **+$2,000.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 12.5% return on the $16,000.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$2,000.00** — the shares gain +$1,500.00 and the options add +$500.00. Maximum gain is **+$2,000.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 12.5% return on the $16,000.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$2,000.00** — the shares gain +$1,500.00 and the options add +$500.00. Maximum gain is **+$2,000.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 12.5% return on the $16,000.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $16,000.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$2,000.00** — the shares gain +$1,500.00 and the options add +$500.00. Maximum gain is **+$2,000.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 12.5% return on the $16,000.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,000.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **+$1,000.00** — the shares gain +$500.00 and the options add +$500.00. Breakeven is $120.00 (20.0% above spot). Maximum gain is **+$2,000.00**. That represents a 12.5% return on the $16,000.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$2,000.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **+$1,000.00** — the shares gain +$500.00 and the options add +$500.00. Breakeven is $120.00 (20.0% above spot). Maximum gain is **+$2,000.00**. That represents a 12.5% return on the $16,000.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **+$1,000.00** — the shares gain +$500.00 and the options add +$500.00. Breakeven is $120.00 (20.0% above spot). Maximum gain is **+$2,000.00**. That represents a 12.5% return on the $16,000.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $16,000.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **+$1,000.00** — the shares gain +$500.00 and the options add +$500.00. Breakeven is $120.00 (20.0% above spot). Maximum gain is **+$2,000.00**. That represents a 12.5% return on the $16,000.00 capital at risk."

### Strategy: S. Put Syn. Straddle (ID=56) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$4,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **+$4,500.00** — the shares gain +$6,000.00 and the options cost −$1,500.00. Breakeven is $45.00 (55.0% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,500.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,500.00** — the shares gain +$5,000.00 and the options add +$500.00. Maximum gain is **+$5,500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 28.2% return on the $19,500.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,500.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,500.00** — the shares gain +$5,000.00 and the options add +$500.00. Maximum gain is **+$5,500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 28.2% return on the $19,500.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,500.00** — the shares gain +$5,000.00 and the options add +$500.00. Maximum gain is **+$5,500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 28.2% return on the $19,500.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,500.00** — the shares gain +$5,000.00 and the options add +$500.00. Maximum gain is **+$5,500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 28.2% return on the $19,500.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $19,500.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,500.00** — the shares gain +$5,000.00 and the options add +$500.00. Maximum gain is **+$5,500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 28.2% return on the $19,500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$4,500.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **+$4,500.00** — the shares gain +$4,000.00 and the options add +$500.00. Breakeven is $155.00 (55.0% above spot). Maximum gain is **+$5,500.00**. That represents a 28.2% return on the $19,500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$5,500.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **+$4,500.00** — the shares gain +$4,000.00 and the options add +$500.00. Breakeven is $155.00 (55.0% above spot). Maximum gain is **+$5,500.00**. That represents a 28.2% return on the $19,500.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **+$4,500.00** — the shares gain +$4,000.00 and the options add +$500.00. Breakeven is $155.00 (55.0% above spot). Maximum gain is **+$5,500.00**. That represents a 28.2% return on the $19,500.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $19,500.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **+$4,500.00** — the shares gain +$4,000.00 and the options add +$500.00. Breakeven is $155.00 (55.0% above spot). Maximum gain is **+$5,500.00**. That represents a 28.2% return on the $19,500.00 capital at risk."

### Strategy: S. Put Syn. Straddle (ID=56) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$2,000.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$2,000.00** — the shares lose −$500.00 and the options cost −$1,500.00. There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,000.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,000.00** — the shares lose −$1,500.00 and the options add +$500.00. Maximum gain is **−$1,000.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,000.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,000.00** — the shares lose −$1,500.00 and the options add +$500.00. Maximum gain is **−$1,000.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$1,000.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,000.00** — the shares lose −$1,500.00 and the options add +$500.00. Maximum gain is **−$1,000.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,000.00** — the shares lose −$1,500.00 and the options add +$500.00. Maximum gain is **−$1,000.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$2,000.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$2,000.00** — the shares lose −$2,500.00 and the options add +$500.00. Maximum gain is **−$1,000.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,000.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$2,000.00** — the shares lose −$2,500.00 and the options add +$500.00. Maximum gain is **−$1,000.00**."

**Zone**: bullish
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$1,000.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$2,000.00** — the shares lose −$2,500.00 and the options add +$500.00. Maximum gain is **−$1,000.00**."

### Strategy: S. Put Syn. Straddle (ID=56) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$5,500.00**"
**Full body**: "Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$5,500.00** — the shares lose −$4,000.00 and the options cost −$1,500.00. There is no cap on downside risk."

**Zone**: bearish
**Check**: MISLEADING_DOWNSIDE
**Text**: "full downside exposure (avg_cost=50, spot=100.0)"
**Full body**: "Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$5,500.00** — the shares lose −$4,000.00 and the options cost −$1,500.00. There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$4,500.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,500.00** — the shares lose −$5,000.00 and the options add +$500.00. Maximum gain is **−$4,500.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$4,500.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,500.00** — the shares lose −$5,000.00 and the options add +$500.00. Maximum gain is **−$4,500.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$4,500.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,500.00** — the shares lose −$5,000.00 and the options add +$500.00. Maximum gain is **−$4,500.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,500.00** — the shares lose −$5,000.00 and the options add +$500.00. Maximum gain is **−$4,500.00**. The premium adds a 5.0% enhancement over holding the stock alone."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$5,500.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$5,500.00** — the shares lose −$6,000.00 and the options add +$500.00. Maximum gain is **−$4,500.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$4,500.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$5,500.00** — the shares lose −$6,000.00 and the options add +$500.00. Maximum gain is **−$4,500.00**."

**Zone**: bullish
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$4,500.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$5,500.00** — the shares lose −$6,000.00 and the options add +$500.00. Maximum gain is **−$4,500.00**."

### Strategy: S. Put Syn. Straddle (ID=56) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,500.00**"
**Full body**: "Below $100.00, the position declines with the stock. At $90.00, the position is **−$1,500.00**. Breakeven is $97.50 (2.5% below spot). Maximum loss is **−$19,500.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$19,500.00**"
**Full body**: "Below $100.00, the position declines with the stock. At $90.00, the position is **−$1,500.00**. Breakeven is $97.50 (2.5% below spot). Maximum loss is **−$19,500.00**."

**Zone**: bearish
**Check**: DECLINE_RISING
**Text**: "'position declines' but P&L rises (-13480->-500)"
**Full body**: "Below $100.00, the position declines with the stock. At $90.00, the position is **−$1,500.00**. Breakeven is $97.50 (2.5% below spot). Maximum loss is **−$19,500.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$500.00**. Maximum gain is **+$500.00**. That represents a 2.5% return on the $20,000.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$500.00**. Maximum gain is **+$500.00**. That represents a 2.5% return on the $20,000.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$500.00**. Maximum gain is **+$500.00**. That represents a 2.5% return on the $20,000.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $20,000.00"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$500.00**. Maximum gain is **+$500.00**. That represents a 2.5% return on the $20,000.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$500.00**"
**Full body**: "At any price above $100.00, gains are capped at **+$500.00**. That represents a 2.5% return on the $20,000.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $100.00, gains are capped at **+$500.00**. That represents a 2.5% return on the $20,000.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $20,000.00"
**Full body**: "At any price above $100.00, gains are capped at **+$500.00**. That represents a 2.5% return on the $20,000.00 capital at risk."

### Strategy: L. Call Syn. Strangle (ID=57) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$320.00**"
**Full body**: "Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **+$320.00** — the shares gain +$1,500.00 and the options cost −$1,180.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$380.00**"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$380.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$320.00**"
**Full body**: "Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$320.00** — the shares lose −$1,500.00 and the options add +$1,820.00. Breakeven is $111.80 (11.8% above spot). There is no cap on upside gains."

### Strategy: L. Call Syn. Strangle (ID=57) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,820.00**"
**Full body**: "Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **+$1,820.00** — the shares gain +$3,000.00 and the options cost −$1,180.00. There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,120.00**"
**Full body**: "Between $92.00 and $108.00, the position captures its maximum gain of **+$1,120.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,820.00**"
**Full body**: "Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$1,820.00** — the shares lose $0.00 and the options add +$1,820.00. There is no cap on upside gains."

### Strategy: L. Call Syn. Strangle (ID=57) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$5,320.00**"
**Full body**: "Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **+$5,320.00** — the shares gain +$6,500.00 and the options cost −$1,180.00. There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$4,620.00**"
**Full body**: "Between $92.00 and $108.00, the position captures its maximum gain of **+$4,620.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$5,320.00**"
**Full body**: "Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$5,320.00** — the shares gain +$3,500.00 and the options add +$1,820.00. There is no cap on upside gains."

### Strategy: L. Call Syn. Strangle (ID=57) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,180.00**"
**Full body**: "Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **−$1,180.00** — the shares gain $0.00 and the options cost −$1,180.00. Breakeven is $73.20 (26.8% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,880.00**"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$1,880.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,180.00**"
**Full body**: "Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **−$1,180.00** — the shares lose −$3,000.00 and the options add +$1,820.00. Breakeven is $126.80 (26.8% above spot). There is no cap on upside gains."

### Strategy: L. Call Syn. Strangle (ID=57) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$4,680.00**"
**Full body**: "Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **−$4,680.00** — the shares lose −$3,500.00 and the options cost −$1,180.00. Breakeven is $38.20 (61.8% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$5,380.00**"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$5,380.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$4,680.00**"
**Full body**: "Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **−$4,680.00** — the shares lose −$6,500.00 and the options add +$1,820.00. Breakeven is $161.80 (61.8% above spot). There is no cap on upside gains."

### Strategy: L. Call Syn. Strangle (ID=57) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,180.00**"
**Full body**: "At any price below $92.00, losses are capped at **−$1,180.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$380.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **−$380.00**. Breakeven is $103.80 (3.8% above spot)."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,820.00**"
**Full body**: "Above $108.00, the position rises with the stock. At $115.00, the position is **+$1,820.00**. There is no cap on upside gains."

### Strategy: L. Put Syn. Strangle (ID=58) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$320.00**"
**Full body**: "Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **+$320.00** — the shares lose −$1,500.00 and the options add +$1,820.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$380.00**"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$380.00**. The cost of protection: $1,180.00 (11.8% of the position) for a guaranteed loss limit at $92.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$320.00**"
**Full body**: "Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$320.00** — the shares gain +$1,500.00 and the options cost −$1,180.00. Breakeven is $111.80 (11.8% above spot). There is no cap on upside gains."

### Strategy: L. Put Syn. Strangle (ID=58) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,180.00**"
**Full body**: "Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **−$1,180.00** — the shares lose −$3,000.00 and the options add +$1,820.00. Breakeven is $73.20 (26.8% below spot). There is no cap on downside risk. Without the put, a drop to $85.00 would mean a −$3,000.00 loss on the shares alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,880.00**"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$1,880.00**. The cost of protection: $1,180.00 (11.8% of the position) for a guaranteed loss limit at $92.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,180.00**"
**Full body**: "Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **−$1,180.00** — the shares gain $0.00 and the options cost −$1,180.00. Breakeven is $126.80 (26.8% above spot). There is no cap on upside gains."

### Strategy: L. Put Syn. Strangle (ID=58) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$4,680.00**"
**Full body**: "Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **−$4,680.00** — the shares lose −$6,500.00 and the options add +$1,820.00. Breakeven is $38.20 (61.8% below spot). There is no cap on downside risk. Without the put, a drop to $85.00 would mean a −$6,500.00 loss on the shares alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$5,380.00**"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$5,380.00**. The cost of protection: $1,180.00 (11.8% of the position) for a guaranteed loss limit at $92.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$4,680.00**"
**Full body**: "Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **−$4,680.00** — the shares lose −$3,500.00 and the options cost −$1,180.00. Breakeven is $161.80 (61.8% above spot). There is no cap on upside gains."

### Strategy: L. Put Syn. Strangle (ID=58) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,820.00**"
**Full body**: "Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **+$1,820.00** — the shares lose $0.00 and the options add +$1,820.00. There is no cap on downside risk. Without the put, a drop to $85.00 would mean a $0.00 loss on the shares alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,120.00**"
**Full body**: "Between $92.00 and $108.00, the position captures its maximum gain of **+$1,120.00**. The cost of protection: $1,180.00 (11.8% of the position) for a guaranteed loss limit at $92.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,820.00**"
**Full body**: "Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$1,820.00** — the shares gain +$3,000.00 and the options cost −$1,180.00. There is no cap on upside gains."

### Strategy: L. Put Syn. Strangle (ID=58) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$5,320.00**"
**Full body**: "Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **+$5,320.00** — the shares gain +$3,500.00 and the options add +$1,820.00. There is no cap on downside risk. Without the put, a drop to $85.00 would mean a +$3,500.00 loss on the shares alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$4,620.00**"
**Full body**: "Between $92.00 and $108.00, the position captures its maximum gain of **+$4,620.00**. The cost of protection: $1,180.00 (11.8% of the position) for a guaranteed loss limit at $92.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$5,320.00**"
**Full body**: "Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$5,320.00** — the shares gain +$6,500.00 and the options cost −$1,180.00. There is no cap on upside gains."

### Strategy: L. Put Syn. Strangle (ID=58) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,820.00**"
**Full body**: "Below $92.00, the position gains value as the stock falls. At $85.00, the position is **+$1,820.00**. There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$380.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **−$380.00**. Breakeven is $96.20 (3.8% below spot). Maximum gain is **+$18,820.00**. That represents significant leverage on the $1,180.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$18,820.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **−$380.00**. Breakeven is $96.20 (3.8% below spot). Maximum gain is **+$18,820.00**. That represents significant leverage on the $1,180.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **−$380.00**. Breakeven is $96.20 (3.8% below spot). Maximum gain is **+$18,820.00**. That represents significant leverage on the $1,180.00 capital at risk."

**Zone**: stagnant
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $1,180"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **−$380.00**. Breakeven is $96.20 (3.8% below spot). Maximum gain is **+$18,820.00**. That represents significant leverage on the $1,180.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,180.00**"
**Full body**: "At any price above $108.00, losses are capped at **−$1,180.00**. That represents significant leverage on the $1,180.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, losses are capped at **−$1,180.00**. That represents significant leverage on the $1,180.00 capital at risk."

**Zone**: bullish
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $1,180"
**Full body**: "At any price above $108.00, losses are capped at **−$1,180.00**. That represents significant leverage on the $1,180.00 capital at risk."

### Strategy: S. Call Syn. Strangle (ID=59) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$320.00**"
**Full body**: "Below $92.00, the client still has full downside exposure, but the +$1,180.00 from the options cushions the move. At $85.00, the client's combined position is **−$320.00** — the shares lose −$1,500.00 and the options add +$1,180.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk. Without the options, the loss would be −$1,500.00."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 2.5% return on the $15,000.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 2.5% return on the $15,000.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $15,000.00"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 2.5% return on the $15,000.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$320.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$320.00** — the shares gain +$1,500.00 and the options cost −$1,820.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 2.5% return on the $15,000.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$380.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$320.00** — the shares gain +$1,500.00 and the options cost −$1,820.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 2.5% return on the $15,000.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$320.00** — the shares gain +$1,500.00 and the options cost −$1,820.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 2.5% return on the $15,000.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $15,000.00"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$320.00** — the shares gain +$1,500.00 and the options cost −$1,820.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 2.5% return on the $15,000.00 capital at risk."

### Strategy: S. Call Syn. Strangle (ID=59) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,820.00**"
**Full body**: "Below $92.00, the client still has full downside exposure, but the +$1,180.00 from the options cushions the move. At $85.00, the client's combined position is **−$1,820.00** — the shares lose −$3,000.00 and the options add +$1,180.00. There is no cap on downside risk. Without the options, the loss would be −$3,000.00."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,120.00**"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$1,120.00**. The premium adds a 3.8% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$1,120.00**. The premium adds a 3.8% enhancement over holding the stock alone."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,820.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$1,820.00** — the shares gain $0.00 and the options cost −$1,820.00. Maximum gain is **−$1,120.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,120.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$1,820.00** — the shares gain $0.00 and the options cost −$1,820.00. Maximum gain is **−$1,120.00**."

**Zone**: bullish
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$1,120.00"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$1,820.00** — the shares gain $0.00 and the options cost −$1,820.00. Maximum gain is **−$1,120.00**."

### Strategy: S. Call Syn. Strangle (ID=59) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$5,320.00**"
**Full body**: "Below $92.00, the client still has full downside exposure, but the +$1,180.00 from the options cushions the move. At $85.00, the client's combined position is **−$5,320.00** — the shares lose −$6,500.00 and the options add +$1,180.00. There is no cap on downside risk. Without the options, the loss would be −$6,500.00."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$4,620.00**"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$4,620.00**. The premium adds a 3.8% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$4,620.00**. The premium adds a 3.8% enhancement over holding the stock alone."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$5,320.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$5,320.00** — the shares lose −$3,500.00 and the options cost −$1,820.00. Maximum gain is **−$4,620.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$4,620.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$5,320.00** — the shares lose −$3,500.00 and the options cost −$1,820.00. Maximum gain is **−$4,620.00**."

**Zone**: bullish
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$4,620.00"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$5,320.00** — the shares lose −$3,500.00 and the options cost −$1,820.00. Maximum gain is **−$4,620.00**."

### Strategy: S. Call Syn. Strangle (ID=59) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,180.00**"
**Full body**: "Below $92.00, the client still has full downside exposure, but the +$1,180.00 from the options cushions the move. At $85.00, the client's combined position is **+$1,180.00** — the shares lose $0.00 and the options add +$1,180.00. Breakeven is $73.20 (26.8% below spot). There is no cap on downside risk. Without the options, the loss would be $0.00."

**Zone**: bearish
**Check**: LOSS_POSITIVE
**Text**: "loss would be $0.00"
**Full body**: "Below $92.00, the client still has full downside exposure, but the +$1,180.00 from the options cushions the move. At $85.00, the client's combined position is **+$1,180.00** — the shares lose $0.00 and the options add +$1,180.00. Breakeven is $73.20 (26.8% below spot). There is no cap on downside risk. Without the options, the loss would be $0.00."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 13.9% return on the $13,500.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 13.9% return on the $13,500.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $13,500.00"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 13.9% return on the $13,500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,180.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$1,180.00** — the shares gain +$3,000.00 and the options cost −$1,820.00. Breakeven is $126.80 (26.8% above spot). Maximum gain is **+$1,880.00**. That represents a 13.9% return on the $13,500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,880.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$1,180.00** — the shares gain +$3,000.00 and the options cost −$1,820.00. Breakeven is $126.80 (26.8% above spot). Maximum gain is **+$1,880.00**. That represents a 13.9% return on the $13,500.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$1,180.00** — the shares gain +$3,000.00 and the options cost −$1,820.00. Breakeven is $126.80 (26.8% above spot). Maximum gain is **+$1,880.00**. That represents a 13.9% return on the $13,500.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $13,500.00"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$1,180.00** — the shares gain +$3,000.00 and the options cost −$1,820.00. Breakeven is $126.80 (26.8% above spot). Maximum gain is **+$1,880.00**. That represents a 13.9% return on the $13,500.00 capital at risk."

### Strategy: S. Call Syn. Strangle (ID=59) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$4,680.00**"
**Full body**: "Below $92.00, the client still has full downside exposure, but the +$1,180.00 from the options cushions the move. At $85.00, the client's combined position is **+$4,680.00** — the shares gain +$3,500.00 and the options add +$1,180.00. Breakeven is $38.20 (61.8% below spot). There is no cap on downside risk. Without the options, the loss would be +$3,500.00."

**Zone**: bearish
**Check**: LOSS_POSITIVE
**Text**: "loss would be +$3,500.00"
**Full body**: "Below $92.00, the client still has full downside exposure, but the +$1,180.00 from the options cushions the move. At $85.00, the client's combined position is **+$4,680.00** — the shares gain +$3,500.00 and the options add +$1,180.00. Breakeven is $38.20 (61.8% below spot). There is no cap on downside risk. Without the options, the loss would be +$3,500.00."

**Zone**: bearish
**Check**: MISLEADING_DOWNSIDE
**Text**: "full downside exposure (avg_cost=50, spot=100.0)"
**Full body**: "Below $92.00, the client still has full downside exposure, but the +$1,180.00 from the options cushions the move. At $85.00, the client's combined position is **+$4,680.00** — the shares gain +$3,500.00 and the options add +$1,180.00. Breakeven is $38.20 (61.8% below spot). There is no cap on downside risk. Without the options, the loss would be +$3,500.00."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 53.8% return on the $10,000.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 53.8% return on the $10,000.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $10,000.00"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 53.8% return on the $10,000.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$4,680.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$4,680.00** — the shares gain +$6,500.00 and the options cost −$1,820.00. Breakeven is $161.80 (61.8% above spot). Maximum gain is **+$5,380.00**. That represents a 53.8% return on the $10,000.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$5,380.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$4,680.00** — the shares gain +$6,500.00 and the options cost −$1,820.00. Breakeven is $161.80 (61.8% above spot). Maximum gain is **+$5,380.00**. That represents a 53.8% return on the $10,000.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$4,680.00** — the shares gain +$6,500.00 and the options cost −$1,820.00. Breakeven is $161.80 (61.8% above spot). Maximum gain is **+$5,380.00**. That represents a 53.8% return on the $10,000.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $10,000.00"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$4,680.00** — the shares gain +$6,500.00 and the options cost −$1,820.00. Breakeven is $161.80 (61.8% above spot). Maximum gain is **+$5,380.00**. That represents a 53.8% return on the $10,000.00 capital at risk."

### Strategy: S. Call Syn. Strangle (ID=59) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,180.00**"
**Full body**: "At any price below $92.00, gains are locked in at **+$1,180.00**."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $92.00, gains are locked in at **+$1,180.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$380.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **+$380.00**. Breakeven is $103.80 (3.8% above spot). Maximum gain is **+$1,180.00**. That represents a 26.9% return on the $4,380.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,180.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **+$380.00**. Breakeven is $103.80 (3.8% above spot). Maximum gain is **+$1,180.00**. That represents a 26.9% return on the $4,380.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **+$380.00**. Breakeven is $103.80 (3.8% above spot). Maximum gain is **+$1,180.00**. That represents a 26.9% return on the $4,380.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $4,380.00"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **+$380.00**. Breakeven is $103.80 (3.8% above spot). Maximum gain is **+$1,180.00**. That represents a 26.9% return on the $4,380.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,820.00**"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$1,820.00**. Maximum gain is **+$1,180.00**. That represents a 26.9% return on the $4,380.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,180.00**"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$1,820.00**. Maximum gain is **+$1,180.00**. That represents a 26.9% return on the $4,380.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$1,820.00**. Maximum gain is **+$1,180.00**. That represents a 26.9% return on the $4,380.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $4,380.00"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$1,820.00**. Maximum gain is **+$1,180.00**. That represents a 26.9% return on the $4,380.00 capital at risk."

### Strategy: Long Put (ID=6) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$750.00**"
**Full body**: "Below $100.00, the position gains value as the stock falls. At $90.00, the position is **+$750.00**. Breakeven is $97.50 (2.5% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$250.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **−$250.00**. Maximum gain is **+$9,750.00**. That represents significant leverage on the $250.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$9,750.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **−$250.00**. Maximum gain is **+$9,750.00**. That represents significant leverage on the $250.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **−$250.00**. Maximum gain is **+$9,750.00**. That represents significant leverage on the $250.00 capital at risk."

**Zone**: stagnant
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $250"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **−$250.00**. Maximum gain is **+$9,750.00**. That represents significant leverage on the $250.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$250.00**"
**Full body**: "At any price above $100.00, losses are capped at **−$250.00**. That represents significant leverage on the $250.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $100.00, losses are capped at **−$250.00**. That represents significant leverage on the $250.00 capital at risk."

**Zone**: bullish
**Check**: SIGNIFICANT_LEVERAGE
**Text**: "significant leverage on the $250"
**Full body**: "At any price above $100.00, losses are capped at **−$250.00**. That represents significant leverage on the $250.00 capital at risk."

### Strategy: S. Put Syn. Strangle (ID=60) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$320.00**"
**Full body**: "Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$320.00** — the shares gain +$1,500.00 and the options cost −$1,820.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 2.6% return on the $14,380.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 2.6% return on the $14,380.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $14,380.00"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 2.6% return on the $14,380.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$320.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$320.00** — the shares lose −$1,500.00 and the options add +$1,180.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 2.6% return on the $14,380.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$380.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$320.00** — the shares lose −$1,500.00 and the options add +$1,180.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 2.6% return on the $14,380.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$320.00** — the shares lose −$1,500.00 and the options add +$1,180.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 2.6% return on the $14,380.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $14,380.00"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$320.00** — the shares lose −$1,500.00 and the options add +$1,180.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 2.6% return on the $14,380.00 capital at risk."

### Strategy: S. Put Syn. Strangle (ID=60) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,180.00**"
**Full body**: "Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **+$1,180.00** — the shares gain +$3,000.00 and the options cost −$1,820.00. Breakeven is $73.20 (26.8% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents an 11.8% return on the $15,880.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents an 11.8% return on the $15,880.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $15,880.00"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents an 11.8% return on the $15,880.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,180.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$1,180.00** — the shares lose $0.00 and the options add +$1,180.00. Breakeven is $126.80 (26.8% above spot). Maximum gain is **+$1,880.00**. That represents an 11.8% return on the $15,880.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,880.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$1,180.00** — the shares lose $0.00 and the options add +$1,180.00. Breakeven is $126.80 (26.8% above spot). Maximum gain is **+$1,880.00**. That represents an 11.8% return on the $15,880.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$1,180.00** — the shares lose $0.00 and the options add +$1,180.00. Breakeven is $126.80 (26.8% above spot). Maximum gain is **+$1,880.00**. That represents an 11.8% return on the $15,880.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $15,880.00"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$1,180.00** — the shares lose $0.00 and the options add +$1,180.00. Breakeven is $126.80 (26.8% above spot). Maximum gain is **+$1,880.00**. That represents an 11.8% return on the $15,880.00 capital at risk."

### Strategy: S. Put Syn. Strangle (ID=60) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$4,680.00**"
**Full body**: "Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **+$4,680.00** — the shares gain +$6,500.00 and the options cost −$1,820.00. Breakeven is $38.20 (61.8% below spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 27.8% return on the $19,380.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 27.8% return on the $19,380.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $19,380.00"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 27.8% return on the $19,380.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$4,680.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$4,680.00** — the shares gain +$3,500.00 and the options add +$1,180.00. Breakeven is $161.80 (61.8% above spot). Maximum gain is **+$5,380.00**. That represents a 27.8% return on the $19,380.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$5,380.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$4,680.00** — the shares gain +$3,500.00 and the options add +$1,180.00. Breakeven is $161.80 (61.8% above spot). Maximum gain is **+$5,380.00**. That represents a 27.8% return on the $19,380.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$4,680.00** — the shares gain +$3,500.00 and the options add +$1,180.00. Breakeven is $161.80 (61.8% above spot). Maximum gain is **+$5,380.00**. That represents a 27.8% return on the $19,380.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $19,380.00"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **+$4,680.00** — the shares gain +$3,500.00 and the options add +$1,180.00. Breakeven is $161.80 (61.8% above spot). Maximum gain is **+$5,380.00**. That represents a 27.8% return on the $19,380.00 capital at risk."

### Strategy: S. Put Syn. Strangle (ID=60) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,820.00**"
**Full body**: "Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$1,820.00** — the shares gain $0.00 and the options cost −$1,820.00. There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,120.00**"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$1,120.00**. The premium adds a 3.8% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$1,120.00**. The premium adds a 3.8% enhancement over holding the stock alone."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,820.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$1,820.00** — the shares lose −$3,000.00 and the options add +$1,180.00. Maximum gain is **−$1,120.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,120.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$1,820.00** — the shares lose −$3,000.00 and the options add +$1,180.00. Maximum gain is **−$1,120.00**."

**Zone**: bullish
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$1,120.00"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$1,820.00** — the shares lose −$3,000.00 and the options add +$1,180.00. Maximum gain is **−$1,120.00**."

### Strategy: S. Put Syn. Strangle (ID=60) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$5,320.00**"
**Full body**: "Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$5,320.00** — the shares lose −$3,500.00 and the options cost −$1,820.00. There is no cap on downside risk."

**Zone**: bearish
**Check**: MISLEADING_DOWNSIDE
**Text**: "full downside exposure (avg_cost=50, spot=100.0)"
**Full body**: "Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$5,320.00** — the shares lose −$3,500.00 and the options cost −$1,820.00. There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$4,620.00**"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$4,620.00**. The premium adds a 3.8% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "Between $92.00 and $108.00, losses are stable at **−$4,620.00**. The premium adds a 3.8% enhancement over holding the stock alone."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$5,320.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$5,320.00** — the shares lose −$6,500.00 and the options add +$1,180.00. Maximum gain is **−$4,620.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$4,620.00**"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$5,320.00** — the shares lose −$6,500.00 and the options add +$1,180.00. Maximum gain is **−$4,620.00**."

**Zone**: bullish
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$4,620.00"
**Full body**: "Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$5,320.00** — the shares lose −$6,500.00 and the options add +$1,180.00. Maximum gain is **−$4,620.00**."

### Strategy: S. Put Syn. Strangle (ID=60) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,820.00**"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **−$1,820.00**. Maximum loss is **−$18,820.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$18,820.00**"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **−$1,820.00**. Maximum loss is **−$18,820.00**."

**Zone**: bearish
**Check**: DECLINE_RISING
**Text**: "'position declines' but P&L rises (-12800->-120)"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **−$1,820.00**. Maximum loss is **−$18,820.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$380.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **+$380.00**. Breakeven is $96.20 (3.8% below spot). Maximum gain is **+$1,180.00**. That represents a 5.9% return on the $20,000.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,180.00**"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **+$380.00**. Breakeven is $96.20 (3.8% below spot). Maximum gain is **+$1,180.00**. That represents a 5.9% return on the $20,000.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **+$380.00**. Breakeven is $96.20 (3.8% below spot). Maximum gain is **+$1,180.00**. That represents a 5.9% return on the $20,000.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $20,000.00"
**Full body**: "Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **+$380.00**. Breakeven is $96.20 (3.8% below spot). Maximum gain is **+$1,180.00**. That represents a 5.9% return on the $20,000.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,180.00**"
**Full body**: "At any price above $108.00, gains are capped at **+$1,180.00**. That represents a 5.9% return on the $20,000.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, gains are capped at **+$1,180.00**. That represents a 5.9% return on the $20,000.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $20,000.00"
**Full body**: "At any price above $108.00, gains are capped at **+$1,180.00**. That represents a 5.9% return on the $20,000.00 capital at risk."

### Strategy: Syn. Covered Call (ID=61) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$10.00**"
**Full body**: "Below $100.00, the position declines with the stock. At $98.00, the position is **−$10.00**. Breakeven is $98.10 (1.9% below spot). Maximum loss is **−$9,810.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$9,810.00**"
**Full body**: "Below $100.00, the position declines with the stock. At $98.00, the position is **−$10.00**. Breakeven is $98.10 (1.9% below spot). Maximum loss is **−$9,810.00**."

**Zone**: bearish
**Check**: DECLINE_RISING
**Text**: "'position declines' but P&L rises (-6800->-310)"
**Full body**: "Below $100.00, the position declines with the stock. At $98.00, the position is **−$10.00**. Breakeven is $98.10 (1.9% below spot). Maximum loss is **−$9,810.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$190.00**"
**Full body**: "Between $100.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **+$190.00**. Maximum gain is **+$990.00**. That represents a 9.2% return on the $10,800.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$990.00**"
**Full body**: "Between $100.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **+$190.00**. Maximum gain is **+$990.00**. That represents a 9.2% return on the $10,800.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $100.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **+$190.00**. Maximum gain is **+$990.00**. That represents a 9.2% return on the $10,800.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $10,800.00"
**Full body**: "Between $100.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **+$190.00**. Maximum gain is **+$990.00**. That represents a 9.2% return on the $10,800.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$990.00**"
**Full body**: "At any price above $108.00, gains are capped at **+$990.00**. That represents a 9.2% return on the $10,800.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, gains are capped at **+$990.00**. That represents a 9.2% return on the $10,800.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $10,800.00"
**Full body**: "At any price above $108.00, gains are capped at **+$990.00**. That represents a 9.2% return on the $10,800.00 capital at risk."

### Strategy: Syn. Covered Put (ID=62) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$990.00**"
**Full body**: "At any price below $92.00, gains are locked in at **+$990.00**."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $92.00, gains are locked in at **+$990.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$190.00**"
**Full body**: "Between $92.00 and $100.00, the position gains value as the stock moves lower. At $100.00, the position is **+$190.00**. Maximum gain is **+$990.00**. That represents a 33.1% return on the $2,990.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$990.00**"
**Full body**: "Between $92.00 and $100.00, the position gains value as the stock moves lower. At $100.00, the position is **+$190.00**. Maximum gain is **+$990.00**. That represents a 33.1% return on the $2,990.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Between $92.00 and $100.00, the position gains value as the stock moves lower. At $100.00, the position is **+$190.00**. Maximum gain is **+$990.00**. That represents a 33.1% return on the $2,990.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,990.00"
**Full body**: "Between $92.00 and $100.00, the position gains value as the stock moves lower. At $100.00, the position is **+$190.00**. Maximum gain is **+$990.00**. That represents a 33.1% return on the $2,990.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$10.00**"
**Full body**: "Above $100.00, losses increase as the stock rises. At $102.00, the position is **−$10.00**. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$990.00**. That represents a 33.1% return on the $2,990.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$990.00**"
**Full body**: "Above $100.00, losses increase as the stock rises. At $102.00, the position is **−$10.00**. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$990.00**. That represents a 33.1% return on the $2,990.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, losses increase as the stock rises. At $102.00, the position is **−$10.00**. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$990.00**. That represents a 33.1% return on the $2,990.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,990.00"
**Full body**: "Above $100.00, losses increase as the stock rises. At $102.00, the position is **−$10.00**. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$990.00**. That represents a 33.1% return on the $2,990.00 capital at risk."

### Strategy: Conversion (ID=63) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Below $100.00, but the long $100.00 put provides a hard floor. Maximum loss is **$0.00** at any price below $300.00. Breakevens are $99.33 (0.7% below spot) and $100.00 (0.0% above spot) (among multiple breakevens). The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **$0.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **$0.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Above $100.00, the short $100.00 call drives losses. Maximum loss is **$0.00** at any price above $0.00. Breakevens are $100.00 (0.0% above spot) and $100.33 (0.3% above spot) (among multiple breakevens). The trade-off: downside protection below $100.00 in exchange for capping gains above $100.00."

### Strategy: Conversion (ID=63) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,500.00**"
**Full body**: "Below $100.00, but the long $100.00 put provides a hard floor. Maximum loss is **−$1,500.00** at any price below $300.00."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,500.00**"
**Full body**: "Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Maximum gain is **−$1,500.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,500.00**"
**Full body**: "Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Maximum gain is **−$1,500.00**."

**Zone**: stagnant
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$1,500.00"
**Full body**: "Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Maximum gain is **−$1,500.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,500.00**"
**Full body**: "Above $100.00, the short $100.00 call drives losses. Maximum loss is **−$1,500.00** at any price above $0.00. The trade-off: downside protection below $100.00 in exchange for capping gains above $100.00."

### Strategy: Conversion (ID=63) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$5,000.00**"
**Full body**: "Below $100.00, but the long $100.00 put provides a hard floor. Maximum loss is **−$5,000.00** at any price below $300.00."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$5,000.00**"
**Full body**: "Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **−$5,000.00** — the shares lose −$5,000.00 and the options add $0.00."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$5,000.00**"
**Full body**: "Above $100.00, the short $100.00 call drives losses. Maximum loss is **−$5,000.00** at any price above $0.00. The trade-off: downside protection below $100.00 in exchange for capping gains above $100.00."

### Strategy: Conversion (ID=63) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,500.00**"
**Full body**: "Below $100.00, but the long $100.00 put provides a hard floor. Maximum loss is **+$1,500.00** at any price below $300.00. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: bearish
**Check**: LOSS_POSITIVE
**Text**: "loss is **+$1,500.00"
**Full body**: "Below $100.00, but the long $100.00 put provides a hard floor. Maximum loss is **+$1,500.00** at any price below $300.00. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,500.00**"
**Full body**: "Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Maximum gain is **+$1,500.00**. That represents a 10.9% return on the $13,750.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,500.00**"
**Full body**: "Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Maximum gain is **+$1,500.00**. That represents a 10.9% return on the $13,750.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Maximum gain is **+$1,500.00**. That represents a 10.9% return on the $13,750.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $13,750.00"
**Full body**: "Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Maximum gain is **+$1,500.00**. That represents a 10.9% return on the $13,750.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,500.00**"
**Full body**: "Above $100.00, the short $100.00 call drives losses. Maximum loss is **+$1,500.00** at any price above $0.00. The trade-off: downside protection below $100.00 in exchange for capping gains above $100.00. That represents a 10.9% return on the $13,750.00 capital at risk."

**Zone**: bullish
**Check**: LOSS_POSITIVE
**Text**: "loss is **+$1,500.00"
**Full body**: "Above $100.00, the short $100.00 call drives losses. Maximum loss is **+$1,500.00** at any price above $0.00. The trade-off: downside protection below $100.00 in exchange for capping gains above $100.00. That represents a 10.9% return on the $13,750.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, the short $100.00 call drives losses. Maximum loss is **+$1,500.00** at any price above $0.00. The trade-off: downside protection below $100.00 in exchange for capping gains above $100.00. That represents a 10.9% return on the $13,750.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $13,750.00"
**Full body**: "Above $100.00, the short $100.00 call drives losses. Maximum loss is **+$1,500.00** at any price above $0.00. The trade-off: downside protection below $100.00 in exchange for capping gains above $100.00. That represents a 10.9% return on the $13,750.00 capital at risk."

### Strategy: Conversion (ID=63) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$5,000.00**"
**Full body**: "Below $100.00, but the long $100.00 put provides a hard floor. Maximum loss is **+$5,000.00** at any price below $300.00. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: bearish
**Check**: LOSS_POSITIVE
**Text**: "loss is **+$5,000.00"
**Full body**: "Below $100.00, but the long $100.00 put provides a hard floor. Maximum loss is **+$5,000.00** at any price below $300.00. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,000.00**"
**Full body**: "Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **+$5,000.00** — the shares gain +$5,000.00 and the options add $0.00. Maximum gain is **+$5,000.00**. That represents a 48.8% return on the $10,250.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,000.00**"
**Full body**: "Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **+$5,000.00** — the shares gain +$5,000.00 and the options add $0.00. Maximum gain is **+$5,000.00**. That represents a 48.8% return on the $10,250.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **+$5,000.00** — the shares gain +$5,000.00 and the options add $0.00. Maximum gain is **+$5,000.00**. That represents a 48.8% return on the $10,250.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $10,250.00"
**Full body**: "Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **+$5,000.00** — the shares gain +$5,000.00 and the options add $0.00. Maximum gain is **+$5,000.00**. That represents a 48.8% return on the $10,250.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$5,000.00**"
**Full body**: "Above $100.00, the short $100.00 call drives losses. Maximum loss is **+$5,000.00** at any price above $0.00. The trade-off: downside protection below $100.00 in exchange for capping gains above $100.00. That represents a 48.8% return on the $10,250.00 capital at risk."

**Zone**: bullish
**Check**: LOSS_POSITIVE
**Text**: "loss is **+$5,000.00"
**Full body**: "Above $100.00, the short $100.00 call drives losses. Maximum loss is **+$5,000.00** at any price above $0.00. The trade-off: downside protection below $100.00 in exchange for capping gains above $100.00. That represents a 48.8% return on the $10,250.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, the short $100.00 call drives losses. Maximum loss is **+$5,000.00** at any price above $0.00. The trade-off: downside protection below $100.00 in exchange for capping gains above $100.00. That represents a 48.8% return on the $10,250.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $10,250.00"
**Full body**: "Above $100.00, the short $100.00 call drives losses. Maximum loss is **+$5,000.00** at any price above $0.00. The trade-off: downside protection below $100.00 in exchange for capping gains above $100.00. That represents a 48.8% return on the $10,250.00 capital at risk."

### Strategy: Conversion (ID=63) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,000.00**"
**Full body**: "Below $100.00, the position gains value as the stock falls. At $90.00, the position is **+$1,000.00**. Breakeven is $100.00 (0.0% above spot). There is no cap on downside risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**$0.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$10,000.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,250.00"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,000.00**"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$1,000.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$10,000.00**"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$1,000.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$1,000.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $2,250.00"
**Full body**: "Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$1,000.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk."

### Strategy: Short Put (ID=7) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$750.00**"
**Full body**: "Below $100.00, the position declines with the stock. At $90.00, the position is **−$750.00**. Breakeven is $97.50 (2.5% below spot). Maximum loss is **−$9,750.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$9,750.00**"
**Full body**: "Below $100.00, the position declines with the stock. At $90.00, the position is **−$750.00**. Breakeven is $97.50 (2.5% below spot). Maximum loss is **−$9,750.00**."

**Zone**: bearish
**Check**: DECLINE_RISING
**Text**: "'position declines' but P&L rises (-6740->-250)"
**Full body**: "Below $100.00, the position declines with the stock. At $90.00, the position is **−$750.00**. Breakeven is $97.50 (2.5% below spot). Maximum loss is **−$9,750.00**."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$250.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$250.00**. Maximum gain is **+$250.00**. That represents a 2.5% return on the $10,000.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$250.00**"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$250.00**. Maximum gain is **+$250.00**. That represents a 2.5% return on the $10,000.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$250.00**. Maximum gain is **+$250.00**. That represents a 2.5% return on the $10,000.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $10,000.00"
**Full body**: "Near $100.00, the position is roughly flat. At $100.00, the position is **+$250.00**. Maximum gain is **+$250.00**. That represents a 2.5% return on the $10,000.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$250.00**"
**Full body**: "At any price above $100.00, gains are capped at **+$250.00**. That represents a 2.5% return on the $10,000.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $100.00, gains are capped at **+$250.00**. That represents a 2.5% return on the $10,000.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $10,000.00"
**Full body**: "At any price above $100.00, gains are capped at **+$250.00**. That represents a 2.5% return on the $10,000.00 capital at risk."

### Strategy: Covered Call (ID=8) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$10.00**"
**Full body**: "Below $100.00, the client still has full downside exposure, but the +$190.00 from the options cushions the move. At $98.00, the client's combined position is **−$10.00** — the shares lose −$200.00 and the options add +$190.00. Breakeven is $98.10 (1.9% below spot). There is no cap on downside risk. Without the options, the loss would be −$200.00."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$190.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$190.00** — the shares gain $0.00 and the options add +$190.00. Maximum gain is **+$990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 6.6% return on the $15,000.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$990.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$190.00** — the shares gain $0.00 and the options add +$190.00. Maximum gain is **+$990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 6.6% return on the $15,000.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$190.00** — the shares gain $0.00 and the options add +$190.00. Maximum gain is **+$990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 6.6% return on the $15,000.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$190.00** — the shares gain $0.00 and the options add +$190.00. Maximum gain is **+$990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 6.6% return on the $15,000.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $15,000.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$190.00** — the shares gain $0.00 and the options add +$190.00. Maximum gain is **+$990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 6.6% return on the $15,000.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$990.00**"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$990.00** — the short call limits further upside. The trade-off: $190.00 in collected premium in exchange for giving up gains above $108.00. That represents a 6.6% return on the $15,000.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$990.00** — the short call limits further upside. The trade-off: $190.00 in collected premium in exchange for giving up gains above $108.00. That represents a 6.6% return on the $15,000.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $15,000.00"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$990.00** — the short call limits further upside. The trade-off: $190.00 in collected premium in exchange for giving up gains above $108.00. That represents a 6.6% return on the $15,000.00 capital at risk."

### Strategy: Covered Call (ID=8) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$1,510.00**"
**Full body**: "Below $100.00, the client still has full downside exposure, but the +$190.00 from the options cushions the move. At $98.00, the client's combined position is **−$1,510.00** — the shares lose −$1,700.00 and the options add +$190.00. There is no cap on downside risk. Without the options, the loss would be −$1,700.00."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,310.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,310.00** — the shares lose −$1,500.00 and the options add +$190.00. Maximum gain is **−$510.00**. The premium adds a 1.9% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$510.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,310.00** — the shares lose −$1,500.00 and the options add +$190.00. Maximum gain is **−$510.00**. The premium adds a 1.9% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$510.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,310.00** — the shares lose −$1,500.00 and the options add +$190.00. Maximum gain is **−$510.00**. The premium adds a 1.9% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,310.00** — the shares lose −$1,500.00 and the options add +$190.00. Maximum gain is **−$510.00**. The premium adds a 1.9% enhancement over holding the stock alone."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$510.00**"
**Full body**: "At any price above $108.00, the client's losses are capped at **−$510.00**. The trade-off: $190.00 in collected premium in exchange for giving up gains above $108.00."

### Strategy: Covered Call (ID=8) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$5,010.00**"
**Full body**: "Below $100.00, the client still has full downside exposure, but the +$190.00 from the options cushions the move. At $98.00, the client's combined position is **−$5,010.00** — the shares lose −$5,200.00 and the options add +$190.00. There is no cap on downside risk. Without the options, the loss would be −$5,200.00."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$4,810.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,810.00** — the shares lose −$5,000.00 and the options add +$190.00. Maximum gain is **−$4,010.00**. The premium adds a 1.9% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$4,010.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,810.00** — the shares lose −$5,000.00 and the options add +$190.00. Maximum gain is **−$4,010.00**. The premium adds a 1.9% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$4,010.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,810.00** — the shares lose −$5,000.00 and the options add +$190.00. Maximum gain is **−$4,010.00**. The premium adds a 1.9% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,810.00** — the shares lose −$5,000.00 and the options add +$190.00. Maximum gain is **−$4,010.00**. The premium adds a 1.9% enhancement over holding the stock alone."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$4,010.00**"
**Full body**: "At any price above $108.00, the client's losses are capped at **−$4,010.00**. The trade-off: $190.00 in collected premium in exchange for giving up gains above $108.00."

### Strategy: Covered Call (ID=8) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$1,490.00**"
**Full body**: "Below $100.00, the client still has full downside exposure, but the +$190.00 from the options cushions the move. At $98.00, the client's combined position is **+$1,490.00** — the shares gain +$1,300.00 and the options add +$190.00. Breakeven is $83.10 (16.9% below spot). There is no cap on downside risk. Without the options, the loss would be +$1,300.00."

**Zone**: bearish
**Check**: LOSS_POSITIVE
**Text**: "loss would be +$1,300.00"
**Full body**: "Below $100.00, the client still has full downside exposure, but the +$190.00 from the options cushions the move. At $98.00, the client's combined position is **+$1,490.00** — the shares gain +$1,300.00 and the options add +$190.00. Breakeven is $83.10 (16.9% below spot). There is no cap on downside risk. Without the options, the loss would be +$1,300.00."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,690.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$1,690.00** — the shares gain +$1,500.00 and the options add +$190.00. Maximum gain is **+$2,490.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents an 18.4% return on the $13,500.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$2,490.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$1,690.00** — the shares gain +$1,500.00 and the options add +$190.00. Maximum gain is **+$2,490.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents an 18.4% return on the $13,500.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$1,690.00** — the shares gain +$1,500.00 and the options add +$190.00. Maximum gain is **+$2,490.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents an 18.4% return on the $13,500.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$1,690.00** — the shares gain +$1,500.00 and the options add +$190.00. Maximum gain is **+$2,490.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents an 18.4% return on the $13,500.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $13,500.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$1,690.00** — the shares gain +$1,500.00 and the options add +$190.00. Maximum gain is **+$2,490.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents an 18.4% return on the $13,500.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$2,490.00**"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$2,490.00** — the short call limits further upside. The trade-off: $190.00 in collected premium in exchange for giving up gains above $108.00. That represents an 18.4% return on the $13,500.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$2,490.00** — the short call limits further upside. The trade-off: $190.00 in collected premium in exchange for giving up gains above $108.00. That represents an 18.4% return on the $13,500.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $13,500.00"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$2,490.00** — the short call limits further upside. The trade-off: $190.00 in collected premium in exchange for giving up gains above $108.00. That represents an 18.4% return on the $13,500.00 capital at risk."

### Strategy: Covered Call (ID=8) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$4,990.00**"
**Full body**: "Below $100.00, the client still has full downside exposure, but the +$190.00 from the options cushions the move. At $98.00, the client's combined position is **+$4,990.00** — the shares gain +$4,800.00 and the options add +$190.00. Breakeven is $48.10 (51.9% below spot). There is no cap on downside risk. Without the options, the loss would be +$4,800.00."

**Zone**: bearish
**Check**: LOSS_POSITIVE
**Text**: "loss would be +$4,800.00"
**Full body**: "Below $100.00, the client still has full downside exposure, but the +$190.00 from the options cushions the move. At $98.00, the client's combined position is **+$4,990.00** — the shares gain +$4,800.00 and the options add +$190.00. Breakeven is $48.10 (51.9% below spot). There is no cap on downside risk. Without the options, the loss would be +$4,800.00."

**Zone**: bearish
**Check**: MISLEADING_DOWNSIDE
**Text**: "full downside exposure (avg_cost=50, spot=100.0)"
**Full body**: "Below $100.00, the client still has full downside exposure, but the +$190.00 from the options cushions the move. At $98.00, the client's combined position is **+$4,990.00** — the shares gain +$4,800.00 and the options add +$190.00. Breakeven is $48.10 (51.9% below spot). There is no cap on downside risk. Without the options, the loss would be +$4,800.00."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,190.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,190.00** — the shares gain +$5,000.00 and the options add +$190.00. Maximum gain is **+$5,990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 59.9% return on the $10,000.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,990.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,190.00** — the shares gain +$5,000.00 and the options add +$190.00. Maximum gain is **+$5,990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 59.9% return on the $10,000.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,190.00** — the shares gain +$5,000.00 and the options add +$190.00. Maximum gain is **+$5,990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 59.9% return on the $10,000.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,190.00** — the shares gain +$5,000.00 and the options add +$190.00. Maximum gain is **+$5,990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 59.9% return on the $10,000.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $10,000.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,190.00** — the shares gain +$5,000.00 and the options add +$190.00. Maximum gain is **+$5,990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 59.9% return on the $10,000.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$5,990.00**"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$5,990.00** — the short call limits further upside. The trade-off: $190.00 in collected premium in exchange for giving up gains above $108.00. That represents a 59.9% return on the $10,000.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$5,990.00** — the short call limits further upside. The trade-off: $190.00 in collected premium in exchange for giving up gains above $108.00. That represents a 59.9% return on the $10,000.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $10,000.00"
**Full body**: "At any price above $108.00, the client's gains are capped at **+$5,990.00** — the short call limits further upside. The trade-off: $190.00 in collected premium in exchange for giving up gains above $108.00. That represents a 59.9% return on the $10,000.00 capital at risk."

### Strategy: Covered Call (ID=8) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$190.00**"
**Full body**: "Below $100.00. Maximum loss is **+$190.00** at any price below $108.00."

**Zone**: bearish
**Check**: LOSS_POSITIVE
**Text**: "loss is **+$190.00"
**Full body**: "Below $100.00. Maximum loss is **+$190.00** at any price below $108.00."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the target outcome. As long as the stock stays between $100.00 and $108.00 — roughly 0.0% up to 8.0% up from here — all options expire worthless and the full $190.00 credit is retained. That represents a 13.7% return on the $1,390.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $1,390.00"
**Full body**: "This is the target outcome. As long as the stock stays between $100.00 and $108.00 — roughly 0.0% up to 8.0% up from here — all options expire worthless and the full $190.00 credit is retained. That represents a 13.7% return on the $1,390.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$510.00**"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$510.00**. Breakeven is $109.90 (9.9% above spot). Maximum gain is **+$190.00**. That represents a 13.7% return on the $1,390.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$190.00**"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$510.00**. Breakeven is $109.90 (9.9% above spot). Maximum gain is **+$190.00**. That represents a 13.7% return on the $1,390.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$510.00**. Breakeven is $109.90 (9.9% above spot). Maximum gain is **+$190.00**. That represents a 13.7% return on the $1,390.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $1,390.00"
**Full body**: "Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$510.00**. Breakeven is $109.90 (9.9% above spot). Maximum gain is **+$190.00**. That represents a 13.7% return on the $1,390.00 capital at risk."

### Strategy: Covered Put (ID=9) -- Cost Basis: Cost Basis = Spot

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$990.00**"
**Full body**: "At any price below $92.00, the client's gains are locked in at **+$990.00**. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $92.00, the client's gains are locked in at **+$990.00**. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$190.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$190.00** — the shares gain $0.00 and the options add +$190.00. Maximum gain is **+$990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents an 8.7% return on the $11,390.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$990.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$190.00** — the shares gain $0.00 and the options add +$190.00. Maximum gain is **+$990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents an 8.7% return on the $11,390.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$190.00** — the shares gain $0.00 and the options add +$190.00. Maximum gain is **+$990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents an 8.7% return on the $11,390.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$190.00** — the shares gain $0.00 and the options add +$190.00. Maximum gain is **+$990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents an 8.7% return on the $11,390.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $11,390.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$190.00** — the shares gain $0.00 and the options add +$190.00. Maximum gain is **+$990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents an 8.7% return on the $11,390.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$10.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **−$10.00** — the shares lose −$200.00 and the options add +$190.00. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$990.00**. That represents an 8.7% return on the $11,390.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$990.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **−$10.00** — the shares lose −$200.00 and the options add +$190.00. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$990.00**. That represents an 8.7% return on the $11,390.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **−$10.00** — the shares lose −$200.00 and the options add +$190.00. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$990.00**. That represents an 8.7% return on the $11,390.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $11,390.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **−$10.00** — the shares lose −$200.00 and the options add +$190.00. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$990.00**. That represents an 8.7% return on the $11,390.00 capital at risk."

### Strategy: Covered Put (ID=9) -- Cost Basis: Cost Basis at 115%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$2,490.00**"
**Full body**: "At any price below $92.00, the client's gains are locked in at **+$2,490.00**. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $92.00, the client's gains are locked in at **+$2,490.00**. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$1,690.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$1,690.00** — the shares gain +$1,500.00 and the options add +$190.00. Maximum gain is **+$2,490.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 19.3% return on the $12,890.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$2,490.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$1,690.00** — the shares gain +$1,500.00 and the options add +$190.00. Maximum gain is **+$2,490.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 19.3% return on the $12,890.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$1,690.00** — the shares gain +$1,500.00 and the options add +$190.00. Maximum gain is **+$2,490.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 19.3% return on the $12,890.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$1,690.00** — the shares gain +$1,500.00 and the options add +$190.00. Maximum gain is **+$2,490.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 19.3% return on the $12,890.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $12,890.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$1,690.00** — the shares gain +$1,500.00 and the options add +$190.00. Maximum gain is **+$2,490.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 19.3% return on the $12,890.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$1,490.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **+$1,490.00** — the shares gain +$1,300.00 and the options add +$190.00. Breakeven is $116.90 (16.9% above spot). Maximum gain is **+$2,490.00**. That represents a 19.3% return on the $12,890.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$2,490.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **+$1,490.00** — the shares gain +$1,300.00 and the options add +$190.00. Breakeven is $116.90 (16.9% above spot). Maximum gain is **+$2,490.00**. That represents a 19.3% return on the $12,890.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **+$1,490.00** — the shares gain +$1,300.00 and the options add +$190.00. Breakeven is $116.90 (16.9% above spot). Maximum gain is **+$2,490.00**. That represents a 19.3% return on the $12,890.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $12,890.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **+$1,490.00** — the shares gain +$1,300.00 and the options add +$190.00. Breakeven is $116.90 (16.9% above spot). Maximum gain is **+$2,490.00**. That represents a 19.3% return on the $12,890.00 capital at risk."

### Strategy: Covered Put (ID=9) -- Cost Basis: Cost Basis at 150%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**+$5,990.00**"
**Full body**: "At any price below $92.00, the client's gains are locked in at **+$5,990.00**. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: bearish
**Check**: LOCKED_IN
**Text**: "gains are locked in at"
**Full body**: "At any price below $92.00, the client's gains are locked in at **+$5,990.00**. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,190.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,190.00** — the shares gain +$5,000.00 and the options add +$190.00. Maximum gain is **+$5,990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 36.5% return on the $16,390.00 capital at risk."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**+$5,990.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,190.00** — the shares gain +$5,000.00 and the options add +$190.00. Maximum gain is **+$5,990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 36.5% return on the $16,390.00 capital at risk."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,190.00** — the shares gain +$5,000.00 and the options add +$190.00. Maximum gain is **+$5,990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 36.5% return on the $16,390.00 capital at risk."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,190.00** — the shares gain +$5,000.00 and the options add +$190.00. Maximum gain is **+$5,990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 36.5% return on the $16,390.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $16,390.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$5,190.00** — the shares gain +$5,000.00 and the options add +$190.00. Maximum gain is **+$5,990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 36.5% return on the $16,390.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$4,990.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **+$4,990.00** — the shares gain +$4,800.00 and the options add +$190.00. Breakeven is $151.90 (51.9% above spot). Maximum gain is **+$5,990.00**. That represents a 36.5% return on the $16,390.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$5,990.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **+$4,990.00** — the shares gain +$4,800.00 and the options add +$190.00. Breakeven is $151.90 (51.9% above spot). Maximum gain is **+$5,990.00**. That represents a 36.5% return on the $16,390.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **+$4,990.00** — the shares gain +$4,800.00 and the options add +$190.00. Breakeven is $151.90 (51.9% above spot). Maximum gain is **+$5,990.00**. That represents a 36.5% return on the $16,390.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $16,390.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **+$4,990.00** — the shares gain +$4,800.00 and the options add +$190.00. Breakeven is $151.90 (51.9% above spot). Maximum gain is **+$5,990.00**. That represents a 36.5% return on the $16,390.00 capital at risk."

### Strategy: Covered Put (ID=9) -- Cost Basis: Cost Basis at 85%

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$510.00**"
**Full body**: "At any price below $92.00, the client's losses are capped at **−$510.00**. Without the options, the loss would be −$700.00."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$1,310.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,310.00** — the shares lose −$1,500.00 and the options add +$190.00. Maximum gain is **−$510.00**. The premium adds a 1.9% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$510.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,310.00** — the shares lose −$1,500.00 and the options add +$190.00. Maximum gain is **−$510.00**. The premium adds a 1.9% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$510.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,310.00** — the shares lose −$1,500.00 and the options add +$190.00. Maximum gain is **−$510.00**. The premium adds a 1.9% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **−$1,310.00** — the shares lose −$1,500.00 and the options add +$190.00. Maximum gain is **−$510.00**. The premium adds a 1.9% enhancement over holding the stock alone."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$1,510.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **−$1,510.00** — the shares lose −$1,700.00 and the options add +$190.00. Maximum gain is **−$510.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$510.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **−$1,510.00** — the shares lose −$1,700.00 and the options add +$190.00. Maximum gain is **−$510.00**."

**Zone**: bullish
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$510.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **−$1,510.00** — the shares lose −$1,700.00 and the options add +$190.00. Maximum gain is **−$510.00**."

### Strategy: Covered Put (ID=9) -- Cost Basis: Cost Basis far below

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$4,010.00**"
**Full body**: "At any price below $92.00, the client's losses are capped at **−$4,010.00**. Without the options, the loss would be −$4,200.00."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$4,810.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,810.00** — the shares lose −$5,000.00 and the options add +$190.00. Maximum gain is **−$4,010.00**. The premium adds a 1.9% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: MD_BOLD
**Text**: "**−$4,010.00**"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,810.00** — the shares lose −$5,000.00 and the options add +$190.00. Maximum gain is **−$4,010.00**. The premium adds a 1.9% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$4,010.00"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,810.00** — the shares lose −$5,000.00 and the options add +$190.00. Maximum gain is **−$4,010.00**. The premium adds a 1.9% enhancement over holding the stock alone."

**Zone**: stagnant
**Check**: ENHANCEMENT
**Text**: "enhancement over holding the stock alone"
**Full body**: "This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **−$4,810.00** — the shares lose −$5,000.00 and the options add +$190.00. Maximum gain is **−$4,010.00**. The premium adds a 1.9% enhancement over holding the stock alone."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$5,010.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **−$5,010.00** — the shares lose −$5,200.00 and the options add +$190.00. Maximum gain is **−$4,010.00**."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**−$4,010.00**"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **−$5,010.00** — the shares lose −$5,200.00 and the options add +$190.00. Maximum gain is **−$4,010.00**."

**Zone**: bullish
**Check**: GAIN_NEGATIVE
**Text**: "gain is **−$4,010.00"
**Full body**: "Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **−$5,010.00** — the shares lose −$5,200.00 and the options add +$190.00. Maximum gain is **−$4,010.00**."

### Strategy: Covered Put (ID=9) -- Cost Basis: Options Only

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$510.00**"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **−$510.00**. Breakeven is $90.10 (9.9% below spot). Maximum loss is **−$9,010.00**."

**Zone**: bearish
**Check**: MD_BOLD
**Text**: "**−$9,010.00**"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **−$510.00**. Breakeven is $90.10 (9.9% below spot). Maximum loss is **−$9,010.00**."

**Zone**: bearish
**Check**: DECLINE_RISING
**Text**: "'position declines' but P&L rises (-6000->190)"
**Full body**: "Below $92.00, the position declines with the stock. At $85.00, the position is **−$510.00**. Breakeven is $90.10 (9.9% below spot). Maximum loss is **−$9,010.00**."

**Zone**: stagnant
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $100.00 — roughly 8.0% down to 0.0% down from here — all options expire worthless and the full $190.00 credit is retained. That represents a 2.1% return on the $9,200.00 capital at risk."

**Zone**: stagnant
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $9,200.00"
**Full body**: "This is the target outcome. As long as the stock stays between $92.00 and $100.00 — roughly 8.0% down to 0.0% down from here — all options expire worthless and the full $190.00 credit is retained. That represents a 2.1% return on the $9,200.00 capital at risk."

**Zone**: bullish
**Check**: MD_BOLD
**Text**: "**+$190.00**"
**Full body**: "Above $100.00. Maximum loss is **+$190.00** at any price above $92.00. That represents a 2.1% return on the $9,200.00 capital at risk."

**Zone**: bullish
**Check**: LOSS_POSITIVE
**Text**: "loss is **+$190.00"
**Full body**: "Above $100.00. Maximum loss is **+$190.00** at any price above $92.00. That represents a 2.1% return on the $9,200.00 capital at risk."

**Zone**: bullish
**Check**: CAPITAL_AT_RISK
**Text**: "capital at risk"
**Full body**: "Above $100.00. Maximum loss is **+$190.00** at any price above $92.00. That represents a 2.1% return on the $9,200.00 capital at risk."

**Zone**: bullish
**Check**: RETURN_ON_CAPITAL
**Text**: "return on the $9,200.00"
**Full body**: "Above $100.00. Maximum loss is **+$190.00** at any price above $92.00. That represents a 2.1% return on the $9,200.00 capital at risk."

