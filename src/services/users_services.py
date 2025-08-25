from src.schemas.schema import CreateUser , ReadUser , UpdateUser 
from sqlalchemy.orm import Session
from fastapi import HTTPException , status
from src.models.models import User


def create_users(user : CreateUser , db : Session):
    user_saved =User(**user.model_dump())
    db.add(user_saved)
    db.commit()
    db.refresh(user_saved)

    return ReadUser.model_validate(user_saved)

def update_users(user_id : int , user : UpdateUser , db :Session):
    current_user = db.query(User).filter(User.id == user_id).first()
    if not current_user:
        raise HTTPException(detail = "User with this Id not found" , status_code = status.HTTP_404_NOT_FOUND)
    
    current_user.nom = current_user.nom if not user.nom else user.nom
    current_user.prenom = current_user.prenom if not user.prenom else user.prenom
    current_user.phone_number = current_user.phone_number if not user.phone_number else user.phone_number

    db.add(current_user)
    db.commit()
    db.refresh(current_user)

    return ReadUser.model_validate(current_user)

def delete_users(user_id : int , db : Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(detail = "User with this id not found" , status_code = status.HTTP_404_NOT_FOUND)
    db.delete(user)
    db.commit()

    return "User Successfully deleted"

def get_users(db : Session):
    users = db.query(User).all()
    if len(users) == 0:
        raise HTTPException(detail = "Aucun utilissateur n s'est inscrits" , status_code = status.HTTP_404_NOT_FOUND)
    return users

def get_user(user_id : int , db : Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(detail = "User Not found " , status_code = status.HTTP_404_NOT_FOUND)

    return ReadUser.model_validate(user)