from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

from models.model_base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    password = Column(String, nullable = False)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_date_time = Column(DateTime, default=datetime.now, nullable=False)
    last_updated_date_time = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )

class UserCreate(BaseModel):
    username: str
    password: str
    
class UserDTO(BaseModel):
    id: int
    username: str
    password: str
    

class Token(BaseModel):
    access_token : str
    token_type: str