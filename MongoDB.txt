Структура БД:
Database:
|
|--Collection 1
   |--Document 1
     |--{key: "value"}
   |--Document 2
|-- Colection 2


Команды терминала MongoDB:
show databases						- посмотреть базы данных
use Mongo						- выбрать БД с указанным именем (создать и выбрать)
show collections					- показать коллекции
db.createCollection("users")				- создать коллекцию с указанным именем users
db.dropDatabase("Mongo")				- удалить БД с указанным именем
db.users.find()						- запрос на получение всех данных из коллекции
db.users.find({age: 25})				- найти записи, где есть поле age равное 25
d.users.find({name: {$exists: true}})			- выбор записи, где существует поле name

Вставка
db.users.insert({name: "Max", age: 25}) 		- вставка записи (записей)
db.users.insertOne({name: "Max", age: 25})		- вставка одной записи (желательный вариант)
db.users.insertMany({name: "Vasya", age: 22},		- вставка нескольких записей
		    {name: "Petya", age: 14})

Выборка с условием
db.users.find({$or: [{name: "Max"}, {age: 25}]})	- ИЛИ, условия в массиве
	     ({age: {$lt:30}})					- МЕНЬШЕ
	     ({age: {$lte:30}})				- МЕНЬШЕ или РАВНО
	     ({age: {$gt: 30}})				- БОЛЬШЕ
	     ({age: {$gte: 30}})				- БОЛЬШЕ или РАВНО
	     ({age: {$ne: 30}})				- НЕ РАВНО

Сортировка
db.users.find().sort({age: 1})				- выбор с сортировкой по возрасту (-1 - обратная сортировка)
db.users.find().limit(4)				- ограничение числа записей
db.users.find().distinct()				- уникальные записи

Обновление уже существующих записей
db.users.update({name: "Max", age: 25}, 		- первый объект - условие выбораб второй - на что заменить
		{$set: {name: "Maks", age: 22}})

db.users.updateOne()					- лучше использовать такие вещи для обновления
db.users.updateMany()					- лучше использовать такие вещи для обновления

Переименовать поле
db.users.updateOne({}, {$rename: {name: "fullname"}}) 	- переименовать поле name в "fullname"

Удалить документ
db.users.deleteOne({age: 25})
ad.users.deleteMany()


Множественный запрос
db.users.bulkWrite([
	{
	 insertOne: {document: {name: "Ira", age: 19}}
	},
	{
	 deleteOne: {filter: {name: "Petya"}}
	},
])


Связь "один-ко-многим"
db.users.update(
	{name: "Petya"},
	{$set: {
		posts: [
			{title: "Java"},
			{title: "Mongo"},
		       ]
	       }
	}
)

db.users.findOne({name: "Petya"}, {posts: 1})		- получаем только посты из записей среди Petya














