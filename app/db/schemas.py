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

    class config:
        from_attributes=True


class PostCreate(BaseModel):
    title: str
    content: str

class PostOut(BaseModel):
    id: int
    title: str
    content: str

    model_config=ConfigDict(from_attributes=True)

class TokenResponse(BaseModel):
    access_token:str
    token_type:str