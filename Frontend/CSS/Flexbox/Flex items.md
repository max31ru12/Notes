
## Flex items properties

[[Flexbox]]
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




## Properties of flex-container's children

### `flex-grow`
**Flex-grow** always applied to child element of a flex container and spiecifies the size of elements inside the container relative to each other (proportion)

![[Pasted image 20250215014910.png]]

```css
<div class="flex-container">
  <div style="flex-grow: 4">1</div>
  <div style="flex-grow: 1">2</div>
  <div style="flex-grow: 8">3</div>
</div>
```

### flex-shrink

Specifies the size relative to other elements inside the container

![[Pasted image 20250215015107.png]]

```css
<div class="flex-container">  
  <div>1</div>  
  <div>2</div>  
  <div style="flex-shrink: 0">3</div>  
  <div>4</div>  
  <div>5</div>  
  <div>6</div>  
  <div>7</div>  
  <div>8</div>  
  <div>9</div>  
  <div>10</div>  
</div>
```

### `flex-basis`
Set the initial length of the flex item

![[Pasted image 20250215015558.png]]

```css
<div class="flex-container">  
  <div>1</div>  
  <div>2</div>  
  <div style="flex-basis: 200px">3</div>  
  <div>4</div>  
</div>
```

### `flex`
It's a shorthand property for the `flex-grow`, `flex-shrink`, and `flex-basis` properties.

```css
<div class="flex-container">  
  <div>1</div>  
  <div>2</div>  
  <div style="flex: 0 0 200px">3</div>  
  <div>4</div>  
</div>
```

###  `align-self` 

The `align-self` property specifies the alignment for the selected item inside the flexible container.

The `align-self` property overrides the default alignment set by the container's `align-items` property.

![[Pasted image 20250215015752.png]]

```css
<div class="flex-container">  
  <div>1</div>  
  <div>2</div>  
  <div style="align-self: center">3</div>  
  <div>4</div>  
</div>
```