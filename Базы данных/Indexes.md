
## Index types Postgresql 

- B-Tree
- Hash
- GiST
- SP-GiST
- GIN
- BRIN

### B-Tree

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

