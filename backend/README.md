# TradingLab Backend (`backend`)

The Python safety-and-glue engine for TradingLab.

## Architectural Boundaries (Strict)
1. **Core (`tradinglab.core`)**: UTC clock, UUIDv7 / ULID generators, typed configuration loader, error taxonomy.
2. **Domain (`tradinglab.domain`)**: Pure immutable domain models (`Instrument`, `Signal`, `OrderIntent`, `Order`, `Fill`, `Position`, `RiskDecision`).
3. **Risk (`tradinglab.risk`)**: The mandatory Risk Gate, position sizing calculator, persistent kill switch, and exposure rules.
4. **Observability (`tradinglab.observability`)**: Structured JSON logging (`structlog`), automatic secret redaction, audit trail persistence, decision logs.
5. **Adapters (`tradinglab.adapters`)**: Thin translation wrappers around adopted third-party libraries (CCXT, MetaTrader5, etc.).
6. **Reconciliation (`tradinglab.reconciliation`)**: Compares internal state against actual broker/exchange records.
7. **Journal (`tradinglab.journal`)**: Cross-market trade records and unified analytics views.
8. **Interfaces (`api/`, `cli/`, `worker/`)**: FastAPI REST endpoints, Typer CLI commands, and asynchronous workers.
