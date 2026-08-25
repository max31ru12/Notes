
## Работа с LLM

### Модель Ollama

```bash
docker pull ollama/ollama

# Создать volume для моделей
docker volume create ollama

# Запустить контейнер
docker run -d --name ollama -p 11434:11434 -v ollama:/root/.ollama ollama/ollama

# Скачать модель
docker exec -it ollama ollama pull qwen3:4b

# Просмотреть скачанные модели
docker exec -it ollama ollama list

# Запустить чат
ollama run qwen3:4b
```

volume нужен для того, чтобы скачанные модели не удалялись при дропе контейнера

#### Конфиг Docker compose 

Запуск Ollama на CPU

```yml
services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    restart: unless-stopped

volumes:
  ollama_data:
```

##### Скачать модель

```shell
docker compose exec ollama ollama pull qwen3:4b
```

##### Посмотреть скачанные модели

```shell
docker compose exec ollama ollama list
```

##### Запустить интерактивный чат

```shell
docker compose exec ollama ollama run qwen3:4b
```

##### Проверить API

```shell
curl http://localhost:11434/api/tags
```

