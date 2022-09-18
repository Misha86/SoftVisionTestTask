from fastapi import FastAPI
from .routers import (users, games, connections)


app = FastAPI()

app.include_router(users.router)
app.include_router(games.router)
app.include_router(connections.router)


