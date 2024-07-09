from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime
from sqlalchemy.orm import Session

from models.cart import CartItem, CartInfo, ProductInfo, CartList
from models.items import Items
from schemas.database import SessionLocal

router = APIRouter(tags=['Cart'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
        item_aggregate = {}
        total_cart_price = 0.0
        cartId = request.cartId
        
        cart_ids = db.query(CartItem).filter(CartItem.cart_id==cartId).all()
        if cart_ids:
            for cart_id in cart_ids:
                db.delete(cart_id)
        db.commit()

    # Aggregate quantities for the same product ID
        for item in request.items_list:
            if item.productId in item_aggregate:
                item_aggregate[item.productId]['quantity'] += item.quantity
            else:
                item_aggregate[item.productId] = {'quantity': item.quantity}
                
        for product_id, aggregated_info in item_aggregate.items():
            # Fetch the item details once per product ID to avoid redundant database calls
            item_detail = db.query(Items).filter(Items.id == product_id).first()
            if item_detail:
                total_price = item_detail.price * aggregated_info['quantity']
                total_cart_price += total_price
                db_item = CartItem(
                    cart_id=request.cartId,
                    product_id=product_id,
                    product_name=item_detail.name,
                    quantity=aggregated_info['quantity'],
                    time=datetime.now(),
                    price=round(total_price, 2),
                )
                
                db.add(db_item)
                cart_products.append(ProductInfo(
                    product_id=product_id,
                    product_name=item_detail.name,
                    time=db_item.time,
                    quantity=aggregated_info['quantity'],
                    product_price=round(total_price, 2),
                ))
        db.commit()
        
        # Construct the response based on the CartInfo model
        response = CartInfo(cartId=request.cartId, product=cart_products, total=round(total_cart_price, 2))
        return response
    finally:
        db.close()
        
@router.get("/cart/view", response_model=CartInfo)
async def get_carts(id: int, db: Session = Depends(get_db)):
    cart_items = db.query(CartItem).filter(CartItem.cart_id == id).all()
    if not cart_items:
        raise HTTPException(status_code=404, detail="Cart not found")

    total_cart_price = 0.0
    product_info_list = []
    for item in cart_items:
        total_price = item.price
        total_cart_price += total_price
        product_info_list.append(ProductInfo(
            product_id=item.product_id,
            product_name=item.product_name,
            time=item.time,
            quantity=item.quantity,
            product_price=round(total_price, 2),
        ))

    response = CartInfo(
        cartId=id,
        product=product_info_list,
        total=round(total_cart_price, 2)
    )
    return response