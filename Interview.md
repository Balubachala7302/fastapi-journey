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

🏆 Interview Readiness Verdict

If you can explain:

JWT flow

OAuth2 form-data requirement

Dependency-based security

Errors faced and fixes applied

👉 You are interview-ready for FastAPI backend roles.
