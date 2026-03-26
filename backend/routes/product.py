from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal
import random

router = APIRouter()

# Dependency to yield a database session per request and ensure it closes cleanly
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new product in the catalog
@router.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    
    # Refresh is required here to retrieve the auto-generated database ID
    db.refresh(db_product)   
    return db_product

# Retrieve all available products
@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

# Simulated AI endpoint to generate marketing copy for a given product
@router.get("/products/{product_id}/auto-description")
def generate_ai_description(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Note: In a production environment, this would make an external API call to an LLM.
    # For this prototype, we are mocking the response with randomized marketing buzzwords.
    buzzwords = ["unparalleled", "next-generation", "industry-leading", "ultra-efficient"]
    pitch = (
        f"Experience {random.choice(buzzwords)} performance with the {product.name}. "
        f"Engineered for reliability, it is the perfect addition to your professional workflow."
    )
    
    return {"description": pitch}