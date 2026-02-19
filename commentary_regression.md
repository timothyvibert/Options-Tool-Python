# Commentary Regression Report

Generated: 2026-02-13

## Summary

- **Total strategies in CSV**: 63
- **Total runs** (options-only + with-stock): 126
- **Errors**: 1
- **Empty/None narratives**: 0
- **Distinct rule IDs matched**: ['call_spread_debit_v1', 'collar_v3', 'covered_call_v3', 'fallback_generic', 'iron_condor_v3', 'protective_put_v3']
- **Duplicate body texts** (same body across 4+ runs): 5

### Errors

- **Custom Strategy** (ID=1, variant=options_only): `No legs and no stock position`

### Duplicate Body Texts (possible generic templating)

- **5 runs** share: "Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. ROI at ..."
  Strategies: Long Put(options_only), Bull Put Ladder(options_only), Long Straddle(options_only), Strip(options_only), Strap(options_only)
- **5 runs** share: "Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. ROI at ..."
  Strategies: Long Put(options_only), Bull Put Ladder(options_only), Long Straddle(options_only), Strip(options_only), Strap(options_only)
- **4 runs** share: "Below $100.00, losses track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic valu..."
  Strategies: Custom Strategy(with_stock), Long Stock(options_only), Long Stock(with_stock), Synthetic Long Stock(with_stock)
- **4 runs** share: "Between $100.00 and $100.00, results follow the shares for the position (100 shares). At expiry, option payoffs settle t..."
  Strategies: Custom Strategy(with_stock), Long Stock(options_only), Long Stock(with_stock), Synthetic Long Stock(with_stock)
- **4 runs** share: "Above $100.00, gains track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value..."
  Strategies: Custom Strategy(with_stock), Long Stock(options_only), Long Stock(with_stock), Synthetic Long Stock(with_stock)

---

## Per-Strategy Results

## Strategy: Custom Strategy (ID=1, Group=Basics, Subgroup=Custom, Kind=STOCK_ONLY)

### Options Only

**ERROR**: `No legs and no stock position`

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement.
  - **Strikes**: --
  - **Breakevens**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement.
  - **Low**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement.
  - **High**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

---

## Strategy: Long Stock (ID=2, Group=Basics, Subgroup=Bullish, Kind=STOCK_ONLY)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement.
  - **Strikes**: --
  - **Breakevens**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement.
  - **Low**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement.
  - **High**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement.
  - **Strikes**: --
  - **Breakevens**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement.
  - **Low**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement.
  - **High**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

---

## Strategy: Short Stock (ID=3, Group=Basics, Subgroup=Bearish, Kind=STOCK_ONLY)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement (in the opposite direction).
  - **Strikes**: --
  - **Breakevens**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement (in the opposite direction).
  - **Low**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement (in the opposite direction).
  - **High**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement (in the opposite direction).

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement (in the opposite direction).
  - **Strikes**: --
  - **Breakevens**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement (in the opposite direction).
  - **Low**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement (in the opposite direction).
  - **High**: **Near current level:** Your result is driven mainly by normal day‑to‑day stock movement (in the opposite direction).

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

---

## Strategy: Long Call (ID=4, Group=Basics, Subgroup=Bullish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.
  - **Strikes**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.
  - **Breakevens**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.
  - **Low**: **Premium‑at‑risk:** The stock is below your call strike (100.00), so the option’s value is limited unless the stock rebounds.
  - **High**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. Maximum loss is $250.00. ROI at $100.00 is -100.0%.
  overlay_pnl=-250.0, stock_only_pnl=0.0, delta_vs_stock=-250.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Breakeven is around $102.50.
  overlay_pnl=-250.0, stock_only_pnl=0.0, delta_vs_stock=-250.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. Maximum loss is $250.00. ROI at $100.00 is -100.0%.
  overlay_pnl=-250.0, stock_only_pnl=0.0, delta_vs_stock=-250.0
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.
  - **Strikes**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.
  - **Breakevens**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.
  - **Low**: **Premium‑at‑risk:** The stock is below your call strike (100.00), so the option’s value is limited unless the stock rebounds.
  - **High**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $250.00 on 1 contracts paid.
  overlay_pnl=-250.0, stock_only_pnl=0.0, delta_vs_stock=-250.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $250.00 on 1 contracts paid.
  overlay_pnl=-250.0, stock_only_pnl=0.0, delta_vs_stock=-250.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $250.00 on 1 contracts paid.
  overlay_pnl=-250.0, stock_only_pnl=0.0, delta_vs_stock=-250.0
  Anchors: Current Market Price@100.0

---

## Strategy: Short Call (ID=5, Group=Basics, Subgroup=Bearish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Watch zone:** Near/above your call strike (100.00), upside gains can be partially offset and risk increases.
  - **Strikes**: **Watch zone:** Near/above your call strike (100.00), upside gains can be partially offset and risk increases.
  - **Breakevens**: **High‑risk zone:** Above the call strike (100.00), losses can continue to grow if the stock keeps rising.
  - **Low**: **Income zone:** Below your call strike (100.00), the call is more likely to expire with limited value.
  - **High**: **High‑risk zone:** Above the call strike (100.00), losses can continue to grow if the stock keeps rising.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. ROI at $100.00 is 11.1%.
  overlay_pnl=250.0, stock_only_pnl=0.0, delta_vs_stock=250.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Net option premium (total): $25,000.00 on 1 contracts received Breakeven is around $102.50.
  overlay_pnl=250.0, stock_only_pnl=0.0, delta_vs_stock=250.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. ROI at $100.00 is 11.1%.
  overlay_pnl=250.0, stock_only_pnl=0.0, delta_vs_stock=250.0
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: covered_call_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Income zone:** If the stock stays below your call strike (100.00), premium income can help support returns.
  - **Strikes**: **Income zone:** If the stock stays below your call strike (100.00), premium income can help support returns.
  - **Breakevens**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position.
  - **Low**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position.
  - **High**: **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, downside follows the shares for the full position (100 of 100 shares). At expiry below $100.00, the call expires worthless on the covered shares. Net option premium (total): $250.00 on 1 contracts received.
  overlay_pnl=250.0, stock_only_pnl=0.0, delta_vs_stock=250.0
  Anchors: Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $100.00 and $100.00
  Body: Between $100.00 and $100.00, gains follow the shares for the full position (100 of 100 shares). At expiry in this range, the call expires worthless on the covered shares. Net option premium (total): $250.00 on 1 contracts received.
  overlay_pnl=250.0, stock_only_pnl=0.0, delta_vs_stock=250.0
  Anchors: Current Market Price@100.0, Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, upside is limited by the call strike for the full position (100 of 100 shares). At expiry above $100.00, shares may be called away at the strike and upside is capped on the covered shares. Maximum combined profit (at expiry): $250.00.
  overlay_pnl=250.0, stock_only_pnl=0.0, delta_vs_stock=250.0
  Anchors: Current Market Price@100.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

---

## Strategy: Long Put (ID=6, Group=Basics, Subgroup=Bearish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Decision zone:** Near your put strike (100.00), downside moves can increase protection quickly.
  - **Strikes**: **Decision zone:** Near your put strike (100.00), downside moves can increase protection quickly.
  - **Breakevens**: **Decision zone:** Near your put strike (100.00), downside moves can increase protection quickly.
  - **Low**: **Decision zone:** Near your put strike (100.00), downside moves can increase protection quickly.
  - **High**: **Premium‑at‑risk:** The stock is above your put strike (100.00), so the option’s value is limited unless the stock falls.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. ROI at $100.00 is -100.0%.
  overlay_pnl=-250.0, stock_only_pnl=0.0, delta_vs_stock=-250.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Breakeven is around $97.50.
  overlay_pnl=-250.0, stock_only_pnl=0.0, delta_vs_stock=-250.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. ROI at $100.00 is -100.0%.
  overlay_pnl=-250.0, stock_only_pnl=0.0, delta_vs_stock=-250.0
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: protective_put_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Buffered exposure:** Between current levels and the protection strike (100.00), you still participate in moves, with downside protection further below.
  - **Strikes**: **Buffered exposure:** Between current levels and the protection strike (100.00), you still participate in moves, with downside protection further below.
  - **Breakevens**: **Buffered exposure:** Between current levels and the protection strike (100.00), you still participate in moves, with downside protection further below.
  - **Low**: **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside on the combined position.
  - **High**: **Buffered exposure:** Between current levels and the protection strike (100.00), you still participate in moves, with downside protection further below.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, the put establishes the floor for the full position (100 of 100 shares). At expiry below $100.00, the put settles at intrinsic value and downside is protected on the protected shares. Maximum combined loss (at expiry): $250.00.
  overlay_pnl=-250.0, stock_only_pnl=0.0, delta_vs_stock=-250.0
  Anchors: Current Market Price@100.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $100.00 and $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry in this range, protection remains in place on the protected shares. Net option premium (total): $250.00 on 1 contracts paid.
  overlay_pnl=-250.0, stock_only_pnl=0.0, delta_vs_stock=-250.0
  Anchors: Current Market Price@100.0, Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, upside participation continues for the full position (100 of 100 shares). At expiry above $100.00, the put expires worthless and gains follow the shares on the protected shares. At $100.00, combined P&L would be -$250.00 (options contribute -$250.00; the shares contribute +$0.00).
  overlay_pnl=-250.0, stock_only_pnl=0.0, delta_vs_stock=-250.0
  Anchors: Upside Target (15%)@114.99999999999999, Stock to Infinity@None

---

## Strategy: Short Put (ID=7, Group=Basics, Subgroup=Bullish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Watch zone:** Near your put strike (100.00), you are closer to being obligated to buy shares at that level.
  - **Strikes**: **Watch zone:** Near your put strike (100.00), you are closer to being obligated to buy shares at that level.
  - **Breakevens**: **Assignment zone:** Below the put strike (100.00), the position behaves more like buying shares at that strike (downside continues below it).
  - **Low**: **Assignment zone:** Below the put strike (100.00), the position behaves more like buying shares at that strike (downside continues below it).
  - **High**: **Income zone:** Above your put strike (100.00), the put is more likely to expire with limited value.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. Maximum loss is $9,750.00.
  overlay_pnl=250.0, stock_only_pnl=0.0, delta_vs_stock=250.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Net option premium (total): $25,000.00 on 1 contracts received Breakeven is around $97.50.
  overlay_pnl=250.0, stock_only_pnl=0.0, delta_vs_stock=250.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. Maximum loss is $9,750.00.
  overlay_pnl=250.0, stock_only_pnl=0.0, delta_vs_stock=250.0
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Watch zone:** Near your put strike (100.00), you are closer to being obligated to buy shares at that level.
  - **Strikes**: **Watch zone:** Near your put strike (100.00), you are closer to being obligated to buy shares at that level.
  - **Breakevens**: **Assignment zone:** Below the put strike (100.00), the position behaves more like buying shares at that strike (downside continues below it).
  - **Low**: **Assignment zone:** Below the put strike (100.00), the position behaves more like buying shares at that strike (downside continues below it).
  - **High**: **Watch zone:** Near your put strike (100.00), you are closer to being obligated to buy shares at that level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $250.00 on 1 contracts received.
  overlay_pnl=250.0, stock_only_pnl=0.0, delta_vs_stock=250.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $250.00 on 1 contracts received.
  overlay_pnl=250.0, stock_only_pnl=0.0, delta_vs_stock=250.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $250.00 on 1 contracts received.
  overlay_pnl=250.0, stock_only_pnl=0.0, delta_vs_stock=250.0
  Anchors: Current Market Price@100.0

---

## Strategy: Covered Call (ID=8, Group=Basics, Subgroup=Bullish, Kind=MIXED)

### Options Only

**Rule matched**: covered_call_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position.
  - **Strikes**: **Income zone:** If the stock stays below your call strike (108.00), premium income can help support returns.
  - **Breakevens**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position.
  - **Low**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position.
  - **High**: **Upside limited:** Above your call strike (108.00), further upside is typically capped because shares may be called away.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $108.00, downside follows the shares for the full position (100 of 100 shares). At expiry below $108.00, the call expires worthless on the covered shares. Net option premium (total): $190.00 on 1 contracts received.
  overlay_pnl=990.0, stock_only_pnl=800.0, delta_vs_stock=190.0
  Anchors: Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $100.00 and $108.00
  Body: Between $100.00 and $108.00, gains follow the shares for the full position (100 of 100 shares). At expiry in this range, the call expires worthless on the covered shares. Net option premium (total): $190.00 on 1 contracts received.
  overlay_pnl=190.0, stock_only_pnl=0.0, delta_vs_stock=190.0
  Anchors: Current Market Price@100.0, Strike@108.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, upside is limited by the call strike for the full position (100 of 100 shares). At expiry above $108.00, shares may be called away at the strike and upside is capped on the covered shares. Maximum combined profit (at expiry): $990.00.
  overlay_pnl=990.0, stock_only_pnl=800.0, delta_vs_stock=190.0
  Anchors: Strike@108.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

### With Underlying Position

