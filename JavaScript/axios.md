# Axios with TS

```ts
const response = await axios.get<Post[]>(URL)

const result = response.data // тип переменной result - Post[]
```

`<Post[]>` - это ReturnType выполненного запроса (массив объектов Post)


# Использование `axios` с `useState` для рендера данных респонса

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

