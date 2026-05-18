
[Документация](https://tanstack.com/query/v3/docs/framework/react/quick-start)


## Подключение к проект

1. Проинициализировать `QueryClientProvider`
```tsx
const queryClient = new QueryClient()

// Добавить к остальным провайдерам (все приложение)
<QueryClientProvider>
	...
</QueryClientProvider>
```



### Запросы на получение данных

Используется хук - `useQuery`

```tsx
const posts = useQuery({
	queryKey: ["posts"],
	queryFn: () => Promise.resolve()
})

// Объект `posts` можно деструктуризировать 
const {data: posts} = useQuery(...)
```

- `queryFn` - должна возвращать какой-то Promise


### Пример с запросом к API

```tsx
function getPosts() {
	return axios.get("http://localhost/posts)").ther((res) => res.data)
}

// В компоненте
const { 
	data: posts, 
	isLoading, 
	isPending, 
	isFetching, 
	error,
	isError,
} = useQuery({
	queryKey: ["posts"],
	queryFn: getPosts, 
	staleTime: 5000,
	gcTime: 10000,
	retry: false, // можно установить флаг, чтобы не делался retry при ошибке
	retryDelay: 1000, // задержка retry
	enabled: isAuth, // выполнять или невыполнять по условию
})
```

- `getPosts` возвращает Promise
- `staleTime` - сколько данные считаются свежими (fresh), прежде чем стать stale (stale данные перезапрашиваются)
- `gcTime` - время, через которое данные вообще удаляются из кэша 