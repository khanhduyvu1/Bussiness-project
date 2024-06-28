from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import SessionLocal
from sqlalchemy.future import select

from models.schemas import BookDisplay, BookCreate
from models.models_controller import Book

router = APIRouter()

async def get_session():
    async with SessionLocal() as session:
        yield session
        
@router.post("/books/", response_model=BookDisplay)
async def create_book(book: BookCreate, session: AsyncSession = Depends(get_session)):
    db_book = Book(**book.model_dump())
    session.add(db_book)
    await session.commit()
    await session.refresh(db_book)
    return db_book

@router.get("/books/", response_model=list[BookDisplay])
async def read_books(session: AsyncSession = Depends(get_session)):
    async with session.begin():
        result = await session.execute(select(Book))
        books = result.scalars().all()
    return books