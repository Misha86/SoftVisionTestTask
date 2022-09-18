from typing import List

from fastapi import (HTTPException, Depends, APIRouter)
from sqlalchemy.orm import Session

from .. import (database, schemas)
from ..crud import games


router = APIRouter(
    prefix="/games",
    tags=["games"],
    responses={404: {"description": "Not found"}},
)

get_db = database.get_db


@router.post("/", response_model=schemas.Game)
def create_game(game: schemas.GameCreate, db: Session = Depends(get_db)):
    db_game = games.get_game_by_name(db, game_name=game.name)
    if db_game:
        raise HTTPException(status_code=400, detail="Game already created")
    return games.create_game(db=db, game=game)


@router.get("/", response_model=List[schemas.Game])
def read_games(db: Session = Depends(get_db)):
    db_games = games.get_games(db)
    return db_games


@router.get("/{game_id}", response_model=schemas.Game)
def read_game(game_id: int, db: Session = Depends(get_db)):
    db_game = games.get_game(db, game_id=game_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return db_game
