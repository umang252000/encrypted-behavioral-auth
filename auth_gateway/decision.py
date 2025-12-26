SIMILARITY_THRESHOLD = 0.85

def decide(similarity_results: list) -> bool:
    """
    Returns True if authentication is accepted.
    """
    if not similarity_results:
        return False

    top_match = max(similarity_results, key=lambda x: x["score"])
    return top_match["score"] >= SIMILARITY_THRESHOLD