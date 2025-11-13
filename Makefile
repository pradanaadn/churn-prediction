.PHONY: build

build:
	DOCKER_BUILDKIT=1 docker build -f Dockerfile -t wwwaste-data-pipeline:latest .

up:
	docker compose -f docker-compose.yaml -p churn-prediction up -d

down:
	docker compose -f docker-compose.yaml -p churn-prediction down

start:
	docker compose -f docker-compose.yaml -p churn-prediction start 

stop:
	docker compose -f docker-compose.yaml -p churn-prediction stop