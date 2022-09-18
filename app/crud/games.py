from sqlalchemy.orm import Session

from .. import models
from ..schemas import games as schemas


def get_game(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()


def get_game_by_name(db: Session, game_name: str):
    return db.query(models.Game).filter(models.Game.name == game_name).first()


def get_games(db: Session):
    return db.query(models.Game).all()


def create_game(db: Session, game: schemas.GameCreate):
    db_game = models.Game(**game.dict())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game
