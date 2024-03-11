from multiprocessing import Pool, cpu_count


def say_hello(name: str):
    return f"Привет, {name}"


if __name__ == "__main__":
    with Pool() as process_pool:
        # apply блокирует выполнение
        # hi_jeff = process_pool.apply(say_hello, args=("jeff", ))
        # hi_john = process_pool.apply(say_hello, args=("john", ))

        # print(hi_jeff)
        # print(hi_john)

        # выполняются конкурентно
        hi_jeff = process_pool.apply_async(say_hello, args=("jeff", ))
        hi_john = process_pool.apply_async(say_hello, args=("john", ))

        # .get() блокирует выполнение
        # результаты функция получаются синхронно
        print(hi_jeff.get())
        print(hi_john.get())
