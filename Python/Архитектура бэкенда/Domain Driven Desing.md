
DDD про разделение логических компонентов на несколько слоев:

1. Presentation - API шлюз приложения
2. Application - Оснновная сложная бизнес-логика
3. Domain - единицы бизнес-логики
4. Infrastructure - 

![[Pasted image 20250102205530.png]]

## Домены

Домены строятся на сущностях из реального мира и ложатся в центр приложения. Домен определяет реализацию БД

![[Pasted image 20250102211444.png]]

### Repository и Unit of Work

#### Repository для моделей

```python
class AbstractRepository(ABC):
    """
    Interface for any repository, which would be used for work with domain model, according DDD.

    Main purpose is to encapsulate internal logic that is associated with the use of one or another data
    storage scheme, for example, ORM.
    """

    @abstractmethod
    async def add(self, model: AbstractModel) -> AbstractModel:
        raise NotImplementedError

    @abstractmethod
    async def get(self, id: int) -> Optional[AbstractModel]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, id: int, model: AbstractModel) -> AbstractModel:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    async def list(self) -> List[AbstractModel]:
        raise NotImplementedError
```


### Пример DDD + Чистая архитектура = 2 Бизнес модели `Author` и `Post`

![[Pasted image 20250102222356.png]]



