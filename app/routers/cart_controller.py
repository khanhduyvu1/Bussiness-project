from fastapi import APIRouter, Depends, HTTPException, Query, Path
from sqlalchemy.orm import Session
from typing import Annotated, List
from sqlalchemy.future import select
from datetime import datetime

from models.cart import CartItem, CartInfo, ProductInfo, CartList
from models.items import Items
from schemas.database import SessionLocal

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
    try:
        validate_cart(request)  # Assuming this is a custom validation function you've defined
        cart_products = []
        for item in request.items_list:
            # Fetch the item details once per product ID to avoid redundant database calls
            item_detail = db.query(Items).filter(Items.id == item.productId).first()
            if item_detail:
                db_item = CartItem(
                    cart_id=request.cartId,
                    product_id=item.productId,
                    product_name=item_detail.name,
                    quantity=item.quantity,
                    time=datetime.now()
                    
                )
                db.add(db_item)
                # Collect data for the response model
                cart_products.append(ProductInfo(
                    product_id=item.productId,
                    product_name=item_detail.name,
                    time=db_item.time,
                    quantity=item.quantity
                ))
        
        db.commit()
        
        # Construct the response based on the CartInfo model
        response = CartInfo(cartId=request.cartId, product=cart_products)
        return response
    finally:
        db.close()