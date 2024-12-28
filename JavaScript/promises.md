# Promise'ы

это спец. объект, который используется для написания и обработки асинхронного кода.

Асинхроные функции возвращают объект `Promise` в качестве значения.

Promise может находиться в одном из трех состояний:

- `pending` - стартовое состояние, операция стартовала
- `fulfilled` - получен результат
- `rejected` - ошибка.

## Создангие Promise'а

```js
let promise = new promise(
    // функция-исполнитель executor
    function(resolve, reject) {
        ...
    }
)
```

функция-исполнитель выполняется автоматически при создании промиса

`resolve` и `reject` - это callback'и. Один из них вызывается, когда **executor** завершает свою работу.

- `resolve(value)` - в случае успеха
- `reject(error)` - в случае неудачи (лучше вызывать с объектом `Error`)


## `then`

```js
promise.then(
    function(result) {}, // Обрабатывает успешное выполнение
    function(error) {} // Обрабатывает ошибку
);
```


#### Пример использования

```js
let promise = new Promise(function(resolve, reject) {
    setTimeout(() => resolve("done!"), 1000);
});

promise.then(
    result => alert(result),
    error => alert(error),
)
```

В случае успеха выполнится первая функция (в данном примере выполнится имеено она, так как в промисе вручную вызывается `resolve`), в случае ошибки выполнится вторая функция.

Если нужно обработать только успешное выполнение, то можно передавать только одну функцию

```js
let promise = new Promise(
    function (resolve, reject){
        setTimeout(() => resolve("done!"), 1000);
    }
);

promise.then(console.log) // Выполнится автоматически и выведет: done!
```


## `catch` - обработка ошибок

#### можно обработать ошибок с помощью `.then`:

```js
let promise = new Promise(resolve => {
    setTimeout(() => resolve("done!"), 1000);
});

promise.then(null, console.log);
```

#### но лучше использовать `.catch`:

```js
let promise = new Promise(
    (resolve, reject) => {
        setTimeout(() => reject(new Error("Ошибка")), 1000);
    }
);

promise.catch(alert);
```

## `finally` 

Выполняется в любом случае и спользуется для очистки ресурсов: закрытия соединенний, остановки индикаторов загрузки, 

# Цепочка промисов

Результаты из `.then()` по цепочке передаются в следубщий `.then()`

```js
new Promise(...).then(...).then(...)
```






# Асинхронные функции

Особенность `async`: такая функция **всегда возвращает промис**


```js
async function f() {
    return 1;
}

f().then(console.log); // выведет 1
```

По сути функция выше это аналог следующего кода:

```js
async function f() {
    return Promise.resolve(1);
}

f().then(console.log); // также выведет 1
```

## `await` 

Можно использовать только внтури `async` - функций

Ключевое слово `await` заставит интерпретатор JS ждать, пока промис справа не выполнится, а затем вернет его результат.

```js
async function f() {
    let promise = new Promise((resolve, reject) => {
        setTimeout(() => resolve("done!"), 1000);
    });

    let result = await promise; //

    alert(result);
};

f();
```

## Обработка ошибок 

```js
async function f() {

    try {
        let response = await fetch("url");
    } catch(err) {
        alert(err);
    }
}

f();
```

#### без `try..catch`

```js
async function f() {
    let response = await fetch("url");
}

// f вернет промис в состоянии rejected
f().catch(alert);
```

Если не ловить ошибку с помощью `catch`, то ошибка будет выведена в консоль