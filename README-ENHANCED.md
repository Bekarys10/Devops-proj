
# 🌦️ Weather Info Web Page (Enhanced Version)

Welcome to the **Weather Info Web Page** — a simple and elegant web application that displays weather information through a static HTML interface. This project is entirely Dockerized and leverages Python's built-in HTTP server for rapid deployment and portability.

---

## 🧭 Overview

This project aims to demonstrate how you can package a lightweight static webpage into a fully functional containerized service using Docker. It's perfect for:

- 🚀 Learning Docker basics
- 📡 Hosting minimal apps or dashboards
- 🎓 Teaching environments or DevOps demos

---

## 🔧 Technologies Used

- **HTML5/CSS3** — for the weather page layout  
- **Python 3.x** — using `http.server` as the backend  
- **Docker & Docker Compose** — for containerization  
- **GitHub Actions** — basic CI/CD pipeline (if configured)

---

## 📂 Project Structure

```
weather-info/
├── index.html                  # Static weather page
├── Dockerfile                  # Docker build instructions
├── docker-compose.yml          # Orchestration setup
└── .github/
    └── workflows/
        └── test.yml            # GitHub Actions CI pipeline
```

---

## 🚀 Running the Project Locally

### Prerequisites

Ensure you have the following installed:

- Docker ≥ 20.10  
- Docker Compose ≥ 1.29  

### Steps

```bash
# Clone the repository
git clone https://github.com/your-username/weather-info.git
cd weather-info

# Build and run the container
docker-compose up --build
```

🖥 Open your browser and visit:  
👉 [http://localhost:5000](http://localhost:5000)

---

## 📦 Docker Compose Configuration

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
```

This exposes the weather page on `localhost:5000`.

---

## 🧪 Continuous Integration

This project optionally supports CI with GitHub Actions:

- Workflow location: `.github/workflows/test.yml`
- Auto-triggers on every push to validate the container

---

## 📥 Download

A packaged version of this project is available as a ZIP archive:  
📎 [Download weather-project.zip](sandbox:/mnt/data/weather-project.zip)

---

## 📸 Optional Preview

> *(Insert a screenshot if available)*

```

---

## 📝 License

This project is licensed under the **MIT License**.  
Feel free to fork, modify, and deploy.

