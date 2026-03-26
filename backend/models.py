from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Vendor(Base):
    __tablename__ = "vendors"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact = Column(String)
    rating = Column(Float)
    
    # Establishes a bidirectional relationship with the PurchaseOrder table
    purchase_orders = relationship("PurchaseOrder", back_populates="vendor")

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sku = Column(String)
    price = Column(Float)
    stock = Column(Integer)

class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"
    
    id = Column(Integer, primary_key=True, index=True)
    vendor_id = Column(Integer, ForeignKey("vendors.id"))
    total = Column(Float)
    status = Column(String)
    
    # Associates the record with a specific user account to ensure data privacy/tenant isolation
    owner_email = Column(String, index=True) 
    
    # Establishes a bidirectional relationship with the Vendor table
    vendor = relationship("Vendor", back_populates="purchase_orders")