# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run app
CMD ["gunicorn", "app.main:app","-k", "uvicorn.workers.UvicornWorker","-w", "4", "-b", "0.0.0.0:8000"]