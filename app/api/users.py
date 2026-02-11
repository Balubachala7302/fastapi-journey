from fastapi import APIRouter, Depends,HTTPException,status
from app.db.database import get_db
from sqlalchemy.orm import session
from app.db import crud,schemas
from app.core.permissions import require_role

router = APIRouter(prefix="/users",tags=["Users"])

@router.post("/register",response_model=schemas.UserOut)

def register_user(
    user:schemas.UserCreate,
    db:session=Depends(get_db)
):
    existing_user=crud.get_user_by_email(db,user.email)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    return crud.create_user(db,user)

@router.get("/admin/dashboard")
def admin_dashboard(
    current_user=Depends(require_role("admin"))
):
    return{"message":"Welcome admin"}
