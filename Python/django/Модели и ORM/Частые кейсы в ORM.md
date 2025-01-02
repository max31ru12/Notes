

## Получить список из `QuerySet'а`:

```python
object_ids = Model.objects.all().values_list("id", flat=True)
```

если не указывать `flat=True`, то будет **QuerySet** вида: `QuerySet[(1, ), (2, ), ...]`

## Исключить из выборки по параметру


