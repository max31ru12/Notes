
## SSL сертификаты

Nginx читает файлы с SSL-сертификатами с диска. Для этого необходимо указать путь к файлам с сертификатами:

```nginx
server {
	listen 443 ssl;
	server_name example.com;

	ssl_certificate /etc/ssl/certs/site.crt;
	ssl_certificate_key /etc/ssl/private.site.key;
}
```

`server_name` - домен



## Certbot для автоматической генерации сертификатов

Certbot получает сертификаты от Let's Encrypt и кладет их к себе в: `/etc/letsencrypt/live/domain`, где **domain** - это имя используемого домена (например, asrpath.org)

Команда `certbot certonly -d asrpath.org` создает структуру:

```bash
/etc/letsencrypt
├── live
│   └── asrpath.org
│       ├── fullchain.pem
│       └── privkey.pem
```

**Nginx не умеет автоматически обновлять сертификаты, надо каждые 90 дней делать `nginx reload`**


### Проверка домена от Let's Encrypt

**Для того, чтобы сервис выпуска сертификатов смог успешно проверить домен, необходимо, чтобы он смог увидеть специальный файл, который создает certbot.**

Let's Encrypt делает запрос `GET /.well-known/acme-challenge/token`

Nginx должен знать про этот файл, поэтому надо добавить в конфигурационный файл такую директиву:

```nginx
location /.well-known/acme-challenge/ {  
	root /var/www/html;  
}
```

Или можно с использованием alias:

```nginx
location /.well-known/acme-challenge/ {
    alias /var/www/html/.well-known/acme-challenge/;
}
```

Let's Encrypt сделает запрос: `GET http://asrpath.org/.well-known/acme-challenge/TOKEN`, nginx будет искать файл: `/var/www/html/.well-known/acme-challenge/TOKEN`, а certbot положит его туда.

Этот файл удаляется после того, как certbot отработал, в а Nginx появляются сертификаты (при правильно настроенный volumes).

> Только после этого можно добавлять https-конфигурацию в конфиг Nginx. Если добавить https до того, как certbot отработает, то запрос на наш `http://domain` nginx проксирует на `https`, и ничего не получится.