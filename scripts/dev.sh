#! /usr/bin/env sh

# Exit in case of error
set -e

docker compose -f docker-compose-dev.yml config > docker-stack-dev.yml

docker compose -f docker-stack-dev.yml build
docker compose -f docker-stack-dev.yml down --remove-orphans
docker compose -f docker-stack-dev.yml up -d
docker compose -f docker-stack-dev.yml exec -T backend bash /app/prestart.sh
