from pika import BlockingConnection, ConnectionParameters
from pika.exchange_type import ExchangeType
import sys, os

def main():
    # создаём подключение
    connection = BlockingConnection(ConnectionParameters(host='localhost'))
    # создаём канал
    channel = connection.channel()

    # создаём обменник
    channel.exchange_declare('new_exchange', ExchangeType.direct)

    # определяем очередь
    queue = channel.queue_declare(queue='new_queue')

    # привязываем очередь к обменнику
    channel.queue_bind(exchange='new_exchange', queue='new_queue', routing_key='key')

    # функция, которая вызывается при получении сообщения
    def handle(ch, method, properties, body):
        print(f"Получено сообщение: {body}")

    # привязываем callback-функцию и очередь
    channel.basic_consume(queue='new_queue', on_message_callback=handle, auto_ack=True)

    print('Ожидание сообщения. Чтобы завершить работу приложения, нажмите ctrl+c')
    channel.start_consuming()


if __name__ == '__main__':
    main()