**Rule matched**: covered_call_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position.
  - **Strikes**: **Income zone:** If the stock stays below your call strike (108.00), premium income can help support returns.
  - **Breakevens**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position.
  - **Low**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position.
  - **High**: **Upside limited:** Above your call strike (108.00), further upside is typically capped because shares may be called away.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $108.00, downside follows the shares for the full position (100 of 100 shares). At expiry below $108.00, the call expires worthless on the covered shares. Net option premium (total): $190.00 on 1 contracts received.
  overlay_pnl=990.0, stock_only_pnl=800.0, delta_vs_stock=190.0
  Anchors: Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $100.00 and $108.00
  Body: Between $100.00 and $108.00, gains follow the shares for the full position (100 of 100 shares). At expiry in this range, the call expires worthless on the covered shares. Net option premium (total): $190.00 on 1 contracts received.
  overlay_pnl=190.0, stock_only_pnl=0.0, delta_vs_stock=190.0
  Anchors: Current Market Price@100.0, Strike@108.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, upside is limited by the call strike for the full position (100 of 100 shares). At expiry above $108.00, shares may be called away at the strike and upside is capped on the covered shares. Maximum combined profit (at expiry): $990.00.
  overlay_pnl=990.0, stock_only_pnl=800.0, delta_vs_stock=190.0
  Anchors: Strike@108.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

---

## Strategy: Covered Put (ID=9, Group=Basics, Subgroup=Bearish, Kind=MIXED)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Watch zone:** Near your put strike (92.00), you are closer to being obligated to buy shares at that level.
  - **Strikes**: **Watch zone:** Near your put strike (92.00), you are closer to being obligated to buy shares at that level.
  - **Breakevens**: **Watch zone:** Near your put strike (92.00), you are closer to being obligated to buy shares at that level.
  - **Low**: **Assignment zone:** Below the put strike (92.00), the position behaves more like buying shares at that strike (downside continues below it).
  - **High**: **Watch zone:** Near your put strike (92.00), you are closer to being obligated to buy shares at that level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $190.00 on 1 contracts received.
  overlay_pnl=990.0, stock_only_pnl=800.0, delta_vs_stock=190.0
  Anchors: Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $92.00
  Body: Between $92.00 and $92.00, results follow the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $190.00 on 1 contracts received.
  overlay_pnl=190.0, stock_only_pnl=0.0, delta_vs_stock=190.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $92.00
  Body: Above $92.00, gains track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $190.00 on 1 contracts received.
  overlay_pnl=990.0, stock_only_pnl=800.0, delta_vs_stock=190.0
  Anchors: Strike@92.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Watch zone:** Near your put strike (92.00), you are closer to being obligated to buy shares at that level.
  - **Strikes**: **Watch zone:** Near your put strike (92.00), you are closer to being obligated to buy shares at that level.
  - **Breakevens**: **Watch zone:** Near your put strike (92.00), you are closer to being obligated to buy shares at that level.
  - **Low**: **Assignment zone:** Below the put strike (92.00), the position behaves more like buying shares at that strike (downside continues below it).
  - **High**: **Watch zone:** Near your put strike (92.00), you are closer to being obligated to buy shares at that level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $190.00 on 1 contracts received.
  overlay_pnl=990.0, stock_only_pnl=800.0, delta_vs_stock=190.0
  Anchors: Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $92.00
  Body: Between $92.00 and $92.00, results follow the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $190.00 on 1 contracts received.
  overlay_pnl=190.0, stock_only_pnl=0.0, delta_vs_stock=190.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $92.00
  Body: Above $92.00, gains track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $190.00 on 1 contracts received.
  overlay_pnl=990.0, stock_only_pnl=800.0, delta_vs_stock=190.0
  Anchors: Strike@92.0

---

## Strategy: Protective Call (ID=10, Group=Basics, Subgroup=Bearish, Kind=MIXED)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Decision zone:** Near your call strike (108.00), small moves can change the option’s value quickly.
  - **Strikes**: **Decision zone:** Near your call strike (108.00), small moves can change the option’s value quickly.
  - **Breakevens**: **Decision zone:** Near your call strike (108.00), small moves can change the option’s value quickly.
  - **Low**: **Decision zone:** Near your call strike (108.00), small moves can change the option’s value quickly.
  - **High**: **Participation zone:** Above your call strike (108.00), gains tend to increase as the stock rises.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $108.00
  Body: Below $108.00, losses track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $190.00 on 1 contracts paid.
  overlay_pnl=-990.0, stock_only_pnl=-800.0, delta_vs_stock=-190.0
  Anchors: Strike@108.0

  **Stagnant Case**
  Condition: If stock stays between $108.00 and $108.00
  Body: Between $108.00 and $108.00, results follow the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $190.00 on 1 contracts paid.
  overlay_pnl=-190.0, stock_only_pnl=0.0, delta_vs_stock=-190.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $190.00 on 1 contracts paid.
  overlay_pnl=-990.0, stock_only_pnl=-800.0, delta_vs_stock=-190.0
  Anchors: Strike@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Decision zone:** Near your call strike (108.00), small moves can change the option’s value quickly.
  - **Strikes**: **Decision zone:** Near your call strike (108.00), small moves can change the option’s value quickly.
  - **Breakevens**: **Decision zone:** Near your call strike (108.00), small moves can change the option’s value quickly.
  - **Low**: **Decision zone:** Near your call strike (108.00), small moves can change the option’s value quickly.
  - **High**: **Participation zone:** Above your call strike (108.00), gains tend to increase as the stock rises.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $108.00
  Body: Below $108.00, losses track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $190.00 on 1 contracts paid.
  overlay_pnl=-990.0, stock_only_pnl=-800.0, delta_vs_stock=-190.0
  Anchors: Strike@108.0

  **Stagnant Case**
  Condition: If stock stays between $108.00 and $108.00
  Body: Between $108.00 and $108.00, results follow the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $190.00 on 1 contracts paid.
  overlay_pnl=-190.0, stock_only_pnl=0.0, delta_vs_stock=-190.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $190.00 on 1 contracts paid.
  overlay_pnl=-990.0, stock_only_pnl=-800.0, delta_vs_stock=-190.0
  Anchors: Strike@108.0

---

## Strategy: Protective Put (ID=11, Group=Basics, Subgroup=Bullish, Kind=MIXED)

### Options Only

**Rule matched**: protective_put_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.
  - **Strikes**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.
  - **Breakevens**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.
  - **Low**: **Protection working:** Below the put strike (92.00), the hedge is designed to limit further downside on the combined position.
  - **High**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, the put establishes the floor for the full position (100 of 100 shares). At expiry below $92.00, the put settles at intrinsic value and downside is protected on the protected shares. At $92.00, combined P&L would be -$990.00 (options contribute -$190.00; the shares contribute -$800.00).
  overlay_pnl=-990.0, stock_only_pnl=-800.0, delta_vs_stock=-190.0
  Anchors: Strike@92.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $100.00
  Body: Between $92.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry in this range, protection remains in place on the protected shares. Net option premium (total): $190.00 on 1 contracts paid.
  overlay_pnl=-190.0, stock_only_pnl=0.0, delta_vs_stock=-190.0
  Anchors: Current Market Price@100.0, Strike@92.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, upside participation continues for the full position (100 of 100 shares). At expiry above $100.00, the put expires worthless and gains follow the shares on the protected shares. At $92.00, combined P&L would be -$990.00 (options contribute -$190.00; the shares contribute -$800.00).
  overlay_pnl=-990.0, stock_only_pnl=-800.0, delta_vs_stock=-190.0
  Anchors: Upside Target (15%)@114.99999999999999, Stock to Infinity@None

### With Underlying Position

**Rule matched**: protective_put_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.
  - **Strikes**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.
  - **Breakevens**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.
  - **Low**: **Protection working:** Below the put strike (92.00), the hedge is designed to limit further downside on the combined position.
  - **High**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, the put establishes the floor for the full position (100 of 100 shares). At expiry below $92.00, the put settles at intrinsic value and downside is protected on the protected shares. At $92.00, combined P&L would be -$990.00 (options contribute -$190.00; the shares contribute -$800.00).
  overlay_pnl=-990.0, stock_only_pnl=-800.0, delta_vs_stock=-190.0
  Anchors: Strike@92.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $100.00
  Body: Between $92.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry in this range, protection remains in place on the protected shares. Net option premium (total): $190.00 on 1 contracts paid.
  overlay_pnl=-190.0, stock_only_pnl=0.0, delta_vs_stock=-190.0
  Anchors: Current Market Price@100.0, Strike@92.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, upside participation continues for the full position (100 of 100 shares). At expiry above $100.00, the put expires worthless and gains follow the shares on the protected shares. At $92.00, combined P&L would be -$990.00 (options contribute -$190.00; the shares contribute -$800.00).
  overlay_pnl=-990.0, stock_only_pnl=-800.0, delta_vs_stock=-190.0
  Anchors: Upside Target (15%)@114.99999999999999, Stock to Infinity@None

---

## Strategy: Collar (ID=12, Group=Basics, Subgroup=Neutral, Kind=MIXED)

### Options Only

**Rule matched**: collar_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Stability zone:** Between the protection level (92.00) and the call strike (108.00), the goal is steadier outcomes versus holding stock alone.
  - **Strikes**: **Stability zone:** Between the protection level (92.00) and the call strike (108.00), the goal is steadier outcomes versus holding stock alone. **Stability zone:** Between the protection level (92.00) and the call strike (108.00), the goal is steadier outcomes versus holding stock alone.
  - **Breakevens**: **Stability zone:** Between the protection level (92.00) and the call strike (108.00), the goal is steadier outcomes versus holding stock alone.
  - **Low**: **Protection working:** Below the put strike (92.00), the hedge is designed to limit further downside.
  - **High**: **Upside limited:** Above your call strike (108.00), further upside is typically capped because shares may be called away.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, the put sets the floor for the full position (100 of 100 shares). At expiry below $92.00, downside is protected on the collared shares. Maximum combined loss (at expiry): $800.00.
  overlay_pnl=-800.0, stock_only_pnl=-800.0, delta_vs_stock=0.0
  Anchors: Lower Strike@92.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, P&L is primarily driven by the shares for the full position (100 of 100 shares). At expiry in this range, the collar legs expire worthless on the collared shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0, Lower Strike@92.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, upside is limited by the call strike for the full position (100 of 100 shares). At expiry above $108.00, shares may be called away at the strike and upside is capped on the collared shares. Maximum combined profit (at expiry): $800.00.
  overlay_pnl=800.0, stock_only_pnl=800.0, delta_vs_stock=0.0
  Anchors: Lower Strike@92.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

### With Underlying Position

**Rule matched**: collar_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Stability zone:** Between the protection level (92.00) and the call strike (108.00), the goal is steadier outcomes versus holding stock alone.
  - **Strikes**: **Stability zone:** Between the protection level (92.00) and the call strike (108.00), the goal is steadier outcomes versus holding stock alone. **Stability zone:** Between the protection level (92.00) and the call strike (108.00), the goal is steadier outcomes versus holding stock alone.
  - **Breakevens**: **Stability zone:** Between the protection level (92.00) and the call strike (108.00), the goal is steadier outcomes versus holding stock alone.
  - **Low**: **Protection working:** Below the put strike (92.00), the hedge is designed to limit further downside.
  - **High**: **Upside limited:** Above your call strike (108.00), further upside is typically capped because shares may be called away.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, the put sets the floor for the full position (100 of 100 shares). At expiry below $92.00, downside is protected on the collared shares. Maximum combined loss (at expiry): $800.00.
  overlay_pnl=-800.0, stock_only_pnl=-800.0, delta_vs_stock=0.0
  Anchors: Lower Strike@92.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, P&L is primarily driven by the shares for the full position (100 of 100 shares). At expiry in this range, the collar legs expire worthless on the collared shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0, Lower Strike@92.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, upside is limited by the call strike for the full position (100 of 100 shares). At expiry above $108.00, shares may be called away at the strike and upside is capped on the collared shares. Maximum combined profit (at expiry): $800.00.
  overlay_pnl=800.0, stock_only_pnl=800.0, delta_vs_stock=0.0
  Anchors: Lower Strike@92.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

---

## Strategy: Bull Call Spread (ID=13, Group=Vertical Spreads, Subgroup=Bullish, Kind=OPTIONS)

### Options Only

**Rule matched**: call_spread_debit_v1 (v1.0)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Higher-price scenario:** Upside payoff mechanics dominate here.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: At expiry below $92.00, both calls expire worthless and the position loses the debit paid. Maximum loss equals the debit paid: $40,000.00 total ($400.00 per share). ROI at $92.00 is -100.0%.
  overlay_pnl=-800.0, stock_only_pnl=0.0, delta_vs_stock=-800.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: At expiry between $92.00 and $108.00, intrinsic value increases as price rises toward the upper strike. Breakeven is around $100.00. Maximum loss remains limited to the debit paid: $40,000.00 total ($400.00 per share). Maximum profit is $800.00.
  overlay_pnl=-2.842170943040401e-14, stock_only_pnl=0.0, delta_vs_stock=-2.842170943040401e-14
  Anchors: Lower Strike@92.0, Upper Strike@108.0, Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: At expiry above $108.00, gains are capped at maximum profit. Maximum profit is $800.00. ROI at $108.00 is 100.0%.
  overlay_pnl=800.0, stock_only_pnl=0.0, delta_vs_stock=800.0
  Anchors: Upper Strike@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $800.00 on 1 contracts paid.
  overlay_pnl=-1600.0, stock_only_pnl=-800.0, delta_vs_stock=-800.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $800.00 on 1 contracts paid.
  overlay_pnl=-2.842170943040401e-14, stock_only_pnl=0.0, delta_vs_stock=-2.842170943040401e-14
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $800.00 on 1 contracts paid.
  overlay_pnl=1600.0, stock_only_pnl=800.0, delta_vs_stock=800.0
  Anchors: Upper Strike@108.0

