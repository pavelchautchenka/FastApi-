from typing import List

from pydantic import BaseModel, Field, EmailStr
from datetime import datetime


class User(BaseModel):
    username: str = Field(..., min_length=2, max_length=100)
    email: EmailStr = Field(None)


class UserCreate(User):
    password: str = Field(..., min_length=8, max_length=300)


class HashPassword(UserCreate):
    hashed_password: str


class TokenPair(BaseModel):
    access_token: str
    refresh_token: str


class AccessToken(BaseModel):
    access_token: str


class RefreshToken(BaseModel):
    refresh_token: str


class UserInEvent(BaseModel):
    id: int
    username: str



class Event(BaseModel):
    id: int
    name: str
    meeting_time: datetime
    description: str
    users: List[UserInEvent] = []
