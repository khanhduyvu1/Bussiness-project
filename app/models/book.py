from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    description: str
    price: float
    in_stock: int


