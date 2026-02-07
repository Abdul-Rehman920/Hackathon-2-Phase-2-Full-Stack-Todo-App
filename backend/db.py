from sqlmodel import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.dialects.postgresql import psycopg  # ← Yeh line add karo (psycopg3 dialect)
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Create the database engine with psycopg3 dialect
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=300,
    dialect=psycopg.dialect(),  # ← Yeh force psycopg3 use karega
)

def get_session():
    """Get a database session"""
    from sqlmodel import Session
    with Session(engine) as session:
        yield session