# User Authentication API

A FastAPI-based REST API for user authentication and profile management.

## Tech Stack

- **Backend Framework**: FastAPI
- **Database**: Aiven PostgreSQL (Cloud-hosted)
- **ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens)
- **Password Hashing**: Bcrypt

## Prerequisites

- Python 3.7+
- pip (Python package manager)
- Aiven PostgreSQL instance (already set up)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Database Configuration:
- The project is configured to use Aiven PostgreSQL
- The connection string is already set up in `database.py`
- No additional database setup is required

## Running the Project

1. Start the FastAPI server:
```bash
uvicorn main:app --reload
```

2. Access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Authentication

1. **Register User**
   - Endpoint: `POST /register`
   - Body: `{ "user": "string", "email": "string", "password": "string" }`
   - Response: User ID and success message

2. **Login**
   - Endpoint: `POST /login`
   - Body: `{ "email": "string", "password": "string" }`
   - Response: JWT access token

### User Profile

1. **Get Profile**
   - Endpoint: `GET /profile/{ID}`
   - Headers: `Authorization: Bearer <token>`
   - Response: User profile details

2. **Update Profile**
   - Endpoint: `PUT /profile/{ID}`
   - Headers: `Authorization: Bearer <token>`
   - Body: `{ "user": "string", "email": "string", "password": "string" }`
   - Response: Updated user profile

## Project Structure

```
├── main.py          # FastAPI application and routes
├── database.py      # Database configuration
├── models.py        # SQLAlchemy models
├── schema.py        # Pydantic schemas
└── auth.py          # Authentication utilities
```

## How It Works

The application implements a secure user authentication system with the following features:

1. **Database Connection**:
   - Uses SQLAlchemy ORM to interact with PostgreSQL
   - Implements connection pooling and session management
   - Handles database migrations and schema creation

2. **Authentication Flow**:
   - User registration with password hashing
   - JWT-based authentication for secure login
   - Protected routes using token validation

3. **API Endpoints**:
   - Register: Creates new user accounts with email validation
   - Login: Authenticates users and issues JWT tokens
   - Profile Management: Secure CRUD operations for user profiles

## Challenges Faced

1. **Security Implementation**:
   - Implementing secure password hashing
   - Managing JWT token lifecycle
   - Protecting sensitive routes

2. **Database Management**:
   - Setting up proper database connections
   - Implementing efficient query patterns
   - Handling concurrent requests

3. **Error Handling**:
   - Implementing proper validation
   - Managing database constraints
   - Providing meaningful error messages

## Future Improvements

1. Add email verification
2. Implement password reset functionality
3. Add rate limiting
4. Implement refresh tokens
5. Add more comprehensive logging 