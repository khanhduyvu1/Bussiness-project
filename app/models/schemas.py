from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    description: str
    price: float
    in_stock: int

class BookDisplay(BookCreate):
    id: int

class UserCreate(BaseModel):
    username: str
    password: str

class UserDisplay(BaseModel):
    id: int
    username: str
    is_active: bool
