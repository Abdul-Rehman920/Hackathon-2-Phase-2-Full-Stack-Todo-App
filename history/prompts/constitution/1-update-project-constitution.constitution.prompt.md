---
id: 1
title: "Update project constitution for Todo app"
stage: constitution
date_iso: "2026-01-08"
surface: agent
model: Qwen
feature: "none"
branch: "main"
user: user
command: "/sp.constitution Project Name: Hackathon Todo Phase 2 - Full-Stack Web App"
labels: ["constitution", "setup", "governance"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - ".specify/memory/constitution.md"
tests_yaml: []
---

# Prompt History Record

## Prompt Text

```
/sp.constitution Project Name: Hackathon Todo Phase 2 - Full-Stack Web App

Project Description:
A modern multi-user Todo web application built from scratch using agentic development workflow. This is Phase II of the hackathon project, evolving from a simple console app into a secure, persistent, full-stack system with authentication and user isolation.

Current Phase: phase2-web

Goal:
Implement all 5 basic Todo features (Add, View, Update, Delete, Mark Complete) as a responsive web application with:
- Multi-user support
- Persistent storage in Neon Serverless PostgreSQL
- Secure authentication using Better Auth with JWT tokens
- Complete user data isolation (each user sees and modifies only their own tasks)

Key Requirements:
- Use Next.js 16+ (App Router) with TypeScript and Tailwind CSS for frontend
- Use Python FastAPI with SQLModel for backend
- REST API endpoints under /api/ with user_id in path (as defined in documentation)
- JWT-based authentication: Shared BETTER_AUTH_SECRET between frontend and backend
- All API calls require valid JWT in Authorization: Bearer header
- Backend verifies JWT and enforces task ownership via user_id filtering
- No manual coding allowed — entire implementation via Claude Code agents using specs

Technology Stack:
- Frontend: Next.js 16+, TypeScript, Tailwind CSS, Better Auth (with JWT plugin)
- Backend: FastAPI, SQLModel
- Database: Neon Serverless PostgreSQL
- Auth: Better Auth + JWT (stateless, shared secret)
- Dev Tools: Claude Projects (with 6 specialized agents), Spec-Kit Plus
```

## Response Text

The project constitution has been successfully updated with the following details:

- **New Version**: 1.0.0 (initial version for this project)
- **Bump Rationale**: This is the initial constitution for the "Hackathon Todo Phase 2 - Full-Stack Web App" project
- **Files Updated**: Only the main constitution file at `.specify/memory/constitution.md`
- **No Manual Follow-up Required**: All dependent templates are compatible with the new constitution
- **Suggested Commit Message**: `docs: add initial constitution for Hackathon Todo Phase 2 project`

The constitution now reflects the specific requirements of your full-stack web application project, including principles for agentic development, security-first architecture, test-driven development, full-stack integration testing, modern technology stack compliance, and REST API standards.

## Outcome

Successfully created a project-specific constitution that aligns with the requirements of the Hackathon Todo Phase 2 project. The constitution establishes clear principles for agentic development, security, testing, and technology stack compliance that will guide the project implementation.

## Evaluation

The constitution template was properly filled with project-specific information, validated for correctness, and written to the appropriate location. All required elements were included as per the execution flow specified in the command.