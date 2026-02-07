# Quickstart Guide: Better Auth Integration

## Setting Up Authentication

### Prerequisites
- Node.js 18+ installed
- Next.js 14+ project with App Router
- FastAPI backend
- Environment variables configured

### Environment Variables
```bash
# Backend
BETTER_AUTH_SECRET=your-super-secret-key-here
DATABASE_URL=your-database-url

# Frontend (if needed)
NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:8000
```

### Backend Setup (FastAPI + python-jose)

1. Install required packages:
```bash
pip install python-jose[cryptography] python-dotenv
```

2. Update dependencies.py to include JWT verification:
```python
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from typing import Dict
import os

security = HTTPBearer()

def verify_token(token: str) -> Dict:
    """
    Verify JWT token and return payload
    """
    secret = os.getenv("BETTER_AUTH_SECRET")
    if not secret:
        raise HTTPException(status_code=500, detail="Missing BETTER_AUTH_SECRET")
    
    try:
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Dependency to get current user from JWT token
    """
    token = credentials.credentials
    payload = verify_token(token)
    user_id = payload.get("user_id")
    
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return {"user_id": user_id}
```

### Frontend Setup (Next.js with Better Auth)

1. Install Better Auth:
```bash
npm install better-auth
```

2. Configure Better Auth in lib/auth.ts:
```typescript
import { betterAuth } from "better-auth";
import { jwt } from "better-auth/plugins";

export const auth = betterAuth({
  plugins: [
    jwt({
      secret: process.env.BETTER_AUTH_SECRET || "your-default-secret",
    }),
  ],
  // other config...
});
```

3. Create signup page at app/signup/page.tsx:
```tsx
"use client";
import { useState } from "react";
import { auth } from "@/lib/auth";

export default function SignUpPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch("/api/auth/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });
      
      if (response.ok) {
        // Redirect to signin or dashboard
        window.location.href = "/signin";
      } else {
        const data = await response.json();
        setError(data.message);
      }
    } catch (err) {
      setError("An error occurred during signup");
    }
  };

  return (
    <div className="container">
      <h1>Sign Up</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Sign Up</button>
      </form>
      {error && <p>{error}</p>}
    </div>
  );
}
```

4. Create signin page at app/signin/page.tsx:
```tsx
"use client";
import { useState } from "react";

export default function SignInPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch("/api/auth/signin", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });
      
      if (response.ok) {
        const data = await response.json();
        
        // Store token in memory or secure cookie
        localStorage.setItem("authToken", data.token);
        
        // Redirect to dashboard
        window.location.href = "/dashboard";
      } else {
        const data = await response.json();
        setError(data.message);
      }
    } catch (err) {
      setError("An error occurred during sign in");
    }
  };

  return (
    <div className="container">
      <h1>Sign In</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Sign In</button>
      </form>
      {error && <p>{error}</p>}
    </div>
  );
}
```

5. Update lib/api.ts to include JWT token in requests:
```typescript
// Function to get JWT token from session
export async function getAuthToken(): Promise<string | null> {
  // This would typically use Better Auth's getSession function
  // For now, we'll use localStorage as an example
  return localStorage.getItem("authToken");
}

// Function to make authenticated API requests
export async function authenticatedRequest<T>(
  url: string,
  options: RequestInit = {}
): Promise<T> {
  const token = await getAuthToken();
  
  const headers = {
    ...options.headers,
    ...(token ? { "Authorization": `Bearer ${token}` } : {}),
    "Content-Type": "application/json",
  };
  
  const response = await fetch(url, {
    ...options,
    headers,
  });
  
  if (response.status === 401) {
    // Handle 401 error by redirecting to signin
    window.location.href = "/signin";
    throw new Error("Authentication required");
  }
  
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  
  return response.json();
}
```

### Testing the Integration

1. Start your backend server
2. Navigate to the signup page and create an account
3. Sign in with your credentials
4. Access protected API endpoints - they should now accept your JWT token
5. Test the 401 handling by removing the token and trying to access protected endpoints