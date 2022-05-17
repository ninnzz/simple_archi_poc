"""
Main file
"""
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

# App related imports
from app.database.setup import SessionLocal, engine, Base
from app.config import get_config

# Routes
from app.routes import context, user

from app.crud.user import populate_users


# Create all tables
Base.metadata.create_all(bind=engine)


# Populate user table
# TODO: For testing purposes only
def populate_table():
    db = SessionLocal()
    populate_users(db)
    db.close()


populate_table()

# Main app object
app = FastAPI()

config = get_config()


# HTTP Middleware
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.exception_handler(Exception)
async def unicorn_exception_handler(_: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "message": "Uh-oh, our gears are broken. Please contact admin.",
            "title": "Internal error occurred.",
            "details": str(exc)
        }
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=config.cors_allow_origin.split(','),
    allow_credentials=config.cors_allow_credentials,
    allow_methods=config.cors_allow_methods.split(','),
    allow_headers=config.cors_allow_headers.split(','),

)

# Template pages if you want to add some basic html pages
templates = Jinja2Templates(directory="pages")

# Add the router here
app.include_router(context.router)
app.include_router(user.router)
