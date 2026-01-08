from .models import AuditEvent


def risk_score(event: AuditEvent) -> int:
    score = 2
    if "admin" in event.actor:
        score += 3
    if "export" in event.action:
        score += 5
    return score
