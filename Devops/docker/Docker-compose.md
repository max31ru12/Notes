В качестве хоста в python-программах указываем имя сервиса: То есть, если хотим подключиться к БД **postgres**, то имя сервиса, например, **postgres**. Указываем `host="postgres"`, docker дальше сам всё сделает.

## Полезные команды

### Запустить в фоновом режиме с указанием пути до compose-файла

```bash
docker compose -f ./compose.yml up --build -d
```

## Контекст для сервисов
Контекст для каждого сервиса указывается в разделе **build**.

```yml
services: 
  app: 
	build: 
	  context: ./app 
	  dockerfile: Dockerfile
```

## Volumes
 Докер будет сам где-то хранить эти волюмы, сам выберет имя и место для них на случай, когда не нужно содержимое этих директорий, но нужно их пошарить между контейнерами

```yml
volumes:
  static_volume:
  media_volume:
```

## Сети
```yml
networks:				
  default:
    name: webnet
    driver: bridge
```

## Переменные окружения

Переменные окружения будут браться из файла `.env`, который располагается по тому же пути, что и файл `docker-compose.yml`:
```yml
environment:
  - NGINX_PORT=80
  - NGINX_USER=${user} # берется из файла .env
  - NGINX_HOST=myhost
```

## Healthcheck

```yml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U username"]
  interval: 30s
  timeout: 10s
  retries: 5
```