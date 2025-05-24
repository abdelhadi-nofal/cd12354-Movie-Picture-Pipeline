# starter/backend/Dockerfile
# Use official Python image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y gcc python3-dev

# Set working directory
WORKDIR /app

# Copy Pipfile and lock file
COPY Pipfile Pipfile.lock ./

# Install pipenv and dependencies
RUN pip install pipenv && pipenv install

# Copy application code
COPY . .

# Run the app
CMD ["pipenv", "run", "python", "app.py"]