#!/bin/bash

docker build -t python_test .
docker run --rm --link demo:pg python_test

