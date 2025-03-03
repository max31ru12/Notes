## Создание объекта

### 1 вариант

Создать объект и сразу добавить в БД

```python
Model.objects.create()
```

### 2 вариант

```python
w1 = Model(**data) # создать объект
w1.save() # добавить объект в БД
```


## Обновление объекта

Метод `update` сразу изменяет состояние БД

```python
Model.objects.update(name="New value")  # для всех объектов

Model.objects.filter(pk__lte=4)  # для первых четырех записей
```

`update` не работает для срезов типа: 

```python
Model.objects.all()[:4].update  # Error
```

## Удаление записей

```python
Model.objects.filter(pk__gte=5).delete()  # Удаление записей
```


## Выборка записей

Выборка записей таким образом возвращает `QuerySet`

```python
Model.objects.all() # выбрать все записи

Model.objects.all()[1] # Выбрать вторую запись 

Model.objects.all()[1:4] # Срез
```

### Фильтрация записей

`.filter()` всегда возвращает **QuerySet** что-то типа `list`

```python
Model.objects.filter(**kwargs) # фильтрация по именованным параметрам
```

#### __lookup'ы:

Пример использования:

```python
Model.objects.filter(name__contains="Max")
```

- `__gte`
- `__gt`
- `__lte`
- `__lt`
- `__contains` - вхождение в поле
- `__icontains` - вхождение без учета регистра
- `__in` - если попадает в список

#### Выбрать одну запись

```python
Models.objects.get(**filters) # выбирает одну запись или генерит исключение
```

#### Исключить записи из полной выборки

```python
Model.objects.exclude(**filter)
```

Причем нет другого способа исключить записи из выборки

### Сортировка записей

```python
Model.objects.all().order_by("field_name")
# Второй вариант
Model.objects.order_by("field_name")
```

#### Сортировка наоборот:

```python
Model.objects.order_by("-title")
```

Можно сначала отфильтровать, а затем отсортировать:

```python
Model.objects.filter(pk__gte=2).order_by("id")
```

#### Сортировка по умолчанию (в модели)

```python
class Model(...):
    ...
    class Meta:
        ordering = ["-id", "title"]
```

### Функции агрегации SUM(), AVG(), COUNT(), MIN(), MAX()

Базовый пример нахождения максимального значения по столбцу:

```python
from django.db.models import Max

Model.objects.aggregate(Max(price))
# или
Model.objects.all().aggregate(Max(price))
```

В результате получится словарь вида:

`{"price__max": 400}`





## Связанные модели

```python
class Category(models.Model):
    ...

class Women(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="posts")

```

### Выбрать связанную с записью в `Women` категорию

```python
Women.objects.get(pk=1).cat  # Дополнительный SQL-запрос
```

### Выбрать связанные с записью в `Category` записи из `Women`

```py
# Без указания related_name в поле ForeignKey
Category.objects.get(pk=1).women_set.all()

# Если указан related_name="posts"
Category.objects.get(pk=1).posts.all()
```

> В данном случае `women_set` и `posts` - это **менеджеры**


## `select_related()`

Извлекает данные связанной модели с помощью `JOIN`

### Standart lookup:

```python
# Hits the database
e = Model.objects.get(id=5)

# Hits the database again
b = e.related_model
```

### `select_related` lookup

`select_related` можно использовать с любой **QuerySet'ом** объектов

```python
# Hits the db
e = Model.objects.select_related("related_model").get(id=5)

# dont hits the db
b = e.related_model
```



## `prefetch_related()`

То же самое, что и `select_related`, но для связи **Many-to-Many** 


Например, есть такие модели:

```python
from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=30)


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    # Этот методе для каждой модели Pizza дергает БД и извлекает связанные модели Topping
    def __str__(self):
        return "%s (%s)" % (
            self.name,
            ", ".join(topping.name for topping in self.toppings.all()),
        )
```


Использование:

```python
Pizza.objects.prefetch_related("toppings")

# затем уже можно работпть с QuerySet'ами, так как данные prefetch_related уже в КЭШе 
...
```

### Пример с несколькими связанными моделями

```python
class Restaurant(models.Model):
    pizzas = models.ManyToManyField(Pizza, related_name="restaurants")
    best_pizza = models.ForeignKey(
        Pizza, related_name="championed_by", on_delete=models.CASCADE
    )
```

Выборка с помощью prefetch_related:

```python
Restaurant.objects.prefetch_related("pizza__toppings")
```

Такой запрос выберет все пиццы, принадлежащие ресторанам и все топпинги, принадлежащие этим пиццам. Причес сделает это в 3 запроса:

- Запрос для `Restaurant`
- Запрос для `Pizza`
- Запрос для `Topping`

> Можно сократить до двух запросов (посмотреть доку)


# Транзакции в Django

> [Документация](https://docs.djangoproject.com/en/5.1/topics/db/transactions/)

### В доке есть:

- обработка ошибок
- выполненией действий после коммита транзакции
- **savepoint** - консистентное состояние перед транзакцией, к которому можно откатиться: `savepoints()`

### Как декоратор

```python
from dajngo.db import transaction

@transcation.atomic
def viewfunc(request):
    # Код происходит внутри транзакции
    do_stuff()
```


### Как контекстный менеджер

```python
from django.db import transaction

def viewfunc(request):
    # Здесь код происходит в режиме АВТО КОММИТА
    do_stuff()
    with transaction.atomic():
        # Этот код выполняется внутри транзакции
        do_stuff_in_transaction()
```



Необходимо вручную возращать поля объекта в момент до выполнянения транзакции, если транзакция не выполнилась:

```python
from django.db import DatabaseError, transaction

obj = MyModel(active=False)
obj.active = True
try:
    with transaction.atomic():
        obj.save()
except DatabaseError:
    obj.active = False

if obj.active:
    ...
```

Это надо делать потому, что транзакция не поменяла состояние БД, но поменяла состояние инстансов моделей, которые пыталась изменить транзакция.

## Использование `F()` - объекта

Позволяет выполнять операции с БД, используя текущие значение полей. Используется тогда, тогда есть риск конфликтов при выполнении параллельных запросов.


## Использование `Q()` - объекта
### Что такое Q

`Q` — это объект, который представляет логическое условие в Django. Он позволяет строить более сложные фильтры с использованием логических операторов, таких как:

- `AND` ( `&` по умолчанию, когда вы используете `filter()`)
- `OR` (используется через `|`, например, `Q(field1=value1) | Q(field2=value2)`)
- `NOT` (используется через `~`, например, `~Q(field1=value1)`)

### Используется:

- Когда  нужно объединять условия с логическими операциями, например, `AND`, `OR` или `NOT`.
- Когда фильтры не могут быть легко записаны с помощью простых аргументов в `filter()` и `exclude()`.
- Когда необходимо динамически строить запросы на основе условий.

