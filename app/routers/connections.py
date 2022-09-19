from typing import List

from fastapi import (HTTPException, Depends, APIRouter)
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..schemas import connections as schemas
from ..crud import connections


router = APIRouter(
    prefix="/connections",
    tags=["connections"],
    responses={404: {"description": "Not found"}}
)


@router.post("/connections", response_model=schemas.Connection)
def create_connection(connection: schemas.ConnectionCreate, db: Session = Depends(get_db)):
    db_connection = connections.get_connection(db, connection=connection)
    if db_connection:
        raise HTTPException(status_code=400, detail="Connection already created")
    return connections.create_connection(db=db, connection=connection)


@router.get("/connections", response_model=List[schemas.Connection])
def read_connections(db: Session = Depends(get_db)):
    db_connections = connections.get_connections(db)
    return db_connections
