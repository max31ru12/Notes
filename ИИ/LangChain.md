

## Основной datatype LangChain - `Document`

`Document` - это контейнер для текста + информация об этом тексте

```python
doc = Document(
	page_content="SOME TEXT",
	metadata={
		"source": "rag.md",
		"section": "introduction",
	}
)
```

### Три основных поля

```python
doc.page_content # сам текст 
doc.metadata # произвольный dict с метаданными 
doc.id # optional идентификатор
```


### Один `Document` не обязательно == целый документ `name.pdf`

Скорее RAG == ЕДИНИЦА retrieval

Пример после чанкинга:

```python
[
    Document(
        page_content="chunk 1...",
        metadata={"source": "rag.md"}
    ),

    Document(
        page_content="chunk 2...",
        metadata={"source": "rag.md"}
    ),

    Document(
        page_content="chunk 3...",
        metadata={"source": "rag.md"}
    ),
]
```

### Пример с чтением файла 

```python
from langchain_core.documents import Document

with open("data/rag.md", encoding="utf-8") as file:
    text = file.read()

document = Document(
    page_content=text,
    metadata={
        "source": "data/rag.md",
    },
)
```

## Text splitters

### Пример
Рекурсивное символьное разбиение

```python
splitter = RecursiveCharacterTextSplitter(
	chunk_size=500,
	chunk_overlap=50,
)

chunks = splitter.split_documents(documents)
```

#### Методы сплиттера

- `split_documents` - принимает массив документов `Document`, возвращает `list[Document]`
- `split_text` - принимает текст (строку)


## Embeddings 

`HuggingFace` - экосистема вокруг LLM, embeddings, NLP, computer vision и т.д.

```python
from langchain_huggingface import HuggingFaceEmbeddings  
  
# Создание embedding-модели
embedding_creator = HuggingFaceEmbeddings(  
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",  
)

# embeddings документов
# embed_documents принимает не list[Document], а именно список строк
embeddings = embedding_creator.embed_documents(
	[  
	    "Документ 1",  
	    "Документ 2",  
	    "Документ 3",  
	]
)

# Вопрос пользователя 
query = "Как модель может использовать внешнюю информацию?"

#Создаём embedding вопроса 
query_vector = embeddings.embed_query(query)
```

`model_name` - имя модели, которая лежит на **Hugging Face Hub**. Библиотека скачает ее оттуда

библиотека `sentence-transformers` тоже берет модели с **HuggingFaceHub**

### Что получается при создании embeddings

- `type(embeddings)` - возвращает список из эмбеддингов документов (эмбеддинг в виде списка)
- `len(embeddings)` - количество переданных документов
- `type(embeddings[0])` - list размерностью 384


### Embeddings и тип Document

Метод `embed_documents` не принимает `Document`, он принимает строки (список строк). Интеграция `Document` происходит при работе с `VectorStore`


## VectorStore (Qdrant) в LangChain

VectorStore связывает `Document` + `Embeddings` + `Векторную БД`

### Библиотека 

```bash
pip install langchain-qdrant
```


### Пример

```python


# 1. Qdrant client
client = QdrantClient(url="http://localhost:6333")


# 2. Embedding-модель
embeddings = HuggingFaceEmbeddings(  
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",  
)


# 3. LangChain VectorStore
vector_store = QdrantVectorStore(
	client=client,
	collection_name="articles",
	embeddings=embeddings,
)
```

`QdrantVectorStore` - актуальная LangChain-интеграция с **Qdrant** (старый класс `Qdrant` сейчас deprecated)


#### Добавление документов

```python
from langchain_core.documents import Document 

documents = [ 
	Document( 
		page_content="RAG позволяет LLM использовать внешние данные.", 
		metadata={"source": "rag.md"}, 
	), 
	Document( 
		page_content="Qdrant — это векторная база данных.", 
		metadata={"source": "qdrant.md"}, 
	), 
]
```


#### Поиск

```python
results = vector_store.similarity_search(
	query="Что позволяет модели использовать дополнительные данные?",
	k=2,
)

# Если нужен score
results = vector_store.similarity_search_with_score( 
	query="Что такое RAG?", 
	k=2, 
) 

for document, score in results: 
	print(document.page_content) 
	print(score)
```


## Retriever
**Retriever** принимает запрос и возвращает релевантные `Document`. Retriever отвязывает RAG от конкретной реализации поиска.

С Qdrant через `VectorStore` это выглядит так:

```python
retriever = vector_store.as_retriever(
	search_kwargs={
		"k": 3, 
	},
	search_type="similarity",
)

# Поиск
documents = retriever.invoke("Что такое RAG?")
```

- `search_kwargs` - опциональный параметр
- `search_type="similarity"` - опциональный параметр (по умолчанию - )

## PromptTemplate / ChatPromptTemplate

`ChatPromptTemplate` нужен, чтобы не собирать prompt руками через f-string 

`PromptTemplate` удобен для обычных LLM. На вход принимает dict, на выходе - готовый текстовый prompt.

### Пример

```python
from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages([ 
	(
		"system", 
		"Ты помощник по RAG. Отвечай только на основе контекста." 
	), 
	(
		"human", 
		""" 
		Контекст: {context} 
		Вопрос: {question} 
		""" 
	), 
])
```

В фигурных скобках переменные, которые подставляются позже

```python
context = """
RAG позволяет языковой модели использовать
внешние источники информации.
"""

question = "Что такое RAG?"

result = prompt.invoke({
    "context": context,
    "question": question,
})
```

Выход - ChatPromptValue:

```
ChatPromptValue 
		↓ 
[ 
	SystemMessage(...), 
	HumanMessage(...) 
]
```

Например концептуально:

```
SystemMessage:
"Ты помощник по RAG. Отвечай только на основе контекста."

HumanMessage:
"
Контекст:
RAG позволяет языковой модели использовать внешние источники информации.

Вопрос:
Что такое RAG?
"
```

#### Роли модели - system, human 

- **system** - инструкция модели, как вести себя
- **human** - сообщение пользователя
- **ai** - предыдущее сообщение модели (используется для передачи истории диалога)
- **tool** - результат вызова tool


## ChatModel / LLM

### Базовый пример

```python
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage


model = ChatOllama(
    model="qwen3:4b",
)

response = model.invoke([
    HumanMessage(
        content="Что такое RAG?"
    )
])

# текст ответа
print(response.content)
```

### Пример вместе с ChatpromptTemplate

```python
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


model = ChatOllama(
    model="qwen3:4b",
)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Отвечай кратко и только на основе переданного контекста."
    ),
    (
        "human",
        """
Контекст:
{context}

Вопрос:
{question}
"""
    ),
])


prompt_value = prompt.invoke({
    "context": "RAG позволяет LLM использовать внешние данные.",
    "question": "Что такое RAG?",
})


response = model.invoke(prompt_value)


print(response.content)
```