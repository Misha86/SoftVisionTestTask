from typing import List

from fastapi import (Depends, FastAPI, HTTPException)
from sqlalchemy.orm import Session

from app import (crud_utils, models, schemas)
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_utils.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_utils.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud_utils.get_users(db)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_utils.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/games", response_model=schemas.Game)
def create_game(game: schemas.GameCreate, db: Session = Depends(get_db)):
    db_game = crud_utils.get_game_by_name(db, game_name=game.name)
    if db_game:
        raise HTTPException(status_code=400, detail="Game already created")
    return crud_utils.create_game(db=db, game=game)


@app.get("/games", response_model=List[schemas.Game])
def read_games(db: Session = Depends(get_db)):
    game = crud_utils.get_games(db)
    return game


@app.get("/games/{game_id}", response_model=schemas.Game)
def read_game(game_id: int, db: Session = Depends(get_db)):
    db_user = crud_utils.get_game(db, game_id=game_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return db_user


@app.post("/connections", response_model=schemas.Connection)
def create_connection(connection: schemas.ConnectionCreate, db: Session = Depends(get_db)):
    db_connection = crud_utils.get_connection(db, connection=connection)
    if db_connection:
        raise HTTPException(status_code=400, detail="Connection already created")
    return crud_utils.create_connection(db=db, connection=connection)


@app.get("/connections", response_model=List[schemas.Connection])
def read_connections(db: Session = Depends(get_db)):
    connections = crud_utils.get_connections(db)
    return connections
