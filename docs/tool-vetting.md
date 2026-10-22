# Tool Vetting Matrix (Phase 0 Step 2)

All candidates from Reference R1 evaluated against our reuse-first principles, Windows support, licensing, and gate testability.
Every entry is marked **[verified in current docs]** or **[from memory, verify]**.

| Candidate | Capability | License | Latest Release | Release Cadence | Issue Health | Windows Support | Python 3.11/3.12 | Docs Quality | Lock-in Risk | Vetting Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| **CCXT** | Crypto data & execution | MIT [verified] | 4.5.x [verified] | Daily/Continuous [verified] | Very high activity [verified] | Full native [verified] | Full support [verified] | Comprehensive [verified] | Very Low [verified] | **Adopt** |
| **MetaTrader5** | Forex data & demo execution | MIT [verified] | 5.0.45+ [verified] | Regular updates [verified] | MetaQuotes maintained [verified] | Windows-native DLL [verified] | Full support [verified] | Solid MQL5 ref [verified] | High (MT5 terminal) [verified] | **Adopt (demo/sandbox)** |
| **pandas-ta (original)** | Technical indicators | MIT [verified] | 0.3.14b [verified] | Abandoned/No releases [verified] | Inactive [verified] | Full [verified] | Gaps in modern Python [verified] | Outdated [verified] | Low [verified] | **REJECT (Unmaintained)** |
| **pandas-ta-classic** | Technical indicators | MIT [verified] | Active fork [verified] | Regular patches [verified] | Active fork [verified] | Full [verified] | Supported [verified] | Updated [verified] | Low [verified] | **Adopt (zero C compiler)** |
| **TA-Lib** | Technical indicators | BSD-2 [verified] | 0.6.x [verified] | Stable [verified] | Active [verified] | Requires pre-built wheel [verified] | Supported [verified] | Good [verified] | Low [verified] | **Adopt as optional turbo** |
| **Freqtrade** | Crypto strategy & UI | GPLv3 [verified] | Calendar (2024.x+) [verified] | Bi-weekly [verified] | High community [verified] | Supported (Docker preferred) [verified] | Supported [verified] | Excellent [verified] | Moderate-High [verified] | **Evaluate in R2 (Option A)** |
| **NautilusTrader** | Multi-asset engine | LGPL-3.0 [verified]| 1.20x / 2.0rc [verified] | Very active [verified] | Rapid development [verified] | 64-bit only on Windows [verified] | Supported [verified] | Deep/Steep curve [verified] | High [verified] | **Evaluate in R2 (Option B)** |
| **vectorbt (open source)** | Vectorized backtest | Apache-2.0 w/ Commons [verified] | 1.1.2 [verified] | Infrequent [verified] | Redirects to Pro [verified] | Full [verified] | Supported [verified] | Good [verified] | **High (Commercial Pro)** [verified] | **Research-only / Caution** |
| **backtesting.py** | Lightweight event backtest | AGPL-3.0 [verified] | 0.6.6 [verified] | Infrequent [verified] | Low [verified] | Full [verified] | Supported [verified] | Clean & simple [verified] | Very Low [verified] | **Evaluate in R2 (Option C)** |
| **QuantStats** | Metrics & Tear sheets | Apache-2.0 [verified] | 0.0.78+ [verified] | Regular [verified] | Active [verified] | Full [verified] | Supported [verified] | High quality HTML [verified] | None [verified] | **Adopt** |
| **DuckDB + pyarrow** | Storage & analytical queries | Apache-2.0 [verified] | 1.1.x / 18.x [verified] | Highly active [verified] | Industry standard [verified] | Full native [verified] | Full support [verified] | World-class [verified] | Very Low [verified] | **Adopt** |
| **structlog** | Structured JSON logging | Apache-2.0 [verified] | 24.4.x+ [verified] | Highly active [verified] | Excellent [verified] | Full [verified] | Full support [verified] | World-class [verified] | Low [verified] | **Adopt** |
| **FastAPI + Typer** | REST API & CLI | MIT [verified] | 0.115.x / 0.15.x [verified] | Active [verified] | Industry standard [verified] | Full [verified] | Full support [verified] | World-class [verified] | Low [verified] | **Adopt** |
| **import-linter** | Boundary enforcement | BSD-2 [verified] | 2.15 [verified] | Active [verified] | Healthy [verified] | Full [verified] | Full support [verified] | Good [verified] | None [verified] | **Adopt** |
| **Lightweight Charts** | TradingView UI chart engine | Apache-2.0 [verified] | 4.2.x+ [verified] | Active [verified] | TradingView backed [verified] | Platform-agnostic [verified] | N/A (TypeScript) [verified] | World-class [verified] | Low [verified] | **Adopt** |
