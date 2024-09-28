FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

COPY . .

RUN poetry install --no-dev --no-interaction --no-ansi

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]