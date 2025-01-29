# Managers



```python
from django.bd import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1)


class Model(models.Model):
    ...
    # объявляем менеджер
    published = PublishedManager()
    objects = models.Manager()     
```

>Простое подключение своего кастомного менеджера убирает возможность пользоваться менеджером `objects`, он просто перестает существовать. Для решения этой проблемы необходимо явно подключить дефолтный менеджер:

```py
objects = models.Manager()
```

То, что вернет метод `get_queryset`, то и буедт возвращать менеджер `PublishedManager`