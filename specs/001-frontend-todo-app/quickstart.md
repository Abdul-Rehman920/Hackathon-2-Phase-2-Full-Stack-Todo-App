# Quickstart Guide: Frontend-Only Todo Web Application

## Overview
This guide provides instructions for setting up, running, and understanding the frontend-only todo web application built with Next.js, TypeScript, and Tailwind CSS.

## Prerequisites
- Node.js version 18.0 or higher
- npm or yarn package manager
- A modern web browser (Chrome, Firefox, Safari, Edge)

## Setup Instructions

### 1. Clone or Create the Project
```bash
# Navigate to your project directory
cd your-project-directory

# If starting fresh, initialize the Next.js project
npx create-next-app@latest frontend --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
```

### 2. Install Dependencies
```bash
cd frontend
npm install
```

### 3. Project Structure
After setup, your project structure should look like:
```
frontend/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   └── login/
│       └── page.tsx
├── components/
│   ├── TaskList.tsx
│   ├── TaskItem.tsx
│   ├── TaskForm.tsx
│   ├── Header.tsx
│   └── ui/
│       ├── Button.tsx
│       ├── Input.tsx
│       ├── Checkbox.tsx
│       └── Modal.tsx
├── lib/
│   ├── mockData.ts
│   └── api.ts
├── public/
├── styles/
│   └── globals.css
├── .gitignore
├── next.config.mjs
├── package.json
├── postcss.config.mjs
├── tailwind.config.ts
└── tsconfig.json
```

## Running the Application

### Development Mode
```bash
npm run dev
```
The application will be available at http://localhost:3000

### Production Build
```bash
npm run build
npm run start
```

## Key Features

### 1. Task Management
- **View Tasks**: See all tasks with title, description, status, and creation date
- **Add Task**: Use the form to create new tasks (title required, description optional)
- **Edit Task**: Modify existing task details
- **Delete Task**: Remove tasks with confirmation dialog
- **Toggle Completion**: Mark tasks as complete/incomplete

### 2. Responsive Design
- Mobile-first approach with responsive breakpoints
- Optimized for both mobile and desktop experiences
- Touch-friendly controls for mobile users

### 3. Mock Data System
- All data stored in-memory using React state
- Simulated API delays to mimic real backend behavior
- No external dependencies required

## Understanding the Code

### Core Components
- `app/page.tsx`: Main dashboard page with task list and add form
- `components/TaskList.tsx`: Displays all tasks with status indicators
- `components/TaskItem.tsx`: Individual task display with action buttons
- `components/TaskForm.tsx`: Reusable form for adding and editing tasks
- `lib/api.ts`: Mock API functions that simulate backend calls
- `lib/mockData.ts`: Contains the in-memory data store

### State Management
- Local state managed with React hooks (useState, useEffect)
- Client components handle all interactive elements
- Mock API layer abstracts data operations

## Development Workflow

### Adding New Features
1. Create new components in the `components/` directory
2. Add UI components to the `components/ui/` directory
3. Update mock data functions in `lib/api.ts` if needed
4. Follow the existing patterns for state management and component composition

### Testing Locally
1. Run `npm run dev` to start the development server
2. Navigate to the appropriate page
3. Test all user interactions and verify functionality
4. Check responsive behavior on different screen sizes

## Troubleshooting

### Common Issues
- **Page doesn't load**: Ensure all dependencies are installed with `npm install`
- **TypeScript errors**: Run `npm run type-check` to identify issues
- **Tailwind styles not working**: Verify `globals.css` imports Tailwind directives

### Performance Tips
- Use React.memo for components that render frequently with same props
- Implement proper key props for list items
- Minimize re-renders by lifting state appropriately