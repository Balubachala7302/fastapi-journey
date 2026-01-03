🚀 FastAPI Journey
This repository documents my FastAPI learning journey following the 80/20 principle — focusing on the most practical concepts needed for backend development and interviews.

📌 Tech Stack

Python 3.11

FastAPI

Pydantic

Uvicorn

JWT (python-jose)

Passlib (bcrypt)

OAuth2 (Password Flow)

📂 Project Structure
Fastapi-Journey/
│
├── main.py          # FastAPI application
├── .gitignore
├── venv/            # Virtual environment (ignored)
└── README.md

🟢 Day 1 – FastAPI Basics

Concepts Covered

Creating FastAPI app

Basic GET endpoints

Path parameters

Simple JSON responses

Swagger UI (/docs)

Endpoints

/ – Root endpoint

/health – Health check

/hello/{name} – Path parameter example

/square/{number} – Simple logic API

🟡 Day 2 – Project Setup & Git

Concepts Covered

Virtual environment

.gitignore

Git init, add, commit

Pushing project to GitHub

GitHub authentication (browser-based)

🟠 Day 3 – Pydantic & Dependencies

Concepts Covered

Request body with Pydantic models

POST requests

Dependency Injection (Depends)

Header-based dependencies

Shared logic using dependencies

Endpoints

/users – Create user (Pydantic model)

/login – Basic login

/profile – Protected via dependency

/info – Header-based dependency

🔵 Day 4 – Authorization & Headers

Concepts Covered

Custom headers

Header validation

Raising HTTPException

Authorization using headers

Clean dependency-based security logic

🔴 Day 5 – JWT Authentication (Major Milestone)

Concepts Covered

Password hashing using bcrypt

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

JWT access token is returned

Token is sent as:

Authorization: Bearer <token>


Protected routes verify token

▶️ How to Run the Project
# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn 
python-jose passlib[bcrypt] 
python-multipart

# Run server
uvicorn main:app --reload


Open:

Swagger UI → http://127.0.0.1:8000/docs

OpenAPI JSON → http://127.0.0.1:8000/openapi.json

🎯 Why This Repo Matters

Covers real interview-level FastAPI

Clean incremental learning

Authentication + authorization included

Strong backend foundation

🧠 Next Planned Topics

Role-based access (RBAC)

Refresh tokens

Database integration (SQLAlchemy)

Async DB sessions

Production-ready folder structure

Environment variables

Docker + deployment
