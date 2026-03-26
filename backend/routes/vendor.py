from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/vendors")
def create_vendor(vendor: schemas.VendorCreate, db: Session = Depends(get_db)):
    db_vendor = models.Vendor(**vendor.dict())
    db.add(db_vendor)
    db.commit()
    return db_vendor

@router.get("/vendors")
def get_vendors(db: Session = Depends(get_db)):
    return db.query(models.Vendor).all()