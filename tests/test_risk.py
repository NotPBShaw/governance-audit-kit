from audit_kit.models import AuditEvent
from audit_kit.risk import risk_score


def test_admin_export_is_high_risk() -> None:
    event = AuditEvent("1", "admin-user", "export_summary", "t")
    assert risk_score(event) >= 7
