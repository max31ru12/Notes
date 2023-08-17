# Интерпретатор попытается выполнить код в блоке try
try:
    a = 7 / 0
# Если в блоке try возникает исключение, то выполняетм код в блоке except
except:
    print('Ошибка, деление на ноль')


# PEP 8 указывает, что желательно указывать тип исключения
try:
    b = 7 / 0
except ZeroDivisionError:
    print('Ошибка! Деление на ноль')


# Перехват абсолютно все исключений
try:
    c = 7 / 0
except Exception:
    print('Любая ошибка!')


# AS - сохраняет ошибку в переменную
try:
    file = open('dile.txt', 'r+', encoding='utf-8')
except Exception as e:
    print(e)


try:
    d = 7 / 2
except ZeroDivisionError:
    print("Нельзя делить на ноль")
else:
    print("Все норм")


# Несколько блоков except

try:
    q = float(input())
    w = float(input())
    r = q / w
except ZeroDivisionError:
    print("Ошибка деления на ноль")
except ValueError:
    print("Неверно введено число")
else:
    print(f"r = {r}")


