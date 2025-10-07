Конфигурационный файл nginx.conf находится в ожном из трех мест:

1) usr/local/nginx/conf
2) etc/nginx
3) usr/local/etc/nginx


Управление nginx:  nginx -s сигнал

1) stop - быстрое завершение
2) quit - плавное завершение
3) reload - перезагрузка конфигурационного файла
4) reopen - переокрытие лог-файлов
### Конфигурационный файл

```nginx
server {
    listen 80;
    server_name domain.com;

	root /var/www/html;
	index /index.html;

    location / {
		proxy_pass http://localhost:8000;
    }

}
```


- `proxy_pass` - проксирует запросы, приходящие на **/** на тот **url**, который указан в `proxy_pass`
- `server_name` - указываем домен для нашего сервера
- `root` - путь к папке, в которой располагаются статические файлы
- `index` - указываем файл по умолчанию
- `try_files $uri /index.html;` — важная строчка для React Router / SPA. Если пользователь заходит напрямую на `/about`, Nginx не найдёт файл `/about`, и вместо 404 отдаст `index.html`, а роутинг возьмёт на себя React.
