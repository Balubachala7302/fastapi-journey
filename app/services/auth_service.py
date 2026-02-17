from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import timedelta
from app.db import crud
from app.core.security import (
    verify_password,
    create_access_token,
    create_refresh_token,
)
from app.core.config import get_settings

settings = get_settings()

def login_user(db: Session, email: str, password: str):
    user = crud.get_user_by_email(db, email)

    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        data={"sub": str(user.id), "role": user.role}
    )

    refresh_token = create_refresh_token(
        data={"sub": str(user.id)},
        expires_delta=timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }