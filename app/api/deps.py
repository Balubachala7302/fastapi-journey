from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.core.security import decode_access_token
from app.db import models
from app.core.redis import redis_client  # if using redis

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    # Optional: Redis blacklist check
    try:
        if redis_client.exists(token):
            raise HTTPException(
                status_code=401,
                detail="Token has been revoked"
            )
    except Exception:
        pass  # ignore if redis not running

    payload = decode_access_token(token)

    user = db.query(models.User).filter(
        models.User.id == payload.get("user_id")
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

def require_role(required_role: str):
    def role_checker(current_user = Depends(get_current_user)):
        if current_user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions"
            )
        return current_user
    return role_checker