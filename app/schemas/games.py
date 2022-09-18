from typing import (Any, List)

from pydantic.utils import GetterDict
from .base_schemas import (UserBase, GameBase)


class GameUserGetter(GetterDict):
    def get(self, key: str, default: Any = None) -> Any:
        if key in {'id', 'name', 'age', 'email'}:
            return getattr(self._obj.user, key)
        else:
            return super().get(key, default)


class GameUserSchema(UserBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = GameUserGetter


class GameCreate(GameBase):
    pass


class Game(GameBase):
    id: int
    users: List[GameUserSchema] = []

    class Config:
        orm_mode = True
