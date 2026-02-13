# Commentary V2 Regression Report

Generated: 2026-02-13

## Summary

- **Total strategies in CSV**: 63
- **Total runs** (options-only + with-stock): 126
- **Errors**: 1
- **Average body length**: 204 chars
- **Bodies mentioning losses** (−$): 199
- **Bodies mentioning 'the client'**: 226
- **Bodies with '--' placeholders**: 0
- **Empty bodies**: 0

### Errors

- **Custom Strategy** (ID=1, variant=options_only): `No legs and no stock position`

---

## Per-Strategy Results

## Strategy: Custom Strategy (ID=1, Code=LNG)

### Options Only

**ERROR**: `No legs and no stock position`

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is −$1,500.00 — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum loss is −$10,000.00.

**Stagnant**: If the stock stays between $97.00 and $103.00
Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is $0.00 — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $115.00, the client's combined position is +$1,500.00 — the shares gain +$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). There is no cap on upside gains.

---

## Strategy: Long Stock (ID=2, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is −$1,500.00 — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum loss is −$10,000.00.

**Stagnant**: If the stock stays between $97.00 and $103.00
Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is $0.00 — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $115.00, the client's combined position is +$1,500.00 — the shares gain +$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is −$1,500.00 — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum loss is −$10,000.00.

**Stagnant**: If the stock stays between $97.00 and $103.00
Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is $0.00 — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $115.00, the client's combined position is +$1,500.00 — the shares gain +$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). There is no cap on upside gains.

---

## Strategy: Short Stock (ID=3, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is +$1,500.00 — the shares gain +$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $97.00 and $103.00
Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is $0.00 — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is +$10,000.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is −$1,500.00 — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is +$10,000.00.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is +$1,500.00 — the shares gain +$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $97.00 and $103.00
Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is $0.00 — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is +$10,000.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is −$1,500.00 — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is +$10,000.00.

---

