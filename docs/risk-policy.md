# Risk Policy (Reference R6)

This document formalizes non-negotiable rules enforced by the TradingLab Risk Gate.

## Invariant Rules
1. **Mandatory Gate Passage**: No order path may reach an execution adapter without passing the Risk Gate.
2. **Fail Closed**: In any uncertain state (clock drift, quote staleness > 10s, unknown account state, audit write failure, or active kill switch), all new risk is blocked. Risk reduction is always permitted.
3. **Position Sizing**: Sizing is dynamically computed from stop-loss distance and capital risk percentage (0.25% default).
4. **Mandatory Stops**: Every entry must carry an explicit, correct-side stop-loss at submission time.
5. **Forbidden Practices**:
   - Martingale / lot doubling on loss.
   - Averaging down losing trades without predefined risk allocation.
   - Removing or widening stop-loss orders after entry.
   - Unhedged exposure beyond correlated limit.
