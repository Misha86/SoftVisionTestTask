import uvicorn
from fastapi import FastAPI
from pydantic import (BaseModel, Field, EmailStr)
from typing import (List, Union)

app = FastAPI()


class Game(BaseModel):
    name: str


class User(BaseModel):
    name: str = Field(title="The name of the user", max_length=50)
    age: int = Field(gt=0, le=100, title="User age")
    email: EmailStr
    games: Union[List[Game], None] = None


@app.get("/games")
def get_games():
    return {"Hello": "Games"}


@app.get("/games/{game_id}")
def get_game(game_id: int):
    return {"Hello": f"World {game_id}"}


@app.put("/games/{game_id}")
def update_game(game_id: int, game: Game):
    return {"Hi": game}


@app.get("/users")
def get_users():
    return {"Hello": "users"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"Hello": f"World {user_id}"}


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {"Hi": user}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

