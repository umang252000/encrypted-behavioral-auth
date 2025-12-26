# 🔐 Encrypted Behavioral Authenticator (CyborgDB)

A privacy-preserving behavioral biometric authentication system where
**behavioral embeddings never exist in plaintext** — even during login verification.

## Problem
Behavioral biometrics improve security but are dangerously invertible
when stored as plaintext embeddings.

## Solution
This system encrypts behavioral embeddings at creation time and performs
authentication entirely inside encrypted vector space using CyborgDB.

## Key Guarantees
- No raw behavior stored
- No plaintext embeddings
- No biometric reconstruction possible
- Accept / Reject only

## Architecture
See docs/architecture.md

## Demo
Live encrypted login verification with real keystroke behavior.

## Built For
Open Innovation • Privacy-First AI • Zero Trust Authentication