from fastapi import FastAPI

from .database import (engine, Base)
from .routers import (users, games, connections, tokens)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(games.router)
app.include_router(connections.router)
app.include_router(tokens.router)


