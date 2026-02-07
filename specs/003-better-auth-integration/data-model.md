# Data Model: Better Auth Integration and Secure API Calls

## User Entity

**Description**: Represents a registered user in the system

**Fields**:
- id (string/UUID): Unique identifier for the user
- email (string): User's email address (unique, required)
- password_hash (string): Hashed password (required)
- created_at (timestamp): Account creation timestamp
- updated_at (timestamp): Last update timestamp
- is_active (boolean): Whether the account is active

**Validation Rules**:
- Email must be a valid email format
- Email must be unique
- Password must meet security requirements (length, complexity)
- created_at and updated_at are automatically managed

**Relationships**:
- One-to-many with Session entities
- One-to-many with application-specific entities (e.g., tasks, posts)

## Session Entity

**Description**: Represents an active user session with JWT token information

**Fields**:
- session_id (string/UUID): Unique session identifier
- user_id (string/UUID): Reference to the user (foreign key)
- token_type (string): Type of token (access, refresh)
- token_hash (string): Hash of the JWT token (for server-side validation)
- expires_at (timestamp): Token expiration time
- created_at (timestamp): Session creation timestamp
- last_used_at (timestamp): Last time the session was used

**Validation Rules**:
- user_id must reference a valid user
- expires_at must be in the future
- token_type must be one of allowed values (access, refresh)

**Relationships**:
- Many-to-one with User entity
- Each user can have multiple active sessions

## JWT Token Structure

**Standard Claims**:
- iss (issuer): The application issuing the token
- sub (subject): The user ID
- aud (audience): The intended audience (application)
- exp (expiration): Token expiration time
- nbf (not before): Time before which token is not valid
- iat (issued at): Time token was issued
- jti (JWT ID): Unique identifier for the token

**Custom Claims**:
- user_id (string): The user's unique identifier
- user_email (string): The user's email address (for convenience)