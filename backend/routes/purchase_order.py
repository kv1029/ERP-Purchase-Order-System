from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import jwt
import models
import schemas
from database import SessionLocal
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

# Authentication configuration 
# Note: These must match the exact configuration used in main.py to successfully decode the token
SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/google")

# Dependency to manage database session lifecycle
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Validates the incoming JWT and extracts the user's identity
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload 
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or missing token")

# Create a new purchase order securely bound to the requesting user
@router.post("/po")
def create_po(po: schemas.POCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    total = 0

    # Calculate the subtotal by fetching the current price of each item from the database
    for item in po.items:
        product = db.query(models.Product).filter(models.Product.id == item['product_id']).first()
        if product:
            total += product.price * item['qty']

    # Apply a standard 5% tax rate
    total_with_tax = total * 1.05

    db_po = models.PurchaseOrder(
        vendor_id=po.vendor_id,
        total=total_with_tax,
        status="CREATED",
        # Isolate data by associating the record with the authenticated user's email
        owner_email=user['sub'] 
    )

    db.add(db_po)
    db.commit()
    db.refresh(db_po)

    return db_po

# Retrieve all purchase orders explicitly belonging to the authenticated user
@router.get("/po")
def get_all_pos(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    orders = db.query(models.PurchaseOrder).filter(models.PurchaseOrder.owner_email == user['sub']).order_by(models.PurchaseOrder.id.desc()).all()
    return orders

# Update the status of an existing order
@router.patch("/po/{po_id}/status")
def update_po_status(po_id: int, new_status: str, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    # Query filters by both order ID and owner email to prevent unauthorized modifications
    po = db.query(models.PurchaseOrder).filter(
        models.PurchaseOrder.id == po_id, 
        models.PurchaseOrder.owner_email == user['sub']
    ).first()
    
    if not po:
        raise HTTPException(status_code=404, detail="Order not found or unauthorized")
        
    po.status = new_status
    db.commit()
    return {"message": f"Status updated to {new_status}"}

# Delete a specific purchase order
@router.delete("/po/{po_id}")
def delete_po(po_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    # Enforce strict ownership checks before allowing deletion
    po = db.query(models.PurchaseOrder).filter(
        models.PurchaseOrder.id == po_id, 
        models.PurchaseOrder.owner_email == user['sub']
    ).first()
    
    if not po:
        raise HTTPException(status_code=404, detail="Order not found or unauthorized")
        
    db.delete(po)
    db.commit()
    return {"message": "Order deleted successfully"}