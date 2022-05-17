"""
Schema file.

Author: Ninz
Declare needed schema for request, response, and data porting.
Use `orm_mode=True` to port to database schema
"""
import datetime
from pydantic import BaseModel, constr
from app.config import get_config


config = get_config()


class User(BaseModel):
    id: int
    name: str
    email: str
    updated_at: datetime.datetime
    created_at: datetime.datetime

    class Config:
        orm_mode = True


class Context(BaseModel):

    id: int
    name: str
    image_url: str
    active: bool
    auto_process: bool
    mask_url: str
    updated_at: datetime.datetime
    created_at: datetime.datetime

    class Config:
        orm_mode = True


class GetUsersFilter(BaseModel):
    name: str | None = None
    email: str | None = None


class CreateContext(BaseModel):
    user_id: int
    name: constr(max_length=config.max_context_name_length)
    image_url: str | None = None
    active: bool = True
    auto_process: bool = True
    mask_url: str | None = None
