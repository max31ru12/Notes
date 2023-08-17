# Объявляем имя функции, которая принимает аргумент
def benchmark(iters):
    # Сам декоратор, который принимает на вход функцию
    # Декоратор возвращает функцию
    def actual_decoraror(func):
        import time

        # Это обертка функции, тут выполняются все дополнительные действия
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                # тут вызывается функция, которая обертывается декоратором
                func(*args, **kwargs)
                end = time.time()
                total = total + (end-start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total/iters))
        # Функция-декоратор возвращает функцию
        return wrapper
    # Функция, принимающая аргументы, возвращает сам декоратор
    return actual_decoraror


# Обертываем функцию в декоратор (Вывывается функция benchmark(10), в ней происходит декорирование)
@benchmark(10)
def ag_and_kwg(*args, **kwargs):
    print('Работает оригинальная функция')
    for number in args:
        print(number)

    for key, value in kwargs.items():
        print('{} : {}'.format(key, value))
    print('Оригинальная функция отработала')
    print()


ag_and_kwg(1, 2, 3, 4, 5, key_1='hello', key_2='Andrew')