---

## Strategy: Bear Put Spread (ID=14, Group=Vertical Spreads, Subgroup=Bearish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Higher-price scenario:** Upside payoff mechanics dominate here.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses can increase. At expiry below $92.00, gains are capped at maximum profit. Maximum loss equals the debit paid: $40,000.00 total ($400.00 per share). ROI at $92.00 is 100.0%.
  overlay_pnl=800.0, stock_only_pnl=0.0, delta_vs_stock=800.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, outcomes depend on where the stock settles. At expiry between $92.00 and $108.00, intrinsic value builds toward maximum profit. Breakeven is around $100.00. Maximum loss remains limited to the debit paid: $40,000.00 total ($400.00 per share). Maximum profit is $800.00.
  overlay_pnl=-2.842170943040401e-14, stock_only_pnl=0.0, delta_vs_stock=-2.842170943040401e-14
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses can increase. At expiry above $108.00, both puts expire worthless. Maximum profit is $800.00. ROI at $108.00 is -100.0%.
  overlay_pnl=-800.0, stock_only_pnl=0.0, delta_vs_stock=-800.0
  Anchors: Upper Strike@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $800.00 on 1 contracts paid.
  overlay_pnl=-2.842170943040401e-14, stock_only_pnl=0.0, delta_vs_stock=-2.842170943040401e-14
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $800.00 on 1 contracts paid.
  overlay_pnl=-2.842170943040401e-14, stock_only_pnl=0.0, delta_vs_stock=-2.842170943040401e-14
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $800.00 on 1 contracts paid.
  overlay_pnl=-2.842170943040401e-14, stock_only_pnl=0.0, delta_vs_stock=-2.842170943040401e-14
  Anchors: Current Market Price@100.0

---

## Strategy: Bear Call Spread (ID=15, Group=Vertical Spreads, Subgroup=Bearish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Higher-price scenario:** Upside payoff mechanics dominate here.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses can increase. At expiry below $92.00, the spread seeks to retain the net credit. Maximum loss is $800.00.
  overlay_pnl=800.0, stock_only_pnl=0.0, delta_vs_stock=800.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, outcomes depend on where the stock settles. At expiry between $92.00 and $108.00, the spread seeks to retain the net credit. Net option premium (total): $40,000.00 on 1 contracts received Breakeven is around $100.00.
  overlay_pnl=2.842170943040401e-14, stock_only_pnl=0.0, delta_vs_stock=2.842170943040401e-14
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses can increase. At expiry above the short strike, losses increase toward the hedge strike ($108.00). Maximum loss is $800.00.
  overlay_pnl=-800.0, stock_only_pnl=0.0, delta_vs_stock=-800.0
  Anchors: Upper Strike@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $800.00 on 1 contracts received.
  overlay_pnl=2.842170943040401e-14, stock_only_pnl=0.0, delta_vs_stock=2.842170943040401e-14
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $800.00 on 1 contracts received.
  overlay_pnl=2.842170943040401e-14, stock_only_pnl=0.0, delta_vs_stock=2.842170943040401e-14
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $800.00 on 1 contracts received.
  overlay_pnl=2.842170943040401e-14, stock_only_pnl=0.0, delta_vs_stock=2.842170943040401e-14
  Anchors: Current Market Price@100.0

---

## Strategy: Bull Put Spread (ID=16, Group=Vertical Spreads, Subgroup=Bullish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Higher-price scenario:** Upside payoff mechanics dominate here.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses can increase. At expiry below the short strike, losses increase toward the hedge strike ($92.00). Maximum loss is $800.00.
  overlay_pnl=-800.0, stock_only_pnl=0.0, delta_vs_stock=-800.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, outcomes depend on where the stock settles. At expiry between $92.00 and $108.00, the spread seeks to retain the net credit. Net option premium (total): $40,000.00 on 1 contracts received Breakeven is around $100.00.
  overlay_pnl=2.842170943040401e-14, stock_only_pnl=0.0, delta_vs_stock=2.842170943040401e-14
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses can increase. At expiry above $108.00, the spread seeks to retain the net credit. Maximum loss is $800.00.
  overlay_pnl=800.0, stock_only_pnl=0.0, delta_vs_stock=800.0
  Anchors: Upper Strike@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $800.00 on 1 contracts received.
  overlay_pnl=-1600.0, stock_only_pnl=-800.0, delta_vs_stock=-800.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $800.00 on 1 contracts received.
  overlay_pnl=2.842170943040401e-14, stock_only_pnl=0.0, delta_vs_stock=2.842170943040401e-14
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $800.00 on 1 contracts received.
  overlay_pnl=1600.0, stock_only_pnl=800.0, delta_vs_stock=800.0
  Anchors: Upper Strike@108.0

---

## Strategy: Call Ratio Backspread (ID=17, Group=Ratio Spreads, Subgroup=Bullish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses can increase. At expiry below $92.00, the spread seeks to retain the net credit. Maximum loss is $990.00.
  overlay_pnl=610.0, stock_only_pnl=0.0, delta_vs_stock=610.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, outcomes depend on where the stock settles. At expiry between $92.00 and $108.00, the spread seeks to retain the net credit. Net option premium (total): $20,333.00 on 1 contracts received Breakeven is around $98.10.
  overlay_pnl=-189.99999999999997, stock_only_pnl=0.0, delta_vs_stock=-189.99999999999997
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses can increase. At expiry above the short strike, losses increase toward the hedge strike ($108.00). Maximum loss is $990.00.
  overlay_pnl=-990.0, stock_only_pnl=0.0, delta_vs_stock=-990.0
  Anchors: Upper Strike@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $610.00 on 1 contracts received.
  overlay_pnl=-190.0, stock_only_pnl=-800.0, delta_vs_stock=610.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $610.00 on 1 contracts received.
  overlay_pnl=-189.99999999999997, stock_only_pnl=0.0, delta_vs_stock=-189.99999999999997
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $610.00 on 1 contracts received.
  overlay_pnl=-190.0, stock_only_pnl=800.0, delta_vs_stock=-990.0
  Anchors: Upper Strike@108.0

---

## Strategy: Put Ratio Backspread (ID=18, Group=Ratio Spreads, Subgroup=Bearish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **High‑risk zone:** Losses may continue to grow if the move extends. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **High‑risk zone:** Losses may continue to grow if the move extends.
  - **High**: **Higher-price scenario:** Upside payoff mechanics dominate here.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses can increase. At expiry below the short strike, losses increase toward the hedge strike ($92.00). ROI at $92.00 is -100.0%.
  overlay_pnl=-990.0, stock_only_pnl=0.0, delta_vs_stock=-990.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, outcomes depend on where the stock settles. At expiry between $92.00 and $108.00, the spread seeks to retain the net credit. Net option premium (total): $20,333.00 on 1 contracts received Breakeven is around $82.10.
  overlay_pnl=-189.99999999999997, stock_only_pnl=0.0, delta_vs_stock=-189.99999999999997
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses can increase. At expiry above $108.00, the spread seeks to retain the net credit. ROI at $108.00 is 61.6%.
  overlay_pnl=610.0, stock_only_pnl=0.0, delta_vs_stock=610.0
  Anchors: Upper Strike@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,220.00 on 2 contracts received.
  overlay_pnl=-1790.0, stock_only_pnl=-800.0, delta_vs_stock=-990.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,220.00 on 2 contracts received.
  overlay_pnl=-189.99999999999997, stock_only_pnl=0.0, delta_vs_stock=-189.99999999999997
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,220.00 on 2 contracts received.
  overlay_pnl=1410.0, stock_only_pnl=800.0, delta_vs_stock=610.0
  Anchors: Upper Strike@108.0

---

## Strategy: Call Ratio Spread (ID=19, Group=Ratio Spreads, Subgroup=Bearish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **High‑risk zone:** Losses may continue to grow if the move extends.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **High‑risk zone:** Losses may continue to grow if the move extends.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses can increase. At expiry below $92.00, both calls expire worthless. Maximum loss equals the debit paid: $20,333.00 total ($203.33 per share). ROI at $92.00 is -21.9%.
  overlay_pnl=-610.0, stock_only_pnl=0.0, delta_vs_stock=-610.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, outcomes depend on where the stock settles. At expiry between $92.00 and $108.00, intrinsic value builds toward maximum profit. Breakeven is around $98.10. Maximum loss remains limited to the debit paid: $20,333.00 total ($203.33 per share). Maximum profit is $990.00.
  overlay_pnl=189.99999999999997, stock_only_pnl=0.0, delta_vs_stock=189.99999999999997
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses can increase. At expiry above $108.00, gains are capped at maximum profit. Maximum profit is $990.00. ROI at $108.00 is 35.6%.
  overlay_pnl=990.0, stock_only_pnl=0.0, delta_vs_stock=990.0
  Anchors: Upper Strike@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Higher-price scenario:** Upside payoff mechanics dominate here.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,220.00 on 2 contracts paid.
  overlay_pnl=-1410.0, stock_only_pnl=-800.0, delta_vs_stock=-610.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,220.00 on 2 contracts paid.
  overlay_pnl=189.99999999999997, stock_only_pnl=0.0, delta_vs_stock=189.99999999999997
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,220.00 on 2 contracts paid.
  overlay_pnl=1790.0, stock_only_pnl=800.0, delta_vs_stock=990.0
  Anchors: Upper Strike@108.0

---

## Strategy: Put Ratio Spread (ID=20, Group=Ratio Spreads, Subgroup=Bullish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Lower-price scenario:** Downside payoff mechanics dominate here. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Higher-price scenario:** Upside payoff mechanics dominate here.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses can increase. At expiry below $92.00, gains are capped at maximum profit. Maximum loss equals the debit paid: $20,333.00 total ($203.33 per share). ROI at $92.00 is 12.1%.
  overlay_pnl=990.0, stock_only_pnl=0.0, delta_vs_stock=990.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, outcomes depend on where the stock settles. At expiry between $92.00 and $108.00, intrinsic value builds toward maximum profit. Breakeven is around $82.10. Maximum loss remains limited to the debit paid: $20,333.00 total ($203.33 per share). Maximum profit is $990.00.
  overlay_pnl=189.99999999999997, stock_only_pnl=0.0, delta_vs_stock=189.99999999999997
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses can increase. At expiry above $108.00, both puts expire worthless. Maximum profit is $990.00. ROI at $108.00 is -7.4%.
  overlay_pnl=-610.0, stock_only_pnl=0.0, delta_vs_stock=-610.0
  Anchors: Upper Strike@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $610.00 on 1 contracts paid.
  overlay_pnl=190.0, stock_only_pnl=-800.0, delta_vs_stock=990.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $610.00 on 1 contracts paid.
  overlay_pnl=189.99999999999997, stock_only_pnl=0.0, delta_vs_stock=189.99999999999997
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $610.00 on 1 contracts paid.
  overlay_pnl=190.0, stock_only_pnl=800.0, delta_vs_stock=-610.0
  Anchors: Upper Strike@108.0

---

## Strategy: Bull Call Ladder (ID=21, Group=Ladders, Subgroup=Bullish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **High‑risk zone:** Losses may continue to grow if the move extends.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **High‑risk zone:** Losses may continue to grow if the move extends.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. Maximum loss equals the debit paid: $41,667.00 total ($416.67 per share). ROI at $100.00 is 7.4%.
  overlay_pnl=250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=250.0000000000001
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Breakeven is around $97.50. Maximum loss remains limited to the debit paid: $41,667.00 total ($416.67 per share). Maximum profit is $250.00.
  overlay_pnl=250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=250.0000000000001
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. Maximum profit is $250.00. ROI at $100.00 is 7.4%.
  overlay_pnl=250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=250.0000000000001
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,500.00 on 2 contracts paid.
  overlay_pnl=250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=250.0000000000001
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,500.00 on 2 contracts paid.
  overlay_pnl=250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=250.0000000000001
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,500.00 on 2 contracts paid.
  overlay_pnl=250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=250.0000000000001
  Anchors: Current Market Price@100.0

---

## Strategy: Bear Put Ladder (ID=22, Group=Ladders, Subgroup=Bearish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Lower-price scenario:** Downside payoff mechanics dominate here. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. Maximum loss equals the debit paid: $41,667.00 total ($416.67 per share). ROI at $100.00 is 3.0%.
  overlay_pnl=250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=250.0000000000001
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Breakeven is around $82.50. Maximum loss remains limited to the debit paid: $41,667.00 total ($416.67 per share). Maximum profit is $250.00.
  overlay_pnl=250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=250.0000000000001
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. Maximum profit is $250.00. ROI at $100.00 is 3.0%.
  overlay_pnl=250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=250.0000000000001
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,250.00 on 1 contracts paid.
  overlay_pnl=250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=250.0000000000001
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,250.00 on 1 contracts paid.
  overlay_pnl=250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=250.0000000000001
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,250.00 on 1 contracts paid.
  overlay_pnl=250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=250.0000000000001
  Anchors: Current Market Price@100.0

