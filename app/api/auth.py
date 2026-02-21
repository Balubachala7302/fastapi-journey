from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.core.config import get_settings
from app.core.response import success_response
from app.core.security import create_access_token, decode_refresh_token
from app.db.schemas import TokenResponse, LoginSchema
from app.db import crud
from app.db.blacklist import is_token_blacklisted, blacklist_token
from app.services.auth_service import login_user


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

settings = get_settings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# -------------------------
# Login
# -------------------------
@router.post(
    "/login",
    response_model=TokenResponse,
    summary="Login user",
    description="Authenticates user and returns access + refresh tokens."
)
def login(
    data: LoginSchema,
    db: Session = Depends(get_db)
):
    tokens = login_user(db, data.email, data.password)

    return success_response(
        data=tokens,
        message="Login successful"
    )


# -------------------------
# Refresh Token
# -------------------------
@router.post(
    "/refresh",
    response_model=TokenResponse,
    summary="Refresh access token",
    description="Generates new access token using valid refresh token."
)
def refresh_token(
    refresh_token: str,
    db: Session = Depends(get_db),
):
    # 1️⃣ Check blacklist
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

    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
        )

    # 3️⃣ Validate user
    user = crud.get_user_by_id(db, user_id)
    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found or inactive",
        )

    # 4️⃣ Blacklist old refresh token
    blacklist_token(db, refresh_token)

    # 5️⃣ Create new access token
    access_token = create_access_token(
        data={"sub": user.id}
    )

    return success_response(
        data={
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        },
        message="Token refreshed successfully"
    )


# -------------------------
# Logout
# -------------------------
@router.post(
    "/logout",
    summary="Logout user",
    description="Blacklists the provided token."
)
def logout(
    token: str,
    db: Session = Depends(get_db)
):
    blacklist_token(db, token)

    return success_response(
        data=None,
        message="Logged out successfully"
    )


# -------------------------
# Current User
# -------------------------
@router.get(
    "/me",
    summary="Get current user",
    description="Returns currently authenticated user details."
)
def get_me(
    current_user = Depends(get_current_user)
):
    return success_response(
        data={
            "id": current_user.id,
            "email": current_user.email,
            "role": current_user.role
        },
        message="User fetched successfully"
    )