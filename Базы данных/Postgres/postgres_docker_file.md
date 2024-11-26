
Где лежат данные БД в контейнере: `/var/lib/postgresql/data`

```yml
version: '3.8'

services:
  postgres:
	container_name: portfolio_db
    image: postgres:latest
    environment:
      - POSTGRES_DB=fast_api
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=test
    volumes:
	  - ./backups:/backups
      - db_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    networks:
      - default
    restart: always # можно использовать unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U username"]
      interval: 30s
      timeout: 10s
      retries: 5

volumes:
  - da_data

networks:
  default:
    driver: bridge
```


`healthcheck` нужен для того, что поменить контейнер, если он не проверяет проверку, указанную в `test`. 

#### Задание переменных окружения с помощью файла `.env`

```yml
environment: 
  POSTGRES_USER: ${POSTGRES_USER} 
  POSTGRES_PASSWORD: ${POSTGRES_PASSWORD} 
  POSTGRES_DB: ${POSTGRES_DB}
```

#### Подключиться к БД с хоста:
```bash
psql -h localhost -p 5432 -U postgres_user -d postgres_db
```


Можно дополнительно задать ресурсы процессора для оптимизации:

```yml
deploy: 
  resources: limits: 
    cpus: "0.5" 
    memory: 512M
```


## Создание бэкапов в Docker Postgres

Более подробно про бэкапы [здесь](./Бэкапы%20и%20дампы%20Postgres.md)

Создание бэкапа внутри директории `backups`

```bash
docker exec postgres pg_dump -U myuser mydatabase > ./backups/backup_$(date +%F).sql
```

Можно создать **cron job** для создания бэкапов с интервалом. 

## Восстановление БД из бэкапа

```bash
 docker exec -i postgres psql -U myuser -d mydatabase < ./backups/backup_YYYY-MM-DD.sql
```

Такое же будет работать с docker compose примерно такими командами:

```bash
docker compose run --rm service_name pd_dump ...
```
