#!/bin/bash
app="docker.flask"

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)

cd /vagrant/flask
docker build -t ${app} .
sudo apt-get install -y docker-compose 

cd /vagrant/traefik
docker-compose up -d