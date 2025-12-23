# Docker Day 2 — Flask App Container

## Run locally
docker build -t flask-demo:1.0 .
docker run -d --name flask-demo -p 5000:5000 flask-demo:1.0

## Test
Open http://localhost:5000
