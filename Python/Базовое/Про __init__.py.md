
Есть папка `utils` с файлами `math_util` и `string_util`. Стандартный базовый импорт выглядит так:

```python
from utils.math_util import smth_1
from utils.string_util import smth_2
```


`__init__.py` позволяет сократить эти импорты до:

```python
from utils import stmt_1, smth_2
```

Для этого необходиом в `__init__.py` импортировать эти переменные/функции. 

## `__init__.py`

```python
from .math_util import add
from .string_util import capitalize
```

С такой конфигурацией файла появляется возможность сократить.

Чтобы не возникало проблем с импортами, лучше использовать `relative import` в файле `__init__.py`