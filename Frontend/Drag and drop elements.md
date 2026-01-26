
## Основы

У React-компонентов есть пропсы:
- `draggable` - делает элемент передвигаемым 
- `onDragStart` - Срабатывает в тот момент, когда мы взяли карточку (событие **dragstart**)
- `onDragOver` - Если мы находимся над зоной приема или каким-то другим объектом (событие **dragover**), нужно вызывать **event.preverntDefault()**
- `onDragLeave` - Срабатывает, если мы вышли за пределы другой карточки или зоны приема (событие **dragleave**)
- `onDragEnd` - Если мы отпустили элемент не зависимо от того, бросили ли куда-то (событие **dragend**)
- `onDrop` - Если мы отпустили карточку над зоной приема (событие **drop**)

```jsx
<div
	draggable={true}
	onDragLeave={(e) = > {dragLeaveHandler(e, card)}}
	onDragStart={(e) = > {dragStartHandler(e)}}
	onDragEnd={(e) = > {dragEndHandler(e)}}
	onDragOver={(e) = > {dragOverHandler(e)}}
	onDrop={(e) = > {dropHandler(e, card)}}
>
	...
</div>
```


### Drop-зона

drop-зона определяется как:

```tsx
<div
  onDragOver={(e) => e.preventDefault()}
  onDrop={(e) => {
    const data = e.dataTransfer.getData('id')
    console.log(data)
  }}
>
  Drop here
</div>
```

Drop-зона:

1. Слушает **drag-события**
2. Явно разрешает **drop**

### Типизация event

**event** всегда типизируется как `React.DragEvent`


### Фикс неполного определения drop-зоны

```tsx
.cardContainer {
  position: relative;
}

.cardContainer * {
  pointer-events: none;
}
```