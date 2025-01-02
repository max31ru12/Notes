Что-то типа version control для базы данных. [Документация](https://docs.djangoproject.com/en/5.1/topics/migrations/)
### Команды миграций
- `migrate`
- `makemigrations`
- `sqlmigrate` - показывает SQL-команды миграций
- `showmigrations` - показывает все миграции по **django-приложениям**

>  Переименовать папку можно с помощью редактировани настройки [`MIGRATION_MODULES`](https://docs.djangoproject.com/en/5.1/ref/settings/#std-setting-MIGRATION_MODULES)

#### Дать имя для миграции

```shell
python manage.py makemigrations --name migration_name app_name
```

### Зависимости 
Зависимости указываются в атрибуте **dependencies** в формате:
`(app_name, migration_name)`. **app_name** может быть именем django-приложения или **label** из файла **apps** приложения.

```python
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [("migrations", "0001_initial")]

    operations = [
        migrations.DeleteModel("Tribble"),
        migrations.AddField("Author", "rating", models.IntegerField(default=0)),
    ]
```