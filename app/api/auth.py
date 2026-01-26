from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer 
from app.core.security import get_current_user
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import create_access_token
from app.db.database import get_db
from app.db import crud
from jose import JWTError,jwt
from app.db.schemas import TokenResponse
from app.core.security import create_access_token, create_refresh_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login")


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Authenticate user and return JWT token
    """
    user = crud.authenticate_user(
        db=db,
        email=form_data.username,
        password=form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }




@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = crud.authenticate_user(
        db,
        email=form_data.username,
        password=form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        data={"sub": user.email}
    )

    refresh_token = create_refresh_token(
        data={"sub": user.email}
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


@router.post("/refresh")
def refresh_token(
    refresh_token: str,
    db: Session = Depends(get_db)
):
    db_token = crud.is_refresh_token_valid(db, refresh_token)

    if not db_token:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    # revoke old
    crud.revoke_refresh_token(db, refresh_token)

    # issue new
    new_refresh = create_refresh_token(
        data={"sub": db_token.user_id, "type": "refresh"}
    )

    crud.create_refresh_token(
        db,
        new_refresh,
        db_token.user_id,
        db_token.device
    )

    access = create_access_token(
        data={"sub": db_token.user_id, "type": "access"}
    )

    return {
        "access_token": access,
        "refresh_token": new_refresh
    }

@router.post("/logout")
def logout(refresh_token: str, db: Session = Depends(get_db)):
    crud.blacklisted_token(db, refresh_token)
    return {"message": "Logged out successfully"}

@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return current_user