"""
HiveBox API - Main Application Module

Exposes the /version endpoint which returns the current app version.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
VERSION = "0.0.1"

@app.get("/version")
def get_version() -> JSONResponse:
    """Return the current application version as a JSON response."""
    return JSONResponse(content={"version": VERSION})
