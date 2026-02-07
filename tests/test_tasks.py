import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

# Mock user ID for testing
MOCK_USER_ID = "test-user-123"

def mock_get_current_user():
    """Mock function to return a test user ID"""
    return MOCK_USER_ID

def test_create_task():
    """
    Test creating a new task
    """
    # Mock the authentication dependency
    with patch('routes.tasks.get_current_user', return_value=MOCK_USER_ID):
        response = client.post("/api/tasks", json={
            "title": "Test Task",
            "description": "Test Description"
        })
        
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Test Task"
        assert data["description"] == "Test Description"
        assert data["user_id"] == MOCK_USER_ID
        assert data["completed"] is False


def test_get_tasks():
    """
    Test getting all tasks for a user
    """
    # Mock the authentication dependency
    with patch('routes.tasks.get_current_user', return_value=MOCK_USER_ID):
        response = client.get("/api/tasks")
        
        assert response.status_code == 200
        data = response.json()
        # May be empty if no tasks exist, but should be a list
        assert isinstance(data, list)


def test_get_single_task():
    """
    Test getting a single task by ID
    """
    # First create a task
    with patch('routes.tasks.get_current_user', return_value=MOCK_USER_ID):
        create_response = client.post("/api/tasks", json={
            "title": "Test Task for Get",
            "description": "Test Description"
        })
        
        assert create_response.status_code == 201
        created_task = create_response.json()
        task_id = created_task["id"]
        
        # Now get the task
        response = client.get(f"/api/tasks/{task_id}")
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == task_id
        assert data["title"] == "Test Task for Get"


def test_update_task():
    """
    Test updating a task
    """
    # First create a task
    with patch('routes.tasks.get_current_user', return_value=MOCK_USER_ID):
        create_response = client.post("/api/tasks", json={
            "title": "Original Task",
            "description": "Original Description"
        })
        
        assert create_response.status_code == 201
        created_task = create_response.json()
        task_id = created_task["id"]
        
        # Now update the task
        response = client.put(f"/api/tasks/{task_id}", json={
            "title": "Updated Task",
            "description": "Updated Description",
            "completed": True
        })
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == task_id
        assert data["title"] == "Updated Task"
        assert data["completed"] is True


def test_delete_task():
    """
    Test deleting a task
    """
    # First create a task
    with patch('routes.tasks.get_current_user', return_value=MOCK_USER_ID):
        create_response = client.post("/api/tasks", json={
            "title": "Task to Delete",
            "description": "Description to Delete"
        })
        
        assert create_response.status_code == 201
        created_task = create_response.json()
        task_id = created_task["id"]
        
        # Now delete the task
        response = client.delete(f"/api/tasks/{task_id}")
        
        assert response.status_code == 204


def test_update_task_completion():
    """
    Test updating task completion status
    """
    # First create a task
    with patch('routes.tasks.get_current_user', return_value=MOCK_USER_ID):
        create_response = client.post("/api/tasks", json={
            "title": "Task to Complete",
            "description": "Description"
        })
        
        assert create_response.status_code == 201
        created_task = create_response.json()
        task_id = created_task["id"]
        
        # Now update completion status
        response = client.patch(f"/api/tasks/{task_id}/complete", json={
            "completed": True
        })
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == task_id
        assert data["completed"] is True