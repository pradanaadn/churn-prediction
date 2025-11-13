# Churn Prediction Pipeline

ML pipeline for customer churn prediction using LightGBM, Prefect, and Evidently.

**[Demo Video](https://www.loom.com/share/61a4b49afc9d499eb54b291d1844d6df)**
**[Drift Detection Monitoring Demo](https://www.loom.com/share/46b64b100b4e4ce9b66df46263f7d403)**
## Quick Start

```bash
# 1. Copy environment file
make copy-env

# 2. Start services
make up

# 3. Access UIs
# Prefect: http://localhost:4200
# Evidently: http://localhost:7000
```

## Stop Services

```bash
make down
```

## Local Development

```bash
# Install dependencies
uv sync

# Copy .env
make copy-env
# run prefect server
uv run prefect server start
# Run flow
uv run src/flow/batch_inference.py
```

## Architecture

| Service | Port |
|---------|------|
| Prefect Server | 4200 |
| Evidently | 7000 |
| PostgreSQL | 5432 |
| Redis | 6379 |

## Make Commands

```bash
make copy-env          # Setup .env
make build             # Build Docker image
make up                # Start services
make up-build-debug    # Start with build logs
make start/stop        # Control services
make down              # Stop & remove
```

## Model

- **Input**: Age, Annual Income, Gender, Membership Duration, Location
- **Output**: Churn prediction (0/1)
- **Algorithm**: LightGBM (200 estimators)