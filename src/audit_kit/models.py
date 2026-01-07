from dataclasses import dataclass


@dataclass
class AuditEvent:
    event_id: str
    actor: str
    action: str
    timestamp: str
