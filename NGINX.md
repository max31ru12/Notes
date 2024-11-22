Конфигурационный файл nginx.conf находится в ожном из трех мест:

1) usr/local/nginx/conf
2) etc/nginx
3) usr/local/etc/nginx


Управление nginx:  nginx -s сигнал

1) stop - быстрое завершение
2) quit - плавное завершение
3) reload - перезагрузка конфигурационного файла
4) reopen - переокрытие лог-файлов

Команды с помощью bash: ps -ax | grep nginx   kill -s QUIT 1628

Команды должны выполняться под тем же пользователе, под которым запущен nginx


Директивы: простая (заканивается ; ), блочная (внутри {} )

### Конфигурационный файл

```nginx
upstream django:8000 {
    server django:8000;
}

server {
    listen 80;
    server_name 192.168.55.107;

    location / {
	proxy_pass http://localhost:8000;
    }

    location /folder/ {
	root /data/w3
    }
}
```

Директивы:

 `server_name 192.168.55.107;` - если не указывать, то сервер будет доступен по адресу http://localhost
`listen 8080;` - если не указывать, то будет 80 порт. По этому порту сервер будет доступен 
(на каком порту принимаем соединения)

```nginx
location /folder/ {
      root data/w3;
  }
```

в ответ на запрос **folder/image.jpg** будет выдан файл по пути: **folder/data/w3/image.jpg**

 `proxy_pass http://localhost:8000/uri/;` - задает адрес и протокол проксируемого сервера, **uri** можно не указывать:
 - в docker-compose вместо localhost нужно указывать имя сервиса
 - location / {} - перенаправляет сюда все динамические запросы (на проксируемый сервер)
  




