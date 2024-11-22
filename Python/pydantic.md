



        МЕТОДЫ МОДЕЛИ (например, user)

# рекурсивно создает словари вложенных моделей (.dict() так не может)
user.model_dump()           - создает словарь полей и значений модели
user.model_copy()           - создает неглубокую копию модели
user.model_dump_json()      - создает JSON-строку модели

# не думаю, что пригодится
user.model_extra            - возвращает словаарь доплнительных полей
user.model_fields_set       - возвращает множество имен полей модели

# чуть более подробное описание полей
user.model_fields           - возвращает множество имен полей модели


        ВАЛИДАЦИЯ ДАННЫХ ИЗ ORM И СВОИХ КЛАССОВ

# В своей модели UserSchema можно приписать такую вещь:
model_config = ConfigDict(from_attributes=True)

# тогда можно создать объект с помощью ORM:
user_orm = UserTable(**kwargs)

# а затем передать этот объект в свою Pydantic-модель:
validated_user = UserSchema.model_validate(user_orm)


        ПОЛЯ МОДЕЛЕЙ

# Базовое поле и его параметры
Field(default="John Doe",				- дефолтное значение
      default_factory=lambda: uuid4().hexб,		- дефолтное значение - результат вызова Callable (uuid4().hex)
      alias='foo',					- alias для поля
      gt, lt, ge, le					- и так понятно 		ЧИСЛОВЫЕ ОГРАНИЧЕНИЯ
      
      min_length, max_length,				- понятно			СТРОКОВЫЕ ОГРАНИЧЕНИЯ
      pattern)						- ругулярка			СТРОКОВЫЕ ОГРАНИЧЕНИЯ
      

Остальные ограничения для разных типов - https://docs.pydantic.dev/latest/concepts/fields/







