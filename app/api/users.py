from fastapi import APIRouter, Depends,HTTPException,status
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import crud,schemas
from app.db.schemas import UserCreate
from app.core.permissions import require_role
from app.services.user_service import register_user

router = APIRouter(prefix="/users",tags=["Users"])



@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user)

@router.get("/admin/dashboard")
def admin_dashboard(
    current_user=Depends(require_role("admin"))
):
    return{"message":"Welcome admin"}
