FROM python:3.13-slim-trixie

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl ca-certificates build-essential git gcc libpq-dev && \
    curl -fsSL https://astral.sh/uv/install.sh -o /uv-installer.sh && \
    sh /uv-installer.sh && rm /uv-installer.sh && \
    export PATH="/root/.local/bin:$PATH" && \
    /root/.local/bin/uv sync --locked && \
    apt-get purge -y --auto-remove build-essential git gcc && \
    rm -rf /var/lib/apt/lists/* /root/.cache /tmp/* && \
    find / -name '__pycache__' -type d -prune -exec rm -rf {} + || true

COPY . /app

ENV PATH="/root/.local/bin:$PATH"

RUN useradd --uid 1000 --create-home appuser && chown -R appuser:appuser /app
USER appuser
