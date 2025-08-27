
from src.schemas.schema import CreateCategorie , ReadCategorie , UpdateCategorie
from sqlalchemy.orm import Session

from fastapi import HTTPException , status

from src.models.models import Categories

def create_categorie(categorie : CreateCategorie, db : Session):
    categorie_saved = Categories(**categorie.model_dump())
    db.add(categorie_saved)
    db.commit()
    db.refresh(categorie_saved)
    return ReadCategorie.model_validate(categorie_saved)

def update_categorie(id : int , categorie : UpdateCategorie , db : Session):
    categorie_updated = db.query(Categories).filter(Categories.id == id).first()
    if not categorie_updated : 
        raise HTTPException(detail = "Categorie with this id not exist" , status_code = status.HTTP_404_NOT_FOUND)
    
    categorie_updated.name = categorie_updated.name if not categorie.name else categorie.name
    db.add(categorie_updated)
    db.commit()
    db.refresh(categorie_updated)
    return ReadCategorie.model_validate(categorie_updated)

def delete_categorie(id : int , db : Session):
    categorie = db.query(Categories).filter(Categories.id == id).first()
    if not categorie:
       raise HTTPException(detail = "Categorie with this Id not exist" , status_code = status.HTTP_404_NOT_FOUND)
    
    db.delete(categorie)
    db.commit()
    return "Categorie successfully deleted"

def get_categories(db : Session):
    categories = db.query(Categories).all()
    if len(categories)<=0:
        raise HTTPException(detail = "Not categorie found" , status_code = status.HTTP_404_NOT_FOUND)
    return categories


def get_categorie(id : int, db : Session):
    categorie = db.query(Categories).filter(Categories.id == id).first()
    if not categorie:
        raise HTTPException(detail = "categorie with this id not found" , status_code = status.HTTP_404_NOT_FOUND)
    
    return ReadCategorie.model_validate(categorie)
