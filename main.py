from fastapi import FastAPI

from initializations.app import get_app
from initializations.db import SQLALCHEMY_DATABASE_URL

app: FastAPI = get_app()

@app.on_event("startup")
async def startup():
    print("[INFO] Starting server...")


@app.on_event("shutdown")
async def shutdown():
    print("[INFO] Shutting down...")

@app.get("/")
async def root() -> dict:
    return {"status": "ok"}


@app.get("/health-check")
async def health_check() -> dict:
    return {"status": "ok"}
