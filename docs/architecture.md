# System Architecture

This system implements encrypted behavioral biometric authentication.

## Design Principles
- No plaintext behavioral data at rest
- No plaintext embeddings at rest
- Encrypted similarity search only
- Accept / Reject output only

## Flow
1. Behavioral signals captured in browser
2. Signals transformed into numeric features
3. Features encoded into embedding
4. Embedding encrypted client-side
5. Encrypted vector stored/searched in CyborgDB
6. Authentication decision returned

## Trust Boundaries
- Browser: trusted for capture + encryption
- Server: untrusted
- Database: untrusted

## Behavioral Encoder

A deterministic embedding encoder converts statistical
behavioral features into a normalized fixed-length vector.

This embedding is:
- Non-invertible
- Stable across sessions
- Suitable for encrypted similarity search

## Encrypted Similarity Search

All authentication comparisons are performed using
encrypted similarity search in CyborgDB.

The server never accesses plaintext vectors or distances.

## Enterprise Controls

- JWT-based authentication
- Role-based access control (RBAC)
- Multi-tenant isolation
- Privacy-safe audit logging

## Advanced Security Features

- Behavioral anomaly detection
- Bot and session hijacking detection
- Privacy-safe authentication analytics