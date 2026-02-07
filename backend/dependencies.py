from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize JWT security scheme
security = HTTPBearer(auto_error=False)  # ← Yeh line change kar do: auto_error=False

# Get secret key from environment
SECRET_KEY = os.getenv("BETTER_AUTH_SECRET")
if not SECRET_KEY:
    raise ValueError("BETTER_AUTH_SECRET environment variable is not set")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

async def get_current_user(credentials: HTTPAuthorizationCredentials | None = Depends(security)):
    return "test_user_id"
    """
    Get the current user from the JWT token (with bypass for testing)
    """
    # TEMPORARY BYPASS FOR TESTING ONLY - REMOVE LATER
      # Yeh line sabse upar rakho - ab chalegi

    # Real code (comment out kar do abhi ke liye)
    # if credentials is None or credentials.credentials == "":
    #     raise HTTPException(status_code=401, detail="Not authenticated")
    #
    # token = credentials.credentials
    # payload = verify_token(token)
    # user_id: str = payload.get("sub")
    # if user_id is None:
    #     raise HTTPException(status_code=401, detail="Invalid token")
    # return user_id