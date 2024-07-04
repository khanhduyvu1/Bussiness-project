from fastapi import APIRouter, Depends, HTTPException
from schemas.database import SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated

from models.items import Items, ItemsInfo
from routers.auth import get_current_user


router = APIRouter(tags=['Items'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/Items", response_model=ItemsInfo)
async def add_items(items: ItemsInfo, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    db_items = Items(**items.model_dump())
    db.add(db_items)
    db.commit()
    db.refresh(db_items)
    return db_items

@router.get("/Items", response_model=ItemsInfo)
async def read_items(items_id: int, db: Session = Depends(get_db)):
    results = db.query(Items).filter(Items.id == items_id).first()
    if not results:
        raise HTTPException(status_code=404, detail="Item not found")
    return results

@router.delete("/Items/{item_id}", status_code=204)
async def delete_item(item_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    # Retrieve the item from the database
    item = db.query(Items).filter(Items.id == item_id).first()
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    # if item.owner_id != user['id']:
    #     raise HTTPException(status_code=403, detail="Not authorized to delete this item")
    # Delete the item from the database
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}