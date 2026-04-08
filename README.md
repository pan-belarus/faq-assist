# faq-assist
The repo for FAQ Assist project

### Prerequisites
The following tools should be installed:
```cmd
docker-compose
company.crt # This is the certificate for the internal company registry.
```

### Up the infrastructure:

```cmd
DOCKER_BUILDKIT=0 docker-compose up -d
DOCKER_BUILDKIT=0 docker-compose up --build faq-assist-api
```

### The health check
```cmd
curl -X GET  http://0.0.0.0:8686/health
```

### Frontend: create the Next.js app with Tailwind CSS, TypeScript, ESLint, and the App Router:
```cmd
npx create-next-app@latest frontend --typescript --tailwind --eslint --app
```

### Check the API code
```cmd
docker exec -it faq-assist-api black --check .
docker exec -it faq-assist-api ruff check .

docker exec -u root -it faq-assist-api apt-get update
docker exec -u root -it faq-assist-api apt-get install -y git
docker exec -it faq-assist-api isort . --check-only
```
### Fix the API code
```cmd
docker exec -it faq-assist-api black .
docker exec -it faq-assist-api ruff check .
docker exec -it faq-assist-api isort .
```

### Check the frontend code
```cmd
docker exec -it faq-assist-ui npx prettier --check "app/**/*.{ts,tsx}"
```

### Fix the frontend code
```cmd
docker exec -it faq-assist-ui npx prettier --write "app/**/*.{ts,tsx}"
```

