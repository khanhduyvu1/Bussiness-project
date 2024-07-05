from fastapi import APIRouter, Depends, HTTPException, Query, Path
from schemas.database import SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated, List
from sqlalchemy.future import select

from models.cart import CartItem, CartInfo, CartList
from models.items import Items

router = APIRouter(tags=['Cart'])

def validate_cart(request):
    db=SessionLocal()
    try:
        items_list = request.items_list
        # take item ID
        itemid = db.query(Items).all()
        item_num = [num.id for num in itemid]
        #print(item_num)
        #compare id from Items and Cart
        for i in items_list:
            #print(i.productId)
            if i.productId not in item_num:
                raise HTTPException(status_code=400, detail='Item not found')
    finally:
        db.close()

@router.post("/cart/add", response_model=CartInfo)
async def add_item_to_cart(request: CartList):
    db = SessionLocal()
    validate_cart(request)
    cart_items = CartItem(**request.model_dump())  
    db.add(cart_items)
    db.commit()
    db.refresh(cart_items)
    return cart_items