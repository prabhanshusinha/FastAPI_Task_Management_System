from fastapi import APIRouter,Depends,status
from src.users.dtos import UserSchema,UserResponseSchema,LoginSchema
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.users import contoller

user_routes=APIRouter(prefix="/user")

@user_routes.post("/register",response_model= UserResponseSchema, status_code=status.HTTP_201_CREATED)
def register(body:UserSchema,db:Session=Depends(get_db)):
    return contoller.register(body,db)

@user_routes.post("/login", status_code=status.HTTP_200_OK)
def login(body:LoginSchema, db:Session=Depends(get_db)):
    return contoller.login_user(body,db)