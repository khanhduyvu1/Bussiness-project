from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from datetime import datetime
from pydantic import BaseModel

from models.model_base import Base

class Report(Base):
    __tablename__ = 'Report'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    report_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    total_price = Column(Float, nullable = False)
    
class ReportInfo(BaseModel):
    report_id: int
    status: str
    created_at: datetime
    total_price: float
    