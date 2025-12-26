METRICS = {
    "logins": 0,
    "failed_logins": 0,
    "anomalies": 0
}

def record(authenticated: bool, anomaly: bool):
    METRICS["logins"] += 1
    if not authenticated:
        METRICS["failed_logins"] += 1
    if anomaly:
        METRICS["anomalies"] += 1