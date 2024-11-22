
```yml
version: '3.8'

services:
  postgres:
    image: postgres:latest
    environment:
      - POSTGRES_DB=fast_api
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=test
    volumes:
      - ./sql:/docker-entrypoint-initdb.d/
    ports:
      - "5433:5432"
    networks:
      - default


networks:
  default:
    driver: bridge
```

#### Подключиться к БД с хоста:
```bash
psql -h localhost -p 5433 -U postgres_user -d postgres_db
```
