#!/usr/bin/env bash
set -euo pipefail
python - <<'PY'
from pathlib import Path
from audit_kit import run
run(Path("reports/sample.json"))
print("wrote reports/sample.json")
PY
