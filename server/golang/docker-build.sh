#! /usr/bin/env bash

BUILD_NO=$1
DATE=`date +%Y%m%d`
TAG="v${DATE}_${BUILD_NO}"
REPO=docker.io
BASE=eonuallain/dcomp-server-golang
#FULL=$REPO/$BASE
FULL=$BASE

if [ "$#" -ne 1 ]; then
    echo "missing build number argument, e.g. 1"
    exit 1
fi

echo "tagging as $FULL:$TAG"

docker build -t $FULL:$TAG -t $FULL:latest .
docker push $FULL:$TAG
docker push $FULL:latest
