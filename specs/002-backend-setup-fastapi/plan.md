# Implementation Plan: Backend Setup with FastAPI, SQLModel, Neon PostgreSQL, and JWT Auth

**Branch**: `002-backend-setup-fastapi` | **Date**: 2026-01-09 | **Spec**: [link](spec.md)
**Input**: Feature specification from `/specs/002-backend-setup-fastapi/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan implements a backend service using FastAPI, SQLModel, and Neon PostgreSQL to support a todo application with user authentication and data isolation. The implementation includes JWT verification middleware to ensure all API endpoints require authentication, and all task operations are filtered by the authenticated user's ID to maintain data privacy. The service provides a health check endpoint and skeleton CRUD endpoints for task management under the /api/tasks path.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: FastAPI, SQLModel, Neon PostgreSQL driver, python-jose[cryptography], pydantic, uvicorn
**Storage**: Neon Serverless PostgreSQL database accessed via DATABASE_URL environment variable
**Testing**: pytest with FastAPI test client, SQLModel testing utilities
**Target Platform**: Linux server (deployable to cloud platforms like Render, Heroku, or AWS)
**Project Type**: Web backend service with REST API endpoints
**Performance Goals**: Support 100 concurrent authenticated users, respond to health check in <1 second, database queries under 100ms
**Constraints**: All API endpoints must require JWT authentication, user data must be isolated by user_id, use environment variables for configuration
**Scale/Scope**: Support 10k+ users with their respective tasks, handle typical todo app load patterns

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Gate 1: Agentic Development Compliance
✅ Plan follows agentic development approach using Claude Code agents and Spec-Kit Plus

### Gate 2: Security-First Architecture
✅ Authentication required for all endpoints using JWT tokens
✅ User data isolation implemented via user_id filtering
✅ JWT verification enforced at backend level using BETTER_AUTH_SECRET

### Gate 3: Technology Stack Compliance
✅ Using Python FastAPI with SQLModel as required
✅ Neon Serverless PostgreSQL for database
✅ Following REST API standards under /api/ endpoints

### Gate 4: Full-Stack Integration Readiness
✅ API endpoints designed for frontend-backend interaction
✅ JWT tokens in Authorization: Bearer header format
✅ Shared BETTER_AUTH_SECRET between frontend and backend

### Gate 5: TDD Compliance
✅ Planning includes test coverage for all endpoints
✅ Will implement Red-Green-Refactor cycle during development

## Project Structure

### Documentation (this feature)

```text
specs/002-backend-setup-fastapi/
├── spec.md              # Feature specification
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── main.py              # FastAPI application entry point
├── db.py                # Database connection and session management
├── models.py            # SQLModel models (Task model with user_id)
├── dependencies.py      # JWT verification dependency and other DI
├── routes/
│   └── tasks.py         # Task CRUD endpoints under /api/tasks
├── .env                 # Environment variables (DATABASE_URL, BETTER_AUTH_SECRET)
├── requirements.txt     # Python dependencies
└── tests/
    ├── conftest.py      # Test configuration
    ├── test_health.py   # Health endpoint tests
    └── test_tasks.py    # Task CRUD endpoint tests
```

**Structure Decision**: Selected web application backend structure to align with frontend in the existing frontend/ directory. Backend service will be in dedicated backend/ directory with proper separation of concerns.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
