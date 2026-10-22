# Claims Ledger

Track every quantitative or behavioral claim with real verified output.
Statuses: `unproven` | `proven` | `disproven`

| ID | Claim | Evidence Required | Real Output Ref | Status |
|---|---|---|---|---|
| CLM-001 | Risk Gate halts orders when Kill Switch is active | Automated safety test blocking order intent | Not run | unproven |
| CLM-002 | Audit trail failure fails closed | Automated test verifying order abortion on log error | Not run | unproven |
| CLM-003 | Sensitive credentials never leak into logs | Redaction safety test | Not run | unproven |
| CLM-004 | Baseline strategy survives transaction costs | Walk-forward holdout with 1.5x stressed costs | Not run | unproven |
