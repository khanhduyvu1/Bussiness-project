from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from schemas.database import SessionLocal
import asyncio

from models.payment import PaymentMethod, Payment, PaymentInfo
from models.cart import CartItem

router = APIRouter(tags=['Payment'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def validate_payment_method(method: str):
    try:
        return PaymentMethod[method]
    except KeyError:
        raise ValueError(f"Invalid payment method: {method}")

@router.post("/payment/create", response_model=PaymentInfo, status_code=201)
async def create_payment(cart_id: int, amount: float, payment_method: str, db: Session = Depends(get_db)):
    try:
        results=db.query(CartItem).all()
        validated_method = validate_payment_method(payment_method)
        payment = Payment(
            cart_id=cart_id,
            amount=amount,
            payment_method=validated_method,
            status='Pending'
        )
        db.add(payment)
        db.commit()
        db.refresh(payment)
        
        await asyncio.sleep(5)
        payment.status = 'Completed'
        db.commit()
        db.refresh(payment)
        for item in results:
            db.delete(item)
        db.commit()
        return payment
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database transaction failed.")

@router.get("/payment/{payment_id}", response_model=PaymentInfo)
async def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(Payment).filter(Payment.cart_id== payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment
