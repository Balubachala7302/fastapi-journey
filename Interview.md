This section contains interview-ready questions and answers based on my FastAPI 80/20 learning journey, including real errors faced and fixed during development.

🟢 Day-1: FastAPI Basics
1️⃣ What is FastAPI?

Answer:
FastAPI is a modern, high-performance Python web framework used to build APIs with automatic validation, type hints, and interactive documentation.

2️⃣ Why is FastAPI fast?

Answer:
FastAPI is built on Starlette and Pydantic, uses ASGI, and leverages Python type hints for efficient request handling.

3️⃣ What is Swagger UI and how do you access it?

Answer:
Swagger UI provides interactive API documentation and can be accessed at /docs.

4️⃣ What are path parameters?

Answer:
Path parameters are dynamic values passed through the URL path, e.g. /square/{number}.

5️⃣ Difference between GET and POST?

Answer:

GET → Fetch data

POST → Send data to server (usually request body)

🟡 Day-2: Request Body & Pydantic
6️⃣ What is Pydantic and why does FastAPI use it?

Answer:
Pydantic validates request data using Python type hints and automatically returns structured error responses.

7️⃣ What happens if invalid data is sent?

Answer:
FastAPI automatically returns a 422 Unprocessable Entity error with validation details.

8️⃣ What is request body?

Answer:
Request body is data sent by the client (usually JSON) for POST/PUT requests.

9️⃣ Advantage of automatic validation?

Answer:
Reduces manual checks, improves reliability, and ensures clean API contracts.

🟠 Day-3: Dependency Injection (Depends)
🔟 What is dependency injection in FastAPI?

Answer:
Dependency injection allows FastAPI to automatically provide required logic (like auth, headers, DB sessions) before route execution.

1️⃣1️⃣ Why use Depends()?

Answer:
To keep routes clean, reusable, testable, and scalable.

1️⃣2️⃣ Can dependencies be reused?

Answer:
Yes. A single dependency can be injected into multiple routes.

1️⃣3️⃣ What happens if a dependency fails?

Answer:
FastAPI stops execution and immediately returns an error response.

🔵 Day-4: Authorization & Headers
1️⃣4️⃣ What is authorization?

Answer:
Authorization checks whether an authenticated user has permission to access a resource.

1️⃣5️⃣ How did you implement authorization?

Answer:
Using header-based validation via Depends() and raising HTTPException on failure.

1️⃣6️⃣ Why return 401 instead of 403?

Answer:

401 → Authentication failed or missing

403 → Authenticated but not permitted

1️⃣7️⃣ Why doesn’t a protected endpoint open in the browser?

Answer:
Because browsers do not send custom headers like Authorization tokens.

🔴 Day-5: JWT & OAuth2 Authentication
1️⃣8️⃣ What is JWT?

Answer:
JWT (JSON Web Token) is a stateless authentication mechanism that securely transfers user identity between client and server.

1️⃣9️⃣ What does a JWT contain?

Answer:

Header

Payload (claims like sub, exp)

Signature

2️⃣0️⃣ Why is JWT stateless?

Answer:
Because all authentication data is stored in the token itself, not on the server.

2️⃣1️⃣ What is OAuth2PasswordBearer?

Answer:
It extracts the Bearer token from the Authorization header and supplies it to FastAPI dependencies.

2️⃣2️⃣ Why does OAuth2 use form-data instead of JSON?

Answer:
OAuth2 specification mandates application/x-www-form-urlencoded for credentials, not JSON.

2️⃣3️⃣ Why use OAuth2PasswordRequestForm instead of Pydantic?

Answer:
Swagger UI and OAuth2PasswordBearer expect form-data fields (username, password), not JSON.

2️⃣4️⃣ How do you protect routes using JWT?

Answer:
By validating the token inside a dependency using Depends(oauth2_scheme) before route execution.

2️⃣5️⃣ What is the Authorization header format?
Authorization: Bearer <JWT_TOKEN>

🔴 Day-5: Error-Based Interview Questions (Very Important)
2️⃣6️⃣ Why did you get 401 Unauthorized after login?

Answer:
Because the JWT token was not sent in the Authorization header or Swagger authorization was not done.

2️⃣7️⃣ Why did Swagger show “Auth error: Unauthorized”?

Answer:
Because the Authorize button was not used or the Bearer token was missing/expired.

2️⃣8️⃣ Why did FastAPI say:
Form data requires "python-multipart"


Answer:
Because OAuth2 login uses form-data, which requires the python-multipart package.

