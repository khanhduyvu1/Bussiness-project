from fastapi import APIRouter, Depends, HTTPException, Query, Path
from schemas.database import SessionLocal
from sqlalchemy.orm import Session
from typing import List

from models.items import Items, ItemsInfo
from routers.auth import get_current_user


router = APIRouter(tags=['Items'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# input item
@router.post("/Items", response_model=ItemsInfo)
async def add_items(items: ItemsInfo, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    db_items = Items(**items.model_dump())
    db.add(db_items)
    db.commit()
    db.refresh(db_items)
    return db_items

# item info
@router.get("/Items", response_model=ItemsInfo)
async def read_items(items_id: int, db: Session = Depends(get_db)):
    results = db.query(Items).filter(Items.id == items_id).first()
    if not results:
        raise HTTPException(status_code=404, detail="Item not found")
    return results

#search item
@router.get("/Items/search", response_model=List[ItemsInfo])
async def search_items(
    name: str = Query(None, description="Search by item name"),
    category: str = Query(None, description="Search by item category"),
    manufacture: str = Query(None, description="Search by manufacture"),
    db: Session = Depends(get_db)
):
    query = db.query(Items)
    if name:
        query = query.filter(Items.name.ilike(f"%{name}%"))
    if category:
        query = query.filter(Items.category.ilike(f"%{category}%"))
    if manufacture:
        query = query.filter(Items.manufacture.ilike(f"%{manufacture}%"))
    
    results = query.all()
    if not results:
        raise HTTPException(status_code=404, detail="No items found matching the criteria")
    
    return results

# update items
@router.put("/Items/update/{item_id}", response_model=ItemsInfo)
async def update_item(
    item_id: int,
    item_update: ItemsInfo = Depends(),
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    item = db.query(Items).filter(Items.id == item_id).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item_data = item_update.model_dump()  
    for key, value in item_data.items():
        setattr(item, key, value)
    
    db.commit()
    db.refresh(item)
    return item

#delete items (should be in the last row)
@router.delete("/Items/delete", status_code=204)
async def delete_item(item_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    # Retrieve the item from the database
    item = db.query(Items).filter(Items.id == item_id).first()
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}