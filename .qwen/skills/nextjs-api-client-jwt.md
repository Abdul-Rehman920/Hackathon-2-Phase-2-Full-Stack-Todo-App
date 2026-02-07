# Skill: Next.js API Client with JWT Attachment

Create a reusable API client in frontend/lib/api.ts:

```ts
import { getSession } from "better-auth/client"

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api"

export const api = {
  async getTasks() {
    const session = await getSession()
    const token = session?.user?.token // or from cookie if stored there

    const res = await fetch(`${API_BASE}/tasks`, {
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    })
    if (!res.ok) throw new Error("Failed")
    return res.json()
  },
  // similar for post, put, delete...
}