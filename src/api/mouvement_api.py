from fastapi import APIRouter ,Depends
from src.schemas.schema import CreateMouvements , ReadMouvements
from src.services import product_mouvements_service
from src.db import get_db

from typing import List

mouvement_router = APIRouter(prefix = "/mouvements")

@mouvement_router.post("/")
def create_product_mouvement(mouvement : CreateMouvements , db = Depends(get_db)):
    product_mouvement = product_mouvements_service.create_mouvement(mouvement , db)
    return product_mouvement

@mouvement_router.get("/" , response_model = List[ReadMouvements])
def get_all_product_mouvements(db = Depends(get_db)):
    mouvements = product_mouvements_service.get_products_historique(db)
    
    return mouvements














































































































