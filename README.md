# 🚀 FastAPI Journey (Day 1 – Day 15)

This repository documents my **15-day hands-on FastAPI learning journey**, where I built a complete backend application with **authentication, authorization, database integration, and JWT security**.

By the end of Day 15, the project includes:
- User registration & login
- JWT authentication
- Protected routes
- Refresh tokens
- SQLite database with SQLAlchemy
- Clean project structure

---

## 🛠 Tech Stack

- **Python 3.11**
- **FastAPI**
- **Uvicorn**
- **SQLAlchemy**
- **SQLite**
- **Pydantic v2**
- **JWT (python-jose)**
- **Passlib (bcrypt)**

---

## 📁 Project Structure

app/
├── api/
│ ├── auth.py
│ ├── users.py
│
├── core/
│ ├── config.py
│ ├── security.py
│
├── db/
│ ├── crud.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│
├── main.py
fastapi.db


---

## 📅 Day-wise Learning Breakdown

---

### ✅ Day 1 – FastAPI Basics
- What is FastAPI
- Project setup
- First FastAPI app
- Running server with `uvicorn`
- `/` root endpoint

---

### ✅ Day 2 – Routing & HTTP Methods
- GET, POST endpoints
- Path & query parameters
- Request & response basics

---

### ✅ Day 3 – Pydantic Schemas
- Request body validation
- Response models
- Introduction to `BaseModel`

---

### ✅ Day 4 – Database Basics
- SQLite introduction
- SQLAlchemy setup
- Engine & session creation

---

### ✅ Day 5 – Models & Tables
- SQLAlchemy models
- Creating tables
- ORM fundamentals

---

### ✅ Day 6 – CRUD Operations
- Create user
- Read user
- Database session handling
- `crud.py` introduction

---

### ✅ Day 7 – Password Security
- Password hashing with `passlib`
- Hash vs verify password
- Never storing plain passwords

---

### ✅ Day 8 – User Registration
- `/register` endpoint
- Email uniqueness check
- Database persistence

---

### ✅ Day 9 – Authentication Basics
- OAuth2PasswordBearer
- Swagger authentication flow
- Common auth errors (401, 403)

> ⚠️ Faced many errors here – **completely normal**

---

### ✅ Day 10 – Login Endpoint
- `/login` endpoint
- Email + password validation
- Returning JWT access token

---

### ✅ Day 11 – JWT Tokens
- Creating JWT tokens
- `sub` claim usage
- Token expiration handling

---

### ✅ Day 12 – Authorization
- Protecting routes
- `Depends(get_current_user)`
- Understanding request lifecycle

---

### ✅ Day 13 – Refresh Tokens
- Refresh token concept
- `/refresh` endpoint
- Generating new access tokens

---

### ✅ Day 14 – Debugging & Fixes
- Fixed schema mismatches
- Fixed CRUD signature issues
- Learned to read stack traces properly

---

### ✅ Day 15 – Final Integration 🎯
- `get_current_user` dependency
- Protected `/me` endpoint
- Swagger authorization working
- End-to-end authentication flow complete

---

## 🔐 Authentication Flow

1. **Register User**

POST /users/register


2. **Login**


POST /auth/login
→ returns access_token


3. **Authorize in Swagger**


Authorization: Bearer <token>


4. **Access Protected Route**


GET /auth/me


---

## 🧪 Run the Project

```bash
# Activate virtual environment
venv\Scripts\activate

# Start server
uvicorn app.main:app --reload


Swagger UI:

http://127.0.0.1:8000/docs

📌 Key Learnings

How real backend authentication works

Debugging FastAPI errors confidently

Clean backend architecture

JWT-based security

Industry-level FastAPI structure

🏁 Status

✅ Day 15 Completed Successfully
🚀 Ready for advanced backend development
