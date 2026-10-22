# Jurisdiction, Access, and Regulatory Report (Ethiopia - R9)

> [!WARNING]
> **Legal Notice**: This report provides technical and architectural regulatory risk analysis for software development purposes and does **not** constitute legal or financial advice.

---

## 1. Regulatory Landscape (National Bank of Ethiopia - NBE)

### Cryptocurrency & Virtual Assets [verified in current docs]
- **Prohibition on Crypto Trading & P2P**: The National Bank of Ethiopia (NBE) maintains a strict prohibition against cryptocurrency trading, payment settlement, and decentralized peer-to-peer (P2P) transfers involving the Ethiopian Birr (ETB).
- **Virtual Asset Services**: Commercial virtual asset service providers (VASPs) are not authorized for retail speculative trading.
- **Status for Live Trading**: **BLOCKED (FAIL-CLOSED)**. No real funds or live exchange accounts may be connected.

### Retail Foreign Exchange (Forex) [verified in current docs]
- **Foreign Exchange Directives (FXD/01/2024 & FXD/04/2026)**: While the NBE transitioned to a market-based foreign exchange rate system via commercial banks and authorized bureaus, strict capital controls govern outbound capital transfers.
- **Offshore Margin Funding**: Private individuals cannot remit foreign currency abroad to fund offshore speculative retail margin accounts without specific authorization.
- **Status for Live Trading**: **BLOCKED (FAIL-CLOSED)**.

---

## 2. Impact on TradingLab Architecture & Development

Per **Hard Rule 5** (*"Demo and sandbox only until a Phase 10 report and written approval"*) and **Hard Rule 12** (*"Run jurisdiction check before real accounts"*):

1. **Development & Backtesting Unrestricted**: Historical data analysis, indicator research, strategy backtesting, and paper trading are software research activities using historical or simulated data.
2. **Sandbox & Demo Execution 100% Free & Compliant**:
   - Demo trading uses virtual test currency ($10,000 simulated paper equity).
   - No deposits, no bank transfers, no currency conversions, and no capital outflow.
   - All external broker connections are permanently locked to `mode: paper` / `sandbox: true`.

---

## 3. Venues Supporting Demo / Sandbox Access for Development

The following platforms support free, unverified sandbox and demo access for algorithmic development:

| Venue / Tool | Asset Class | Testnet / Demo Environment | Access Mechanism | KYC / Funding Required? |
|---|---|---|---|---|
| **MetaTrader 5 (MetaQuotes Demo)** | Forex | `MetaQuotes-Demo` server | Native MT5 Python client | None (instant virtual account) |
| **Binance Testnet** | Crypto | `testnet.binance.vision` | CCXT (`sandbox: true`) | None (free testnet API keys) |
| **Bybit Testnet** | Crypto | `testnet.bybit.com` | CCXT (`sandbox: true`) | Free registration, testnet coins via faucet |
| **OKX Demo Trading** | Crypto | OKX Demo Mode | CCXT (`sandbox: true`) | Simulated portfolio API |

---

## 4. Tax Treatment & Record-Keeping Invariants
- Even in simulation and paper trading, TradingLab maintains full institutional-grade record keeping in `tradinglab.journal` and `logs/audit.log` (UTC timestamps, fill slippage, commission costs, and order identifiers).
- Should regulatory sandboxes or licensed avenues open in the future, the immutable audit trail guarantees full tax and transaction traceability.
