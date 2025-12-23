# Docker Day 1 — Nginx Container Demo

## Goal
Run a production-style container locally using Docker + WSL2.

## Commands Used
- docker run -d --name nginx-demo -p 8080:80 nginx
- docker ps
- docker logs nginx-demo --tail 20

## Result
- Nginx running locally at: http://localhost:8080
- Verified container running via `docker ps`

## What I learned
- Images vs containers
- Port mapping (host:container)
- Basic container lifecycle checks

