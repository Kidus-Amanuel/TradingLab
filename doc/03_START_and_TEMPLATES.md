# START HERE, THEN REUSE THE TEMPLATES

Paste the Core first (with the MODE line set), attach the Reference, then paste the Phase 0 prompt below.

---

## PHASE 0 PROMPT: Decisions, tool vetting, jurisdiction (no production code)

Begin Phase 0. Work in these steps and stop after each one for my reply.

**Step 1: Decisions (max 3 questions at a time, each with a default I can accept with "ok").** Proposed defaults, which I may change:
- Forex pair: EURUSD. Crypto pair: BTC/USDT. Main timeframe: 1h.
- Account currency: USD. Paper equity: 10,000.
- Risk per trade: 0.25%. Max daily loss: 2%. Max drawdown: 10%. Max open positions: 3.
- History length: 5 years Forex, 3 years crypto.
- Go/no-go numbers (R7), maximum hypotheses (default 5 strategy families) and time budget (default 12 weeks to a Phase 4 verdict).
Save answers to `docs/decisions.md`.

**Step 2: Tool vetting.** Search current docs and release pages. Produce a table for every candidate in R1: license, latest release, cadence, issue health, Windows, Python 3.11/3.12, docs, lock-in. Mark each fact [verified] or [verify]. Flag anything unmaintained.

**Step 3: Framework decision.** Run R2, rank options A, B and C, include the gate-test result for each, recommend one. Write `docs/adr/0001-framework.md`. Wait for my approval.

**Step 4: Jurisdiction and access check (R9).** Report findings and open questions. Do not recommend specific brokers or exchanges for live use. List which ones support demo or sandbox from my country for development.

**Step 5: Smoke tests, one per chosen tool, minimal code.** Examples: fetch a few days of the crypto pair through the data library, read a few Forex bars from an MT5 demo (if available), compute one indicator, run one trivial backtest in the chosen engine. Give commands and expected output. Wait for my results.

---

## PHASE 1 PROMPT: Foundation (only after Phase 0 is approved)

Goal: a clean skeleton that wraps the chosen tools, with logging and safety from day one. No trading logic.

**Step 0:** give me these commands, then wait for the output.
```powershell
py --version
py -0p
git --version
```
Tell me which Python version to use and why.

**Step 1:** briefly explain (thin monorepo, adapters, environment config, virtual environments) and show the Phase 1 file tree from R3.

**Step 2:** deliver in groups, confirming after each:
1. Skeleton with importable packages
2. `.gitignore`, `.env.example`, `.editorconfig`, pre-commit with secret scanning
3. Pinned `requirements.txt` and `requirements-dev.txt` (versions verified, R8 followed)
4. Typed config loader. Safe defaults: paper mode, live disabled, risk 0.25%
5. Logging foundation: structlog, redaction, context IDs, audit table, event catalogue
6. Kill switch (persistent flag) and a stub Risk Gate that rejects everything by default
7. FastAPI `/health` (status, version, mode, kill-switch state, audit-log state)
8. Safety tests: kill switch blocks orders, secrets never logged, audit failure fails closed
9. `README.md` with exact Windows setup, `git init`, first commit message

**Step 3:** verification commands and expected output. **Step 4:** concept note (fail-closed design) and one check question.

Do not start Phase 2. Wait for my results.

---

## TEMPLATE: PHASE PROMPT (Phase 2 onward)
```text
Phase N: <name>
Current state: <what works, last test output, open issues>
Goal: <one sentence>
Out of scope: <what we are NOT doing now>
Time box: <max days>
Inputs from me: <files, errors, decisions>

Please follow the standard response shape. State what we ADOPT and what we BUILD
(ADR if new). Include acceptance criteria. Stop and wait.
Gate: no Phase N+1 until criteria are met and I confirm.
```

## TEMPLATE: BUILD-VS-BUY CHECK (use when the assistant starts writing something generic)
```text
Stop. Before writing this, search for an existing maintained library or framework.
Report candidates, license, latest release, Windows and Python support, fit, and
whether it can sit behind our Risk Gate. Build only if none fits, and write the
exception as an ADR.
```

## TEMPLATE: CLAIM CHECK (use whenever a result looks good)
```text
Treat this result as suspicious. List: how many trials led to it, which costs and
fills were assumed, whether the holdout was touched before, what the result is
after the multiple-testing adjustment, which regime or trades carry the profit,
and the cheapest test that could disprove it.
```

## TEMPLATE: RED-TEAM REVIEW (end of every phase)
```text
Act as a skeptical reviewer and try to break this phase:
1. Where could look-ahead or leakage hide, including inside adopted tools?
2. Which adopted tool's default assumption (fills, fees, rounding) would hurt most if wrong?
3. Which path could reach an order without the Risk Gate or kill switch?
4. What input crashes it or silently produces wrong numbers?
5. Which claim in the ledger is weakest?
Give a ranked top 5, each with a test I can write.
```

## TEMPLATE: HANDOFF BLOCK (top of a new chat)
```text
MODE:
CURRENT STATE
Phase and step:
Chosen tools and ADRs:
Last passing test run:
Open bugs:
Key decisions (docs/decisions.md):
Claims ledger (proven / unproven / disproven):
Experiments so far (count, best result, data version):
Files changed since last handoff:
```

## SESSION HYGIENE
- Paste real error output, never a paraphrase. Commit after every working increment.
- New chat when answers degrade or get inconsistent; use the handoff block.
- Do not change parameters after seeing holdout results.
