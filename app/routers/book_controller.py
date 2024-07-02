from fastapi import APIRouter, Depends, HTTPException
from schemas.database import SessionLocal
from sqlalchemy.orm import Session

from models.book import BookCreate, Book


router = APIRouter(tags=['Book'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/books/", response_model=BookCreate)
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get("/books/", response_model=BookCreate)
async def read_books(book_id: int, db: Session = Depends(get_db)):
    results = db.query(Book).filter(Book.id == book_id).first()
    if not results:
        raise HTTPException(status_code=404, detail="Book not found")
    return results