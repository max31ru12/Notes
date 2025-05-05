
## Interface

### Использование
```ts
const dog: Dog = {
	name: "Бобик",
	bark: () => console.log("Гав")
}
```

#### Использование с классами
```ts
interface Human {
	name: string;
}

class Woman implements Human {
	sex: string = 'woman';
	name: string;

	constructor(name: string) {
		this.name = name;
	}
}
```

### Расширение `extends`
```ts
interface Animal {
	name: string;
}

interface Dog extends Animal {
	bark: () => void;
}
```

## Разница Type и Interface
1. `Interface` только для объектов, `Type` - для различных типов, включая объекты
2. `Type` может использоваться с примитивами, пересечениями и списками


## Шаблонный литерал

```ts
// Начинается с user_id_
type UserId = `user_id_${string}`
```