# Индексы Django

```py
class Model(...):
    ...
    class Meta:
        indexes = [
            models.index(fields=["last_name", "first_name"]),
            models.Index(fields=["first_name"], name="first_name_index")
        ]
```