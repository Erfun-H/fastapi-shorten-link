from fastapi import FastAPI
from src.shortener.routers import shortener_router

import os

app = FastAPI(debug=os.getenv("DEBUG"))

app.include_router(shortener_router, tags=["shortener"])
