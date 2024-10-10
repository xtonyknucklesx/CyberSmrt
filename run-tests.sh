#!/bin/bash

# Run the tests
docker-compose -f docker-compose.yml -f docker-compose.test.yml up --abort-on-container-exit

# Bring down the containers after the tests finish
docker-compose -f docker-compose.yml -f docker-compose.test.yml down