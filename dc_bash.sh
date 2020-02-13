#!/usr/bin/env bash

# Run from outside of docker
# Assumes that `dc_up_local.sh` has already been run.
# Will give you a bash shell inside of the xturf container.

set -e
set -o pipefail

docker exec -it test_symfonyplay_1 bash