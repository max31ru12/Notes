# Axios with TS

```ts
const response = await axios.get<Post[]>(URL)

const result = response.data // тип переменной result - Post[]
```

`<Post[]>` - это ReturnType выполненного запроса (массив объектов Post)



