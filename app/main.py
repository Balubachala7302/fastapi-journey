from datetime import timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from app.core.config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

from app.core.security import (
    create_access_token,
    get_current_user,
    verify_password
)

app = FastAPI(
    title="FastAPI Journey",
    version="0.1.0"
)

# -------------------------------------------------
# Fake Database (Day-7 → reused)
# -------------------------------------------------
fake_user_db = {
    "bhaskar@example.com": {
        "username": "bhaskar",
        "email": "bhaskar@example.com",
        "hashed_password": "$2b$12$2ie3kibFP5IdiCFk9wJ8metH7juzSlp57gs/0Cbp0sHgM/f7cZTP2",
        "role": "admin"
    },
    "user@example.com": {
        "username": "normaluser",
        "email": "user@example.com",
        "hashed_password": "$2b$12$RELGUZrYHw13vOdMa00yVOcJ8O3.0aEDu2f0Rz1xw5Y.wvpMkgTDi",
        "role": "user"
    }
}

# -------------------------------------------------
# Schemas (NEW in Day-8)
# -------------------------------------------------
class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    username: str
    email: str
    role: str


# -------------------------------------------------
# Auth Helpers
# -------------------------------------------------
def authenticate_user(email: str, password: str):
    user = fake_user_db.get(email)
    if not user:
        return None
    if not verify_password(password, user["hashed_password"]):
        return None
    return user


def require_admin(user: dict = Depends(get_current_user)):
    if user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return user


# -------------------------------------------------
# Public Routes
# -------------------------------------------------
@app.get("/", tags=["Public"])
def root():
    return {"message": "FastAPI 80/20 Journey Begins"}


@app.get("/health", tags=["Public"])
def health():
    return {"status": "OK", "service": "FastAPI"}


@app.get("/hello/{name}", tags=["Public"])
def hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/square/{number}", tags=["Public"])
def square(number: int):
    return {"number": number, "square": number * number}


@app.get("/about", tags=["Public"])
def about():
    return {
        "name": "Bala",
        "learning": "FastAPI",
        "day": 8
    }


# -------------------------------------------------
# Auth Routes
# -------------------------------------------------
@app.post(
    "/login",
    response_model=TokenResponse,
    tags=["Authentication"]
)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        data={"sub": user["email"]},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# -------------------------------------------------
# Protected Routes
# -------------------------------------------------
@app.get(
    "/profile",
    response_model=UserResponse,
    tags=["User"]
)
def profile(user: dict = Depends(get_current_user)):
    return {
        "username": user["username"],
        "email": user["email"],
        "role": user["role"]
    }


@app.get(
    "/me",
    tags=["User"]
)
def my_profile(user: dict = Depends(get_current_user)):
    return {
        "username": user["username"],
        "role": user["role"]
    }


# -------------------------------------------------
# Admin Routes
# -------------------------------------------------
@app.get(
    "/admin/dashboard",
    tags=["Admin"]
)
def admin_dashboard(admin: dict = Depends(require_admin)):
    return {
        "message": "Welcome Admin",
        "admin": admin["username"]
    }
