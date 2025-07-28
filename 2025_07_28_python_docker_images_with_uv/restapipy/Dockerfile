# 3.13.5-alpine3.22
FROM python@sha256:610020b9ad8ee92798f1dbe18d5e928d47358db698969d12730f9686ce3a3191 AS builder

# 0.8.3
COPY --from=ghcr.io/astral-sh/uv@sha256:ef11ed817e6a5385c02cd49fdcc99c23d02426088252a8eace6b6e6a2a511f36 /uv /uvx /bin/
ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev --locked --no-editable --no-install-project

COPY README.md src ./
RUN uv sync --no-dev --locked --no-editable

RUN uv run --no-sync generate_openapi_json

# 3.13.5-alpine3.22
FROM python@sha256:610020b9ad8ee92798f1dbe18d5e928d47358db698969d12730f9686ce3a3191 AS runtime

COPY --from=builder --chown=root:root /app/.venv /app/.venv
COPY --from=builder --chown=root:root /app/openapi.json /app/openapi.json

RUN chmod -R o=rx /app

RUN adduser -D -H worker
USER worker
EXPOSE 9876

ENV PYTHONPATH=/app/.venv/lib/python3.13/site-packages
CMD ["python", "-m", "restapipy"]