from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


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


def create_connection(db: Session, connection: schemas.ConnectionCreate):
    db_connection = models.Connection(**connection.dict())
    db.add(db_connection)
    db.commit()
    db.refresh(db_connection)
    return db_connection


def get_connection(db: Session, connection: schemas.ConnectionCreate):
    return db.query(models.Connection).filter(
        models.Connection.user_id == connection.user_id,
        models.Connection.game_id == connection.game_id
    ).first()


def get_connections(db: Session):
    return db.query(models.Connection).all()

