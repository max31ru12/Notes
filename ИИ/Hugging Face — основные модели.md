

## LLM

### Qwen

**Пример:** `Qwen/Qwen3.5-9B`

- Универсальная LLM: текст, reasoning, coding, RAG.
- Хороший выбор для локального запуска.
- **Брать, если:** нужна основная LLM для своего приложения.

### Mistral

**Пример:** `mistralai/Mistral-Small-3.2-24B-Instruct`

- Универсальная LLM, сильна в instruction following и tool calling.
- **Брать, если:** строишь assistant/agent/RAG и хватает ресурсов.

### Gemma

**Пример:** `google/gemma-3-4b-it`

- Небольшая качественная LLM.
- **Брать, если:** нужна модель полегче для локального запуска.

### Phi

**Пример:** `microsoft/Phi-4-mini-instruct`

- Очень маленькая LLM, неплохая в reasoning/code.
- **Брать, если:** мало RAM/VRAM.

### DeepSeek

**Пример:** `deepseek-ai/DeepSeek-R1`

- Сильные reasoning-модели.
- Обычно тяжелые.
- **Брать, если:** нужны сложные рассуждения и есть ресурсы.

### Llama

**Пример:** модели семейства `meta-llama`

- Универсальные LLM с огромной экосистемой.
- **Брать, если:** важна совместимость с большим количеством готовых инструментов/fine-tunes.

---

# Embeddings

### Qwen3-Embedding

**Пример:** `Qwen/Qwen3-Embedding-0.6B`

- Превращает текст в векторы.
- Сильный вариант для современного RAG.
- **Брать, если:** делаешь multilingual/Russian RAG.

### BGE-M3

**`BAAI/bge-m3`**

- Популярная embedding-модель для multilingual RAG.
- **Брать, если:** нужен проверенный baseline.

### Multilingual E5

**`intfloat/multilingual-e5-large`**

- Хорошие multilingual embeddings.
- **Брать, если:** нужен простой проверенный вариант для русского/английского.

### EmbeddingGemma

**`google/embeddinggemma-300m`**

- Маленькая embedding-модель.
- **Брать, если:** важны скорость и низкое потребление ресурсов.

### MiniLM

**`sentence-transformers/all-MiniLM-L6-v2`**

- Очень легкая embedding-модель.
- В основном для английского.
- **Брать, если:** обучение, тесты, простой prototype.

---

# Rerankers

### Qwen3-Reranker

**Пример:** `Qwen/Qwen3-Reranker-0.6B`

- Пересортировывает chunks после vector search.
- Повышает точность RAG.

```
query
 ↓
embedding
 ↓
Qdrant → top 20
 ↓
reranker → top 5
 ↓
LLM
```

## Если запомнить только главное

```
Qwen       → основная LLM
Gemma/Phi  → маленькие LLM

Qwen3-Embedding → embeddings для RAG
BGE-M3           → хороший alternative
E5               → проверенный multilingual baseline

Qwen3-Reranker   → улучшение retrieval
```