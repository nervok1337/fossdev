FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml poetry.lock ./
run pip install poetry && poetry install --only main --no-root

copy src/app ./app

CMD ["poetry", "run", "uvicorn", "app.main:app","--host", "0.0.0.0", "--port", "8000"]