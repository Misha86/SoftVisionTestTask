from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import (database_exists, create_database)
from decouple import config


def get_postgres_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    return create_engine(url, echo=True)


engine = get_postgres_engine(
    user=config("POSTGRES_USER"),
    passwd=config("POSTGRES_PASSWORD"),
    host=config("POSTGRES_HOST"),
    port=config("POSTGRES_PORT"),
    db=config("POSTGRES_DB")
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
