from .models import AuditEvent


BLOCKED_ACTIONS = {"export_raw_pii", "disable_guardrails"}


def check_policy(event: AuditEvent) -> bool:
    return event.action not in BLOCKED_ACTIONS
