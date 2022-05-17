"""
DB Model Files
"""
import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship, backref

from app.database.setup import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    email = Column(String, unique=True, index=True)
    name = Column(String, unique=False, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    context_list = relationship("UserContext", back_populates="user")


class Context(Base):

    __tablename__ = "context"

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    image_url = Column(Text, nullable=True)
    active = Column(Boolean)
    auto_process = Column(Boolean)
    mask_url = Column(Text, nullable=True)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)


class UserContext(Base):
    __tablename__ = "user_context"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    context_id = Column(Integer, ForeignKey("context.id"))
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    user = relationship("User", back_populates="context_list")
    context_info = relationship("Context", backref=backref("info", lazy="joined"))
