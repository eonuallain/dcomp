#! /usr/bin/env bash

cp ../../client/console/task_base.py .
cp ../../client/console/task_enc.py .

TAG=v20191030_1
REPO=docker.io
BASE=eonuallain/dcomp-task-enc
FULL=$REPO/$BASE

echo "tagging as $FULL:$TAG"

ID=$(docker build -t $FULL:$TAG -t $FULL:latest .)

docker push $FULL:$TAG
docker push $FULL:latest
