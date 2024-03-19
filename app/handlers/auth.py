from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.exc import NoResultFound
from fastapi.security import OAuth2PasswordRequestForm
from app.services import models
from app.schemas.auth import User, UserCreate, TokenPair
from ..services.auth import create_jwt_token_pair, get_current_user, is_admin_user
from app.database.connector import AsyncConnection, db_conn

router = APIRouter(prefix="/api", tags=["api"])


@router.get("/users", response_model=list[User])
async def get_users(admin: User = Depends(is_admin_user)):
    users = await models.User.all()

    return users


@router.post("/users", response_model=User)
async def register_user(user: UserCreate):
    new_user = await models.User.create_user(username=user.username, password=user.password, email=user.email)
    return new_user


@router.post("/token", )
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await  models.User.get_valid_user(username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_jwt_token_pair(user.id)
    return {"access_token": access_token, "token_type": "bearer"}
