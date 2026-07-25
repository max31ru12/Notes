
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
	refetchInterval: 5000, // перезапрашивать каждые 5 секунд
	initialData: [ // fallback для данных (когда нет данных из запроса)
		{ id: 1, title: "####"},
		{ id: 2, title: "####"},
	],
	placheholderData: [ // просто заглушка, не попадают в кэш
		{ id: 1, title: "####"},
		{ id: 2, title: "####"},
	]
})
```

- `getPosts` возвращает Promise
- `staleTime` - сколько данные считаются свежими (fresh), прежде чем стать stale (stale данные перезапрашиваются)
- `gcTime` - время, через которое данные вообще удаляются из кэша 
- `initiaData` - реальные данные, которые попадают в кэш и могут устаревать и т.д. Используется при серверном рендеринге



### Прямой доступ к кэшу

```tsx
const queryClient = useQueryClient()

const posts = queryClient.getQueryData(["posts"])
```


### Мутации

```tsx
const createUser = (username: string, age: number) => {
	await axios.post("/users", {username, age})
}


export function useCreateUserMutation() {

	const queryClient = useQueryClient()

	return useMutation({
		mutationFn: createUser,
		onSuccess: () => {
			queryClient.invalidateQueries({
				queryKey: ["users"]
			})
			alert("Runs on success")
		},
		onError: () => alert("Runs on error"),
		onSettled: () => alert("Runs always")
	})
}

useCreateUserMutation.mutate({ username, age })
// Так тоже можно
const result = await useCreateUserMutation.mutateAsync({ username, age })
```

### Добавлять данные в мутации напрямую (без перезапроса)

Надо вставлять данные из ответа в конец кэша:

```tsx
onSuccess: (data) => {
	queryClient.setQueryData(
		["users"], 
		(oldData: User[]) => [...oldData, data]
	)
}

```