
## 1 to Many

### User

```python
if TYPE_CHECKING:
	from .post import Post

class User(Base):
	posts: Mapped[list["Post"]] = relationship(back_populates="user")
```

### Post

```python
from typing import TYPE_CHECKING

# Если идет проверка типов, а не выполенение кода, то импортируем User
# надо для relationship, чтобы исключить циклические импорты
if TYPE_CHECKING:
	from .user import User


class Post(Base):
	__tablename__ = "..."

	user_id: Mapped[int] = mapped_column(
		ForeignKey("users.id"),
	)
	
	user: Mapped["User"] = relationship(back_populates="posts")
```

`"users.id"` - название таблицы. Можно сослаться на модель `User.id`, но тогда может быть циклический импорт
`back_populates` - с `User` можем обратиться к `posts`, чтобы получить все связанные с юзером поля 


Добавление `relashionship` не меняет состояние БД, а значит, что не надо проводить миграции



## 1 to 1 

```python





```



[Видео по связям в SQLAchemy](https://www.youtube.com/watch?v=kFp9fdv9i_I&list=PLN0sMOjX-lm5Pz5EeX1rb3yilzMNT6qLM&index=10)

## Lazy Load (N + 1 Problem)

Получим записи из таблицы `A`. Пройдемся по полученным записям циклом и для каждой из них делаем отдельный запрос в таблицу `B`, чтобы получить связанные записи из таблицы B для полученных записей из таблицы `A`. 

В результате получается `1 запрос` для таблицы `A` = `N записей` и `N запросов` для таблицы `B` (по одному запросу для каждой полученной записи из таблицы `A`)


[Calculate timestamps within your DB, not your client
For sanity, you probably want to have all datetimes calculated by your DB server, rather than the application server. Calculating the timestamp in the application can lead to problems because network latency is variable, clients experience slightly different clock drift, and different programming languages occasionally calculate time slightly differently.

SQLAlchemy allows you to do this by passing func.now() or func.current_timestamp() (they are aliases of each other) which tells the DB to calculate the timestamp itself.

Use SQLALchemy's server_default
Additionally, for a default where you're already telling the DB to calculate the value, it's generally better to use server_default instead of default. This tells SQLAlchemy to pass the default value as part of the CREATE TABLE statement.

For example, if you write an ad hoc script against this table, using server_default means you won't need to worry about manually adding a timestamp call to your script--the database will set it automatically.

### [Understanding SQLAlchemy's onupdate/server_onupdate](https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime)
