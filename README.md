# CyborgDB-Powered Encrypted Behavioral Authenticator
Modern authentication increasingly relies on behavioral biometrics such as typing rhythm and mouse movement to prevent account takeover. However, storing behavioral embeddings in plaintext creates severe privacy and security risks, as these embeddings are invertible and can be reconstructed if breached.

This project introduces a privacy-preserving behavioral authentication system that performs login verification entirely on encrypted behavioral embeddings using CyborgDB.
The system releases only a single-bit decision (accept/reject) while ensuring behavioral patterns, identities, and embeddings are mathematically impossible to reconstruct — even by the system operator.

<img width="1536" height="1024" alt="ChatGPT Image Dec 25, 2025, 05_34_06 PM" src="https://github.com/user-attachments/assets/48e50531-ef8b-4124-adfa-f20631e8c3d2" />

## Problem Statement

Behavioral biometrics (keystroke dynamics, mouse movement, interaction rhythm) are increasingly used to strengthen authentication and detect account takeover.

However, almost all existing systems store behavioral embeddings in plaintext.

This is dangerous.

Behavioral embeddings are invertible — if a database is breached, attackers can reconstruct sensitive biometric patterns, impersonate users, or build spoofing attacks.
As a result, organizations face an impossible trade-off:

- Strong behavioral security or
- Biometric privacy and regulatory safety

Today, enterprises avoid behavioral biometrics not because they don’t work — but because they are too risky to store.

## Innovation

This project introduces a new authentication paradigm:

Behavioral biometrics that are usable, accurate, and mathematically private.

Instead of storing raw behavior or plaintext embeddings, the system:

- Converts behavioral signals into embeddings
- Encrypts those embeddings before storage or transmission
- Performs similarity search directly on encrypted vectors
- Releases only one bit of information:
##### ACCEPT or REJECT
At no point can behavioral patterns be reconstructed —
##### not by attackers, not by insiders, not even by the system owner.

## Why This Is Different
#### Traditional → Behavioral Auth	This System
- Plaintext embeddings →	Encrypted embeddings only
- DB breach = biometric leak →	DB breach reveals nothing
- Invertible vectors →	Inversion-resistant
- Server sees behavio r→	Server never sees behavior
- Privacy risk →	Privacy by construction

## Core Idea

We replace plaintext vector matching with encrypted vector similarity search powered by CyborgDB.

CyborgDB enables:

- Encrypted vector storage
- Encrypted similarity search
- Inversion-resistant embeddings
- Low-latency encrypted queries suitable for real-time login

This allows authentication systems where biometrics remain encrypted even during use.

## System Architecture (High-Level)
Browser (User)
  ↓
  
Behavior Capture (keystroke, mouse)

  ↓
  
Feature Extraction

  ↓
  
Behavioral Embedding

  ↓
Client-Side Encryption

  ↓
  
Auth Gateway (FastAPI)

  ↓
  
Encrypted Vector Search (CyborgDB)

  ↓
  
Decision Engine

  ↓
  
ACCEPT / REJECT

<img width="1536" height="1024" alt="ChatGPT Image Dec 25, 2025, 05_35_32 PM" src="https://github.com/user-attachments/assets/51ac94aa-a1a6-42fb-bbeb-d0d17bc4c154" />

### Trust Model

- Browser: trusted for capture + encryption
- Server: untrusted
- Database: untrusted

## Behavioral Signals Used (Privacy-Safe)
#### What We Collect

- Keystroke timing (dwell time, flight time)
- Mouse movement deltas, velocity, acceleration
- Statistical summaries only

#### What We Never Collect

- Typed characters
- Passwords
- Screen content
- UI context
- Raw behavioral logs

This design is safe even under forensic scrutiny.

## Encryption-in-Use

- Behavioral embeddings are encrypted using AES-GCM
- Encryption happens immediately after embedding generation
- No plaintext embeddings are stored, logged, or transmitted
- Keys are BYOK / HSM-ready

Even similarity search is performed inside encrypted space.

<img width="1536" height="1024" alt="ChatGPT Image Dec 25, 2025, 05_39_57 PM" src="https://github.com/user-attachments/assets/fc65016e-0a27-406b-99bb-b8335906ffb9" />

## Authentication Logic

- 1.User attempts login
- 2.New behavioral embedding is generated and encrypted
- 3.Encrypted similarity search is executed
- 4.Threshold-based decision is computed
- 5.Output:
- authenticated: true | false
- Optional anomaly flag

No scores, vectors, or identities are exposed.

## Advanced Security Features

- Behavioral anomaly detection
- Bot activity
- Session hijacking
- Replay behavior
- Multi-tenant isolation
- JWT-based authentication
- Role-Based Access Control (RBAC)
- Privacy-safe audit logging
- Security analytics without surveillance

## Privacy Guarantees

##### This system guarantees:

- Behavioral patterns cannot be reconstructed
- Embeddings cannot be inverted
- Server operators cannot access biometrics
- Database breaches reveal no usable data
- Only accept/reject decisions are exposed

##### This enables compliance with:

- GDPR
- HIPAA-style biometric protections
- Enterprise security reviews

## How to Run (One Command)
###### Requirements
- Docker ≥ 24
- Docker Compose ≥ v2

###### Start the system
- cd infra
- docker compose --env-file .env up --build

###### Open:
- http://localhost:8000/docs

You will see a fully functional Swagger UI.

### How to Test

- 1.Generate encrypted behavioral embeddings
- 2.Register once using /register
- 3.Login using /login
- 4.Observe:
- authenticated: true | false
- anomaly detection flag
- 5.Check /metrics (admin-only)

No plaintext data is ever exposed.

#### Demo Highlights

- Live behavioral capture
- Encrypted embedding generation
- Encrypted vector similarity search
- Accept / reject authentication
- Privacy guarantees slide

## Impact
#### This system enables:

- Secure enterprise login
- Passwordless authentication
- Phishing resistance
- Bot & credential-stuffing defense
- Zero-trust identity systems

#### Applicable to:

- Finance
- Healthcare
- Government
- Enterprise SSO
- Critical infrastructure portals

### Why This Matters

Behavioral biometrics are powerful — but unsafe today.

This project shows that behavior-based authentication can be both secure and private, unlocking adoption at global scale.

- This is not just a feature.
- It is a new model for authentication.

### Built With

- Python 3.10
- FastAPI
- AES-GCM encryption
- Encrypted vector search (CyborgDB)
- Docker & Docker Compose

#### Final Note

This prototype demonstrates that AI systems do not need to trade privacy for intelligence.

Encrypted behavioral authentication is no longer theoretical —
it is deployable, auditable, and safe.
