from datetime import timedelta

from fastapi import (HTTPException, Depends, APIRouter)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from .. import settings
from ..crud.tokens import create_access_token, authenticate_user
from ..dependencies import get_db
from ..schemas.tokens import Token

router = APIRouter(
    prefix="/login",
    tags=["tokens"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=Token)
async def login(db: Session = Depends(get_db),
                form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db=db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
