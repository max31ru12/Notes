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