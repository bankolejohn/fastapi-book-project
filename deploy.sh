#!/bin/bash

echo "Pulling image for $DOCKER_HUB_USERNAME"
docker pull $DOCKER_HUB_USERNAME/fastapi-app:latest

docker stop fastapi-app || true
docker rm fastapi-app || true

echo "Running pulled image"
docker run -d --restart always -p 8000:8000 --name fastapi-app $DOCKER_HUB_USERNAME/fastapi-app:latest
