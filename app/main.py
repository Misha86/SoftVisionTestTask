from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    age: int
    email: str


class Game(BaseModel):
    id: int
    name: str
    users: Optional[int]


@app.get("/games")
def get_games():
    return {"Hello": "Games"}


@app.get("/games/{game_id}")
def get_game(game_id: int):
    return {"Hello": f"World {game_id}"}


@app.put("/games/{game_id}")
def update_game(game_id: int, game: Game):
    return {"Hi": game}
