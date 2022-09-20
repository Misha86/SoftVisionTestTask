from pydantic import (BaseModel, Field, EmailStr)


class UserBase(BaseModel):
    name: str = Field(title="The name of the user", max_length=50)
    age: int = Field(gt=0, le=100, title="User age")
    email: EmailStr


class GameBase(BaseModel):
    name: str


class ConnectionBase(BaseModel):
    game_id: int
