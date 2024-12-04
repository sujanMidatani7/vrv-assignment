from fastapi import APIRouter, Depends, HTTPException
from auth.utils import get_current_user

router = APIRouter(prefix="/protected", tags=["Protected"])

@router.get("/admin")
async def admin_route(current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "Admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return {"message": "Welcome, Admin!"}

@router.get("/user")
async def user_route(current_user: dict = Depends(get_current_user)):
    return {"message": f"Hello, {current_user['username']}"}
