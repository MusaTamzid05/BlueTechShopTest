#!/bin/bash

docker build -t python_test .
docker run --rm -t -i --link demo:pg python_test

