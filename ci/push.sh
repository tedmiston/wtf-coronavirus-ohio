#!/usr/bin/env bash

set -euo pipefail

DOCKER_USERNAME=${DOCKER_USERNAME:-''}
DOCKER_PASSWORD=${DOCKER_PASSWORD:-''}
GITHUB_ACTIONS=${GITHUB_ACTIONS:-false}

IMAGE=${1}

if [ "${GITHUB_ACTIONS}" == true ]; then
    echo "${DOCKER_PASSWORD}" | docker login --username="${DOCKER_USERNAME}" --password-stdin
fi

docker push "${IMAGE}"

if [ "${GITHUB_ACTIONS}" == true ]; then
    docker logout
fi
