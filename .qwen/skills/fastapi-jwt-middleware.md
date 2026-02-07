# Skill: FastAPI JWT Verification Middleware

Use this pattern to verify JWT and get current user in FastAPI:

```python
from fastapi import Depends, HTTPException, Header
from jose import JWTError, jwt
from sqlmodel import Session

SECRET_KEY = os.getenv("BETTER_AUTH_SECRET")
ALGORITHM = "HS256"

def get_current_user(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(401, "Invalid token")
    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(401, "Invalid token")
        return user_id
    except JWTError:
        raise HTTPException(401, "Invalid token")

# Use in routes
@router.get("/tasks")
def get_tasks(user_id: str = Depends(get_current_user), session: Session = Depends(get_db)):
    tasks = session.exec(select(Task).where(Task.user_id == user_id)).all()
    return tasks