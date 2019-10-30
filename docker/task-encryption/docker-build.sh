#! /usr/bin/env bash

cp ../../client/console/task_base.py .
cp ../../client/console/task_enc.py .

docker build .
