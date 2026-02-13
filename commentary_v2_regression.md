# Commentary V2 Regression Report

Generated: 2026-02-13

## Summary

- **Total strategies in CSV**: 63
- **Total runs** (options-only + with-stock): 126
- **Errors**: 1
- **Average body length**: 348 chars
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
Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum loss is **−$10,000.00**.

**Stagnant**: If the stock stays between $97.00 and $103.00
Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). There is no cap on upside gains.

---

## Strategy: Long Stock (ID=2, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum loss is **−$10,000.00**.

**Stagnant**: If the stock stays between $97.00 and $103.00
Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum loss is **−$10,000.00**.

**Stagnant**: If the stock stays between $97.00 and $103.00
Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). There is no cap on upside gains.

---

## Strategy: Short Stock (ID=3, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $97.00 and $103.00
Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 100.0% return on the $10,001.00 capital at risk.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 100.0% return on the $10,001.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $97.00 and $103.00
Between $97.00 and $103.00, the client's position moves with the stock. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 100.0% return on the $10,001.00 capital at risk.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 100.0% return on the $10,001.00 capital at risk.

---

## Strategy: Long Call (ID=4, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
At any price below $100.00, losses are capped at **−$250.00**.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is **−$250.00**.

**Bullish**: If the stock rises above $100.00
Above $100.00, the position rises with the stock. At $110.00, the position is **+$750.00**. Breakeven is $102.50 (2.5% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$1,250.00** — the shares lose −$1,000.00 and the options cost −$250.00. Maximum loss is **−$10,250.00**.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $250.00 option cost. At $100.00, the client's combined position is **−$250.00** — the shares gain $0.00 and the options cost −$250.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **+$1,750.00** — the shares gain +$1,000.00 and the options add +$750.00. Breakeven is $101.25 (1.2% above spot). There is no cap on upside gains.

---

## Strategy: Short Call (ID=5, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $100.00
At any price below $100.00, gains are locked in at **+$250.00**.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is **+$250.00**. Maximum gain is **+$250.00**. That represents a 11.1% return on the $2,250.00 capital at risk.

**Bullish**: If the stock rises above $100.00
Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$750.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$250.00**. That represents a 11.1% return on the $2,250.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure, but the +$250.00 from the options cushions the move. At $90.00, the client's combined position is **−$750.00** — the shares lose −$1,000.00 and the options add +$250.00. Breakeven is $97.50 (2.5% below spot). Maximum loss is **−$9,750.00**. Without the options, the loss would be −$1,000.00.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $250.00 in premium on top of share movement. At $100.00, the client's combined position is **+$250.00** — the shares gain $0.00 and the options add +$250.00. Maximum gain is **+$250.00**. The premium adds a 2.5% enhancement over holding the stock alone. That represents a 1.7% return on the $15,000.00 capital at risk.

**Bullish**: If the stock rises above $100.00
At any price above $100.00, the client's gains are capped at **+$250.00** — the short call limits further upside. The trade-off: $250.00 in collected premium in exchange for giving up gains above $100.00. That represents a 1.7% return on the $15,000.00 capital at risk.

---

## Strategy: Long Put (ID=6, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position gains value as the stock falls. At $90.00, the position is **+$750.00**. Breakeven is $97.50 (2.5% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is **−$250.00**. Maximum gain is **+$9,750.00**. That represents a 3900.0% return on the $250.00 capital at risk.

**Bullish**: If the stock rises above $100.00
At any price above $100.00, losses are capped at **−$250.00**. That represents a 3900.0% return on the $250.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
At any price below $100.00, the client's losses are capped at **−$250.00** — the long $100.00 put provides a hard floor.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $250.00 option cost. At $100.00, the client's combined position is **−$250.00** — the shares gain $0.00 and the options cost −$250.00. The cost of protection: $250.00 (2.5% of the position) for a guaranteed loss limit at $100.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **+$750.00** — the shares gain +$1,000.00 and the options cost −$250.00. Breakeven is $102.50 (2.5% above spot). There is no cap on upside gains.

---

## Strategy: Short Put (ID=7, Code=CSPT)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position declines with the stock. At $90.00, the position is **−$750.00**. Breakeven is $97.50 (2.5% below spot). Maximum loss is **−$9,750.00**.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is **+$250.00**. Maximum gain is **+$250.00**. That represents a 2.5% return on the $10,000.00 capital at risk.

**Bullish**: If the stock rises above $100.00
At any price above $100.00, gains are capped at **+$250.00**. That represents a 2.5% return on the $10,000.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$1,750.00** — the shares lose −$1,000.00 and the options cost −$750.00. Breakeven is $98.75 (1.2% below spot). Maximum loss is **−$19,750.00**.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $250.00 in premium on top of share movement. At $100.00, the client's combined position is **+$250.00** — the shares gain $0.00 and the options add +$250.00. The premium adds a 2.5% enhancement over holding the stock alone.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **+$1,250.00** — the shares gain +$1,000.00 and the options add +$250.00. There is no cap on upside gains.

---

## Strategy: Covered Call (ID=8, Code=CCOV)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure, but the +$190.00 from the options cushions the move. At $98.00, the client's combined position is **−$10.00** — the shares lose −$200.00 and the options add +$190.00. Breakeven is $98.10 (1.9% below spot). There is no cap on downside risk. Without the options, the loss would be −$200.00.

**Stagnant**: If the stock stays between $100.00 and $108.00
This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$190.00** — the shares gain $0.00 and the options add +$190.00. Maximum gain is **+$990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 6.6% return on the $15,000.00 capital at risk.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at **+$990.00** — the short call limits further upside. The trade-off: $190.00 in collected premium in exchange for giving up gains above $108.00. That represents a 6.6% return on the $15,000.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure, but the +$190.00 from the options cushions the move. At $98.00, the client's combined position is **−$10.00** — the shares lose −$200.00 and the options add +$190.00. Breakeven is $98.10 (1.9% below spot). There is no cap on downside risk. Without the options, the loss would be −$200.00.

**Stagnant**: If the stock stays between $100.00 and $108.00
This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$190.00** — the shares gain $0.00 and the options add +$190.00. Maximum gain is **+$990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 6.6% return on the $15,000.00 capital at risk.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at **+$990.00** — the short call limits further upside. The trade-off: $190.00 in collected premium in exchange for giving up gains above $108.00. That represents a 6.6% return on the $15,000.00 capital at risk.

---

## Strategy: Covered Put (ID=9, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's gains are locked in at **+$990.00**. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable.

**Stagnant**: If the stock stays between $92.00 and $100.00
This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$190.00** — the shares gain $0.00 and the options add +$190.00. Maximum gain is **+$990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 8.7% return on the $11,390.00 capital at risk.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **−$10.00** — the shares lose −$200.00 and the options add +$190.00. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$990.00**. That represents a 8.7% return on the $11,390.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's gains are locked in at **+$990.00**. The client bought the stock below the protection floor, so even in a severe decline, the position is profitable.

**Stagnant**: If the stock stays between $92.00 and $100.00
This is the ideal range — the options expire worthless and the client keeps the full $190.00 in premium on top of share movement. At $100.00, the client's combined position is **+$190.00** — the shares gain $0.00 and the options add +$190.00. Maximum gain is **+$990.00**. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 8.7% return on the $11,390.00 capital at risk.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's losses increase as the stock rises. At $102.00, the client's combined position is **−$10.00** — the shares lose −$200.00 and the options add +$190.00. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$990.00**. That represents a 8.7% return on the $11,390.00 capital at risk.

---

## Strategy: Protective Call (ID=10, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $98.00, the client's combined position is **+$10.00** — the shares gain +$200.00 and the options cost −$190.00. Breakeven is $98.10 (1.9% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $100.00 and $108.00
Between $100.00 and $108.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is **−$190.00** — the shares gain $0.00 and the options cost −$190.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's losses are capped at **−$990.00**.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $98.00, the client's combined position is **+$10.00** — the shares gain +$200.00 and the options cost −$190.00. Breakeven is $98.10 (1.9% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $100.00 and $108.00
Between $100.00 and $108.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is **−$190.00** — the shares gain $0.00 and the options cost −$190.00.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's losses are capped at **−$990.00**.

---

## Strategy: Protective Put (ID=11, Code=PPRT)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's losses are capped at **−$990.00** — the long $92.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $100.00
Between $92.00 and $100.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is **−$190.00** — the shares gain $0.00 and the options cost −$190.00. The cost of protection: $190.00 (1.9% of the position) for a guaranteed loss limit at $92.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $102.00, the client's combined position is **+$10.00** — the shares gain +$200.00 and the options cost −$190.00. Breakeven is $101.90 (1.9% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's losses are capped at **−$990.00** — the long $92.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $100.00
Between $92.00 and $100.00, the client's position moves with the stock, reduced by the $190.00 option cost. At $100.00, the client's combined position is **−$190.00** — the shares gain $0.00 and the options cost −$190.00. The cost of protection: $190.00 (1.9% of the position) for a guaranteed loss limit at $92.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $102.00, the client's combined position is **+$10.00** — the shares gain +$200.00 and the options cost −$190.00. Breakeven is $101.90 (1.9% above spot). There is no cap on upside gains.

---

## Strategy: Collar (ID=12, Code=COL_EQ)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's losses are capped at **−$800.00** — the long $92.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 5.3% return on the $15,190.00 capital at risk.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at **+$800.00** — the short call limits further upside. The trade-off: downside protection below $92.00 in exchange for capping gains above $108.00. That represents a 5.3% return on the $15,190.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's losses are capped at **−$800.00** — the long $92.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 5.3% return on the $15,190.00 capital at risk.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at **+$800.00** — the short call limits further upside. The trade-off: downside protection below $92.00 in exchange for capping gains above $108.00. That represents a 5.3% return on the $15,190.00 capital at risk.

---

## Strategy: Bull Call Spread (ID=13, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, losses are capped at **−$800.00**.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, gains are capped at **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$2,300.00** — the shares lose −$1,500.00 and the options cost −$800.00. Maximum loss is **−$10,800.00**.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, reduced by the $800.00 option cost. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options cost $0.00. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$2,300.00** — the shares gain +$1,500.00 and the options add +$800.00. There is no cap on upside gains.

---

## Strategy: Bear Put Spread (ID=14, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, gains are locked in at **+$800.00**.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, losses are capped at **−$800.00**. That represents a 100.0% return on the $800.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure, but the +$800.00 from the options cushions the move. At $85.00, the client's combined position is **−$700.00** — the shares lose −$1,500.00 and the options add +$800.00. Breakeven is $92.00 (8.0% below spot). Maximum loss is **−$9,200.00**. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at **$0.00**. Breakevens are $92.00 (8.0% below spot) and $92.31 (7.7% below spot) and $94.31 (5.7% below spot) and $96.32 (3.7% below spot) and $97.32 (2.7% below spot) and $103.34 (3.3% above spot) and $105.35 (5.4% above spot) and $107.36 (7.4% above spot) and $108.00 (8.0% above spot). The cost of protection: $800.00 (8.0% of the position) for a guaranteed loss limit at $108.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$700.00** — the shares gain +$1,500.00 and the options cost −$800.00. Breakeven is $108.00 (8.0% above spot). There is no cap on upside gains.

---

## Strategy: Bear Call Spread (ID=15, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, gains are locked in at **+$800.00**.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, losses are capped at **−$800.00**. That represents a 100.0% return on the $800.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure, but the +$800.00 from the options cushions the move. At $85.00, the client's combined position is **−$700.00** — the shares lose −$1,500.00 and the options add +$800.00. Breakeven is $92.00 (8.0% below spot). Maximum loss is **−$9,200.00**. Without the options, the loss would be −$1,500.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $800.00 credit is retained. Breakevens are $92.00 (8.0% below spot) and $93.31 (6.7% below spot) and $96.32 (3.7% below spot) and $103.34 (3.3% above spot) and $106.35 (6.4% above spot) and $108.00 (8.0% above spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$700.00** — the shares gain +$1,500.00 and the options cost −$800.00. Breakeven is $108.00 (8.0% above spot). There is no cap on upside gains.

---

## Strategy: Bull Put Spread (ID=16, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, losses are capped at **−$800.00** — the long $92.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, gains are capped at **+$800.00**. That represents a 100.0% return on the $800.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$2,300.00** — the shares lose −$1,500.00 and the options cost −$800.00. Maximum loss is **−$10,800.00**.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, enhanced by the $800.00 net credit received. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$2,300.00** — the shares gain +$1,500.00 and the options add +$800.00. There is no cap on upside gains.

---

## Strategy: Call Ratio Backspread (ID=17, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, gains are locked in at **+$610.00**.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **−$190.00**. Breakeven is $98.10 (1.9% below spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the position rises with the stock. At $115.00, the position is **−$290.00**. Breakeven is $117.90 (17.9% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure, but the +$610.00 from the options cushions the move. At $85.00, the client's combined position is **−$890.00** — the shares lose −$1,500.00 and the options add +$610.00. Maximum loss is **−$9,390.00**. Without the options, the loss would be −$1,500.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at **−$190.00**. The premium adds a 1.9% enhancement over holding the stock alone.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$1,210.00** — the shares gain +$1,500.00 and the options cost −$290.00. Breakeven is $108.95 (9.0% above spot). There is no cap on upside gains.

---

## Strategy: Put Ratio Backspread (ID=18, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the position gains value as the stock falls. At $85.00, the position is **−$290.00**. Breakeven is $82.10 (17.9% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **−$190.00**. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$8,210.00**. That represents a 274.6% return on the $2,990.00 capital at risk.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, gains are capped at **+$610.00**. That represents a 274.6% return on the $2,990.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's losses are capped at **−$1,790.00** — the long $92.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, enhanced by the $610.00 net credit received. At $100.00, the client's combined position is **−$190.00** — the shares gain $0.00 and the options cost −$190.00. Breakeven is $100.95 (1.0% above spot). The premium adds a 1.9% enhancement over holding the stock alone.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$2,110.00** — the shares gain +$1,500.00 and the options add +$610.00. There is no cap on upside gains.

---

## Strategy: Call Ratio Spread (ID=19, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, losses are capped at **−$610.00**.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **+$190.00**. Breakeven is $98.10 (1.9% below spot). Maximum gain is **+$990.00**. That represents a 35.6% return on the $2,780.00 capital at risk.

**Bullish**: If the stock rises above $108.00
Above $108.00, losses increase as the stock rises. At $115.00, the position is **+$290.00**. Breakeven is $117.90 (17.9% above spot). Maximum gain is **+$990.00**. That represents a 35.6% return on the $2,780.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$2,110.00** — the shares lose −$1,500.00 and the options cost −$610.00. There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, reduced by the $610.00 option cost. At $100.00, the client's combined position is **+$190.00** — the shares gain $0.00 and the options add +$190.00. Breakeven is $99.05 (1.0% below spot). Maximum gain is **+$1,790.00**. That represents a 14.0% return on the $12,780.00 capital at risk.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at **+$1,790.00** — the short call limits further upside. The trade-off: $610.00 in collected premium in exchange for giving up gains above $108.00. That represents a 14.0% return on the $12,780.00 capital at risk.

---

## Strategy: Put Ratio Spread (ID=20, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the position declines with the stock. At $85.00, the position is **+$290.00**. Breakeven is $82.10 (17.9% below spot). Maximum loss is **−$8,210.00**.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position gains value as the stock moves lower. At $100.00, the position is **+$190.00**. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$990.00**. That represents a 12.1% return on the $8,210.00 capital at risk.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, losses are capped at **−$610.00**. That represents a 12.1% return on the $8,210.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure, but the +$290.00 from the options cushions the move. At $85.00, the client's combined position is **−$1,210.00** — the shares lose −$1,500.00 and the options add +$290.00. Breakeven is $91.05 (9.0% below spot). Maximum loss is **−$18,210.00**. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position captures its maximum gain of **+$190.00**. The cost of protection: $610.00 (6.1% of the position) for a guaranteed loss limit at $108.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$890.00** — the shares gain +$1,500.00 and the options cost −$610.00. There is no cap on upside gains.

---

## Strategy: Bull Call Ladder (ID=21, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $85.00
At any price below $85.00, losses are capped at **−$1,250.00**.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position gains value as the stock moves higher. At $100.00, the position is **+$250.00**. Breakeven is $97.50 (2.5% below spot). Maximum gain is **+$250.00**. That represents a 7.4% return on the $3,388.00 capital at risk.

**Bullish**: If the stock rises above $115.00
Above $115.00, losses increase as the stock rises. At $115.00, the position is **+$250.00**. Breakeven is $117.50 (17.5% above spot). Maximum gain is **+$250.00**. That represents a 7.4% return on the $3,388.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$2,750.00** — the shares lose −$1,500.00 and the options cost −$1,250.00. Maximum loss is **−$11,250.00**.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, reduced by the $1,250.00 option cost. At $100.00, the client's combined position is **+$250.00** — the shares gain $0.00 and the options add +$250.00. Breakeven is $98.75 (1.2% below spot). Maximum gain is **+$1,750.00**. That represents a 6.2% return on the $28,250.00 capital at risk.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, the client's gains are capped at **+$1,750.00** — the short call limits further upside. The trade-off: $1,250.00 in collected premium in exchange for giving up gains above $100.00. That represents a 6.2% return on the $28,250.00 capital at risk.

---

## Strategy: Bear Put Ladder (ID=22, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $85.00
Below $85.00, the position declines with the stock. At $85.00, the position is **+$250.00**. Breakeven is $82.50 (17.5% below spot). Maximum loss is **−$8,250.00**.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position gains value as the stock moves lower. At $100.00, the position is **+$250.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$250.00**. That represents a 3.0% return on the $8,250.00 capital at risk.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, losses are capped at **−$1,250.00**. That represents a 3.0% return on the $8,250.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure, but the +$250.00 from the options cushions the move. At $85.00, the client's combined position is **−$1,250.00** — the shares lose −$1,500.00 and the options add +$250.00. Maximum loss is **−$18,250.00**. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, reduced by the $1,250.00 option cost. At $100.00, the client's combined position is **+$250.00** — the shares gain $0.00 and the options add +$250.00. Breakeven is $97.50 (2.5% below spot). The cost of protection: $1,250.00 (12.5% of the position) for a guaranteed loss limit at $115.00.

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$250.00** — the shares gain +$1,500.00 and the options cost −$1,250.00. There is no cap on upside gains.

---

## Strategy: Bear Call Ladder (ID=23, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $85.00
At any price below $85.00, gains are locked in at **+$1,250.00**.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position gains value as the stock moves lower. At $100.00, the position is **−$250.00**. Breakeven is $97.50 (2.5% below spot).

**Bullish**: If the stock rises above $115.00
Above $115.00, the position rises with the stock. At $115.00, the position is **−$250.00**. Breakeven is $117.50 (17.5% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure, but the +$1,250.00 from the options cushions the move. At $85.00, the client's combined position is **−$250.00** — the shares lose −$1,500.00 and the options add +$1,250.00. Maximum loss is **−$8,750.00**. Without the options, the loss would be −$1,500.00.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, enhanced by the $1,250.00 net credit received. At $100.00, the client's combined position is **−$250.00** — the shares gain $0.00 and the options cost −$250.00. Breakeven is $102.50 (2.5% above spot). The premium adds a 2.5% enhancement over holding the stock alone.

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$1,250.00** — the shares gain +$1,500.00 and the options cost −$250.00. There is no cap on upside gains.

---

## Strategy: Bull Put Ladder (ID=24, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $85.00
Below $85.00, the position gains value as the stock falls. At $85.00, the position is **−$250.00**. Breakeven is $82.50 (17.5% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position gains value as the stock moves higher. At $100.00, the position is **−$250.00**. Breakeven is $102.50 (2.5% above spot). Maximum gain is **+$8,250.00**. That represents a 226.8% return on the $3,638.00 capital at risk.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, gains are capped at **+$1,250.00**. That represents a 226.8% return on the $3,638.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
At any price below $85.00, the client's losses are capped at **−$1,750.00** — the long $100.00 put provides a hard floor.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, enhanced by the $1,250.00 net credit received. At $100.00, the client's combined position is **−$250.00** — the shares gain $0.00 and the options cost −$250.00. Breakeven is $101.25 (1.2% above spot). The premium adds a 2.5% enhancement over holding the stock alone.

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$2,750.00** — the shares gain +$1,500.00 and the options add +$1,250.00. There is no cap on upside gains.

---

## Strategy: Long Call Butterfly (ID=25, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $85.00
At any price below $85.00, losses are capped at **−$1,276.00**.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, losses are capped at **−$1,276.00**. That represents a 17.6% return on the $1,276.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$2,776.00** — the shares lose −$1,500.00 and the options cost −$1,276.00. Maximum loss is **−$11,276.00**.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, reduced by the $1,276.00 option cost. At $100.00, the client's combined position is **+$224.00** — the shares gain $0.00 and the options add +$224.00. Breakeven is $98.88 (1.1% below spot).

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$224.00** — the shares gain +$1,500.00 and the options cost −$1,276.00. There is no cap on upside gains.

---

## Strategy: Long Put Butterfly (ID=26, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $85.00
At any price below $85.00, losses are capped at **−$1,276.00** — the long $85.00 put provides a hard floor.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, losses are capped at **−$1,276.00**. That represents a 17.6% return on the $1,276.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$2,776.00** — the shares lose −$1,500.00 and the options cost −$1,276.00. Maximum loss is **−$11,276.00**.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, reduced by the $1,276.00 option cost. At $100.00, the client's combined position is **+$224.00** — the shares gain $0.00 and the options add +$224.00. Breakeven is $98.88 (1.1% below spot). The cost of protection: $1,276.00 (12.8% of the position) for a guaranteed loss limit at $85.00.

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$224.00** — the shares gain +$1,500.00 and the options cost −$1,276.00. There is no cap on upside gains.

---

## Strategy: Iron Butterfly (ID=27, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $85.00
At any price below $85.00, losses are capped at **−$1,276.00** — the long $85.00 put provides a hard floor.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position reaches its maximum gain of **+$224.00** at $100.00 and deteriorates toward the zone boundaries. At $100.00, the position is **+$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$224.00**. That represents a 17.6% return on the $1,276.00 capital at risk.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, losses are capped at **−$1,276.00**. That represents a 17.6% return on the $1,276.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$2,776.00** — the shares lose −$1,500.00 and the options cost −$1,276.00. Maximum loss is **−$11,276.00**.

**Stagnant**: If the stock stays between $85.00 and $115.00
This is the ideal range — the options expire worthless and the client keeps the full $224.00 in premium on top of share movement. At $100.00, the client's combined position is **+$224.00** — the shares gain $0.00 and the options add +$224.00. Breakeven is $98.88 (1.1% below spot). The premium adds a 2.2% enhancement over holding the stock alone.

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$224.00** — the shares gain +$1,500.00 and the options cost −$1,276.00. There is no cap on upside gains.

---

## Strategy: Long Call Condor (ID=28, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00. Maximum loss is **−$1,020.00** at any price below $80.00. Breakeven is $90.20 (9.8% below spot).

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position captures its maximum gain of **+$180.00**. That represents a 4.1% return on the $4,380.00 capital at risk.

**Bullish**: If the stock rises above $108.00
Above $108.00, the short $108.00 call drives losses, but the long $120.00 call caps the damage. Maximum loss is **−$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot). That represents a 4.1% return on the $4,380.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$2,020.00** — the shares lose −$1,500.00 and the options cost −$520.00. Maximum loss is **−$11,020.00**.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, reduced by the $1,020.00 option cost. At $100.00, the client's combined position is **+$180.00** — the shares gain $0.00 and the options add +$180.00. Breakeven is $98.20 (1.8% below spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$980.00** — the shares gain +$1,500.00 and the options cost −$520.00. There is no cap on upside gains.

---

## Strategy: Long Put Condor (ID=29, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the short $92.00 put drives losses, but the long $80.00 put provides a hard floor. Maximum loss is **−$1,020.00** at any price below $80.00. Breakeven is $90.20 (9.8% below spot).

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position captures its maximum gain of **+$180.00**. That represents a 17.6% return on the $1,020.00 capital at risk.

**Bullish**: If the stock rises above $108.00
Above $108.00. Maximum loss is **−$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot). That represents a 17.6% return on the $1,020.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$2,020.00** — the shares lose −$1,500.00 and the options cost −$520.00. Maximum loss is **−$11,020.00**.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, reduced by the $1,020.00 option cost. At $100.00, the client's combined position is **+$180.00** — the shares gain $0.00 and the options add +$180.00. Breakeven is $98.20 (1.8% below spot). The cost of protection: $1,020.00 (10.2% of the position) for a guaranteed loss limit at $80.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$980.00** — the shares gain +$1,500.00 and the options cost −$520.00. There is no cap on upside gains.

---

## Strategy: Iron Condor (ID=30, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the short $92.00 put drives losses, but the long $80.00 put provides a hard floor. Maximum loss is **−$1,020.00** at any price below $80.00. Breakeven is $90.20 (9.8% below spot).

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $180.00 credit is retained. That represents a 6.5% return on the $2,780.00 capital at risk.

**Bullish**: If the stock rises above $108.00
Above $108.00, the short $108.00 call drives losses, but the long $120.00 call caps the damage. Maximum loss is **−$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot). That represents a 6.5% return on the $2,780.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$2,020.00** — the shares lose −$1,500.00 and the options cost −$520.00. Maximum loss is **−$11,020.00**.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the ideal range — the options expire worthless and the client keeps the full $180.00 in premium on top of share movement. At $100.00, the client's combined position is **+$180.00** — the shares gain $0.00 and the options add +$180.00. Breakeven is $98.20 (1.8% below spot). The premium adds a 1.8% enhancement over holding the stock alone.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$980.00** — the shares gain +$1,500.00 and the options cost −$520.00. There is no cap on upside gains.

---

## Strategy: Short Call Butterfly (ID=31, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $85.00
At any price below $85.00, gains are locked in at **+$1,276.00**.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents a 569.6% return on the $224.00 capital at risk.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, gains are capped at **+$1,276.00**. That represents a 569.6% return on the $224.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure, but the +$1,276.00 from the options cushions the move. At $85.00, the client's combined position is **−$224.00** — the shares lose −$1,500.00 and the options add +$1,276.00. Maximum loss is **−$8,724.00**. Without the options, the loss would be −$1,500.00.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, enhanced by the $1,276.00 net credit received. At $100.00, the client's combined position is **−$224.00** — the shares gain $0.00 and the options cost −$224.00. Breakeven is $101.12 (1.1% above spot). The premium adds a 2.2% enhancement over holding the stock alone.

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$2,776.00** — the shares gain +$1,500.00 and the options add +$1,276.00. There is no cap on upside gains.

---

## Strategy: Short Put Butterfly (ID=32, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $85.00
At any price below $85.00, gains are locked in at **+$1,276.00**.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents a 569.6% return on the $224.00 capital at risk.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, gains are capped at **+$1,276.00**. That represents a 569.6% return on the $224.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure, but the +$1,276.00 from the options cushions the move. At $85.00, the client's combined position is **−$224.00** — the shares lose −$1,500.00 and the options add +$1,276.00. Maximum loss is **−$8,724.00**. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, enhanced by the $1,276.00 net credit received. At $100.00, the client's combined position is **−$224.00** — the shares gain $0.00 and the options cost −$224.00. Breakeven is $101.12 (1.1% above spot). The premium adds a 2.2% enhancement over holding the stock alone.

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$2,776.00** — the shares gain +$1,500.00 and the options add +$1,276.00. There is no cap on upside gains.

---

## Strategy: Rev Iron Butterfly (ID=33, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $85.00
At any price below $85.00, gains are locked in at **+$1,276.00**.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the position reaches its maximum loss of **−$224.00** at $100.00 and improves toward the zone boundaries. At $100.00, the position is **−$224.00**. Breakevens are $97.76 (2.2% below spot) and $102.24 (2.2% above spot). Maximum gain is **+$1,276.00**. That represents a 569.6% return on the $224.00 capital at risk.

**Bullish**: If the stock rises above $115.00
At any price above $115.00, gains are capped at **+$1,276.00**. That represents a 569.6% return on the $224.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $85.00
Below $85.00, the client still has full downside exposure, but the +$1,276.00 from the options cushions the move. At $85.00, the client's combined position is **−$224.00** — the shares lose −$1,500.00 and the options add +$1,276.00. Maximum loss is **−$8,724.00**. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $85.00 and $115.00
Between $85.00 and $115.00, the client's position moves with the stock, reduced by the $224.00 option cost. At $100.00, the client's combined position is **−$224.00** — the shares gain $0.00 and the options cost −$224.00. Breakeven is $101.12 (1.1% above spot). The cost of protection: $224.00 (2.2% of the position) for a guaranteed loss limit at $100.00.

**Bullish**: If the stock rises above $115.00
Above $115.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$2,776.00** — the shares gain +$1,500.00 and the options add +$1,276.00. There is no cap on upside gains.

---

## Strategy: Short Call Condor (ID=34, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00. Maximum loss is **+$1,020.00** at any price below $80.00. Breakeven is $90.20 (9.8% below spot).

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at **−$180.00**.

**Bullish**: If the stock rises above $108.00
Above $108.00, the short $120.00 call drives losses, but the long $108.00 call caps the damage. Maximum loss is **+$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot).

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client's position loses value as the stock falls. At $85.00, the client's combined position is **−$980.00** — the shares lose −$1,500.00 and the options add +$520.00. Maximum loss is **−$8,980.00**. Without the options, the loss would be −$1,500.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, enhanced by the $1,020.00 net credit received. At $100.00, the client's combined position is **−$180.00** — the shares gain $0.00 and the options cost −$180.00. Breakeven is $101.80 (1.8% above spot). The premium adds a 1.8% enhancement over holding the stock alone.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$2,020.00** — the shares gain +$1,500.00 and the options add +$520.00. There is no cap on upside gains.

