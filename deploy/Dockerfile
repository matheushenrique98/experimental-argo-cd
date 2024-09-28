FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev

COPY . .

RUN poetry install

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
