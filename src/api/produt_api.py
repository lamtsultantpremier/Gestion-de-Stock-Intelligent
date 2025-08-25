from fastapi import FastAPI, APIRouter , Depends
from src.db import get_db

product_router = APIRouter(prefix = "/produits " )

@product_router.post("/")
def create_product(db = Depends(get_db)):
    return {"message" : "Database correctly created"}