

## Начальный SQL-запрос

```postgresql
WITH helper2 AS (
	SELECT *, compensation-avg_workload_compensation AS compensation_diff
	FROM (
		SELECT 
			w.id,
			w.username,
			r.compensation,
			r.workload,
			avg(r.compensation) OVER (PARTITION BY workload)::int AS avg_workload_compensation 
			FROM resumes r
			JOIN workers w ON r.worker_id = w.id) helper1
)

SELECT * FROM helper2
ORDER BY compensation_diff DESC;
```


## Alias для таблицы 

```python
from sqlalchemy.orm import aliased

# таблицы Resumes и Workers
r = aliased(Resumes)
w = aliased(Workers) 
```


### Запрос

```python
subq = (
	select(
		r,
		w,
		func.avg(r.compensation).over(partition_by=r.workload.cast(Integer).label("avg_workload_compensation"))
	)
	.select_from
)
```





## Join'ы

По дефолту применяется `INNER JOIN` 

Примеры для таблиц `User` и `Address`

### Inner Join

Возвращает только те строки, где есть совпадение в обеих таблицах

> Сами по себе JOIN'ы не решают N+1 проблему. Они просто позволяют применять условия условия фильтрации, агрегации и прочее. N+1 проблему решают 
> 

- `selectinload()` - самый оптимальный,
- `joinedload()` - может раздуть результат
- `subqueryload()` - использует **SUBQUERY** вместо **IN**
- `contains_eager()` - ручной контроль, используется в сочетании с обычными join'ами

```python
# Просто получаем юзера
select(User).join(Address)  

# Получаем список кортежей (User, Address)
select(User, Address).join(Address)

# Join condition
select(User, Address).join(Address, User.id == Address.user_id)
```

#### Инверсия inner join

```python
select(User, Address).join(Address, full=True).filter(User.address == None, Address.user_id == None)
```


#### Две модели в select

**Join** != выбор данных. То есть если мы запросили только `User`  и сделал join на `Address`, то join выполнится, но вернуться только полям модели `User`. Чтобы получить обе сущности, надо явно их указать:

```python
select(User, Address).join(Address)
```


### Left Outer Join

Возвращает все строки из левой таблицы, даже если справа нет совпадений


```python
# Первый вариант
select(User).outerjoin(Address)

# Второй вариант
select(User).join(Address, isouter=True) 
```

#### User with no address

```python
select(User).outerjoin(Address).filter(User.address == None) # 1 to 1

select(User).outerjoin(Address).filter(~User.address.any()) # 1 to M | M to M

~User.address.any() - пользователи, у которых есть адрес
```

### Right Outer Join

В алхимии нет прямой поддержки `RIGHT OUTER JOIN`


```python
select(Address).outerjoin(User)
```


### Full Join

```python
# left join
left_join = select(User, Address).outerjoin(Address)

# Right join
right_join = select(Address, User).outerjoin(User)

# Full join
full_outer_join = left_join.union(right_join)
```



## Selectinload

Подгружает связанные объекты отдельным дополнительным запросом через `IN (...)`.

То есть сначала ORM получает основные сущности, а потом одним или несколькими отдельными запросами достаёт связанные записи для всех найденных объектов.

Обычно хорошо подходит для `one-to-many` и `many-to-many`, когда `joinedload` может сильно раздувать результирующую выборку.

### Плюсы

- не размножает строки основной выборки
- часто лучше работает на коллекциях
- обычно не требует `unique()`

### Минусы

- делает не один SQL-запрос, а несколько
- при очень маленьких выборках может быть менее выгоден, чем `joinedload`

### Пример использования

```python
result = await session.execute(
    select(User).options(selectinload(User.posts))
)

users = result.scalars().all()

for user in users:
    user_posts = user.posts
```

## Joinedload

Подгружает связанные объекты через `JOIN` в рамках того же SQL-запроса.

То есть основная сущность и связанные данные вытаскиваются сразу одной SQL-командой.

Обычно хорошо подходит для `many-to-one` и `one-to-one`, а также для небольших коллекций, если ты понимаешь, что раздувание выборки будет некритичным.

### Плюсы

- всё загружается одним запросом
- удобно, когда связей немного
- часто хорошо подходит для одиночных связанных объектов

### Минусы

- при `one-to-many` и `many-to-many` размножает строки результата
- может сильно увеличить объём выборки
- для коллекций обычно нужно использовать `unique()`

### Пример использования

```python
result = await session.execute(  
    select(User).options(joinedload(User.posts))  
)  
  
users = result.scalars().unique().all()  
  
for user in users:  
    user_posts = user.posts
```

Необходимо использовать `unique()`, так как `joinedload` размножает строки в выборке.


#### Раздувка результата


##### Почему `joinedload` раздувает результат

`joinedload` делает `JOIN` между основной таблицей и связанной таблицей.

Если у одной основной сущности несколько связанных записей, то в SQL-результате основная строка повторяется несколько раз — по одной строке на каждую связанную запись.

Именно это и называют “раздуванием результата”.

---

##### Пример

Пусть есть таблицы:

### `users`

| id | name   |
|----|--------|
| 1  | Alice  |
| 2  | Bob    |

### `posts`

| id | user_id | title      |
|----|---------|------------|
| 10 | 1       | Post A1    |
| 11 | 1       | Post A2    |
| 12 | 1       | Post A3    |
| 13 | 2       | Post B1    |

---

##### Что происходит при `joinedload(User.posts)`

Пример ORM-запроса:

```python
result = await session.execute(
    select(User).options(joinedload(User.posts))
)

users = result.scalars().unique().all()


С точки зрения Python-объектов ты хочешь получить:

- одного `User(id=1)` с тремя постами
- одного `User(id=2)` с одним постом

Но из SQL пришло **4 строки**, и `Alice` повторилась 3 раза.
```

```sql
SELECT
    users.id,
    users.name,
    posts.id,
    posts.user_id,
    posts.title
FROM users
LEFT OUTER JOIN posts ON users.id = posts.user_id;
```

##### Результат SQL-запроса

|users.id|users.name|posts.id|posts.user_id|posts.title|
|---|---|---|---|---|
|1|Alice|10|1|Post A1|
|1|Alice|11|1|Post A2|
|1|Alice|12|1|Post A3|
|2|Bob|13|2|Post B1|
