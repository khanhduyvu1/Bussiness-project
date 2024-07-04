from fastapi import APIRouter, Depends, HTTPException
from schemas.database import SessionLocal
from sqlalchemy.orm import Session

from models.items import Items, ItemsInfo


router = APIRouter(tags=['Items'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/Items", response_model=ItemsInfo)
async def add_items(items: ItemsInfo, db: Session = Depends(get_db)):
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