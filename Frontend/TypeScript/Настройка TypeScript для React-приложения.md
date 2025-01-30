
## Импорт без указания расширения

```json
{  
  "compilerOptions": {  
    "target": "es2016",  
    "module": "commonjs",  
    "esModuleInterop": true,  
    "forceConsistentCasingInFileNames": true,  
    "strict": true,  
    "skipLibCheck": true,  
    "moduleResolution": "node",  
    "baseUrl": "./",  
    "paths": {  
      "*": ["*", ".js", ".jsx", ".ts", ".tsx"]  
    },  
    "jsx": "react-jsx",  # Для обработки jsx-разметки
  }  
}
```

## Установка @types/react @types/react-dom

```shell
npm install --save-dev @types/react @types/react-dom
```


## Настройка `eslint`

##### 1. Установить eslint

```shell
npx eslint --init
```

##### 2. Настроить `eslint.config.mjs` 

```js
import globals from "globals";  
import pluginJs from "@eslint/js";  
import tseslint from "typescript-eslint";  
import pluginReact from "eslint-plugin-react";  
import * as react from "typescript-eslint";  
  
  
/** @type {import('eslint').Linter.Config[]} */  
export default [  
  {  
    files: ["**/*.{js,mjs,cjs,ts,jsx,tsx}"]  
  },  
  {  
    languageOptions: {  
      globals: globals.browser  
    }  
  },  
  react.configs.recommended,  
  react.configs["jsx-runtime"],  
  {  
    rules: {  
      "no-console": "warn",  
      "react/react-in-jsx-scope": "off" // React 17+ не требует import React  
    }  
  },  
  pluginJs.configs.recommended,  
  ...tseslint.configs.recommended,  
  pluginReact.configs.flat.recommended,  
];
```

##### 3. Установить хуки

```
npm install eslint-plugin-react-hooks --save-dev
```

##### 4. Установить хуки и настроить

```js
import globals from "globals";  
import pluginJs from "@eslint/js";  
import tseslint from "typescript-eslint";  
import pluginReact from "eslint-plugin-react";  
import * as react from "typescript-eslint";  
import reactHooks from "eslint-plugin-react-hooks";  
  
  
/** @type {import('eslint').Linter.Config[]} */  
export default [  
  {  
    files: ["**/*.{js,mjs,cjs,ts,jsx,tsx}"]  
  },  
  {  
    languageOptions: {  
      globals: globals.browser  
    }  
  },  
  react.configs.recommended,   // Подключаем стандартные правила React  
  react.configs["jsx-runtime"], // Разрешает использовать JSX без импорта React  
  reactHooks.configs.recommended, // Подключаем правила хуков  
  {  
    rules: {  
      "no-console": "warn",  
      "react/react-in-jsx-scope": "off", // Отключает требование `import React`  
      "react-hooks/rules-of-hooks": "error", // Ошибка при неправильном использовании хуков  
      "react-hooks/exhaustive-deps": "warn"  // Предупреждение при ошибках в deps useEffect  
    }  
  },  
  pluginJs.configs.recommended,  
  ...tseslint.configs.recommended,  
  pluginReact.configs.flat.recommended,  
];
```


## Настройка `prettier`

```shell
npm install --save-dev --save-exact prettier

echo {}> .prettierrc.json
```

### Файл `.prettierrc.json`:

```json
{  
  "trailingComma": "es5",  
  "tabWidth": 4,  
  "semi": false,  
  "singleQuote": true  
}
```

- **"trailingComma"** - отвечает за висящие, (или "последние") запятые. Можно разрешить Prettier ставить их там, где это возможно, или отключить эту функцию
- **"tabWidth"** - ширина отступа, в пробелах
- **"semi"** - отвечает за добавление точек с запятыми в конце инструкций. Можно добавлять, можно не добавлять
- **"singleQuote"** - отвечает за использование одинарных или двойные кавычек

```js
import globals from "globals";  
import pluginJs from "@eslint/js";  
import tseslint from "typescript-eslint";  
import pluginReact from "eslint-plugin-react";  
import * as react from "typescript-eslint";  
import reactHooks from "eslint-plugin-react-hooks";  
import js from "@eslint/js";  
import importPlugin from "eslint-plugin-import";  
import prettier from "eslint-plugin-prettier";  
import prettierConfig from "eslint-config-prettier";  
  
  
/** @type {import('eslint').Linter.Config[]} */  
export default [  
  {  
    files: ["**/*.{js,mjs,cjs,ts,jsx,tsx}"]  
  },  
  {  
    languageOptions: {  
      globals: globals.browser  
    }  
  },  
  js.configs.recommended,  
  react.configs.recommended,   // Подключаем стандартные правила React  
  react.configs["jsx-runtime"], // Разрешает использовать JSX без импорта React  
  reactHooks.configs.recommended, // Подключаем правила хуков  
  importPlugin.configs.recommended, // Подключает проверку импортов  
  prettierConfig, // Отключает конфликтующие правила ESLint  
  {  
    plugins: {  
      prettier // Включаем Prettier как плагин  
    },  
    rules: {  
      "no-console": "warn",  
      "react/react-in-jsx-scope": "off", // Отключает требование `import React`  
      "react-hooks/rules-of-hooks": "error", // Ошибка при неправильных хуках  
      "react-hooks/exhaustive-deps": "warn",  // Предупреждение при deps useEffect  
      "import/no-unresolved": "error",  // Ошибка, если импорт не найден  
      "import/order": ["warn", { "groups": ["builtin", "external", "internal"] }], // Упорядочивание импортов  
      "prettier/prettier": "warn" // Включаем проверку формата через Prettier  
    }  
  },  
  pluginJs.configs.recommended,  
  ...tseslint.configs.recommended,  
  pluginReact.configs.flat.recommended,  
];
```

## Правила Airbnb

```shell
npm install --save-dev eslint-config-airbnb
```

Разобраться, как добавлять в `eslint.config.mjs`

## Работа с css-модулями

```tsx
npm install --save-dev @types/css-modules
```