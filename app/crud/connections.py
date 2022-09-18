from fastapi import HTTPException
from sqlalchemy.orm import Session

from .. import models
from ..schemas import connections as schemas


def create_connection(db: Session, connection: schemas.ConnectionCreate):
    db_connection = models.Connection(**connection.dict())
    db.add(db_connection)
    db.commit()
    db.refresh(db_connection)
    return db_connection


def get_connection(db: Session, connection: schemas.ConnectionCreate):
    user_exists = db.query(models.User.id).filter_by(id=connection.user_id).first()
    game_exists = db.query(models.Game.id).filter_by(id=connection.game_id).first()
    if not user_exists and not game_exists:
        raise HTTPException(
            status_code=404, detail={"user": "User doesn't exist", "game": "Game doesn't exist"}
        )
    if not user_exists or not game_exists:
        raise HTTPException(
            status_code=404, detail=f"{'Game'if user_exists else 'User'} doesn't exist"
        )
    return db.query(models.Connection).filter(
        models.Connection.user_id == connection.user_id,
        models.Connection.game_id == connection.game_id
    ).first()


def get_connections(db: Session):
    return db.query(models.Connection).all()

