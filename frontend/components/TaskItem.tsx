'use client';

import { Task } from '@/lib/types';
import { useState } from 'react';

interface TaskItemProps {
  task: Task;
  onEdit: (task: Task) => void;
  onDelete: (id: string) => void;
  onToggle: (id: string) => void;
}

export default function TaskItem({ task, onEdit, onDelete, onToggle }: TaskItemProps) {
  const isCompleted = task.status === 'completed';

  return (
    <div className={`
      bg-white rounded-xl shadow-md p-6 mb-4 transition-all duration-300 hover:shadow-xl hover:-translate-y-1
      border border-gray-100 ${isCompleted ? 'opacity-70' : ''}
    `}>
      <div className="flex items-start justify-between">
        <div className="flex items-center gap-4">
          <input
            type="checkbox"
            checked={isCompleted}
            onChange={() => onToggle(task.id)}
            className="w-5 h-5 accent-blue-600 cursor-pointer"
          />
          <div>
            <h3 className={`font-semibold text-lg ${isCompleted ? 'line-through text-gray-500' : 'text-gray-800'}`}>
              {task.title}
            </h3>
            {task.description && (
              <p className="text-gray-600 mt-1 text-sm">{task.description}</p>
            )}
            <p className="text-xs text-gray-500 mt-2">
              Created: {new Date(task.createdAt).toLocaleDateString()}
            </p>
          </div>
        </div>

        <div className="flex gap-2">
          <button
            onClick={() => onEdit(task)}
            className="text-blue-600 hover:text-blue-800 font-medium"
          >
            Edit
          </button>
          <button
            onClick={() => onDelete(task.id)}
            className="text-red-600 hover:text-red-800 font-medium"
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  );
}