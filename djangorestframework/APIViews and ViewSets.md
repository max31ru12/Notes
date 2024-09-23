# APIViews and ViewSets 

APIViews - это

ViewSets - это

## [Создание эндпоинтов с помощью функций](https://www.django-rest-framework.org/api-guide/views/#function-based-views)

```py
@api_view(methdos=["GET", "POST"])
def list_smth(request):
    return Response(data=[1, 2, 3])
```

Также можно сделать метод и подвязать его к классу, про это можно прочитать по ссылке

# APIViews

## Class-based views

```py
class SnippetList(APIView):

    def get(self, request):
        return Response(...)

    def post(self, request):
        return Response(...)
```

### Миксины

- `CreateModelMixin` - реализует метод `.create()`, 
- `ListModelMixin` - реализует метод `.list()`
- `DestroymodelMixin` - реализует метод `.destroy()`

**Как использовать миксины:**

```py
class SnippetList(GenericAPIView,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  ):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwags)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

## [Generic API Views](https://www.django-rest-framework.org/api-guide/generic-views/)

Позволяют наследоваться от классов и реализовать различные методы путем наследования

### Методы и атрибуты Generic APi Views

#### Атрибуты

- `queryset` - возвращает объекты из View можно использовать `.get_queryset()`
- `serializer_class` - класс сериалайзера
- `lookup_field` - поиск по полю из одного объекта
- `lookup_url_kwarg` - поиск по полям (если предыдущий атрибут не выставлен)
- `pagination_class` - класс пагинатора
- `filter_backends` - список (list) классов-фильтров, которые фильтруют **queryset** 

#### Методы

- `.get_queryset()` - возвращает **queryset**, нужно использовать вместо обращения к **self.queryset**
- `.get_object()` - возвращет объект для **detail_view**, по дефолту использует **lookup_field**
- `.filter_queryset()` - возвращает **queryset**, отфильрованный с помощью **filter_backends**
- `.get_serializer_class()` - возвращает сериалайзер


# ViewSets

**ViewSets** не реализуют методы `.get()`, `.post()` и тд. Вместо них **ViewSets** сразу реализуют методы: 
- `.list()`
- `.create()` 
- `.destroy()`
- `.update()`
- `.partial_update()`
- `.retrieve()`

