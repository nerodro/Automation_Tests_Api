from pydantic import BaseModel, validator, Field

from typing import ClassVar, Dict, List, Optional, Literal

class Post_Create(BaseModel):
    id: int
    name: Literal["johns"]
    job: str
    createdAt: str

class Post_Register(BaseModel):
    id: int
    email: Literal["eve.holt@reqres.in"]
    password: Literal["pistol"]
    #token: str

class Post_Login(BaseModel):
    token: str