---

## Strategy: Bear Call Ladder (ID=23, Group=Ladders, Subgroup=Bearish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. Maximum loss is $250.00.
  overlay_pnl=-250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-250.0000000000001
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Net option premium (total): $41,667.00 on 1 contracts received Breakeven is around $97.50.
  overlay_pnl=-250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-250.0000000000001
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. Maximum loss is $250.00.
  overlay_pnl=-250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-250.0000000000001
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,250.00 on 1 contracts received.
  overlay_pnl=-250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-250.0000000000001
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,250.00 on 1 contracts received.
  overlay_pnl=-250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-250.0000000000001
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,250.00 on 1 contracts received.
  overlay_pnl=-250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-250.0000000000001
  Anchors: Current Market Price@100.0

---

## Strategy: Bull Put Ladder (ID=24, Group=Ladders, Subgroup=Bullish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **High‑risk zone:** Losses may continue to grow if the move extends. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **High‑risk zone:** Losses may continue to grow if the move extends.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. ROI at $100.00 is -100.0%.
  overlay_pnl=-250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-250.0000000000001
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Net option premium (total): $41,667.00 on 1 contracts received Breakeven is around $82.50.
  overlay_pnl=-250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-250.0000000000001
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. ROI at $100.00 is -100.0%.
  overlay_pnl=-250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-250.0000000000001
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,500.00 on 2 contracts received.
  overlay_pnl=-250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-250.0000000000001
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,500.00 on 2 contracts received.
  overlay_pnl=-250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-250.0000000000001
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,500.00 on 2 contracts received.
  overlay_pnl=-250.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-250.0000000000001
  Anchors: Current Market Price@100.0

---

## Strategy: Long Call Butterfly (ID=25, Group=Condors & Flys, Subgroup=Short Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: call_spread_debit_v1 (v1.0)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $97.76
  Body: At expiry below --, both calls expire worthless and the position loses the debit paid. Maximum loss equals the debit paid: $31,900.00 total ($319.00 per share). ROI at $97.76 is 0.0%.
  overlay_pnl=6.252776074688882e-13, stock_only_pnl=0.0, delta_vs_stock=6.252776074688882e-13
  Anchors: Downside (15%)@85.0

  **Stagnant Case**
  Condition: If stock stays between $97.76 and $102.24
  Body: At expiry between -- and --, intrinsic value increases as price rises toward the upper strike. Breakeven is around $97.76. Maximum loss remains limited to the debit paid: $31,900.00 total ($319.00 per share). Maximum profit is $224.00.
  overlay_pnl=224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=224.0000000000001
  Anchors: Downside (15%)@85.0, Current Market Price@100.0, Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $102.24
  Body: At expiry above --, gains are capped at maximum profit. Maximum profit is $224.00. ROI at $102.24 is 0.0%.
  overlay_pnl=6.252776074688882e-13, stock_only_pnl=0.0, delta_vs_stock=6.252776074688882e-13
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,552.00 on 2 contracts paid.
  overlay_pnl=224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=224.0000000000001
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,552.00 on 2 contracts paid.
  overlay_pnl=224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=224.0000000000001
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,552.00 on 2 contracts paid.
  overlay_pnl=224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=224.0000000000001
  Anchors: Current Market Price@100.0

---

## Strategy: Long Put Butterfly (ID=26, Group=Condors & Flys, Subgroup=Short Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. Maximum loss equals the debit paid: $31,900.00 total ($319.00 per share). ROI at $100.00 is 17.6%.
  overlay_pnl=224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=224.0000000000001
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Breakeven is around $97.76. Maximum loss remains limited to the debit paid: $31,900.00 total ($319.00 per share). Maximum profit is $224.00.
  overlay_pnl=224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=224.0000000000001
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. Maximum profit is $224.00. ROI at $100.00 is 17.6%.
  overlay_pnl=224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=224.0000000000001
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,552.00 on 2 contracts paid.
  overlay_pnl=224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=224.0000000000001
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,552.00 on 2 contracts paid.
  overlay_pnl=224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=224.0000000000001
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,552.00 on 2 contracts paid.
  overlay_pnl=224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=224.0000000000001
  Anchors: Current Market Price@100.0

---

## Strategy: Iron Butterfly (ID=27, Group=Condors & Flys, Subgroup=Short Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: iron_condor_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $97.76
  Body: Below --, losses build toward the lower hedge at --. At expiry below --, losses increase toward the lower hedge at --. Maximum loss is $1,276.00.
  overlay_pnl=5.115907697472721e-13, stock_only_pnl=0.0, delta_vs_stock=5.115907697472721e-13
  Anchors: Downside (15%)@85.0, Current Market Price@100.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $97.76 and $102.24
  Body: Between -- and --, the short options stay out of the money. At expiry in this range, the short options expire worthless and the strategy retains the net credit. Net option premium (total): $5,600.00 on 1 contracts received Breakeven is around $97.76.
  overlay_pnl=224.0, stock_only_pnl=0.0, delta_vs_stock=224.0
  Anchors: Current Market Price@100.0, Upside (15%)@115.0, Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $102.24
  Body: Above --, losses build toward the upper hedge at --. At expiry above --, losses increase toward the upper hedge at --. Maximum loss is $1,276.00.
  overlay_pnl=5.115907697472721e-13, stock_only_pnl=0.0, delta_vs_stock=5.115907697472721e-13
  Anchors: Upside (15%)@115.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $224.00 on 1 contracts received.
  overlay_pnl=224.0, stock_only_pnl=0.0, delta_vs_stock=224.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $224.00 on 1 contracts received.
  overlay_pnl=224.0, stock_only_pnl=0.0, delta_vs_stock=224.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $224.00 on 1 contracts received.
  overlay_pnl=224.0, stock_only_pnl=0.0, delta_vs_stock=224.0
  Anchors: Current Market Price@100.0

---

## Strategy: Long Call Condor (ID=28, Group=Condors & Flys, Subgroup=Short Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses can increase. At expiry below $92.00, both calls expire worthless. Maximum loss equals the debit paid: $25,500.00 total ($255.00 per share). ROI at $92.00 is 17.6%.
  overlay_pnl=180.0, stock_only_pnl=0.0, delta_vs_stock=180.0
  Anchors: Strike (Lower Middle)@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, outcomes depend on where the stock settles. At expiry between $92.00 and $108.00, intrinsic value builds toward maximum profit. Breakeven is around $90.20. Maximum loss remains limited to the debit paid: $25,500.00 total ($255.00 per share). Maximum profit is $180.00.
  overlay_pnl=180.0, stock_only_pnl=0.0, delta_vs_stock=180.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses can increase. At expiry above $108.00, gains are capped at maximum profit. Maximum profit is $180.00. ROI at $108.00 is 17.6%.
  overlay_pnl=180.0, stock_only_pnl=0.0, delta_vs_stock=180.0
  Anchors: Strike (Upper Middle)@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,040.00 on 2 contracts paid.
  overlay_pnl=-620.0, stock_only_pnl=-800.0, delta_vs_stock=180.0
  Anchors: Strike (Lower Middle)@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,040.00 on 2 contracts paid.
  overlay_pnl=180.0, stock_only_pnl=0.0, delta_vs_stock=180.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,040.00 on 2 contracts paid.
  overlay_pnl=980.0, stock_only_pnl=800.0, delta_vs_stock=180.0
  Anchors: Strike (Upper Middle)@108.0

---

## Strategy: Long Put Condor (ID=29, Group=Condors & Flys, Subgroup=Short Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses can increase. At expiry below $92.00, gains are capped at maximum profit. Maximum loss equals the debit paid: $25,500.00 total ($255.00 per share). ROI at $92.00 is 17.6%.
  overlay_pnl=180.0, stock_only_pnl=0.0, delta_vs_stock=180.0
  Anchors: Strike (Lower Middle)@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, outcomes depend on where the stock settles. At expiry between $92.00 and $108.00, intrinsic value builds toward maximum profit. Breakeven is around $90.20. Maximum loss remains limited to the debit paid: $25,500.00 total ($255.00 per share). Maximum profit is $180.00.
  overlay_pnl=180.0, stock_only_pnl=0.0, delta_vs_stock=180.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses can increase. At expiry above $108.00, both puts expire worthless. Maximum profit is $180.00. ROI at $108.00 is 17.6%.
  overlay_pnl=180.0, stock_only_pnl=0.0, delta_vs_stock=180.0
  Anchors: Strike (Upper Middle)@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,040.00 on 2 contracts paid.
  overlay_pnl=-620.0, stock_only_pnl=-800.0, delta_vs_stock=180.0
  Anchors: Strike (Lower Middle)@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,040.00 on 2 contracts paid.
  overlay_pnl=180.0, stock_only_pnl=0.0, delta_vs_stock=180.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,040.00 on 2 contracts paid.
  overlay_pnl=980.0, stock_only_pnl=800.0, delta_vs_stock=180.0
  Anchors: Strike (Upper Middle)@108.0

---

## Strategy: Iron Condor (ID=30, Group=Condors & Flys, Subgroup=Short Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: iron_condor_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses build toward the lower hedge at $80.00. At expiry below $92.00, losses increase toward the lower hedge at $80.00. ROI at $92.00 is 17.6%.
  overlay_pnl=180.0, stock_only_pnl=0.0, delta_vs_stock=180.0
  Anchors: Strike (Lowest)@80.0, Strike (Lower Middle)@92.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, the short options stay out of the money. At expiry in this range, the short options expire worthless and the strategy retains the net credit. Net option premium (total): $4,500.00 on 1 contracts received Breakeven is around $90.20.
  overlay_pnl=180.0, stock_only_pnl=0.0, delta_vs_stock=180.0
  Anchors: Strike (Lower Middle)@92.0, Strike (Upper Middle)@108.0, Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses build toward the upper hedge at $120.00. At expiry above $108.00, losses increase toward the upper hedge at $120.00. ROI at $108.00 is 17.6%.
  overlay_pnl=180.0, stock_only_pnl=0.0, delta_vs_stock=180.0
  Anchors: Strike (Upper Middle)@108.0, Strike (Highest)@120.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $180.00 on 1 contracts received.
  overlay_pnl=-620.0, stock_only_pnl=-800.0, delta_vs_stock=180.0
  Anchors: Strike (Lower Middle)@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $180.00 on 1 contracts received.
  overlay_pnl=180.0, stock_only_pnl=0.0, delta_vs_stock=180.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $180.00 on 1 contracts received.
  overlay_pnl=980.0, stock_only_pnl=800.0, delta_vs_stock=180.0
  Anchors: Strike (Upper Middle)@108.0

---

## Strategy: Short Call Butterfly (ID=31, Group=Condors & Flys, Subgroup=Long Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. Maximum loss is $224.00.
  overlay_pnl=-224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-224.0000000000001
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Net option premium (total): $31,900.00 on 1 contracts received Breakeven is around $97.76.
  overlay_pnl=-224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-224.0000000000001
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. Maximum loss is $224.00.
  overlay_pnl=-224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-224.0000000000001
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,552.00 on 2 contracts received.
  overlay_pnl=-224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-224.0000000000001
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,552.00 on 2 contracts received.
  overlay_pnl=-224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-224.0000000000001
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,552.00 on 2 contracts received.
  overlay_pnl=-224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-224.0000000000001
  Anchors: Current Market Price@100.0

---

## Strategy: Short Put Butterfly (ID=32, Group=Condors & Flys, Subgroup=Long Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. Maximum loss is $224.00.
  overlay_pnl=-224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-224.0000000000001
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Net option premium (total): $31,900.00 on 1 contracts received Breakeven is around $97.76.
  overlay_pnl=-224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-224.0000000000001
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. Maximum loss is $224.00.
  overlay_pnl=-224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-224.0000000000001
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,552.00 on 2 contracts received.
  overlay_pnl=-224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-224.0000000000001
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,552.00 on 2 contracts received.
  overlay_pnl=-224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-224.0000000000001
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,552.00 on 2 contracts received.
  overlay_pnl=-224.0000000000001, stock_only_pnl=0.0, delta_vs_stock=-224.0000000000001
  Anchors: Current Market Price@100.0

---

