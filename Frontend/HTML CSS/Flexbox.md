
## Базовая информация

Дочерние элемент **flex-контейнера** автоматическти становятся **flexible**. 

**Layout modes:**
- `block` for section in a webpage
- `Inline` for text
- `Table` for tables
- `Positioned` for explicit position of an element


Чтобы использовать `flexbox` необходимо создать flex-контейнер:

```html
<div class="flex-container" style="display: flex">  
  <div>1</div>  
  <div>2</div>  
  <div>3</div>  
</div>
```

Свойство `display: flex` позволяет сделать контейнер **flexible**. Также позволяет свойству `margin: auto` выравнивать блоки и по вертикали (по умолчанию он выравнивает только по горизонтали)

#### Свойства flex контейнеров:
- [`flex-direction`](https://www.w3schools.com/css/css3_flexbox_container.asp#flex-direction)
- [`flex-wrap`](https://www.w3schools.com/css/css3_flexbox_container.asp#flex-wrap)
- [`flex-flow`](https://www.w3schools.com/css/css3_flexbox_container.asp#flex-flow)
- [`justify-content`](https://www.w3schools.com/css/css3_flexbox_container.asp#justify-content)
- [`align-items`](https://www.w3schools.com/css/css3_flexbox_container.asp#align-items)
- [`align-content`](https://www.w3schools.com/css/css3_flexbox_container.asp#align-content)


### `flex-wrap`

Без flex-wrap:

```css
flex-wrap: nowrap
```

![[Pasted image 20241119140525.png]]

С использованием flex-wrap:

```css
flex-wrap: wrap
```

![[Pasted image 20241119140428.png]]


### `justify-content`

Дефолтное значение - `flex-start`

`center` - выравнивает элементы по центру контейнера:

![[Pasted image 20241119141207.png]]

`flex-start` - выравнивает элементы с начала контейнеров:

![[Pasted image 20241119141352.png]]

`space-around` - space before, between, and after the lines:

![[Pasted image 20241119141542.png]]

`space-between`

![[Pasted image 20241119141852.png]]

### `align-items`

Используется для выравнивания элементов в зависимости от той оси, которая выбрана в `flex-direction`.

Есть варианты **align-items**:
- `center`;
- `flex-start`;
- `flex-end`;
- `stretch` (default) - растягиванет на всю длин (или высоту контейнера);
- `baseline` - выравнивает водль базовой линии.

### `align-content`

**Позволяет выровнять по вертикали надписи внутри li**

`align-content` нужно для выравнивания **flex-линий**. Судя по всему работает с связке с **flex-wrap**.

![[Pasted image 20241119143231.png]]





## The CSS Flexbox Container Properties

![[Pasted image 20241119143449.png]]


## Perfect centering

```css
.flex-container {  
	display: flex;  
	height: 300px;  
	justify-content: center;  
	align-items: center;
}
```

## Flex items properties

[Про свойства flex-элементов](https://www.w3schools.com/css/css3_flexbox_items.asp)

`Пример:` Сделать третий элемент в 8 раз больше, чем первые 2:
```html
<div class="flex-container">  
  <div style="flex-grow: 1">1</div>  
  <div style="flex-grow: 1">2</div>  
  <div style="flex-grow: 8">3</div>  
</div>
```

Эта штука поделит контейнер на 10 частей в отношении 1 : 1 : 8.




