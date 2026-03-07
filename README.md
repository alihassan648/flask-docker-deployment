# Flask Docker Deployment

A production-ready Python web application deployed on a Linux VPS using Docker and Nginx.

## Live Demo
https://sohailali.site

## Architecture
```
Client → HTTPS (SSL) → Nginx (Reverse Proxy) → Docker Container → Flask App
```

## Stack
- Python 3.11 + Flask
- Docker + Docker Compose
- Nginx reverse proxy
- Let's Encrypt SSL certificate
- DigitalOcean Ubuntu VPS

## Features
- Live HTTPS endpoint
- /health monitoring endpoint
- Auto-restart on failure (restart: always)
- Production Nginx configuration

## Deployment
```bash
git clone https://github.com/alihassan648/flask-docker-deployment
cd flask-docker-deployment
docker compose up -d --build
```

## Author
Sohail Ali — DevOps Engineer
https://sohailali.site
