from typing import List

from fastapi import (HTTPException, Depends, APIRouter)
from sqlalchemy.orm import Session

from ..dependencies import (get_db, get_current_user)
from ..schemas.connections import (Connection, ConnectionCreate)
from ..schemas.users import User
from ..crud import connections


router = APIRouter(
    prefix="/connections",
    tags=["connections"],
    responses={404: {"description": "Not found"}}
)


@router.post("/", response_model=Connection)
def create_connection(connection: ConnectionCreate, db: Session = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    db_connection = connections.get_connection(db, connection=connection, user=current_user)
    if db_connection:
        raise HTTPException(status_code=400, detail="Connection already created")
    return connections.create_connection(db=db, connection=connection, user=current_user)


@router.get("/", response_model=List[Connection])
def read_connections(db: Session = Depends(get_db)):
    db_connections = connections.get_connections(db)
    return db_connections
