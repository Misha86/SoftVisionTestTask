from sqlalchemy import (Column, Integer, String, ForeignKey)
from sqlalchemy.orm import relationship

from .database import Base


class Connection(Base):
    __tablename__ = "connection"

    user_id = Column(ForeignKey("user.id"), primary_key=True)
    game_id = Column(ForeignKey("game.id"), primary_key=True)
    user = relationship("User", back_populates="games")
    game = relationship("Game", back_populates="users")

    def __repr__(self):
        return f"Connection: user {self.user} - game {self.game}"


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String, unique=True)
    games = relationship("Connection", back_populates="user")

    def __repr__(self):
        return self.name


class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    users = relationship("Connection", back_populates="game")

    def __repr__(self):
        return self.name

