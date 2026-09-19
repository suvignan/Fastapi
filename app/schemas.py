from  pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime


class UpdatePost(BaseModel):
    title : Optional[str] = None
    content : Optional[str] = None
    published : Optional[bool] = None

class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True

class PostCreate(PostBase): # Inherits from PostBase
    pass

class Post(PostBase): # Inherits from PostBase
    id : int
    created_at : datetime
    owner_id : int
    owner : "UserOut" # this is used to get the user who created the post, this is used to get the user who created the post


    class config:
        orm_mode = True


class UserCreate(BaseModel):
    email : EmailStr
    password : str

class UserOut(BaseModel):
    id :int
    email : EmailStr
    created_at : datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email : EmailStr
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None