# Redux Toolkit

`npm install @reduxjs/toolkit react-redux`


## Summary

- Create a Redux store with configureStore
    - configureStore accepts a reducer function as a named argument
    - configureStore automatically sets up the store with good default settings
- Provide the Redux store to the React application components
    - Put a React-Redux <Provider> component around your <App />
    - Pass the Redux store as <Provider store={store}>
- Create a Redux "slice" reducer with createSlice
    - Call createSlice with a string name, an initial state, and named reducer functions
    - Reducer functions may "mutate" the state using Immer
    - Export the generated slice reducer and action creators
- Use the React-Redux useSelector/useDispatch hooks in React components
    - Read data from the store with the useSelector hook
    - Get the dispatch function with the useDispatch hook, and dispatch actions as needed




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



```js
import React from 'react';
import { useSelector, useDispatch} from 'react-redux';
import { decrement, increment } from "../redux-toolkit/slices/counterSlice";

export function Counter() {
    // counter - это reducer, подключенный по имени `counter` в store
    const count = useSelector((state) => state.counter.value);
    const dispatch = useDispatch();

    return (
        <div>
            <div>
                <button aria-label="Increment value" onClick={() => dispatch(increment())}>
                    Increment
                </button>
                <span>{count}</span>
                <button aria-label="Increment value" onClick={() => dispatch(decrement())}>
                    Decrement
                </button>
            </div>
        </div>
    )
}
```

