import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def load_master_key():
    """
    In production, replace with:
    - HSM
    - KMS
    - BYOK vault
    """
    key = os.environ.get("MASTER_ENC_KEY")
    if key is None:
        raise RuntimeError("MASTER_ENC_KEY not set")
    return bytes.fromhex(key)

def generate_session_key():
    return AESGCM.generate_key(bit_length=256)