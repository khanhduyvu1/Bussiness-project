from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import timedelta, datetime, timezone
from jose import jwt, JWTError
from starlette import status
import os

from models.user import UserCreate, User, Token, UserDTO
from schemas.database import SessionLocal


router = APIRouter(tags=['User'])

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/users/", response_model=UserDTO)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = User(username=user.username, password = user.password, 
                       hashed_password=bcrypt_context.hash(user.password))
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        db.close()
        raise HTTPException(status_code=400, detail=str(e))
@router.post("/token", response_model=Token)
async def token_login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], 
                      db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code = 401, detail = 'Invalid user')
    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return{'access_token': token, 'token_type': 'bearer'}

def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))

@router.get("/users/")
async def user_info(user_id: int, db: Session = Depends(get_db)):
    results = db.query(User).filter(User.id == user_id).first()
    if not results:
        raise HTTPException(status_code=404, detail="User not found")
    return results