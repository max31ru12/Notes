Выгрузка существующих данных: c. 174

python manage.py dumpdata --indent=2 --output=mysite_data.json

Если что-то пошло не так, то:
python -Xutf8 manage.py dumpdata --indent=2 --output=mysite_data.json


Postgres:

psql -U postgres
CREATE USER blog WITH PASSWORD '****';
CREATE DATABASE blog OWNER blog ENCODING 'UTF8';

settings.py:

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'Blog',
		'USER': 'Blog',
		'PASSWORD': '****',
	}
}


Загрузка данных в новую базу:

python manage.py loaddata mysite_data.json