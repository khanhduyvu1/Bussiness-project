from pydantic import BaseModel
from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Float
from datetime import datetime

from models.model_base import Base

class CartItem(Base):
    __tablename__ = "Cart_Items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, primary_key=True, nullable = False)
    product_id = Column(Integer, ForeignKey("Items.id"), nullable=False)
    product_name = Column(String, nullable=False)
    time = Column(TIMESTAMP, default=datetime.now)
    quantity = Column(Integer, default=0)
    price = Column(Float, nullable = False)
    
class ProductInfo(BaseModel):
    product_id: int
    product_name: str
    time: datetime
    quantity: int
    product_price: float
    
class CartInfo(BaseModel):
    cartId: int
    product: List[ProductInfo]
    total: float

class Cart(BaseModel):
    productId: int
    quantity: int

class CartList(BaseModel):
    cartId: int
    items_list: List[Cart]