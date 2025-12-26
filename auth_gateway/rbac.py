from jose import jwt
from datetime import datetime, timedelta

SECRET = "CHANGE_ME_FOR_PROD"
ALGO = "HS256"

def issue_token(user_id: str, role: str, tenant: str):
    payload = {
        "sub": user_id,
        "role": role,
        "tenant": tenant,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET, algorithm=ALGO)

def verify_token(token: str):
    return jwt.decode(token, SECRET, algorithms=[ALGO])