# Implementation Plan: Better Auth Integration and Secure API Calls

**Feature**: 003-better-auth-integration
**Created**: 2026-01-11
**Status**: Draft

## Technical Context

This feature implements Better Auth integration with JWT for secure API calls in a full-stack application. The implementation will include:

- Frontend authentication setup with Better Auth and JWT plugin
- Signup and signin forms
- JWT token retrieval from session and attachment to API requests
- Backend JWT verification middleware using python-jose
- Proper error handling for unauthorized access

### Technology Stack

- Frontend: Next.js with Better Auth client
- Backend: FastAPI with JWT middleware
- Authentication: Better Auth with JWT plugin
- Token Verification: python-jose library

### Unknowns

- JWT claims structure: Using standard claims with user_id for identification
- Token expiration policy: 15-minute access tokens with 7-day refresh tokens
- Frontend framework: Next.js 14 with App Router

## Constitution Check

### Alignment with Project Principles

- Security-First Architecture: JWT tokens will be properly validated to ensure secure access and user data isolation
- Agentic Development First: All implementation will follow agent specification and planning workflow
- Test-Driven Development: Comprehensive tests will be created for authentication functionality
- Modern Technology Stack: Using Better Auth with JWT plugin and python-jose as required
- Full-Stack Integration: Proper integration between frontend authentication and backend validation

### Potential Violations

- [GATE] Security: Ensure JWT tokens are properly validated using BETTER_AUTH_SECRET and user_id filtering is enforced
- [GATE] TDD: All authentication features must have tests written before implementation
- [GATE] Agentic Dev: All code must be generated through agent workflow, no manual coding

## Phase 0: Outline & Research

### Research Tasks

1. Better Auth JWT plugin implementation
2. JWT token handling in Next.js applications
3. python-jose library usage for token validation
4. Best practices for attaching JWT tokens to API requests
5. Frontend error handling for 401 responses

## Phase 1: Design & Contracts

### Data Model

#### User Entity
- id: Unique identifier for the user
- email: User's email address
- password: Hashed password
- createdAt: Account creation timestamp
- updatedAt: Last update timestamp

#### Session Entity
- sessionId: Unique session identifier
- userId: Reference to the user
- token: JWT token
- expiresAt: Token expiration time

### API Contracts

#### Authentication Endpoints

POST /api/auth/signup
- Request: {email: string, password: string}
- Response: {success: boolean, message?: string}

POST /api/auth/signin
- Request: {email: string, password: string}
- Response: {token: string, user: {id, email}}

GET /api/auth/me
- Headers: Authorization: Bearer {token}
- Response: {user: {id, email}}

#### Protected API Endpoints

GET /api/tasks
- Headers: Authorization: Bearer {token}
- Response: [{id, title, completed, userId}]

POST /api/tasks
- Headers: Authorization: Bearer {token}
- Request: {title: string, completed: boolean}
- Response: {id, title, completed, userId}

## Phase 2: Implementation Approach

### Frontend Implementation

1. Install Better Auth with JWT plugin
2. Configure authentication in lib/auth.ts
3. Create signup page at app/signup/page.tsx
4. Create signin page at app/signin/page.tsx
5. Implement getSession in lib/api.ts to retrieve token
6. Attach token to Authorization header for API calls
7. Handle 401 errors by redirecting to signin page

### Backend Implementation

1. Update JWT middleware in dependencies.py
2. Use python-jose to decode and verify tokens
3. Extract user_id from token
4. Ensure all protected endpoints validate JWT tokens
5. Return 401 responses for invalid tokens

## Phase 3: Testing Strategy

### Unit Tests

- JWT token validation functionality
- Authentication middleware
- API endpoint access controls

### Integration Tests

- End-to-end authentication flow
- Token refresh mechanisms
- Error handling for invalid tokens

## Phase 4: Deployment Considerations

- Environment variables for BETTER_AUTH_SECRET
- Secure storage of secrets
- HTTPS enforcement for authentication endpoints