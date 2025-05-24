FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y gcc python3-dev

# Set working directory
WORKDIR /app

# Copy Pipfile and lock file
COPY Pipfile Pipfile.lock ./

# Install pipenv and dependencies
RUN pip install pipenv && pipenv install --system --deploy

# Verify /app contents before copying
RUN ls -la /app

# Explicitly copy application code to /app
COPY ./app.py /app/

# Run the app
CMD ["python", "/app/app.py"]
