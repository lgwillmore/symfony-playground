#!/usr/bin/env bash

# Run from outside of docker
# Will stop docker compose network
# Start up our network with all of the running services and execute the tests
set -e
set -o pipefail

pushd docker/test
docker-compose down
popd