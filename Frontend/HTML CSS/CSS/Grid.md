
## Grid-контейнер
Это контейнер, которому применены `display: grid` или `display: inline-grid` 

- ширина: занимает всю доступную ширину
- высота: это высота содержимого
- размеры inline-grid: зависят от внутреннего содержимого 

Просмотреть **grid-сетку**:

![[Pasted image 20250218221337.png|400x400]]

### grid-yemplate-columns

Задает количество и размер колонок, на которое будет разделено пространство. Внутренние элементы переносятся как при `flex-wrap: wrap`

```css
diplay: grid;
grid-template-columns: auto auto auto; /* 3 колонки ширины auto */
/* имена для grid-линий */
grid-template-columns: [first] 50px [second] 70% [third] auto [fourth];
/* 3 колонки по 150px */
grid-template-column: repeat(3, 150px);

grid-template-column: repeat(3, 1fr);
/* первый столбец регулируется самостоятельно от 35% процетов длины контейнера до 200px */
grid-template-column: minmax(200px, 35%) 1fr 50px;

/* не переносить колонки, указанные в grid-auto-columns на новую строку после колонок, указанных в grid-template-columns */
grid-auto-columns: 50px 100px;
grid-auto-flow;
```

`1fr` **(fraction - дробь/доля/часть)** - на сколько равных частей будет поделен каждый элемент. **В данном случае - 1/3** (работает как соотношение во flex-wrap)

![[Pasted image 20250218221259.png]]

### grip-template-rows

Регулирование строк

```css
grid-template-rows: 40px 80px;
/* Все последующие строки по 15px */
grid-auto-rows: 15px;
```

![[Pasted image 20250218222202.png]]


### grid-template-areas

Позволяет указать шаблон сетки grid-контейнера


```css
display: grid;
grid-template-columns: 25% auto 15%;
grid-template-areas:
	"menu catalog advertisement"
	"menu catalog advertisement"
	"menu catalog ."
	"menu order order"
```

### Отступы

- **gap**: 10px 20px
- **row-gap**
- **column-gap**
- **justify-content**
- **align-items**
- **place-item: center end** - shortcut для *justify-content* и *align-items* (в таком порядке)

### Растянуть элемент на все колонки

```css
grid-column: -1 / 1;
```