'use client';

import { useEffect, useState } from 'react';
import { getTasks, deleteTask, toggleComplete } from '@/lib/api';
import { Task } from '@/lib/types';

interface TaskListProps {
  onTaskUpdate: () => void;
}

export default function TaskList({ onTaskUpdate }: TaskListProps) {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchTasks = async () => {
      try {
        setLoading(true);
        setError(null);
        const data = await getTasks();
        setTasks(data);
      } catch (err: any) {
        console.error('Error fetching tasks:', err);
        setError(err.message || 'Failed to load tasks');
      } finally {
        setLoading(false);
      }
    };

    fetchTasks();
  }, [onTaskUpdate]);

  const handleToggle = async (id: number) => {
    try {
      await toggleComplete(id);
      onTaskUpdate();
    } catch (err: any) {
      alert('Failed to update task: ' + err.message);
    }
  };

  const handleDelete = async (id: number) => {
    if (!confirm('Delete this task?')) return;

    try {
      await deleteTask(id);
      onTaskUpdate();
    } catch (err: any) {
      alert('Failed to delete task: ' + err.message);
    }
  };

  if (loading) {
    return (
      <div className="text-center py-12">
        <div className="inline-block w-8 h-8 border-4 border-gray-200 border-t-blue-600 rounded-full animate-spin"></div>
        <p className="text-gray-500 mt-4">Loading tasks...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-50 border border-red-200 rounded-lg p-4">
        <p className="text-red-800">{error}</p>
      </div>
    );
  }

  if (tasks.length === 0) {
    return (
      <div className="text-center py-12">
        <svg className="w-16 h-16 text-gray-300 mx-auto mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
        </svg>
        <p className="text-gray-500 text-lg">No tasks yet</p>
        <p className="text-gray-400 text-sm mt-2">Click "New Task" to get started</p>
      </div>
    );
  }

  return (
    <div className="space-y-3">
      {tasks.map((task) => (
        <div
          key={task.id}
          className="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-sm transition-shadow"
        >
          <div className="flex items-start gap-3">
            <input
              type="checkbox"
              checked={task.completed}
              onChange={() => handleToggle(task.id)}
              className="mt-1 w-5 h-5 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
            />
            
            <div className="flex-1 min-w-0">
              <h3
                className={`font-medium ${
                  task.completed
                    ? 'line-through text-gray-400'
                    : 'text-gray-900'
                }`}
              >
                {task.title}
              </h3>
              
              {task.description && (
                <p className={`text-sm mt-1 ${
                  task.completed ? 'text-gray-400' : 'text-gray-600'
                }`}>
                  {task.description}
                </p>
              )}
              
              <p className="text-xs text-gray-400 mt-2">
                {new Date(task.created_at).toLocaleDateString()}
              </p>
            </div>

            <button
              onClick={() => handleDelete(task.id)}
              className="text-gray-400 hover:text-red-600 transition-colors"
            >
              <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
            </button>
          </div>
        </div>
      ))}
    </div>
  );
}