from typing import List
from sqlalchemy.orm import joinedload
from fastapi import Depends,status
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.exc import NoResultFound
from fastapi.security import OAuth2PasswordRequestForm
from app.services import models
from app.schemas.auth import User, UserCreate, TokenPair, Event
from ..services.auth import create_jwt_token_pair,get_current_user
from app.database.connector import AsyncConnection, db_conn
from datetime import datetime


router = APIRouter(prefix="/api", tags=["api"])


@router.get("/events", response_model=list[Event])
async def get_events():
    events = await models.Event.get_event()
    return events

@router.post("/event/{event_id}")
async def subscribe_to_event(event_id: int, user: User = Depends(get_current_user)):
    event = await models.Event.get_event(id=event_id)
    new_data = await models.User_Event.create(user_id=user.id,event_id=event.id)
    return new_data