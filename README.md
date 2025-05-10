# Simple Weather Info Web Page (Dockerized)

This project displays a static weather info page using Python's built-in HTTP server.

## How to Run

```bash
docker-compose up --build
```

Then open: http://localhost:5000

## File Summary

- `index.html`: weather page
- `Dockerfile`: container definition
- `docker-compose.yml`: compose configuration
- `.github/workflows/test.yml`: GitHub Actions for CI