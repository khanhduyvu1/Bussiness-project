from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
import bcrypt

from models.schemas import UserCreate, UserDisplay
from models.models_controller import User
from database import SessionLocal

router = APIRouter()

async def get_session():
    async with SessionLocal() as session:
        yield session
        
@router.post("/users/", response_model=UserDisplay)
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = User(username=user.username, hashed_password=hashed_password.decode('utf-8'))
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user