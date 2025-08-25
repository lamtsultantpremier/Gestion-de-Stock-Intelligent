from sqlalchemy.orm import DeclarativeBase , MappedAsDataclass,Mapped, mapped_column , relationship
from sqlalchemy import String , FLOAT,ForeignKey , Enum , INTEGER , DateTime , func
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

    categorie : Mapped["Categories"] = relationship(back_populates = "produits")

    mouvement : Mapped["Mouvements"] = relationship(back_populates = "produits")
    
    categorie_id : Mapped[int] = mapped_column(ForeignKey("categorie.id") , nullable = True , default = None)
class Categories(Base):
    
    __tablename__ = "categorie"

    id : Mapped[int] = mapped_column(primary_key = True , autoincrement = True , init = False)
    name : Mapped[str] = mapped_column(String(255))

    produits : Mapped[List[Produits]] = relationship(back_populates = "categorie" , default_factory = list)

class MouvementType(enum.Enum):
   COME = "ENTREE"
   OUT = "SORTIE"

class Mouvements(Base):
    __tablename__ = "mouvement"

    id : Mapped[int] = mapped_column(primary_key = True , autoincrement = True , init = False)
    type : Mapped[MouvementType] = mapped_column(Enum(MouvementType , create_constraint = True))
    quantite : Mapped[int] = mapped_column(INTEGER)
    date : Mapped[datetime] = mapped_column(DateTime(timezone = True) , server_default = func.now()) 

    id_produit : Mapped[int] = mapped_column(ForeignKey("produits.id"))
    produits : Mapped[List[Produits]] =relationship(back_populates = "mouvement")

    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    user : Mapped["User"] = relationship(back_populates = "mouvements")

class User(Base):
    __tablename__ = "users"
    id : Mapped[int] = mapped_column(primary_key = True , autoincrement = True , init = False)
    nom : Mapped[str] = mapped_column(String(255))
    prenom : Mapped[str] = mapped_column(String(255))
    
    mouvements : Mapped[List[Mouvements]] = relationship(back_populates = "user" , default_factory = list)


    
