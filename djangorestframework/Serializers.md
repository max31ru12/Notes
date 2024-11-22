## [Замена днищенской доки для DRF](https://www.cdrf.co/)

## Парс JSON - JSONParser

```py
JSONParser.renser()  # JSON-строка в байтах

JSONparser()  # из JSON-строки в байтах в Python DataTypes
```

## Создание и изменение объектов в сериалайзерах

Методы:

- `create()` - создание инстанса 

```py
def create(self, validated_data):
    return Comment.objects.create(**validated_data)
```

- `update()` - создание и изменение инстанса

```py
def update(self, instance, validated_data):
    ...
    instance.save()
    return instance
```

## Валидация полей при POST-запросах

Валидировать сериалайзер можно с помощью метода: `serializer.is_valid()`

Валидировать поля запроса можно через создание метода validate_<имя валидируемого поля> валидации поля:

```python
def validate_fieldname(self, value):
    if 'django' in value:
        raise serializers.ValidationError("description")
    return value
```

Валидация сразу нескольких полей:

```python
def validate(self, data):
    ...
    return data
```

# ModelSerializer

- автоматически генерит поля для модели
- автоматически генерит валидаторы
- имеет дефолтные методы `.create()` и `.update()`

Все связи мапятся в `PrimaryKeyRelatedField`

**Обратные связи указываются явно!!!**

Выводимые в эндпоинте поля указываются в классе `Meta`:

```python
class SomeSerializer(...):

    class Meta:
        model = Model
        fields = (список атрибутов) или "__all__"
        exclude: (список исключаемых атрибутов)
```

Обязательно необходимо указывать одно из полей: либо `fields`, либо `exclude`

# HyperLinkedModelSerializer

Почти то же самое, что и `ModelSerializer`, только нужен для генерации ссылок на связанные записи

# [Serializers Relations](https://www.django-rest-framework.org/api-guide/relations/)

Поля сериализаторов для связанных моделей и как они отображаются в JSON 


1. SlugRelatedField - выброка из связанной модели любого поля

```python
field = serializers.SlugRelatedField(slug_field="field_name", many=True, read_only=True)
```

`slug_field` - это поле в связанной модели, например, для **DictionarySerializer**:

**Dictionary : Objects === М : 1**

```python
obj_code = serialaizers.SlugRelatedField(slug_field="obj", ...)
```

`obj` - это поле из модели **Objects**

2. PrimaryKeyRelatedField

```python
obj = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
```