## Strategy: Rev Iron Butterfly (ID=33, Group=Condors & Flys, Subgroup=Long Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: iron_condor_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $97.76
  Body: Below --, losses build toward the lower hedge at --. At expiry below --, losses increase toward the lower hedge at --. Maximum loss is $224.00. ROI at $97.76 is -0.0%.
  overlay_pnl=-5.115907697472721e-13, stock_only_pnl=0.0, delta_vs_stock=-5.115907697472721e-13
  Anchors: Downside (15%)@85.0, Current Market Price@100.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $97.76 and $102.24
  Body: Between -- and --, the short options stay out of the money. At expiry in this range, the short options expire worthless and the strategy retains the net credit. Breakeven is around $97.76.
  overlay_pnl=-224.0, stock_only_pnl=0.0, delta_vs_stock=-224.0
  Anchors: Current Market Price@100.0, Upside (15%)@115.0, Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $102.24
  Body: Above --, losses build toward the upper hedge at --. At expiry above --, losses increase toward the upper hedge at --. Maximum loss is $224.00. ROI at $102.24 is -0.0%.
  overlay_pnl=-5.115907697472721e-13, stock_only_pnl=0.0, delta_vs_stock=-5.115907697472721e-13
  Anchors: Upside (15%)@115.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $224.00 on 1 contracts paid.
  overlay_pnl=-224.0, stock_only_pnl=0.0, delta_vs_stock=-224.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $224.00 on 1 contracts paid.
  overlay_pnl=-224.0, stock_only_pnl=0.0, delta_vs_stock=-224.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $224.00 on 1 contracts paid.
  overlay_pnl=-224.0, stock_only_pnl=0.0, delta_vs_stock=-224.0
  Anchors: Current Market Price@100.0

---

## Strategy: Short Call Condor (ID=34, Group=Condors & Flys, Subgroup=Long Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses can increase. At expiry below $92.00, the spread seeks to retain the net credit. Maximum loss is $180.00.
  overlay_pnl=-180.0, stock_only_pnl=0.0, delta_vs_stock=-180.0
  Anchors: Strike (Lower Middle)@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, outcomes depend on where the stock settles. At expiry between $92.00 and $108.00, the spread seeks to retain the net credit. Net option premium (total): $25,500.00 on 1 contracts received Breakeven is around $90.20.
  overlay_pnl=-180.0, stock_only_pnl=0.0, delta_vs_stock=-180.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses can increase. At expiry above the short strike, losses increase toward the hedge strike ($120.00). Maximum loss is $180.00.
  overlay_pnl=-180.0, stock_only_pnl=0.0, delta_vs_stock=-180.0
  Anchors: Strike (Upper Middle)@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,040.00 on 2 contracts received.
  overlay_pnl=-980.0, stock_only_pnl=-800.0, delta_vs_stock=-180.0
  Anchors: Strike (Lower Middle)@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,040.00 on 2 contracts received.
  overlay_pnl=-180.0, stock_only_pnl=0.0, delta_vs_stock=-180.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,040.00 on 2 contracts received.
  overlay_pnl=620.0, stock_only_pnl=800.0, delta_vs_stock=-180.0
  Anchors: Strike (Upper Middle)@108.0

---

## Strategy: Short Put Condor (ID=35, Group=Condors & Flys, Subgroup=Long Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses can increase. At expiry below the short strike, losses increase toward the hedge strike ($80.00). ROI at $92.00 is -100.0%.
  overlay_pnl=-180.0, stock_only_pnl=0.0, delta_vs_stock=-180.0
  Anchors: Strike (Lower Middle)@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, outcomes depend on where the stock settles. At expiry between $92.00 and $108.00, the spread seeks to retain the net credit. Net option premium (total): $25,500.00 on 1 contracts received Breakeven is around $90.20.
  overlay_pnl=-180.0, stock_only_pnl=0.0, delta_vs_stock=-180.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses can increase. At expiry above $108.00, the spread seeks to retain the net credit. ROI at $108.00 is -100.0%.
  overlay_pnl=-180.0, stock_only_pnl=0.0, delta_vs_stock=-180.0
  Anchors: Strike (Upper Middle)@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,040.00 on 2 contracts received.
  overlay_pnl=-980.0, stock_only_pnl=-800.0, delta_vs_stock=-180.0
  Anchors: Strike (Lower Middle)@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,040.00 on 2 contracts received.
  overlay_pnl=-180.0, stock_only_pnl=0.0, delta_vs_stock=-180.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $2,040.00 on 2 contracts received.
  overlay_pnl=620.0, stock_only_pnl=800.0, delta_vs_stock=-180.0
  Anchors: Strike (Upper Middle)@108.0

---

## Strategy: Rev Iron Condor (ID=36, Group=Condors & Flys, Subgroup=Long Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: iron_condor_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses build toward the lower hedge at $80.00. At expiry below $92.00, losses increase toward the lower hedge at $80.00. ROI at $92.00 is -100.0%.
  overlay_pnl=-180.0, stock_only_pnl=0.0, delta_vs_stock=-180.0
  Anchors: Strike (Lowest)@80.0, Strike (Lower Middle)@92.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, the short options stay out of the money. At expiry in this range, the short options expire worthless and the strategy retains the net credit. Breakeven is around $90.20.
  overlay_pnl=-180.0, stock_only_pnl=0.0, delta_vs_stock=-180.0
  Anchors: Strike (Lower Middle)@92.0, Strike (Upper Middle)@108.0, Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses build toward the upper hedge at $120.00. At expiry above $108.00, losses increase toward the upper hedge at $120.00. ROI at $108.00 is -100.0%.
  overlay_pnl=-180.0, stock_only_pnl=0.0, delta_vs_stock=-180.0
  Anchors: Strike (Upper Middle)@108.0, Strike (Highest)@120.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Scenario overview:** Review P&L sensitivity around this level.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $180.00 on 1 contracts paid.
  overlay_pnl=-980.0, stock_only_pnl=-800.0, delta_vs_stock=-180.0
  Anchors: Strike (Lower Middle)@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $180.00 on 1 contracts paid.
  overlay_pnl=-180.0, stock_only_pnl=0.0, delta_vs_stock=-180.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $180.00 on 1 contracts paid.
  overlay_pnl=620.0, stock_only_pnl=800.0, delta_vs_stock=-180.0
  Anchors: Strike (Upper Middle)@108.0

---

## Strategy: Long Straddle (ID=37, Group=Straddles, Subgroup=Long Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Strikes**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Breakevens**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time. **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Low**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **High**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. ROI at $100.00 is -100.0%.
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Breakeven is around $95.00.
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. ROI at $100.00 is -100.0%.
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Strikes**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Breakevens**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Low**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **High**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $500.00 on 1 contracts paid.
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $500.00 on 1 contracts paid.
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $500.00 on 1 contracts paid.
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Current Market Price@100.0

---

## Strategy: Short Straddle (ID=38, Group=Straddles, Subgroup=Short Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.
  - **Strikes**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.
  - **Breakevens**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium. **High‑risk zone:** With a continued large move, losses can keep growing (risk is not naturally capped).
  - **Low**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.
  - **High**: **High‑risk zone:** With a continued large move, losses can keep growing (risk is not naturally capped).

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. ROI at $100.00 is 11.1%.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Net option premium (total): $25,000.00 on 1 contracts received Breakeven is around $95.00.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. ROI at $100.00 is 11.1%.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.
  - **Strikes**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.
  - **Breakevens**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.
  - **Low**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.
  - **High**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $500.00 on 1 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $500.00 on 1 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $500.00 on 1 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

---

## Strategy: Long Strangle (ID=39, Group=Straddles, Subgroup=Long Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.
  - **Strikes**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time. **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.
  - **Breakevens**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time. **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.
  - **Low**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.
  - **High**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses can increase. At expiry below the lower strike, losses increase toward the hedge strike ($92.00). ROI at $92.00 is -100.0%.
  overlay_pnl=-380.0, stock_only_pnl=0.0, delta_vs_stock=-380.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, outcomes depend on where the stock settles. At expiry between the strikes, intrinsic value builds toward maximum profit. Breakeven is around $88.20.
  overlay_pnl=-380.0, stock_only_pnl=0.0, delta_vs_stock=-380.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses can increase. At expiry above the upper strike, losses increase toward the hedge strike ($108.00). ROI at $108.00 is -100.0%.
  overlay_pnl=-380.0, stock_only_pnl=0.0, delta_vs_stock=-380.0
  Anchors: Upper Strike@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.
  - **Strikes**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time. **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.
  - **Breakevens**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.
  - **Low**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.
  - **High**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $380.00 on 1 contracts paid.
  overlay_pnl=-1180.0, stock_only_pnl=-800.0, delta_vs_stock=-380.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $380.00 on 1 contracts paid.
  overlay_pnl=-380.0, stock_only_pnl=0.0, delta_vs_stock=-380.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $380.00 on 1 contracts paid.
  overlay_pnl=420.0, stock_only_pnl=800.0, delta_vs_stock=-380.0
  Anchors: Upper Strike@108.0

---

## Strategy: Short Strangle (ID=40, Group=Straddles, Subgroup=Short Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **Strikes**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium. **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **Breakevens**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium. **High‑risk zone:** With a continued large move, losses can keep growing (risk is not naturally capped).
  - **Low**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **High**: **High‑risk zone:** With a continued large move, losses can keep growing (risk is not naturally capped).

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses can increase. At expiry below the lower strike, losses increase toward the hedge strike ($92.00). ROI at $92.00 is 13.7%.
  overlay_pnl=380.0, stock_only_pnl=0.0, delta_vs_stock=380.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, outcomes depend on where the stock settles. At expiry between the strikes, the strategy seeks to retain the net credit. Net option premium (total): $19,000.00 on 1 contracts received Breakeven is around $88.20.
  overlay_pnl=380.0, stock_only_pnl=0.0, delta_vs_stock=380.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses can increase. At expiry above the upper strike, losses increase toward the hedge strike ($108.00). ROI at $108.00 is 13.7%.
  overlay_pnl=380.0, stock_only_pnl=0.0, delta_vs_stock=380.0
  Anchors: Upper Strike@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **Strikes**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium. **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **Breakevens**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **Low**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **High**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $380.00 on 1 contracts received.
  overlay_pnl=-420.0, stock_only_pnl=-800.0, delta_vs_stock=380.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $380.00 on 1 contracts received.
  overlay_pnl=380.0, stock_only_pnl=0.0, delta_vs_stock=380.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $380.00 on 1 contracts received.
  overlay_pnl=1180.0, stock_only_pnl=800.0, delta_vs_stock=380.0
  Anchors: Upper Strike@108.0

---

## Strategy: Long Guts (ID=41, Group=Straddles, Subgroup=Long Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.
  - **Strikes**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time. **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.
  - **Breakevens**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time. **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.
  - **Low**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.
  - **High**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses can increase. At expiry below the lower strike, losses increase toward the hedge strike ($92.00). ROI at $92.00 is -100.0%.
  overlay_pnl=-380.0, stock_only_pnl=0.0, delta_vs_stock=-380.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, outcomes depend on where the stock settles. At expiry between the strikes, intrinsic value builds toward maximum profit. Breakeven is around $88.20.
  overlay_pnl=-380.00000000000006, stock_only_pnl=0.0, delta_vs_stock=-380.00000000000006
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses can increase. At expiry above the upper strike, losses increase toward the hedge strike ($108.00). ROI at $108.00 is -100.0%.
  overlay_pnl=-380.0, stock_only_pnl=0.0, delta_vs_stock=-380.0
  Anchors: Upper Strike@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.
  - **Strikes**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time. **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.
  - **Breakevens**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.
  - **Low**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.
  - **High**: **Needs movement:** If the stock stays between 92.00 and 108.00, the options can lose value over time.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,980.00 on 1 contracts paid.
  overlay_pnl=-1180.0, stock_only_pnl=-800.0, delta_vs_stock=-380.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,980.00 on 1 contracts paid.
  overlay_pnl=-380.00000000000006, stock_only_pnl=0.0, delta_vs_stock=-380.00000000000006
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,980.00 on 1 contracts paid.
  overlay_pnl=420.0, stock_only_pnl=800.0, delta_vs_stock=-380.0
  Anchors: Upper Strike@108.0

---

## Strategy: Short Guts (ID=42, Group=Straddles, Subgroup=Short Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **Strikes**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium. **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **Breakevens**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium. **High‑risk zone:** With a continued large move, losses can keep growing (risk is not naturally capped).
  - **Low**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **High**: **High‑risk zone:** With a continued large move, losses can keep growing (risk is not naturally capped).

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses can increase. At expiry below the lower strike, losses increase toward the hedge strike ($92.00). ROI at $92.00 is 6.4%.
  overlay_pnl=380.0, stock_only_pnl=0.0, delta_vs_stock=380.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, outcomes depend on where the stock settles. At expiry between the strikes, the strategy seeks to retain the net credit. Net option premium (total): $99,000.00 on 1 contracts received Breakeven is around $88.20.
  overlay_pnl=380.00000000000006, stock_only_pnl=0.0, delta_vs_stock=380.00000000000006
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses can increase. At expiry above the upper strike, losses increase toward the hedge strike ($108.00). ROI at $108.00 is 6.4%.
  overlay_pnl=380.0, stock_only_pnl=0.0, delta_vs_stock=380.0
  Anchors: Upper Strike@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **Strikes**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium. **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **Breakevens**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **Low**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **High**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,980.00 on 1 contracts received.
  overlay_pnl=-420.0, stock_only_pnl=-800.0, delta_vs_stock=380.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,980.00 on 1 contracts received.
  overlay_pnl=380.00000000000006, stock_only_pnl=0.0, delta_vs_stock=380.00000000000006
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,980.00 on 1 contracts received.
  overlay_pnl=1180.0, stock_only_pnl=800.0, delta_vs_stock=380.0
  Anchors: Upper Strike@108.0

