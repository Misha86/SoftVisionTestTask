from fastapi import HTTPException
from sqlalchemy.orm import Session

from .. import models
from ..schemas.connections import ConnectionCreate
from ..schemas.users import User


def create_connection(db: Session, connection: ConnectionCreate, user: User):
    db_connection = models.Connection(game_id=connection.game_id, user_id=user.id)
    db.add(db_connection)
    db.commit()
    db.refresh(db_connection)
    return db_connection


def get_connection(db: Session, connection: ConnectionCreate, user: User):
    user_exists = db.query(models.User.id).filter_by(id=user.id).first()
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
        models.Connection.user_id == user.id,
        models.Connection.game_id == connection.game_id
    ).first()


def get_connections(db: Session):
    return db.query(models.Connection).all()

