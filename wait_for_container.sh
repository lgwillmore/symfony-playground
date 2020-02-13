#!/usr/bin/env bash

function is_container_running() {
  docker container inspect $1 >>/dev/null 2>&1
  retVal=$?
  if [ $retVal -ne 0 ]; then
    # False
    return 0
  else
    # True
    return 1
  fi
}

function wait_for_container() {
  start=$(date +%s)
  now=$start
  is_container_running $1
  while [ $? -eq 0 ] && [ $((now - start)) -le $2 ]; do
    sleep 5
    now=$(date +%s)
    is_container_running $1
  done
}

function main() {
  local container_name=$1
  local timeout=$2
  wait_for_container $container_name $timeout
  is_container_running $container_name
  if [ $retVal -ne 0 ]; then
    echo "Waited $timeout seconds for $container_name. No container started"
    exit 1
  else
    echo "$container_name is up and running"
    exit 0
  fi
}

main "$1" "$2"
