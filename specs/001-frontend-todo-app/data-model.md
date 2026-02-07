# Data Model: Frontend-Only Todo Web Application

## Overview
This document defines the data structures and relationships for the frontend-only todo web application. Since this is a mock implementation, the data model represents the structure of objects that will be stored in-memory and manipulated by the frontend.

## Entity: Task

### Fields
- **id**: string (required, unique identifier)
  - Generated using a UUID or timestamp-based approach
  - Used to uniquely identify each task
  
- **title**: string (required)
  - The main text of the task
  - Minimum length: 1 character
  - Maximum length: 255 characters
  
- **description**: string (optional)
  - Additional details about the task
  - Can be empty or null
  - Maximum length: 1000 characters
  
- **status**: string (required)
  - Possible values: "pending", "completed"
  - Determines the visual representation and behavior of the task
  
- **createdAt**: Date (required)
  - Timestamp when the task was created
  - Stored as ISO string format or Date object
  - Used for sorting and display purposes

### Relationships
- No relationships with other entities in this simplified model

### Validation Rules
- title must not be empty
- status must be one of the allowed values ("pending", "completed")
- createdAt must be a valid date

### State Transitions
- Status can transition from "pending" to "completed" when user marks task as complete
- Status can transition from "completed" to "pending" when user unmarks task as complete

## Entity: TaskFormData

### Fields
- **title**: string (required)
  - User input for task title
  - Will be validated before creating/updating a Task entity
  
- **description**: string (optional)
  - User input for task description
  - Optional field that can be empty

### Purpose
- Used for form validation and data transfer between UI and task creation/updating functions
- Contains the raw input from user forms before validation and transformation into Task entities

## Mock Data Structure

### Task Collection
- Array of Task entities stored in-memory
- Maintained in lib/mockData.ts
- Operations (CRUD) performed directly on this array
- Simulated with artificial delays to mimic real API calls