REDIS:

ТИПЫ ДАННЫХ: strings, sets (set), hashes (dict), Lists (list)

		Основные команды:

SET car Ferrari 	- записать ключ со значением 'Ferrari'
GET car			- выбрать все данные из ключа car
GET bike 		- получить несуществующий ключ (результат: 'nil')
DEL car			- кдалить ключ car

KEYS * 			- вывести все ключи

EXPIRE timer 30		- задать время на удаления ключа (в секундах)
TTL timer		- посмотреть оставшееся время жизни ключа

SET my-cache Max EX 10	- создать ключ со значением Max и временем жизни 10 секунд


		Как работать с LISTS

SADD fruits apple 		- создать набор fruits с элементом apple [apple, ]
SADD fruits banana lime		- добавить в набор значения [apple, banana, lime]
SMEMBERS fruits			- посмотреть набор
SREM fruits banana		- удалить из набора fruits элемент со значением banana



		Redis в Docker

docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest

docker exec -it container_name redis-cli -a пароль

		Redis в Python

pip install redis

redis_client = redis.Redis(host=, port=, db=0, password)

# *db - метод разделения (для удобства), всего есть 16 db

redis_client.close() # обязательно закрываем

# Команды абсолютно такие же
redis_client.set()
redis_client.get()
redis_client.delete()
redis_client.expire()

Примеры команд:
redis_client.set(name="test_key", value=10)
redis_client.get("test_key") # получаем байты (b'10')


		Docker-Compose

  redis:
    image: redis:latest
    restart: always
    entrypoint: redis-server --appendonly yes --requirepass ${REDIS_PASSWORD} --maxmemory 256mb --maxmemory-policy allkeys-lru
    ports:
      - "6379:6379"
    volumes:
      - /redis/appdata/redis/data:/data
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    networks:
      - default

