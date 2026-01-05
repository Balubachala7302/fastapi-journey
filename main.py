from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import FastAPI, Depends,HTTPException, status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

app = FastAPI()

SECRET_KEY = "super-secret-key"   # later → env variable
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

fake_user_db = {
    "bhaskar@example.com": {
        "username": "bhaskar",
        "email": "bhaskar@example.com",
        "hashed_password": "$2b$12$2ie3kibFP5IdiCFk9wJ8metH7juzSlp57gs/0Cbp0sHgM/f7cZTP2",  # password123
        "role": "admin"
    },
     "user@example.com": {
        "username": "normaluser",
        "email": "user@example.com",
        "hashed_password": "$2b$12$RELGUZrYHw13vOdMa00yVOcJ8O3.0aEDu2f0Rz1xw5Y.wvpMkgTDi", #password123
        "role": "user"
    }
}

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def authenticate_user(email: str, password: str):
    user = fake_user_db.get(email)
    if not user or not verify_password(password, user["hashed_password"]):
        return None
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = fake_user_db.get(email)
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def require_admin(user: dict = Depends(get_current_user)):
    if user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return user

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
    return{
  "name": "Bala",
  "learning": "FastAPI",
  "day": 1
}

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created",
        "user": user
    }


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

@app.get("/profile")
def profile(user: dict = Depends(get_current_user)):
    return {
        "message": "JWT authenticated profile",
        "user": user
    }


@app.get("/info")
def info(user: dict = Depends(get_current_user)):
    return {
        "message": "JWT authorized info access",
        "user": user
    }

@app.get("/admin/dashboard")
def admin_dashboard(admin: dict = Depends(require_admin)):
    return {
        "message": "Welcome Admin",
        "admin": admin["username"]
    }

@app.get("/me")
def my_profile(user: dict = Depends(get_current_user)):
    return {
        "message": "User profile",
        "user": user["username"],
        "role": user["role"]
    }