---

## Strategy: Short Put Condor (ID=35, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the short $80.00 put drives losses, but the long $92.00 put provides a hard floor. Maximum loss is **+$1,020.00** at any price below $80.00. Breakeven is $90.20 (9.8% below spot).

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at **−$180.00**. That represents a 19.6% return on the $5,200.00 capital at risk.

**Bullish**: If the stock rises above $108.00
Above $108.00. Maximum loss is **+$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot). That represents a 19.6% return on the $5,200.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client's position loses value as the stock falls. At $85.00, the client's combined position is **−$980.00** — the shares lose −$1,500.00 and the options add +$520.00. Maximum loss is **−$8,980.00**. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, enhanced by the $1,020.00 net credit received. At $100.00, the client's combined position is **−$180.00** — the shares gain $0.00 and the options cost −$180.00. Breakeven is $101.80 (1.8% above spot). The premium adds a 1.8% enhancement over holding the stock alone.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$2,020.00** — the shares gain +$1,500.00 and the options add +$520.00. There is no cap on upside gains.

---

## Strategy: Rev Iron Condor (ID=36, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the short $80.00 put drives losses, but the long $92.00 put provides a hard floor. Maximum loss is **+$1,020.00** at any price below $80.00. Breakeven is $90.20 (9.8% below spot).

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at **−$180.00**.

