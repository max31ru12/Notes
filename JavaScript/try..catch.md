
## Синтаксис try..catch

```js
try {
	// код
} catch (err) {
	// обработка ошибок
} finally {
	// выполняется всегда
}
```

`(err)` можно пропустить, если не нужна ошибки
### Объект ошибки

`name` - имя ошибки, например, **ReferenceError**
`message` - текстовое сообщение о деталях ошибки


## Выброс ошибки

```js
let error = new Error(message);

let error = new ReferenceError(message);
let error = new SuntaxError(message);

throw error;

throw new SyntaxError("Wrong syntax")
```