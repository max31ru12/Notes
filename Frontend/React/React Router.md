
## Создание Router'а

```js
// index.js
import * as React from "react";
import * as ReactDOM from "react-dom/client";
import {
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";
import reportWebVitals from './reportWebVitals';

const router = createBrowserRouter([
    {
        path: "/",
        element: <Root /> // Root - это свой компонент
    }
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrinctMode>
        <RouterProvider router={router}>
    <React.StrictMode/>
);

reportWebVitals();
```


## Обработка исключений

Вынести в отдельный файл `./error-page.jsx`

```js
import { useRouteError } from "react-router-dom";
import { Link }


export default function ErrorPage() {
    const error = useRouteError();
    console.error(error);

    return (
        <div id="error-page">
            <h1>Oops!</h1>
            <p>Sorry, an unexpected error has occurred.</p>
            <p>
                <i>{error.statusText || error.message}</i>
            </p>
        </div>
    );
};

```


## Render another links

1. Можно просто добавить второй маршрут в `router`:

```js
const router = createBrowserRouter([
  {
      path: "/",
      element: <Root />,
      errorElement: <ErrorPage />,
  },
  {
    path: "/contacts/:contactId",
    element: <Contacts />,
  }
]);

```


2. Добавить дочерний элемент в первый маршрут

    `<Outlet />` компонент - это компонент, в котором будут рендериться дочерние компоненты, т.е. `children`

    - добавить в `root.jsx` компонент `<Outlet />`

        ```js
        import { Outlet } from "react-router-dom";

        export default function Root() {
        return (
            <>
            {/* all the other elements */}
            <div id="detail">
                <Outlet />
            </div>
            </>
        );
        }
        ```
    
    - добавить дочерний элемент в уже существующий роутер (с сохранением контекста)!!!

        ```js
        const router = createBrowserRouter([
        {
            path: "/",
            element: <Root />,
            errorElement: <ErrorPage />,
            children: [
                {
                path: "/contacts/:contactId",
                element: <Contacts />,
                },
            ]
        },
        ]);
        ```

### Client Side Routing: `Link` 

`Link` позволяет обновлять **URL** так, чтобы браузер не запрашивал новый документ, а ре-рендерил поверх старого документа

```js
<Link to="/">Home<Link/>
```


### URL params

#### Как это выглядит в роутере:

```js
...
{
    path: "contacts/:contactId",
    element: < />
}
```

#### Использование параметров в компоненте

`useParams` вернет все параметры, доступные для этой страницы

```js
import { useParams } from "react-router-dom";


export default function ContactPage() {
    const params = useParams();
}
```

**TypeScript** типизация для `useParams`:

```js
const params = useParams<{ profileId: string }>();
```