from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.schema import UserCreate,User
from auth.utils import get_password_hash, get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register")
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if username or email exists
    existing_user = await db.execute(User.__table__.select().where((User.username == user.username) | (User.email == user.email)))
    if existing_user.scalars().first():
        raise HTTPException(status_code=400, detail="Username or email already exists")
    
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=get_password_hash(user.password),
        role="User"
    )
    db.add(new_user)
    await db.commit()
    return {"message": f"User {user.username} registered successfully"}
