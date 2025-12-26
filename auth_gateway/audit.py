from datetime import datetime

AUDIT_LOG = []

def log_event(event: str, tenant: str, success: bool):
    AUDIT_LOG.append({
        "event": event,
        "tenant": tenant,
        "success": success,
        "timestamp": datetime.utcnow().isoformat()
    })