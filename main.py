from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

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

@app.post("/Login")
def Login(data :Login):
    return{
        "message":"User login Successful",
        "email":data.email
    }