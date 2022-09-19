from typing import List

from fastapi import (HTTPException, Depends, APIRouter)
from sqlalchemy.orm import Session

from ..crud.users import get_user_by_email
from ..dependencies import (get_db, get_current_user)
from ..schemas import users as schemas
from ..crud import users


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.UserCreate)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = users.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return users.create_user(db=db, user=user)


@router.get("/", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    db_users = users.get_users(db)
    return db_users


@router.get("/me")
async def read_users_me(current_user: schemas.User = Depends(get_current_user)):
    return current_user


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = users.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/me/games")
async def read_own_games(db: Session = Depends(get_db),
                         current_user: schemas.User = Depends(get_current_user)) -> List:
    db_user = get_user_by_email(db=db, email=current_user.email)
    return [g.game.__dict__ for g in db_user.games]





