from fastapi import APIRouter, Depends, HTTPException
from database import SessionLocal
from sqlalchemy.orm import Session

from models.book import BookCreate
from models.models_controller import Book

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/books/")
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get("/books/")
async def read_books(book_id: int, db: Session = Depends(get_db)):
    results = db.query(Book).filter(Book.id == book_id)
    if not results:
        raise HTTPException(status_code=404, detail="Book not found")
    return results