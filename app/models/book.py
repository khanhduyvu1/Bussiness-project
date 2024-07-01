from pydantic import BaseModel
from model_base import BareBaseModel

class BookCreate(BareBaseModel):
    title: str
    author: str
    description: str
    price: float
    in_stock: int


