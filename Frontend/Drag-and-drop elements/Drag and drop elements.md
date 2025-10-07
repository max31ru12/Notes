
# Основы

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