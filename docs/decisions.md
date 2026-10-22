# System Decisions (Phase 0)

This document records the baseline parameters, initial test instruments, and validation rules for TradingLab.

> [!NOTE]
> **Multi-Asset Architecture**: The system is fully multi-pair and multi-asset. Any Forex pair (`GBPUSD`, `USDJPY`, `AUDUSD`, etc.) or Crypto pair can be activated simply by adding an entry to `config/instruments.yaml`. `EURUSD` and `BTC/USDT` are selected as the **initial development fixtures** for building and testing data pipelines.

---

## 1. Initial Development Instruments (Test Fixtures)

| Parameter | Initial Development Value | Production Capability | Rationale |
|---|---|---|---|
| **Primary Forex Pair** | `EURUSD` | Any major/minor Forex pair | Highest global liquidity, tightest spreads, universal tick data benchmark. |
| **Primary Crypto Pair** | `BTC/USDT` | Any spot/perpetual crypto pair | Deepest book, 24/7 liquidity, standard CCXT test fixture. |
| **Main Timeframe** | `1h` (1 Hour) | Configurable (`1m`, `5m`, `15m`, `1h`, `1d`) | Balances signal frequency against spread/commission drag. |

---

## 2. Risk Gate Baselines (Why Define Before Code?)

In quant trading, defining risk rules *before* running backtests prevents **p-hacking** (tweaking stops or leverage after seeing losses to falsely curve-fit historical data).

| Parameter | Baseline Value | Configuration Location | Purpose |
|---|---|---|---|
| **Account Currency** | `USD` | `config/risk.yaml` | Base currency for equity and risk calculation. |
| **Starting Paper Equity** | `$10,000.00` | `config/risk.yaml` | Standard test balance for realistic lot sizing. |
| **Risk per Trade** | `0.25%` ($25.00) | `config/risk.yaml` | Position size derived from stop distance: `Size = Risk $ / Stop Distance`. |
| **Max Daily Loss Limit** | `2.0%` ($200.00) | `config/risk.yaml` | Circuit breaker: halts new entries if a day goes poorly. |
| **Max Portfolio Drawdown** | `10.0%` ($1,000.00) | `config/risk.yaml` | Emergency threshold: trips kill switch for human review. |
| **Max Open Positions** | `3` | `config/risk.yaml` | Prevents over-leveraging across correlated pairs. |
| **Mandatory Stop-Loss** | Required on every order | Risk Gate code | Core invariant: orders without stops are rejected immediately. |

---

## 3. Validation Rigor & Scientific Guardrails (Reference R7)

| Guideline | Baseline | Purpose |
|---|---|---|
| **Forex History Length** | 5 Years | Ensures testing across diverse market regimes (trending, ranging, crises). |
| **Crypto History Length** | 3 Years | Covers post-2020 liquidity regimes. |
| **Cost Stress Multipliers**| `1.0x`, `1.5x`, `2.0x` | Rejects strategies that only appear profitable under zero-fee fantasy conditions. |
| **Multiple Testing Deflation**| Mandatory | Haircuts performance metrics based on how many trials were attempted. |
| **Hypothesis Budget** | 5 strategy families | Prevents endless random parameter mining. If 5 families fail, rethink edge. |
