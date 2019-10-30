#! /usr/bin/env bash

if [[ $# -eq 0 ]] ; then
    echo 'Missing server URL argument, exiting'
    exit 1
fi

echo "using server URL $1"

python3 main.py $1