2️⃣9️⃣ Why did bcrypt throw version errors?

Answer:
Due to incompatibility between bcrypt, passlib, and Python 3.11 on Windows. Fixed by pinning stable versions.

3️⃣0️⃣ Why did /profile return Not authenticated in browser?

Answer:
Because browsers do not send Authorization headers automatically.

3️⃣1️⃣ Difference between 401 and 403?

Answer:

401 → Authentication problem

403 → Authorization problem

Perfect 👍
Below is a clean, interview-ready README.md content covering Day-6 to Day-8, including concept questions + real errors you faced and their explanations.

You can copy-paste this directly into README.md.


---

🚀 FastAPI Interview Preparation

Day-6 to Day-8 (Auth → JWT → Project Refactor)


---

📅 Day-6: Dependency Injection & Authorization Basics

1️⃣ What is Dependency Injection in FastAPI?

Answer:
Dependency Injection (DI) allows FastAPI to automatically provide required objects (like authenticated users, headers, DB sessions) to endpoints using Depends().

def get_current_user():
    return {"username": "bhaskar"}

@app.get("/profile")
def profile(user=Depends(get_current_user)):
    return user


---

2️⃣ Why does FastAPI use Depends()?

Answer:

Code reuse

Separation of concerns

Cleaner and testable architecture



---

3️⃣ Difference between Authentication and Authorization?

Authentication	Authorization

Who you are	What you can access
Login	Role / Permission
JWT / OAuth	Admin, User, RBAC



---

4️⃣ How do you restrict access to an endpoint?

Answer:
By validating user role or permissions inside a dependency.

def require_admin(user=Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403)


---

❌ Common Day-6 Error

Error: 401 Unauthorized
Reason: Missing dependency or invalid token
Fix: Ensure Depends() is used and token is passed correctly.


---

📅 Day-7: JWT Authentication & Role-Based Access


---

5️⃣ What is JWT?

Answer:
JWT (JSON Web Token) is a signed token used to securely transmit user identity between client and server.

Structure:

HEADER.PAYLOAD.SIGNATURE


---

6️⃣ Why JWT is stateless?

Answer:
The server does not store sessions. All user data is inside the token.


---

7️⃣ What is OAuth2PasswordBearer?

Answer:
It tells FastAPI:

Token comes from Authorization: Bearer <token>

Used to extract JWT automatically


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


---

8️⃣ Difference between 401 and 403?

Code	Meaning

401	Not authenticated
403	Authenticated but forbidden



---

9️⃣ How do you implement Admin-only access?

Answer:

def require_admin(user=Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403)


---

❌ Real Day-7 Errors You Faced

Error: python-multipart not installed

Reason:
OAuth2 login uses form data.

Fix:

pip install python-multipart


---

Error: bcrypt has no attribute __about__

Reason:
Version conflict between bcrypt and passlib.

Fix:

pip install bcrypt==4.0.1 passlib==1.7.4


---

Error: Swagger shows Unauthorized after login

Reason:
Token not applied via Authorize button.

Fix:
Click Authorize → Paste Bearer token → Authorize


---

📅 Day-8: Project Refactor & APIRouter


---

🔟 Why refactor FastAPI projects?

Answer:

Maintainability

Scalability

Industry-standard structure

Interview expectation



---

1️⃣1️⃣ What is APIRouter?

Answer:
APIRouter helps split routes into multiple files.

router = APIRouter()

@router.get("/profile")
def profile():
    pass


---

1️⃣2️⃣ How do you register routers?

Answer:

app.include_router(auth.router)


---

1️⃣3️⃣ What should main.py contain after refactor?

Answer:
ONLY:

App initialization

Router registration

Health/root endpoints


❌ No business logic
❌ No auth logic


---

1️⃣4️⃣ Why separate core, api, models?

Folder	Responsibility

core	Config, security
api	Routes
models	Schemas



---

❌ Day-8 Git Errors & Fixes

Error: Could not import module "main"

Reason:
main.py moved inside app/

Fix:

uvicorn app.main:app --reload


---

Error: deleted: main.py

Reason:
You moved main.py into app/

Fix:

git add app
git commit -m "Refactor project structure"


---

Error: fatal: pathspec did not match

Reason:
File path changed after refactor.

Fix:

git status
git add app/


---

🧠 Interview Power Questions (Direct)

❓ Why FastAPI over Django/Flask?

Async support

Automatic docs

Type safety

Faster performance



---

❓ How would you scale this project?

Database layer

Pagination

Background tasks

Caching 
