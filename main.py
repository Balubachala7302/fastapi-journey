from pydantic import BaseModel
from fastapi import FastAPI,Depends,Header,HTTPException,status

app = FastAPI()


def common_headers(token: str = Header(...)):
    if token !="my-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid or missing Token"
        )
    return {"app": "fastapi-journey", "version": "day-3"}

def get_current_user(token: str = Header(...)):
    if token !="secret-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid or missing token"
        )
    return{"username": "bhaskar","role": "admin"}

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

class Login(BaseModel):
    email: str
    password: str

@app.post("/login")
def login(data :Login):
    return{
        "message":"User login Successful",
        "email":data.email
    }

@app.get("/profile")
def profile(user: dict = Depends(get_current_user)):
    return {
        "message": "Autherization profile access",
        "user": user
    }

@app.get("/info")
def info(headers: dict= Depends(common_headers)):
    return{
        "message":"Authetrization Header access",
        "headers": headers
    }