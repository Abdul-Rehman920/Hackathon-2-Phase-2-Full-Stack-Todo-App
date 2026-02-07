# Research: Better Auth Integration and Secure API Calls

## Decision: JWT Claims Structure
**Rationale**: Using standard JWT claims with additional user-specific information for identification and authorization.
**Alternatives considered**: 
- Custom claims only
- Standard claims with minimal user data
- Full user object in token

**Chosen approach**: Standard claims (iss, sub, aud, exp, nbf, iat, jti) with user_id as a custom claim for identification.

## Decision: Token Expiration Policy
**Rationale**: Short-lived access tokens (15 minutes) with refresh tokens (7 days) provide security balance.
**Alternatives considered**:
- Long-lived tokens (hours/days)
- Session-based tokens without expiration
- Server-side token validation on each request

**Chosen approach**: 15-minute access tokens to minimize exposure window while using refresh tokens for user experience.

## Decision: Frontend Framework Approach
**Rationale**: Next.js 13+ with App Router provides the best developer experience and performance.
**Alternatives considered**:
- Next.js Pages Router
- React with other routing solutions
- Other frameworks (Vue, Angular)

**Chosen approach**: Next.js 14 with App Router using the new app directory structure.

## Research: Better Auth JWT Implementation
**Findings**: Better Auth provides built-in JWT support with customization options for token structure and signing.
- Better Auth can generate JWTs with custom claims
- Supports both access and refresh tokens
- Provides client-side utilities for token management
- Integrates well with Next.js App Router

## Research: python-jose for Token Validation
**Findings**: python-jose is a robust library for JWT operations in Python, supporting various signing algorithms.
- Supports RS256, HS256, and other common algorithms
- Provides token decoding and validation functions
- Compatible with FastAPI and other Python web frameworks
- Properly handles token expiration and signature verification

## Research: Best Practices for Attaching JWT Tokens to API Requests
**Findings**: Attaching JWT tokens in the Authorization header as a Bearer token is the standard approach.
- Standard format: "Authorization: Bearer <token>"
- Secure transmission over HTTPS
- Server-side validation required for each protected endpoint
- Client-side storage in memory or secure cookies (not localStorage for sensitive apps)

## Research: Frontend Error Handling for 401 Responses
**Findings**: Proper error handling includes both automatic redirection and user feedback.
- Interceptors can catch 401 responses globally
- Automatic redirection to signin page when authentication fails
- Clear user messaging about session expiration
- Preserving user context before redirection when possible