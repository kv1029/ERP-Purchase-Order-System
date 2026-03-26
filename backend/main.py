from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import jwt
import datetime
import models
from database import engine

from routes.vendor import router as vendor_router
from routes.product import router as product_router
from routes.purchase_order import router as po_router

import os
from dotenv import load_dotenv

load_dotenv()

# Initialize database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Modern PO System API")

# Configure CORS to allow the frontend to communicate with the API
app.add_middleware(
    CORSMiddleware,
    # SECURITY NOTE: Wildcard origins ["*"] are fine for local dev, 
    # but should be restricted to the specific frontend domain in production.
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# JWT auth setup
SECRET_KEY = os.getenv("JWT_SECRET") 
ALGORITHM = "HS256"
# Points to our login endpoint so Swagger UI knows how to authenticate
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/google")

class GoogleToken(BaseModel):
    token: str
    email: str
    name: str

# Dependency to verify JWT on protected routes
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Health check endpoint
@app.get("/")
def root():
    return {"status": "Online", "version": "2.0.0"}

# Issue internal JWT upon receiving Google auth payload
@app.post("/auth/google")
def google_auth(data: GoogleToken):
    # SECURITY NOTE: For this assignment, we are trusting the token provided by the frontend.
    # In a production environment, you must cryptographically verify the Google token signature 
    # using Google's public keys before issuing your own session token to prevent spoofing.
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    
    jwt_payload = {
        "sub": data.email,
        "name": data.name,
        "exp": expiration
    }
    
    encoded_jwt = jwt.encode(jwt_payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": encoded_jwt, "token_type": "bearer"}

# Test route to verify token decoding works
@app.get("/secure-data")
def secure_data(user: dict = Depends(get_current_user)):
    return {"message": f"Hello {user['name']}, you are authenticated!"}

# Mount domain-specific routers
app.include_router(vendor_router, tags=["Vendors"])
app.include_router(product_router, tags=["Products"])
app.include_router(po_router, tags=["Purchase Orders"])