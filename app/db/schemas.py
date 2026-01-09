from pydantic import BaseModel, EmailStr
from pydantic import ConfigDict

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    username: str
    email: EmailStr
    role: str

    model_config=ConfigDict(from_attributes=True)