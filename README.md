# Proyecto DevOps - Flask + Jenkins + Docker

Este proyecto implementa un pipeline CI/CD usando Jenkins y Docker.

## Tecnologías
- Python (Flask)
- Docker
- Jenkins
- GitHub Webhooks

## Flujo
1. Se hace push al repositorio
2. GitHub dispara webhook
3. Jenkins ejecuta pipeline
4. Se construye imagen Docker
5. Se despliega automáticamente
