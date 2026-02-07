<!--
SYNC IMPACT REPORT
Version change: N/A → 1.0.0
Added sections: All principles and sections as per project requirements
Removed sections: None (new constitution)
Modified principles: None (new constitution)
Templates requiring updates:
  - ✅ .specify/templates/plan-template.md - No changes needed
  - ✅ .specify/templates/spec-template.md - No changes needed
  - ✅ .specify/templates/tasks-template.md - No changes needed
  - ✅ .qwen/commands/*.toml - No changes needed
Follow-up TODOs: None
-->

# Hackathon Todo Phase 2 - Full-Stack Web App Constitution

## Core Principles

### Agentic Development First
Every feature and implementation starts with agent specification and planning; All code must be generated through Claude Code agents using specs; No manual coding allowed - complete implementation via agentic workflow

### Security-First Architecture
Authentication required for all endpoints using Better Auth with JWT tokens; User data isolation mandatory - each user sees only their own tasks; JWT verification and user_id filtering enforced at backend level

### Test-Driven Development (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced; All features must have comprehensive test coverage before implementation

### Full-Stack Integration Testing
Focus areas requiring integration tests: API endpoint authentication, User data isolation, Cross-service communication, Database persistence, Frontend-backend interaction

### Modern Technology Stack Compliance
Frontend: Next.js 16+ with TypeScript and Tailwind CSS; Backend: Python FastAPI with SQLModel; Database: Neon Serverless PostgreSQL; Authentication: Better Auth with JWT plugin

### REST API Standards
All API endpoints under /api/ with user_id in path; JWT tokens in Authorization: Bearer header; Shared BETTER_AUTH_SECRET between frontend and backend

## Additional Constraints and Requirements
Multi-user support with persistent storage; Responsive web application design; 5 basic Todo features: Add, View, Update, Delete, Mark Complete; Complete user data isolation; Phase II of hackathon project evolving from console app

## Development Workflow
Use Claude Projects with 6 specialized agents; Spec-Kit Plus for specification management; All implementation via agent specifications; Next.js App Router pattern; SQLModel for database modeling

## Governance
All PRs/reviews must verify agentic development compliance; All code changes must follow specification-driven approach; Architecture decisions require ADR documentation; Manual code changes are prohibited

**Version**: 1.0.0 | **Ratified**: 2026-01-08 | **Last Amended**: 2026-01-08
