# ☀️ Weather Info App

Интерактивное веб-приложение на Flask, которое отображает текущую погоду по нескольким локациям. Доступно в Docker-контейнере и поддерживает работу с PostgreSQL через docker-compose.

---

## 🚀 Быстрый старт

### 📦 С Docker
```bash
docker-compose up --build
```

Открой в браузере: [http://localhost:5000](http://localhost:5000)

---

### 🐘 С Базой Данных
```bash
docker-compose -f docker-compose-with-db.yml up --build
```

> Образ PostgreSQL автоматически поднимается и доступен по адресу: `postgres://user:password@db/weather`

---

## 📁 Структура проекта

```
weather-app/
├── app.py                      # Основное Flask-приложение
├── templates/
│   └── index.html              # HTML-шаблон интерфейса
├── requirements.txt            # Зависимости Python
├── Dockerfile                  # Docker-инструкция
├── docker-compose.yml          # Docker-сборка без БД
├── docker-compose-with-db.yml  # Docker-сборка с PostgreSQL
├── test.yml                    # GitHub Actions CI
└── README.md                   # Документация
```

---

## 🌐 Интерфейс

Простой и информативный UI:

![UI Screenshot](https://via.placeholder.com/600x200.png?text=Weather+UI+Preview)

---

## 🧪 Тестирование (CI)

Файл `test.yml` настроен для запуска на GitHub Actions:

- Проверка зависимостей
- Юнит-тесты
- CI при `push`

---

## ⚙️ Зависимости

- Python 3.10
- Flask
- psycopg2-binary
- Docker & Docker Compose

---

## 📬 Обратная связь

Создавай issue или pull request — будем рады доработкам! 🙌

---

## 📝 Лицензия

MIT License. Используй свободно — и не забудь поставить ⭐️ :)
