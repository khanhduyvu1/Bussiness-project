from pydantic import BaseModel
from sqlalchemy import Column, Integer, Float, String, ForeignKey, TIMESTAMP
from datetime import datetime
from models.model_base import Base
import enum
from sqlalchemy import Enum

class PaymentMethod(enum.Enum):
    credit_card = "credit_card"
    paypal = "paypal"
    debit_card = "debit_card"
    apple_pay = "apple_pay"
    google_pay = "google_pay"

class Payment(Base):
    __tablename__ = "Payments"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, default='pending')  # e.g., pending, completed, failed
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now)

class PaymentInfo(BaseModel):
    cart_id: int
    amount: float
    status: str
    payment_method: str
    created_at: datetime
