import os
import numpy as np
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_embedding(embedding: np.ndarray, key: bytes) -> dict:
    """
    Encrypts a behavioral embedding using AES-GCM.
    """
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)

    payload = embedding.astype(np.float32).tobytes()
    ciphertext = aesgcm.encrypt(nonce, payload, None)

    return {
        "ciphertext": ciphertext.hex(),
        "nonce": nonce.hex()
    }

def decrypt_embedding(enc: dict, key: bytes) -> np.ndarray:
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(
        bytes.fromhex(enc["nonce"]),
        bytes.fromhex(enc["ciphertext"]),
        None
    )
    return np.frombuffer(plaintext, dtype=np.float32)