.PHONY: build

build:
	DOCKER_BUILDKIT=1 docker build -f deployments/docker/Dockerfile -t wwwaste-data-pipeline:latest .

up:
	docker compose up -d

down:
	docker compose down

start:
	dockercompose start

stop:
	docker compose stop
