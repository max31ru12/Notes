

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


1. Document
2. Document Loaders

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


## Retriever


## Prompt + ChatModel



