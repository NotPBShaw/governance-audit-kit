# Governance Audit Kit

Audit, policy, and risk scoring for AI governance workflows.

[![CI](https://github.com/NotPBShaw/governance-audit-kit/actions/workflows/ci.yml/badge.svg)](https://github.com/NotPBShaw/governance-audit-kit/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Score audit events against policy rules, compute risk, and export a structured report.

## Why this exists

Governance tooling often lives in proprietary dashboards. This kit provides composable primitives — policy checks, risk scoring, and report generation — that integrate into CI pipelines or agent runtimes.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -c "from audit_kit.cli import run; from pathlib import Path; run(Path('report.json'))"
cat report.json
```

## Usage

Load events from `examples/events.json` and evaluate policy + risk:

```python
from audit_kit.models import AuditEvent
from audit_kit.policy import check_policy
from audit_kit.risk import risk_score

event = AuditEvent("e-1", "admin-user", "export_summary", "2026-02-05T10:00:00Z")
print(check_policy(event), risk_score(event))
```

## Architecture

- `policy.py` — allow/deny decisions on audit events
- `risk.py` — numeric risk scoring for flagged actions
- `reporter.py` — JSON report output
- `trail.py` — event trail formatting helpers

## Development

```bash
make check
pytest -q
```

## License

MIT — see [LICENSE](LICENSE).
