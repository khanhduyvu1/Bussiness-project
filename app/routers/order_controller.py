from fastapi import APIRouter, Depends, HTTPException
from schemas.database import SessionLocal
from sqlalchemy.orm import Session

from models.cart import CartItem
from models.order import Order
from routers.auth import get_current_user

router = APIRouter(tags=['Orders'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/orders")
def create_order(db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    cart_items = db.query(CartItem).filter(CartItem.user_id == user_id).all()
    if not cart_items:
        raise HTTPException(status_code=404, detail="No items in cart to create order")

    # Create and save a new order
    new_order = Order(user_id=user_id)
    db.add(new_order)
    db.commit()
    
    # Assume the cart is cleared after the order is created
    for item in cart_items:
        db.delete(item)
    db.commit()

    return {"order_id": new_order.id, "status": "Order created"}