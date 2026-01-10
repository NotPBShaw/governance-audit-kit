from .models import AuditEvent


def format_trail(event: AuditEvent) -> str:
    return f"{event.timestamp} actor={event.actor} action={event.action}"
