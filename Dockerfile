FROM "python:3.9.9-slim-buster"

WORKDIR /app
COPY pyproject.toml ./
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . .



CMD uvicorn app.infer:app --host 0.0.0.0 --port 8080