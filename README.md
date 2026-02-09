# 🚀 FastAPI Journey (Day 1 – Day 21)

This repository documents my **hands-on FastAPI learning journey**, where I progressively built a **production-ready backend application** with authentication, authorization, database integration, JWT security, refresh tokens, token revocation, migrations, and best practices.

By **Day 21**, the project evolved from basics to **real-world backend architecture**.

---

## 🛠 Tech Stack

- Python 3.11  
- FastAPI  
- Uvicorn  
- SQLAlchemy  
- Alembic (migrations)  
- SQLite  
- Pydantic v2  
- JWT (python-jose)  
- Passlib (bcrypt)  

---

## 📁 Project Structure
app/ ├── api/ │   ├── auth.py │   ├── users.py │   ├── deps.py │ ├── core/ │   ├── config.py │   ├── security.py │   ├── logger.py │   ├── exceptions.py │   ├── response.py │ ├── db/ │   ├── crud.py │   ├── database.py │   ├── models.py │   ├── schemas.py │ ├── main.py │ alembic/ alembic.ini fastapi.db .env

---

## 📅 Day-wise Learning Breakdown

### ✅ Day 1 – FastAPI Basics
- What is FastAPI
- Project setup
- First FastAPI app
- Running server with `uvicorn`
- Root endpoint (`/`)

---

### ✅ Day 2 – Routing & HTTP Methods
- GET, POST endpoints
- Path & query parameters
- Request–response flow

---

### ✅ Day 3 – Pydantic Schemas
- Request body validation
- Response models
- `BaseModel` usage

---

### ✅ Day 4 – Database Basics
- SQLite introduction
- SQLAlchemy setup
- Engine & session creation

---

### ✅ Day 5 – Models & Tables
- SQLAlchemy ORM models
- Table creation
- Relationships basics

---

### ✅ Day 6 – CRUD Operations
- Create & read users
- Session handling
- `crud.py` structure

---

### ✅ Day 7 – Password Security
- Password hashing using `passlib`
- Hash vs verify
- Secure password storage

---

### ✅ Day 8 – User Registration
- `/register` endpoint
- Email uniqueness validation
- Database persistence

---

### ✅ Day 9 – Authentication Basics
- OAuth2PasswordBearer
- Swagger auth flow
- Handling 401 / 403 errors

---

### ✅ Day 10 – Login Endpoint
- `/login` endpoint
- Email & password verification
- JWT access token generation

---

### ✅ Day 11 – JWT Tokens
- JWT structure
- `sub` claim usage
- Token expiration handling

---

### ✅ Day 12 – Authorization
- Protecting routes
- `Depends(get_current_user)`
- Request lifecycle understanding

---

### ✅ Day 13 – Refresh Tokens
- Refresh token concept
- `/refresh` endpoint
- Issuing new access tokens

---

### ✅ Day 14 – Debugging & Fixes
- Schema mismatches
- CRUD signature fixes
- Reading stack traces properly

---

### ✅ Day 15 – Authentication Integration 🎯
- `get_current_user` dependency
- Protected `/me` endpoint
- End-to-end JWT authentication
- Swagger authorization fully working

---

### ✅ Day 16 – Code Refactor & Stability
- Fixed import issues
- Improved project structure
- Removed circular dependencies
- Cleaned authentication flow

---

### ✅ Day 17 – Validation & Model Improvements
- Pydantic field fixes
- SQLAlchemy model alignment
- Cleaner request/response handling

---

### ✅ Day 18 – Database Polish
- Boolean & column fixes
- CRUD optimization
- Better query structure

---

### ✅ Day 19 – Token Blacklisting
- Token revocation concept
- Refresh token invalidation
- Blacklist checks during refresh

---

### ✅ Day 20 – Alembic & Token Revocation System
- Alembic migrations setup
- Database-driven token blacklist
- Refresh token verification with DB
- Production-level JWT security flow

---

### ✅ Day 21 – Production Polish & Best Practices 🚀
- Centralized exception handling
- Consistent API response schema
- Application logging (no `print`)
- Environment-based configuration
- Health check endpoint
- Clean Swagger metadata

---

## 🔐 Authentication Flow

1. Register User

POST /users/register


2. Login

POST /auth/login → returns access_token + refresh_token


3. Authorize in Swagger

Authorization: Bearer <access_token>


4. Access Protected Route

GET /auth/me


5. Refresh Token

POST /auth/refresh


6. Logout / Revoke Token

Token added to blacklist

---

## 🧪 Run the Project

```bash
# Activate virtual environment
venv\Scripts\activate

# Start server
uvicorn app.main:app --reload

Swagger UI:
https://127.0.0.1:8000/docs

Key Learnings
Real-world authentication & authorization
JWT + refresh token security
Token revocation strategy
Database migrations with Alembic
Debugging FastAPI like a backend developer
Clean, scalable backend architecture
Production-ready FastAPI practices