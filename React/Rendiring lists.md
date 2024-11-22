# Rendering Lists

### Использование `map`

1. Массив данных:

```js
const people = [
  'Creola Katherine Johnson: mathematician',
  'Mario José Molina-Pasquel Henríquez: chemist',
  'Mohammad Abdus Salam: physicist',
  'Percy Lavon Julian: chemist',
  'Subrahmanyan Chandrasekhar: astrophysicist'
];
```

2. Смапить массив в новый массив:

```js
const listItems = people.map(person => <li>{person}</li>);
```

3. Вернуть компонент списка

```js
return <ul>{listItems}</ul>;
```

### Использование `filter`

```js
const chemists = people.filter(person =>
    person.profession === 'chemist'
);
```

## Все `li` списка должны иметь свойство `key`

```html
<li key={person.id}>...</li>
```

- Лучше прокидывать `key` из данных или из БД
- Ключи должны быть уникальными между дочерними элементами списка
- Нельзя генерить ключ при рендере страницы

