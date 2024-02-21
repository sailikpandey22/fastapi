from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime


class Post_base(BaseModel):
    title: str
    content: str
    published: bool = True


class Create_post(Post_base):
    pass


class Update_post(Post_base):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class Post(Post_base):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True


class CreatUser(BaseModel):
    email: EmailStr
    password: str


class Userlogin(BaseModel):
    email: EmailStr
    password: str


class Token (BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id: int

    class Config:
        from_attributes = True
