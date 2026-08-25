
## Client


```python
from qdrant_client import QdrantClient  
  
  
client = QdrantClient(  
    host="localhost",  
    port=6333,  
)
```


## Создание коллекции

```python
client.create_collection(  
    collection_name="documents",  
    vectors_config=VectorParams(  
        size=3,  
        distance=Distance.COSINE,  # сравнивай векторы по cosine similarity  
    )  
)
```

 `size` -  каждый вектор в этой collection должен содержать ровно 3 числа

## Вставка данных в коллекцию

```python
client.upsert(  
    collection_name="documents",  
    points=[  
        PointStruct(  
            id=1,  
            vector=[0.9, 0.1, 0.1],  
            payload={  
                "text": "Python is a programming language"  
            },  
        ),  
        PointStruct(  
            id=2,  
            vector=[0.1, 0.9, 0.1],  
            payload={  
                "text": "Dogs are animals"  
            },  
        ),  
        PointStruct(  
            id=3,  
            vector=[0.85, 0.15, 0.1],  
            payload={  
                "text": "FastAPI is a Python web framework"  
            },  
        ),  
    ]  
)
```


## Поиск ближайших точек

```python
# Поиск ближайших точек  
query_vector = [0.88, 0.12, 0.1]  
  
results = client.query_points(  
    collection_name="documents",  
    query=query_vector,  
    limit=2,  
)  
  
print(results)
```