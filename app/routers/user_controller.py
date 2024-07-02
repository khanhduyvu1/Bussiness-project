from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
import bcrypt
from sqlalchemy.orm import Session

from models.user import UserCreate, UserDisplay, User
from schemas.database import SessionLocal

router = APIRouter(tags=['User'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/users/", response_model=UserDisplay)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    #hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    try:
        db_user = User(username=user.username, password=user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        db.close()
        raise HTTPException(status_code=400, detail=str(e))
@router.get("/users/")
async def user_info(user_id: int, db: Session = Depends(get_db)):
    results = db.query(User).filter(User.id == user_id).first()
    if not results:
        raise HTTPException(status_code=404, detail="User not found")
    return results