**Bullish**: If the stock rises above $108.00
Above $108.00, the short $120.00 call drives losses, but the long $108.00 call caps the damage. Maximum loss is **+$1,020.00** at any price above $120.00. Breakeven is $109.80 (9.8% above spot).

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client's position loses value as the stock falls. At $85.00, the client's combined position is **−$980.00** — the shares lose −$1,500.00 and the options add +$520.00. Maximum loss is **−$8,980.00**. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, reduced by the $180.00 option cost. At $100.00, the client's combined position is **−$180.00** — the shares gain $0.00 and the options cost −$180.00. Breakeven is $101.80 (1.8% above spot). The cost of protection: $180.00 (1.8% of the position) for a guaranteed loss limit at $92.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$2,020.00** — the shares gain +$1,500.00 and the options add +$520.00. There is no cap on upside gains.

---

## Strategy: Long Straddle (ID=37, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position gains value as the stock falls. At $90.00, the position is **+$500.00**. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is **−$500.00**.

**Bullish**: If the stock rises above $100.00
Above $100.00, the position rises with the stock. At $110.00, the position is **+$500.00**. Breakeven is $105.00 (5.0% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
At any price below $100.00, the client's losses are capped at **−$500.00** — the long $100.00 put provides a hard floor.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is **−$500.00** — the shares gain $0.00 and the options cost −$500.00. The cost of protection: $500.00 (5.0% of the position) for a guaranteed loss limit at $100.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **+$1,500.00** — the shares gain +$1,000.00 and the options add +$500.00. Breakeven is $102.50 (2.5% above spot). There is no cap on upside gains.

---

## Strategy: Short Straddle (ID=38, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position declines with the stock. At $90.00, the position is **−$500.00**. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is **+$500.00**. Maximum gain is **+$500.00**. That represents a 11.1% return on the $4,500.00 capital at risk.

**Bullish**: If the stock rises above $100.00
Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$500.00**. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents a 11.1% return on the $4,500.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$1,500.00** — the shares lose −$1,000.00 and the options cost −$500.00. Breakeven is $97.50 (2.5% below spot). Maximum loss is **−$19,500.00**.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 1.7% return on the $29,500.00 capital at risk.

**Bullish**: If the stock rises above $100.00
At any price above $100.00, the client's gains are capped at **+$500.00** — the short call limits further upside. The trade-off: $500.00 in collected premium in exchange for giving up gains above $100.00. That represents a 1.7% return on the $29,500.00 capital at risk.

---

## Strategy: Long Strangle (ID=39, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the position gains value as the stock falls. At $85.00, the position is **+$320.00**. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at **−$380.00**.

**Bullish**: If the stock rises above $108.00
Above $108.00, the position rises with the stock. At $115.00, the position is **+$320.00**. Breakeven is $111.80 (11.8% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's losses are capped at **−$1,180.00** — the long $92.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, reduced by the $380.00 option cost. At $100.00, the client's combined position is **−$380.00** — the shares gain $0.00 and the options cost −$380.00. Breakeven is $103.80 (3.8% above spot). The cost of protection: $380.00 (3.8% of the position) for a guaranteed loss limit at $92.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$1,820.00** — the shares gain +$1,500.00 and the options add +$320.00. There is no cap on upside gains.

---

## Strategy: Short Strangle (ID=40, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the position declines with the stock. At $85.00, the position is **−$320.00**. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $380.00 credit is retained. That represents a 13.7% return on the $2,780.00 capital at risk.

**Bullish**: If the stock rises above $108.00
Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$320.00**. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 13.7% return on the $2,780.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$1,820.00** — the shares lose −$1,500.00 and the options cost −$320.00. There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$380.00** — the shares gain $0.00 and the options add +$380.00. Breakeven is $96.20 (3.8% below spot). Maximum gain is **+$1,180.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 9.2% return on the $12,780.00 capital at risk.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at **+$1,180.00** — the short call limits further upside. The trade-off: $380.00 in collected premium in exchange for giving up gains above $108.00. That represents a 9.2% return on the $12,780.00 capital at risk.

---

## Strategy: Long Guts (ID=41, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the position gains value as the stock falls. At $85.00, the position is **+$320.00**. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at **−$380.00**.

**Bullish**: If the stock rises above $108.00
Above $108.00, the position rises with the stock. At $115.00, the position is **+$320.00**. Breakeven is $111.80 (11.8% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's losses are capped at **−$1,180.00** — the long $108.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, reduced by the $1,980.00 option cost. At $100.00, the client's combined position is **−$380.00** — the shares gain $0.00 and the options cost −$380.00. Breakeven is $103.80 (3.8% above spot). The cost of protection: $1,980.00 (19.8% of the position) for a guaranteed loss limit at $108.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$1,820.00** — the shares gain +$1,500.00 and the options add +$320.00. There is no cap on upside gains.

---

## Strategy: Short Guts (ID=42, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the position declines with the stock. At $85.00, the position is **−$320.00**. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,980.00 credit is retained. That represents a 6.4% return on the $5,980.00 capital at risk.

**Bullish**: If the stock rises above $108.00
Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$320.00**. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 6.4% return on the $5,980.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$1,820.00** — the shares lose −$1,500.00 and the options cost −$320.00. There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, enhanced by the $1,980.00 net credit received. At $100.00, the client's combined position is **+$380.00** — the shares gain $0.00 and the options add +$380.00. Breakeven is $96.20 (3.8% below spot). Maximum gain is **+$1,180.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 7.4% return on the $15,980.00 capital at risk.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at **+$1,180.00** — the short call limits further upside. The trade-off: $1,980.00 in collected premium in exchange for giving up gains above $92.00. That represents a 7.4% return on the $15,980.00 capital at risk.

---

## Strategy: Strip (ID=43, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position gains value as the stock falls. At $90.00, the position is **+$1,250.00**. Breakeven is $96.25 (3.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is **−$750.00**.

**Bullish**: If the stock rises above $100.00
Above $100.00, the position rises with the stock. At $110.00, the position is **+$250.00**. Breakeven is $107.50 (7.5% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is **+$250.00** — the shares lose −$1,000.00 and the options add +$1,250.00. Breakeven is $92.50 (7.5% below spot). There is no cap on downside risk. Without the put, a drop to $90.00 would mean a −$1,000.00 loss on the shares alone.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $750.00 option cost. At $100.00, the client's combined position is **−$750.00** — the shares gain $0.00 and the options cost −$750.00. The cost of protection: $750.00 (7.5% of the position) for a guaranteed loss limit at $100.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **+$1,250.00** — the shares gain +$1,000.00 and the options add +$250.00. Breakeven is $103.75 (3.8% above spot). There is no cap on upside gains.

---

## Strategy: Strap (ID=44, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position gains value as the stock falls. At $90.00, the position is **+$250.00**. Breakeven is $92.50 (7.5% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is **−$750.00**.

**Bullish**: If the stock rises above $100.00
Above $100.00, the position rises with the stock. At $110.00, the position is **+$1,250.00**. Breakeven is $103.75 (3.8% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
At any price below $100.00, the client's losses are capped at **−$750.00** — the long $100.00 put provides a hard floor.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $750.00 option cost. At $100.00, the client's combined position is **−$750.00** — the shares gain $0.00 and the options cost −$750.00. The cost of protection: $750.00 (7.5% of the position) for a guaranteed loss limit at $100.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **+$2,250.00** — the shares gain +$1,000.00 and the options add +$1,250.00. Breakeven is $102.50 (2.5% above spot). There is no cap on upside gains.

---

## Strategy: Covered Short Straddle (ID=45, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$1,500.00** — the shares lose −$1,000.00 and the options cost −$500.00. Breakeven is $97.50 (2.5% below spot). Maximum loss is **−$19,500.00**.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 1.7% return on the $29,500.00 capital at risk.

**Bullish**: If the stock rises above $100.00
At any price above $100.00, the client's gains are capped at **+$500.00** — the short call limits further upside. The trade-off: $500.00 in collected premium in exchange for giving up gains above $100.00. That represents a 1.7% return on the $29,500.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$1,500.00** — the shares lose −$1,000.00 and the options cost −$500.00. Breakeven is $97.50 (2.5% below spot). Maximum loss is **−$19,500.00**.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 1.7% return on the $29,500.00 capital at risk.

**Bullish**: If the stock rises above $100.00
At any price above $100.00, the client's gains are capped at **+$500.00** — the short call limits further upside. The trade-off: $500.00 in collected premium in exchange for giving up gains above $100.00. That represents a 1.7% return on the $29,500.00 capital at risk.

---

## Strategy: Covered Short Strangle (ID=46, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$1,820.00** — the shares lose −$1,500.00 and the options cost −$320.00. There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$380.00** — the shares gain $0.00 and the options add +$380.00. Breakeven is $96.20 (3.8% below spot). Maximum gain is **+$1,180.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 9.2% return on the $12,780.00 capital at risk.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at **+$1,180.00** — the short call limits further upside. The trade-off: $380.00 in collected premium in exchange for giving up gains above $108.00. That represents a 9.2% return on the $12,780.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$1,820.00** — the shares lose −$1,500.00 and the options cost −$320.00. There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the ideal range — the options expire worthless and the client keeps the full $380.00 in premium on top of share movement. At $100.00, the client's combined position is **+$380.00** — the shares gain $0.00 and the options add +$380.00. Breakeven is $96.20 (3.8% below spot). Maximum gain is **+$1,180.00**. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 9.2% return on the $12,780.00 capital at risk.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at **+$1,180.00** — the short call limits further upside. The trade-off: $380.00 in collected premium in exchange for giving up gains above $108.00. That represents a 9.2% return on the $12,780.00 capital at risk.

---

## Strategy: Long Box Spread (ID=47, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the short $92.00 put drives losses, but the long $108.00 put provides a hard floor. Maximum loss is **$0.00** at any price below $300.00. Breakevens are $0.00 (100.0% below spot) and $1.00 (99.0% below spot) and $2.01 (98.0% below spot) and $3.01 (97.0% below spot) and $4.01 (96.0% below spot) and $5.02 (95.0% below spot) and $6.02 (94.0% below spot) and $7.02 (93.0% below spot) and $8.03 (92.0% below spot) and $10.03 (90.0% below spot) and $12.04 (88.0% below spot) and $14.05 (86.0% below spot) and $16.05 (83.9% below spot) and $17.06 (82.9% below spot) and $18.06 (81.9% below spot) and $19.06 (80.9% below spot) and $20.07 (79.9% below spot) and $21.07 (78.9% below spot) and $22.07 (77.9% below spot) and $23.08 (76.9% below spot) and $24.08 (75.9% below spot) and $25.08 (74.9% below spot) and $26.09 (73.9% below spot) and $34.11 (65.9% below spot) and $35.12 (64.9% below spot) and $36.12 (63.9% below spot) and $37.12 (62.9% below spot) and $38.13 (61.9% below spot) and $39.13 (60.9% below spot) and $41.14 (58.9% below spot) and $42.14 (57.9% below spot) and $43.14 (56.9% below spot) and $44.15 (55.9% below spot) and $45.15 (54.8% below spot) and $46.15 (53.8% below spot) and $47.16 (52.8% below spot) and $48.16 (51.8% below spot) and $49.16 (50.8% below spot) and $52.68 (47.3% below spot) and $55.18 (44.8% below spot) and $57.19 (42.8% below spot) and $58.19 (41.8% below spot) and $59.20 (40.8% below spot) and $60.20 (39.8% below spot) and $61.20 (38.8% below spot) and $62.21 (37.8% below spot) and $63.21 (36.8% below spot) and $64.21 (35.8% below spot) and $65.22 (34.8% below spot) and $66.22 (33.8% below spot) and $67.22 (32.8% below spot) and $68.23 (31.8% below spot) and $69.23 (30.8% below spot) and $70.23 (29.8% below spot) and $71.74 (28.3% below spot) and $73.24 (26.8% below spot) and $75.25 (24.7% below spot) and $78.26 (21.7% below spot) and $82.27 (17.7% below spot) and $84.28 (15.7% below spot) and $86.29 (13.7% below spot) and $88.29 (11.7% below spot) and $92.00 (8.0% below spot).

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at **$0.00**. Breakevens are $92.00 (8.0% below spot) and $103.34 (3.3% above spot) and $108.00 (8.0% above spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the short $108.00 call drives losses, but the long $92.00 call caps the damage. Maximum loss is **$0.00** at any price above $0.00. Breakevens are $108.00 (8.0% above spot) and $108.36 (8.4% above spot) and $111.37 (11.4% above spot) and $112.37 (12.4% above spot) and $114.38 (14.4% above spot) and $116.39 (16.4% above spot) and $117.89 (17.9% above spot) and $120.40 (20.4% above spot) and $123.41 (23.4% above spot) and $124.41 (24.4% above spot) and $126.92 (26.9% above spot) and $128.43 (28.4% above spot) and $129.43 (29.4% above spot) and $130.43 (30.4% above spot) and $131.44 (31.4% above spot) and $132.44 (32.4% above spot) and $133.44 (33.4% above spot) and $134.45 (34.4% above spot) and $135.45 (35.5% above spot) and $136.45 (36.5% above spot) and $137.46 (37.5% above spot) and $138.46 (38.5% above spot) and $139.46 (39.5% above spot) and $140.47 (40.5% above spot) and $141.47 (41.5% above spot) and $142.47 (42.5% above spot) and $143.48 (43.5% above spot) and $144.48 (44.5% above spot) and $145.48 (45.5% above spot) and $147.99 (48.0% above spot) and $150.50 (50.5% above spot) and $151.51 (51.5% above spot) and $152.51 (52.5% above spot) and $153.51 (53.5% above spot) and $154.52 (54.5% above spot) and $155.52 (55.5% above spot) and $156.52 (56.5% above spot) and $157.53 (57.5% above spot) and $158.53 (58.5% above spot) and $159.53 (59.5% above spot) and $160.54 (60.5% above spot) and $161.54 (61.5% above spot) and $162.54 (62.5% above spot) and $163.55 (63.5% above spot) and $164.55 (64.5% above spot) and $165.55 (65.6% above spot) and $170.57 (70.6% above spot) and $171.57 (71.6% above spot) and $174.58 (74.6% above spot) and $175.59 (75.6% above spot) and $176.59 (76.6% above spot) and $177.59 (77.6% above spot) and $178.60 (78.6% above spot) and $179.60 (79.6% above spot) and $180.60 (80.6% above spot) and $181.61 (81.6% above spot) and $182.61 (82.6% above spot) and $183.61 (83.6% above spot) and $184.62 (84.6% above spot) and $186.62 (86.6% above spot) and $187.63 (87.6% above spot) and $189.63 (89.6% above spot) and $191.64 (91.6% above spot) and $192.64 (92.6% above spot) and $193.65 (93.6% above spot) and $194.65 (94.6% above spot) and $195.65 (95.7% above spot) and $196.66 (96.7% above spot) and $197.66 (97.7% above spot) and $198.66 (98.7% above spot) and $199.67 (99.7% above spot) and $200.67 (100.7% above spot) and $201.67 (101.7% above spot) and $202.68 (102.7% above spot) and $203.68 (103.7% above spot) and $204.68 (104.7% above spot) and $205.69 (105.7% above spot) and $206.69 (106.7% above spot) and $207.69 (107.7% above spot) and $208.70 (108.7% above spot) and $209.70 (109.7% above spot) and $210.70 (110.7% above spot) and $211.71 (111.7% above spot) and $212.71 (112.7% above spot) and $213.71 (113.7% above spot) and $214.72 (114.7% above spot) and $215.72 (115.7% above spot) and $216.72 (116.7% above spot) and $217.73 (117.7% above spot) and $218.73 (118.7% above spot) and $219.73 (119.7% above spot) and $220.74 (120.7% above spot) and $221.74 (121.7% above spot) and $222.74 (122.7% above spot) and $223.75 (123.7% above spot) and $224.75 (124.7% above spot) and $225.75 (125.8% above spot) and $226.76 (126.8% above spot) and $227.76 (127.8% above spot) and $228.76 (128.8% above spot) and $229.77 (129.8% above spot) and $230.77 (130.8% above spot) and $231.77 (131.8% above spot) and $232.78 (132.8% above spot) and $233.78 (133.8% above spot) and $234.78 (134.8% above spot) and $235.79 (135.8% above spot) and $236.79 (136.8% above spot) and $237.79 (137.8% above spot) and $238.80 (138.8% above spot) and $239.80 (139.8% above spot) and $240.80 (140.8% above spot) and $241.81 (141.8% above spot) and $242.81 (142.8% above spot) and $243.81 (143.8% above spot) and $244.82 (144.8% above spot) and $245.82 (145.8% above spot) and $246.82 (146.8% above spot) and $247.83 (147.8% above spot) and $248.83 (148.8% above spot) and $249.83 (149.8% above spot) and $250.84 (150.8% above spot) and $251.84 (151.8% above spot) and $252.84 (152.8% above spot) and $253.85 (153.8% above spot) and $254.85 (154.8% above spot) and $255.85 (155.9% above spot) and $256.86 (156.9% above spot) and $257.86 (157.9% above spot) and $258.86 (158.9% above spot) and $259.87 (159.9% above spot) and $260.87 (160.9% above spot) and $261.87 (161.9% above spot) and $262.88 (162.9% above spot) and $263.88 (163.9% above spot) and $264.88 (164.9% above spot) and $265.89 (165.9% above spot) and $266.89 (166.9% above spot) and $269.90 (169.9% above spot) and $270.90 (170.9% above spot) and $272.41 (172.4% above spot) and $273.91 (173.9% above spot) and $274.92 (174.9% above spot) and $275.92 (175.9% above spot) and $276.92 (176.9% above spot) and $277.93 (177.9% above spot) and $278.93 (178.9% above spot) and $279.93 (179.9% above spot) and $280.94 (180.9% above spot) and $281.94 (181.9% above spot) and $282.94 (182.9% above spot) and $283.95 (183.9% above spot) and $284.95 (184.9% above spot) and $285.95 (186.0% above spot) and $286.96 (187.0% above spot) and $287.96 (188.0% above spot) and $288.96 (189.0% above spot) and $289.97 (190.0% above spot) and $290.97 (191.0% above spot) and $291.97 (192.0% above spot) and $292.98 (193.0% above spot) and $293.98 (194.0% above spot) and $294.98 (195.0% above spot) and $295.99 (196.0% above spot) and $296.99 (197.0% above spot) and $297.99 (198.0% above spot) and $299.00 (199.0% above spot).

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options cost $0.00. Maximum loss is **−$10,000.00**.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, reduced by the $1,600.00 option cost. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options cost $0.00. Breakeven is $100.00 (0.0% above spot). The cost of protection: $1,600.00 (16.0% of the position) for a guaranteed loss limit at $108.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options cost $0.00. There is no cap on upside gains.

---

## Strategy: Short Box Spread (ID=48, Code=SPR)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the short $108.00 put drives losses, but the long $92.00 put provides a hard floor. Maximum loss is **$0.00** at any price below $300.00. Breakevens are $0.00 (100.0% below spot) and $1.00 (99.0% below spot) and $2.01 (98.0% below spot) and $3.01 (97.0% below spot) and $4.01 (96.0% below spot) and $5.02 (95.0% below spot) and $6.02 (94.0% below spot) and $7.02 (93.0% below spot) and $8.03 (92.0% below spot) and $10.03 (90.0% below spot) and $12.04 (88.0% below spot) and $14.05 (86.0% below spot) and $16.05 (83.9% below spot) and $17.06 (82.9% below spot) and $18.06 (81.9% below spot) and $19.06 (80.9% below spot) and $20.07 (79.9% below spot) and $21.07 (78.9% below spot) and $22.07 (77.9% below spot) and $23.08 (76.9% below spot) and $24.08 (75.9% below spot) and $25.08 (74.9% below spot) and $26.09 (73.9% below spot) and $34.11 (65.9% below spot) and $35.12 (64.9% below spot) and $36.12 (63.9% below spot) and $37.12 (62.9% below spot) and $38.13 (61.9% below spot) and $39.13 (60.9% below spot) and $41.14 (58.9% below spot) and $42.14 (57.9% below spot) and $43.14 (56.9% below spot) and $44.15 (55.9% below spot) and $45.15 (54.8% below spot) and $46.15 (53.8% below spot) and $47.16 (52.8% below spot) and $48.16 (51.8% below spot) and $49.16 (50.8% below spot) and $52.68 (47.3% below spot) and $55.18 (44.8% below spot) and $57.19 (42.8% below spot) and $58.19 (41.8% below spot) and $59.20 (40.8% below spot) and $60.20 (39.8% below spot) and $61.20 (38.8% below spot) and $62.21 (37.8% below spot) and $63.21 (36.8% below spot) and $64.21 (35.8% below spot) and $65.22 (34.8% below spot) and $66.22 (33.8% below spot) and $67.22 (32.8% below spot) and $68.23 (31.8% below spot) and $69.23 (30.8% below spot) and $70.23 (29.8% below spot) and $71.74 (28.3% below spot) and $73.24 (26.8% below spot) and $75.25 (24.7% below spot) and $78.26 (21.7% below spot) and $82.27 (17.7% below spot) and $84.28 (15.7% below spot) and $86.29 (13.7% below spot) and $88.29 (11.7% below spot) and $92.00 (8.0% below spot).

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,600.00 credit is retained. Breakevens are $92.00 (8.0% below spot) and $103.34 (3.3% above spot) and $108.00 (8.0% above spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the short $92.00 call drives losses, but the long $108.00 call caps the damage. Maximum loss is **$0.00** at any price above $0.00. Breakevens are $108.00 (8.0% above spot) and $108.36 (8.4% above spot) and $111.37 (11.4% above spot) and $112.37 (12.4% above spot) and $114.38 (14.4% above spot) and $116.39 (16.4% above spot) and $117.89 (17.9% above spot) and $120.40 (20.4% above spot) and $123.41 (23.4% above spot) and $124.41 (24.4% above spot) and $126.92 (26.9% above spot) and $128.43 (28.4% above spot) and $129.43 (29.4% above spot) and $130.43 (30.4% above spot) and $131.44 (31.4% above spot) and $132.44 (32.4% above spot) and $133.44 (33.4% above spot) and $134.45 (34.4% above spot) and $135.45 (35.5% above spot) and $136.45 (36.5% above spot) and $137.46 (37.5% above spot) and $138.46 (38.5% above spot) and $139.46 (39.5% above spot) and $140.47 (40.5% above spot) and $141.47 (41.5% above spot) and $142.47 (42.5% above spot) and $143.48 (43.5% above spot) and $144.48 (44.5% above spot) and $145.48 (45.5% above spot) and $147.99 (48.0% above spot) and $150.50 (50.5% above spot) and $151.51 (51.5% above spot) and $152.51 (52.5% above spot) and $153.51 (53.5% above spot) and $154.52 (54.5% above spot) and $155.52 (55.5% above spot) and $156.52 (56.5% above spot) and $157.53 (57.5% above spot) and $158.53 (58.5% above spot) and $159.53 (59.5% above spot) and $160.54 (60.5% above spot) and $161.54 (61.5% above spot) and $162.54 (62.5% above spot) and $163.55 (63.5% above spot) and $164.55 (64.5% above spot) and $165.55 (65.6% above spot) and $170.57 (70.6% above spot) and $171.57 (71.6% above spot) and $174.58 (74.6% above spot) and $175.59 (75.6% above spot) and $176.59 (76.6% above spot) and $177.59 (77.6% above spot) and $178.60 (78.6% above spot) and $179.60 (79.6% above spot) and $180.60 (80.6% above spot) and $181.61 (81.6% above spot) and $182.61 (82.6% above spot) and $183.61 (83.6% above spot) and $184.62 (84.6% above spot) and $186.62 (86.6% above spot) and $187.63 (87.6% above spot) and $189.63 (89.6% above spot) and $191.64 (91.6% above spot) and $192.64 (92.6% above spot) and $193.65 (93.6% above spot) and $194.65 (94.6% above spot) and $195.65 (95.7% above spot) and $196.66 (96.7% above spot) and $197.66 (97.7% above spot) and $198.66 (98.7% above spot) and $199.67 (99.7% above spot) and $200.67 (100.7% above spot) and $201.67 (101.7% above spot) and $202.68 (102.7% above spot) and $203.68 (103.7% above spot) and $204.68 (104.7% above spot) and $205.69 (105.7% above spot) and $206.69 (106.7% above spot) and $207.69 (107.7% above spot) and $208.70 (108.7% above spot) and $209.70 (109.7% above spot) and $210.70 (110.7% above spot) and $211.71 (111.7% above spot) and $212.71 (112.7% above spot) and $213.71 (113.7% above spot) and $214.72 (114.7% above spot) and $215.72 (115.7% above spot) and $216.72 (116.7% above spot) and $217.73 (117.7% above spot) and $218.73 (118.7% above spot) and $219.73 (119.7% above spot) and $220.74 (120.7% above spot) and $221.74 (121.7% above spot) and $222.74 (122.7% above spot) and $223.75 (123.7% above spot) and $224.75 (124.7% above spot) and $225.75 (125.8% above spot) and $226.76 (126.8% above spot) and $227.76 (127.8% above spot) and $228.76 (128.8% above spot) and $229.77 (129.8% above spot) and $230.77 (130.8% above spot) and $231.77 (131.8% above spot) and $232.78 (132.8% above spot) and $233.78 (133.8% above spot) and $234.78 (134.8% above spot) and $235.79 (135.8% above spot) and $236.79 (136.8% above spot) and $237.79 (137.8% above spot) and $238.80 (138.8% above spot) and $239.80 (139.8% above spot) and $240.80 (140.8% above spot) and $241.81 (141.8% above spot) and $242.81 (142.8% above spot) and $243.81 (143.8% above spot) and $244.82 (144.8% above spot) and $245.82 (145.8% above spot) and $246.82 (146.8% above spot) and $247.83 (147.8% above spot) and $248.83 (148.8% above spot) and $249.83 (149.8% above spot) and $250.84 (150.8% above spot) and $251.84 (151.8% above spot) and $252.84 (152.8% above spot) and $253.85 (153.8% above spot) and $254.85 (154.8% above spot) and $255.85 (155.9% above spot) and $256.86 (156.9% above spot) and $257.86 (157.9% above spot) and $258.86 (158.9% above spot) and $259.87 (159.9% above spot) and $260.87 (160.9% above spot) and $261.87 (161.9% above spot) and $262.88 (162.9% above spot) and $263.88 (163.9% above spot) and $264.88 (164.9% above spot) and $265.89 (165.9% above spot) and $266.89 (166.9% above spot) and $269.90 (169.9% above spot) and $270.90 (170.9% above spot) and $272.41 (172.4% above spot) and $273.91 (173.9% above spot) and $274.92 (174.9% above spot) and $275.92 (175.9% above spot) and $276.92 (176.9% above spot) and $277.93 (177.9% above spot) and $278.93 (178.9% above spot) and $279.93 (179.9% above spot) and $280.94 (180.9% above spot) and $281.94 (181.9% above spot) and $282.94 (182.9% above spot) and $283.95 (183.9% above spot) and $284.95 (184.9% above spot) and $285.95 (186.0% above spot) and $286.96 (187.0% above spot) and $287.96 (188.0% above spot) and $288.96 (189.0% above spot) and $289.97 (190.0% above spot) and $290.97 (191.0% above spot) and $291.97 (192.0% above spot) and $292.98 (193.0% above spot) and $293.98 (194.0% above spot) and $294.98 (195.0% above spot) and $295.99 (196.0% above spot) and $296.99 (197.0% above spot) and $297.99 (198.0% above spot) and $299.00 (199.0% above spot).

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure, but the $0.00 from the options cushions the move. At $85.00, the client's combined position is **−$1,500.00** — the shares lose −$1,500.00 and the options add $0.00. Maximum loss is **−$10,000.00**.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock, enhanced by the $1,600.00 net credit received. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$1,500.00** — the shares gain +$1,500.00 and the options add $0.00. There is no cap on upside gains.

---

## Strategy: Synthetic Long Stock (ID=49, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position declines with the stock. At $90.00, the position is **−$1,000.00**. Breakeven is $100.00 (0.0% above spot). Maximum loss is **−$10,000.00**.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $100.00
Above $100.00, the position rises with the stock. At $110.00, the position is **+$1,000.00**. Breakeven is $100.00 (0.0% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$2,000.00** — the shares lose −$1,000.00 and the options cost −$1,000.00. Breakeven is $100.00 (0.0% above spot). Maximum loss is **−$20,000.00**.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **+$2,000.00** — the shares gain +$1,000.00 and the options add +$1,000.00. Breakeven is $100.00 (0.0% above spot). There is no cap on upside gains.

---

## Strategy: Synthetic Short Stock (ID=50, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position gains value as the stock falls. At $90.00, the position is **+$1,000.00**. Breakeven is $100.00 (0.0% above spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the position is roughly flat. At $100.00, the position is **$0.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk.

**Bullish**: If the stock rises above $100.00
Above $100.00, losses increase as the stock rises. At $110.00, the position is **−$1,000.00**. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$10,000.00**. That represents a 444.4% return on the $2,250.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, but the long $100.00 put provides a hard floor. Maximum loss is **$0.00** at any price below $300.00. Breakevens are $0.00 (100.0% below spot) and $1.00 (99.0% below spot) and $2.01 (98.0% below spot) and $3.01 (97.0% below spot) and $4.01 (96.0% below spot) and $5.02 (95.0% below spot) and $6.02 (94.0% below spot) and $7.02 (93.0% below spot) and $8.03 (92.0% below spot) and $9.03 (91.0% below spot) and $10.03 (90.0% below spot) and $11.04 (89.0% below spot) and $12.04 (88.0% below spot) and $13.04 (87.0% below spot) and $14.05 (86.0% below spot) and $15.05 (84.9% below spot) and $17.06 (82.9% below spot) and $18.06 (81.9% below spot) and $19.06 (80.9% below spot) and $20.07 (79.9% below spot) and $21.07 (78.9% below spot) and $22.07 (77.9% below spot) and $23.08 (76.9% below spot) and $24.08 (75.9% below spot) and $25.08 (74.9% below spot) and $26.09 (73.9% below spot) and $27.09 (72.9% below spot) and $28.09 (71.9% below spot) and $29.10 (70.9% below spot) and $30.10 (69.9% below spot) and $31.10 (68.9% below spot) and $32.11 (67.9% below spot) and $33.11 (66.9% below spot) and $34.11 (65.9% below spot) and $35.12 (64.9% below spot) and $36.12 (63.9% below spot) and $37.12 (62.9% below spot) and $38.13 (61.9% below spot) and $39.13 (60.9% below spot) and $40.13 (59.9% below spot) and $41.14 (58.9% below spot) and $42.14 (57.9% below spot) and $43.14 (56.9% below spot) and $44.15 (55.9% below spot) and $45.15 (54.8% below spot) and $46.15 (53.8% below spot) and $47.16 (52.8% below spot) and $48.16 (51.8% below spot) and $49.16 (50.8% below spot) and $50.17 (49.8% below spot) and $51.17 (48.8% below spot) and $52.17 (47.8% below spot) and $53.18 (46.8% below spot) and $54.18 (45.8% below spot) and $55.18 (44.8% below spot) and $56.19 (43.8% below spot) and $58.19 (41.8% below spot) and $59.20 (40.8% below spot) and $60.20 (39.8% below spot) and $61.20 (38.8% below spot) and $62.21 (37.8% below spot) and $63.21 (36.8% below spot) and $64.21 (35.8% below spot) and $65.22 (34.8% below spot) and $66.22 (33.8% below spot) and $67.22 (32.8% below spot) and $68.23 (31.8% below spot) and $69.23 (30.8% below spot) and $70.23 (29.8% below spot) and $71.24 (28.8% below spot) and $72.24 (27.8% below spot) and $73.24 (26.8% below spot) and $74.25 (25.8% below spot) and $75.25 (24.7% below spot) and $76.25 (23.7% below spot) and $77.26 (22.7% below spot) and $78.26 (21.7% below spot) and $79.26 (20.7% below spot) and $80.27 (19.7% below spot) and $81.27 (18.7% below spot) and $82.27 (17.7% below spot) and $83.28 (16.7% below spot) and $84.28 (15.7% below spot) and $85.28 (14.7% below spot) and $86.29 (13.7% below spot) and $87.29 (12.7% below spot) and $88.29 (11.7% below spot) and $89.30 (10.7% below spot) and $90.30 (9.7% below spot) and $91.30 (8.7% below spot) and $92.31 (7.7% below spot) and $93.31 (6.7% below spot) and $94.31 (5.7% below spot) and $95.32 (4.7% below spot) and $96.32 (3.7% below spot) and $97.32 (2.7% below spot) and $98.33 (1.7% below spot) and $99.33 (0.7% below spot) and $100.00 (0.0% above spot). The client bought the stock below the protection floor, so even in a severe decline, the position is profitable.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **$0.00**.

**Bullish**: If the stock rises above $100.00
Above $100.00, the short $100.00 call drives losses. Maximum loss is **$0.00** at any price above $0.00. Breakevens are $100.00 (0.0% above spot) and $100.33 (0.3% above spot) and $101.34 (1.3% above spot) and $102.34 (2.3% above spot) and $103.34 (3.3% above spot) and $104.35 (4.3% above spot) and $105.35 (5.4% above spot) and $106.35 (6.4% above spot) and $107.36 (7.4% above spot) and $108.36 (8.4% above spot) and $109.36 (9.4% above spot) and $110.37 (10.4% above spot) and $111.37 (11.4% above spot) and $112.37 (12.4% above spot) and $113.38 (13.4% above spot) and $114.38 (14.4% above spot) and $115.38 (15.4% above spot) and $116.39 (16.4% above spot) and $117.39 (17.4% above spot) and $118.39 (18.4% above spot) and $119.40 (19.4% above spot) and $120.40 (20.4% above spot) and $122.41 (22.4% above spot) and $123.41 (23.4% above spot) and $124.41 (24.4% above spot) and $125.42 (25.4% above spot) and $126.42 (26.4% above spot) and $127.42 (27.4% above spot) and $128.43 (28.4% above spot) and $129.43 (29.4% above spot) and $130.43 (30.4% above spot) and $131.44 (31.4% above spot) and $132.44 (32.4% above spot) and $133.44 (33.4% above spot) and $134.45 (34.4% above spot) and $135.45 (35.5% above spot) and $136.45 (36.5% above spot) and $137.46 (37.5% above spot) and $138.46 (38.5% above spot) and $139.46 (39.5% above spot) and $140.47 (40.5% above spot) and $141.47 (41.5% above spot) and $142.47 (42.5% above spot) and $143.48 (43.5% above spot) and $144.48 (44.5% above spot) and $145.48 (45.5% above spot) and $146.49 (46.5% above spot) and $147.49 (47.5% above spot) and $148.49 (48.5% above spot) and $149.50 (49.5% above spot) and $150.50 (50.5% above spot) and $151.51 (51.5% above spot) and $152.51 (52.5% above spot) and $153.51 (53.5% above spot) and $154.52 (54.5% above spot) and $155.52 (55.5% above spot) and $156.52 (56.5% above spot) and $157.53 (57.5% above spot) and $158.53 (58.5% above spot) and $159.53 (59.5% above spot) and $160.54 (60.5% above spot) and $161.54 (61.5% above spot) and $162.54 (62.5% above spot) and $163.55 (63.5% above spot) and $164.55 (64.5% above spot) and $165.55 (65.6% above spot) and $166.56 (66.6% above spot) and $167.56 (67.6% above spot) and $168.56 (68.6% above spot) and $169.57 (69.6% above spot) and $170.57 (70.6% above spot) and $171.57 (71.6% above spot) and $172.58 (72.6% above spot) and $173.58 (73.6% above spot) and $174.58 (74.6% above spot) and $175.59 (75.6% above spot) and $176.59 (76.6% above spot) and $177.59 (77.6% above spot) and $178.60 (78.6% above spot) and $179.60 (79.6% above spot) and $180.60 (80.6% above spot) and $181.61 (81.6% above spot) and $183.61 (83.6% above spot) and $184.62 (84.6% above spot) and $185.62 (85.6% above spot) and $186.62 (86.6% above spot) and $187.63 (87.6% above spot) and $188.63 (88.6% above spot) and $189.63 (89.6% above spot) and $190.64 (90.6% above spot) and $191.64 (91.6% above spot) and $192.64 (92.6% above spot) and $193.65 (93.6% above spot) and $194.65 (94.6% above spot) and $195.65 (95.7% above spot) and $196.66 (96.7% above spot) and $197.66 (97.7% above spot) and $198.66 (98.7% above spot) and $199.67 (99.7% above spot) and $200.67 (100.7% above spot) and $201.67 (101.7% above spot) and $202.68 (102.7% above spot) and $203.68 (103.7% above spot) and $204.68 (104.7% above spot) and $205.69 (105.7% above spot) and $206.69 (106.7% above spot) and $207.69 (107.7% above spot) and $208.70 (108.7% above spot) and $209.70 (109.7% above spot) and $210.70 (110.7% above spot) and $211.71 (111.7% above spot) and $212.71 (112.7% above spot) and $213.71 (113.7% above spot) and $214.72 (114.7% above spot) and $215.72 (115.7% above spot) and $216.72 (116.7% above spot) and $217.73 (117.7% above spot) and $218.73 (118.7% above spot) and $219.73 (119.7% above spot) and $220.74 (120.7% above spot) and $221.74 (121.7% above spot) and $222.74 (122.7% above spot) and $223.75 (123.7% above spot) and $224.75 (124.7% above spot) and $225.75 (125.8% above spot) and $226.76 (126.8% above spot) and $227.76 (127.8% above spot) and $228.76 (128.8% above spot) and $229.77 (129.8% above spot) and $230.77 (130.8% above spot) and $231.77 (131.8% above spot) and $232.78 (132.8% above spot) and $233.78 (133.8% above spot) and $234.78 (134.8% above spot) and $235.79 (135.8% above spot) and $236.79 (136.8% above spot) and $237.79 (137.8% above spot) and $238.80 (138.8% above spot) and $239.80 (139.8% above spot) and $240.80 (140.8% above spot) and $241.81 (141.8% above spot) and $242.81 (142.8% above spot) and $243.81 (143.8% above spot) and $244.82 (144.8% above spot) and $245.82 (145.8% above spot) and $246.82 (146.8% above spot) and $247.83 (147.8% above spot) and $248.83 (148.8% above spot) and $249.83 (149.8% above spot) and $250.84 (150.8% above spot) and $251.84 (151.8% above spot) and $252.84 (152.8% above spot) and $253.85 (153.8% above spot) and $254.85 (154.8% above spot) and $255.85 (155.9% above spot) and $256.86 (156.9% above spot) and $257.86 (157.9% above spot) and $258.86 (158.9% above spot) and $259.87 (159.9% above spot) and $260.87 (160.9% above spot) and $261.87 (161.9% above spot) and $262.88 (162.9% above spot) and $263.88 (163.9% above spot) and $264.88 (164.9% above spot) and $265.89 (165.9% above spot) and $266.89 (166.9% above spot) and $267.89 (167.9% above spot) and $268.90 (168.9% above spot) and $269.90 (169.9% above spot) and $270.90 (170.9% above spot) and $271.91 (171.9% above spot) and $272.91 (172.9% above spot) and $273.91 (173.9% above spot) and $274.92 (174.9% above spot) and $275.92 (175.9% above spot) and $276.92 (176.9% above spot) and $277.93 (177.9% above spot) and $278.93 (178.9% above spot) and $279.93 (179.9% above spot) and $280.94 (180.9% above spot) and $281.94 (181.9% above spot) and $282.94 (182.9% above spot) and $283.95 (183.9% above spot) and $284.95 (184.9% above spot) and $285.95 (186.0% above spot) and $286.96 (187.0% above spot) and $287.96 (188.0% above spot) and $288.96 (189.0% above spot) and $289.97 (190.0% above spot) and $290.97 (191.0% above spot) and $291.97 (192.0% above spot) and $292.98 (193.0% above spot) and $293.98 (194.0% above spot) and $294.98 (195.0% above spot) and $295.99 (196.0% above spot) and $296.99 (197.0% above spot) and $297.99 (198.0% above spot) and $299.00 (199.0% above spot). The trade-off: downside protection below $100.00 in exchange for capping gains above $100.00.

---

## Strategy: Long Combo (ID=51, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the position declines with the stock. At $85.00, the position is **−$700.00**. Breakeven is $92.00 (8.0% below spot). Maximum loss is **−$9,200.00**.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position captures its maximum gain of **$0.00**. Breakevens are $92.00 (8.0% below spot) and $92.31 (7.7% below spot) and $93.31 (6.7% below spot) and $94.31 (5.7% below spot) and $95.32 (4.7% below spot) and $96.32 (3.7% below spot) and $97.32 (2.7% below spot) and $98.33 (1.7% below spot) and $99.33 (0.7% below spot) and $100.33 (0.3% above spot) and $101.34 (1.3% above spot) and $102.34 (2.3% above spot) and $103.34 (3.3% above spot) and $104.35 (4.3% above spot) and $105.35 (5.4% above spot) and $106.35 (6.4% above spot) and $107.36 (7.4% above spot) and $108.00 (8.0% above spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the position rises with the stock. At $115.00, the position is **+$700.00**. Breakeven is $108.00 (8.0% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$2,200.00** — the shares lose −$1,500.00 and the options cost −$700.00. Maximum loss is **−$19,200.00**.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot).

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$2,200.00** — the shares gain +$1,500.00 and the options add +$700.00. There is no cap on upside gains.

---

## Strategy: Short Combo (ID=52, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the position gains value as the stock falls. At $85.00, the position is **+$700.00**. Breakeven is $92.00 (8.0% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the position captures its maximum gain of **$0.00**. Breakevens are $92.00 (8.0% below spot) and $92.31 (7.7% below spot) and $93.31 (6.7% below spot) and $94.31 (5.7% below spot) and $95.32 (4.7% below spot) and $96.32 (3.7% below spot) and $97.32 (2.7% below spot) and $98.33 (1.7% below spot) and $99.33 (0.7% below spot) and $100.33 (0.3% above spot) and $101.34 (1.3% above spot) and $102.34 (2.3% above spot) and $103.34 (3.3% above spot) and $104.35 (4.3% above spot) and $105.35 (5.4% above spot) and $106.35 (6.4% above spot) and $107.36 (7.4% above spot) and $108.00 (8.0% above spot). That represents a 661.9% return on the $1,390.00 capital at risk.

**Bullish**: If the stock rises above $108.00
Above $108.00, losses increase as the stock rises. At $115.00, the position is **−$700.00**. Breakeven is $108.00 (8.0% above spot). Maximum gain is **+$9,200.00**. That represents a 661.9% return on the $1,390.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
At any price below $92.00, the client's losses are capped at **−$800.00** — the long $92.00 put provides a hard floor.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **+$800.00**. That represents a 5.3% return on the $15,190.00 capital at risk.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, the client's gains are capped at **+$800.00** — the short call limits further upside. The trade-off: downside protection below $92.00 in exchange for capping gains above $108.00. That represents a 5.3% return on the $15,190.00 capital at risk.

---

## Strategy: L. Call Syn. Straddle (ID=53, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is **+$500.00** — the shares gain +$1,000.00 and the options cost −$500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is **−$500.00** — the shares gain $0.00 and the options cost −$500.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **+$500.00** — the shares lose −$1,000.00 and the options add +$1,500.00. Breakeven is $105.00 (5.0% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is **+$500.00** — the shares gain +$1,000.00 and the options cost −$500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is **−$500.00** — the shares gain $0.00 and the options cost −$500.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **+$500.00** — the shares lose −$1,000.00 and the options add +$1,500.00. Breakeven is $105.00 (5.0% above spot). There is no cap on upside gains.

---

## Strategy: L. Put Syn. Straddle (ID=54, Code=PPRT)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is **+$500.00** — the shares lose −$1,000.00 and the options add +$1,500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk. Without the put, a drop to $90.00 would mean a −$1,000.00 loss on the shares alone.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is **−$500.00** — the shares gain $0.00 and the options cost −$500.00. The cost of protection: $500.00 (5.0% of the position) for a guaranteed loss limit at $100.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **+$500.00** — the shares gain +$1,000.00 and the options cost −$500.00. Breakeven is $105.00 (5.0% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client's position gains value as the stock falls. At $90.00, the client's combined position is **+$500.00** — the shares lose −$1,000.00 and the options add +$1,500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk. Without the put, a drop to $90.00 would mean a −$1,000.00 loss on the shares alone.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock, reduced by the $500.00 option cost. At $100.00, the client's combined position is **−$500.00** — the shares gain $0.00 and the options cost −$500.00. The cost of protection: $500.00 (5.0% of the position) for a guaranteed loss limit at $100.00.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's position rises with the stock. At $110.00, the client's combined position is **+$500.00** — the shares gain +$1,000.00 and the options cost −$500.00. Breakeven is $105.00 (5.0% above spot). There is no cap on upside gains.

---

## Strategy: S. Call Syn. Straddle (ID=55, Code=CCOV)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure, but the +$500.00 from the options cushions the move. At $90.00, the client's combined position is **−$500.00** — the shares lose −$1,000.00 and the options add +$500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk. Without the options, the loss would be −$1,000.00.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 3.3% return on the $15,000.00 capital at risk.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$500.00** — the shares gain +$1,000.00 and the options cost −$1,500.00. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents a 3.3% return on the $15,000.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure, but the +$500.00 from the options cushions the move. At $90.00, the client's combined position is **−$500.00** — the shares lose −$1,000.00 and the options add +$500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk. Without the options, the loss would be −$1,000.00.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 3.3% return on the $15,000.00 capital at risk.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$500.00** — the shares gain +$1,000.00 and the options cost −$1,500.00. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents a 3.3% return on the $15,000.00 capital at risk.

---

## Strategy: S. Put Syn. Straddle (ID=56, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$500.00** — the shares gain +$1,000.00 and the options cost −$1,500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 3.4% return on the $14,500.00 capital at risk.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$500.00** — the shares lose −$1,000.00 and the options add +$500.00. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents a 3.4% return on the $14,500.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $90.00, the client's combined position is **−$500.00** — the shares gain +$1,000.00 and the options cost −$1,500.00. Breakeven is $95.00 (5.0% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays near $100.00
This is the ideal range — the options expire worthless and the client keeps the full $500.00 in premium on top of share movement. At $100.00, the client's combined position is **+$500.00** — the shares gain $0.00 and the options add +$500.00. Maximum gain is **+$500.00**. The premium adds a 5.0% enhancement over holding the stock alone. That represents a 3.4% return on the $14,500.00 capital at risk.

**Bullish**: If the stock rises above $100.00
Above $100.00, the client's losses increase as the stock rises. At $110.00, the client's combined position is **−$500.00** — the shares lose −$1,000.00 and the options add +$500.00. Breakeven is $105.00 (5.0% above spot). Maximum gain is **+$500.00**. That represents a 3.4% return on the $14,500.00 capital at risk.

---

## Strategy: L. Call Syn. Strangle (ID=57, Code=LNG)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **+$320.00** — the shares gain +$1,500.00 and the options cost −$1,180.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at **−$380.00**.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$320.00** — the shares lose −$1,500.00 and the options add +$1,820.00. Breakeven is $111.80 (11.8% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **+$320.00** — the shares gain +$1,500.00 and the options cost −$1,180.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at **−$380.00**.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$320.00** — the shares lose −$1,500.00 and the options add +$1,820.00. Breakeven is $111.80 (11.8% above spot). There is no cap on upside gains.

---

## Strategy: L. Put Syn. Strangle (ID=58, Code=PPRT)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **+$320.00** — the shares lose −$1,500.00 and the options add +$1,820.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at **−$380.00**. The cost of protection: $1,180.00 (11.8% of the position) for a guaranteed loss limit at $92.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$320.00** — the shares gain +$1,500.00 and the options cost −$1,180.00. Breakeven is $111.80 (11.8% above spot). There is no cap on upside gains.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client's position gains value as the stock falls. At $85.00, the client's combined position is **+$320.00** — the shares lose −$1,500.00 and the options add +$1,820.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk. Without the put, a drop to $85.00 would mean a −$1,500.00 loss on the shares alone.

**Stagnant**: If the stock stays between $92.00 and $108.00
Between $92.00 and $108.00, losses are stable at **−$380.00**. The cost of protection: $1,180.00 (11.8% of the position) for a guaranteed loss limit at $92.00.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$320.00** — the shares gain +$1,500.00 and the options cost −$1,180.00. Breakeven is $111.80 (11.8% above spot). There is no cap on upside gains.

---

## Strategy: S. Call Syn. Strangle (ID=59, Code=CCOV)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure, but the +$1,180.00 from the options cushions the move. At $85.00, the client's combined position is **−$320.00** — the shares lose −$1,500.00 and the options add +$1,180.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk. Without the options, the loss would be −$1,500.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 2.5% return on the $15,000.00 capital at risk.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$320.00** — the shares gain +$1,500.00 and the options cost −$1,820.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 2.5% return on the $15,000.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure, but the +$1,180.00 from the options cushions the move. At $85.00, the client's combined position is **−$320.00** — the shares lose −$1,500.00 and the options add +$1,180.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk. Without the options, the loss would be −$1,500.00.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 2.5% return on the $15,000.00 capital at risk.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$320.00** — the shares gain +$1,500.00 and the options cost −$1,820.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 2.5% return on the $15,000.00 capital at risk.

---

## Strategy: S. Put Syn. Strangle (ID=60, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$320.00** — the shares gain +$1,500.00 and the options cost −$1,820.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 2.6% return on the $14,380.00 capital at risk.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$320.00** — the shares lose −$1,500.00 and the options add +$1,180.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 2.6% return on the $14,380.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure. At $85.00, the client's combined position is **−$320.00** — the shares gain +$1,500.00 and the options cost −$1,820.00. Breakeven is $88.20 (11.8% below spot). There is no cap on downside risk.

**Stagnant**: If the stock stays between $92.00 and $108.00
This is the target outcome. As long as the stock stays between $92.00 and $108.00 — roughly 8.0% down to 8.0% up from here — all options expire worthless and the full $1,180.00 credit is retained. The premium adds a 3.8% enhancement over holding the stock alone. That represents a 2.6% return on the $14,380.00 capital at risk.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's losses increase as the stock rises. At $115.00, the client's combined position is **−$320.00** — the shares lose −$1,500.00 and the options add +$1,180.00. Breakeven is $111.80 (11.8% above spot). Maximum gain is **+$380.00**. That represents a 2.6% return on the $14,380.00 capital at risk.

---

## Strategy: Syn. Covered Call (ID=61, Code=CSPT)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, the position declines with the stock. At $98.00, the position is **−$10.00**. Breakeven is $98.10 (1.9% below spot). Maximum loss is **−$9,810.00**.

**Stagnant**: If the stock stays between $100.00 and $108.00
Between $100.00 and $108.00, the position gains value as the stock moves higher. At $100.00, the position is **+$190.00**. Maximum gain is **+$990.00**. That represents a 9.2% return on the $10,800.00 capital at risk.

**Bullish**: If the stock rises above $108.00
At any price above $108.00, gains are capped at **+$990.00**. That represents a 9.2% return on the $10,800.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, the client still has full downside exposure. At $98.00, the client's combined position is **−$210.00** — the shares lose −$200.00 and the options cost −$10.00. Breakeven is $99.05 (1.0% below spot). Maximum loss is **−$19,810.00**.

**Stagnant**: If the stock stays between $100.00 and $108.00
Between $100.00 and $108.00, the client's position moves with the stock, enhanced by the $990.00 net credit received. At $100.00, the client's combined position is **+$190.00** — the shares lose $0.00 and the options add +$190.00. The premium adds a 1.9% enhancement over holding the stock alone.

**Bullish**: If the stock rises above $108.00
Above $108.00, the client's position rises with the stock. At $115.00, the client's combined position is **+$2,490.00** — the shares gain +$1,500.00 and the options add +$990.00. There is no cap on upside gains.

---

## Strategy: Syn. Covered Put (ID=62, Code=NAK)

### Options Only

**Bearish**: If the stock falls below $92.00
At any price below $92.00, gains are locked in at **+$990.00**.

**Stagnant**: If the stock stays between $92.00 and $100.00
Between $92.00 and $100.00, the position gains value as the stock moves lower. At $100.00, the position is **+$190.00**. Maximum gain is **+$990.00**. That represents a 33.1% return on the $2,990.00 capital at risk.

**Bullish**: If the stock rises above $100.00
Above $100.00, losses increase as the stock rises. At $102.00, the position is **−$10.00**. Breakeven is $101.90 (1.9% above spot). Maximum gain is **+$990.00**. That represents a 33.1% return on the $2,990.00 capital at risk.

### With Underlying Position

**Bearish**: If the stock falls below $92.00
Below $92.00, the client still has full downside exposure, but the +$990.00 from the options cushions the move. At $85.00, the client's combined position is **−$510.00** — the shares lose −$1,500.00 and the options add +$990.00. Breakeven is $90.10 (9.9% below spot). There is no cap on downside risk. Without the options, the loss would be −$1,500.00.

**Stagnant**: If the stock stays between $92.00 and $100.00
This is the target outcome. As long as the stock stays between $92.00 and $100.00 — roughly 8.0% down to 0.0% down from here — all options expire worthless and the full $990.00 credit is retained. The premium adds a 1.9% enhancement over holding the stock alone. That represents a 1.3% return on the $15,000.00 capital at risk.

**Bullish**: If the stock rises above $100.00
Above $100.00, the short $92.00 call drives losses. Maximum loss is **+$190.00** at any price above $92.00. The trade-off: $990.00 in collected premium in exchange for giving up gains above $92.00. That represents a 1.3% return on the $15,000.00 capital at risk.

---

## Strategy: Conversion (ID=63, Code=COL_EQ)

### Options Only

**Bearish**: If the stock falls below $100.00
Below $100.00, but the long $100.00 put provides a hard floor. Maximum loss is **$0.00** at any price below $300.00. Breakevens are $0.00 (100.0% below spot) and $1.00 (99.0% below spot) and $2.01 (98.0% below spot) and $3.01 (97.0% below spot) and $4.01 (96.0% below spot) and $5.02 (95.0% below spot) and $6.02 (94.0% below spot) and $7.02 (93.0% below spot) and $8.03 (92.0% below spot) and $9.03 (91.0% below spot) and $10.03 (90.0% below spot) and $11.04 (89.0% below spot) and $12.04 (88.0% below spot) and $13.04 (87.0% below spot) and $14.05 (86.0% below spot) and $15.05 (84.9% below spot) and $17.06 (82.9% below spot) and $18.06 (81.9% below spot) and $19.06 (80.9% below spot) and $20.07 (79.9% below spot) and $21.07 (78.9% below spot) and $22.07 (77.9% below spot) and $23.08 (76.9% below spot) and $24.08 (75.9% below spot) and $25.08 (74.9% below spot) and $26.09 (73.9% below spot) and $27.09 (72.9% below spot) and $28.09 (71.9% below spot) and $29.10 (70.9% below spot) and $30.10 (69.9% below spot) and $31.10 (68.9% below spot) and $32.11 (67.9% below spot) and $33.11 (66.9% below spot) and $34.11 (65.9% below spot) and $35.12 (64.9% below spot) and $36.12 (63.9% below spot) and $37.12 (62.9% below spot) and $38.13 (61.9% below spot) and $39.13 (60.9% below spot) and $40.13 (59.9% below spot) and $41.14 (58.9% below spot) and $42.14 (57.9% below spot) and $43.14 (56.9% below spot) and $44.15 (55.9% below spot) and $45.15 (54.8% below spot) and $46.15 (53.8% below spot) and $47.16 (52.8% below spot) and $48.16 (51.8% below spot) and $49.16 (50.8% below spot) and $50.17 (49.8% below spot) and $51.17 (48.8% below spot) and $52.17 (47.8% below spot) and $53.18 (46.8% below spot) and $54.18 (45.8% below spot) and $55.18 (44.8% below spot) and $56.19 (43.8% below spot) and $58.19 (41.8% below spot) and $59.20 (40.8% below spot) and $60.20 (39.8% below spot) and $61.20 (38.8% below spot) and $62.21 (37.8% below spot) and $63.21 (36.8% below spot) and $64.21 (35.8% below spot) and $65.22 (34.8% below spot) and $66.22 (33.8% below spot) and $67.22 (32.8% below spot) and $68.23 (31.8% below spot) and $69.23 (30.8% below spot) and $70.23 (29.8% below spot) and $71.24 (28.8% below spot) and $72.24 (27.8% below spot) and $73.24 (26.8% below spot) and $74.25 (25.8% below spot) and $75.25 (24.7% below spot) and $76.25 (23.7% below spot) and $77.26 (22.7% below spot) and $78.26 (21.7% below spot) and $79.26 (20.7% below spot) and $80.27 (19.7% below spot) and $81.27 (18.7% below spot) and $82.27 (17.7% below spot) and $83.28 (16.7% below spot) and $84.28 (15.7% below spot) and $85.28 (14.7% below spot) and $86.29 (13.7% below spot) and $87.29 (12.7% below spot) and $88.29 (11.7% below spot) and $89.30 (10.7% below spot) and $90.30 (9.7% below spot) and $91.30 (8.7% below spot) and $92.31 (7.7% below spot) and $93.31 (6.7% below spot) and $94.31 (5.7% below spot) and $95.32 (4.7% below spot) and $96.32 (3.7% below spot) and $97.32 (2.7% below spot) and $98.33 (1.7% below spot) and $99.33 (0.7% below spot) and $100.00 (0.0% above spot). The client bought the stock below the protection floor, so even in a severe decline, the position is profitable.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **$0.00**.

**Bullish**: If the stock rises above $100.00
Above $100.00, the short $100.00 call drives losses. Maximum loss is **$0.00** at any price above $0.00. Breakevens are $100.00 (0.0% above spot) and $100.33 (0.3% above spot) and $101.34 (1.3% above spot) and $102.34 (2.3% above spot) and $103.34 (3.3% above spot) and $104.35 (4.3% above spot) and $105.35 (5.4% above spot) and $106.35 (6.4% above spot) and $107.36 (7.4% above spot) and $108.36 (8.4% above spot) and $109.36 (9.4% above spot) and $110.37 (10.4% above spot) and $111.37 (11.4% above spot) and $112.37 (12.4% above spot) and $113.38 (13.4% above spot) and $114.38 (14.4% above spot) and $115.38 (15.4% above spot) and $116.39 (16.4% above spot) and $117.39 (17.4% above spot) and $118.39 (18.4% above spot) and $119.40 (19.4% above spot) and $120.40 (20.4% above spot) and $122.41 (22.4% above spot) and $123.41 (23.4% above spot) and $124.41 (24.4% above spot) and $125.42 (25.4% above spot) and $126.42 (26.4% above spot) and $127.42 (27.4% above spot) and $128.43 (28.4% above spot) and $129.43 (29.4% above spot) and $130.43 (30.4% above spot) and $131.44 (31.4% above spot) and $132.44 (32.4% above spot) and $133.44 (33.4% above spot) and $134.45 (34.4% above spot) and $135.45 (35.5% above spot) and $136.45 (36.5% above spot) and $137.46 (37.5% above spot) and $138.46 (38.5% above spot) and $139.46 (39.5% above spot) and $140.47 (40.5% above spot) and $141.47 (41.5% above spot) and $142.47 (42.5% above spot) and $143.48 (43.5% above spot) and $144.48 (44.5% above spot) and $145.48 (45.5% above spot) and $146.49 (46.5% above spot) and $147.49 (47.5% above spot) and $148.49 (48.5% above spot) and $149.50 (49.5% above spot) and $150.50 (50.5% above spot) and $151.51 (51.5% above spot) and $152.51 (52.5% above spot) and $153.51 (53.5% above spot) and $154.52 (54.5% above spot) and $155.52 (55.5% above spot) and $156.52 (56.5% above spot) and $157.53 (57.5% above spot) and $158.53 (58.5% above spot) and $159.53 (59.5% above spot) and $160.54 (60.5% above spot) and $161.54 (61.5% above spot) and $162.54 (62.5% above spot) and $163.55 (63.5% above spot) and $164.55 (64.5% above spot) and $165.55 (65.6% above spot) and $166.56 (66.6% above spot) and $167.56 (67.6% above spot) and $168.56 (68.6% above spot) and $169.57 (69.6% above spot) and $170.57 (70.6% above spot) and $171.57 (71.6% above spot) and $172.58 (72.6% above spot) and $173.58 (73.6% above spot) and $174.58 (74.6% above spot) and $175.59 (75.6% above spot) and $176.59 (76.6% above spot) and $177.59 (77.6% above spot) and $178.60 (78.6% above spot) and $179.60 (79.6% above spot) and $180.60 (80.6% above spot) and $181.61 (81.6% above spot) and $183.61 (83.6% above spot) and $184.62 (84.6% above spot) and $185.62 (85.6% above spot) and $186.62 (86.6% above spot) and $187.63 (87.6% above spot) and $188.63 (88.6% above spot) and $189.63 (89.6% above spot) and $190.64 (90.6% above spot) and $191.64 (91.6% above spot) and $192.64 (92.6% above spot) and $193.65 (93.6% above spot) and $194.65 (94.6% above spot) and $195.65 (95.7% above spot) and $196.66 (96.7% above spot) and $197.66 (97.7% above spot) and $198.66 (98.7% above spot) and $199.67 (99.7% above spot) and $200.67 (100.7% above spot) and $201.67 (101.7% above spot) and $202.68 (102.7% above spot) and $203.68 (103.7% above spot) and $204.68 (104.7% above spot) and $205.69 (105.7% above spot) and $206.69 (106.7% above spot) and $207.69 (107.7% above spot) and $208.70 (108.7% above spot) and $209.70 (109.7% above spot) and $210.70 (110.7% above spot) and $211.71 (111.7% above spot) and $212.71 (112.7% above spot) and $213.71 (113.7% above spot) and $214.72 (114.7% above spot) and $215.72 (115.7% above spot) and $216.72 (116.7% above spot) and $217.73 (117.7% above spot) and $218.73 (118.7% above spot) and $219.73 (119.7% above spot) and $220.74 (120.7% above spot) and $221.74 (121.7% above spot) and $222.74 (122.7% above spot) and $223.75 (123.7% above spot) and $224.75 (124.7% above spot) and $225.75 (125.8% above spot) and $226.76 (126.8% above spot) and $227.76 (127.8% above spot) and $228.76 (128.8% above spot) and $229.77 (129.8% above spot) and $230.77 (130.8% above spot) and $231.77 (131.8% above spot) and $232.78 (132.8% above spot) and $233.78 (133.8% above spot) and $234.78 (134.8% above spot) and $235.79 (135.8% above spot) and $236.79 (136.8% above spot) and $237.79 (137.8% above spot) and $238.80 (138.8% above spot) and $239.80 (139.8% above spot) and $240.80 (140.8% above spot) and $241.81 (141.8% above spot) and $242.81 (142.8% above spot) and $243.81 (143.8% above spot) and $244.82 (144.8% above spot) and $245.82 (145.8% above spot) and $246.82 (146.8% above spot) and $247.83 (147.8% above spot) and $248.83 (148.8% above spot) and $249.83 (149.8% above spot) and $250.84 (150.8% above spot) and $251.84 (151.8% above spot) and $252.84 (152.8% above spot) and $253.85 (153.8% above spot) and $254.85 (154.8% above spot) and $255.85 (155.9% above spot) and $256.86 (156.9% above spot) and $257.86 (157.9% above spot) and $258.86 (158.9% above spot) and $259.87 (159.9% above spot) and $260.87 (160.9% above spot) and $261.87 (161.9% above spot) and $262.88 (162.9% above spot) and $263.88 (163.9% above spot) and $264.88 (164.9% above spot) and $265.89 (165.9% above spot) and $266.89 (166.9% above spot) and $267.89 (167.9% above spot) and $268.90 (168.9% above spot) and $269.90 (169.9% above spot) and $270.90 (170.9% above spot) and $271.91 (171.9% above spot) and $272.91 (172.9% above spot) and $273.91 (173.9% above spot) and $274.92 (174.9% above spot) and $275.92 (175.9% above spot) and $276.92 (176.9% above spot) and $277.93 (177.9% above spot) and $278.93 (178.9% above spot) and $279.93 (179.9% above spot) and $280.94 (180.9% above spot) and $281.94 (181.9% above spot) and $282.94 (182.9% above spot) and $283.95 (183.9% above spot) and $284.95 (184.9% above spot) and $285.95 (186.0% above spot) and $286.96 (187.0% above spot) and $287.96 (188.0% above spot) and $288.96 (189.0% above spot) and $289.97 (190.0% above spot) and $290.97 (191.0% above spot) and $291.97 (192.0% above spot) and $292.98 (193.0% above spot) and $293.98 (194.0% above spot) and $294.98 (195.0% above spot) and $295.99 (196.0% above spot) and $296.99 (197.0% above spot) and $297.99 (198.0% above spot) and $299.00 (199.0% above spot). The trade-off: downside protection below $100.00 in exchange for capping gains above $100.00.

### With Underlying Position

**Bearish**: If the stock falls below $100.00
Below $100.00, but the long $100.00 put provides a hard floor. Maximum loss is **$0.00** at any price below $300.00. Breakevens are $0.00 (100.0% below spot) and $1.00 (99.0% below spot) and $2.01 (98.0% below spot) and $3.01 (97.0% below spot) and $4.01 (96.0% below spot) and $5.02 (95.0% below spot) and $6.02 (94.0% below spot) and $7.02 (93.0% below spot) and $8.03 (92.0% below spot) and $9.03 (91.0% below spot) and $10.03 (90.0% below spot) and $11.04 (89.0% below spot) and $12.04 (88.0% below spot) and $13.04 (87.0% below spot) and $14.05 (86.0% below spot) and $15.05 (84.9% below spot) and $17.06 (82.9% below spot) and $18.06 (81.9% below spot) and $19.06 (80.9% below spot) and $20.07 (79.9% below spot) and $21.07 (78.9% below spot) and $22.07 (77.9% below spot) and $23.08 (76.9% below spot) and $24.08 (75.9% below spot) and $25.08 (74.9% below spot) and $26.09 (73.9% below spot) and $27.09 (72.9% below spot) and $28.09 (71.9% below spot) and $29.10 (70.9% below spot) and $30.10 (69.9% below spot) and $31.10 (68.9% below spot) and $32.11 (67.9% below spot) and $33.11 (66.9% below spot) and $34.11 (65.9% below spot) and $35.12 (64.9% below spot) and $36.12 (63.9% below spot) and $37.12 (62.9% below spot) and $38.13 (61.9% below spot) and $39.13 (60.9% below spot) and $40.13 (59.9% below spot) and $41.14 (58.9% below spot) and $42.14 (57.9% below spot) and $43.14 (56.9% below spot) and $44.15 (55.9% below spot) and $45.15 (54.8% below spot) and $46.15 (53.8% below spot) and $47.16 (52.8% below spot) and $48.16 (51.8% below spot) and $49.16 (50.8% below spot) and $50.17 (49.8% below spot) and $51.17 (48.8% below spot) and $52.17 (47.8% below spot) and $53.18 (46.8% below spot) and $54.18 (45.8% below spot) and $55.18 (44.8% below spot) and $56.19 (43.8% below spot) and $58.19 (41.8% below spot) and $59.20 (40.8% below spot) and $60.20 (39.8% below spot) and $61.20 (38.8% below spot) and $62.21 (37.8% below spot) and $63.21 (36.8% below spot) and $64.21 (35.8% below spot) and $65.22 (34.8% below spot) and $66.22 (33.8% below spot) and $67.22 (32.8% below spot) and $68.23 (31.8% below spot) and $69.23 (30.8% below spot) and $70.23 (29.8% below spot) and $71.24 (28.8% below spot) and $72.24 (27.8% below spot) and $73.24 (26.8% below spot) and $74.25 (25.8% below spot) and $75.25 (24.7% below spot) and $76.25 (23.7% below spot) and $77.26 (22.7% below spot) and $78.26 (21.7% below spot) and $79.26 (20.7% below spot) and $80.27 (19.7% below spot) and $81.27 (18.7% below spot) and $82.27 (17.7% below spot) and $83.28 (16.7% below spot) and $84.28 (15.7% below spot) and $85.28 (14.7% below spot) and $86.29 (13.7% below spot) and $87.29 (12.7% below spot) and $88.29 (11.7% below spot) and $89.30 (10.7% below spot) and $90.30 (9.7% below spot) and $91.30 (8.7% below spot) and $92.31 (7.7% below spot) and $93.31 (6.7% below spot) and $94.31 (5.7% below spot) and $95.32 (4.7% below spot) and $96.32 (3.7% below spot) and $97.32 (2.7% below spot) and $98.33 (1.7% below spot) and $99.33 (0.7% below spot) and $100.00 (0.0% above spot). The client bought the stock below the protection floor, so even in a severe decline, the position is profitable.

**Stagnant**: If the stock stays near $100.00
Near $100.00, the client's position moves with the stock — the collar has no net cost in this range. At $100.00, the client's combined position is **$0.00** — the shares gain $0.00 and the options add $0.00. Breakeven is $100.00 (0.0% above spot). Maximum gain is **$0.00**.

**Bullish**: If the stock rises above $100.00
Above $100.00, the short $100.00 call drives losses. Maximum loss is **$0.00** at any price above $0.00. Breakevens are $100.00 (0.0% above spot) and $100.33 (0.3% above spot) and $101.34 (1.3% above spot) and $102.34 (2.3% above spot) and $103.34 (3.3% above spot) and $104.35 (4.3% above spot) and $105.35 (5.4% above spot) and $106.35 (6.4% above spot) and $107.36 (7.4% above spot) and $108.36 (8.4% above spot) and $109.36 (9.4% above spot) and $110.37 (10.4% above spot) and $111.37 (11.4% above spot) and $112.37 (12.4% above spot) and $113.38 (13.4% above spot) and $114.38 (14.4% above spot) and $115.38 (15.4% above spot) and $116.39 (16.4% above spot) and $117.39 (17.4% above spot) and $118.39 (18.4% above spot) and $119.40 (19.4% above spot) and $120.40 (20.4% above spot) and $122.41 (22.4% above spot) and $123.41 (23.4% above spot) and $124.41 (24.4% above spot) and $125.42 (25.4% above spot) and $126.42 (26.4% above spot) and $127.42 (27.4% above spot) and $128.43 (28.4% above spot) and $129.43 (29.4% above spot) and $130.43 (30.4% above spot) and $131.44 (31.4% above spot) and $132.44 (32.4% above spot) and $133.44 (33.4% above spot) and $134.45 (34.4% above spot) and $135.45 (35.5% above spot) and $136.45 (36.5% above spot) and $137.46 (37.5% above spot) and $138.46 (38.5% above spot) and $139.46 (39.5% above spot) and $140.47 (40.5% above spot) and $141.47 (41.5% above spot) and $142.47 (42.5% above spot) and $143.48 (43.5% above spot) and $144.48 (44.5% above spot) and $145.48 (45.5% above spot) and $146.49 (46.5% above spot) and $147.49 (47.5% above spot) and $148.49 (48.5% above spot) and $149.50 (49.5% above spot) and $150.50 (50.5% above spot) and $151.51 (51.5% above spot) and $152.51 (52.5% above spot) and $153.51 (53.5% above spot) and $154.52 (54.5% above spot) and $155.52 (55.5% above spot) and $156.52 (56.5% above spot) and $157.53 (57.5% above spot) and $158.53 (58.5% above spot) and $159.53 (59.5% above spot) and $160.54 (60.5% above spot) and $161.54 (61.5% above spot) and $162.54 (62.5% above spot) and $163.55 (63.5% above spot) and $164.55 (64.5% above spot) and $165.55 (65.6% above spot) and $166.56 (66.6% above spot) and $167.56 (67.6% above spot) and $168.56 (68.6% above spot) and $169.57 (69.6% above spot) and $170.57 (70.6% above spot) and $171.57 (71.6% above spot) and $172.58 (72.6% above spot) and $173.58 (73.6% above spot) and $174.58 (74.6% above spot) and $175.59 (75.6% above spot) and $176.59 (76.6% above spot) and $177.59 (77.6% above spot) and $178.60 (78.6% above spot) and $179.60 (79.6% above spot) and $180.60 (80.6% above spot) and $181.61 (81.6% above spot) and $183.61 (83.6% above spot) and $184.62 (84.6% above spot) and $185.62 (85.6% above spot) and $186.62 (86.6% above spot) and $187.63 (87.6% above spot) and $188.63 (88.6% above spot) and $189.63 (89.6% above spot) and $190.64 (90.6% above spot) and $191.64 (91.6% above spot) and $192.64 (92.6% above spot) and $193.65 (93.6% above spot) and $194.65 (94.6% above spot) and $195.65 (95.7% above spot) and $196.66 (96.7% above spot) and $197.66 (97.7% above spot) and $198.66 (98.7% above spot) and $199.67 (99.7% above spot) and $200.67 (100.7% above spot) and $201.67 (101.7% above spot) and $202.68 (102.7% above spot) and $203.68 (103.7% above spot) and $204.68 (104.7% above spot) and $205.69 (105.7% above spot) and $206.69 (106.7% above spot) and $207.69 (107.7% above spot) and $208.70 (108.7% above spot) and $209.70 (109.7% above spot) and $210.70 (110.7% above spot) and $211.71 (111.7% above spot) and $212.71 (112.7% above spot) and $213.71 (113.7% above spot) and $214.72 (114.7% above spot) and $215.72 (115.7% above spot) and $216.72 (116.7% above spot) and $217.73 (117.7% above spot) and $218.73 (118.7% above spot) and $219.73 (119.7% above spot) and $220.74 (120.7% above spot) and $221.74 (121.7% above spot) and $222.74 (122.7% above spot) and $223.75 (123.7% above spot) and $224.75 (124.7% above spot) and $225.75 (125.8% above spot) and $226.76 (126.8% above spot) and $227.76 (127.8% above spot) and $228.76 (128.8% above spot) and $229.77 (129.8% above spot) and $230.77 (130.8% above spot) and $231.77 (131.8% above spot) and $232.78 (132.8% above spot) and $233.78 (133.8% above spot) and $234.78 (134.8% above spot) and $235.79 (135.8% above spot) and $236.79 (136.8% above spot) and $237.79 (137.8% above spot) and $238.80 (138.8% above spot) and $239.80 (139.8% above spot) and $240.80 (140.8% above spot) and $241.81 (141.8% above spot) and $242.81 (142.8% above spot) and $243.81 (143.8% above spot) and $244.82 (144.8% above spot) and $245.82 (145.8% above spot) and $246.82 (146.8% above spot) and $247.83 (147.8% above spot) and $248.83 (148.8% above spot) and $249.83 (149.8% above spot) and $250.84 (150.8% above spot) and $251.84 (151.8% above spot) and $252.84 (152.8% above spot) and $253.85 (153.8% above spot) and $254.85 (154.8% above spot) and $255.85 (155.9% above spot) and $256.86 (156.9% above spot) and $257.86 (157.9% above spot) and $258.86 (158.9% above spot) and $259.87 (159.9% above spot) and $260.87 (160.9% above spot) and $261.87 (161.9% above spot) and $262.88 (162.9% above spot) and $263.88 (163.9% above spot) and $264.88 (164.9% above spot) and $265.89 (165.9% above spot) and $266.89 (166.9% above spot) and $267.89 (167.9% above spot) and $268.90 (168.9% above spot) and $269.90 (169.9% above spot) and $270.90 (170.9% above spot) and $271.91 (171.9% above spot) and $272.91 (172.9% above spot) and $273.91 (173.9% above spot) and $274.92 (174.9% above spot) and $275.92 (175.9% above spot) and $276.92 (176.9% above spot) and $277.93 (177.9% above spot) and $278.93 (178.9% above spot) and $279.93 (179.9% above spot) and $280.94 (180.9% above spot) and $281.94 (181.9% above spot) and $282.94 (182.9% above spot) and $283.95 (183.9% above spot) and $284.95 (184.9% above spot) and $285.95 (186.0% above spot) and $286.96 (187.0% above spot) and $287.96 (188.0% above spot) and $288.96 (189.0% above spot) and $289.97 (190.0% above spot) and $290.97 (191.0% above spot) and $291.97 (192.0% above spot) and $292.98 (193.0% above spot) and $293.98 (194.0% above spot) and $294.98 (195.0% above spot) and $295.99 (196.0% above spot) and $296.99 (197.0% above spot) and $297.99 (198.0% above spot) and $299.00 (199.0% above spot). The trade-off: downside protection below $100.00 in exchange for capping gains above $100.00.

---

