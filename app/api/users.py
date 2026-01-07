from fastapi import APIRouter, Depends
from app.core.security import get_current_user

router = APIRouter(tags=["Users"])

@router.get("/me")
def my_profile(user: dict = Depends(get_current_user)):
    return {
        "username": user["username"],
        "role": user["role"]
    }
