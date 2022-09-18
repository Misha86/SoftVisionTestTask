from pydantic import (BaseModel, Field, EmailStr)
from typing import (List, Any)
from pydantic.utils import GetterDict

from .base_schemas import (GameBase, UserBase)


class UserGameGetter(GetterDict):
    def get(self, key: str, default: Any = None) -> Any:
        if key in {'id', 'name'}:
            return getattr(self._obj.game, key)
        else:
            return super().get(key, default)


class UserCreate(UserBase):
    pass


class UserGameSchema(GameBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = UserGameGetter


class User(UserBase):
    id: int
    games: List[UserGameSchema] = []

    class Config:
        orm_mode = True
