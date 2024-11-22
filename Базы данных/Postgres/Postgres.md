### СОЗДАНИЕ И УДАЛЕНИЕ БАЗЫ ДАННЫХ	

`CREATE DATABASE db_name` - создать базу данных (с указанием имени БД)
`DROP DATABASE db_name` - Удалить БД (с указанием имени БД)

### СОЗДАНИЕ ТАБЛИЦЫ
`CREATE TABLE table_name` - Создать таблицу с укказанием имени таблицы

### Пример `INSERT`
```sql
INSERT INTO employee(
	first_name,
	last_name,
	gender,
	email,
	date_of_birth
)
VALUES ('John', 'Doe', 'Male', 'Jd@mail.com', '01/01/2000');
```

> Обязательно в `VALUES` указывать значения в **одинарных кавычках**


### Работа с датой и временем
`SELECT NOW();` - выводит текущее время
`SELECT NOW()::DATE;` - выводит только дату
`SELECT NOW()::TIME;` - выводит только время

`SELECT NOW() - INTERVAL '1 YEAR';` - от текущей даты перемещаемся на интервал 1 год
`SELECT NOW() - INTERVAL '10 MONTHs';` - переместиться на 10 месяцев назад
`SELECT NOW() - INTERVAL '10 DAYS';` - переместиться на 10 дней назад

`SELECT EXTRACT(YEAR FROM NOW());` - Выбрать из текущей даты ГОД или МЕСЯЦ или ДЕНЬ
`SELECT EXTRACT(DOW FROM NOW());` - Выбрать день недели

`SELECT first_name, last_name, AGE(NOW(), date_of_birth) AS age FROM employee;` - Функция AGE


### Ограничения (CONSTRAINT)
```sql
ALTER TABLE employee ADD CONSTRAINT unique_email_address UNIQUE (email);
```

Добавить ограниченияе уникальности на поле email (UNIQUE)
`unique_email_adress`  - это имя ограничения

```sql
ALTER TABLE gender ADD CONSTRAIN gender_constraint CHECK (gender = 'Female' OR gender = 'Male');
```

Добавить ограничение на гендер, либо то либо то значение 

### Внешние ключи и связи (FOREIGN KEYS)

В таблице employee создаем поле `bicycle_id`, которое будет ссылаться на поле `id` таблицы `bicycle`

```sql
ALTER TABLE employee ADD bicycle_id BIGINT REFERENCES bicycle (id);
ALTER TABLE employee ADD UNIQUE(bicycle_id);
```

Делаем поле `bicycle_id` уникальным


### Экспорт SQL-запроса в таблицу CSV
```bash
\copy (SELECT * FROM employee WHERE bicycle_id IS NOT NULL) TO 'C:/Path_to_db' DELIMITER ',' CSV HEADER;
```

