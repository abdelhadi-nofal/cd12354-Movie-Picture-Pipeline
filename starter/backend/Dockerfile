# starter/backend/Dockerfile
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y gcc python3-dev

# Set working directory
WORKDIR /app

# Copy Pipfile and lock file
COPY Pipfile Pipfile.lock ./

# Install pipenv and dependencies
RUN pip install pipenv && pipenv install --system --deploy

# Copy application code
COPY app.py .

# Run the app
CMD ["python", "app.py"]