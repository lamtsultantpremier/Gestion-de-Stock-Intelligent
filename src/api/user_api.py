from fastapi import APIRouter , Depends
from src.services import users_services
from src.schemas.schema import CreateUser , ReadUser , UpdateUser
from src.db import get_db

from typing import List

user_router = APIRouter(prefix = "/users")

@user_router.post("/" , response_model = ReadUser)
def create_user(user : CreateUser , db = Depends(get_db)):
    user = users_services.create_users(user , db)

    return user


@user_router.put("/{user_id}" , response_model = ReadUser)
def update_users(user_id : int , user : UpdateUser , db = Depends(get_db)):
    user = users_services.update_users(user_id , user , db)

    return user

@user_router.delete("/{user_id}")
def delete_user(user_id : int , db = Depends(get_db)):
    status = users_services.delete_users(user_id , db)

    return status
    
@user_router.get("/" , response_model = List[ReadUser])
def get_all_users(db = Depends(get_db)):
    users = users_services.get_users(db)

    return users

@user_router.get("/{user_id}")
def get_user_by_id(user_id : int , db = Depends(get_db)):
   user = users_services.get_user(user_id , db)

   return user
