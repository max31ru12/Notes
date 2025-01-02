## 1. Dockerfile: `poetry` + `fastapi`

[Статья про poetry в докер](https://medium.com/@albertazzir/blazing-fast-python-docker-builds-with-poetry-a78a66f5aed0)


Простейшая конфигурация:

```dockerfile
FROM python:3.12-slim

RUN pip install poetry

WORKDIR /project # Корневая папка всего проекта

COPY poetry.lock ./
COPY pyproject.toml ./

RUN poetry install

COPY app ./app # Папка приложения, где находится main.py

ENTRYPOINT ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]

EXPOSE 8000 # Мб не надо
```

#### Самое важное:

- указываем хост `0.0.0.0`, чтобы можно было получить доступ с хоста (т.е. снаружи контейнера)
- если билдить образ вручную, то надо учитывать контекст билда (в данном случае контекст билда это текущая директория: `.`):
```shell
docker build . -t name:version -f path/to/dockerfile
```

## 2. Docker Compose: `db` + `api`

```yml
version: "3.8"

services:
  db:
    container_name: portfolio_db
    image: postgres
    environment:
      - POSTGRES_USER=test
      - POSTGRES_USER=test
      - POSTGRES_PASSWORD=test
    volumes:
      - db:/data/postgres
    ports:
      - "5432:5432"
    networks:
      - default
    restart: unless-stopped

  api:
    depends_on:
      - db
    build:
      dockerfile: /compose/api/Dockerfile
    container_name: api
    environment:
      - DB_HOST=localhost
      - DB_PORT=5432
      - DB_PASSWORD=test
      - DB_USER=test
      - DB_NAME=test
    ports:
      - "8000:8000"
    networks:
      - default


networks:
  default:
    driver: bridge

volumes:
  db:
```
