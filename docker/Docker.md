## Команды docker:


- `docker ps` 			                     -посмотреть запущенные контейнеры
- `docker stop id` 			            -остановить контейнер с указанным id
- `docker images` 			            -посмотреть образы
- `docker ps -a`  			            -посмотреть абсолютно все контейнеры
- `docker rm id` 			                    -удалить контейнер с указанным id
- `docker rmi id` 			            -удалить образ с указанным id
- `docker pull nginx`		                    -скачать образ
- `docker exec -it id bash`		    -запустить файловую систему контейнера в bash


## ЗАПУСТИТЬ ОБРАЗ:

```shell
docker run -d -p 443:80 image-name
```

`443` - порт на хосте;
`80` - порт в контейнере


```shell
docker run -it --rm -v testdata:/data busybox
```

- `busybox` - имя образа

- `it` - t - многоцветная консоль, i - интерактивный режим (если не указывать, то контейнер не реагирует на Ctrl + C)

- `v` - volumes

- `d` - запустить в фоновом режиме

- `--`name "container_name"

- `testdata` - том на компе

- `data` - куда будет примонтирован в контейнере

- `rm` - удалить при остановке

## ПРОКИНУТЬ ПЕРМЕННЫЕ ОКРУЖЕНИЯ (в docker run):

```shell
--env "DB_LINK=env_variable" 
```

`DB_LINK` - имя переменной \
`env_variable` - значение перменной

> если несколько перменных, то несколько опций `--env`


## СОЗДАТЬ ОБРАЗ:
```shell
docker build -t name:v1 dockerfile-dir-path
```

`name:v1` - задать имя образа и версию \
`dockerfile-dir-path` - абсолютный путь до dockerfile'a

- `-t` - хотим указать тег для нашего image'а

- `-f` - если не указываем, то ищется только файл с именем Dockerfile,
     если указывает

`PAUSE` и `UNPAUSE` сохраняют состояние контейнера:
```shell
docker pause/unpause container_name
```

### Еще интересные команды:

```shell
docker create ... (дальше все так же)
```

#### Запустить созданный контейнер
```shell
docker start container_name
``` 	

- `-a` - сразу зайти в контейнер

#### Убить контейнер (можно передать сигнал)

```shell
docker kill container_name	
```


# Описание команд Dockerfile:

`RUN` - команда запускается во время build'а образа

`WORKDIR` - устанавливает рабочую директорию (дальше команды будут выполняться из этой рабочей директории)

`CMD` - выполнение консольной команды при запуске контейнера принято писать как `["python3", "main.py", "--host", "0.0.0.0"]`, но можно просто `python3 main py "--host", "0.0.0.0"` нужно указывать, чтобы был доступен `localhost` контейнера  хоста

`ENTRYPOINT` - точка входа приложения (например, uvicorn или python3), а параметры берутся из, например, 
CMD ["main.py"]

`EXPOSE` - открываем порт контейнера (по сути просто документирует порт для открытия)

`ENV DB_NAME "defalut-db-name-value"`



# ПРО КЭШИРОВАНИЕ В DOCKER

Можно отдельно установить зависимости, чтобы сделать их отдельным кэшем
Тогда при повторном билде зависимости не будут заново устанавливаться:

```dockerfile
COPY requirements.txt requirements.txt
RUN pip install --no cache-dir -r requirements.txt
```

`--no-cahe-dir` - не используем директории для кэша внутри контейнера, потому что они не используюся, а просто теряются

#### Отдельно копируем свой код, чтобы у кода был отдельный кэш

```dockerfile
COPY your_project your_project
```

Dockerfile:


```dockerfile
FROM ubuntu:latest			    # образ:версия

MAINTAINER				    # создатель (необязательно)

RUN apt-get update -qy			    # выполнить команду при запуске

COPY ./откуда ./куда			    # скопировать паппку с компа в контейнер

WORKDIR dir_name			    # рабочая папка в контейнере

ENV request_delay=10000			    # переменные окружения

RUN pip intall -r requirements.txt          # установка зависимостей

CMD ["python3", "manage.py"]		    # выполнить команду из папки WORKDIR

VOLUME какие-то параметры		    # волюмы (разобраться)

EXPOSE 80				    # открыть 80 порт контейнера

```


# Docker-Compose

## Внешняя есть для сервисов из разных Compose-файлов

```yaml
networks:
  default:
    external:
      name: interservice-network
```

Эта сеть не под управлением `Docker-Compose`, поэтому надо создавать вручную:

```shell
docker network create inserservice-network
```

Такая сеть позволяет объединить сервисы из разных docker-compose файлов.







