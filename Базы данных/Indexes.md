
## Index types Postgresql 

- B-Tree
- Hash
- GiST
- SP-GiST
- GIN
- BRIN

### B-Tree

#### Операции сравнения
- больше
- меньше
- равно

**B-Tree** is used for searching in the range, ordering and unique constraints. Used for `BETWEEN` and `IN` statements, also `IS NULL` and `IS NOT NULL` can be used with **B-Tree**.

**Example:**

```postgresql
CREATE INDEX example_btree ON example_table (column_name);
```

#### Инициализация

Создается пустой **корневой узел** и **порядок** - число, которое определяет кол-во ключей в узле.

#### Вставка

Сначала идет поиск подходящего узла. Заполненный узел разделяется на два узла и начинается перераспределение ключей по дереву. Дерево остается сбалансированным.

#### Удаление

После удаления значения из B-Tree происходит перераспределение ключей и дерево заново балансируется.

#### Поиск

Поиск значения начинается с корневого узла. Искомый ключ сравнивается с ключами узлами, а затем осуществляет переход по одному из указателей текущего узла к следующему узлу.



### Hash

Stores a 32-bit hash code. 

Hash-index is used when needed to get fast access by equality. Hash doesn't provide ordering or getting an access by a range. 

```postgresql
CREATE INDEX ix_example_hash ON example_table USING hash (column_name);
```


### GiST (generalized search tree)

Это не какой-то определенный тип индекса, а инфраструктура для реализации индекса для произвольных типов данных. 

Можно использовать для данных с размерностью больше одного, в отличие от `b-tree`б который используется для данных с размерностью 1.

сбалансированное дерево поиска, как и `b-tree`, но с поддержкой больше количества операций сравнения. `GiST` сбалансирован по высоте.

#### Когда использовать
- сложные (составные) индексы
- пространственные типы данных
- запросы по диапазону

#### Пример создания

```postgresql
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  description TEXT,
  price NUMERIC,
  category VARCHAR(50)
);

CREATE INDEX idx_products_price_category ON products USING GIST (price, category);
```


### SP-GiST (Space-Partitioned Generalized Search Tree)

```postgresql
CREATE INDEX idx_point_spgist ON spatial_table USING spgist (geom);
```

#### Когда использовать
- неоднородные данные (например, иерархические)
- пространственные данные
- проверка пересечений
- строковые данные (для поиска подстрок)


### GIN (Generalized Inverted Index)

```postgresql
CREATE INDEX idx_jsonb_gin ON documents USING gin (data jsonb_path_ops);
```

#### Когда использовать
- поиск по множествам (массивам)
- поиск по JSONB


### BRIN (Block Rabge Index)

```postgresql
CREATE INDEX idx_date_brin ON events USING brin (event_date);
```

#### Когда использовать
- быстрый поиск по большим данным
- данные упорядочены по колонке
- когда нужен индекс, занимающий меньшее кол-во места
- временные данные


