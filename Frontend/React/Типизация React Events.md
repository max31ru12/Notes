
## Краткая таблица

|JSX|Тип события|
|---|---|
|`<form onSubmit>`|`FormEvent<HTMLFormElement>`|
|`<input onChange>`|`ChangeEvent<HTMLInputElement>`|
|`<textarea onChange>`|`ChangeEvent<HTMLTextAreaElement>`|
|`<select onChange>`|`ChangeEvent<HTMLSelectElement>`|
|`<button onClick>`|`MouseEvent<HTMLButtonElement>`|
|`<div onClick>`|`MouseEvent<HTMLDivElement>`|
|`onKeyDown`|`KeyboardEvent<HTMLInputElement>`|
|`onFocus / onBlur`|`FocusEvent<HTMLInputElement>`|
|`onPaste`|`ClipboardEvent<HTMLElement>`|
|`onDragStart`|`DragEvent<HTMLElement>`|

# 📌 React + TypeScript — типизация событий (шпаргалка)

## 📝 Формы

```tsx
onSubmit    → FormEvent<HTMLFormElement> 
onReset     → FormEvent<HTMLFormElement>
```


---

## ✏️ Input / Select / Textarea

```tsx
<input onChange>        → ChangeEvent<HTMLInputElement> 
<textarea onChange>     → ChangeEvent<HTMLTextAreaElement> 
<select onChange>       → ChangeEvent<HTMLSelectElement> 
<input type="checkbox"> → ChangeEvent<HTMLInputElement> (checked) 
<input type="file">     → ChangeEvent<HTMLInputElement> (files)
```

---

## 🖱 Кнопки и мышь

```tsx
<button onClick>      → MouseEvent<HTMLButtonElement> 
<div onClick>         → MouseEvent<HTMLDivElement> 
onMouseEnter / Leave  → MouseEvent<HTMLElement>
```

---

## ⌨️ Клавиатура


```tsx
onKeyDown / onKeyUp   → KeyboardEvent<HTMLInputElement>
```


---

## 👆 Focus

```tsx
onFocus / onBlur      → FocusEvent<HTMLInputElement>`
```

---

## 🧲 Drag & Drop

```tsx
onDragStart           → DragEvent<HTMLElement> 
onDrop                → DragEvent<HTMLElement>
```

---

## 📦 Clipboard

```tsx
onPaste / onCopy      → ClipboardEvent<HTMLElement>
```