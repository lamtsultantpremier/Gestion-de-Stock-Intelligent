from sqlalchemy.orm import Session
from src.schemas.schema import CreateMouvements , ReadMouvements
from fastapi import HTTPException , status
from src.models.models import Mouvements , Produits , User

def create_mouvement(mouvement : CreateMouvements , db : Session):

    produit = db.query(Produits).filter(Produits.id == mouvement.id_produit).first()
    user = db.query(User).filter(User.id == mouvement.user_id).first()

    if mouvement.type.value == "ENTREE" :
        produit.stocke +=mouvement.quantite
        mouvement_created = Mouvements(type = mouvement.type,
                                   quantite = mouvement.quantite,
                                   id_produit = mouvement.id_produit,
                                   user_id = mouvement.user_id, 
                                   produit = produit , 
                                   user = user)
        
    elif mouvement.type.value == "SORTIE" and produit.stocke >= mouvement.quantite:
        produit.stocke -=mouvement.quantite
        mouvement_created = Mouvements(type = mouvement.type,
                                   quantite = mouvement.quantite,
                                   id_produit = mouvement.id_produit,
                                   user_id = mouvement.user_id, 
                                   produit = produit, 
                                   user = user)
        
    else:
        raise HTTPException(detail = "La quantité en stock n'est pas suffisante" , status_code = status.HTTP_409_CONFLICT)
    
    db.add(mouvement_created)
    db.commit()
    db.refresh(mouvement_created)

    return ReadMouvements.model_validate(mouvement_created)

def get_products_historique(db : Session):
    mouvements = db.query(Mouvements).all()
    if len(mouvements)== 0:
        raise HTTPException(detail = "Not Mouvements Found" , status_code = status.HTTP_404_NOT_FOUND)
    
    return mouvements