# 🚀 FastAPI Interview Preparation (Day 1 – Day 15)
**80/20 Learning + Real Errors Faced & Fixed**

This document contains interview-ready questions and answers based on my 15-day FastAPI learning journey, including real errors I faced and fixed during development.

---

## 🟢 Day-1: FastAPI Basics

### 1. What is FastAPI?
FastAPI is a modern, high-performance Python web framework used to build APIs with automatic validation, type hints, and interactive documentation.

### 2. Why is FastAPI fast?
- Built on Starlette (ASGI)
- Uses Pydantic for validation
- Async-first architecture

### 3. What is Swagger UI?
Swagger UI provides interactive API documentation.  
Access it at:

/docs

 
### 4. What are path parameters?
Dynamic values passed through the URL path.
Example:
/square/{number}

yaml
Copy code

### 5. Difference between GET and POST?
- GET → Fetch data
- POST → Send data to server

---

## 🟡 Day-2: Request Body & Pydantic

### 6. What is Pydantic?
Pydantic validates request data using Python type hints and returns structured errors automatically.

### 7. What happens if invalid data is sent?
FastAPI returns:
422 Unprocessable Entity

yaml
Copy code

### 8. What is request body?
JSON data sent from the client for POST/PUT requests.

### 9. Advantage of automatic validation?
- Less manual checks
- Safer APIs
- Clean contracts

---

## 🟠 Day-3: Dependency Injection (Depends)

### 10. What is dependency injection?
FastAPI runs shared logic before executing routes using `Depends()`.

### 11. Why use Depends()?
- Code reuse
- Cleaner routes
- Testability

### 12. Can dependencies be reused?
Yes, across multiple endpoints.

### 13. What happens if a dependency fails?
FastAPI stops execution and returns the error immediately.

---

## 🔵 Day-4: Authorization & Headers

### 14. What is authorization?
Authorization checks what an authenticated user can access.

### 15. How did you implement authorization?
Using `Depends()` and raising `HTTPException`.

### 16. Difference between 401 and 403?
- 401 → Authentication failed
- 403 → Authenticated but forbidden

### 17. Why protected endpoints don’t open in browser?
Browsers don’t send Authorization headers automatically.

---

## 🔴 Day-5: OAuth2 & JWT Authentication

### 18. What is JWT?
JWT is a stateless authentication mechanism.

### 19. What does JWT contain?
- Header
- Payload (`sub`, `exp`)
- Signature

### 20. Why is JWT stateless?
All auth data is inside the token, not stored on the server.

### 21. What is OAuth2PasswordBearer?
Extracts the Bearer token from Authorization header.

### 22. Why OAuth2 uses form-data?
OAuth2 spec requires `application/x-www-form-urlencoded`.

### 23. Authorization header format
Authorization: Bearer <JWT_TOKEN>

yaml
Copy code

---

## ❌ Day-5: Real Errors (Interview Gold)

### Error: Form data requires python-multipart
**Fix**
pip install python-multipart

markdown
Copy code

### Error: bcrypt has no attribute __about__
**Fix**
pip install bcrypt==4.0.1 passlib==1.7.4

yaml
Copy code

### Error: Swagger shows Unauthorized after login
**Reason**
Token not applied using Authorize button.

---

## 🟣 Day-6: Database & SQLAlchemy

### 24. Why SQLAlchemy?
ORM to interact with DB using Python objects.

### 25. What is a DB session?
Manages database transactions.

### Error: UserCreate has no attribute 'mail'
**Fix**
Use `user.email` instead of `user.mail`.

---

## 🟤 Day-7: CRUD Layer

### 26. Why separate CRUD logic?
- Clean architecture
- Reusability
- Testability

### Error: create_user() missing arguments
**Fix**
Align CRUD function signature with schema fields.

---

## 🔵 Day-8: Project Refactor & APIRouter

### 27. What is APIRouter?
Splits routes into multiple files.

### 28. What should main.py contain?
- App initialization
- Router registration
- No business logic

### Git Error: Could not import module "main"
**Fix**
uvicorn app.main:app --reload

yaml
Copy code

---

## 🟢 Day-9: Authentication Debugging

### 29. Why login works but protected route fails?
Token not sent in Authorization header.

---

## 🟡 Day-10: Login Endpoint

### 30. What happens during login?
- Validate credentials
- Create JWT
- Return token

### Error: Invalid credentials
**Reason**
Password compared without hashing.

---

## 🔵 Day-11: get_current_user Dependency

### 31. What is get_current_user?
Extracts JWT, decodes it, and fetches user from DB.

### Error: get_current_user not defined
**Fix**
Import dependency properly.

---

## 🔴 Day-12: Authorization & Roles

### 32. How are routes protected?
Using:
Depends(get_current_user)

yaml
Copy code

### Authentication vs Authorization
| Authentication | Authorization |
|----------------|--------------|
| Who you are | What you can access |

---

## 🟠 Day-13: Refresh Tokens

### 33. Why refresh tokens?
Generate new access tokens without re-login.

### What if refresh token expires?
User must login again.

---

## 🔵 Day-14: Debugging Skills

### Biggest skill learned?
Reading stack traces and fixing schema/CRUD mismatches.

### Error: unexpected keyword argument
**Fix**
Align schema and CRUD parameters.

---

## 🏁 Day-15: Final Integration

### What was completed?
- Registration
- Login
- JWT auth
- Refresh token
- Protected routes
- Clean architecture

### Is Day-15 final?
Final foundation day before advanced backend topics.

---

## 🎯 Interview Power Questions

### Why FastAPI over Flask/Django?
- Async support
- Automatic docs
- Type safety
- High performance

### How would you scale this project?
- PostgreSQL
- Alembic migrations
- RBAC
- Redis caching
- Docker & deployment

---
