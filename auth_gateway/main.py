from fastapi import FastAPI, Header, HTTPException
from auth_gateway.routes.register import register_user
from auth_gateway.routes.login import login_user
from auth_gateway.rbac import verify_token
from auth_gateway.metrics import METRICS

app = FastAPI()


def require_role(token: str, allowed_roles: list):
    """
    Verifies JWT and enforces RBAC
    """
    claims = verify_token(token)

    if claims["role"] not in allowed_roles:
        raise HTTPException(
            status_code=403,
            detail="Forbidden: insufficient role"
        )

    return claims


@app.get("/metrics")
def metrics(authorization: str = Header(...)):
    require_role(authorization.split()[1], ["admin"])
    return METRICS


@app.post("/register")
def register(payload: dict, authorization: str = Header(...)):
    """
    Admin-only user enrollment
    """
    claims = require_role(authorization.split()[1], ["admin"])

    return register_user(
        payload["user_id"],
        payload["encrypted_embedding"],
        claims["tenant"]
    )


@app.post("/login")
def login(payload: dict, authorization: str = Header(...)):
    """
    Behavioral authentication (user or admin)
    """
    claims = require_role(authorization.split()[1], ["user", "admin"])

    return login_user(
        payload["encrypted_embedding"],
        tenant=claims["tenant"]
    )


@app.get("/health")
def health():
    return {"status": "ok"}