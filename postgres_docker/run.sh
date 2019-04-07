#!/bin/bash

image_name="final_postgres"
postgres_container_name="demo"

docker build -t $image_name .
docker run --name $postgres_container_name -e POSTGRES_USER=blue -e  POSTGRES_PASSWORD=blue -e POSTGRES_DB=blue -d -p 5432:5432 $image_name

