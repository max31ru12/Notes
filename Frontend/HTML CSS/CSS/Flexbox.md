
## Базовая информация

Дочерние элемент **flex-контейнера** автоматически становятся **flexible** - [[Flex items]]

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

### inline-flex
Это как `display: flex`, только размер контейнера будет высчитывать по его содержимому

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

Используется для выравнивания элементов в зависимости от той оси, которая выбрана в `flex-direction`. Работает только при заданной высоте контейнера (для **flex-direction: row**) чтобы было место, куда выравнивать. Аналогично **width** для **column**


Есть варианты **align-items**:
- `center`;
- `flex-start`;
- `flex-end`;
- `stretch` (default) - растягиванет на всю длин (или высоту контейнера);
- `baseline` - выравнивает водль базовой линии.

### `align-content`

`align-content` нужно для выравнивания **flex-линий**. Помогает распределить свободное пространство между рядами flex-элементов по поперечной оси

![[Pasted image 20250216155326.png]]





## The CSS Flexbox Container Properties

![[Pasted image 20241119143449.png]]

![[Pasted image 20250215010325.png]]
## Perfect centering

```css
.flex-container {  
	display: flex;  
	height: 300px;  
	justify-content: center;  
	align-items: center;
}
```