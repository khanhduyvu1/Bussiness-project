from fastapi import APIRouter, Depends, HTTPException, Path
from schemas.database import SessionLocal
from sqlalchemy.orm import Session
from datetime import datetime

from models.payment import Payment
from models.report import Report, ReportInfo
from routers.auth import get_current_user

router = APIRouter(tags=['Reports'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/report/insert/{report_id}")
def report_summary(report_id: int = Path(..., description="report_id = cart_id"), 
                   db: Session = Depends(get_db),
                   user: dict = Depends(get_current_user)):
    results = db.query(Payment).filter(Payment.cart_id == report_id).all()
    
    if not results:
        raise HTTPException(status_code=404, detail="No items in cart to create order")
    total_price = sum(item.price for item in results)
    # Create and save a new order
    
    new_report = Report(report_id=report_id,
                       total_price=total_price,
                       created_at=datetime.now(),
                       )
    db.add(new_report)
    db.commit()

    report = ReportInfo(
        report_id=new_report.report_id,
        status="Report created",
        created_at=new_report.created_at,
        total_price=new_report.total_price
    )
    
    return report

@router.get("/report/view")
async def report_summary_view(report_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    results = db.query(Report).filter(Report.report_id == report_id).first()
    if not results:
        raise HTTPException(status_code=404, detail="Report not found")
    return results