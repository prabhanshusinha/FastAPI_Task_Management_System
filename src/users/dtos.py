from pydantic import BaseModel

class UserSchema(BaseModel):
    name : str
    username : str
    password : str
    email : str
    mobile_no :str

class UserResponseSchema(BaseModel):
    name : str
    username : str
    email : str
    mobile_no :str
    id : int


class LoginSchema(BaseModel):
    username : str
    password : str