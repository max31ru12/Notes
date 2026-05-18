
### Сертификаты 

#### Обновить сертификаты (при уже существующих сертификатах)

```bash
docker compose -f production.yml run --rm certbot certonly --webroot -w /var/www/html -d asrpath.org --email you@example.com --agree-tos --no-eff-email --force-renewal
```

#### Перезапустить Nginx

```bash
docker compose -f production.yml exec nginx nginx -s reload
```

#### Автоматизация


```bash
sudo crontab -e
```

задаем там строку

```
0 3 * * * cd /path/to/rsapa-backend && docker compose -f production.yml run --rm certbot renew --webroot -w /var/www/html --quiet && docker compose -f production.yml exec nginx nginx -s reload

```


## Дампы базы данных 

### Создать дамп

#### Дамп данных таблицы

```bash
docker exec -i asrp_database pg_dump -U <user> -d <database> 
--table=public.table_name --data-only > data_dump.sql
```


### Применить дамп

#### Отдельная таблица

Применить `--data-only` на одну таблицу

```bash
psql -U <user> -d <database> -f users_data.sql 
```

Таблица `public.users` должна уже существовать

Для `docker`:

```bash
docker exec -i asrp_databse psql -U <user> -d <database> < databse_dump.sql
```


#### Вся БД

Был сделан дамп базы `source_db` в файл `data_only_dump.sql`:

```bash
pg_dump -U <user> -d <source_db> --data-only -f data_only_dump.sql
```

Можно восстановить данные в другую базу:

```bash
psql -U <user> -d <database> -f data_only_dump.sql
```

Через `docker`:

```bash
docker exec -i container_name psql -U <user> -d <target_db> < data_only_dump.sql
```
