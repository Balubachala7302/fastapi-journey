# 🚀 FastAPI Production Backend (Day 1 – Day 35 Journey)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production--Ready-green)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![Redis](https://img.shields.io/badge/Redis-Caching-red)
![Celery](https://img.shields.io/badge/Celery-Background--Workers-darkgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

This repository documents my **35-day hands-on FastAPI learning journey**, where I progressively built a **production-ready backend system** with authentication, caching, background workers, containerization, and modern backend architecture.

By the end of this journey, the project evolved from simple endpoints into a **scalable backend architecture similar to modern SaaS systems**.

---

# 🧠 Key Highlights

✔ JWT Authentication with Refresh Tokens  
✔ Redis-based Token Blacklisting  
✔ Role-Based Access Control (RBAC)  
✔ Database Migrations with Alembic  
✔ Background Workers with Celery + Redis  
✔ API Rate Limiting  
✔ Dockerized Deployment  
✔ Gunicorn Production Server  
✔ Structured Logging & Global Error Handling  
✔ Pagination, Filtering, and Sorting APIs  

---

# 🛠 Tech Stack

| Layer | Technology |
|------|-------------|
| Language | Python 3.11 |
| API Framework | FastAPI |
| Server | Uvicorn / Gunicorn |
| ORM | SQLAlchemy |
| Database | SQLite |
| Migrations | Alembic |
| Caching | Redis |
| Background Jobs | Celery |
| Containerization | Docker & Docker Compose |
| Authentication | JWT (python-jose) |
| Password Hashing | Passlib (bcrypt) |
| Validation | Pydantic v2 |

---

# 🏗 System Architecture

Client
   │
   ▼
Gunicorn
   │
   ▼
FastAPI Application
   │
   ├── PostgreSQL / SQLite (Database)
   │
   ├── Redis (Caching + Token Blacklist)
   │
   └── Celery Workers
          │
          └── Background Tasks (Emails, Jobs)

---

# 📁 Project Structure

app/
│
├── api/
│   ├── auth.py
│   ├── users.py
│   └── deps.py
│
├── core/
│   ├── config.py
│   ├── security.py
│   ├── redis.py
│   ├── rate_limiter.py
│   ├── logger.py
│   ├── response.py
│   └── exceptions.py
│
├── db/
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
│
├── services/
│   ├── auth_service.py
│   └── user_service.py
│
├── tasks/
│   ├── celery_app.py
│   └── tasks.py
│
└── main.py

alembic/
docker-compose.yml
Dockerfile
.env

---

# 🔐 Authentication Flow

### Register User

POST /users/register

### Login

POST /auth/login

Returns:
    |access_token
    |refresh_token

### Authorize

Authorization : Bearer <access_token>

### Access Protected Route

Get /me

### Refresh Toke

POST /auth/refresh
### Logout

Token is added to a **Redis blacklist** preventing reuse.

---

# ⚡ Features Implemented

### Security
- JWT authentication
- Refresh token rotation
- Token revocation
- Role-based authorization
- API rate limiting

### Backend Architecture
- Dependency Injection
- Service Layer Pattern
- Clean API Router Design
- Global Exception Handling
- Structured Logging Middleware

### Performance & Scaling
- Redis caching
- Pagination & filtering
- Celery background workers
- API rate limiting

### Production Setup
- Docker containerization
- Docker Compose orchestration
- Gunicorn production server
- Health check endpoint

---

# 🧪 Running the Application

### Activate Virtual Environment

    |venv\Scripts\activate


### Run FastAPI Server

    |uvicorn app.main:app --reload

### Swagger Documentation:
    |http://127.0.0.1:8000/docs


---

# 🐳 Running with Docker

    |docker compose up --build

This will start:

- FastAPI Application
- Redis Server
- Celery Worker

---

# 📊 Learning Timeline

| Phase | Focus |
|------|------|
| Day 1–10 | FastAPI fundamentals & authentication |
| Day 11–20 | JWT security & database architecture |
| Day 21–25 | production practices & clean architecture |
| Day 26–30 | pagination, logging, API improvements |
| Day 30–33 | Docker + Celery + Redis workers |
| Day 34 | API rate limiting |
| Day 35 | production hardening |

---

# 🎯 Key Backend Concepts Learned

- REST API Design
- Authentication & Authorization
- Dependency Injection
- Database Migrations
- Token Revocation
- Background Task Processing
- Caching Strategies
- Containerized Deployment
- Production Logging
- API Security

---

# 🏁 Project Status

    |✔ FastAPI Backend Journey Completed (Day 1 – Day 35) ✔ Production-Ready Backend Architecture Implemented---

# 👨‍💻 Author

**Bala Bhaskar**

Backend Developer | Python | FastAPI

---

# ⭐ Future Improvements

- PostgreSQL integration
- CI/CD pipelines
- API versioning
- Automated testing (pytest)
- Kubernetes deployment

