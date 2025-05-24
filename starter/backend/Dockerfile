# starter/backend/Dockerfile
FROM python:3.9-slim

RUN apt-get update && apt-get install -y gcc python3-dev

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && pipenv install --system --deploy

COPY movies/ ./movies
COPY movies/app.py .

CMD ["python", "app.py"]