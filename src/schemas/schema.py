from pydantic import BaseModel , Field , ConfigDict
from typing import Optional , List
from enum import Enum
from datetime import datetime
# Create User Schema
class UserBase(BaseModel):
    nom : str
    prenom : str
    phone_number : str
   
    model_config = ConfigDict(from_attributes = True)

class CreateUser(BaseModel):
    nom : str
    prenom : str
    phone_number : str



class ReadUser(CreateUser):
    id : int
    mouvements : Optional[List] = Field(default_factory = list)

    model_config = ConfigDict(from_attributes = True)

class UpdateUser(BaseModel):
    nom : str|None = None
    prenom : str|None = None
    phone_number : str|None = None


# Create Categorie Schema

class CreateCategorie(BaseModel):
    name : str

class ReadCategorie(BaseModel):
    id : int
    name : str

    model_config = ConfigDict(from_attributes = True)

class UpdateCategorie(BaseModel): 
    name : str

#Create Produit Schema
class ProduitBase(BaseModel):
    name : str
    prix : float
    stocke : int
    
    model_config = ConfigDict(from_attributes = True)

class CreateProduit(BaseModel):
    name : str
    prix : float
    id_categorie : Optional[int] = None

    model_config = ConfigDict(from_attributes = True)

class ReadProduit(BaseModel):
    id:int
    name : str
    prix : float
    stocke : int

    categorie : Optional[ReadCategorie] = None
    
    model_config = ConfigDict(from_attributes = True)

class UpdateProduit(BaseModel):
    name : str|None = None
    prix : float = None
    id_categorie : int|None = None
    

# Create Product Mouvements schema
class MouvementType(str, Enum):
    ENTREE = "ENTREE"
    SORTIE = "SORTIE"

class BaseMouvements(BaseModel):

    type : MouvementType
    quantite : int
    id_produit : int
    user_id : int

class CreateMouvements(BaseMouvements):
    pass

class ReadMouvements(BaseMouvements):
    id : int
    date: datetime

    user : Optional[UserBase] = None
    produit : Optional[ProduitBase] = None

    model_config = ConfigDict(from_attributes = True)


