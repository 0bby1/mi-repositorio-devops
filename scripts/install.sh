#!/bin/bash

cd /home/ubuntu/app/app

docker stop flask-app || true
docker rm flask-app || true
docker rmi flask-app || true

docker build -t flask-app .
docker run -d -p 5000:5000 flask-app
