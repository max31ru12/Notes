
```nginx

server {
    listen 80;
    server_name asrpath.org;

    location /.well-known/acme-challenge/ {
        alias /var/www/html/.well-known/acme-challenge/;
        try_files $uri =404;
    }

    location / {
        return 200 "ok";
    }
}


```