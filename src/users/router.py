from fastapi import APIRouter,Depends,status
from src.users.dtos import UserSchema
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.users import contoller

user_routes=APIRouter(prefix="/user")

@user_routes.post("/register",status_code=status.HTTP_201_CREATED)
def register(body:UserSchema,db:Session=Depends(get_db)):
    return contoller.register(body,db)


