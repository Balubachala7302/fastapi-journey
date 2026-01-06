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

app = FastAPI()

# -------------------------------
# Fake Database (Day-7)
# -------------------------------
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

# -------------------------------
# Auth helpers
# -------------------------------
def authenticate_user(email: str, password: str):
    user = fake_user_db.get(email)
    if not user or not verify_password(password, user["hashed_password"]):
        return None
    return user

def require_admin(user: dict = Depends(get_current_user)):
    if user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return user

# -------------------------------
# Public Routes
# -------------------------------
@app.get("/")
def root():
    return {"message": "FastAPI 80/20 Journey Begins"}

@app.get("/health")
def health():
    return {"status": "OK", "service": "FastAPI"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/square/{number}")
def square(number: int):
    return {"number": number, "square": number * number}

@app.get("/about")
def about():
    return {
        "name": "Bala",
        "learning": "FastAPI",
        "day": 7
    }

# -------------------------------
# Auth Routes
# -------------------------------
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        data={"sub": user["email"]},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# -------------------------------
# Protected Routes
# -------------------------------
@app.get("/profile")
def profile(user: dict = Depends(get_current_user)):
    return {
        "message": "JWT authenticated profile",
        "user": user
    }

@app.get("/me")
def my_profile(user: dict = Depends(get_current_user)):
    return {
        "username": user["username"],
        "role": user["role"]
    }

# -------------------------------
# Admin-only Route
# -------------------------------
@app.get("/admin/dashboard")
def admin_dashboard(admin: dict = Depends(require_admin)):
    return {
        "message": "Welcome Admin",
        "admin": admin["username"]
    }
