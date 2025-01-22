# Redux Toolkit

`npm install @reduxjs/toolkit react-redux`

## Create redux store

```js
import {configureStore} from "@reduxjs/toolkit";

const store = configureStore({
    reducer: {},
})
```

## Подключение store к проекту

`store` подключается с помощью Provider, который мы импортируем. Это пример подключения вместе с роутером (кажется, работает, но надо уточнить)

```js
import { store } from "./redux-toolkit/store.js";
import { Provider } from 'react-redux';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Provider store={store}>
    <React.StrictMode>
      <RouterProvider router={router} />
    </React.StrictMode>
  </Provider>
);
```

## Creating slices

`Slice` - это штука, которая содержит в себе логику **reducer'а** и **action creator'ов** (в общем, логику работы с состоянием)

### Создание слайса

**Redux** требует, чтобы состояние менялось через копирование состояния и изменения копий состояния. Redux делает это под капотом с помощью `reducer'ов`. 

```js
import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    value: 0;
}

export const counterSlice = createSlice({
    name: 'counter', // имя слайса
    initialState,
    // метод - один редьюсер (increment, decrement, ...)
    reducers: { // редьюсеры
        increment: (state) => {
            state.value += 1;
        },
        decrement: (state) => {
            state.value -= 1;
        },
        incrementByAmount: (state, action) => {
            state.value += action.payload;
        },
    },
})

// прокидываем редьюсеры как actions в counterSlice
export const { increment, decrement, incrementByAmount } = counterSlice.actions
// импортируем counterSlice как редьюсер
export default counterSlice.reducer
```


### Add Slice Reducers to the Store


```js
// .../store.js
import counterStore from '../features/counter/counterSlice';

export const store = configureStore({
  reducer: {
    counter: counterReducer,
  },
})
```


## Use Redux State and Actions in React Components

- `useSelector` - читать данные из **store** (принимает функцию, которая возвращает значение)
- `useDispatch` - отправлять изменения в **store**
- `state` - текущее состояние Redux


`(state) => state.counter.value` принимает объект состояния и возвращает значение

# Redux API

## createReducer

`builder` реализует `addCase`, `addMatcher`, `addDefaultCase`.

```js
import { createReducer, createAction } from '@reduxjs/toolkit'

const increment = createAction('counter/increment')
const decrement = createAction('counter/decrement')
const incrementByAmount = createAction('counter/incrementByAmount')

const initialState = { value: 0 }

const counterReducer = createReducer(initialState, (builder) => {
    builder
        .addCase(increment, (state, action) => {
            state.value++
        })
        .addCase(decrement, (state, action) => {
            state.value--
        })
        .addCase(incrementByAmount, (state, action) => {
            state.value += action.payload
        })
        .addDefaultCase((state, action) => {})
})
```

## Методы builder'а

### `addCase`

Добавляет кейс (аналог case в switch) для обработки одного `action type`

`addCase` - должен идти перед `addMatcher` и перед `addDefaultCase`.

### `addMatcher`

Позволяет сравнить входящие `actions` со своим собственным фильтром.

Должны быть определены строго после всех `addCase`



```js
function isActionWithNumberPayload(action) {
    return typeof action.payload === "number"
}

builder.addMatcher(isActionWithNumberPayload, (state, action) => {})
```


### `addDefaultCase`



# Thunks

Нужны (в основном) для асинхронного запроса к бэку

## Thunk creation


### Очень простой пример создания thunk'а

#### Создание `thunk`

```js
export const fetchPerson = createAsyncThunk("person/fetch", async (thunkAPI) => 
    const response = await fetch(
        "http://localhost:8000/person", {method: "GET"}
        );
    const data = response.json();
    return data;
);
```

В данном случае то, что вернет функция внутри параметров `createAsyncThunk` - это то, что будет использоваться в `Slice'ах` через `action.payload`;

#### Использование `thunk'а` 

Подключаются `thunks` в `slice'ы` через параметр `extraReducers`:

```js
export const PersonSlice(
    initialState,
    reducers: {
        addPerson: (state, action) => {
            state.persons.push(...);
        } 
    },
    extraReducers: (builder) => {
        // fetchPerson - это thunk
        builder.addCase(fetchPerson.fulfilled, (state, action) => {
            state.persons = action.payload;
        });
    },
)


export default PersonSlice.reducer;
```

Можно использовать это `thunk` как, как fetchPerson 


### Еще один пример

```js
import { createAsyncThunk, createSlice } from '@reduxjs/toolkit'
import { userAPI } from '/userAPI'

const fetchUserById = createAsyncThunk(
    'users/fetchByIdStatus',
    async (userId: number, thunkAPI) => {
        const response = await userAPI.fetchById(userId)
        return response.data
    },
)

initialState = {
    entities: [],
    loading: 'idle',
}

const usersSlice = createSlice({
    name: 'users',
    inititalState,
    reducers: {
        // reducer logic
    },
    extraReducers: (builder) => {
        builder.addCase(fetchUserById.fulfilled, (state, action) => {
            // Меняем state
            // payload - это то, что возвращает асинхронная функция (второй параметр)
            state.entites.push(action.payload)
        })
    },
})
```

- `thunkAPI` - обязательный параметр
- `userId` - дополнительный параметр


`createAsyncThunk` принимает 2 параметра:

1. `type`: строка, например `'users/requestStatus'`, которая генерирует дополнительные action-констатнты
    - `pending`: `'users/requestStatus/pending'`
    - `fulfilled`: `'users/requestStatus/fulfilled'`
    - `rejected`: `'users/requestStatus/rejected'`
2. `payloadCreator`: callback-функция, которая возвращает **promise**.
Этот **promise** хранит в себе результаты какой-то асинхронной логики
либо возвращает ошибку. `payloadCreator` принимает 2 аргумента:
    - `arg`:
    - `thunkAPI`: содержит в себе все функции, которые содержат в себе **thunks**


# RTK with Type Script


## Конфигурация `store` с TypeScript

```ts
import { useDispatch, useSelector } from 'react-redux'

export const store = configureStore({
  reducer: {
    posts: postsReducer,
    comments: commentsReducer,
    users: usersReducer,
  },
})

// Получаем ТИП СОСТОЯНИЯ STORE (какие есть методы, атрибуты и т.д.)
export type RootState = ReturnType<typeof store.getState>
// Получаем ТИП СОСТОЯНИЯ DISPATCH (какие есть методы, атрибу и т.д.)
export type AppDispatch = typeof store.dispatch

export const useAppDispatch = useDispatch.withTypes<AppDispatch>()  
export const useAppSelector = useSelector.withTypes<RootState>()
```

`useDispatch` и `useSelector` по умолчанию не знают, какие действия у нас есть, поэтому необходимо получить актуальные типы для `state` и `dispatch`,  а затем сказать `useDispatch` и `useSelector`, что им надо работать с этими типами.


## Action typing

```ts
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

const initialState = createSlice({
    name: '',
    initialState,
    reducers: {
        incrementByAmount: (state, action: PayloadAction<number>) => {
            state.person.name = action.name;
        }
    }
})
```

`PayloadAction<number>` - определяет, какого типа должен быть `action.payload`



## createAction typing

```ts
const increment = createAction<number>('increment')

function test(action: Action) {
  if (increment.match(action)) {
    // action.payload inferred correctly here
    action.payload
  }
}
```
