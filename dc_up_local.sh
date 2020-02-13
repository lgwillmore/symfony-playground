#!/usr/bin/env bash

# Run from outside of docker
# Will give us a running local docker compose network.
set -e
set -o pipefail

# First build our base php environment container
pushd docker
./build_base_php.sh
popd

# Start up our network with all of the running services and execute the tests
pushd docker/test
docker-compose build
docker-compose up -d
popd

./wait_for_container.sh test_symfonyplay_1 90