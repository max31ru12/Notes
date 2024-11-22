# 1 класс = 1 задача (одна зона ответственности)


# Модель данных отдельно от поведения
class User:

    # Аннотация типов
    ID: int
    username: str
    password: str

    def __init__(self, ID, username, passwd):
        self.id = ID
        self.username = username
        self.password = passwd


# Задача - сохранение пользователя в БД
class UserRepo:

    def save(self, user: User):
        # Сохранение юзера в БД
        pass


# Задача - логировапние
class UserLogger:

    def log(self, user: User):
        # логирование
        print(print(user))


# Задача - работа с http
class UserController:

    # Отправляем по Http
    def send_http(self, user: User):
        pass

    # Получаем по Http
    def get_http(self, message, user: User):
        pass
