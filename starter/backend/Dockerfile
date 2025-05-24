# starter/backend/Dockerfile
FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --system --deploy
COPY . .

CMD ["python", "app.py"]
