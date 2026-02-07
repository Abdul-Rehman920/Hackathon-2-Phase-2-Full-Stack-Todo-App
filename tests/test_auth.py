import pytest
from fastapi.testclient import TestClient
from fastapi import HTTPException
from jose import jwt
import os
from datetime import datetime, timedelta
from backend.main import app
from backend.dependencies import verify_token, create_access_token
from backend.models import User
from sqlmodel import Session, select

# Set up test environment
os.environ["BETTER_AUTH_SECRET"] = "test-secret-key-for-testing"

client = TestClient(app)

def test_create_access_token():
    """Test creating an access token"""
    data = {"sub": "test-user-id"}
    token = create_access_token(data=data)
    
    # Decode the token to verify it was created correctly
    decoded = jwt.decode(token, os.environ["BETTER_AUTH_SECRET"], algorithms=["HS256"])
    assert decoded["sub"] == "test-user-id"
    assert "exp" in decoded

def test_verify_valid_token():
    """Test verifying a valid token"""
    # Create a valid token
    data = {"sub": "test-user-id"}
    token = create_access_token(data=data)
    
    # Verify the token
    payload = verify_token(token)
    assert payload["sub"] == "test-user-id"

def test_verify_invalid_token():
    """Test verifying an invalid token"""
    # Create an invalid token
    invalid_token = "invalid.token.here"
    
    # Verify should raise an HTTPException
    with pytest.raises(HTTPException) as exc_info:
        verify_token(invalid_token)
    
    assert exc_info.value.status_code == 401

def test_verify_expired_token():
    """Test verifying an expired token"""
    # Create an expired token
    data = {"sub": "test-user-id"}
    expired_token = create_access_token(
        data=data, 
        expires_delta=timedelta(seconds=-1)  # Expired 1 second ago
    )
    
    # Verify should raise an HTTPException
    with pytest.raises(HTTPException) as exc_info:
        verify_token(expired_token)
    
    assert exc_info.value.status_code == 401

def test_auth_signup():
    """Test user signup endpoint"""
    # Clear any existing test user
    with Session(app.state.engine) as session:
        existing_user = session.exec(select(User).where(User.email == "test@example.com")).first()
        if existing_user:
            session.delete(existing_user)
            session.commit()
    
    # Test signup
    response = client.post("/api/auth/signup", json={
        "email": "test@example.com",
        "password": "securepassword123"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True

def test_auth_signin():
    """Test user signin endpoint"""
    # First, create a user
    signup_response = client.post("/api/auth/signup", json={
        "email": "signin-test@example.com",
        "password": "securepassword123"
    })
    assert signup_response.status_code == 200
    
    # Then try to sign in
    response = client.post("/api/auth/signin", json={
        "email": "signin-test@example.com",
        "password": "securepassword123"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert "user" in data
    assert "id" in data["user"]
    assert "email" in data["user"]

def test_auth_me_with_valid_token():
    """Test /auth/me endpoint with valid token"""
    # First, create and sign in a user to get a token
    signup_response = client.post("/api/auth/signup", json={
        "email": "me-test@example.com",
        "password": "securepassword123"
    })
    assert signup_response.status_code == 200
    
    signin_response = client.post("/api/auth/signin", json={
        "email": "me-test@example.com",
        "password": "securepassword123"
    })
    assert signin_response.status_code == 200
    token_data = signin_response.json()
    token = token_data["access_token"]
    
    # Call /auth/me with the token
    response = client.get("/api/auth/me", headers={
        "Authorization": f"Bearer {token}"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert "user" in data
    assert "id" in data["user"]
    assert "email" in data["user"]

def test_auth_me_with_invalid_token():
    """Test /auth/me endpoint with invalid token"""
    response = client.get("/api/auth/me", headers={
        "Authorization": "Bearer invalid-token"
    })
    
    assert response.status_code == 401