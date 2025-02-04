## Axios with TS

```ts
const response = await axios.get<Post[]>(URL)

const result = response.data // тип переменной result - Post[]
```

`<Post[]>` - это ReturnType выполненного запроса (массив объектов Post)


## Использование `axios` с `useState` для рендера данных респонса

```ts
import React, {useState, useEffect} from "react";
import axios from "axios";

interface Address {
    "street": string
    "suite": string
    "city": string
    "zipcode": string
    "geo": {
        "lat": string
        "lng": string
    }
}

interface Company {
    "name": string
    "catchPhrase": string
    "bs": string
}

interface User {
    "id": number
    "name": string
    "username": string
    "email": string
    "address": Address
    "phone": string
    "website": string
    "company": Company
}


export default function Counter(){

    const [users, setUsers] = useState<User[]>([])
    const url = "https://jsonplaceholder.typicode.com/users"

    useEffect(() => {
        const response = axios.get<User[]>(url).then(res => setUsers(res.data))
    }, [])

    return (
        <ul>
            {users.map(user => <li key={user.id}>{user.username}</li>)}
        </ul>
    )
}
```


## Настройка axios для сохранения cookies в storage

```ts
import axios from "axios";  
  
const api = axios.create({  
    baseURL: "http://localhost:8000/api/v1",   
    withCredentials: true, // ОБЯЗАТЕЛЬНО для передачи cookies  
});  
  
export default api;
```


## interceptor

Позволяют перехватывать запрос перед тем, как они уйдут на сервер или с сервера придут в js-код.

### **Два типа интерцепторов в `axios`**

1. **`interceptors.request.use(...)`** — перехватывает **запросы**, перед тем как они уйдут на сервер.
2. **`interceptors.response.use(...)`** — перехватывает **ответы** сервера перед передачей их в код.

```js
const api = axios.create({
baseUrl: "https://api.example.com",
})

// Добавление interceptor для запроса
api.interceptors.request.use(
	(config) => {
		console.log(" Отправка запроса", config.url)
		return config
	},
	(error) => {
		console.error("❌ Ошибка запроса:", error)
		return Promise.reject(error)
	}
)

// 3️⃣ Добавляем interceptor для ответов 
api.interceptors.response.use( 
	(response) => { 
		console.log("✅ Успешный ответ:", response.data);
		return response; 
	}, 
	async (error) => { // Можно делать async 
		console.error("❌ Ошибка ответа:", error.response?.status);
		if (error.response?.status === 401) {
			// do smth
		}
		return Promise.reject(error);
	}
)
```

### Добавление Authorization

```js
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("accessToken");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

```