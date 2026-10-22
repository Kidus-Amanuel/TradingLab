# TradingLab

A research and paper-trading system for Forex and Crypto assembled using proven open-source tools with custom fail-closed safety and risk gates.

## Architecture & Layout

This repository is structured as a polyglot monorepo:
- **`pnpm`** coordinates TypeScript packages (`frontend` Next.js dashboard + `@tradinglab/contracts` schema bridge).
- **Python (>=3.11)** powers the quantitative research and execution safety engine (`backend/`).
- **`config/`** contains versioned, non-secret parameters (instruments, costs, risk policies, strategies, logging).
- **`docs/`** hosts Phase 0 decisions, ADRs, risk policies, claims ledgers, and experiment tracking.

```
TradingLab/
├── pnpm-workspace.yaml          # pnpm workspace definition (frontend + contracts)
├── package.json                 # Monorepo root scripts
├── .gitignore                   # Ignores dependencies, runtime data, and secrets
├── .editorconfig                # Format consistency (2 spaces JS/TS, 4 spaces Python)
├── .env.example                 # Environment template with safe defaults
├── config/                      # Non-secret YAML configs
│   ├── instruments.yaml
│   ├── costs.yaml
│   ├── risk.yaml
│   ├── strategies.yaml
│   └── logging.yaml
├── docs/                        # Architecture & decision trail
│   ├── decisions.md
│   ├── claims-ledger.md
│   ├── risk-policy.md
│   ├── experiment-log.md
│   ├── adr/
│   └── runbooks/
├── contracts/                   # TypeScript contract library (@tradinglab/contracts)
│   ├── package.json
│   ├── tsconfig.json
│   └── src/
├── frontend/                    # Next.js UI dashboard
│   ├── package.json
│   ├── tsconfig.json
│   └── src/
├── backend/                     # Python quant & risk engine
│   ├── pyproject.toml
│   ├── src/tradinglab/
│   │   ├── core/                # Clock, ids, context, config, errors
│   │   ├── domain/              # Pure domain entities (Order, Fill, Position, Signal)
│   │   ├── observability/       # structlog, redaction, audit trail
│   │   ├── risk/                # Gate, sizing, kill switch, limits
│   │   ├── adapters/            # CCXT, MT5, backtest wrappers
│   │   ├── journal/             # Cross-market journal & analytics
│   │   ├── reconciliation/      # Local vs broker state comparison
│   │   ├── api/                 # FastAPI server & schema export
│   │   ├── cli/                 # Typer command line interface
│   │   └── worker/              # Asynchronous tasks
│   └── tests/
│       ├── unit/
│       ├── integration/
│       ├── safety/              # Fail-closed, kill-switch, secret-redaction tests
│       └── golden/
├── scripts/                     # PowerShell automation scripts
├── data/                        # Market data cache (git-ignored)
├── runs/                        # Experiment runs & artifacts (git-ignored)
└── logs/                        # Operational and audit logs (git-ignored)
```
