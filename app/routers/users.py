from typing import List

from fastapi import (HTTPException, Depends, APIRouter)
from sqlalchemy.orm import Session

from .. import (database, schemas)
from ..crud import users

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

get_db = database.get_db


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = users.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return users.create_user(db=db, user=user)


@router.get("/", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    db_users = users.get_users(db)
    return db_users


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = users.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
