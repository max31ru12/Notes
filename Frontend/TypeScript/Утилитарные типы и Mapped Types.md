
## Утилитарные типы

### Пример

```ts
interface User {
	name: string
	age: number
	type: string
	friends: Array<string>
}

// Вытаскивает указанные поля
type NewUser = Pick<User, "name" | "age">
// Исключает указанные поля
type NewUser = Omit<User, "age" | "type">

// вытащить возвращаемое значение
type ReactTypeFn = ReturnType<typeof React.render>
// Вытащить тип параметров
type ReactFnParameters = Parameters<typeof React.render>
```


## MappedTypes

Типы, которые позволяют создавать новые типы

## Тип для `readonly` полей

```ts
type ReadonlyType<T> {
	readonly [K in keyof T]?: T[K] | null
}
```

- `[K in keyof T]` - вытаскиваем ключи из дженерика `T`
- `T[K]` - по этому ключу получаем значение из дженерика 
- `readonly` - делаем все поля **readonly**
- `?` - можно сделать опциональными (`-?` - отменить опциональность)

## Исключать поля

Преобразуем **K** к типу, у которого исключено (exclude) поле **fieldName** 

```ts
type WithoutField<T> {
	[K in keyof T as Exclude<K, "fieldName">]: T[K]
}
```