---

## Strategy: Strip (ID=43, Group=Straddles, Subgroup=Bearish/Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Strikes**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Breakevens**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time. **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Low**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **High**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. ROI at $100.00 is -100.0%.
  overlay_pnl=-750.0, stock_only_pnl=0.0, delta_vs_stock=-750.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Breakeven is around $96.25.
  overlay_pnl=-750.0, stock_only_pnl=0.0, delta_vs_stock=-750.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. ROI at $100.00 is -100.0%.
  overlay_pnl=-750.0, stock_only_pnl=0.0, delta_vs_stock=-750.0
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Strikes**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Breakevens**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time. **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Low**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **High**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,500.00 on 2 contracts paid.
  overlay_pnl=-750.0, stock_only_pnl=0.0, delta_vs_stock=-750.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,500.00 on 2 contracts paid.
  overlay_pnl=-750.0, stock_only_pnl=0.0, delta_vs_stock=-750.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,500.00 on 2 contracts paid.
  overlay_pnl=-750.0, stock_only_pnl=0.0, delta_vs_stock=-750.0
  Anchors: Current Market Price@100.0

---

## Strategy: Strap (ID=44, Group=Straddles, Subgroup=Bullish/Vol, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Strikes**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Breakevens**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time. **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Low**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **High**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. ROI at $100.00 is -100.0%.
  overlay_pnl=-750.0, stock_only_pnl=0.0, delta_vs_stock=-750.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Breakeven is around $92.50.
  overlay_pnl=-750.0, stock_only_pnl=0.0, delta_vs_stock=-750.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. ROI at $100.00 is -100.0%.
  overlay_pnl=-750.0, stock_only_pnl=0.0, delta_vs_stock=-750.0
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Strikes**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Breakevens**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **Low**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.
  - **High**: **Needs movement:** If the stock stays near the strike (100.00), the options can lose value over time.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $750.00 on 1 contracts paid.
  overlay_pnl=-750.0, stock_only_pnl=0.0, delta_vs_stock=-750.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $750.00 on 1 contracts paid.
  overlay_pnl=-750.0, stock_only_pnl=0.0, delta_vs_stock=-750.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $750.00 on 1 contracts paid.
  overlay_pnl=-750.0, stock_only_pnl=0.0, delta_vs_stock=-750.0
  Anchors: Current Market Price@100.0

---

## Strategy: Covered Short Straddle (ID=45, Group=Straddles, Subgroup=Bullish, Kind=MIXED)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.
  - **Strikes**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.
  - **Breakevens**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.
  - **Low**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.
  - **High**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $500.00 on 1 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $500.00 on 1 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $500.00 on 1 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.
  - **Strikes**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.
  - **Breakevens**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.
  - **Low**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.
  - **High**: **Income zone:** If the stock stays near the strike (100.00), this position is designed to keep more of the premium.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $500.00 on 1 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $500.00 on 1 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $500.00 on 1 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

---

## Strategy: Covered Short Strangle (ID=46, Group=Straddles, Subgroup=Bullish, Kind=MIXED)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **Strikes**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium. **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **Breakevens**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **Low**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **High**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $380.00 on 1 contracts received.
  overlay_pnl=-420.0, stock_only_pnl=-800.0, delta_vs_stock=380.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $380.00 on 1 contracts received.
  overlay_pnl=380.0, stock_only_pnl=0.0, delta_vs_stock=380.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $380.00 on 1 contracts received.
  overlay_pnl=1180.0, stock_only_pnl=800.0, delta_vs_stock=380.0
  Anchors: Upper Strike@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **Strikes**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium. **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **Breakevens**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **Low**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.
  - **High**: **Income zone:** If the stock stays between 92.00 and 108.00, this position is designed to keep more of the premium.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $380.00 on 1 contracts received.
  overlay_pnl=-420.0, stock_only_pnl=-800.0, delta_vs_stock=380.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $380.00 on 1 contracts received.
  overlay_pnl=380.0, stock_only_pnl=0.0, delta_vs_stock=380.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $380.00 on 1 contracts received.
  overlay_pnl=1180.0, stock_only_pnl=800.0, delta_vs_stock=380.0
  Anchors: Upper Strike@108.0

---

## Strategy: Long Box Spread (ID=47, Group=Boxes, Subgroup=Neutral, Kind=OPTIONS)

### Options Only

**Rule matched**: iron_condor_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Higher-price scenario:** Upside payoff mechanics dominate here.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $0.00
  Body: Below --, losses build toward the lower hedge at --. At expiry below --, losses increase toward the lower hedge at --. Maximum loss is $0.00. ROI at $0.00 is 0.0%.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Breakeven 63@92.0, Breakeven 65@108.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $0.00 and $299.00
  Body: Between -- and --, the short options stay out of the money. At expiry in this range, the short options expire worthless and the strategy retains the net credit. Breakeven is around $0.00.
  overlay_pnl=-5.684341886080802e-14, stock_only_pnl=0.0, delta_vs_stock=-5.684341886080802e-14
  Anchors: Breakeven 65@108.0, Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $299.00
  Body: Above --, losses build toward the upper hedge at --. At expiry above --, losses increase toward the upper hedge at --. Maximum loss is $0.00. ROI at $299.00 is 0.0%.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Upside Target (15%)@114.99999999999999, Stock to Infinity@None

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,600.00 on 1 contracts paid.
  overlay_pnl=-800.0, stock_only_pnl=-800.0, delta_vs_stock=0.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,600.00 on 1 contracts paid.
  overlay_pnl=-5.684341886080802e-14, stock_only_pnl=0.0, delta_vs_stock=-5.684341886080802e-14
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,600.00 on 1 contracts paid.
  overlay_pnl=800.0, stock_only_pnl=800.0, delta_vs_stock=0.0
  Anchors: Upper Strike@108.0

---

## Strategy: Short Box Spread (ID=48, Group=Boxes, Subgroup=Neutral, Kind=OPTIONS)

### Options Only

