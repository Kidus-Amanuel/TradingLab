# Frontend Dashboard (`frontend`)

Next.js web UI for TradingLab (Phase 8), integrating:
- TradingView Lightweight Charts for multi-asset candlestick / indicator display
- Real-time Kill Switch toggle and status indicator
- Live risk exposure gauges and reconciliation diff tables
- Audit trail event streaming

Boundary rule: The frontend communicates strictly with the FastAPI backend endpoints and never has direct broker or database access.
