.PHONY: dev prod test down

dev:
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build

prod:
    docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d

test:
    docker-compose -f docker-compose.yml -f docker-compose.test.yml up --build

down:
    docker-compose down