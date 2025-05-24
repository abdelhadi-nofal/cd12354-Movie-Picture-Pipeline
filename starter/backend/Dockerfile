# starter/backend/Dockerfile
FROM python:3.9-slim  # Remove --platform=linux/amd64

WORKDIR /app
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --system --deploy
COPY . .