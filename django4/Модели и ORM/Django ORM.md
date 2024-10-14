# Django ORM

## Создание объекта

### 1 вариант

Создать объект и сразу добавить в БД

```py
Model.objects.create()
```

### 2 вариант

```py
w1 = Model(**data) # создать объект
w1.save() # добавить объект в БД
```


## Обновление объекта

Метод `update` сразу изменяет состояние БД

```py
Model.objects.update(name="New value")  # для всех объектов

Model.objects.filter(pk__lte=4)  # для первых четырех записей
```

`update` не работает для срезов типа: 
```py
Model.objects.all()[:4].update  # Error
```


## Удаление записей

```py
Model.objects.filter(pk__gte=5).delete()  # Удаление записей
```


## Выборка записей

Выборка записей таким образом возвращает `QuerySet`

```py
Model.objects.all() # выбрать все записи

Model.objects.all()[1] # Выбрать вторую запись 

Model.objects.all[1:4] # Срез
```

### Фильтрация записей

`.filter()` всегда возвращает `list`

```py
Model.objects.filter(**kwargs) # фильтрация по именованным параметрам
```

#### __lookup'ы:

Пример использования:

```py
Model.objects.filter(name__contains="Max")
```

- `__gte`
- `__gt`
- `__lte`
- `__lt`
- `__contains` - вхождние в поле
- `__icontains` - вхождение без учета регистра
- `__in` - если попадает в список

#### Выбрать одну запись

```py
Models.objects.get(**filters) # выбирает одну запись или генерит исключение
```

#### Исключить записи из полной выборки

```py
Model.objects.exclude(**filter)
```


### Сортировка записей

```py
Model.objects.all().order_by("field_name")
# Второй вариант
Model.objects.order_by("field_name")
```

#### Сортировка наоборот:

```py
Model.objects.order_by("-title")
```

Можно сначала отфильтровать, а затем отсортировать:

```py
Model.objects.filter(pk__gte=2).order_by("id")
```

#### Сортировка по умолчанию (в модели)

```py
class Model(...):
    ...
    class Meta:
        ordering = ["-id", "title"]
```


## Связанные модели

```py
class Category(models.Model):
    ...

class Women(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="posts")

```

### Выбрать связанную с записью в `Women` категорию

```py
Women.objects.get(pk=1).cat  # Дополнительный SQL-запрос
```

### Выбрать связанные с записью в `Category` записи из `Women`

```py
# Без указания related_name в поле ForeignKey
Category.objects.get(pk=1).women_set.all()

# Если указан related_name
Category.objects.get(pk=1).posts.all()
```

> В данном случае `women_set` и `posts` - это **менеджеры**





