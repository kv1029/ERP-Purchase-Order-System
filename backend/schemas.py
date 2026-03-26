from pydantic import BaseModel

class VendorCreate(BaseModel):
    name: str
    contact: str
    rating: float

class ProductCreate(BaseModel):
    name: str
    sku: str
    price: float
    stock: int

class POCreate(BaseModel):
    vendor_id: int
    items: list
