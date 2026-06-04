from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from src.shortener.routers import shortener_router

import os

app = FastAPI(debug=os.getenv("DEBUG"))

app.include_router(shortener_router, tags=["shortener"])


@app.exception_handler(RequestValidationError)
async def request_validation_handler(request: Request, exc: RequestValidationError):
    errors = [
        {
            "type": error.get("type"),
            "field": error.get("loc")[-1],
            "message": error.get("msg"),
            "input": error.get("input")
        }
        for error in exc.errors()
    ]

    return JSONResponse(
        status_code=400,
        content={
            "errors": errors
        }
    )
