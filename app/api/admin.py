from fastapi import APIRouter, Depends, HTTPException, status
from app.core.security import get_current_user

router = APIRouter(tags=["Admin"])

def require_admin(user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return user

@router.get("/admin/dashboard")
def admin_dashboard(admin: dict = Depends(require_admin)):
    return {"message": "Welcome Admin", "admin": admin["username"]}
