from sqlalchemy.orm import DeclarativeBase , MappedAsDataclass,Mapped, mapped_column , relationship
from sqlalchemy import String , FLOAT,ForeignKey , Enum , INTEGER , DateTime , func , text
from typing import List 
from datetime import datetime
import enum
class Base(DeclarativeBase , MappedAsDataclass):
    pass

class Produits(Base):
    __tablename__ = "produits"

    id : Mapped[int] = mapped_column(primary_key = True , autoincrement=True , init = False)

    name : Mapped[str] = mapped_column(String(255))
    prix : Mapped[float] = mapped_column(FLOAT)
    categorie_id : Mapped[int] = mapped_column(ForeignKey("categorie.id") , nullable = True)
    stocke : Mapped[int] = mapped_column(INTEGER , default = 0 , init = False , server_default = text("0"))

    
    categorie : Mapped["Categories"] = relationship(back_populates = "produits", default = None)

    mouvements : Mapped[List["Mouvements"]] = relationship(back_populates = "produit" , init = False , default_factory= list)
      
class Categories(Base):
    
    __tablename__ = "categorie"

    id : Mapped[int] = mapped_column(primary_key = True , autoincrement = True , init = False)
    name : Mapped[str] = mapped_column(String(255))

    produits : Mapped[List[Produits]] = relationship(back_populates = "categorie" , default_factory = list)

class MouvementType(enum.Enum):
   ENTREE = "ENTREE"
   SORTIE = "SORTIE"

class Mouvements(Base):
    __tablename__ = "mouvement"

    id : Mapped[int] = mapped_column(primary_key = True , autoincrement = True , init = False)
    type : Mapped[MouvementType] = mapped_column(Enum(MouvementType))
    quantite : Mapped[int] = mapped_column(INTEGER)
    date : Mapped[datetime] = mapped_column(DateTime(timezone = True) , init = False, server_default = func.now())

    id_produit : Mapped[int] = mapped_column(ForeignKey("produits.id"))
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))

    produit : Mapped[Produits] =relationship(back_populates = "mouvements")
    user : Mapped["User"] = relationship(back_populates = "mouvements")

class User(Base):
    __tablename__ = "users"
    id : Mapped[int] = mapped_column(primary_key = True , autoincrement = True , init = False)
    nom : Mapped[str] = mapped_column(String(255))
    prenom : Mapped[str] = mapped_column(String(255))
    phone_number : Mapped[str] = mapped_column(String(10))

    mouvements : Mapped[List[Mouvements]] = relationship(back_populates = "user" , init = False ,default_factory = list)


    
