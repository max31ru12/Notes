
## Передача выполнения команды в переменную

```bash
mydir=`pwd` # Обратные кавычки

mydir=$(pwd) # второй способ
```

## Математические операции

```bash
$((a+b))
```


##### Пример

```bash
!#/bin/bash

var1=$(( 5 + 5))

var2=$(( $var1 * 2 ))
```


## if then else


Команда в условии `if` может вернуть либо `0`, либо `1`.

##### Пример

```bash
!#/bin/bash

user=anotherUser

if grep $user /etc/passwd
then
echo "The user $user exists"
else
echo "Ther user $user does not exist"
fi
```

### Сравнение чисел в условии if

Обязательно отделять квадратные скобочки пробелом от операндов

```bash
!#/bin/bash

var1=5

if [ $var1 -eq 5 ]
	then
		...
	else
		...
fi
```

### Проверка условий, касающихся файлов

- `-d <fname>ile` - проверить, существует ли файл и является ли директорией
- `-e <filename>` - проверяет, существует ли файл
- `-f <filename>` - проверяет, существует ли файл и является ли он файлом
- `-r` - существует ли файл и доступен ли он для чтения
- `-s` - существует ли файл и является ли он пустым
- `-w` - существует ли файл и доступен ли он для записи
- `-x` - существует ли файл и является ли он исполняемым
- `file1 -nt file2` - новее ли файл1 чем файл2
- `file1 -ot file2` - старше ли файл1 чем файл2
- `-O` - является ли его владельцем текущий пользователь
- `-G` - соответствует ли идентификатор группы текущего пользователя идентификатору группы файла

##### Пример

```bash
!#/bin/bash

mydir=/home/mydir

if [ -d $mydir ]
	then
		echo "The $mydir directory exists"
		cd $mydir
		ls
	else
		echo "The $mydir directory does not exist"
fi
```



## Циклы

```bash
#!/bin/bash

for var in first second third fourth fifth
do
	echo "The $var item"
done
```

















