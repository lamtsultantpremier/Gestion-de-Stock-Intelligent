from fastapi import APIRouter , Depends
from src.db import get_db

from src.schemas.schema import CreateCategorie , UpdateCategorie
from src.services import categories_services
categorie_router = APIRouter(prefix = "/categories")

@categorie_router.post("/")
def create_categorie(categorie : CreateCategorie , db = Depends(get_db)):
    categorie = categories_services.create_categorie(categorie , db)
    return categorie

@categorie_router.put("/{id}")
def update_categorie(id : int , categorie : UpdateCategorie , db = Depends(get_db)):
    categorie = categories_services.update_categorie(id , categorie , db)
    return categorie

@categorie_router.delete("/{id}")
def delete_categorie(id : int , db = Depends(get_db)):
    message = categories_services.delete_categorie(id , db)
    return message

@categorie_router.get("/")
def get_all_categories(db = Depends(get_db)):
    categories = categories_services.get_categories(db)
    return categories

@categorie_router.get("/{id}")
def get_categorie_by_id(id : int , db = Depends(get_db)):
    categorie = categories_services.get_categorie(id, db)
    return categorie