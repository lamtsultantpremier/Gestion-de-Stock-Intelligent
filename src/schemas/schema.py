from pydantic import BaseModel , Field , ConfigDict
from typing import Optional , List

# Create User Schema
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
class CreateProduit(BaseModel):
    name : str
    prix : float
    id_categorie : Optional[int] = None

class ReadProduit(BaseModel):
    id:int
    name : str
    prix : float

    categorie : Optional[ReadCategorie] = None
    
    model_config = ConfigDict(from_attributes = True)

class UpdateProduit(BaseModel):
    name : str|None = None
    prix : float = None
    id_categorie : int|None = None
    




