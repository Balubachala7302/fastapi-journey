🚀 FastAPI Journey

This repository documents my FastAPI learning journey following the 80/20 principle — focusing on the most practical concepts required for backend development, real projects, and interviews.

📌 Tech Stack

Python 3.11

FastAPI

Pydantic

Uvicorn

JWT (python-jose)

Passlib (bcrypt)

OAuth2 (Password Flow)

📂 Project Structure (Day-8)
Fastapi-Journey/
│
├── app/
│   ├── main.py              # Application entry point
│   ├── core/
│   │   ├── config.py        # App configuration
│   │   └── security.py      # JWT & password security
│   ├── api/
│   │   ├── auth.py          # Authentication routes
│   │   ├── users.py         # User routes
│   │   └── admin.py         # Admin-only routes
│
├── .env                     # Environment variables
├── .gitignore
├── venv/                    # Virtual environment (ignored)
└── README.md

🟢 Day 1 – FastAPI Basics
Concepts Covered

Creating a FastAPI app

Basic GET endpoints

Path parameters

JSON responses

Swagger UI (/docs)

Endpoints

/ – Root endpoint

/health – Health check

/hello/{name} – Path parameter example

/square/{number} – Simple logic API

🟡 Day 2 – Project Setup & Git
Concepts Covered

Virtual environment setup

.gitignore

Git init, add, commit

Pushing project to GitHub

GitHub authentication (browser-based)

🟠 Day 3 – Pydantic & Dependencies
Concepts Covered

Request body with Pydantic models

POST requests

Dependency Injection using Depends

Header-based dependencies

Shared reusable logic

Endpoints

/users – Create user (Pydantic model)

/login – Basic login

/profile – Dependency-protected route

/info – Header-based dependency

🔵 Day 4 – Authorization & Headers
Concepts Covered

Custom request headers

Header validation

Raising HTTPException

Authorization using headers

Clean dependency-based security logic

🔴 Day 5 – JWT Authentication (Major Milestone)
Concepts Covered

Password hashing with bcrypt

JWT creation & verification

OAuth2 Password Flow

Token-based authentication

Protecting routes with JWT

Swagger UI authorization flow

Security Stack

OAuth2PasswordBearer

OAuth2PasswordRequestForm

python-jose

passlib[bcrypt]

Endpoints

/login – Generates JWT access token

/profile – JWT-protected endpoint

/info – JWT-protected endpoint

🔐 Authentication Flow (Day 5)

User logs in via /login

Server validates credentials

JWT access token is generated

Token is sent as:

Authorization: Bearer <token>


Protected routes validate the token

🟣 Day 6 – Authorization & Access Control
Concepts Covered

Authentication vs Authorization

Securing routes with dependencies

Handling 401 Unauthorized vs 403 Forbidden

Clean authorization checks

🟤 Day 7 – Role-Based Access Control (RBAC) & Refactor
Concepts Covered

Admin vs User roles

Role-based route protection

Reusable authorization dependencies

Refactoring project into modules

Separating config & security logic

Production-style folder structure

Key Features

Admin-only routes

JWT + role validation

Clean main.py

⚫ Day 8 – Clean Architecture & APIRouter
Concepts Covered

Modular routing using APIRouter

Feature-based route separation

Thin main.py

Clean API grouping

Interview-ready FastAPI architecture

Benefits

Scalable codebase

Easy maintenance

Real-world backend structure

▶️ How to Run the Project
# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn python-jose passlib[bcrypt] python-multipart

# Run the server
uvicorn app.main:app --reload

Open:

Swagger UI → http://127.0.0.1:8000/docs

OpenAPI JSON → http://127.0.0.1:8000/openapi.json

🎯 Why This Repository Matters

Covers interview-level FastAPI concepts

Incremental, structured learning

Authentication + Authorization included

Clean architecture & best practices

Strong backend foundation

🧠 Next Planned Topics

Refresh tokens

Database integration (SQLAlchemy / SQLModel)

Async DB sessions

Advanced dependency injection

Environment-based configuration

Docker & deployment

Production security best practices
