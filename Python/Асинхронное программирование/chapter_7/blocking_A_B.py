from threading import Lock, Thread
import time

# Взаимоблокировка
lock_a = Lock()
lock_b = Lock()


def a():
    with lock_a:
        print("Захвачена блокировка a из метода а!")
        time.sleep(1)
        with lock_b:
            print("Захвачены обе блокировки из метода а!!")


def b():
    with lock_b:
        print("Захвачена блокировка b из метода b!")
        with lock_b:
            print("Захвачены обе блокировки из метода b!!")


# Поток 1 захватывает блокировку a, затем спит 1 секунду, и в это время поток 2 захватывает блоиковку b
# Затем поток 1 пытается захватить блокировку b, но она уже захвачена потоком 2
# В это же время поток 2 пытается захватить блокировку а, но она захвачена потоком b
thread_1 = Thread(target=a)
thread_2 = Thread(target=b)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
