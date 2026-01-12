from audit_kit.models import AuditEvent
from audit_kit.trail import format_trail


def test_trail_format_contains_actor_and_action() -> None:
    event = AuditEvent("1", "ops", "approve", "2026-02-01")
    out = format_trail(event)
    assert "actor=ops" in out and "action=approve" in out
