
**Бэкап** - физическая копия БД для восстановления базы целиком.

**Дамп** - логическая копия базы **(структура + данные)** в виде текста или SQL-команд, подходит для:
- переноса данных на другую СУБД; 
- частичного восстановления;
- обновления между версиями.


## Утилиты для дампа

1. `pg_dump` - создает файл с sql-командами для создания и заполнения таблиц 
   
```bash
# первый вариант использования
pg_dump -U username -p 5432 -d db_name > test_dump.sql

# более явный вариант
pg_dump -h 127.0.0.1 -p 5432 -U test -d test -f test_dump.dump
```

если указать параметры `-Fc`, то дамп будет создан в виде архива 

2. `pg_basebackup` 

## Восстановить БД из файла
Необходимо удалить старую и создать новую БД (либо создать нову и восстановить базу туда).

```bash
psql -h 127.0.0.1 -p 5432 -U test -c "DROP DATABASE IF EXISTS test;"
psql -h 127.0.0.1 -p 5432 -U test -c "CREATE DATABASE test;"
```

Затем восстанавливаем базу:

```bash
# Если это текстовый файл
psql -h 127.0.0.1 -p 5432 -U test -d test -f test_dump.dump

# Если дамп в виде архива
pg_restore -h 127.0.0.1 -p 5432 -U test -d test -v test_dump.dump
```
