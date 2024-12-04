from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.schema import UserLogin
from auth.utils import verify_password, create_access_token, get_db
from db.schema import User
from sqlalchemy.future import select

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    query = select(User).where(User.username == user.username)
    result = await db.execute(query)
    db_user = result.scalars().first()

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": db_user.username, "role": db_user.role})
    return {"access_token": token, "token_type": "bearer"}
