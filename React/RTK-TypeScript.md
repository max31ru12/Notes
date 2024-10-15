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

export const useAppDispatch = useDispatch.withTypwes<appDispatch>()
export const useAppSelector = useSelector.withtypes<RootState>()
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