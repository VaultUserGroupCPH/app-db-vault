#!/usr/bin/env sh

# Setup environment
shopt -s expand_aliases
# TODO: extract main-secrets from docker/awk.
alias vault='docker exec -it main-secrets vault "$@"'
export VAULT_HOST=$(echo $DOCKER_HOST | grep -Eo '\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'):8200

# Initialize
OUTPUT="$( { vault init -key-shares=1 -key-threshold=1 | head -n2; } 2> /dev/null)"

VAULT_KEY=$(echo "$OUTPUT" | grep 'Key' | awk -F': ' '{print $2}')

export VAULT_TOKEN=$(echo "$OUTPUT" | grep 'Root Token' | awk -F': ' '{print $2}' | tr -d ' ')

# Unseal
vault unseal $VAULT_KEY
