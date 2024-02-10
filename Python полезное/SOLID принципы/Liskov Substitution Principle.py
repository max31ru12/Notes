# Дочерний класс не замещает поведение базового, а дополняет его


# Выносим специфичные методы для конкретных БД в отдельные классы
# В родительском классе остаются только общие методы


# Неправильный подход
class Database:

    def write(self):
        pass

    def read(self):
        pass

    def join_tables(self):
        pass


class SQLDatabases(Database):

    # имеем все методы родительского класса, все работает правильно
    pass


class MongoDB(Database):
    # У Mongo нет таблиц, поэтому метод join_table сломается, переопределяя его мы нарушаем LSP
    def join_tables(self):
        return "У MongoDB нет таблиц"


# Правильный подход
class DB:

    def write(self):
        pass

    def read(self):
        pass


class SQLDB(DB):
    # Расширяем класс, чтобы работать с таблицами только там, где они есть
    def join_tables(self):
        pass


# Используем весь функционал родительского класса без ошибок
class Mongo(DB):
    # метод для работы только с MongoDB
    def create_collection(self):
        pass
