from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer 
from app.api.deps import get_current_user
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.security import create_access_token
from app.db import crud
from jose import JWTError,jwt
from app.db.schemas import TokenResponse
from app.core.security import create_access_token, create_refresh_token,blacklist_token,decode_refresh_token
from app.db.crud import authenticate_user
from app.api.deps import get_db
from app.db.blacklist import is_token_blacklisted,blacklist_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

settings=get_settings()

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login")



@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form.username, form.password)
    access_token=create_access_token(
    data={
        "sub":str(user.id),
        "role":user.role
    }
)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        {"sub": user.email},
        timedelta(minutes=15)
    )

    refresh_token = create_refresh_token(
        {"sub": user.email},
        timedelta(days=7)
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


@router.post("/refresh")
def refresh_token(
    refresh_token: str,
    db: Session = Depends(get_db),
):
    # 1️⃣ Check if refresh token is blacklisted
    if is_token_blacklisted(db, refresh_token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token revoked",
        )

    # 2️⃣ Decode refresh token
    try:
        payload = decode_refresh_token(refresh_token)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )

    user_id: int | None = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
        )

    # 3️⃣ Get user from DB
    user = crud.get_user_by_id(db, user_id)
    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found or inactive",
        )

    # 4️⃣ Blacklist old refresh token (important 🔥)
    blacklist_token(db, refresh_token)

    # 5️⃣ Create new access token
    access_token = create_access_token(
        data={"sub": user.id}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }



@router.post("/logout")
def logout(token: str,
           db:Session=Depends(get_db)):
    blacklist_token(db,refresh_token)
    return{"message":"Logged out successfully"}

@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return current_user