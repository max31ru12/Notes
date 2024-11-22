```docker
FROM python:3.9-slim as base
LABEL maintainer="Make <maxevg72@gmail.com"

# Сборка зависимостей
ARG BUILD_DEPS="curl"
RUN apt-get update && apt-get install -y $BUILD_DEPS

# Установка poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.2.0 POETRY_HOME=/root/poetry python3 -
ENV PATH="${PATH}:/root/poetry/bin"

# Инициализация проекта
WORKDIR /app
ENTRYPOINT ["./docker-entrypoint.sh"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установка питонячьих библиотек
COPY poetry.lock pyproject.toml /
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Копирование в контейнер папок и файлов.
COPY . .
```

`PYTHONUNBUFFERED` отвечает за отключение буферизации вывода (output). То есть непустое значение данной переменной среды гарантирует, что мы можем видеть выходные данные нашего приложения в режиме реального времени.

`PYTHONDONTWRITEBYTECODE` означает, что Python не будет пытаться создавать файлы .pyc.

`virtualenvs.create false` - отключаем создание виртуального окружения

`--no-interaction` - интерактив

`--no-ansi` - ANSI-output