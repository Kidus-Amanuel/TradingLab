# ADR 0001: Core Architecture Framework Selection

## 5-Line Summary
- **Need**: Unified backtesting, research, and paper-execution architecture spanning Forex and Crypto under a mandatory fail-closed Risk Gate on Windows.
- **Options**: Option A (Freqtrade crypto + MT5 stack), Option B (NautilusTrader multi-asset framework), Option C (Modular library stack: CCXT + MT5 + lightweight backtest engine + custom safety glue).
- **Choice**: **Option C (Modular Library Stack)**.
- **Why**: 100% flawless Gate Test pass (zero third-party order bypass), native Windows support without Docker/Wine, zero dual-stack maintenance, and zero commercial or platform lock-in.
- **Exit Plan**: All external libraries (CCXT, MT5, backtesting engines) sit behind thin adapters in `tradinglab.adapters`; any engine can be swapped by replacing a single adapter file.

---

## Evaluation Matrix

| Criterion | Option A (Freqtrade + MT5 Forex) | Option B (NautilusTrader) | Option C (Modular Library Stack) |
|---|---|---|---|
| **Forex Coverage** | Poor (Freqtrade is crypto-only; requires 2nd stack) | Moderate (Interactive Brokers/OANDA; MT5 requires community bridge) | **Complete** (Official `MetaTrader5` package for Windows) |
| **Crypto Coverage** | Excellent (CCXT-based, spot + perps) | Excellent (Native Binance, Bybit, OKX adapters) | **Complete** (Direct CCXT integration) |
| **Gate Test Result** | **FAIL / RISKY**: Freqtrade internal loop controls order dispatch; difficult to guarantee Risk Gate interception on liquidations/stops. | **HIGH FRICTION**: Cython/Rust actor model complicates external audit fail-closed gate injection. | **100% PASS**: Zero external code can dispatch orders. Only `tradinglab.risk.RiskGate` issues authorized orders. |
| **Windows Support** | Friction: Freqtrade recommends Docker/WSL, but MT5 requires native Windows host. | Moderate: Pre-built Windows wheels limited to 64-bit precision; MSVC lacks `__int128`. | **100% Native Windows**: CCXT (pure Python/aiohttp) + MT5 (native Windows DLL). |
| **Lock-in Risk** | Moderate-High (tied to Freqtrade strategy syntax and FreqUI). | High (deeply coupled to Nautilus event-driven actor abstractions). | **Zero Lock-in**: Strategies depend only on pure domain models (`Signal`, `Bar`). |
| **UI & Observability** | FreqUI (crypto only) + external logs for Forex. | Jupyter / terminal only (no official web UI). | **Unified**: FastAPI REST API + Next.js dashboard + TradingView Lightweight Charts (Phase 8). |
| **Glue Code Volume** | High (must reconcile and bridge two disjoint trading engines). | Medium volume, but extreme complexity (Cython / FFI bindings). | **Targeted & Clean**: Safety layer only (Risk Gate, kill switch, audit trail, adapters). |

---

## Detailed Analysis

### Why Option C is Recommended
1. **Absolute Gate Test Compliance**: Hard Rule 2 dictates: *"The Risk Gate is mandatory. No order path skips it, including tests and experiments."* Monolithic frameworks like Freqtrade have their own internal order management lifecycle; preventing them from ever bypassing an external gate is brittle. With Option C, every order path is authored by us and physically cannot reach the network without passing the Risk Gate.
2. **Unified Developer Experience**: Under Option A, you would have to write crypto strategies in Freqtrade's dataframe format and Forex strategies in a completely different paradigm. Under Option C, a single unified strategy interface handles both Forex and Crypto.
3. **Environment Alignment**: Option C runs 100% natively on Windows with 16 GB RAM without Docker overhead or Linux VM bridging.

---

## Architectural Boundaries Enforced
- Strategies depend strictly on `tradinglab.domain` and `tradinglab.core`.
- Only `tradinglab.risk.RiskGate` can approve an `OrderIntent` into an authorized `Order`.
- Only `tradinglab.adapters.brokers` can transmit orders to MT5 or CCXT.
- The persistent Kill Switch is checked synchronously before every external call.
