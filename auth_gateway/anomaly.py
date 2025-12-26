def anomaly_score(results) -> float:
    """
    Compute anomaly score from encrypted similarity search results.

    Uses only distance values returned by CyborgDB.
    No plaintext embeddings are ever accessed.
    """

    if not results:
        # No prior behavioral reference = highly anomalous
        return 1.0

    distances = [r["distance"] for r in results]

    # Smaller distance = more similar behavior
    min_distance = min(distances)

    return float(min_distance)


def is_anomalous(anomaly_score: float, threshold: float = 0.3) -> bool:
    """
    Flag anomalous authentication attempts.
    """
    return anomaly_score > threshold