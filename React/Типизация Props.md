

## prop-types

Вариант с **PropTypes** не использует TypeScript

```ts
import PropTypes from 'prop-types';


const Component = ({ name, age, isActive }) => (  
	<div>...</div>
);

Component.propTypes = {
	name: PropTypes.string.isRequired,
	age: PropTypes.number.isRequired,
	isActive: PropTypes.bool,
}
```


## Типизация с помощью Generic

```ts
import React from "react";


interface ComponentProps {
	name: string;
	age: number;
	isActive?: boolean; // ? - необязательный пропс
}

conts Component: React.FC<ComponentProps> = ({ name, age, isActive }) => {
	<div>...</div>
}
```


## С помощью интерфейса

```ts
inteface ComponentProps {
	name: string
	age: number
}

const Component = ({ name, age }: ComponentProps) => {
	<div>...</div>
}
```

## С помощью интерфейса и Generic'а

Такой подход подкидывает в props'ы параметр `children`, который стоит типизировать со всеми остальными пропсами

```ts
import { FC. ReactNode } from "react";

inteface ComponentProps {
	name: string
	age: number
	children?: ReactNode
};

const MyComponent: FC<ComponentProps> = ({ name, age, children = null }) => {
	<div>...</div>
}
```

**Хорошая практика:** присваивать значение `null` по умолчанию для `children`

### Типизация children

Самый универсальный варинат - `ReactNode`. Он включает в себя все типы данных, а также `ReactElement`.

`ReactElement` - только JSX или компоненты.