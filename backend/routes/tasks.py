from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlmodel import Session, select
from datetime import datetime

from models import Task, TaskCreate, TaskUpdate, TaskCompletionUpdate
from dependencies import get_current_user
from db import get_session

router = APIRouter()

@router.get("/tasks", response_model=List[Task])
def get_tasks(
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Get all tasks for the authenticated user
    """
    try:
        # Query tasks filtered by user_id
        statement = select(Task).where(Task.user_id == current_user_id)
        tasks = session.exec(statement).all()
        return tasks
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )


@router.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(
    task: TaskCreate,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Create a new task for the authenticated user
    """
    try:
        # Create task with the authenticated user's ID
        db_task = Task(
            title=task.title,
            description=task.description,
            completed=task.completed,
            user_id=current_user_id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        return db_task
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )


@router.get("/tasks/{task_id}", response_model=Task)
def get_task(
    task_id: int,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Get a specific task by ID for the authenticated user
    """
    try:
        statement = select(Task).where(Task.id == task_id, Task.user_id == current_user_id)
        task = session.exec(statement).first()

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        return task
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )


@router.put("/tasks/{task_id}", response_model=Task)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Update a specific task by ID for the authenticated user
    """
    try:
        statement = select(Task).where(Task.id == task_id, Task.user_id == current_user_id)
        db_task = session.exec(statement).first()

        if not db_task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        # Update task fields
        for field, value in task_update.dict(exclude_unset=True).items():
            setattr(db_task, field, value)

        db_task.updated_at = datetime.utcnow()
        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        return db_task
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Delete a specific task by ID for the authenticated user
    """
    try:
        statement = select(Task).where(Task.id == task_id, Task.user_id == current_user_id)
        db_task = session.exec(statement).first()

        if not db_task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        session.delete(db_task)
        session.commit()
        return
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )


@router.patch("/tasks/{task_id}/complete", response_model=Task)
def toggle_task_completion(
    task_id: int,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Toggle task completion status"""
    try:
        statement = select(Task).where(Task.id == task_id, Task.user_id == current_user_id)
        db_task = session.exec(statement).first()

        if not db_task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        # SIMPLE TOGGLE - body ki zarurat nahi
        db_task.completed = not db_task.completed
        db_task.updated_at = datetime.utcnow()

        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        return db_task
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {str(e)}"
        )