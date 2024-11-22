from multiprocessing import Process, Value


def increment_value(shared_int: Value):
    # Блокируем процесс
    shared_int.get_lock().acquire()
    shared_int.value = shared_int.value + 1
    # Освобождаем процесс
    shared_int.get_lock().release()


# Применение блокировок, чтобы избежать состояние гонки
if __name__ == "__main__":
    # 2 операции блокировки: ЗАХВАТ и ОСВОБОЖДЕНИЕ
    for _ in range(100):
        integer = Value('i', 0)
        procs = [Process(target=increment_value, args=(integer, )),
                 Process(target=increment_value, args=(integer, ))]

        [p.start() for p in procs]
        [p.join() for p in procs]

        print(integer.value)
        assert (integer.value == 2)
