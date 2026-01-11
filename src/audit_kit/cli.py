from pathlib import Path

from .models import AuditEvent
from .policy import check_policy
from .reporter import write_report
from .risk import risk_score


def run(output: Path) -> None:
    event = AuditEvent("e-1", "admin-user", "export_summary", "2026-02-05T10:00:00Z")
    write_report([{"allowed": check_policy(event), "risk": risk_score(event)}], output)
