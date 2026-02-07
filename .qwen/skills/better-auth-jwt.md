# Skill: Better Auth with JWT Configuration

To enable JWT in Better Auth (Next.js):

- Install the JWT plugin if needed
- In your Better Auth config (usually in lib/auth.ts or similar):
  ```ts
  import { BetterAuth } from "better-auth"
  import { jwt } from "better-auth/plugins"

  export const auth = BetterAuth({
    plugins: [jwt()],
    jwt: {
      secret: process.env.BETTER_AUTH_SECRET!,
    },
    // other config...
  })