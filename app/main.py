from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import router
from .config import templates

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(router)
