from fastapi import FastAPI, APIRouter , Depends
from src.db import get_db
from typing import List
from src.schemas.schema import CreateProduit , ReadProduit , UpdateProduit
from src.services import products_services
product_router = APIRouter(prefix = "/produits" )

@product_router.post("/")
def create_product(create_produit : CreateProduit , db = Depends(get_db)):
    produit = products_services.create_produit(create_produit , db)
    return produit

@product_router.get("/{id}")
def read_produit(id : int , db = Depends(get_db)):
    produit = products_services.read_produit(id , db)
    return produit

@product_router.get("/" , response_model = List[ReadProduit])
def read_produits(db = Depends(get_db)):
    produits = products_services.read_produits(db)
    return produits

@product_router.put("/{id}")
def update_produit(id:int , produit : UpdateProduit , db = Depends(get_db)):
    produit = products_services.update_produit(id , produit , db)
    return produit

@product_router.delete("/{id}")
def delete_produit(id : int , db = Depends(get_db)):
    message = products_services.delete_produit(id , db)
    return {"message" : message}