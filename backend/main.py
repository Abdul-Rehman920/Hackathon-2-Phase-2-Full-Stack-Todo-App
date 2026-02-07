import logging
from fastapi import FastAPI, Depends, HTTPException, status, Request
from contextlib import asynccontextmanager
from typing import Generator
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import timedelta

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import database engine
from db import engine

# Import models to register them with SQLModel
from models import Task, User, Session

# Import dependencies for authentication
from dependencies import create_access_token, get_current_user

# Import routes
from routes import tasks

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@asynccontextmanager
async def lifespan(app: FastAPI) -> Generator:
    """
    Lifespan event handler for startup and shutdown events
    """
    # Startup: Initialize database connection
    logger.info("Initializing database connection...")
    try:
        # Attempt to connect to the database
        with engine.connect() as conn:
            logger.info("Database connection successful")

        # TEMPORARY: Create table if not exists (for dev only)
        from sqlmodel import SQLModel
        SQLModel.metadata.create_all(engine)  # ← Yeh line add kar do
        logger.info("Tables created or already exist")
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise

    yield  # Application runs during this period

    # Shutdown: Cleanup operations
    logger.info("Shutting down...")

# Create FastAPI app instance
app = FastAPI(
    title="Todo Backend API",
    description="API for managing user tasks with authentication and user isolation",
    version="1.0.0",
    lifespan=lifespan
)

# CORS Middleware (frontend se requests allow karne ke liye)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Authentication request/response models
class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    id: str
    email: str

# Authentication endpoints
@app.post("/api/auth/signup", tags=["authentication"])
async def signup(user_data: UserCreate):
    """
    Register a new user
    """
    from sqlmodel import Session as SQLSession
    from models import User

    # Check if user already exists
    with SQLSession(engine) as session:
        existing_user = session.query(User).filter(User.email == user_data.email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email already exists"
            )

        # Hash the password
        hashed_password = pwd_context.hash(user_data.password)

        # Create new user
        db_user = User(email=user_data.email, password_hash=hashed_password)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)

    return {"success": True, "message": "User registered successfully"}

@app.post("/api/auth/signin", tags=["authentication"])
async def signin(user_data: UserLogin):
    """
    Authenticate user and return JWT token
    """
    from sqlmodel import Session as SQLSession
    from models import User

    # Find user by email
    with SQLSession(engine) as session:
        db_user = session.query(User).filter(User.email == user_data.email).first()

        if not db_user or not pwd_context.verify(user_data.password, db_user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password"
            )

        # Create access token
        access_token_expires = timedelta(minutes=15)  # 15 minutes as per research
        access_token = create_access_token(
            data={"sub": db_user.id}, expires_delta=access_token_expires
        )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": db_user.id,
            "email": db_user.email
        }
    }

@app.get("/api/auth/me", tags=["authentication"])
async def get_current_user_info(current_user_id: str = Depends(get_current_user)):
    """
    Get current user info from JWT token
    """
    from sqlmodel import Session as SQLSession
    from models import User

    with SQLSession(engine) as session:
        user = session.get(User, current_user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return {"user": {"id": user.id, "email": user.email}}

# Include routes
app.include_router(tasks.router, prefix="/api", tags=["tasks"])

@app.get("/health", tags=["health"])
def health_check():
    """
    Health check endpoint with database connectivity
    """
    try:
        # Test database connectivity
        with engine.connect() as conn:
            logger.info("Health check: Database connection successful")
            pass  # Connection successful if no exception raised

        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)