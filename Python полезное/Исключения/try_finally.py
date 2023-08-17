# код в блоке finally выполняется в любом случае
# file = open('file.txt', 'w+', encoding='utf-8')
#
# try:
#     lines = file.readlines()
#     print(lines[5])
# finally:
#     file.close()
#     if file.closed:
#         print("Файл закрыт")


# три блока сразу
def summa(a, b):
    res = 0

    try:
        res = a + b
    except TypeError:
        res = int(a) + int(b)
    finally:
        print(f"a = {a}, b = {b}, res = {res}")


summa("1", 2)



