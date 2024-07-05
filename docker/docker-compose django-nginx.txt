# docker compose run python manage.py migrate - вручную необходимо произвести миграции	

version: "3.8"

services:
  django:
    build: .
    command: sh -c "gunicorn --bind 0.0.0.0:8000 MorphViewBlog.wsgi" 		# это для запуска с помощью gunicorn (для nginx)
#    command: python manage.py runserver 0.0.0.0:8000 				# это бля локального запуска без nginx
    environment:
      - SECRET_KEY=${SECRET_KEY}
      - DEBUG=${DEBUG}
      - DB_NAME=${DB_NAME}
      - DB_USER=${DB_USER}
      - DB_PASSWORD=${DB_PASSWORD}
      - DB_HOST=${DB_HOST}
      - DB_PORT=${DB_PORT}
      - REDIS_PASSWORD=${REDIS_PASSWORD}
      - REDIS_HOST=${REDIS_HOST}
      - EMAIL_HOST_USER=${EMAIL_HOST_USER}
      - EMAIL_HOST_PASSWORD=${EMAIL_HOST_PASSWORD}
    expose:
      - 8000
    ports:
      - "8000:8000"
    depends_on:
      - postgres
      - redis
    networks:
      - default

  nginx:
    image: nginx
    depends_on:
      - django
    ports:
      - "80:80"
    volumes:
      - ./nginx-conf-d/nginx.conf:/etc/nginx/conf.d/default.conf:ro	# пробрасываем файл-конфигурацию
      - ./MorphViewBlog/static/:/var/www/html/static/			# пробрасываем статику


networks:
  default:
    driver: bridge