# Authentication Flow Documentation

## Overview
This document describes the authentication flow implemented in the fullstack todo app using Better Auth with JWT tokens.

## Components

### Frontend
- `lib/auth.ts`: Better Auth configuration with JWT plugin
- `lib/api.ts`: API request utilities with JWT token handling
- `app/signup/page.tsx`: User registration page
- `app/signin/page.tsx`: User sign-in page

### Backend
- `dependencies.py`: JWT verification middleware
- `models.py`: User and Session entities
- `main.py`: Authentication endpoints

## Authentication Flow

### User Registration
1. User navigates to `/signup`
2. User enters email and password
3. Form data is sent to `/api/auth/signup`
4. Backend creates a new user with hashed password
5. User is redirected to `/signin`

### User Sign-in
1. User navigates to `/signin`
2. User enters email and password
3. Form data is sent to `/api/auth/signin`
4. Backend validates credentials and creates JWT token
5. Token is stored in localStorage
6. User is redirected to dashboard

### Protected API Access
1. Frontend retrieves JWT token from localStorage
2. Token is attached to Authorization header: `Bearer {token}`
3. Request is sent to protected endpoint
4. Backend verifies JWT token and extracts user_id
5. Request is processed with user context

### Session Management
1. Token is stored in localStorage for persistence
2. Session validation checks token expiration
3. On token expiration, user is redirected to signin

### Session Expiration Handling
1. API requests return 401 for invalid/expired tokens
2. Frontend intercepts 401 responses
3. Token is cleared from localStorage
4. User receives feedback about session expiration
5. User is redirected to signin page

## Security Considerations
- JWT tokens have 15-minute expiration (as per research)
- Passwords are hashed using bcrypt
- All API requests require valid JWT tokens
- User data is isolated by user_id