## Strategy: Long Call (ID=4, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
At any price below $100.00, losses are capped at −$250.00.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is −$250.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the position rises with the stock. At $110.00, the position is +$750.00. Breakeven is $102.50 (2.5% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is −$1,250.00 — the shares lose −$1,000.00 and the options cost −$250.00. Maximum loss is −$10,250.00.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $250.00 option cost. At $100.00, the client's combined position is −$250.00 — the shares gain $0.00 and the options cost −$250.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is +$1,750.00 — the shares gain +$1,000.00 and the options add +$750.00. Breakeven is $101.25 (1.2% above spot). There is no cap on upside gains.

---

## Strategy: Short Call (ID=5, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $100.00
At any price below $100.00, the position achieves its maximum gain of +$250.00.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is +$250.00. Maximum gain is +$250.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, losses increase as the stock rises. At $110.00, the position is −$750.00. Breakeven is $102.50 (2.5% above spot). Maximum gain is +$250.00.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure, but the +$250.00 from the options cushions the move. At $90.00, the client's combined position is −$750.00 — the shares lose −$1,000.00 and the options add +$250.00. Breakeven is $97.50 (2.5% below spot). Maximum loss is −$9,750.00. Without the options, the loss would be −$1,000.00.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $250.00 in premium on top of share movement. At $100.00, the client's combined position is +$250.00 — the shares gain $0.00 and the options add +$250.00. Maximum gain is +$250.00.

**Bullish**: If the stock rises above $100.00
At any price above $100.00, the client's gains are capped at +$250.00 — the short call limits further upside. The trade-off: $250.00 in collected premium in exchange for giving up gains above $100.00.

---

## Strategy: Long Put (ID=6, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position gains value as the stock falls. At $90.00, the position is +$750.00. Breakeven is $97.50 (2.5% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is −$250.00. Maximum gain is +$9,750.00.

**Bullish**: If the stock rises above $100.00
At any price above $100.00, losses are capped at −$250.00.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
At any price below $100.00, the client's losses are capped at −$250.00 — the long $100.00 put provides a hard floor.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $250.00 option cost. At $100.00, the client's combined position is −$250.00 — the shares gain $0.00 and the options cost −$250.00. The cost of protection: $250.00 (2.5% of the position) for a guaranteed loss limit at $100.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is +$750.00 — the shares gain +$1,000.00 and the options cost −$250.00. Breakeven is $102.50 (2.5% above spot). There is no cap on upside gains.

---

## Strategy: Short Put (ID=7, Code=CSPT)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position loses value as the stock falls. At $90.00, the position is −$750.00. Breakeven is $97.50 (2.5% below spot). Maximum loss is −$9,750.00.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is +$250.00. Maximum gain is +$250.00.

**Bullish**: If the stock rises above $100.00
At any price above $100.00, gains are capped at +$250.00.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is −$1,750.00 — the shares lose −$1,000.00 and the options cost −$750.00. Breakeven is $98.75 (1.2% below spot). Maximum loss is −$19,750.00.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $250.00 in premium on top of share movement. At $100.00, the client's combined position is +$250.00 — the shares gain $0.00 and the options add +$250.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is +$1,250.00 — the shares gain +$1,000.00 and the options add +$250.00. There is no cap on upside gains.

---

## Strategy: Covered Call (ID=8, Code=CCOV)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure, but the +$190.00 from the options cushions the move. At $98.00, the client's combined position is −$10.00 — the shares lose −$200.00 and the options add +$190.00. Breakeven is $98.10 (1.9% below spot). There is no cap on downside risk. Without the options, the loss would be −$200.00.

**Stagnant**: If the stock stays between $100.00 and $108.00
This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is +$190.00 — the shares gain $0.00 and the options add +$190.00. Maximum gain is +$990.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at +$990.00 — the short call limits further upside. The trade-off: $190.00 in collected premium in exchange for giving up gains above $108.00.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure, but the +$190.00 from the options cushions the move. At $98.00, the client's combined position is −$10.00 — the shares lose −$200.00 and the options add +$190.00. Breakeven is $98.10 (1.9% below spot). There is no cap on downside risk. Without the options, the loss would be −$200.00.

**Stagnant**: If the stock stays between $100.00 and $108.00
This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is +$190.00 — the shares gain $0.00 and the options add +$190.00. Maximum gain is +$990.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at +$990.00 — the short call limits further upside. The trade-off: $190.00 in collected premium in exchange for giving up gains above $108.00.

---

## Strategy: Covered Put (ID=9, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the minimum outcome is +$990.00. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable.

**Stagnant**: If the stock stays between $92.00 and $100.00
This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is +$190.00 — the shares gain $0.00 and the options add +$190.00. Maximum gain is +$990.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is −$10.00 — the shares lose −$200.00 and the options add +$190.00. Breakeven is $101.90 (1.9% above spot). Maximum gain is +$990.00.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the minimum outcome is +$990.00. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable.

**Stagnant**: If the stock stays between $92.00 and $100.00
This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is +$190.00 — the shares gain $0.00 and the options add +$190.00. Maximum gain is +$990.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is −$10.00 — the shares lose −$200.00 and the options add +$190.00. Breakeven is $101.90 (1.9% above spot). Maximum gain is +$990.00.

---

## Strategy: Protective Call (ID=10, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $98.00, the client's combined position is +$10.00 — the shares gain +$200.00 and the options cost −$190.00. Breakeven is $98.10 (1.9% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $100.00 and $108.00
Between $100.00 and $108.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is −$190.00 — the shares gain $0.00 and the options cost −$190.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's losses are capped at −$990.00.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $98.00, the client's combined position is +$10.00 — the shares gain +$200.00 and the options cost −$190.00. Breakeven is $98.10 (1.9% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $100.00 and $108.00
Between $100.00 and $108.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is −$190.00 — the shares gain $0.00 and the options cost −$190.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's losses are capped at −$990.00.

---

## Strategy: Protective Put (ID=11, Code=PPRT)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's losses are capped at −$990.00 — the long $92.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $100.00
Between $92.00 and $100.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is −$190.00 — the shares gain $0.00 and the options cost −$190.00. The cost of protection: $190.00 (1.9% of the position) for a guaranteed loss limit at $92.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $102.00, the client's combined position is +$10.00 — the shares gain +$200.00 and the options cost −$190.00. Breakeven is $101.90 (1.9% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's losses are capped at −$990.00 — the long $92.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $100.00
Between $92.00 and $100.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is −$190.00 — the shares gain $0.00 and the options cost −$190.00. The cost of protection: $190.00 (1.9% of the position) for a guaranteed loss limit at $92.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $102.00, the client's combined position is +$10.00 — the shares gain +$200.00 and the options cost −$190.00. Breakeven is $101.90 (1.9% above spot). There is no cap on upside gains.

---

## Strategy: Collar (ID=12, Code=COL_EQ)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's losses are capped at −$800.00 — the long $92.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is $0.00 — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is +$800.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at +$800.00 — the short call limits further upside. The trade-off: downside protection below $92.00 in exchange for capping gains above $108.00.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's losses are capped at −$800.00 — the long $92.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is $0.00 — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is +$800.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at +$800.00 — the short call limits further upside. The trade-off: downside protection below $92.00 in exchange for capping gains above $108.00.

---

## Strategy: Bull Call Spread (ID=13, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, losses are capped at −$800.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is +$800.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, gains are capped at +$800.00.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is −$2,300.00 — the shares lose −$1,500.00 and the options cost −$800.00. Maximum loss is −$10,800.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, reduced by the $800.00 option cost. At $100.00, the client's combined position is $0.00 — the shares gain $0.00 and the options cost $0.00. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$2,300.00 — the shares gain +$1,500.00 and the options add +$800.00. There is no cap on upside gains.

---

## Strategy: Bear Put Spread (ID=14, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the position achieves its maximum gain of +$800.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is +$800.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, losses are capped at −$800.00.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure, but the +$800.00 from the options cushions the move. At $85.00, the client's combined position is −$700.00 — the shares lose −$1,500.00 and the options add +$800.00. Breakeven is $92.00 (8.0% below spot). Maximum loss is −$9,200.00. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at $0.00. Breakevens are $97.32 (2.7% below spot) and $103.34 (3.3% above spot) (among multiple breakevens). The cost of protection: $800.00 (8.0% of the position) for a guaranteed loss limit at $108.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$700.00 — the shares gain +$1,500.00 and the options cost −$800.00. Breakeven is $108.00 (8.0% above spot). There is no cap on upside gains.

---

## Strategy: Bear Call Spread (ID=15, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the position achieves its maximum gain of +$800.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is +$800.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, losses are capped at −$800.00.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure, but the +$800.00 from the options cushions the move. At $85.00, the client's combined position is −$700.00 — the shares lose −$1,500.00 and the options add +$800.00. Breakeven is $92.00 (8.0% below spot). Maximum loss is −$9,200.00. Without the options, the loss would be −$1,500.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $800.00 credit is retained. Breakevens are $96.32 (3.7% below spot) and $103.34 (3.3% above spot) (among multiple breakevens).

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$700.00 — the shares gain +$1,500.00 and the options cost −$800.00. Breakeven is $108.00 (8.0% above spot). There is no cap on upside gains.

---

## Strategy: Bull Put Spread (ID=16, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, losses are capped at −$800.00 — the long $92.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is +$800.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, gains are capped at +$800.00.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is −$2,300.00 — the shares lose −$1,500.00 and the options cost −$800.00. Maximum loss is −$10,800.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, enhanced by the $800.00 net credit received. At $100.00, the client's combined position is $0.00 — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$2,300.00 — the shares gain +$1,500.00 and the options add +$800.00. There is no cap on upside gains.

---

## Strategy: Call Ratio Backspread (ID=17, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the position achieves its maximum gain of +$610.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is −$190.00. Breakeven is $98.10 (1.9% below spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the position rises with the stock. At $115.00, the position is −$290.00. Breakeven is $117.90 (17.9% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure, but the +$610.00 from the options cushions the move. At $85.00, the client's combined position is −$890.00 — the shares lose −$1,500.00 and the options add +$610.00. Maximum loss is −$9,390.00. Without the options, the loss would be −$1,500.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at −$190.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$1,210.00 — the shares gain +$1,500.00 and the options cost −$290.00. Breakeven is $108.95 (9.0% above spot). There is no cap on upside gains.

---

## Strategy: Put Ratio Backspread (ID=18, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the position gains value as the stock falls. At $85.00, the position is −$290.00. Breakeven is $82.10 (17.9% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is −$190.00. Breakeven is $101.90 (1.9% above spot). Maximum gain is +$8,210.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, gains are capped at +$610.00.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's losses are capped at −$1,790.00 — the long $92.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, enhanced by the $610.00 net credit received. At $100.00, the client's combined position is −$190.00 — the shares gain $0.00 and the options cost −$190.00. Breakeven is $100.95 (1.0% above spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$2,110.00 — the shares gain +$1,500.00 and the options add +$610.00. There is no cap on upside gains.

---

## Strategy: Call Ratio Spread (ID=19, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, losses are capped at −$610.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is +$190.00. Breakeven is $98.10 (1.9% below spot). Maximum gain is +$990.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, losses increase as the stock rises. At $115.00, the position is +$290.00. Breakeven is $117.90 (17.9% above spot). Maximum gain is +$990.00.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is −$2,110.00 — the shares lose −$1,500.00 and the options cost −$610.00. There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, reduced by the $610.00 option cost. At $100.00, the client's combined position is +$190.00 — the shares gain $0.00 and the options add +$190.00. Breakeven is $99.05 (1.0% below spot). Maximum gain is +$1,790.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at +$1,790.00 — the short call limits further upside. The trade-off: $610.00 in collected premium in exchange for giving up gains above $108.00.

---

## Strategy: Put Ratio Spread (ID=20, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the position loses value as the stock falls. At $85.00, the position is +$290.00. Breakeven is $82.10 (17.9% below spot). Maximum loss is −$8,210.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is +$190.00. Breakeven is $101.90 (1.9% above spot). Maximum gain is +$990.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, losses are capped at −$610.00.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure, but the +$290.00 from the options cushions the move. At $85.00, the client's combined position is −$1,210.00 — the shares lose −$1,500.00 and the options add +$290.00. Breakeven is $91.05 (9.0% below spot). Maximum loss is −$18,210.00. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position captures its maximum gain of +$190.00. The cost of protection: $610.00 (6.1% of the position) for a guaranteed loss limit at $108.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$890.00 — the shares gain +$1,500.00 and the options cost −$610.00. There is no cap on upside gains.

---

## Strategy: Bull Call Ladder (ID=21, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $85.00
At any price below $85.00, losses are capped at −$1,250.00.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position gains value as the stock moves higher. At $100.00, the position is +$250.00. Breakeven is $97.50 (2.5% below spot). Maximum gain is +$250.00.

**Bullish**: If the stock rises above $115.00
Above $115.00, losses increase as the stock rises. At $115.00, the position is +$250.00. Breakeven is $117.50 (17.5% above spot). Maximum gain is +$250.00.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure. At $85.00, the client's combined position is −$2,750.00 — the shares lose −$1,500.00 and the options cost −$1,250.00. Maximum loss is −$11,250.00.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, reduced by the $1,250.00 option cost. At $100.00, the client's combined position is +$250.00 — the shares gain $0.00 and the options add +$250.00. Breakeven is $98.75 (1.2% below spot). Maximum gain is +$1,750.00.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, the client's gains are capped at +$1,750.00 — the short call limits further upside. The trade-off: $1,250.00 in collected premium in exchange for giving up gains above $100.00.

---

## Strategy: Bear Put Ladder (ID=22, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $85.00
Below $85.00, the position loses value as the stock falls. At $85.00, the position is +$250.00. Breakeven is $82.50 (17.5% below spot). Maximum loss is −$8,250.00.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position gains value as the stock moves lower. At $100.00, the position is +$250.00. Breakeven is $102.50 (2.5% above spot). Maximum gain is +$250.00.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, losses are capped at −$1,250.00.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure, but the +$250.00 from the options cushions the move. At $85.00, the client's combined position is −$1,250.00 — the shares lose −$1,500.00 and the options add +$250.00. Maximum loss is −$18,250.00. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, reduced by the $1,250.00 option cost. At $100.00, the client's combined position is +$250.00 — the shares gain $0.00 and the options add +$250.00. Breakeven is $97.50 (2.5% below spot). The cost of protection: $1,250.00 (12.5% of the position) for a guaranteed loss limit at $115.00.

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is +$250.00 — the shares gain +$1,500.00 and the options cost −$1,250.00. There is no cap on upside gains.

---

## Strategy: Bear Call Ladder (ID=23, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $85.00
At any price below $85.00, the position achieves its maximum gain of +$1,250.00.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position gains value as the stock moves lower. At $100.00, the position is −$250.00. Breakeven is $97.50 (2.5% below spot).

**Bullish**: If the stock rises above $115.00
Above $115.00, the position rises with the stock. At $115.00, the position is −$250.00. Breakeven is $117.50 (17.5% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure, but the +$1,250.00 from the options cushions the move. At $85.00, the client's combined position is −$250.00 — the shares lose −$1,500.00 and the options add +$1,250.00. Maximum loss is −$8,750.00. Without the options, the loss would be −$1,500.00.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, enhanced by the $1,250.00 net credit received. At $100.00, the client's combined position is −$250.00 — the shares gain $0.00 and the options cost −$250.00. Breakeven is $102.50 (2.5% above spot).

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is +$1,250.00 — the shares gain +$1,500.00 and the options cost −$250.00. There is no cap on upside gains.

---

## Strategy: Bull Put Ladder (ID=24, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $85.00
Below $85.00, the position gains value as the stock falls. At $85.00, the position is −$250.00. Breakeven is $82.50 (17.5% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position gains value as the stock moves higher. At $100.00, the position is −$250.00. Breakeven is $102.50 (2.5% above spot). Maximum gain is +$8,250.00.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, gains are capped at +$1,250.00.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
At any price below $85.00, the client's losses are capped at −$1,750.00 — the long $100.00 put provides a hard floor.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, enhanced by the $1,250.00 net credit received. At $100.00, the client's combined position is −$250.00 — the shares gain $0.00 and the options cost −$250.00. Breakeven is $101.25 (1.2% above spot).

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is +$2,750.00 — the shares gain +$1,500.00 and the options add +$1,250.00. There is no cap on upside gains.

---

## Strategy: Long Call Butterfly (ID=25, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $85.00
At any price below $85.00, losses are capped at −$1,276.00.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position reaches its maximum gain of +$224.00 at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is +$224.00. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is +$224.00.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, losses are capped at −$1,276.00.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure. At $85.00, the client's combined position is −$2,776.00 — the shares lose −$1,500.00 and the options cost −$1,276.00. Maximum loss is −$11,276.00.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, reduced by the $1,276.00 option cost. At $100.00, the client's combined position is +$224.00 — the shares gain $0.00 and the options add +$224.00. Breakeven is $98.88 (1.1% below spot).

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is +$224.00 — the shares gain +$1,500.00 and the options cost −$1,276.00. There is no cap on upside gains.

---

## Strategy: Long Put Butterfly (ID=26, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $85.00
At any price below $85.00, losses are capped at −$1,276.00 — the long $85.00 put provides a hard floor.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position reaches its maximum gain of +$224.00 at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is +$224.00. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is +$224.00.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, losses are capped at −$1,276.00.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure. At $85.00, the client's combined position is −$2,776.00 — the shares lose −$1,500.00 and the options cost −$1,276.00. Maximum loss is −$11,276.00.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, reduced by the $1,276.00 option cost. At $100.00, the client's combined position is +$224.00 — the shares gain $0.00 and the options add +$224.00. Breakeven is $98.88 (1.1% below spot). The cost of protection: $1,276.00 (12.8% of the position) for a guaranteed loss limit at $85.00.

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is +$224.00 — the shares gain +$1,500.00 and the options cost −$1,276.00. There is no cap on upside gains.

---

## Strategy: Iron Butterfly (ID=27, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $85.00
At any price below $85.00, losses are capped at −$1,276.00 — the long $85.00 put provides a hard floor.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position reaches its maximum gain of +$224.00 at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is +$224.00. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is +$224.00.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, losses are capped at −$1,276.00.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure. At $85.00, the client's combined position is −$2,776.00 — the shares lose −$1,500.00 and the options cost −$1,276.00. Maximum loss is −$11,276.00.

**Stagnant**: If the stock stays between $85.00 and $115.00
This is the ideal range — the options expire worthless and the client keeps the full $224.00 in premium on top of share movement. At $100.00, the client's combined position is +$224.00 — the shares gain $0.00 and the options add +$224.00. Breakeven is $98.88 (1.1% below spot).

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is +$224.00 — the shares gain +$1,500.00 and the options cost −$1,276.00. There is no cap on upside gains.

---

## Strategy: Long Call Condor (ID=28, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00. Maximum loss is −$1,020.00 at any price below $80.00. Breakeven is $90.20 (9.8% below spot).

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position captures its maximum gain of +$180.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the short $108.00 call drives losses, but the long $120.00 call caps the damage. Maximum loss is −$1,020.00 at any price above $120.00. Breakeven is $109.80 (9.8% above spot).

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is −$2,020.00 — the shares lose −$1,500.00 and the options cost −$520.00. Maximum loss is −$11,020.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, reduced by the $1,020.00 option cost. At $100.00, the client's combined position is +$180.00 — the shares gain $0.00 and the options add +$180.00. Breakeven is $98.20 (1.8% below spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$980.00 — the shares gain +$1,500.00 and the options cost −$520.00. There is no cap on upside gains.

---

## Strategy: Long Put Condor (ID=29, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the short $92.00 put drives losses, but the long $80.00 put provides a hard floor. Maximum loss is −$1,020.00 at any price below $80.00. Breakeven is $90.20 (9.8% below spot).

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position captures its maximum gain of +$180.00.

**Bullish**: If the stock rises above $108.00
Above $108.00. Maximum loss is −$1,020.00 at any price above $120.00. Breakeven is $109.80 (9.8% above spot).

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is −$2,020.00 — the shares lose −$1,500.00 and the options cost −$520.00. Maximum loss is −$11,020.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, reduced by the $1,020.00 option cost. At $100.00, the client's combined position is +$180.00 — the shares gain $0.00 and the options add +$180.00. Breakeven is $98.20 (1.8% below spot). The cost of protection: $1,020.00 (10.2% of the position) for a guaranteed loss limit at $80.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$980.00 — the shares gain +$1,500.00 and the options cost −$520.00. There is no cap on upside gains.

---

## Strategy: Iron Condor (ID=30, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the short $92.00 put drives losses, but the long $80.00 put provides a hard floor. Maximum loss is −$1,020.00 at any price below $80.00. Breakeven is $90.20 (9.8% below spot).

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $180.00 credit is retained.

**Bullish**: If the stock rises above $108.00
Above $108.00, the short $108.00 call drives losses, but the long $120.00 call caps the damage. Maximum loss is −$1,020.00 at any price above $120.00. Breakeven is $109.80 (9.8% above spot).

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is −$2,020.00 — the shares lose −$1,500.00 and the options cost −$520.00. Maximum loss is −$11,020.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the ideal range — the options expire worthless and the client keeps the full $180.00 in premium on top of share movement. At $100.00, the client's combined position is +$180.00 — the shares gain $0.00 and the options add +$180.00. Breakeven is $98.20 (1.8% below spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$980.00 — the shares gain +$1,500.00 and the options cost −$520.00. There is no cap on upside gains.

---

## Strategy: Short Call Butterfly (ID=31, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $85.00
At any price below $85.00, the position achieves its maximum gain of +$1,276.00.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position reaches its maximum loss of −$224.00 at $100.00 and improves toward the zone boundaries. At $100.00, the position is −$224.00. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is +$1,276.00.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, gains are capped at +$1,276.00.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure, but the +$1,276.00 from the options cushions the move. At $85.00, the client's combined position is −$224.00 — the shares lose −$1,500.00 and the options add +$1,276.00. Maximum loss is −$8,724.00. Without the options, the loss would be −$1,500.00.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, enhanced by the $1,276.00 net credit received. At $100.00, the client's combined position is −$224.00 — the shares gain $0.00 and the options cost −$224.00. Breakeven is $101.12 (1.1% above spot).

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is +$2,776.00 — the shares gain +$1,500.00 and the options add +$1,276.00. There is no cap on upside gains.

---

## Strategy: Short Put Butterfly (ID=32, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $85.00
At any price below $85.00, the position achieves its maximum gain of +$1,276.00.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position reaches its maximum loss of −$224.00 at $100.00 and improves toward the zone boundaries. At $100.00, the position is −$224.00. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is +$1,276.00.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, gains are capped at +$1,276.00.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure, but the +$1,276.00 from the options cushions the move. At $85.00, the client's combined position is −$224.00 — the shares lose −$1,500.00 and the options add +$1,276.00. Maximum loss is −$8,724.00. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, enhanced by the $1,276.00 net credit received. At $100.00, the client's combined position is −$224.00 — the shares gain $0.00 and the options cost −$224.00. Breakeven is $101.12 (1.1% above spot).

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is +$2,776.00 — the shares gain +$1,500.00 and the options add +$1,276.00. There is no cap on upside gains.

---

## Strategy: Rev Iron Butterfly (ID=33, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $85.00
At any price below $85.00, the position achieves its maximum gain of +$1,276.00.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position reaches its maximum loss of −$224.00 at $100.00 and improves toward the zone boundaries. At $100.00, the position is −$224.00. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is +$1,276.00.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, gains are capped at +$1,276.00.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure, but the +$1,276.00 from the options cushions the move. At $85.00, the client's combined position is −$224.00 — the shares lose −$1,500.00 and the options add +$1,276.00. Maximum loss is −$8,724.00. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, reduced by the $224.00 option cost. At $100.00, the client's combined position is −$224.00 — the shares gain $0.00 and the options cost −$224.00. Breakeven is $101.12 (1.1% above spot). The cost of protection: $224.00 (2.2% of the position) for a guaranteed loss limit at $100.00.

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is +$2,776.00 — the shares gain +$1,500.00 and the options add +$1,276.00. There is no cap on upside gains.

---

## Strategy: Short Call Condor (ID=34, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00. The worst outcome is +$1,020.00 at any price below $80.00. Breakeven is $90.20 (9.8% below spot).

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at −$180.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the short $120.00 call drives losses, but the long $108.00 call caps the damage. The worst outcome is +$1,020.00 at any price above $120.00. Breakeven is $109.80 (9.8% above spot).

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client's position loses value as the stock falls. At $85.00, the client's combined position is −$980.00 — the shares lose −$1,500.00 and the options add +$520.00. Maximum loss is −$8,980.00. Without the options, the loss would be −$1,500.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, enhanced by the $1,020.00 net credit received. At $100.00, the client's combined position is −$180.00 — the shares gain $0.00 and the options cost −$180.00. Breakeven is $101.80 (1.8% above spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$2,020.00 — the shares gain +$1,500.00 and the options add +$520.00. There is no cap on upside gains.

---

## Strategy: Short Put Condor (ID=35, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the short $80.00 put drives losses, but the long $92.00 put provides a hard floor. The worst outcome is +$1,020.00 at any price below $80.00. Breakeven is $90.20 (9.8% below spot).

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at −$180.00.

**Bullish**: If the stock rises above $108.00
Above $108.00. The worst outcome is +$1,020.00 at any price above $120.00. Breakeven is $109.80 (9.8% above spot).

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client's position loses value as the stock falls. At $85.00, the client's combined position is −$980.00 — the shares lose −$1,500.00 and the options add +$520.00. Maximum loss is −$8,980.00. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, enhanced by the $1,020.00 net credit received. At $100.00, the client's combined position is −$180.00 — the shares gain $0.00 and the options cost −$180.00. Breakeven is $101.80 (1.8% above spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$2,020.00 — the shares gain +$1,500.00 and the options add +$520.00. There is no cap on upside gains.

---

## Strategy: Rev Iron Condor (ID=36, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the short $80.00 put drives losses, but the long $92.00 put provides a hard floor. The worst outcome is +$1,020.00 at any price below $80.00. Breakeven is $90.20 (9.8% below spot).

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at −$180.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the short $120.00 call drives losses, but the long $108.00 call caps the damage. The worst outcome is +$1,020.00 at any price above $120.00. Breakeven is $109.80 (9.8% above spot).

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client's position loses value as the stock falls. At $85.00, the client's combined position is −$980.00 — the shares lose −$1,500.00 and the options add +$520.00. Maximum loss is −$8,980.00. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, reduced by the $180.00 option cost. At $100.00, the client's combined position is −$180.00 — the shares gain $0.00 and the options cost −$180.00. Breakeven is $101.80 (1.8% above spot). The cost of protection: $180.00 (1.8% of the position) for a guaranteed loss limit at $92.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$2,020.00 — the shares gain +$1,500.00 and the options add +$520.00. There is no cap on upside gains.

---

## Strategy: Long Straddle (ID=37, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position gains value as the stock falls. At $90.00, the position is +$500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is −$500.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the position rises with the stock. At $110.00, the position is +$500.00. Breakeven is $105.00 (5.0% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
At any price below $100.00, the client's losses are capped at −$500.00 — the long $100.00 put provides a hard floor.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is −$500.00 — the shares gain $0.00 and the options cost −$500.00. The cost of protection: $500.00 (5.0% of the position) for a guaranteed loss limit at $100.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is +$1,500.00 — the shares gain +$1,000.00 and the options add +$500.00. Breakeven is $102.50 (2.5% above spot). There is no cap on upside gains.

---

## Strategy: Short Straddle (ID=38, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position loses value as the stock falls. At $90.00, the position is −$500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is +$500.00. Maximum gain is +$500.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, losses increase as the stock rises. At $110.00, the position is −$500.00. Breakeven is $105.00 (5.0% above spot). Maximum gain is +$500.00.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is −$1,500.00 — the shares lose −$1,000.00 and the options cost −$500.00. Breakeven is $97.50 (2.5% below spot). Maximum loss is −$19,500.00.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is +$500.00 — the shares gain $0.00 and the options add +$500.00. Maximum gain is +$500.00.

**Bullish**: If the stock rises above $100.00
At any price above $100.00, the client's gains are capped at +$500.00 — the short call limits further upside. The trade-off: $500.00 in collected premium in exchange for giving up gains above $100.00.

---

## Strategy: Long Strangle (ID=39, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the position gains value as the stock falls. At $85.00, the position is +$320.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at −$380.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the position rises with the stock. At $115.00, the position is +$320.00. Breakeven is $111.80 (11.8% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's losses are capped at −$1,180.00 — the long $92.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, reduced by the $380.00 option cost. At $100.00, the client's combined position is −$380.00 — the shares gain $0.00 and the options cost −$380.00. Breakeven is $103.80 (3.8% above spot). The cost of protection: $380.00 (3.8% of the position) for a guaranteed loss limit at $92.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$1,820.00 — the shares gain +$1,500.00 and the options add +$320.00. There is no cap on upside gains.

---

## Strategy: Short Strangle (ID=40, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the position loses value as the stock falls. At $85.00, the position is −$320.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $380.00 credit is retained.

**Bullish**: If the stock rises above $108.00
Above $108.00, losses increase as the stock rises. At $115.00, the position is −$320.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is +$380.00.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is −$1,820.00 — the shares lose −$1,500.00 and the options cost −$320.00. There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is +$380.00 — the shares gain $0.00 and the options add +$380.00. Breakeven is $96.20 (3.8% below spot). Maximum gain is +$1,180.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at +$1,180.00 — the short call limits further upside. The trade-off: $380.00 in collected premium in exchange for giving up gains above $108.00.

---

## Strategy: Long Guts (ID=41, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the position gains value as the stock falls. At $85.00, the position is +$320.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at −$380.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the position rises with the stock. At $115.00, the position is +$320.00. Breakeven is $111.80 (11.8% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's losses are capped at −$1,180.00 — the long $108.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, reduced by the $1,980.00 option cost. At $100.00, the client's combined position is −$380.00 — the shares gain $0.00 and the options cost −$380.00. Breakeven is $103.80 (3.8% above spot). The cost of protection: $1,980.00 (19.8% of the position) for a guaranteed loss limit at $108.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$1,820.00 — the shares gain +$1,500.00 and the options add +$320.00. There is no cap on upside gains.

---

## Strategy: Short Guts (ID=42, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the position loses value as the stock falls. At $85.00, the position is −$320.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,980.00 credit is retained.

**Bullish**: If the stock rises above $108.00
Above $108.00, losses increase as the stock rises. At $115.00, the position is −$320.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is +$380.00.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is −$1,820.00 — the shares lose −$1,500.00 and the options cost −$320.00. There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, enhanced by the $1,980.00 net credit received. At $100.00, the client's combined position is +$380.00 — the shares gain $0.00 and the options add +$380.00. Breakeven is $96.20 (3.8% below spot). Maximum gain is +$1,180.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at +$1,180.00 — the short call limits further upside. The trade-off: $1,980.00 in collected premium in exchange for giving up gains above $92.00.

---

## Strategy: Strip (ID=43, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position gains value as the stock falls. At $90.00, the position is +$1,250.00. Breakeven is $96.25 (3.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is −$750.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the position rises with the stock. At $110.00, the position is +$250.00. Breakeven is $107.50 (7.5% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is +$250.00 — the shares lose −$1,000.00 and the options add +$1,250.00. Breakeven is $92.50 (7.5% below spot). There is no cap on downside risk. Without the put, a drop to $90.00 would mean a −$1,000.00 loss on the shares alone.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $750.00 option cost. At $100.00, the client's combined position is −$750.00 — the shares gain $0.00 and the options cost −$750.00. The cost of protection: $750.00 (7.5% of the position) for a guaranteed loss limit at $100.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is +$1,250.00 — the shares gain +$1,000.00 and the options add +$250.00. Breakeven is $103.75 (3.8% above spot). There is no cap on upside gains.

---

## Strategy: Strap (ID=44, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position gains value as the stock falls. At $90.00, the position is +$250.00. Breakeven is $92.50 (7.5% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is −$750.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the position rises with the stock. At $110.00, the position is +$1,250.00. Breakeven is $103.75 (3.8% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
At any price below $100.00, the client's losses are capped at −$750.00 — the long $100.00 put provides a hard floor.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $750.00 option cost. At $100.00, the client's combined position is −$750.00 — the shares gain $0.00 and the options cost −$750.00. The cost of protection: $750.00 (7.5% of the position) for a guaranteed loss limit at $100.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is +$2,250.00 — the shares gain +$1,000.00 and the options add +$1,250.00. Breakeven is $102.50 (2.5% above spot). There is no cap on upside gains.

---

## Strategy: Covered Short Straddle (ID=45, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is −$1,500.00 — the shares lose −$1,000.00 and the options cost −$500.00. Breakeven is $97.50 (2.5% below spot). Maximum loss is −$19,500.00.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is +$500.00 — the shares gain $0.00 and the options add +$500.00. Maximum gain is +$500.00.

**Bullish**: If the stock rises above $100.00
At any price above $100.00, the client's gains are capped at +$500.00 — the short call limits further upside. The trade-off: $500.00 in collected premium in exchange for giving up gains above $100.00.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is −$1,500.00 — the shares lose −$1,000.00 and the options cost −$500.00. Breakeven is $97.50 (2.5% below spot). Maximum loss is −$19,500.00.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is +$500.00 — the shares gain $0.00 and the options add +$500.00. Maximum gain is +$500.00.

**Bullish**: If the stock rises above $100.00
At any price above $100.00, the client's gains are capped at +$500.00 — the short call limits further upside. The trade-off: $500.00 in collected premium in exchange for giving up gains above $100.00.

---

## Strategy: Covered Short Strangle (ID=46, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is −$1,820.00 — the shares lose −$1,500.00 and the options cost −$320.00. There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is +$380.00 — the shares gain $0.00 and the options add +$380.00. Breakeven is $96.20 (3.8% below spot). Maximum gain is +$1,180.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at +$1,180.00 — the short call limits further upside. The trade-off: $380.00 in collected premium in exchange for giving up gains above $108.00.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is −$1,820.00 — the shares lose −$1,500.00 and the options cost −$320.00. There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is +$380.00 — the shares gain $0.00 and the options add +$380.00. Breakeven is $96.20 (3.8% below spot). Maximum gain is +$1,180.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at +$1,180.00 — the short call limits further upside. The trade-off: $380.00 in collected premium in exchange for giving up gains above $108.00.

---

## Strategy: Long Box Spread (ID=47, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the short $92.00 put drives losses, but the long $108.00 put provides a hard floor Breakevens are $88.29 (11.7% below spot) and $92.00 (8.0% below spot) (among multiple breakevens).

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at $0.00. Breakevens are $92.00 (8.0% below spot) and $103.34 (3.3% above spot) and $108.00 (8.0% above spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the short $108.00 call drives losses, but the long $92.00 call caps the damage Breakevens are $108.00 (8.0% above spot) and $108.36 (8.4% above spot) (among multiple breakevens).

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is −$1,500.00 — the shares lose −$1,500.00 and the options cost $0.00. Maximum loss is −$10,000.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, reduced by the $1,600.00 option cost. At $100.00, the client's combined position is $0.00 — the shares gain $0.00 and the options cost $0.00. Breakeven is $100.00 (0.0% above spot). The cost of protection: $1,600.00 (16.0% of the position) for a guaranteed loss limit at $108.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$1,500.00 — the shares gain +$1,500.00 and the options cost $0.00. There is no cap on upside gains.

---

## Strategy: Short Box Spread (ID=48, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the short $108.00 put drives losses, but the long $92.00 put provides a hard floor Breakevens are $88.29 (11.7% below spot) and $92.00 (8.0% below spot) (among multiple breakevens).

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,600.00 credit is retained. Breakevens are $92.00 (8.0% below spot) and $103.34 (3.3% above spot) and $108.00 (8.0% above spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the short $92.00 call drives losses, but the long $108.00 call caps the damage Breakevens are $108.00 (8.0% above spot) and $108.36 (8.4% above spot) (among multiple breakevens).

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure, but the $0.00 from the options cushions the move. At $85.00, the client's combined position is −$1,500.00 — the shares lose −$1,500.00 and the options add $0.00. Maximum loss is −$10,000.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, enhanced by the $1,600.00 net credit received. At $100.00, the client's combined position is $0.00 — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$1,500.00 — the shares gain +$1,500.00 and the options add $0.00. There is no cap on upside gains.

---

## Strategy: Synthetic Long Stock (ID=49, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position loses value as the stock falls. At $90.00, the position is −$1,000.00. Breakeven is $100.00 (0.0% above spot). Maximum loss is −$10,000.00.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is $0.00. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $100.00
Above $100.00, the position rises with the stock. At $110.00, the position is +$1,000.00. Breakeven is $100.00 (0.0% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is −$2,000.00 — the shares lose −$1,000.00 and the options cost −$1,000.00. Breakeven is $100.00 (0.0% above spot). Maximum loss is −$20,000.00.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock. At $100.00, the client's combined position is $0.00 — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is +$2,000.00 — the shares gain +$1,000.00 and the options add +$1,000.00. Breakeven is $100.00 (0.0% above spot). There is no cap on upside gains.

---

## Strategy: Synthetic Short Stock (ID=50, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position gains value as the stock falls. At $90.00, the position is +$1,000.00. Breakeven is $100.00 (0.0% above spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is +$10,000.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, losses increase as the stock rises. At $110.00, the position is −$1,000.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is +$10,000.00.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, but the long $100.00 put provides a hard floor Breakevens are $99.33 (0.7% below spot) and $100.00 (0.0% above spot) (among multiple breakevens). The client bought the stock below the protection floor, so even in a severe decline, the position is profitable.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is $0.00 — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is $0.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the short $100.00 call drives losses Breakevens are $100.00 (0.0% above spot) and $100.33 (0.3% above spot) (among multiple breakevens). The trade-off: downside protection below $100.00 in exchange for capping gains above $100.00.

---

## Strategy: Long Combo (ID=51, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the position loses value as the stock falls. At $85.00, the position is −$700.00. Breakeven is $92.00 (8.0% below spot). Maximum loss is −$9,200.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position captures its maximum gain of $0.00. Breakevens are $99.33 (0.7% below spot) and $100.33 (0.3% above spot) (among multiple breakevens).

**Bullish**: If the stock rises above $108.00
Above $108.00, the position rises with the stock. At $115.00, the position is +$700.00. Breakeven is $108.00 (8.0% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is −$2,200.00 — the shares lose −$1,500.00 and the options cost −$700.00. Maximum loss is −$19,200.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock. At $100.00, the client's combined position is $0.00 — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$2,200.00 — the shares gain +$1,500.00 and the options add +$700.00. There is no cap on upside gains.

---

## Strategy: Short Combo (ID=52, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the position gains value as the stock falls. At $85.00, the position is +$700.00. Breakeven is $92.00 (8.0% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position captures its maximum gain of $0.00. Breakevens are $99.33 (0.7% below spot) and $100.33 (0.3% above spot) (among multiple breakevens).

**Bullish**: If the stock rises above $108.00
Above $108.00, losses increase as the stock rises. At $115.00, the position is −$700.00. Breakeven is $108.00 (8.0% above spot). Maximum gain is +$9,200.00.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's losses are capped at −$800.00 — the long $92.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is $0.00 — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is +$800.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at +$800.00 — the short call limits further upside. The trade-off: downside protection below $92.00 in exchange for capping gains above $108.00.

---

## Strategy: L. Call Syn. Straddle (ID=53, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is +$500.00 — the shares gain +$1,000.00 and the options cost −$500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is −$500.00 — the shares gain $0.00 and the options cost −$500.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is +$500.00 — the shares lose −$1,000.00 and the options add +$1,500.00. Breakeven is $105.00 (5.0% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is +$500.00 — the shares gain +$1,000.00 and the options cost −$500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is −$500.00 — the shares gain $0.00 and the options cost −$500.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is +$500.00 — the shares lose −$1,000.00 and the options add +$1,500.00. Breakeven is $105.00 (5.0% above spot). There is no cap on upside gains.

---

## Strategy: L. Put Syn. Straddle (ID=54, Code=PPRT)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is +$500.00 — the shares lose −$1,000.00 and the options add +$1,500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk. Without the put, a drop to $90.00 would mean a −$1,000.00 loss on the shares alone.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is −$500.00 — the shares gain $0.00 and the options cost −$500.00. The cost of protection: $500.00 (5.0% of the position) for a guaranteed loss limit at $100.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is +$500.00 — the shares gain +$1,000.00 and the options cost −$500.00. Breakeven is $105.00 (5.0% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is +$500.00 — the shares lose −$1,000.00 and the options add +$1,500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk. Without the put, a drop to $90.00 would mean a −$1,000.00 loss on the shares alone.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is −$500.00 — the shares gain $0.00 and the options cost −$500.00. The cost of protection: $500.00 (5.0% of the position) for a guaranteed loss limit at $100.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is +$500.00 — the shares gain +$1,000.00 and the options cost −$500.00. Breakeven is $105.00 (5.0% above spot). There is no cap on upside gains.

---

## Strategy: S. Call Syn. Straddle (ID=55, Code=CCOV)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure, but the +$500.00 from the options cushions the move. At $90.00, the client's combined position is −$500.00 — the shares lose −$1,000.00 and the options add +$500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk. Without the options, the loss would be −$1,000.00.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is +$500.00 — the shares gain $0.00 and the options add +$500.00. Maximum gain is +$500.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is −$500.00 — the shares gain +$1,000.00 and the options cost −$1,500.00. Breakeven is $105.00 (5.0% above spot). Maximum gain is +$500.00.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure, but the +$500.00 from the options cushions the move. At $90.00, the client's combined position is −$500.00 — the shares lose −$1,000.00 and the options add +$500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk. Without the options, the loss would be −$1,000.00.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is +$500.00 — the shares gain $0.00 and the options add +$500.00. Maximum gain is +$500.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is −$500.00 — the shares gain +$1,000.00 and the options cost −$1,500.00. Breakeven is $105.00 (5.0% above spot). Maximum gain is +$500.00.

---

## Strategy: S. Put Syn. Straddle (ID=56, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is −$500.00 — the shares gain +$1,000.00 and the options cost −$1,500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is +$500.00 — the shares gain $0.00 and the options add +$500.00. Maximum gain is +$500.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is −$500.00 — the shares lose −$1,000.00 and the options add +$500.00. Breakeven is $105.00 (5.0% above spot). Maximum gain is +$500.00.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is −$500.00 — the shares gain +$1,000.00 and the options cost −$1,500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is +$500.00 — the shares gain $0.00 and the options add +$500.00. Maximum gain is +$500.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is −$500.00 — the shares lose −$1,000.00 and the options add +$500.00. Breakeven is $105.00 (5.0% above spot). Maximum gain is +$500.00.

---

## Strategy: L. Call Syn. Strangle (ID=57, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is +$320.00 — the shares gain +$1,500.00 and the options cost −$1,180.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at −$380.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$320.00 — the shares lose −$1,500.00 and the options add +$1,820.00. Breakeven is $111.80 (11.8% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is +$320.00 — the shares gain +$1,500.00 and the options cost −$1,180.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at −$380.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$320.00 — the shares lose −$1,500.00 and the options add +$1,820.00. Breakeven is $111.80 (11.8% above spot). There is no cap on upside gains.

---

## Strategy: L. Put Syn. Strangle (ID=58, Code=PPRT)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is +$320.00 — the shares lose −$1,500.00 and the options add +$1,820.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at −$380.00. The cost of protection: $1,180.00 (11.8% of the position) for a guaranteed loss limit at $92.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$320.00 — the shares gain +$1,500.00 and the options cost −$1,180.00. Breakeven is $111.80 (11.8% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is +$320.00 — the shares lose −$1,500.00 and the options add +$1,820.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at −$380.00. The cost of protection: $1,180.00 (11.8% of the position) for a guaranteed loss limit at $92.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$320.00 — the shares gain +$1,500.00 and the options cost −$1,180.00. Breakeven is $111.80 (11.8% above spot). There is no cap on upside gains.

---

## Strategy: S. Call Syn. Strangle (ID=59, Code=CCOV)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure, but the +$1,180.00 from the options cushions the move. At $85.00, the client's combined position is −$320.00 — the shares lose −$1,500.00 and the options add +$1,180.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk. Without the options, the loss would be −$1,500.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is −$320.00 — the shares gain +$1,500.00 and the options cost −$1,820.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is +$380.00.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure, but the +$1,180.00 from the options cushions the move. At $85.00, the client's combined position is −$320.00 — the shares lose −$1,500.00 and the options add +$1,180.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk. Without the options, the loss would be −$1,500.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is −$320.00 — the shares gain +$1,500.00 and the options cost −$1,820.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is +$380.00.

---

## Strategy: S. Put Syn. Strangle (ID=60, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is −$320.00 — the shares gain +$1,500.00 and the options cost −$1,820.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is −$320.00 — the shares lose −$1,500.00 and the options add +$1,180.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is +$380.00.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is −$320.00 — the shares gain +$1,500.00 and the options cost −$1,820.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is −$320.00 — the shares lose −$1,500.00 and the options add +$1,180.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is +$380.00.

---

## Strategy: Syn. Covered Call (ID=61, Code=CSPT)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position loses value as the stock falls. At $98.00, the position is −$10.00. Breakeven is $98.10 (1.9% below spot). Maximum loss is −$9,810.00.

**Stagnant**: If the stock stays between $100.00 and $108.00
Between $100.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is +$190.00. Maximum gain is +$990.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, gains are capped at +$990.00.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $98.00, the client's combined position is −$210.00 — the shares lose −$200.00 and the options cost −$10.00. Breakeven is $99.05 (1.0% below spot). Maximum loss is −$19,810.00.

**Stagnant**: If the stock stays between $100.00 and $108.00
Between $100.00 and $108.00, the client's position moves with the stock, enhanced by the $990.00 net credit received. At $100.00, the client's combined position is +$190.00 — the shares lose $0.00 and the options add +$190.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is +$2,490.00 — the shares gain +$1,500.00 and the options add +$990.00. There is no cap on upside gains.

---

## Strategy: Syn. Covered Put (ID=62, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the position achieves its maximum gain of +$990.00.

**Stagnant**: If the stock stays between $92.00 and $100.00
Between $92.00 and $100.00, the position gains value as the stock moves lower. At $100.00, the position is +$190.00. Maximum gain is +$990.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, losses increase as the stock rises. At $102.00, the position is −$10.00. Breakeven is $101.90 (1.9% above spot). Maximum gain is +$990.00.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure, but the +$990.00 from the options cushions the move. At $85.00, the client's combined position is −$510.00 — the shares lose −$1,500.00 and the options add +$990.00. Breakeven is $90.10 (9.9% below spot). There is no cap on downside risk. Without the options, the loss would be −$1,500.00.

**Stagnant**: If the stock stays between $92.00 and $100.00
This is the target outcome. As long as the stock stays between $92.00 and $100.00 — roughly 8.0% down to 0.0% down from here — all options expire worthless and the full $990.00 credit is retained.

**Bullish**: If the stock rises above $100.00
Above $100.00, the short $92.00 call drives losses. The worst outcome is +$190.00 at any price above $92.00. The trade-off: $990.00 in collected premium in exchange for giving up gains above $92.00.

---

## Strategy: Conversion (ID=63, Code=COL_EQ)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, but the long $100.00 put provides a hard floor Breakevens are $99.33 (0.7% below spot) and $100.00 (0.0% above spot) (among multiple breakevens). The client bought the stock below the protection floor, so even in a severe decline, the position is profitable.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is $0.00 — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is $0.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the short $100.00 call drives losses Breakevens are $100.00 (0.0% above spot) and $100.33 (0.3% above spot) (among multiple breakevens). The trade-off: downside protection below $100.00 in exchange for capping gains above $100.00.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, but the long $100.00 put provides a hard floor Breakevens are $99.33 (0.7% below spot) and $100.00 (0.0% above spot) (among multiple breakevens). The client bought the stock below the protection floor, so even in a severe decline, the position is profitable.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is $0.00 — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is $0.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the short $100.00 call drives losses Breakevens are $100.00 (0.0% above spot) and $100.33 (0.3% above spot) (among multiple breakevens). The trade-off: downside protection below $100.00 in exchange for capping gains above $100.00.

---

