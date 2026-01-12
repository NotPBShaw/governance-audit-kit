from audit_kit.models import AuditEvent
from audit_kit.policy import check_policy


def test_blocked_action_denied() -> None:
    event = AuditEvent("1", "analyst", "disable_guardrails", "t")
    assert not check_policy(event)
