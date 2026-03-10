# Flask Docker Deployment

A production-ready Python web application deployed on a Linux VPS 
using Docker, PostgreSQL, Nginx and Gunicorn.

## Live Demo
https://sohailali.site

## Architecture
```
Client → HTTPS (SSL) → Nginx (Reverse Proxy) → Gunicorn → Flask App → PostgreSQL
```

## Stack
- Python 3.11 + Flask
- Gunicorn (production WSGI server, 4 workers)
- PostgreSQL 15 (containerized, private network)
- Docker + Docker Compose
- Nginx reverse proxy
- Let's Encrypt SSL certificate
- DigitalOcean Ubuntu VPS

## Key Concepts Demonstrated
- Multi-container Docker application
- Private Docker networking between containers
- Database never exposed to internet
- Environment variables for configuration
- Production WSGI server (not development server)
- Automated SSL certificate renewal

## Endpoints
- / → Main page
- /health → Returns database connection status

## Deployment
```bash
git clone https://github.com/alihassan648/flask-docker-deployment
cd flask-docker-deployment
docker compose up -d --build
```

## Author
Sohail Ali — DevOps Engineer
https://sohailali.site
