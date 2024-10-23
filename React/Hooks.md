# Hooks

## `useRef` hook

Это хук, который используется для вещей, которые не нужно рендерить (не возвращаются компонентом). 

> В отличие от `useState`, `useRef` не вызывает ре-рендер компонента!

### Использование `useRef` с `input`:

```ts
inputRef = useRef<HTMLInputElement | null>(null)


return (
    <input type="text" ref={inputRef}/>
)
```

React обрабатывает задание значения `inputRef.current` в **input**