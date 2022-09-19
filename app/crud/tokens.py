from datetime import datetime, timedelta
from typing import Union

from jose import jwt
from sqlalchemy.orm import Session

from app import settings
from .users import get_user_by_email, verify_password


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def authenticate_user(email: str, password: str, db: Session):
    user = get_user_by_email(db=db, email=email)
    if not user or not verify_password(password, user.password):
        return False
    return user
