# Самостоятельный вызов исключений

min = 100

try:
    if min > 10:
        raise Exception('min must be less than 10')
except Exception:
    print('Моя ошибка')
    raise



