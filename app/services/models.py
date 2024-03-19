from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey, select, DateTime, Boolean
from sqlalchemy.orm import relationship
from ..database.base import Base, Manager
from passlib.context import CryptContext
from app.database.connector import db_conn



class User_Event(Base, Manager):
    __tablename__ = "user_event"

    user_id = Column(ForeignKey('users.id'),primary_key=True)
    event_id = Column(ForeignKey('events.id'), primary_key=True)

class User(Base, Manager):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(300), nullable=False)
    email = Column(String(100), nullable=True)
    is_admin = Column(Boolean(False))

    events = relationship("Event", secondary= User_Event.__table__, back_populates="users")

    def __str__(self):
        return f"User: {self.id}({self.username})"

    @classmethod
    async def create_user(cls, **kwargs):
        password = kwargs.get("password")
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        kwargs["password"] = pwd_context.hash(password)
        return await super().create(**kwargs)

    @classmethod
    async def get_valid_user(self, username: str, password: str) -> "User":
        query = select(User).where(User.username == username, User.password == password)
        async with db_conn.session as session:
            user = await session.execute(query)
            return user.scalar_one()
        if pwd_context.verify(password, user.password):
            return user
        else:
            return None

class Event(Base, Manager):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    description = Column(String(150),nullable=False)
    meeting_time = Column(DateTime, nullable=False)
    users = relationship("User", secondary=User_Event.__table__, back_populates="events", lazy="subquery")




