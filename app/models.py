from sqlalchemy import (Column, Integer, String, ForeignKey)
from sqlalchemy.orm import relationship

from .database import Base


class Connection(Base):
    __tablename__ = "connections"

    user_id = Column(ForeignKey("users.id"), primary_key=True)
    game_id = Column(ForeignKey("games.id"), primary_key=True)
    user = relationship("User", back_populates="games")
    game = relationship("Game", back_populates="users")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String, unique=True)
    games = relationship("Connection", back_populates="user")

    def __repr__(self):
        return self.name


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    users = relationship("Connection", back_populates="game")

    def __repr__(self):
        return self.name

