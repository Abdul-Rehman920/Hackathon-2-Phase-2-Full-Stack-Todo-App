# API Contract: Frontend-Only Todo Web Application

## Overview
This document defines the API contract for the mock API layer in the frontend-only todo web application. Since this is a frontend-only implementation with mock data, these endpoints represent the interface that would exist if there were a real backend service.

## Base URL
For the mock implementation, all API calls are handled internally within the frontend application using mock functions.

## Common Headers
- Content-Type: application/json
- Authorization: Bearer {token} (Not required for mock implementation)

## Common Response Format
All API responses follow this structure:
```json
{
  "data": { ... }, // Actual response data
  "success": true, // Boolean indicating success
  "message": "..." // Optional message providing additional context
}
```

## Error Response Format
When an API call fails, the response follows this structure:
```json
{
  "error": {
    "code": "...", // Error code
    "message": "..." // Human-readable error message
  },
  "success": false
}
```

## Endpoints

### GET /api/tasks
Retrieve all tasks for the current user.

#### Request
- Method: GET
- URL: /api/tasks
- Headers: Authorization: Bearer {token} (Not required for mock)
- Query Parameters:
  - status (optional): Filter by status ("pending", "completed", or "all")
  - limit (optional): Limit number of results returned
  - offset (optional): Offset for pagination

#### Response
- Status: 200 OK
- Body:
```json
{
  "data": [
    {
      "id": "string",
      "title": "string",
      "description": "string",
      "status": "pending|completed",
      "createdAt": "ISODateString"
    }
  ],
  "success": true
}
```

### POST /api/tasks
Create a new task.

#### Request
- Method: POST
- URL: /api/tasks
- Headers: Authorization: Bearer {token} (Not required for mock)
- Body:
```json
{
  "title": "string", // Required
  "description": "string" // Optional
}
```

#### Response
- Status: 201 Created
- Body:
```json
{
  "data": {
    "id": "string",
    "title": "string",
    "description": "string",
    "status": "pending",
    "createdAt": "ISODateString"
  },
  "success": true
}
```

### PUT /api/tasks/{id}
Update an existing task.

#### Request
- Method: PUT
- URL: /api/tasks/{id}
- Headers: Authorization: Bearer {token} (Not required for mock)
- Body:
```json
{
  "title": "string", // Required
  "description": "string" // Optional
}
```

#### Response
- Status: 200 OK
- Body:
```json
{
  "data": {
    "id": "string",
    "title": "string",
    "description": "string",
    "status": "pending|completed",
    "createdAt": "ISODateString"
  },
  "success": true
}
```

### PATCH /api/tasks/{id}/status
Toggle the completion status of a task.

#### Request
- Method: PATCH
- URL: /api/tasks/{id}/status
- Headers: Authorization: Bearer {token} (Not required for mock)
- Body: (empty)

#### Response
- Status: 200 OK
- Body:
```json
{
  "data": {
    "id": "string",
    "title": "string",
    "description": "string",
    "status": "pending|completed",
    "createdAt": "ISODateString"
  },
  "success": true
}
```

### DELETE /api/tasks/{id}
Delete a task.

#### Request
- Method: DELETE
- URL: /api/tasks/{id}
- Headers: Authorization: Bearer {token} (Not required for mock)

#### Response
- Status: 200 OK
- Body:
```json
{
  "data": {
    "id": "string"
  },
  "success": true
}
```