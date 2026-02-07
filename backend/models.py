from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, DateTime, Boolean, String, Index
import uuid


class UserBase(SQLModel):
    email: str = Field(unique=True, nullable=False)
    password_hash: str = Field(nullable=False)


class User(UserBase, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True)

    # Indexes for efficient querying
    __table_args__ = (
        Index('idx_user_email', 'email'),
        Index('idx_user_active', 'is_active'),
        {'extend_existing': True}
    )


class SessionBase(SQLModel):
    user_id: str = Field(nullable=False)
    token_type: str = Field(max_length=20, nullable=False)  # access, refresh
    token_hash: str = Field(max_length=255, nullable=False)
    expires_at: datetime = Field(nullable=False)


class Session(SessionBase, table=True):
    session_id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_used_at: datetime = Field(default_factory=datetime.utcnow)

    # Indexes for efficient querying
    __table_args__ = (
        Index('idx_session_user_id', 'user_id'),
        Index('idx_session_expires_at', 'expires_at'),
        Index('idx_session_token_type', 'token_type'),
        {'extend_existing': True}
    )


class TaskBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)
    user_id: str = Field(min_length=1)


class Task(TaskBase, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Indexes for efficient querying
    __table_args__ = (
        Index('idx_user_id', 'user_id'),
        Index('idx_completed', 'completed'),
        Index('idx_user_id_completed', 'user_id', 'completed'),
        {'extend_existing': True}
    )


class TaskCreate(TaskBase):
    pass


class TaskUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: Optional[bool] = None


class TaskCompletionUpdate(SQLModel):
    completed: bool