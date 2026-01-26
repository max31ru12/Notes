Определяет метод позиционирования для элемента:

#### Типы позиционирования
- static
- relative
- fixed
- absolute
- sticky

Элементы позиционируют с помощью `left`, `top`, `right` и `bottom`

### Static
Дефолтное позиционирование, которое не определяется с помощью `left`, `top`, `right` и `bottom`

### Relative
Элемент позиционируется относительно его НОРМАЛЬНОЙ позиции, по сути это просто смещение. 

**Следует размерам родителя**

```css
div.relative {  
	position: relative;  
	left: 30px;  
	border: 3px solid #73AD21;
}
```

###  Fixed
Фиксируется в одном месте

```css
div.fixed {  
	position: fixed;  
	bottom: 0;  
	right: 0;  
	width: 300px;  
	border: 3px solid #73AD21;
}
```

С помощью таких стилей позиция элемента задается в правом нижнем углу.

### Absolute
Позиционируется относительно ближайшего предка

**Ширина посдcтраивается под контент**

### Sticky
Позволяет переключаться между позиционированием `relative` и `fixed`. Остается `relative`, пока при скролле не наступит указанное положение `left`, `top`, `right` или `bottom`:

```css
div.fixed {  
	position: fixed;  
	bottom: 0;  
	right: 0;  
	width: 300px;  
	border: 3px solid #73AD21;
}
```