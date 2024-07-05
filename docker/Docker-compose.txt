В качестве хоста в python-программах указываем имя сервиса: То есть, если хотим подключиться к БД postgres, то 
имя сервиса, например, postgres. Указываем host="postgres", docker дальше сам всё сделает.


version: "3.5"				-версия docker-compose

services:				-перечисляем сервисы
  web-server:				-имя сервиса
    image: nginx:latest			-образ
    build: dockerfile_relative_path	-создать образ из докер-файла
    container_name: mynginx   		-имя контейнера
    volumes:				-волюмы
      - /opt/web/html:/var/www/html	-локальная_директория:директория_в_контейнере

    volumes:
      - ..:/code            - грубо говоря, compose берет изменения из директории пониже (или указанной, если указывать)
                            и переносит их в папку code в контейнере (вроде как отслеживает изменения)
      - static_volume:/folder_in_container  - используем общий волюм
    env_file:
      - .env_file_name
    environment:			-переменные окружения
      - NGINX_PORT=80
      - NGINX_USER=${user}		- берется из файла .env
      - NGINX_HOST=myhost		
    ports:				-проброс портов (порт_хоста:порт_контейнера)
      - "80:80"
      - "443:443"
    restart: unless-stopped		-что делать с контейнером при остановке
    depends_on:				-запуск контейнера после запуска перечисленных контейнеров
      - app-db				-имена контейнеров (тоже в файле)
      - postgres

# Докер будет сам где-то хранить эти волюмы, сам выберет имя и место для них 
# на случай, когда не нужно содержимое этих директорий, но нужно их пошарить между контейнерами
volumes:				-объявляем общие волюмы
  static_volume:
  media_volume:



networks:				-Описывает сети
  default				-стандартная сеть для контейнера
    name: webnet
    driver: bridge
  internet:
    name: appnet
    driver: bridge


ПРО ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ

Данная запись значит, что перменные окружения будут браться из файла .env, который располагается
по тому же пути, что и файл docker-compose.yml

    environment:
      - SECRET_KEY=${SECRET_KEY}
      - DEBUG=${DEBUG}
      - DB_NAME=${DB_NAME}


