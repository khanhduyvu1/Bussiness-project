from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from datetime import datetime
from pydantic import BaseModel

from models.model_base import Base

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    order_id = Column(Integer, nullable=False)
    status = Column(String, default='pending')
    created_at = Column(DateTime, default=datetime.now)
    product_id = Column(Integer, ForeignKey("Items.id"), nullable=False)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, default=0)
    price = Column(Float, nullable = False)
    
class OrderInfo(BaseModel):
    order_id: int
    status: str
    created_at: datetime
    total_price: float
    