'use client';

import { useState } from 'react';
import TaskList from '@/components/TaskList';
import TaskForm from '@/components/TaskForm';
import { createTask } from '@/lib/api';

export default function Home() {
  const [taskUpdateTrigger, setTaskUpdateTrigger] = useState(0);
  const [showForm, setShowForm] = useState(false);

  const handleAddTask = async (taskData: { title: string; description?: string }) => {
    try {
      await createTask(taskData);
      setTaskUpdateTrigger(prev => prev + 1);
      setShowForm(false);
    } catch (error: any) {
      console.error('Failed to add task:', error);
      alert('Failed to add task: ' + error.message);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Simple Header */}
      <header className="bg-white border-b border-gray-200">
        <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
              <svg className="w-5 h-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              </svg>
            </div>
            <h1 className="text-xl font-semibold text-gray-900">TaskApp</h1>
          </div>
          
          <button
            onClick={() => setShowForm(true)}
            className="px-4 py-2 bg-blue-600 text-white text-sm font-medium rounded-lg hover:bg-blue-700 transition-colors"
          >
            + New Task
          </button>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-6xl mx-auto px-4 py-8">
        {showForm && (
          <TaskForm 
            onSubmit={handleAddTask}
            onCancel={() => setShowForm(false)}
          />
        )}
        
        <TaskList 
          key={taskUpdateTrigger} 
          onTaskUpdate={() => setTaskUpdateTrigger(prev => prev + 1)} 
        />
      </main>
    </div>
  );
}