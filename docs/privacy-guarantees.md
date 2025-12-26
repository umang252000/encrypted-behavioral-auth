# Privacy Guarantees

This system guarantees:

- Behavioral patterns cannot be reconstructed
- Embeddings cannot be inverted
- Server operators cannot access biometric data
- Database breaches reveal nothing usable
- Only accept/reject is exposed

This enables compliance with:
- GDPR
- HIPAA-style biometric protections
- Enterprise privacy policies

## Encryption-in-Use

Behavioral embeddings are encrypted immediately after creation.
No plaintext embeddings are stored, transmitted, or logged.

Similarity search operates on encrypted vectors only.

## Analytics Without Surveillance

The system tracks only aggregate counts
(logins, failures, anomalies).

No user behavior, embeddings, or scores
are logged or exposed.