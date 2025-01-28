
## Замыкания
Способность функции запоминать лексическое окружение, в котором она была создана. 

**Лексическое окружение** - невидимый скрытый объект, который есть у любого блока, скрипта или функции. Состоит из:

1. Объект с переменными в текущей области видимости
2. Ссылка на родительское (внешнее) лексическое окружение

## Контекст (call/bind/apply)
Привязывает контекст выполнения


## Event loop

**Event loop** принимает в себя асинхронные таски, например, таймаут и держит их, пока в текущей функции функции не выполнятся все синхронные таски (точнее пока не очистится **Call Stack**)

**Event loop** - это стек, который хранит все асинхронные задачи, которые не вошли в сихронный поток выполнения. После завершения синхронного потока начинают выполняться задачи из Event Loop'а.

### Деление задач на подпиты внутри Event Loop:
- **Макрозадачи** - запросы, `setTimeout` (все микрозадачи завершаются до обработки каких-либо событий или рендеринга, или перехода к другой макрозадаче)
- **Микрозадачи** - `then` у промисов, Intersection Observer
- **Задачи отрисовки** - отрисовка и обновление контента страницы

### Упрощенный алгоритм работы событийного цикла
1. Сначала Event Loop проверяет выполнились ли все синхронные задачи
2. Потом выполняются **все задачи** из микротасков
3. После выполнения всех микротасков - очередь очищается
4. Затем мы берем **одну** макрозадачу из списка и выполняем ее
5. После выполнения мы смотрим нужно ли нам сделать перерисовку страницы
6. Если перерисовать страницу нужно - делаем это
7. Все снова начинается с первого пункта :)

```js
console.log("Step 1: In global scope - sync task")

setTimeout(() => console.log("Step 2: In setTimeout MacroTask "))

new Promise((resolve) => {
  console.log("Step 3: In promise constructor Sync Task")
  resolve()
}).then(() => console.log("Step 4: First then:: MicroTask")).then(
  () => console.log("Step 5: Second then Macrotask:: MiacroTask"))
  
setTimeout(() => console.log("Step 6: Another setTimeout macrotask"))

new Promise((resolve) => {
	console.log("Step 7: Another promise constructor Sync Task")
	resolve();
}).then(() => console.log("Step 8: Third then:: MicroTask")).then(
	() => console.log('Step 9: In Fourth then:: MicroTask'));
```

Пследовательность выполнения:
- **Step 1**: *In global scope - sync task*
- **Step 3**: *In promise constructor Sync Task*
- **Step 7**: *Another promise constructor Sync Task*
- **Step 4**: *First then:: MacroTask*
- **Step 8**: *Third then:: MacroTask*
- **Step 5**: *Second then Macrotask:: MacroTask*
- **Step 9**: *In Fourth then:: MacroTask*
- **Step 2**: *In setTimeout MicroTask*
- **Step 6**: *Another setTimeout microtask*








