import React from 'react'

const LoginPage = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="max-w-md w-full space-y-8 p-8 bg-white rounded-lg shadow">
        <div className="text-center">
          <h2 className="mt-6 text-3xl font-extrabold text-gray-900">
            Coming Soon
          </h2>
          <p className="mt-2 text-sm text-gray-600">
            The login functionality will be available in the next phase
          </p>
        </div>
        <div className="mt-8">
          <p className="text-center text-gray-500">
            For now, you can explore the demo application
          </p>
          <div className="mt-6 text-center">
            <a 
              href="/"
              className="font-medium text-blue-600 hover:text-blue-500"
            >
              Go back to the app
            </a>
          </div>
        </div>
      </div>
    </div>
  )
}

export default LoginPage