**Rule matched**: iron_condor_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Lower-price scenario:** Downside payoff mechanics dominate here. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here. **Higher-price scenario:** Upside payoff mechanics dominate here.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Higher-price scenario:** Upside payoff mechanics dominate here.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $0.00
  Body: Below --, losses build toward the lower hedge at --. At expiry below --, losses increase toward the lower hedge at --. Maximum loss is $0.00.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Breakeven 63@92.0, Breakeven 65@108.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $0.00 and $299.00
  Body: Between -- and --, the short options stay out of the money. At expiry in this range, the short options expire worthless and the strategy retains the net credit. Net option premium (total): $40,000.00 on 1 contracts received Breakeven is around $0.00.
  overlay_pnl=5.684341886080802e-14, stock_only_pnl=0.0, delta_vs_stock=5.684341886080802e-14
  Anchors: Breakeven 65@108.0, Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $299.00
  Body: Above --, losses build toward the upper hedge at --. At expiry above --, losses increase toward the upper hedge at --. Maximum loss is $0.00.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Upside Target (15%)@114.99999999999999, Stock to Infinity@None

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,600.00 on 1 contracts received.
  overlay_pnl=-800.0, stock_only_pnl=-800.0, delta_vs_stock=0.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,600.00 on 1 contracts received.
  overlay_pnl=5.684341886080802e-14, stock_only_pnl=0.0, delta_vs_stock=5.684341886080802e-14
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the full position (100 of 100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,600.00 on 1 contracts received.
  overlay_pnl=800.0, stock_only_pnl=800.0, delta_vs_stock=0.0
  Anchors: Upper Strike@108.0

---

## Strategy: Synthetic Long Stock (ID=49, Group=Synthetics, Subgroup=Bullish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. Maximum loss is $10,000.00. ROI at $100.00 is 0.0%.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Breakeven is around $100.00.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. Maximum loss is $10,000.00. ROI at $100.00 is 0.0%.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

---

## Strategy: Synthetic Short Stock (ID=50, Group=Synthetics, Subgroup=Bearish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **High‑risk zone:** Losses may continue to grow if the move extends.
  - **High**: **High‑risk zone:** Losses may continue to grow if the move extends.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. ROI at $100.00 is 0.0%.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Maximum profit is $10,000.00. Breakeven is around $100.00.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. ROI at $100.00 is 0.0%.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: collar_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Stability zone:** Between the protection level (100.00) and the call strike (100.00), the goal is steadier outcomes versus holding stock alone.
  - **Strikes**: **Stability zone:** Between the protection level (100.00) and the call strike (100.00), the goal is steadier outcomes versus holding stock alone.
  - **Breakevens**: **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Stability zone:** Between the protection level (100.00) and the call strike (100.00), the goal is steadier outcomes versus holding stock alone. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away.
  - **Low**: **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside.
  - **High**: **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, the put sets the floor for the full position (100 of 100 shares). At expiry below $100.00, downside is protected on the collared shares. Maximum combined loss (at expiry): $0.00.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $100.00 and $100.00
  Body: Between $100.00 and $100.00, P&L is primarily driven by the shares for the full position (100 of 100 shares). At expiry in this range, the collar legs expire worthless on the collared shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0, Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, upside is limited by the call strike for the full position (100 of 100 shares). At expiry above $100.00, shares may be called away at the strike and upside is capped on the collared shares. Maximum combined profit (at expiry): $0.00.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

---

## Strategy: Long Combo (ID=51, Group=Synthetics, Subgroup=Bullish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. Maximum loss is $9,200.00. ROI at $100.00 is 0.0%.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Breakeven is around $92.00.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. Maximum loss is $9,200.00. ROI at $100.00 is 0.0%.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $92.00, combined P&L would be -$800.00 (options contribute +$0.00; the shares contribute -$800.00).
  overlay_pnl=-800.0, stock_only_pnl=-800.0, delta_vs_stock=0.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. At $108.00, combined P&L would be +$800.00 (options contribute +$0.00; the shares contribute +$800.00).
  overlay_pnl=800.0, stock_only_pnl=800.0, delta_vs_stock=0.0
  Anchors: Upper Strike@108.0

---

## Strategy: Short Combo (ID=52, Group=Synthetics, Subgroup=Bearish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **High‑risk zone:** Losses may continue to grow if the move extends.
  - **High**: **High‑risk zone:** Losses may continue to grow if the move extends.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry below this price, losses can increase. ROI at $100.00 is 0.0%.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry within the key range, the strategy seeks to perform best. Maximum profit is $9,200.00. Breakeven is around $92.00.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Around the strikes, outcomes depend on where the stock settles. At expiry above this price, losses can increase. ROI at $100.00 is 0.0%.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: collar_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Stability zone:** Between the protection level (92.00) and the call strike (108.00), the goal is steadier outcomes versus holding stock alone.
  - **Strikes**: **Stability zone:** Between the protection level (92.00) and the call strike (108.00), the goal is steadier outcomes versus holding stock alone. **Stability zone:** Between the protection level (92.00) and the call strike (108.00), the goal is steadier outcomes versus holding stock alone.
  - **Breakevens**: **Stability zone:** Between the protection level (92.00) and the call strike (108.00), the goal is steadier outcomes versus holding stock alone.
  - **Low**: **Protection working:** Below the put strike (92.00), the hedge is designed to limit further downside.
  - **High**: **Upside limited:** Above your call strike (108.00), further upside is typically capped because shares may be called away.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, the put sets the floor for the full position (100 of 100 shares). At expiry below $92.00, downside is protected on the collared shares. Maximum combined loss (at expiry): $800.00.
  overlay_pnl=-800.0, stock_only_pnl=-800.0, delta_vs_stock=0.0
  Anchors: Lower Strike@92.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, P&L is primarily driven by the shares for the full position (100 of 100 shares). At expiry in this range, the collar legs expire worthless on the collared shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0, Lower Strike@92.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, upside is limited by the call strike for the full position (100 of 100 shares). At expiry above $108.00, shares may be called away at the strike and upside is capped on the collared shares. Maximum combined profit (at expiry): $800.00.
  overlay_pnl=800.0, stock_only_pnl=800.0, delta_vs_stock=0.0
  Anchors: Lower Strike@92.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

---

## Strategy: L. Call Syn. Straddle (ID=53, Group=Synthetics, Subgroup=Long Vol, Kind=MIXED)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.
  - **Strikes**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.
  - **Breakevens**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly. **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.
  - **Low**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.
  - **High**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,000.00 on 2 contracts paid.
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,000.00 on 2 contracts paid.
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,000.00 on 2 contracts paid.
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.
  - **Strikes**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.
  - **Breakevens**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly. **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.
  - **Low**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.
  - **High**: **Decision zone:** Near your call strike (100.00), small moves can change the option’s value quickly.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,000.00 on 2 contracts paid.
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,000.00 on 2 contracts paid.
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,000.00 on 2 contracts paid.
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Current Market Price@100.0

---

## Strategy: L. Put Syn. Straddle (ID=54, Group=Synthetics, Subgroup=Long Vol, Kind=MIXED)

### Options Only

**Rule matched**: protective_put_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Buffered exposure:** Between current levels and the protection strike (100.00), you still participate in moves, with downside protection further below.
  - **Strikes**: **Buffered exposure:** Between current levels and the protection strike (100.00), you still participate in moves, with downside protection further below.
  - **Breakevens**: **Buffered exposure:** Between current levels and the protection strike (100.00), you still participate in moves, with downside protection further below. **Buffered exposure:** Between current levels and the protection strike (100.00), you still participate in moves, with downside protection further below.
  - **Low**: **Buffered exposure:** Between current levels and the protection strike (100.00), you still participate in moves, with downside protection further below.
  - **High**: **Buffered exposure:** Between current levels and the protection strike (100.00), you still participate in moves, with downside protection further below.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, the put establishes the floor for the full position (100 of 100 shares). At expiry below $100.00, the put settles at intrinsic value and downside is protected on the protected shares. At $100.00, combined P&L would be -$500.00 (options contribute -$500.00; the shares contribute +$0.00).
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Current Market Price@100.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $100.00 and $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry in this range, protection remains in place on the protected shares. Net option premium (total): $1,000.00 on 2 contracts paid.
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Current Market Price@100.0, Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, upside participation continues for the full position (100 of 100 shares). At expiry above $100.00, the put expires worthless and gains follow the shares on the protected shares. At $100.00, combined P&L would be -$500.00 (options contribute -$500.00; the shares contribute +$0.00).
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Upside Target (15%)@114.99999999999999, Stock to Infinity@None

### With Underlying Position

**Rule matched**: protective_put_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Buffered exposure:** Between current levels and the protection strike (100.00), you still participate in moves, with downside protection further below.
  - **Strikes**: **Buffered exposure:** Between current levels and the protection strike (100.00), you still participate in moves, with downside protection further below.
  - **Breakevens**: **Buffered exposure:** Between current levels and the protection strike (100.00), you still participate in moves, with downside protection further below. **Buffered exposure:** Between current levels and the protection strike (100.00), you still participate in moves, with downside protection further below.
  - **Low**: **Buffered exposure:** Between current levels and the protection strike (100.00), you still participate in moves, with downside protection further below.
  - **High**: **Buffered exposure:** Between current levels and the protection strike (100.00), you still participate in moves, with downside protection further below.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, the put establishes the floor for the full position (100 of 100 shares). At expiry below $100.00, the put settles at intrinsic value and downside is protected on the protected shares. At $100.00, combined P&L would be -$500.00 (options contribute -$500.00; the shares contribute +$0.00).
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Current Market Price@100.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $100.00 and $100.00
  Body: Between $100.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry in this range, protection remains in place on the protected shares. Net option premium (total): $1,000.00 on 2 contracts paid.
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Current Market Price@100.0, Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, upside participation continues for the full position (100 of 100 shares). At expiry above $100.00, the put expires worthless and gains follow the shares on the protected shares. At $100.00, combined P&L would be -$500.00 (options contribute -$500.00; the shares contribute +$0.00).
  overlay_pnl=-500.0, stock_only_pnl=0.0, delta_vs_stock=-500.0
  Anchors: Upside Target (15%)@114.99999999999999, Stock to Infinity@None

---

## Strategy: S. Call Syn. Straddle (ID=55, Group=Synthetics, Subgroup=Short Vol, Kind=MIXED)

### Options Only

**Rule matched**: covered_call_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Income zone:** If the stock stays below your call strike (100.00), premium income can help support returns.
  - **Strikes**: **Income zone:** If the stock stays below your call strike (100.00), premium income can help support returns.
  - **Breakevens**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position. **Income zone:** If the stock stays below your call strike (100.00), premium income can help support returns.
  - **Low**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position.
  - **High**: **Income zone:** If the stock stays below your call strike (100.00), premium income can help support returns.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, downside follows the shares for the full position (100 of 100 shares). At expiry below $100.00, the call expires worthless on the covered shares. Net option premium (total): $1,000.00 on 2 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $100.00 and $100.00
  Body: Between $100.00 and $100.00, gains follow the shares for the full position (100 of 100 shares). At expiry in this range, the call expires worthless on the covered shares. Net option premium (total): $1,000.00 on 2 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0, Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, upside is limited by the call strike for the full position (100 of 100 shares). At expiry above $100.00, shares may be called away at the strike and upside is capped on the covered shares. Maximum combined profit (at expiry): $500.00.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

### With Underlying Position

**Rule matched**: covered_call_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Income zone:** If the stock stays below your call strike (100.00), premium income can help support returns.
  - **Strikes**: **Income zone:** If the stock stays below your call strike (100.00), premium income can help support returns.
  - **Breakevens**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position. **Income zone:** If the stock stays below your call strike (100.00), premium income can help support returns.
  - **Low**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position.
  - **High**: **Income zone:** If the stock stays below your call strike (100.00), premium income can help support returns.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, downside follows the shares for the full position (100 of 100 shares). At expiry below $100.00, the call expires worthless on the covered shares. Net option premium (total): $1,000.00 on 2 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $100.00 and $100.00
  Body: Between $100.00 and $100.00, gains follow the shares for the full position (100 of 100 shares). At expiry in this range, the call expires worthless on the covered shares. Net option premium (total): $1,000.00 on 2 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0, Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, upside is limited by the call strike for the full position (100 of 100 shares). At expiry above $100.00, shares may be called away at the strike and upside is capped on the covered shares. Maximum combined profit (at expiry): $500.00.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

---

## Strategy: S. Put Syn. Straddle (ID=56, Group=Synthetics, Subgroup=Short Vol, Kind=MIXED)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Watch zone:** Near your put strike (100.00), you are closer to being obligated to buy shares at that level.
  - **Strikes**: **Watch zone:** Near your put strike (100.00), you are closer to being obligated to buy shares at that level.
  - **Breakevens**: **Assignment zone:** Below the put strike (100.00), the position behaves more like buying shares at that strike (downside continues below it). **Watch zone:** Near your put strike (100.00), you are closer to being obligated to buy shares at that level.
  - **Low**: **Assignment zone:** Below the put strike (100.00), the position behaves more like buying shares at that strike (downside continues below it).
  - **High**: **Watch zone:** Near your put strike (100.00), you are closer to being obligated to buy shares at that level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,000.00 on 2 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,000.00 on 2 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,000.00 on 2 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Watch zone:** Near your put strike (100.00), you are closer to being obligated to buy shares at that level.
  - **Strikes**: **Watch zone:** Near your put strike (100.00), you are closer to being obligated to buy shares at that level.
  - **Breakevens**: **Assignment zone:** Below the put strike (100.00), the position behaves more like buying shares at that strike (downside continues below it). **Watch zone:** Near your put strike (100.00), you are closer to being obligated to buy shares at that level.
  - **Low**: **Assignment zone:** Below the put strike (100.00), the position behaves more like buying shares at that strike (downside continues below it).
  - **High**: **Watch zone:** Near your put strike (100.00), you are closer to being obligated to buy shares at that level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, losses track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,000.00 on 2 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

  **Stagnant Case**
  Condition: If stock stays near $100.00
  Body: Between $100.00 and $100.00, results follow the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,000.00 on 2 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, gains track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,000.00 on 2 contracts received.
  overlay_pnl=500.0, stock_only_pnl=0.0, delta_vs_stock=500.0
  Anchors: Current Market Price@100.0

---

## Strategy: L. Call Syn. Strangle (ID=57, Group=Synthetics, Subgroup=Long Vol, Kind=MIXED)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **High‑risk zone:** Losses may continue to grow if the move extends. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **High‑risk zone:** Losses may continue to grow if the move extends.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,180.00 on 1 contracts paid.
  overlay_pnl=-380.0, stock_only_pnl=800.0, delta_vs_stock=-1180.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,180.00 on 1 contracts paid.
  overlay_pnl=-380.0, stock_only_pnl=0.0, delta_vs_stock=-380.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,180.00 on 1 contracts paid.
  overlay_pnl=-380.0, stock_only_pnl=-800.0, delta_vs_stock=420.0
  Anchors: Upper Strike@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **High‑risk zone:** Losses may continue to grow if the move extends. **Scenario overview:** Review P&L sensitivity around this level.
  - **Low**: **High‑risk zone:** Losses may continue to grow if the move extends.
  - **High**: **Scenario overview:** Review P&L sensitivity around this level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,180.00 on 1 contracts paid.
  overlay_pnl=-380.0, stock_only_pnl=800.0, delta_vs_stock=-1180.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,180.00 on 1 contracts paid.
  overlay_pnl=-380.0, stock_only_pnl=0.0, delta_vs_stock=-380.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,180.00 on 1 contracts paid.
  overlay_pnl=-380.0, stock_only_pnl=-800.0, delta_vs_stock=420.0
  Anchors: Upper Strike@108.0

---

## Strategy: L. Put Syn. Strangle (ID=58, Group=Synthetics, Subgroup=Long Vol, Kind=MIXED)

### Options Only

**Rule matched**: protective_put_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.
  - **Strikes**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below. **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.
  - **Breakevens**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below. **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.
  - **Low**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.
  - **High**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $108.00
  Body: Below $108.00, the put establishes the floor for the full position (100 of 100 shares). At expiry below $108.00, the put settles at intrinsic value and downside is protected on the protected shares. Maximum combined loss (at expiry): $380.00.
  overlay_pnl=-380.0, stock_only_pnl=800.0, delta_vs_stock=-1180.0
  Anchors: Lower Strike@92.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $100.00 and $108.00
  Body: Between $108.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry in this range, protection remains in place on the protected shares. Net option premium (total): $2,360.00 on 2 contracts paid.
  overlay_pnl=-380.0, stock_only_pnl=0.0, delta_vs_stock=-380.0
  Anchors: Current Market Price@100.0, Lower Strike@92.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, upside participation continues for the full position (100 of 100 shares). At expiry above $100.00, the put expires worthless and gains follow the shares on the protected shares. At $108.00, combined P&L would be -$380.00 (options contribute -$1,180.00; the shares contribute +$800.00).
  overlay_pnl=-380.0, stock_only_pnl=800.0, delta_vs_stock=-1180.0
  Anchors: Upside Target (15%)@114.99999999999999, Stock to Infinity@None

### With Underlying Position

**Rule matched**: protective_put_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.
  - **Strikes**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below. **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.
  - **Breakevens**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below. **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.
  - **Low**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.
  - **High**: **Buffered exposure:** Between current levels and the protection strike (92.00), you still participate in moves, with downside protection further below.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $108.00
  Body: Below $108.00, the put establishes the floor for the full position (100 of 100 shares). At expiry below $108.00, the put settles at intrinsic value and downside is protected on the protected shares. Maximum combined loss (at expiry): $380.00.
  overlay_pnl=-380.0, stock_only_pnl=800.0, delta_vs_stock=-1180.0
  Anchors: Lower Strike@92.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $100.00 and $108.00
  Body: Between $108.00 and $100.00, results follow the shares for the full position (100 of 100 shares). At expiry in this range, protection remains in place on the protected shares. Net option premium (total): $2,360.00 on 2 contracts paid.
  overlay_pnl=-380.0, stock_only_pnl=0.0, delta_vs_stock=-380.0
  Anchors: Current Market Price@100.0, Lower Strike@92.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, upside participation continues for the full position (100 of 100 shares). At expiry above $100.00, the put expires worthless and gains follow the shares on the protected shares. At $108.00, combined P&L would be -$380.00 (options contribute -$1,180.00; the shares contribute +$800.00).
  overlay_pnl=-380.0, stock_only_pnl=800.0, delta_vs_stock=-1180.0
  Anchors: Upside Target (15%)@114.99999999999999, Stock to Infinity@None

---

## Strategy: S. Call Syn. Strangle (ID=59, Group=Synthetics, Subgroup=Short Vol, Kind=MIXED)

### Options Only

**Rule matched**: covered_call_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Income zone:** If the stock stays below your call strike (108.00), premium income can help support returns.
  - **Strikes**: **Income zone:** If the stock stays below your call strike (108.00), premium income can help support returns. **Income zone:** If the stock stays below your call strike (108.00), premium income can help support returns.
  - **Breakevens**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position. **Income zone:** If the stock stays below your call strike (108.00), premium income can help support returns.
  - **Low**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position.
  - **High**: **Income zone:** If the stock stays below your call strike (108.00), premium income can help support returns.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $92.00, downside follows the shares for the full position (100 of 100 shares). At expiry below $92.00, the call expires worthless on the covered shares. Net option premium (total): $2,360.00 on 2 contracts received.
  overlay_pnl=380.0, stock_only_pnl=-800.0, delta_vs_stock=1180.0
  Anchors: Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $100.00
  Body: Between $100.00 and $92.00, gains follow the shares for the full position (100 of 100 shares). At expiry in this range, the call expires worthless on the covered shares. Net option premium (total): $2,360.00 on 2 contracts received.
  overlay_pnl=380.0, stock_only_pnl=0.0, delta_vs_stock=380.0
  Anchors: Current Market Price@100.0, Lower Strike@92.0

  **Bullish Case**
  Condition: If stock rises above $92.00
  Body: Above $92.00, upside is limited by the call strike for the full position (100 of 100 shares). At expiry above $92.00, shares may be called away at the strike and upside is capped on the covered shares. Maximum combined profit (at expiry): $380.00.
  overlay_pnl=380.0, stock_only_pnl=-800.0, delta_vs_stock=1180.0
  Anchors: Lower Strike@92.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

### With Underlying Position

**Rule matched**: covered_call_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Income zone:** If the stock stays below your call strike (108.00), premium income can help support returns.
  - **Strikes**: **Income zone:** If the stock stays below your call strike (108.00), premium income can help support returns. **Income zone:** If the stock stays below your call strike (108.00), premium income can help support returns.
  - **Breakevens**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position. **Income zone:** If the stock stays below your call strike (108.00), premium income can help support returns.
  - **Low**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position.
  - **High**: **Income zone:** If the stock stays below your call strike (108.00), premium income can help support returns.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $92.00, downside follows the shares for the full position (100 of 100 shares). At expiry below $92.00, the call expires worthless on the covered shares. Net option premium (total): $2,360.00 on 2 contracts received.
  overlay_pnl=380.0, stock_only_pnl=-800.0, delta_vs_stock=1180.0
  Anchors: Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $100.00
  Body: Between $100.00 and $92.00, gains follow the shares for the full position (100 of 100 shares). At expiry in this range, the call expires worthless on the covered shares. Net option premium (total): $2,360.00 on 2 contracts received.
  overlay_pnl=380.0, stock_only_pnl=0.0, delta_vs_stock=380.0
  Anchors: Current Market Price@100.0, Lower Strike@92.0

  **Bullish Case**
  Condition: If stock rises above $92.00
  Body: Above $92.00, upside is limited by the call strike for the full position (100 of 100 shares). At expiry above $92.00, shares may be called away at the strike and upside is capped on the covered shares. Maximum combined profit (at expiry): $380.00.
  overlay_pnl=380.0, stock_only_pnl=-800.0, delta_vs_stock=1180.0
  Anchors: Lower Strike@92.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

---

## Strategy: S. Put Syn. Strangle (ID=60, Group=Synthetics, Subgroup=Short Vol, Kind=MIXED)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Lower-price scenario:** Downside payoff mechanics dominate here. **High‑risk zone:** Losses may continue to grow if the move extends.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **High‑risk zone:** Losses may continue to grow if the move extends.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,180.00 on 1 contracts received.
  overlay_pnl=380.0, stock_only_pnl=800.0, delta_vs_stock=-420.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,180.00 on 1 contracts received.
  overlay_pnl=380.0, stock_only_pnl=0.0, delta_vs_stock=380.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,180.00 on 1 contracts received.
  overlay_pnl=380.0, stock_only_pnl=-800.0, delta_vs_stock=1180.0
  Anchors: Upper Strike@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Scenario overview:** Review P&L sensitivity around this level.
  - **Strikes**: **Scenario overview:** Review P&L sensitivity around this level. **Scenario overview:** Review P&L sensitivity around this level.
  - **Breakevens**: **Lower-price scenario:** Downside payoff mechanics dominate here. **High‑risk zone:** Losses may continue to grow if the move extends.
  - **Low**: **Lower-price scenario:** Downside payoff mechanics dominate here.
  - **High**: **High‑risk zone:** Losses may continue to grow if the move extends.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,180.00 on 1 contracts received.
  overlay_pnl=380.0, stock_only_pnl=800.0, delta_vs_stock=-420.0
  Anchors: Lower Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $108.00
  Body: Between $92.00 and $108.00, results follow the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,180.00 on 1 contracts received.
  overlay_pnl=380.0, stock_only_pnl=0.0, delta_vs_stock=380.0
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares. At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $1,180.00 on 1 contracts received.
  overlay_pnl=380.0, stock_only_pnl=-800.0, delta_vs_stock=1180.0
  Anchors: Upper Strike@108.0

---

## Strategy: Syn. Covered Call (ID=61, Group=Synthetics, Subgroup=Bullish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Assignment zone:** Below the put strike (108.00), the position behaves more like buying shares at that strike (downside continues below it).
  - **Strikes**: **Watch zone:** Near your put strike (108.00), you are closer to being obligated to buy shares at that level.
  - **Breakevens**: **Assignment zone:** Below the put strike (108.00), the position behaves more like buying shares at that strike (downside continues below it).
  - **Low**: **Assignment zone:** Below the put strike (108.00), the position behaves more like buying shares at that strike (downside continues below it).
  - **High**: **Income zone:** Above your put strike (108.00), the put is more likely to expire with limited value.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $108.00
  Body: Below $108.00, losses can increase. At expiry below the lower strike, losses increase toward the hedge strike. Maximum loss is $9,810.00.
  overlay_pnl=990.0, stock_only_pnl=0.0, delta_vs_stock=990.0
  Anchors: Strike@108.0

  **Stagnant Case**
  Condition: If stock stays between $108.00 and $108.00
  Body: Between $108.00 and $108.00, outcomes depend on where the stock settles. At expiry between the strikes, the strategy seeks to retain the net credit. Net option premium (total): $99,000.00 on 1 contracts received Breakeven is around $98.10.
  overlay_pnl=190.00000000000003, stock_only_pnl=0.0, delta_vs_stock=190.00000000000003
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, losses can increase. At expiry above the upper strike, losses increase toward the hedge strike. Maximum loss is $9,810.00.
  overlay_pnl=990.0, stock_only_pnl=0.0, delta_vs_stock=990.0
  Anchors: Strike@108.0

### With Underlying Position

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **Assignment zone:** Below the put strike (108.00), the position behaves more like buying shares at that strike (downside continues below it).
  - **Strikes**: **Watch zone:** Near your put strike (108.00), you are closer to being obligated to buy shares at that level.
  - **Breakevens**: **Assignment zone:** Below the put strike (108.00), the position behaves more like buying shares at that strike (downside continues below it).
  - **Low**: **Assignment zone:** Below the put strike (108.00), the position behaves more like buying shares at that strike (downside continues below it).
  - **High**: **Watch zone:** Near your put strike (108.00), you are closer to being obligated to buy shares at that level.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $108.00
  Body: Below $108.00, losses track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $990.00 on 1 contracts received.
  overlay_pnl=1790.0, stock_only_pnl=800.0, delta_vs_stock=990.0
  Anchors: Strike@108.0

  **Stagnant Case**
  Condition: If stock stays between $108.00 and $108.00
  Body: Between $108.00 and $108.00, results follow the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $990.00 on 1 contracts received.
  overlay_pnl=190.00000000000003, stock_only_pnl=0.0, delta_vs_stock=190.00000000000003
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $108.00
  Body: Above $108.00, gains track the shares for the position (100 shares). At expiry, option payoffs settle to intrinsic value and are applied to the shares. Net option premium (total): $990.00 on 1 contracts received.
  overlay_pnl=1790.0, stock_only_pnl=800.0, delta_vs_stock=990.0
  Anchors: Strike@108.0

---

## Strategy: Syn. Covered Put (ID=62, Group=Synthetics, Subgroup=Bearish, Kind=OPTIONS)

### Options Only

**Rule matched**: fallback_generic (vfallback_v2)

**Commentary Blocks:**
  - **Spot**: **High‑risk zone:** Above the call strike (92.00), losses can continue to grow if the stock keeps rising.
  - **Strikes**: **Watch zone:** Near/above your call strike (92.00), upside gains can be partially offset and risk increases.
  - **Breakevens**: **High‑risk zone:** Above the call strike (92.00), losses can continue to grow if the stock keeps rising.
  - **Low**: **Income zone:** Below your call strike (92.00), the call is more likely to expire with limited value.
  - **High**: **High‑risk zone:** Above the call strike (92.00), losses can continue to grow if the stock keeps rising.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $92.00
  Body: Below $92.00, losses can increase. At expiry below the lower strike, losses increase toward the hedge strike. ROI at $92.00 is 33.1%.
  overlay_pnl=990.0, stock_only_pnl=0.0, delta_vs_stock=990.0
  Anchors: Strike@92.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $92.00
  Body: Between $92.00 and $92.00, outcomes depend on where the stock settles. At expiry between the strikes, the strategy seeks to retain the net credit. Net option premium (total): $99,000.00 on 1 contracts received Breakeven is around $101.90.
  overlay_pnl=190.00000000000003, stock_only_pnl=0.0, delta_vs_stock=190.00000000000003
  Anchors: Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $92.00
  Body: Above $92.00, losses can increase. At expiry above the upper strike, losses increase toward the hedge strike. ROI at $92.00 is 33.1%.
  overlay_pnl=990.0, stock_only_pnl=0.0, delta_vs_stock=990.0
  Anchors: Strike@92.0

### With Underlying Position

**Rule matched**: covered_call_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Upside limited:** Above your call strike (92.00), further upside is typically capped because shares may be called away.
  - **Strikes**: **Income zone:** If the stock stays below your call strike (92.00), premium income can help support returns.
  - **Breakevens**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position.
  - **Low**: **Down move:** The option premium can soften losses, but a large sell‑off still reduces the value of the position.
  - **High**: **Upside limited:** Above your call strike (92.00), further upside is typically capped because shares may be called away.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $92.00, downside follows the shares for the full position (100 of 100 shares). At expiry below $92.00, the call expires worthless on the covered shares. Net option premium (total): $990.00 on 1 contracts received.
  overlay_pnl=190.0, stock_only_pnl=-800.0, delta_vs_stock=990.0
  Anchors: Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $92.00 and $100.00
  Body: Between $100.00 and $92.00, gains follow the shares for the full position (100 of 100 shares). At expiry in this range, the call expires worthless on the covered shares. Net option premium (total): $990.00 on 1 contracts received.
  overlay_pnl=190.00000000000003, stock_only_pnl=0.0, delta_vs_stock=190.00000000000003
  Anchors: Current Market Price@100.0, Strike@92.0

  **Bullish Case**
  Condition: If stock rises above $92.00
  Body: Above $92.00, upside is limited by the call strike for the full position (100 of 100 shares). At expiry above $92.00, shares may be called away at the strike and upside is capped on the covered shares. Maximum combined profit (at expiry): $190.00.
  overlay_pnl=190.0, stock_only_pnl=-800.0, delta_vs_stock=990.0
  Anchors: Strike@92.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

---

## Strategy: Conversion (ID=63, Group=Arbitrage, Subgroup=Neutral, Kind=MIXED)

### Options Only

**Rule matched**: collar_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Stability zone:** Between the protection level (100.00) and the call strike (100.00), the goal is steadier outcomes versus holding stock alone.
  - **Strikes**: **Stability zone:** Between the protection level (100.00) and the call strike (100.00), the goal is steadier outcomes versus holding stock alone.
  - **Breakevens**: **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Stability zone:** Between the protection level (100.00) and the call strike (100.00), the goal is steadier outcomes versus holding stock alone. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away.
  - **Low**: **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside.
  - **High**: **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, the put sets the floor for the full position (100 of 100 shares). At expiry below $100.00, downside is protected on the collared shares. Maximum combined loss (at expiry): $0.00.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $100.00 and $100.00
  Body: Between $100.00 and $100.00, P&L is primarily driven by the shares for the full position (100 of 100 shares). At expiry in this range, the collar legs expire worthless on the collared shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0, Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, upside is limited by the call strike for the full position (100 of 100 shares). At expiry above $100.00, shares may be called away at the strike and upside is capped on the collared shares. Maximum combined profit (at expiry): $0.00.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

### With Underlying Position

**Rule matched**: collar_v3 (v3.0)

**Commentary Blocks:**
  - **Spot**: **Stability zone:** Between the protection level (100.00) and the call strike (100.00), the goal is steadier outcomes versus holding stock alone.
  - **Strikes**: **Stability zone:** Between the protection level (100.00) and the call strike (100.00), the goal is steadier outcomes versus holding stock alone.
  - **Breakevens**: **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside. **Stability zone:** Between the protection level (100.00) and the call strike (100.00), the goal is steadier outcomes versus holding stock alone. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away. **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away.
  - **Low**: **Protection working:** Below the put strike (100.00), the hedge is designed to limit further downside.
  - **High**: **Upside limited:** Above your call strike (100.00), further upside is typically capped because shares may be called away.

**Narrative Scenarios:**

  **Bearish Case**
  Condition: If stock falls below $100.00
  Body: Below $100.00, the put sets the floor for the full position (100 of 100 shares). At expiry below $100.00, downside is protected on the collared shares. Maximum combined loss (at expiry): $0.00.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0, Downside Target (15%)@85.0, Stock to Zero@0.0

  **Stagnant Case**
  Condition: If stock stays between $100.00 and $100.00
  Body: Between $100.00 and $100.00, P&L is primarily driven by the shares for the full position (100 of 100 shares). At expiry in this range, the collar legs expire worthless on the collared shares. At $100.00, combined P&L would be +$0.00 (options contribute +$0.00; the shares contribute +$0.00).
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0, Current Market Price@100.0

  **Bullish Case**
  Condition: If stock rises above $100.00
  Body: Above $100.00, upside is limited by the call strike for the full position (100 of 100 shares). At expiry above $100.00, shares may be called away at the strike and upside is capped on the collared shares. Maximum combined profit (at expiry): $0.00.
  overlay_pnl=0.0, stock_only_pnl=0.0, delta_vs_stock=0.0
  Anchors: Current Market Price@100.0, Upside Target (15%)@114.99999999999999, Stock to Infinity@None

---

