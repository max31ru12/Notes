

#### Пример использования Subquery

```python
recent_books = Book.objects.filter(published_data__gte=last_year)

authors_with_recent_books = Author.objects.filter(												id__in=Subquery(recent_books.values("author_id"))
)
```

Эквивалент без `Subquery`:

```python
recent_books = Book.objects.filter(published_data__gte=last_year)
author_ids = [book.author_id for book in recent_books]
authors_with_recent_books = Author.objects.filter(id__in=authors_ids)
```


## OuterRef

Позволяет ссылкаться на значение из внешнего запроса внутри подзапроса. Нужно использовать тогда, когда необходимо выполнить фильтрацию или `lookups`, основанные на значениях из внешнего запроса