def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        print('В аргумент args передалось: {}'.format(args))
        print('В аргумент kwargs передалось: {}'.format(kwargs))
        end = time.time()
        print('Время выполнения функции: {} секунд'.format(end - start))
        return return_value

    return wrapper


@benchmark
def some_func(*args, **kwargs):
    print('Данная функция выводит такой-то результат {}')
    print(args)
    print(kwargs)
    for key, value in kwargs.items():
        print(key, ' : ', value)

some_func(1234, 1234, 4321, 4321, kwargs_1='hello', kwargs_2='goodbye')
