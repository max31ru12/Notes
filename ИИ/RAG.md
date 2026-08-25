

## Основные термины 

1. `Cosine similarity` - способ узнать, насколько похожи два вектора, измеряя косинус угла между ними, игнорируя из длину
2. `batch` - группа объектов, которую модель обрабатывает за один проход
3. `Телеметрия` - это отправка программой служебной информации разработчику

## Создание  Embeddings

### Pipeline

text -> токенизация -> Transformer -> pooling -> [0.12, -0.34, ...]

#### Создание простых embeddings

```python
from sentence_transformers import SentenceTransformer  
  
  
model = SentenceTransformer(
	"sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
	convert_to_tensor=True,  # конвертировать в тензоры
	normalize_embeddings=True,  # делать векторы единичной длины
)  
  
  
text_1 = "Кошка спит на диване"  
text_2 = "Python используется для разработки программ."


embedding_1 = model.encode(text_1)  
embedding_2 = model.encode(text_2)  
  
  
print(f"{embedding_1.shape=}")  # (384,)
print(f"{embedding_2.shape=}")  # (384,)
```


**Embeddings** создаваемые одной моделью имеют одинаковый размер. Это необходимо для того, чтобы вектора находились в одном и том же пространстве. Тогда их сравнение будет являться корректным 

#### Правило:
> Embeddings документов и embedding пользовательского запроса должны быть созданы одной и той же моделью (тогда их можно корректно сравнивать)


#### Повторные embeddings

```python
text = "Кошка спит на диване"

first_embedding = model.encode(text) 
second_embedding = model.encode(text)

# Повторные embeddings совпадают
np.allclose(first_embedding, second_embedding)  # True
```


#### Кодирование списка предложений

```python
texts = [ 
	"Кошка спит на диване.", 
	"Кот отдыхает на софе.", 
	"PostgreSQL — это реляционная база данных.", 
] 

embeddings = model.encode(texts)

embeddings.shape  # (3, 384)
```


#### Batch

```python
texts = [ 
	chunk["content"] for chunk in chunks 
] 

embeddings = model.encode(texts, batch_size=32)
```

Модель будет обрабатывать тексты примерно так:

```
chunks 0–31   → batch 1
chunks 32–63  → batch 2
chunks 64–95  → batch 3
chunks 96–99  → batch 4
```


### Cosine Similarity

способ узнать, насколько похожи два вектора, измеряя косинус угла между ними, игнорируя из длину (значение между `-1` и `1`, `1` - полное совпадение, `0` - независимость, `-1` - противоположность)
   ![[Pasted image 20260726232929.png]]

![[Pasted image 20260726232958.png|300x300]]
![[Pasted image 20260726233055.png]]

#### Пример расчета в коде

```python
# Скалярное произведение
dot_product = torch.dot(
	embedding_1,
	embedding_2,
)

norm_1 = torch.linalg.vector_norm(embedding_1)
norm_2 = torch.linalg.vector_norm(embedding_2)

similarity = dot_product / (norm_1 * norm_2)  # tensor(-0.0301)
```


## Построение промпта

### Хороший промпт

1. Роль и правила
2. Контекст (то, что мы собираем из чанков)
3. Вопрос
4. Место для ответа

Если написать инструкции после огромного текста, то модель может уделить им меньше внимания


