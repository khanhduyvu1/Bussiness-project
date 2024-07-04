from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from models.model_base import Base

class Items(Base):
    __tablename__ = "Items"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    category = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    manufacture = Column(String, nullable=True)
    created_date_time = Column(DateTime, default=datetime.now, nullable=False)
    last_updated_date_time = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )


class ItemsInfo(BaseModel):
    name: str
    category: str
    description: str
    price: float
    quantity: int
    manufacture: str


