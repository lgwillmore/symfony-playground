#!/usr/bin/env bash

# Run from outside of docker
# Assumes that `dc_up_local.sh` has already been run.
# Runs all the tests
set -e
set -o pipefail

docker exec test_xturf_1 /var/www/xturf-api/docker/test/composer_install.py
docker exec test_xturf_1 /var/www/xturf-api/docker/test/clean_db.py
docker exec test_xturf_1 /var/www/xturf-api/docker/test/run_test.py

