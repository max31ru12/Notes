

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