from pydantic import (BaseModel, EmailStr)
from .base_schemas import ConnectionBase


class ConnectionCreate(ConnectionBase):
    pass


class ConnectionUser(BaseModel):

    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class ConnectionGame(BaseModel):

    id: int
    name: str

    class Config:
        orm_mode = True


class Connection(BaseModel):

    user: ConnectionUser
    game: ConnectionGame

    class Config:
        orm_mode = True


