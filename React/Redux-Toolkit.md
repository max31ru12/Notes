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
    // один объект - один редьюсер, методы - это actions (increment, decrement, ...) редьюсера
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


export const { increment, decrement, incrementByAmount } = counterSlice.actions

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

- `useSelector` - читать данные из **store**
- `useDispatch` - отправлять изменения в **store**

```js
import React from 'react';
import { useSelector, useDispatch} from 'react-redux';
import { decrement, descrement, increment } from "../redux-toolkit/slices/counterSlice";

export function Counter() {
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

