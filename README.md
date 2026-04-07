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

curl -X POST "http://localhost:8686/messages/?session_id=6f56c1596e34473485fc05c30c3ae764" \
-H "Content-Type: application/json" \
-d '{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "hello",
    "arguments": {}
  }
}'

### Frontend
```cmd
npx create-next-app@latest frontend --typescript --tailwind --eslint --app
```
