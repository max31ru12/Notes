
[Руководство по использованию Vite в React](https://www.dev-notes.ru/articles/react/guide-to-using-vite-with-react/#introduction)

- `tsconfig.app.json` (основной для React-приложения)
- `tsconfig.node.json` (для Vite-конфигов, скриптов и т.д.)

## Линтеры

### eslint

#### Установка с eslint.config.js

Команду установки можно найти в доке

- `.eslintrc.json` - старый файл
- `eslint.config.js` - новый файл конфигурации
- `eslint.config.mjs` - явное указание, что файл является модулем

Добавляем эту штуку в `eslint.confug.js`, чтобы не импортировать react. Удаляем вторую штуку, чтобы не было ошибок

```tsx
rules: {  
	"react/react-in-jsx-scope": "off"  // Добавить
	'no-unused-vars': "warn",  // предупреждение на unused vars
	'semi': ['error', 'never'], // не разрешать semicolon
}

pluginReact.configs.flat.recommended // Удалить 
```

### prettier

```shell
npx prettier . --write  # запустить prettier 
```

#### Установка

```shell
npm install --save-dev prettier eslint-config-prettier
```

#### Файл конфигурации `.prettierrc` (создать вручную)

```json
{
  "singleQuote": true,
  "semi": false,
  "trailingComma": "all", // закрывающая запятая
  "printWidth": 100,
  "bracketSpacing": true, // обязательные пробелы в импорте import { smth } from ...
  tabWidth: 4, // ширина отступов
  arrowParents, // добавление круглых скоробок в стрелочные функции (arg1) => {}
  endOfLine: "lf" // конец строки, так надо
}
```

#### Игнорирование `.prettierignore`

```
node_modules
build
dist
```

#### Интеграция с eslint
В `eslint.config.js` добавить `eslint-config-prettier` последним в `extends`, чтобы отключить правила ESLint, конфликтующие с Prettier:


```js
import prettier from "eslint-config-prettier"

export default defineConfig([
  {
    files: ["**/*.{js,mjs,cjs,ts,jsx,tsx}"],
    plugins: { js },
    extends: ["js/recommended", prettier],
    rules: {
      "react/react-in-jsx-scope": "off"
    }
  },
  { files: ["**/*.{js,mjs,cjs,ts,jsx,tsx}"], languageOptions: { globals: globals.browser } },
  tseslint.configs.recommended,
])
```


### pre-commit hook

**husky** - библиотека для управления гит-хуками (идет вместе с pre-commit)

#### Установка `pre-commit` и необходимых хуков:

```shell
npm install --save-dev husky

npx husky init # Создает pre-commit файл в папке .husky
```


#### Добавить в scripts в package.json

```json
"scripts": {  
  "dev": "vite",  
  "build": "tsc -b && vite build",  
  "lint": "eslint . ./src --ext .ts,.tsx --fix",  // раширения обязательно, так как файлы .ts и .tsx не проверяются автоматически
  "preview": "vite preview",  
  "format": "prettier ./src --write",  
  "prepare": "husky"  
},
// list-staged проводит проверки только для изменнных файлов
"lint-staged": {  
  "*.{ts,tsx}": [  
    "eslint --fix",  
    "prettier --write"  
  ]  
},
```

Команды из `scripts` можно выполнять с помощью `npm run <script name>` в `pre-commit` husky

#### Конфигурация husky в `pre-commit`

##### Провести проверки для всех файлов

```
npm run lint
npm run format
```

##### Провести проверки только для измененных файлов

```
npx lint-staged
```


