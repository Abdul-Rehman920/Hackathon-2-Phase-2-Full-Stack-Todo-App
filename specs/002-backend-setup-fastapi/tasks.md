# Implementation Tasks: Backend Setup with FastAPI, SQLModel, Neon PostgreSQL, and JWT Auth

**Feature**: Backend Setup with FastAPI, SQLModel, Neon PostgreSQL, and JWT Auth  
**Feature Branch**: `002-backend-setup-fastapi`  
**Spec**: [spec.md](spec.md) | **Plan**: [plan.md](plan.md)  
**Created**: 2026-01-09

## Overview

This document outlines the implementation tasks for creating a backend service using FastAPI, SQLModel, and Neon PostgreSQL to support a todo application with user authentication and data isolation. The implementation includes JWT verification middleware to ensure all API endpoints require authentication, and all task operations are filtered by the authenticated user's ID to maintain data privacy. The service provides a health check endpoint and skeleton CRUD endpoints for task management under the /api/tasks path.

## Implementation Strategy

- **MVP Approach**: Start with User Story 1 (Backend Server Initialization) to establish the foundation
- **Incremental Delivery**: Each user story builds upon the previous, creating a working system at each phase
- **Parallel Opportunities**: Database models and authentication can be developed in parallel after foundational setup
- **Test-Driven**: Each component includes appropriate tests to ensure functionality

## Dependencies

- User Story 1 (Backend Server Initialization) must be completed before User Stories 2 and 3
- User Story 3 (JWT Authentication) must be implemented before User Story 2 (Task Management) endpoints become fully functional
- Database setup (Neon PostgreSQL) must be configured before task operations can be implemented

## Parallel Execution Examples

Per User Story:
- US1: Database setup and FastAPI app creation can happen in parallel
- US2: Individual CRUD endpoints can be implemented in parallel after base task model is created
- US3: JWT utility functions and middleware can be developed in parallel

---

## Phase 1: Setup

**Goal**: Establish project structure and foundational dependencies

- [X] T001 Create backend/ directory structure
- [X] T002 [P] Create requirements.txt with FastAPI, SQLModel, python-jose[cryptography], uvicorn, pytest, python-dotenv
- [X] T003 [P] Initialize .env file with DATABASE_URL and BETTER_AUTH_SECRET placeholders
- [X] T004 Create tests/ directory structure
- [X] T005 Create backend/routes/ directory

## Phase 2: Foundational Components

**Goal**: Set up core infrastructure needed by all user stories

- [X] T006 Install and configure python-dotenv for environment variable management
- [X] T007 Create backend/db.py with database engine and session setup using DATABASE_URL
- [X] T008 Create backend/models.py with Task SQLModel including id, title, description, completed, user_id, created_at, updated_at
- [X] T009 Create backend/dependencies.py with JWT verification dependency using BETTER_AUTH_SECRET
- [X] T010 Create backend/main.py with basic FastAPI app setup

## Phase 3: User Story 1 - Backend Server Initialization (Priority: P1)

**Goal**: Initialize FastAPI server that connects to Neon PostgreSQL and provides health endpoint

**Independent Test**: Server starts successfully and connects to database, health endpoint returns status

- [X] T011 [US1] Configure database connection in main.py using backend/db.py
- [X] T012 [US1] Create /health endpoint in main.py that returns {"status": "healthy"}
- [X] T013 [US1] Add database connectivity check to health endpoint
- [X] T014 [US1] Create tests/test_health.py with health endpoint tests
- [X] T015 [US1] Add startup event handler to verify database connection

## Phase 4: User Story 2 - Task Management with User Isolation (Priority: P2)

**Goal**: Implement task CRUD operations that are properly isolated by user

**Independent Test**: Create tasks for different users and verify each user can only access their own tasks

- [X] T016 [US2] Create backend/routes/tasks.py file
- [X] T017 [US2] Implement GET /api/tasks endpoint with user_id filtering
- [X] T018 [US2] Implement POST /api/tasks endpoint to create tasks with user_id
- [X] T019 [US2] Implement GET /api/tasks/{id} endpoint with user_id verification
- [X] T020 [US2] Implement PUT /api/tasks/{id} endpoint with user_id verification
- [X] T021 [US2] Implement DELETE /api/tasks/{id} endpoint with user_id verification
- [X] T022 [US2] Implement PATCH /api/tasks/{id}/complete endpoint with user_id verification
- [X] T023 [US2] Add user_id filtering to all task operations to ensure data isolation
- [X] T024 [US2] Create tests/test_tasks.py with task CRUD tests
- [X] T025 [US2] Add indexes to Task model (user_id, completed, user_id+completed)

## Phase 5: User Story 3 - JWT Authentication Middleware (Priority: P3)

**Goal**: Implement JWT verification middleware so that all API endpoints can authenticate users

**Independent Test**: Send requests with valid and invalid JWT tokens to protected endpoints and verify proper authentication

- [X] T026 [US3] Enhance JWT verification dependency in backend/dependencies.py
- [X] T027 [US3] Add JWT token decoding using BETTER_AUTH_SECRET
- [X] T028 [US3] Extract user_id from JWT token for user isolation
- [X] T029 [US3] Apply JWT authentication to all task endpoints
- [X] T030 [US3] Create proper error responses for invalid/missing JWT tokens
- [X] T031 [US3] Add authorization checks to prevent users from accessing other users' tasks
- [X] T032 [US3] Update tests to include JWT authentication

## Phase 6: Polish & Cross-Cutting Concerns

**Goal**: Finalize implementation with proper error handling, validation, and documentation

- [X] T033 Add comprehensive error handling with appropriate HTTP status codes
- [X] T034 Add input validation for all API endpoints using Pydantic models
- [X] T035 Add logging for important operations and errors
- [X] T036 Add database transaction management where needed
- [X] T037 Update API documentation with authentication requirements
- [X] T038 Perform security review of JWT implementation
- [X] T039 Add performance optimizations (indexing, query optimization)
- [X] T040 Conduct end-to-end testing of all functionality