from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from models.model_base import Base

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, index=True)
    author = Column(String)
    description = Column(String)
    price = Column(Float)
    in_stock = Column(Integer)
    created_date_time = Column(DateTime, default=datetime.now, nullable=False)
    last_updated_date_time = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )


class BookCreate(BaseModel):
    title: str
    author: str
    description: str
    price: float
    in_stock: int


