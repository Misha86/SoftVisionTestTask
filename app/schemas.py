from pydantic import (BaseModel, Field, EmailStr)
from typing import (List, Any)
from pydantic.utils import GetterDict


class UserGameGetter(GetterDict):
    def get(self, key: str, default: Any = None) -> Any:
        if key in {'id', 'name'}:
            return getattr(self._obj.game, key)
        else:
            return super().get(key, default)


class UserBase(BaseModel):
    name: str = Field(title="The name of the user", max_length=50)
    age: int = Field(gt=0, le=100, title="User age")
    email: EmailStr


class GameBase(BaseModel):
    name: str


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


class ConnectionBase(BaseModel):
    user_id: int
    game_id: int


class ConnectionCreate(ConnectionBase):
    pass


class Connection(ConnectionBase):

    class Config:
        orm_mode = True


