from pydantic import BaseModel , Field , ConfigDict
from typing import Optional , List

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