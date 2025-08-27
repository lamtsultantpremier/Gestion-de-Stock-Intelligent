
from sqlalchemy.orm import Session
from fastapi import HTTPException , status
from src.schemas.schema import CreateProduit , ReadProduit , UpdateProduit
from src.models.models import Produits , Categories 

def create_produit(produit : CreateProduit , db : Session):
    current_categorie = db.query(Categories).filter(Categories.id == produit.id_categorie).first()
    produit_saved = Produits(name = produit.name,
                              prix = produit.prix,
                              categorie_id = current_categorie.id,
                              categorie = current_categorie)
    db.add(produit_saved)
    db.commit()
    db.refresh(produit_saved)

    return ReadProduit.model_validate(produit_saved)

def read_produit(id : int , db : Session):
    produit = db.query(Produits).filter(Produits.id == id).first()
    if not produit:
        raise HTTPException(detail = "Product with this id not found" , status_code = status.HTTP_404_NOT_FOUND)
    return ReadProduit.model_validate(produit)

def read_produits(db : Session):
    produits = db.query(Produits).all()
    if not produits:
        raise HTTPException(detail = "No products found")
    return produits

def update_produit(id : int , produit : UpdateProduit , db : Session):
    current_produit = db.query(Produits).filter(Produits.id == id).first()

    if not current_produit:
        raise HTTPException(detail = "Product with this id not exist in database")
    
    current_produit.name = current_produit.name if not produit.name else produit.name
    current_produit.prix = current_produit.prix if not produit.prix else produit.prix

    if produit.id_categorie is not None:
        current_produit.categorie_id == produit.id_categorie
        categorie = db.query(Categories).filter(Categories.id == produit.id_categorie).first()
        current_produit.categorie = categorie

    db.add(current_produit)
    db.commit()
    db.refresh(current_produit)
    return ReadProduit.model_validate(current_produit)

def delete_produit(id : int , db : Session):
    produit = db.query(Produits).filter(Produits.id == id).first()
    if not produit:
        raise HTTPException(detail = "Product with this id not found" , status_code = status.HTTP_404_NOT_FOUND)
    db.delete(produit)
    db.commit()
    return "Product successfully deleted"
    