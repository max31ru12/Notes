from pika import BlockingConnection, ConnectionParameters
from pika.exchange_type import ExchangeType

# Создаем подключение
connection = BlockingConnection(ConnectionParameters('localhost'))

# Создаем канал
channel = connection.channel()

# Создаем обменник
channel.exchange_declare("new_exchange", ExchangeType.direct)

# Определяем очередь
queue = channel.queue_declare(queue="new_queue")

# Привязывает очередь к обменнику
channel.queue_bind(exchange="new_exchange", queue="new_queue", routing_key="key")

# Публикуем сообщение
channel.basic_publish(exchange="new_exchange", routing_key="key", body=b"Hello, world!")

connection.close()


