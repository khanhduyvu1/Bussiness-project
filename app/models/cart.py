from pydantic import BaseModel
from typing import List
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP
from datetime import datetime

from models.model_base import Base


class CartItem(Base):
    __tablename__ = "Cart_Items"

    cart_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, nullable=False)
    product_name = Column(String, nullable=False)
    time = Column(TIMESTAMP, default=datetime.now)
    quantity = Column(Integer, default=0)
    
class CartInfo(BaseModel):
    cart_id: int
    product_id: int
    product_name: str
    time: datetime
    quantity: int

class Cart(BaseModel):
    productId: int
    quantity: int

class CartList(BaseModel):
    cart_id: int
    items_list: List[Cart]