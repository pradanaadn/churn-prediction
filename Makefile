.PHONY: build

build:
	DOCKER_BUILDKIT=1 docker build -f Dockerfile -t wwwaste-data-pipeline:latest .
copy-env:
	cp .env.example .env
up:
	docker compose -p churn-prediction up -d

up-build-debug:
	docker compose -f docker-compose.yaml -p churn-prediction up --build 
down:
	docker compose  -p churn-prediction down

start:
	docker compose  -p churn-prediction start 

stop:
	docker compose  -p churn-prediction stop