# ☀️ Weather Info App

A simple interactive Flask web application that displays current weather conditions for various locations. Easily deployable using Docker and supports PostgreSQL integration via Docker Compose.

---

## 🚀 Quick Start

### 📦 Run with Docker
```bash
docker-compose up --build
```

Then open in your browser: [http://localhost:5000](http://localhost:5000)

---

### 🐘 Run with PostgreSQL
```bash
docker-compose -f docker-compose-with-db.yml up --build
```

> PostgreSQL container will be available at: `postgres://user:password@db/weather`

---

## 📁 Project Structure

```
weather-app/
├── app.py                      # Main Flask application
├── templates/
│   └── index.html              # HTML UI template
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker build instructions
├── docker-compose.yml          # Docker Compose (no DB)
├── docker-compose-with-db.yml  # Docker Compose with PostgreSQL
├── test.yml                    # GitHub Actions CI pipeline
└── README.md                   # Project documentation
```

---

## 🌐 UI Preview

Simple and informative user interface:

![UI Screenshot](https://via.placeholder.com/600x200.png?text=Weather+UI+Preview)

---

## 🧪 Testing (CI)

The `test.yml` file is configured for GitHub Actions:

- Dependency installation
- Unit testing
- CI pipeline on every `push`

---

## ⚙️ Tech Stack

- Python 3.10
- Flask
- psycopg2-binary
- Docker & Docker Compose

---

## 📬 Feedback

Feel free to open an issue or contribute with a PR — contributions are welcome! 🙌

---

## 📝 License

MIT License. Use freely and don't forget to ⭐️ the repo!
