
## Примеры

### Базовое использование

```ts
interface ApiResponse<T> {
	status: number
	metaData: string
	data: T
}

interface UserData {
	username: string
}

const UserApiResponse: ApiResponse<UserData> {
	status: 200,
	metaData: "MetaData",
	data: {
		username: "Max",
	},
}
```

### Generics в стрелочных функциях

```ts
const arrowGeneric = <T,>(arg: T): T => {
	return arg
}
```

> Запятая нужна при использовании `React`, так как треугольные скобочки могут рассматриваться как JSX-разметка

### Ограничения в Generics

```ts
function createEntity = <T extends {id: number, createdAt: Date}>(arg: T) => {
	arg.id...
	arg.createdAt
}
```

У типа `T` должны быть свойства `id` и `createdAt`.


### Дефолтный тип

```ts
intreface ApiResponse<Data = string> {
	status?: number
	requestId?: string
	data: Data
}
```

### Условные типы

```ts
// Является ли тип массивом
type isArray<T> T extends any[] ? true : false
// не обязательно true or false
type isArray<T> T extends any[] ? Array : number
```