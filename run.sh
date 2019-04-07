#!/bin/bash


echo "Creating postgress docker"

cd postgres_docker
sh run.sh

echo "postgress docker complete"

cd ../
echo "Running python scripts"

cd python_test
sh run.sh

echo "Python script running complete."
cd ..

echo "Cleaning"

sh clean.sh


