from cyborgdb.client import CyborgDBClient
from cyborgdb.singleton import db

db = CyborgDBClient()

def register_user(user_id: str, encrypted_embedding: dict, tenant: str):
    db.insert(tenant, encrypted_embedding, user_id)
    return {"status": "registered"}