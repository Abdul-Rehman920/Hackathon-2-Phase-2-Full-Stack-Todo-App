# Quickstart Guide: Backend Setup with FastAPI, SQLModel, Neon PostgreSQL, and JWT Auth

## Prerequisites

- Python 3.11+
- pip package manager
- Access to Neon PostgreSQL database (connection string)
- BETTER_AUTH_SECRET for JWT verification

## Setup Instructions

### 1. Clone and Navigate to Backend Directory
```bash
cd backend/
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the backend directory with the following:
```env
DATABASE_URL=your_neon_postgresql_connection_string
BETTER_AUTH_SECRET=your_jwt_secret_key
```

### 5. Run the Application
```bash
uvicorn main:app --reload --port 8000
```

The application will be available at `http://localhost:8000`

## API Endpoints

### Health Check
- `GET /health` - Check if the service is running

### Task Management
- `GET /api/tasks` - Get all tasks for authenticated user
- `POST /api/tasks` - Create a new task
- `GET /api/tasks/{id}` - Get a specific task
- `PUT /api/tasks/{id}` - Update a specific task
- `DELETE /api/tasks/{id}` - Delete a specific task
- `PATCH /api/tasks/{id}/complete` - Update task completion status

## Authentication

All task endpoints require a valid JWT token in the Authorization header:
```
Authorization: Bearer <your-jwt-token>
```

The token will be verified using the BETTER_AUTH_SECRET, and the user_id will be extracted to ensure proper data isolation.

## Testing

Run the tests using pytest:
```bash
pytest tests/
```

## Development

For development, use the `--reload` flag with uvicorn to automatically restart the server when code changes are detected.